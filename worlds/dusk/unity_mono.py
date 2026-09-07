from typing import Dict, List, Optional, Tuple

import ctypes
import ctypes.wintypes
import struct

import pymem.process
import pymem.ressources.structure

from pymem import Pymem


ctypes.windll.kernel32.CreateRemoteThread.restype = ctypes.wintypes.HANDLE

ctypes.windll.kernel32.CreateRemoteThread.argtypes = [
    ctypes.wintypes.HANDLE,
    ctypes.c_void_p,
    ctypes.c_size_t,
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.wintypes.DWORD,
    ctypes.c_void_p,
]


def get_module_base_address(process: Pymem, module_name: str) -> int:
    module: pymem.ressources.structure.MODULEINFO = pymem.process.module_from_name(process.process_handle, module_name)

    if module is None:
        raise RuntimeError(f"Module {module_name} not found in target process")

    return module.lpBaseOfDll


def read_mono_object_array(process: Pymem, array_address: int) -> List[int]:
    if not array_address:
        return list()

    length: int = process.read_longlong(array_address + 0x18)

    if length <= 0:
        return list()

    if length > 4096:
        raise RuntimeError(f"MonoArray length {length} exceeds sanity ceiling of 4096; array_address is likely wrong")

    raw_bytes: bytes = process.read_bytes(array_address + 0x20, length * 8)

    return list(struct.unpack(f"<{length}Q", raw_bytes))


def read_mono_string(process: Pymem, string_address: int, max_characters: int = 256) -> Optional[str]:
    if not string_address:
        return None

    length: int = process.read_int(string_address + 0x10)

    if length <= 0 or length > max_characters:
        return None

    raw_bytes: bytes = process.read_bytes(string_address + 0x14, length * 2)

    return raw_bytes.decode("utf-16-le", errors="replace")


def write_mono_bool_array_element(process: Pymem, array_address: int, index: int, value: bool) -> None:
    process.write_bool(array_address + 0x20 + index, value)


def write_mono_float_array_element(process: Pymem, array_address: int, index: int, value: float) -> None:
    process.write_float(array_address + 0x20 + index * 4, value)


def build_call_stub(function_address: int, args: List[int], result_address: int) -> bytes:
    padded_args: List[int] = (list(args) + [0, 0, 0, 0])[:4]

    code: bytes = bytes()

    code += b"\x48\x83\xEC\x28"  # sub rsp, 0x28
    code += b"\x48\xB9" + struct.pack("<Q", padded_args[0])  # mov rcx, padded_args[0]
    code += b"\x48\xBA" + struct.pack("<Q", padded_args[1])  # mov rdx, padded_args[1]
    code += b"\x49\xB8" + struct.pack("<Q", padded_args[2])  # mov r8, padded_args[2]
    code += b"\x49\xB9" + struct.pack("<Q", padded_args[3])  # mov r9, padded_args[3]
    code += b"\x48\xB8" + struct.pack("<Q", function_address)  # mov rax, function_address
    code += b"\xFF\xD0"  # call rax
    code += b"\x49\xBA" + struct.pack("<Q", result_address)  # mov r10, result_address
    code += b"\x49\x89\x02"  # mov [r10], rax
    code += b"\x48\x83\xC4\x28"  # add rsp, 0x28
    code += b"\x31\xC0"  # xor eax, eax
    code += b"\xC3"  # ret

    return code


def build_attached_call_stub(
    attach_address: int,
    domain_address: int,
    function_address: int,
    args: List[int],
    detach_address: int,
    result_address: int,
) -> bytes:
    padded_args: List[int] = (list(args) + [0, 0, 0, 0])[:4]

    code: bytes = bytes()

    code += b"\x48\x83\xEC\x28"  # sub rsp, 0x28

    # mono_thread_attach(domain) -> rbx
    code += b"\x48\xB9" + struct.pack("<Q", domain_address)  # mov rcx, domain_address
    code += b"\x48\xB8" + struct.pack("<Q", attach_address)  # mov rax, attach_address
    code += b"\xFF\xD0"  # call rax
    code += b"\x48\x89\xC3"  # mov rbx, rax

    code += b"\x48\xB9" + struct.pack("<Q", padded_args[0])  # mov rcx, padded_args[0]
    code += b"\x48\xBA" + struct.pack("<Q", padded_args[1])  # mov rdx, padded_args[1]
    code += b"\x49\xB8" + struct.pack("<Q", padded_args[2])  # mov r8,  padded_args[2]
    code += b"\x49\xB9" + struct.pack("<Q", padded_args[3])  # mov r9,  padded_args[3]
    code += b"\x48\xB8" + struct.pack("<Q", function_address)  # mov rax, function_address
    code += b"\xFF\xD0"  # call rax
    code += b"\x49\xBA" + struct.pack("<Q", result_address)  # mov r10, result_address
    code += b"\x49\x89\x02"  # mov [r10], rax

    # mono_thread_detach(rbx)
    code += b"\x48\x89\xD9"  # mov rcx, rbx
    code += b"\x48\xB8" + struct.pack("<Q", detach_address)  # mov rax, detach_address
    code += b"\xFF\xD0"  # call rax

    code += b"\x48\x83\xC4\x28"  # add rsp, 0x28
    code += b"\x31\xC0"  # xor eax, eax
    code += b"\xC3"  # ret

    return code


class MonoRemoteCaller:
    process: Pymem

    buffer_address: int

    result_address: int
    exception_address: int

    cursor_address: int

    attach_address: Optional[int]
    detach_address: Optional[int]
    domain_address: Optional[int]

    def __init__(self, process: Pymem) -> None:
        self.process = process

        self.buffer_address = process.allocate(0x2000)

        self.result_address = self.buffer_address + 0x800
        self.exception_address = self.buffer_address + 0x808

        self.cursor_address = self.buffer_address + 0x810

        self.attach_address = None
        self.detach_address = None
        self.domain_address = None

    @property
    def is_attachable(self) -> bool:
        return self.attach_address is not None

    def enable_thread_attach(self, attach_address: int, detach_address: int, domain_address: int) -> None:
        self.attach_address = attach_address
        self.detach_address = detach_address
        self.domain_address = domain_address

    def write_int32_to_buffer(self, value: int) -> int:
        address: int = self.cursor_address

        self.process.write_int(address, value)
        self.cursor_address += 4 + 8

        return address

    def write_qword_to_buffer(self, value: int) -> int:
        address: int = self.cursor_address

        self.process.write_longlong(address, value)
        self.cursor_address += 8 + 8

        return address

    def write_cstring_to_buffer(self, text: str) -> int:
        text_bytes: bytes = text.encode("ascii") + b"\x00"
        address: int = self.cursor_address

        self.process.write_bytes(address, text_bytes, len(text_bytes))
        self.cursor_address += len(text_bytes) + 8

        return address

    def write_vector2_to_buffer(self, x: float, y: float) -> int:
        vector2_bytes: bytes = struct.pack("<2f", x, y)
        address: int = self.cursor_address

        self.process.write_bytes(address, vector2_bytes, len(vector2_bytes))
        self.cursor_address += len(vector2_bytes) + 8

        return address

    def write_pointer_array_to_buffer(self, addresses: List[int]) -> int:
        array_bytes: bytes = b"".join(struct.pack("<Q", address) for address in addresses)
        address: int = self.cursor_address

        self.process.write_bytes(address, array_bytes, len(array_bytes))
        self.cursor_address += len(array_bytes) + 8

        return address

    def call(self, function_address: int, args: Optional[List[int]] = None) -> int:
        args = args or list()
        code: bytes

        if self.is_attachable:
            code = build_attached_call_stub(
                self.attach_address,
                self.domain_address,
                function_address,
                args,
                self.detach_address,
                self.result_address,
            )
        else:
            code = build_call_stub(function_address, args, self.result_address)

        self.process.write_bytes(self.buffer_address, code, len(code))

        thread: Optional[int] = ctypes.windll.kernel32.CreateRemoteThread(
            self.process.process_handle,
            None,
            0,
            self.buffer_address,
            None,
            0,
            None
        )

        if not thread:
            raise RuntimeError("CreateRemoteThread failed")

        wait_result: int = ctypes.windll.kernel32.WaitForSingleObject(thread, 1000)
        ctypes.windll.kernel32.CloseHandle(thread)

        if wait_result == 0x102:
            raise RuntimeError("WaitForSingleObject timeout")
        elif wait_result != 0x0:
            raise RuntimeError(f"WaitForSingleObject returned unexpected value {hex(wait_result)}")

        result: int = self.process.read_longlong(self.result_address)

        self.cursor_address = self.buffer_address + 0x810

        return result


# Exported Function RVAs of interest from mono-2.0-bdwgc.dll. Identified with PE-bear.
MONO_EXPORTED_FUNCTION_RVAS = {
    "mono_assembly_get_image": 0x2FBA0,
    "mono_class_from_name": 0x383E0,
    "mono_class_get_method_from_name": 0x3A210,
    "mono_class_get_type": 0x3A960,
    "mono_class_vtable": 0xB5380,
    "mono_domain_assembly_open": 0x2BA60,
    "mono_get_root_domain": 0x2CC40,
    "mono_runtime_invoke": 0xBAAF0,
    "mono_string_new": 0xBC080,
    "mono_thread_attach": 0xD1390,
    "mono_thread_detach": 0xD1D40,
    "mono_type_get_object": 0xF8210,
}


class MonoResolver:
    caller: MonoRemoteCaller
    function_addresses: Dict[str, int]
    root_domain: Optional[int]

    _class_cache: Dict[Tuple[int, str, str], int]
    _method_cache: Dict[Tuple[int, str, int], int]
    _system_type_cache: Dict[int, int]
    _image_cache: Dict[str, int]

    def __init__(self, process: Pymem, dll_name: str = "mono-2.0-bdwgc.dll") -> None:
        self.caller = MonoRemoteCaller(process)

        self.function_addresses = {
            name: get_module_base_address(process, dll_name) + rva for name, rva in MONO_EXPORTED_FUNCTION_RVAS.items()
        }

        self.root_domain = None

        self._class_cache = dict()  # (image_address, namespace, class_name) -> class_address
        self._method_cache = dict()  # (class_address, method_name, arg_count) -> method_address
        self._system_type_cache = dict()  # class_address -> System.Type reflection object address
        self._image_cache = dict()  # assembly_name -> image_address

    def get_class(self, image_address: int, namespace: str, class_name: str, verbose: bool = False) -> int:
        cache_key: Tuple[int, str, str] = (image_address, namespace, class_name)

        if cache_key in self._class_cache:
            return self._class_cache[cache_key]

        namespace_address: int = self.caller.write_cstring_to_buffer(namespace)
        class_name_address: int = self.caller.write_cstring_to_buffer(class_name)

        class_address: int = self.caller.call(
            self.function_addresses["mono_class_from_name"],
            [image_address, namespace_address, class_name_address],
        )

        if class_address in (0, None):
            raise RuntimeError(f"mono_class_from_name returned NULL for '{namespace}.{class_name}'")

        if verbose:
            print(f"  class = 0x{class_address:X}  ({namespace}.{class_name})")

        self._class_cache[cache_key] = class_address

        return class_address

    def get_method(self, class_address: int, name: str, arg_count: int, verbose: bool = False) -> int:
        cache_key: Tuple[int, str, int] = (class_address, name, arg_count)

        if cache_key in self._method_cache:
            return self._method_cache[cache_key]

        name_address: int = self.caller.write_cstring_to_buffer(name)

        method_address: int = self.caller.call(
            self.function_addresses["mono_class_get_method_from_name"],
            [class_address, name_address, arg_count],
        )

        if method_address in (0, None):
            raise RuntimeError(f"Method {name!r} (argc={arg_count}) not found in class")

        if verbose:
            print(f"  method = 0x{method_address:X}  ({name}/{arg_count})")

        self._method_cache[cache_key] = method_address

        return method_address

    def get_system_type(self, class_address: int, verbose: bool = False) -> int:
        if class_address in self._system_type_cache:
            return self._system_type_cache[class_address]

        domain_address: int = self._ensure_domain(verbose)

        mono_type_address: int = self.caller.call(self.function_addresses["mono_class_get_type"], [class_address])

        if mono_type_address in (0, None):
            raise RuntimeError("mono_class_get_type returned NULL")

        type_object_address: int = self.caller.call(
            self.function_addresses["mono_type_get_object"], [domain_address, mono_type_address]
        )

        if type_object_address in (0, None):
            raise RuntimeError("mono_type_get_object returned NULL")

        if verbose:
            print(f"  system_type = 0x{type_object_address:X}")

        self._system_type_cache[class_address] = type_object_address

        return type_object_address

    def get_image(self, assembly_name: str, verbose: bool = False) -> int:
        if assembly_name in self._image_cache:
            return self._image_cache[assembly_name]

        domain_address: int = self._ensure_domain(verbose)

        assembly_name_address: int = self.caller.write_cstring_to_buffer(assembly_name)

        assembly_address: int = self.caller.call(
            self.function_addresses["mono_domain_assembly_open"], [domain_address, assembly_name_address]
        )

        if assembly_address in (0, None):
            raise RuntimeError(f"mono_domain_assembly_open returned NULL for {assembly_name!r}")

        if verbose:
            print(f"  assembly = 0x{assembly_address:X}  ({assembly_name})")

        image_address: int = self.caller.call(self.function_addresses["mono_assembly_get_image"], [assembly_address])

        if image_address in (0, None):
            raise RuntimeError("mono_assembly_get_image returned NULL")

        if verbose:
            print(f"  image = 0x{image_address:X}")

        self._image_cache[assembly_name] = image_address

        return image_address

    def read_mono_string(self, string_address: int, max_characters: int = 256) -> Optional[str]:
        return read_mono_string(self.caller.process, string_address, max_characters)

    @staticmethod
    def unbox_address(boxed_pointer: int) -> int:
        return boxed_pointer + 0x10

    def unbox_int32(self, boxed_pointer: int) -> int:
        return self.caller.process.read_int(self.unbox_address(boxed_pointer))

    def unbox_bool(self, boxed_pointer: int) -> bool:
        raw_byte: int = self.caller.process.read_bytes(self.unbox_address(boxed_pointer), 1)[0]
        return bool(raw_byte)

    def get_vtable_for_class(self, class_address: int, verbose: bool = False) -> int:
        domain_address: int = self._ensure_domain(verbose)

        vtable_address: int = self.caller.call(self.function_addresses["mono_class_vtable"], [domain_address, class_address])

        if vtable_address in (0, None):
            raise RuntimeError("mono_class_vtable returned NULL")

        if verbose:
            print(f"  vtable = 0x{vtable_address:X}")

        return vtable_address

    def get_vtable(self, assembly_name: str, namespace: str, class_name: str, verbose: bool = False) -> int:
        image_address: int = self.get_image(assembly_name, verbose)
        class_address: int = self.get_class(image_address, namespace, class_name, verbose)

        return self.get_vtable_for_class(class_address, verbose)

    def invoke(self, method_address: int, object_address: int = 0, params_address: int = 0) -> int:
        self.caller.process.write_longlong(self.caller.exception_address, 0)

        result_address: int = self.caller.call(
            self.function_addresses["mono_runtime_invoke"],
            [method_address, object_address, params_address, self.caller.exception_address],
        )

        exception_pointer: int = self.caller.process.read_longlong(self.caller.exception_address)

        if exception_pointer != 0:
            raise RuntimeError(f"Managed method threw (MonoException* = 0x{exception_pointer:X})")

        return result_address

    # Generic Unity Object Lookup / Creation
    def find_objects_of_type(self, class_address: int, verbose: bool = False) -> List[int]:
        core_image_address: int = self.get_image("UnityEngine.CoreModule", verbose)

        object_class_address: int = self.get_class(core_image_address, "UnityEngine", "Object", verbose)

        find_objects_method_address: int = self.get_method(
            object_class_address, "FindObjectsOfType", 1, verbose
        )

        type_object_address: int = self.get_system_type(class_address, verbose)
        params_address: int = self.caller.write_pointer_array_to_buffer([type_object_address])

        result_array_address: int = self.invoke(
            find_objects_method_address, object_address=0, params_address=params_address
        )

        return read_mono_object_array(self.caller.process, result_array_address)

    def new_string(self, text: str, verbose: bool = False) -> int:
        domain_address: int = self._ensure_domain(verbose)
        text_address: int = self.caller.write_cstring_to_buffer(text)

        return self.caller.call(self.function_addresses["mono_string_new"], [domain_address, text_address])

    # GameObject Lookup / Creation
    def find_game_object(self, name: str, verbose: bool = False) -> int:
        core_image_address: int = self.get_image("UnityEngine.CoreModule", verbose)
        game_object_class_address: int = self.get_class(core_image_address, "UnityEngine", "GameObject", verbose)
        find_method_address: int = self.get_method(game_object_class_address, "Find", 1, verbose)

        name_address: int = self.new_string(name, verbose)
        params_address: int = self.caller.write_pointer_array_to_buffer([name_address])

        return self.invoke(find_method_address, object_address=0, params_address=params_address)

    def instantiate(self, object_address: int, parent_transform_address: int = 0, verbose: bool = False) -> int:
        core_image_address: int = self.get_image("UnityEngine.CoreModule", verbose)
        unity_object_class_address: int = self.get_class(core_image_address, "UnityEngine", "Object", verbose)

        if parent_transform_address:
            instantiate_method_address: int = self.get_method(unity_object_class_address, "Instantiate", 2, verbose)

            params_address: int = self.caller.write_pointer_array_to_buffer(
                [object_address, parent_transform_address]
            )
        else:
            instantiate_method_address: int = self.get_method(unity_object_class_address, "Instantiate", 1, verbose)
            params_address: int = self.caller.write_pointer_array_to_buffer([object_address])

        return self.invoke(instantiate_method_address, object_address=0, params_address=params_address)

    # Component / Hierarchy Navigation
    def get_component(self, game_object_address: int, component_class_address: int, verbose: bool = False) -> int:
        core_image_address: int = self.get_image("UnityEngine.CoreModule", verbose)
        game_object_class_address: int = self.get_class(core_image_address, "UnityEngine", "GameObject", verbose)
        get_component_method_address: int = self.get_method(game_object_class_address, "GetComponent", 1, verbose)

        type_object_address: int = self.get_system_type(component_class_address, verbose)
        params_address: int = self.caller.write_pointer_array_to_buffer([type_object_address])

        return self.invoke(
            get_component_method_address, object_address=game_object_address, params_address=params_address
        )

    def get_components_in_children(self, root_transform_address: int, component_class_address: int, include_inactive: bool = True, verbose: bool = False) -> List[int]:
        core_image_address: int = self.get_image("UnityEngine.CoreModule", verbose)
        component_class_general_address: int = self.get_class(core_image_address, "UnityEngine", "Component", verbose)
        get_components_method_address: int = self.get_method(component_class_general_address, "GetComponentsInChildren", 2, verbose)

        type_object_address: int = self.get_system_type(component_class_address, verbose)
        include_inactive_address: int = self.caller.write_int32_to_buffer(1 if include_inactive else 0)
        params_address: int = self.caller.write_pointer_array_to_buffer([type_object_address, include_inactive_address])

        result_array_address: int = self.invoke(
            get_components_method_address, object_address=root_transform_address, params_address=params_address
        )

        return read_mono_object_array(self.caller.process, result_array_address)

    def get_transform(self, game_object_address: int, verbose: bool = False) -> int:
        core_image_address: int = self.get_image("UnityEngine.CoreModule", verbose)
        game_object_class_address: int = self.get_class(core_image_address, "UnityEngine", "GameObject", verbose)
        get_transform_method_address: int = self.get_method(game_object_class_address, "get_transform", 0, verbose)

        return self.invoke(get_transform_method_address, object_address=game_object_address)

    def get_child_count(self, transform_address: int, verbose: bool = False) -> int:
        core_image_address: int = self.get_image("UnityEngine.CoreModule", verbose)
        transform_class_address: int = self.get_class(core_image_address, "UnityEngine", "Transform", verbose)

        get_child_count_method_address: int = self.get_method(
            transform_class_address, "get_childCount", 0, verbose
        )

        boxed_count_address: int = self.invoke(get_child_count_method_address, object_address=transform_address)

        return self.unbox_int32(boxed_count_address)

    def get_child(self, transform_address: int, index: int, verbose: bool = False) -> int:
        core_image_address: int = self.get_image("UnityEngine.CoreModule", verbose)
        transform_class_address: int = self.get_class(core_image_address, "UnityEngine", "Transform", verbose)
        get_child_method_address: int = self.get_method(transform_class_address, "GetChild", 1, verbose)

        index_address: int = self.caller.write_int32_to_buffer(index)
        params_address: int = self.caller.write_pointer_array_to_buffer([index_address])

        return self.invoke(get_child_method_address, object_address=transform_address, params_address=params_address)

    def get_game_object(self, component_address: int, verbose: bool = False) -> int:
        core_image_address: int = self.get_image("UnityEngine.CoreModule", verbose)
        component_class_address: int = self.get_class(core_image_address, "UnityEngine", "Component", verbose)

        get_game_object_method_address: int = self.get_method(
            component_class_address, "get_gameObject", 0, verbose
        )

        return self.invoke(get_game_object_method_address, object_address=component_address)

    # Hierarchy Search
    def find_child_by_name(self, root_transform_address: int, name: str, verbose: bool = False) -> int:
        core_image_address: int = self.get_image("UnityEngine.CoreModule", verbose)
        transform_class_address: int = self.get_class(core_image_address, "UnityEngine", "Transform", verbose)

        transform_addresses: List[int] = self.get_components_in_children(
            root_transform_address, transform_class_address, include_inactive=True, verbose=verbose
        )

        transform_address: int
        for transform_address in transform_addresses:
            game_object_address: int = self.get_game_object(transform_address, verbose)

            if self.get_object_name(game_object_address, verbose) == name:
                return game_object_address

        return 0

    # UnityEngine.Object Properties
    def get_object_name(self, unity_object_address: int, verbose: bool = False) -> Optional[str]:
        core_image_address: int = self.get_image("UnityEngine.CoreModule", verbose)
        unity_object_class_address: int = self.get_class(core_image_address, "UnityEngine", "Object", verbose)
        get_name_method_address: int = self.get_method(unity_object_class_address, "get_name", 0, verbose)

        name_address: int = self.invoke(get_name_method_address, object_address=unity_object_address)

        return self.read_mono_string(name_address)

    def get_object_tag(self, game_object_address: int, verbose: bool = False) -> Optional[str]:
        core_image_address: int = self.get_image("UnityEngine.CoreModule", verbose)
        game_object_class_address: int = self.get_class(core_image_address, "UnityEngine", "GameObject", verbose)
        get_tag_method_address: int = self.get_method(game_object_class_address, "get_tag", 0, verbose)

        tag_address: int = self.invoke(get_tag_method_address, object_address=game_object_address)

        return self.read_mono_string(tag_address)

    def set_active(self, game_object_address: int, active: bool, verbose: bool = False) -> None:
        core_image_address: int = self.get_image("UnityEngine.CoreModule", verbose)
        game_object_class_address: int = self.get_class(core_image_address, "UnityEngine", "GameObject", verbose)
        set_active_method_address: int = self.get_method(game_object_class_address, "SetActive", 1, verbose)

        active_address: int = self.caller.write_int32_to_buffer(1 if active else 0)
        params_address: int = self.caller.write_pointer_array_to_buffer([active_address])

        self.invoke(set_active_method_address, object_address=game_object_address, params_address=params_address)

    def set_name(self, unity_object_address: int, name: str, verbose: bool = False) -> None:
        core_image_address: int = self.get_image("UnityEngine.CoreModule", verbose)
        unity_object_class_address: int = self.get_class(core_image_address, "UnityEngine", "Object", verbose)
        set_name_method_address: int = self.get_method(unity_object_class_address, "set_name", 1, verbose)

        new_name_address: int = self.new_string(name, verbose)
        params_address: int = self.caller.write_pointer_array_to_buffer([new_name_address])

        self.invoke(set_name_method_address, object_address=unity_object_address, params_address=params_address)

    # UnityEngine.UI.Text Properties
    def set_text(self, text_component_address: int, text: str, verbose: bool = False) -> None:
        ui_image_address: int = self.get_image("UnityEngine.UI", verbose)
        ui_text_class_address: int = self.get_class(ui_image_address, "UnityEngine.UI", "Text", verbose)
        set_text_method_address: int = self.get_method(ui_text_class_address, "set_text", 1, verbose)

        new_text_address: int = self.new_string(text, verbose)
        params_address: int = self.caller.write_pointer_array_to_buffer([new_text_address])

        self.invoke(set_text_method_address, object_address=text_component_address, params_address=params_address)

    def set_font_size(self, text_component_address: int, size: int, verbose: bool = False) -> None:
        ui_image_address: int = self.get_image("UnityEngine.UI", verbose)
        ui_text_class_address: int = self.get_class(ui_image_address, "UnityEngine.UI", "Text", verbose)
        set_font_size_method_address: int = self.get_method(ui_text_class_address, "set_fontSize", 1, verbose)

        size_address: int = self.caller.write_int32_to_buffer(size)
        params_address: int = self.caller.write_pointer_array_to_buffer([size_address])

        self.invoke(set_font_size_method_address, object_address=text_component_address, params_address=params_address)

    # Behaviour Properties
    def set_enabled(self, behaviour_address: int, enabled: bool, verbose: bool = False) -> None:
        core_image_address: int = self.get_image("UnityEngine.CoreModule", verbose)
        behaviour_class_address: int = self.get_class(core_image_address, "UnityEngine", "Behaviour", verbose)
        set_enabled_method_address: int = self.get_method(behaviour_class_address, "set_enabled", 1, verbose)

        enabled_address: int = self.caller.write_int32_to_buffer(1 if enabled else 0)
        params_address: int = self.caller.write_pointer_array_to_buffer([enabled_address])

        self.invoke(set_enabled_method_address, object_address=behaviour_address, params_address=params_address)

    # Transform Properties
    def get_position(self, transform_address: int, verbose: bool = False) -> Tuple[float, float, float]:
        core_image_address: int = self.get_image("UnityEngine.CoreModule", verbose)
        transform_class_address: int = self.get_class(core_image_address, "UnityEngine", "Transform", verbose)
        get_position_method_address: int = self.get_method(transform_class_address, "get_position", 0, verbose)

        boxed_address: int = self.invoke(get_position_method_address, object_address=transform_address)
        data_address: int = self.unbox_address(boxed_address)

        return struct.unpack("<3f", self.caller.process.read_bytes(data_address, 12))

    # RectTransform Properties
    def get_anchored_position(self, rect_transform_address: int, verbose: bool = False) -> Tuple[float, float]:
        core_image_address: int = self.get_image("UnityEngine.CoreModule", verbose)
        rect_transform_class_address: int = self.get_class(core_image_address, "UnityEngine", "RectTransform", verbose)
        get_method_address: int = self.get_method(rect_transform_class_address, "get_anchoredPosition", 0, verbose)

        boxed_address: int = self.invoke(get_method_address, object_address=rect_transform_address)
        data_address: int = self.unbox_address(boxed_address)

        return struct.unpack("<2f", self.caller.process.read_bytes(data_address, 8))

    def set_anchored_position(self, rect_transform_address: int, x: float, y: float, verbose: bool = False) -> None:
        core_image_address: int = self.get_image("UnityEngine.CoreModule", verbose)
        rect_transform_class_address: int = self.get_class(core_image_address, "UnityEngine", "RectTransform", verbose)
        set_method_address: int = self.get_method(rect_transform_class_address, "set_anchoredPosition", 1, verbose)

        position_address: int = self.caller.write_vector2_to_buffer(x, y)
        params_address: int = self.caller.write_pointer_array_to_buffer([position_address])

        self.invoke(set_method_address, object_address=rect_transform_address, params_address=params_address)

    def _ensure_domain(self, verbose: bool = False) -> int:
        if self.root_domain is not None:
            return self.root_domain

        root_domain_address: int = self.caller.call(self.function_addresses["mono_get_root_domain"])

        if root_domain_address in (0, None):
            raise RuntimeError("mono_get_root_domain returned NULL")

        if verbose:
            print(f"  root_domain = 0x{root_domain_address:X}")

        self.caller.enable_thread_attach(
            self.function_addresses["mono_thread_attach"],
            self.function_addresses["mono_thread_detach"],
            root_domain_address,
        )

        self.root_domain = root_domain_address

        return self.root_domain

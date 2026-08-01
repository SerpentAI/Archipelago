from typing import Any, Dict, NamedTuple, Optional, Tuple

import struct

import pymem.process
import pymem.ressources.structure

from pymem import Pymem

from .data.game_data import game_mode_internal_id_to_game_mode, table_internal_name_to_table

from .enums import PinballFXGameModes, PinballFXTables


class GameState(NamedTuple):
    is_valid: bool

    is_in_menu: Optional[bool] = None
    is_on_table: Optional[bool] = None

    table: Optional[PinballFXTables] = None
    game_mode: Optional[PinballFXGameModes] = None
    score: Optional[int] = None


class GameStateManager:
    process_name: str = "PinballFX-Win64-Shipping.exe"

    gnames_offset: int = 0x5F23600
    gobjects_offset: int = 0x5F7BA40
    gworld_offset: int = 0x60C6720

    process_event_offset: int = 0x1A6EF40
    process_event_vtable_offset: int = 0x44

    process: Optional[Pymem]
    is_process_running: bool

    gnames_mapping: Dict[int, str]
    gnames_mapping_reverse: Dict[str, int]

    gobjects_name_to_object: Dict[str, Dict[str, Any]]
    gobjects_address_to_object: Dict[int, Dict[str, Any]]

    last_seen_is_in_menu: Optional[bool]
    last_seen_is_on_table: Optional[bool]

    game_state: Optional[GameState]

    def __init__(self) -> None:
        self.process = None
        self.is_process_running = False

        self.gnames_mapping = dict()
        self.gnames_mapping_reverse = dict()

        self.gobjects_name_to_object = dict()
        self.gobjects_address_to_object = dict()

        self.last_seen_is_in_menu = False
        self.last_seen_is_on_table = False

        self.game_state = GameState(is_valid=False)

    def open_process_handle(self) -> bool:
        try:
            self.process = Pymem(self.process_name)
            self.is_process_running = True

            self._generate_gnames_mapping()

            self.gnames_mapping_reverse = {v: k for k, v in self.gnames_mapping.items()}

            self._refresh_gobjects_mapping()
        except Exception:
            return False

        return True

    def close_process_handle(self) -> bool:
        if pymem.process.close_handle(self.process.process_handle):
            self.is_process_running = False
            self.process = None

            self.gnames_mapping = dict()
            self.gnames_mapping_reverse = dict()

            self.gobjects_name_to_object = dict()
            self.gobjects_address_to_object = dict()

            self.last_seen_is_in_menu = False
            self.last_seen_is_on_table = False

            self.game_state = GameState(is_valid=False)

            return True

        return False

    def is_process_still_running(self) -> bool:
        try:
            self.process.read_int(self.process.base_address)
        except Exception:
            self.is_process_running = False
            self.process = None

            self.gnames_mapping = dict()
            self.gnames_mapping_reverse = dict()

            self.gobjects_name_to_object = dict()
            self.gobjects_address_to_object = dict()

            self.last_seen_is_in_menu = False
            self.last_seen_is_on_table = False

            self.game_state = GameState(is_valid=False)

            return False

        return True

    def determine_game_state(self) -> GameState:
        self.game_state = self._determine_game_state()
        return self.game_state

    def enable_black_and_white_trap(self) -> bool:
        if not self.is_process_running:
            return False

        camera_component_address: int = self._resolve_address(self.gworld_offset, (0x128, 0x258, 0x0, 0x2A8, 0x4D8, 0x0))

        if camera_component_address in (None, 0):
            return False

        override_color_saturation_address: int = camera_component_address + 0x290
        color_saturation_base_address: int = camera_component_address + 0x2C0
        color_contrast_base_address: int = camera_component_address + 0x2D0

        bitfield_value: int = self.process.read_int(override_color_saturation_address)

        bitfield_value |= (1 << 3)
        bitfield_value |= (1 << 4)

        self.process.write_int(override_color_saturation_address, bitfield_value)

        self.process.write_float(color_saturation_base_address + 0xC, 0.0)
        self.process.write_float(color_contrast_base_address + 0xC, 20.0)

        return True

    def disable_black_and_white_trap(self) -> bool:
        if not self.is_process_running:
            return False

        camera_component_address: int = self._resolve_address(self.gworld_offset, (0x128, 0x258, 0x0, 0x2A8, 0x4D8, 0x0))

        if camera_component_address in (None, 0):
            return False

        override_color_saturation_address: int = camera_component_address + 0x290
        color_saturation_base_address: int = camera_component_address + 0x2C0
        color_contrast_base_address: int = camera_component_address + 0x2D0

        bitfield_value: int = self.process.read_int(override_color_saturation_address)

        bitfield_value &= ~(1 << 3)
        bitfield_value &= ~(1 << 4)

        self.process.write_int(override_color_saturation_address, bitfield_value)

        self.process.write_float(color_saturation_base_address + 0xC, 1.0)
        self.process.write_float(color_contrast_base_address + 0xC, 1.0)

        return True

    def enable_bloom_trap(self) -> bool:
        if not self.is_process_running:
            return False

        camera_component_address: int = self._resolve_address(self.gworld_offset, (0x128, 0x258, 0x0, 0x2A8, 0x4D8, 0x0))

        if camera_component_address in (None, 0):
            return False

        override_color_gain_address: int = camera_component_address + 0x290
        override_bloom_intensity_address: int = camera_component_address + 0x296

        color_gain_base_address: int = camera_component_address + 0x2F0
        bloom_intensity_address: int = camera_component_address + 0x4AC

        bitfield_value: int = self.process.read_int(override_color_gain_address)
        bitfield_value |= (1 << 6)

        self.process.write_int(override_color_gain_address, bitfield_value)

        bitfield_value: int = self.process.read_int(override_bloom_intensity_address)
        bitfield_value |= (1 << 3)

        self.process.write_int(override_bloom_intensity_address, bitfield_value)

        self.process.write_float(color_gain_base_address + 0xC, 10.0)
        self.process.write_float(bloom_intensity_address, 24.0)

        return True

    def disable_bloom_trap(self) -> bool:
        if not self.is_process_running:
            return False

        camera_component_address: int = self._resolve_address(self.gworld_offset, (0x128, 0x258, 0x0, 0x2A8, 0x4D8, 0x0))

        if camera_component_address in (None, 0):
            return False

        override_color_gain_address: int = camera_component_address + 0x290
        override_bloom_intensity_address: int = camera_component_address + 0x296

        color_gain_base_address: int = camera_component_address + 0x2F0
        bloom_intensity_address: int = camera_component_address + 0x4AC

        bitfield_value: int = self.process.read_int(override_color_gain_address)
        bitfield_value &= ~(1 << 6)

        self.process.write_int(override_color_gain_address, bitfield_value)

        bitfield_value: int = self.process.read_int(override_bloom_intensity_address)
        bitfield_value &= ~(1 << 3)

        self.process.write_int(override_bloom_intensity_address, bitfield_value)

        self.process.write_float(color_gain_base_address + 0xC, 1.0)
        self.process.write_float(bloom_intensity_address, 0.675)

        return True

    def enable_chromatic_trap(self) -> bool:
        if not self.is_process_running:
            return False

        camera_component_address: int = self._resolve_address(self.gworld_offset, (0x128, 0x258, 0x0, 0x2A8, 0x4D8, 0x0))

        if camera_component_address in (None, 0):
            return False

        override_color_saturation_address: int = camera_component_address + 0x290
        color_saturation_base_address: int = camera_component_address + 0x2C0

        bitfield_value: int = self.process.read_int(override_color_saturation_address)
        bitfield_value |= (1 << 3)

        self.process.write_int(override_color_saturation_address, bitfield_value)

        self.process.write_float(color_saturation_base_address + 0xC, 18.0)

        return True

    def disable_chromatic_trap(self) -> bool:
        if not self.is_process_running:
            return False

        camera_component_address: int = self._resolve_address(self.gworld_offset, (0x128, 0x258, 0x0, 0x2A8, 0x4D8, 0x0))

        if camera_component_address in (None, 0):
            return False

        override_color_saturation_address: int = camera_component_address + 0x290
        color_saturation_base_address: int = camera_component_address + 0x2C0

        bitfield_value: int = self.process.read_int(override_color_saturation_address)
        bitfield_value &= ~(1 << 3)

        self.process.write_int(override_color_saturation_address, bitfield_value)

        self.process.write_float(color_saturation_base_address + 0xC, 1.0)

        return True

    def enable_color_inversion_trap(self) -> bool:
        if not self.is_process_running:
            return False

        camera_component_address: int = self._resolve_address(self.gworld_offset, (0x128, 0x258, 0x0, 0x2A8, 0x4D8, 0x0))

        if camera_component_address in (None, 0):
            return False

        override_color_saturation_address: int = camera_component_address + 0x290
        color_saturation_base_address: int = camera_component_address + 0x2C0

        bitfield_value: int = self.process.read_int(override_color_saturation_address)
        bitfield_value |= (1 << 3)

        self.process.write_int(override_color_saturation_address, bitfield_value)

        self.process.write_float(color_saturation_base_address, -1.0)
        self.process.write_float(color_saturation_base_address + 0x4, -1.0)
        self.process.write_float(color_saturation_base_address + 0x8, -1.0)

        return True

    def disable_color_inversion_trap(self) -> bool:
        if not self.is_process_running:
            return False

        camera_component_address: int = self._resolve_address(self.gworld_offset, (0x128, 0x258, 0x0, 0x2A8, 0x4D8, 0x0))

        if camera_component_address in (None, 0):
            return False

        override_color_saturation_address: int = camera_component_address + 0x290
        color_saturation_base_address: int = camera_component_address + 0x2C0

        bitfield_value: int = self.process.read_int(override_color_saturation_address)
        bitfield_value &= ~(1 << 3)

        self.process.write_int(override_color_saturation_address, bitfield_value)

        self.process.write_float(color_saturation_base_address, 1.0)
        self.process.write_float(color_saturation_base_address + 0x4, 1.0)
        self.process.write_float(color_saturation_base_address + 0x8, 1.0)

        return True

    def enable_grainy_trap(self) -> bool:
        if not self.is_process_running:
            return False

        camera_component_address: int = self._resolve_address(self.gworld_offset, (0x128, 0x258, 0x0, 0x2A8, 0x4D8, 0x0))

        if camera_component_address in (None, 0):
            return False

        override_grain_jitter_address: int = camera_component_address + 0x29C
        grain_jitter_base_address: int = camera_component_address + 0x694

        bitfield_value: int = self.process.read_int(override_grain_jitter_address)
        bitfield_value |= (1 << 5)

        self.process.write_int(override_grain_jitter_address, bitfield_value)

        self.process.write_float(grain_jitter_base_address, 100.0)

        return True

    def disable_grainy_trap(self) -> bool:
        if not self.is_process_running:
            return False

        camera_component_address: int = self._resolve_address(self.gworld_offset, (0x128, 0x258, 0x0, 0x2A8, 0x4D8, 0x0))

        if camera_component_address in (None, 0):
            return False

        override_grain_jitter_address: int = camera_component_address + 0x29C
        grain_jitter_base_address: int = camera_component_address + 0x694

        bitfield_value: int = self.process.read_int(override_grain_jitter_address)
        bitfield_value &= ~(1 << 5)

        self.process.write_int(override_grain_jitter_address, bitfield_value)

        self.process.write_float(grain_jitter_base_address, 0.0)

        return True

    def enable_tunnel_vision_trap(self) -> bool:
        if not self.is_process_running:
            return False

        camera_component_address: int = self._resolve_address(self.gworld_offset, (0x128, 0x258, 0x0, 0x2A8, 0x4D8, 0x0))

        if camera_component_address in (None, 0):
            return False

        override_vignette_intensity_address: int = camera_component_address + 0x29C
        vignette_intensity_address: int = camera_component_address + 0x690

        bitfield_value: int = self.process.read_int(override_vignette_intensity_address)
        bitfield_value |= (1 << 3)

        self.process.write_int(override_vignette_intensity_address, bitfield_value)

        self.process.write_float(vignette_intensity_address, 7.0)

        return True

    def disable_tunnel_vision_trap(self) -> bool:
        if not self.is_process_running:
            return False

        camera_component_address: int = self._resolve_address(self.gworld_offset, (0x128, 0x258, 0x0, 0x2A8, 0x4D8, 0x0))

        if camera_component_address in (None, 0):
            return False

        override_vignette_intensity_address: int = camera_component_address + 0x29C
        vignette_intensity_address: int = camera_component_address + 0x690

        bitfield_value: int = self.process.read_int(override_vignette_intensity_address)
        bitfield_value &= ~(1 << 3)

        self.process.write_int(override_vignette_intensity_address, bitfield_value)

        self.process.write_float(vignette_intensity_address, 0.4)

        return True

    def _determine_game_state(self) -> GameState:
        if not self.is_process_running:
            return GameState(is_valid=False)

        gworld_address: int = self._resolve_address(self.gworld_offset, (0x0,))

        if gworld_address in [0, None]:
            return GameState(is_valid=False)

        level_name: Optional[str] = None

        try:
            level_name_index: int = self.process.read_int(gworld_address + 0x18)
            level_name = self.gnames_mapping[level_name_index].lower()
        except Exception:
            GameState(is_valid=False)

        if level_name not in table_internal_name_to_table and level_name != "playroom":
            return GameState(is_valid=False)

        if level_name == "playroom":
            is_in_menu: bool = True
            is_on_table: bool = False

            if is_in_menu != self.last_seen_is_in_menu:
                self._refresh_gobjects_mapping()

                self.last_seen_is_in_menu = is_in_menu
                self.last_seen_is_on_table = is_on_table

            return GameState(
                is_valid=True,
                is_in_menu=is_in_menu,
                is_on_table=is_on_table,
            )
        else:
            is_in_menu: bool = False
            is_on_table: bool = True

            if is_on_table != self.last_seen_is_on_table:
                self._refresh_gobjects_mapping()

                self.last_seen_is_in_menu = is_in_menu
                self.last_seen_is_on_table = is_on_table

            is_valid: bool = True

            try:
                table: PinballFXTables = table_internal_name_to_table[level_name]

                game_mode: Optional[PinballFXGameModes] = None
                game_mode_address: int = self._resolve_address(self.gworld_offset, (0x188, 0xF8, 0x0))

                if game_mode_address not in [0, None]:
                    game_mode = game_mode_internal_id_to_game_mode.get(self.process.read_int(game_mode_address + 0x6C0 + 0x198))

                score: int = 0
                score_address = self._resolve_address(self.gworld_offset, (0x188, 0x438, 0x2B0, 0x20, 0x0))

                if score_address not in [0, None]:
                    score = self.process.read_longlong(score_address + 0x80)

            except Exception:
                is_valid = False

            if not is_valid:
                return GameState(is_valid=False)

            return GameState(
                is_valid=True,
                is_in_menu=is_in_menu,
                is_on_table=is_on_table,
                table=table,
                game_mode=game_mode,
                score=score,
            )

    def _generate_gnames_mapping(self):
        if not self.is_process_still_running():
            return

        mapping: Dict[int, str] = dict()

        gnames_pointer: int = self.process.base_address + self.gnames_offset
        blocks_base_address: int = gnames_pointer + 0x10

        try:
            table_data: bytes = self.process.read_bytes(blocks_base_address, 8192 * 8)
            block_pointers: Tuple[int, ...] = struct.unpack("<8192Q", table_data)
        except:
            return

        block_index: int
        block_pointer: int
        for block_index, block_pointer in enumerate(block_pointers):
            if not block_pointer:
                continue

            try:
                chunk_data: bytes = self.process.read_bytes(block_pointer, 0x40000)
            except:
                continue

            offset: int = 0
            while offset < 0x40000 - 6:
                header: int = int.from_bytes(chunk_data[offset + 4: offset + 6], "little")

                if header == 0:
                    break

                is_wide: bool = header & 0x1
                length: int = header >> 1

                if length <= 0:
                    break

                name_index: int = (block_index << 16) | (offset // 4)

                start: int = offset + 6

                entry_size: int
                name: str

                if is_wide:
                    end: int = start + (length * 2)
                    name = chunk_data[start:end].decode("utf-16", errors="ignore")
                    entry_size = 6 + (length * 2)
                else:
                    end: int = start + length
                    name = chunk_data[start:end].decode("utf-8", errors="ignore")
                    entry_size = 6 + length

                mapping[name_index] = name

                offset += (entry_size + 3) & ~3

        self.gnames_mapping = mapping

    def _refresh_gobjects_mapping(self):
        if not self.is_process_still_running():
            return

        self.gobjects_name_to_object = dict()
        self.gobjects_address_to_object = dict()

        gobjects_address: int = self.process.base_address + self.gobjects_offset

        chunks_pointer_base_address: int = self.process.read_longlong(gobjects_address + 0x0)
        element_count: int = self.process.read_int(gobjects_address + 0x14)

        chunk_index: int
        for chunk_index in range((element_count // 65536) + 1):
            chunk_address: int = self.process.read_longlong(chunks_pointer_base_address + (chunk_index * 8))

            if not chunk_address:
                continue

            bytes_to_read: int = min(65536, element_count - (chunk_index * 65536))

            chunk_bytes: bytes = self.process.read_bytes(chunk_address, bytes_to_read * 24)

            i: int
            for i in range(bytes_to_read):
                object_pointer: int
                internal_flags: int

                object_pointer, internal_flags = struct.unpack("<QI", chunk_bytes[(i * 24):(i * 24 + 12)])

                internal_flags_exclude_mask: int = 0x30200000  # Unreachable | PendingKill | Garbage

                if internal_flags & internal_flags_exclude_mask:
                    continue

                if object_pointer > 0x100000:
                    try:
                        header_bytes: bytes = self.process.read_bytes(object_pointer + 0x8, 40)

                        object_flags: int
                        class_pointer: int
                        name_index: int
                        name_number: int
                        outer_pointer: int

                        object_flags, _, class_pointer, _, name_index, name_number, _, outer_pointer = struct.unpack("<IIQIIIIQ", header_bytes)

                        object_flags_exclude_mask: int = 0x60018000  # RF_Garbage | RF_PendingKill | RF_BeginDestroyed | RF_FinishDestroyed

                        if object_flags & object_flags_exclude_mask:
                            continue

                        display_name: str = self.gnames_mapping.get(name_index, "Unknown Object")

                        if name_number > 0:
                            display_name = f"{display_name}_{name_number - 1}"

                        if display_name not in self.gobjects_name_to_object:
                            self.gobjects_name_to_object[display_name] = list()

                        self.gobjects_name_to_object[display_name].append({
                            "name": display_name,
                            "address": object_pointer,
                            "outer": outer_pointer,
                            "class": class_pointer,
                        })

                        self.gobjects_address_to_object[object_pointer] = {
                            "name": display_name,
                            "address": object_pointer,
                            "outer": outer_pointer,
                            "class": class_pointer,
                        }
                    except:
                        continue

    def _resolve_address(self, base_offset: int, offsets: Tuple[int, ...]) -> Optional[int]:
        address: int = self.process.read_longlong(self.process.base_address + base_offset)

        for offset in offsets[:-1]:
            try:
                address = self.process.read_longlong(address + offset)
            except Exception:
                return None

        return address + offsets[-1]

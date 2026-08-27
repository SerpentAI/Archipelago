from typing import List, NamedTuple, Optional, Tuple

import struct

import pymem.process
import pymem.ressources.structure

from pymem import Pymem

from .data.game_data import scene_internal_name_to_level

from .enums import PoolsLevels


class GameState(NamedTuple):
    is_valid: bool

    is_in_menu: Optional[bool] = None
    is_in_level: Optional[bool] = None

    level: Optional[PoolsLevels] = None
    level_progress_flags: Optional[Tuple[str, ...]] = None
    coordinates: Optional[Tuple[float, float, float]] = None
    collisions: Optional[Tuple[str, ...]] = None
    is_in_water: Optional[bool] = None
    is_rewinding: Optional[bool] = None
    is_zoomed_in: Optional[bool] = None
    is_sitting: Optional[bool] = None


class GameStateManager:
    process_name: str = "POOLS.exe"
    module_name: str = "GameAssembly.dll"

    autosave_offset: int = 0x41ABDF8
    camera_rewind_offset: int = 0x41AC018
    camera_stand_offset: int = 0x41AC258
    fps_controller_offset: int = 0x41AD3B8
    level_manager_offset: int = 0x41AE958
    water_lens_offset: int = 0x41B3C98
    zoom_offset: int = 0x41B40F8

    process: Optional[Pymem]
    is_process_running: bool

    module: Optional[pymem.ressources.structure.MODULEINFO]
    module_base_address: int

    last_seen_is_in_menu: Optional[bool]
    last_seen_is_in_level: Optional[bool]

    game_state: Optional[GameState]

    def __init__(self) -> None:
        self.process = None
        self.is_process_running = False

        self.module = None

        self.last_seen_is_in_menu = False
        self.last_seen_is_in_level = False

        self.game_state = GameState(is_valid=False)

    def open_process_handle(self) -> bool:
        try:
            self.process = Pymem(self.process_name)
            self.is_process_running = True

            self.module = pymem.process.module_from_name(self.process.process_handle, self.module_name)
            self.module_base_address = self.module.lpBaseOfDll
        except Exception:
            return False

        return True

    def close_process_handle(self) -> bool:
        if pymem.process.close_handle(self.process.process_handle):
            self.is_process_running = False
            self.process = None

            self.module = None
            self.module_base_address = None

            self.last_seen_is_in_menu = False
            self.last_seen_is_in_level = False

            self.game_state = GameState(is_valid=False)

            return True

        return False

    def is_process_still_running(self) -> bool:
        try:
            self.process.read_int(self.process.base_address)
        except Exception:
            self.is_process_running = False
            self.process = None

            self.module = None
            self.module_base_address = None

            self.last_seen_is_in_menu = False
            self.last_seen_is_in_level = False

            self.game_state = GameState(is_valid=False)

            return False

        return True

    def determine_game_state(self) -> GameState:
        self.game_state = self._determine_game_state()
        return self.game_state

    def set_walk_speed(self, walk_speed: float) -> bool:
        if not self.is_process_running:
            return False

        fps_controller_address: int = self._resolve_address(self.fps_controller_offset, (0xB8, 0x0, 0x0))

        if fps_controller_address in (None, 0):
            return False

        walk_speed_address: int = fps_controller_address + 0xD4

        self.process.write_float(walk_speed_address, walk_speed)

        return True

    def set_run_speed(self, run_speed: float) -> bool:
        if not self.is_process_running:
            return False

        fps_controller_address: int = self._resolve_address(self.fps_controller_offset, (0xB8, 0x0, 0x0))

        if fps_controller_address in (None, 0):
            return False

        walk_speed_address: int = fps_controller_address + 0xD8

        self.process.write_float(walk_speed_address, run_speed)

        return True

    def enable_no_look_trap(self) -> bool:
        if not self.is_process_running:
            return False

        fps_controller_address: int = self._resolve_address(self.fps_controller_offset, (0xB8, 0x0, 0x0))

        if fps_controller_address in (None, 0):
            return False

        ignore_look_input_address: int = fps_controller_address + 0x1AE

        self.process.write_bool(ignore_look_input_address, True)

        return True

    def disable_no_look_trap(self) -> bool:
        if not self.is_process_running:
            return False

        fps_controller_address: int = self._resolve_address(self.fps_controller_offset, (0xB8, 0x0, 0x0))

        if fps_controller_address in (None, 0):
            return False

        ignore_look_input_address: int = fps_controller_address + 0x1AE

        self.process.write_bool(ignore_look_input_address, False)

        return True

    def enable_rewind_trap(self) -> bool:
        if not self.is_process_running:
            return False

        camera_rewind_address: int = self._resolve_address(self.camera_rewind_offset, (0xB8, 0x0, 0x0))

        if camera_rewind_address in (None, 0):
            return False

        state_address: int = camera_rewind_address + 0x30

        self.process.write_int(state_address, 1)

        return True

    def disable_rewind_trap(self) -> bool:
        if not self.is_process_running:
            return False

        camera_rewind_address: int = self._resolve_address(self.camera_rewind_offset, (0xB8, 0x0, 0x0))

        if camera_rewind_address in (None, 0):
            return False

        state_address: int = camera_rewind_address + 0x30

        self.process.write_int(state_address, 0)

        return True

    def enable_slow_trap(self) -> bool:
        results: List[bool] = list()

        results.append(self.set_walk_speed(3.0))
        results.append(self.set_run_speed(3.0))

        return all(results)

    def disable_slow_trap(self) -> bool:
        # The game controller will resume updating the speeds according to the items received once the trap expires
        return True

    def enable_wet_trap(self) -> bool:
        if not self.is_process_running:
            return False

        water_lens_address: int = self._resolve_address(self.water_lens_offset, (0xB8, 0x0, 0x0))

        if water_lens_address in (None, 0):
            return False

        wetness_address: int = water_lens_address + 0x50

        self.process.write_float(wetness_address, 1.0)

        return True

    def disable_wet_trap(self) -> bool:
        # Let the wetness fade naturally
        return True

    def _determine_game_state(self) -> GameState:
        if not self.is_process_running:
            return GameState(is_valid=False)

        level_manager_address: int = self._resolve_address(self.level_manager_offset, (0xB8, 0x0, 0x0))

        is_level_manager_present: bool = True

        if level_manager_address in [0, None]:
            is_level_manager_present = False

        autosave_address: int = self._resolve_address(self.autosave_offset, (0xB8, 0x0, 0x0))

        is_autosave_present: bool = True

        if autosave_address in [0, None]:
            is_autosave_present = False

        if not is_level_manager_present and not is_autosave_present:
            return GameState(is_valid=False)

        if is_level_manager_present:
            is_in_menu: bool = True
            is_in_level: bool = False

            if is_in_menu != self.last_seen_is_in_menu:
                self.last_seen_is_in_menu = is_in_menu
                self.last_seen_is_in_level = is_in_level

            return GameState(
                is_valid=True,
                is_in_menu=is_in_menu,
                is_in_level=is_in_level,
            )
        elif is_autosave_present:
            is_in_menu: bool = False
            is_in_level: bool = True

            if is_in_level != self.last_seen_is_in_level:
                self.last_seen_is_in_menu = is_in_menu
                self.last_seen_is_in_level = is_in_level

            is_valid = True

            try:
                # Level
                scene_string_address: int = self._resolve_address(self.autosave_offset, (0xB8, 0x0, 0x30, 0x10, 0x0))
                scene_string_length: int = self.process.read_int(scene_string_address + 0x10)

                scene_bytes: bytes = self.process.read_bytes(scene_string_address + 0x14, scene_string_length * 2)
                scene_string: str = scene_bytes.decode("utf-16-le")

                level: PoolsLevels = scene_internal_name_to_level.get(scene_string)

                if level == PoolsLevels.ENDING:
                    return GameState(
                        is_valid=True,
                        is_in_menu=is_in_menu,
                        is_in_level=is_in_level,
                        level=level,
                    )

                # Level Progress Flags
                level_progress_flags_address: int = self._resolve_address(self.autosave_offset, (0xB8, 0x0, 0x30, 0x20, 0x0))
                level_progress_flags_length: int = self.process.read_int(level_progress_flags_address + 0x18)

                level_progress_flags: List[str] = list()

                i: int
                for i in range(level_progress_flags_length):
                    flag_string_address = self._resolve_address(self.autosave_offset, (0xB8, 0x0, 0x30, 0x20, 0x10, 0x20 + (i * 0x8), 0x0))
                    flag_string_length: int = self.process.read_int(flag_string_address + 0x10)

                    flag_bytes: bytes = self.process.read_bytes(flag_string_address + 0x14, flag_string_length * 2)
                    flag_string: str = flag_bytes.decode("utf-16-le")

                    level_progress_flags.append(flag_string)

                # Coordinates
                camera_stand_address: int = self._resolve_address(self.camera_stand_offset, (0xB8, 0x0, 0x0))
                coordinates: Tuple[float, float, float] = struct.unpack("<3f", self.process.read_bytes(camera_stand_address + 0x50, 12))

                # Is Sitting?
                is_sitting: bool = not self.process.read_bool(camera_stand_address + 0x71)

                # Collisions
                mesh_colliders_address: int = self._resolve_address(self.fps_controller_offset, (0xB8, 0x0, 0x1F0, 0x28, 0x0))
                mesh_colliders_length: int = self.process.read_int(mesh_colliders_address + 0x18)

                collisions: List[str] = list()

                i: int
                for i in range(mesh_colliders_length):
                    mesh_collider_name_string_address: int = self._resolve_address(self.fps_controller_offset, (0xB8, 0x0, 0x1F0, 0x28, 0x10, 0x20 + (i * 0x8), 0x10, 0x20, 0x50, 0x0))

                    mesh_collider_name_bytes: bytes = self.process.read_bytes(mesh_collider_name_string_address, 0x50).split(b"\x00", 1)[0]
                    mesh_collider_name: str = mesh_collider_name_bytes.decode("utf-8")

                    collisions.append(mesh_collider_name)

                # Is In Water?
                fps_controller_address: int = self._resolve_address(self.fps_controller_offset, (0xB8, 0x0, 0x0))
                is_in_water: bool = self.process.read_int(fps_controller_address + 0x180) == 1

                # Is Rewinding?
                camera_rewind_address: int = self._resolve_address(self.camera_rewind_offset, (0xB8, 0x0, 0x0))
                is_rewinding: bool = self.process.read_int(camera_rewind_address + 0x30) == 1

                # Is Zoomed In?
                zoom_address: int = self._resolve_address(self.zoom_offset, (0xB8, 0x0, 0x0))
                is_zoomed_in: bool = self.process.read_float(zoom_address + 0x60) < 1.0

            except Exception:
                is_valid = False

            if not is_valid:
                return GameState(is_valid=False)

            return GameState(
                is_valid=True,
                is_in_menu=is_in_menu,
                is_in_level=is_in_level,
                level=level,
                level_progress_flags=tuple(level_progress_flags),
                coordinates=coordinates,
                collisions=tuple(collisions),
                is_in_water=is_in_water,
                is_rewinding=is_rewinding,
                is_zoomed_in=is_zoomed_in,
                is_sitting=is_sitting,
            )

        return GameState(is_valid=False)

    def _resolve_address(self, base_offset: int, offsets: Tuple[int, ...]) -> Optional[int]:
        address: int = self.process.read_longlong(self.module_base_address + base_offset)

        for offset in offsets[:-1]:
            try:
                address = self.process.read_longlong(address + offset)
            except Exception:
                return None

        return address + offsets[-1]

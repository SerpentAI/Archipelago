from typing import Any, Dict, List, NamedTuple, Optional, Tuple

import struct

import pymem.process
import pymem.ressources.structure

from pymem import Pymem

from .data.game_data import (
    difficulty_internal_index_to_difficulty,
    level_internal_name_to_level,
    mutator_internal_index_to_mutator,
    stylish_action_internal_index_to_stylish_action,
)

from .enums import (
    SeveredSteelDifficulties,
    SeveredSteelLevels,
    SeveredSteelMutators,
    SeveredSteelStylishActions,
)


class GameState(NamedTuple):
    is_valid: bool

    is_in_menu: Optional[bool] = None
    is_in_level: Optional[bool] = None

    level: Optional[SeveredSteelLevels] = None
    difficulty: Optional[SeveredSteelDifficulties] = None
    mutator_count: Optional[int] = None
    mutators: Optional[List[SeveredSteelMutators]] = None
    is_mirrored: Optional[bool] = None
    time: Optional[float] = None
    is_level_complete: Optional[bool] = None
    was_level_completed_recently: Optional[bool] = None
    score: Optional[int] = None
    kill_count: Optional[int] = None
    stylish_action_counts: Optional[Dict[SeveredSteelStylishActions, int]] = None
    completed_challenge_count: Optional[int] = None


class GameStateManager:
    process_name: str = "ThankYouVeryCool-Win64-Shipping.exe"

    gnames_offset: int = 0x5A018C0
    gobjects_offset: int = 0x5A3DC10
    gworld_offset: int = 0x5B85440

    process_event_offset: int = 0x1AC4EB0
    process_event_vtable_offset: int = 0x44

    process: Optional[Pymem]
    is_process_running: bool

    gnames_mapping: Dict[int, str]
    gnames_mapping_reverse: Dict[str, int]

    gobjects_name_to_object: Dict[str, Dict[str, Any]]
    gobjects_address_to_object: Dict[int, Dict[str, Any]]

    last_seen_is_in_menu: Optional[bool]
    last_seen_is_in_level: Optional[bool]

    has_seen_mirrored: bool
    has_seen_victory_widget: bool

    game_state: Optional[GameState]

    def __init__(self) -> None:
        self.process = None
        self.is_process_running = False

        self.gnames_mapping = dict()
        self.gnames_mapping_reverse = dict()

        self.gobjects_name_to_object = dict()
        self.gobjects_address_to_object = dict()

        self.last_seen_is_in_menu = False
        self.last_seen_is_in_level = False

        self.has_seen_mirrored = False
        self.has_seen_victory_widget = False

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
            self.last_seen_is_in_level = False

            self.has_seen_mirrored = False
            self.has_seen_victory_widget = False

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
            self.last_seen_is_in_level = False

            self.has_seen_mirrored = False
            self.has_seen_victory_widget = False

            self.game_state = GameState(is_valid=False)

            return False

        return True

    def determine_game_state(self) -> GameState:
        self.game_state = self._determine_game_state()
        return self.game_state

    def disable_upload_to_leaderboard(self) -> bool:
        if not self.is_process_running:
            return False

        try:
            game_mode_address: int = self._resolve_address(self.gworld_offset, (0x118, 0x0))
            self.process.write_bool(game_mode_address + 0x1229, False)
        except Exception:
            return False

        return True

    def enable_unlock_all(self) -> bool:
        if not self.is_process_running:
            return False

        try:
            game_mode_address: int = self._resolve_address(self.gworld_offset, (0x118, 0x0))
            self.process.write_bool(game_mode_address + 0x1445, True)
        except Exception:
            return False

        return True

    def set_multiplier_burn_rate(self, multiplier_burn_rate: float) -> bool:
        if not self.is_process_running:
            return False
        elif not self.game_state.is_in_level:
            return False

        try:
            pawn_address: int = self._resolve_address(self.gworld_offset, (0x120, 0x238, 0x0, 0x280, 0x0))

            if pawn_address in [0, None]:
                return False

            self.process.write_float(pawn_address + 0xCDC, multiplier_burn_rate)
        except Exception:
            return False

        return True

    def set_fresh_cooldown(self, fresh_cooldown: float) -> bool:
        if not self.is_process_running:
            return False
        elif not self.game_state.is_in_level:
            return False

        try:
            stats_manager_address: int = self._resolve_address(self.gworld_offset, (0x118, 0x1470, 0x0))

            if stats_manager_address in [0, None]:
                return False

            self.process.write_float(stats_manager_address + 0x308, fresh_cooldown)
        except Exception:
            return False

        return True

    def enable_unlimited_ammo(self) -> bool:
        if not self.is_process_running:
            return False
        elif not self.game_state.is_in_level:
            return False

        try:
            game_mode_address: int = self._resolve_address(self.gworld_offset, (0x118, 0x0))

            if game_mode_address in [0, None]:
                return False

            self.process.write_bool(game_mode_address + 0x1457, True)
        except Exception:
            return False

        return True

    def disable_unlimited_ammo(self) -> bool:
        if not self.is_process_running:
            return False
        elif not self.game_state.is_in_level:
            return False

        try:
            game_mode_address: int = self._resolve_address(self.gworld_offset, (0x118, 0x0))

            if game_mode_address in [0, None]:
                return False

            self.process.write_bool(game_mode_address + 0x1457, False)
        except Exception:
            return False

        return True

    def enable_unlimited_cannon_ammo(self) -> bool:
        if not self.is_process_running:
            return False
        elif not self.game_state.is_in_level:
            return False

        try:
            game_mode_address: int = self._resolve_address(self.gworld_offset, (0x118, 0x0))

            if game_mode_address in [0, None]:
                return False

            self.process.write_bool(game_mode_address + 0x1448, True)
        except Exception:
            return False

        return True

    def disable_unlimited_cannon_ammo(self) -> bool:
        if not self.is_process_running:
            return False
        elif not self.game_state.is_in_level:
            return False

        try:
            game_mode_address: int = self._resolve_address(self.gworld_offset, (0x118, 0x0))

            if game_mode_address in [0, None]:
                return False

            self.process.write_bool(game_mode_address + 0x1448, False)
        except Exception:
            return False

        return True

    def enable_god_mode(self) -> bool:
        if not self.is_process_running:
            return False
        elif not self.game_state.is_in_level:
            return False

        try:
            game_mode_address: int = self._resolve_address(self.gworld_offset, (0x118, 0x0))

            if game_mode_address in [0, None]:
                return False

            self.process.write_bool(game_mode_address + 0x2F0, True)
        except Exception:
            return False

        return True

    def disable_god_mode(self) -> bool:
        if not self.is_process_running:
            return False
        elif not self.game_state.is_in_level:
            return False

        try:
            game_mode_address: int = self._resolve_address(self.gworld_offset, (0x118, 0x0))

            if game_mode_address in [0, None]:
                return False

            self.process.write_bool(game_mode_address + 0x2F0, False)
        except Exception:
            return False

        return True

    def enable_black_and_white_trap(self) -> bool:
        if not self.is_process_running:
            return False

        camera_component_address: int = self._resolve_address(self.gworld_offset, (0x120, 0x238, 0x0, 0x280, 0x1390, 0x0))

        if camera_component_address in (None, 0):
            return False

        override_color_saturation_address: int = camera_component_address + 0x270
        color_saturation_base_address: int = camera_component_address + 0x2A0
        color_contrast_base_address: int = camera_component_address + 0x2B0

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

        camera_component_address: int = self._resolve_address(self.gworld_offset, (0x120, 0x238, 0x0, 0x280, 0x1390, 0x0))

        if camera_component_address in (None, 0):
            return False

        override_color_saturation_address: int = camera_component_address + 0x270
        color_saturation_base_address: int = camera_component_address + 0x2A0
        color_contrast_base_address: int = camera_component_address + 0x2B0

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

        camera_component_address: int = self._resolve_address(self.gworld_offset, (0x120, 0x238, 0x0, 0x280, 0x1390, 0x0))

        if camera_component_address in (None, 0):
            return False

        override_color_gain_address: int = camera_component_address + 0x270
        override_bloom_intensity_address: int = camera_component_address + 0x276

        color_gain_base_address: int = camera_component_address + 0x2D0
        bloom_intensity_address: int = camera_component_address + 0x48C

        bitfield_value: int = self.process.read_int(override_color_gain_address)
        bitfield_value |= (1 << 6)

        self.process.write_int(override_color_gain_address, bitfield_value)

        bitfield_value: int = self.process.read_int(override_bloom_intensity_address)
        bitfield_value |= (1 << 3)

        self.process.write_int(override_bloom_intensity_address, bitfield_value)

        self.process.write_float(color_gain_base_address + 0xC, 10.0)
        self.process.write_float(bloom_intensity_address, 6.0)

        return True

    def disable_bloom_trap(self) -> bool:
        if not self.is_process_running:
            return False

        camera_component_address: int = self._resolve_address(self.gworld_offset, (0x120, 0x238, 0x0, 0x280, 0x1390, 0x0))

        if camera_component_address in (None, 0):
            return False

        override_color_gain_address: int = camera_component_address + 0x270
        override_bloom_intensity_address: int = camera_component_address + 0x276

        color_gain_base_address: int = camera_component_address + 0x2D0
        bloom_intensity_address: int = camera_component_address + 0x48C

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

        camera_component_address: int = self._resolve_address(self.gworld_offset, (0x120, 0x238, 0x0, 0x280, 0x1390, 0x0))

        if camera_component_address in (None, 0):
            return False

        override_color_saturation_address: int = camera_component_address + 0x270
        color_saturation_base_address: int = camera_component_address + 0x2A0

        bitfield_value: int = self.process.read_int(override_color_saturation_address)
        bitfield_value |= (1 << 3)

        self.process.write_int(override_color_saturation_address, bitfield_value)

        self.process.write_float(color_saturation_base_address + 0xC, 18.0)

        return True

    def disable_chromatic_trap(self) -> bool:
        if not self.is_process_running:
            return False

        camera_component_address: int = self._resolve_address(self.gworld_offset, (0x120, 0x238, 0x0, 0x280, 0x1390, 0x0))

        if camera_component_address in (None, 0):
            return False

        override_color_saturation_address: int = camera_component_address + 0x270
        color_saturation_base_address: int = camera_component_address + 0x2A0

        bitfield_value: int = self.process.read_int(override_color_saturation_address)
        bitfield_value &= ~(1 << 3)

        self.process.write_int(override_color_saturation_address, bitfield_value)

        self.process.write_float(color_saturation_base_address + 0xC, 1.0)

        return True

    def enable_cinematic_trap(self) -> bool:
        if not self.is_process_running:
            return False

        camera_component_address: int = self._resolve_address(self.gworld_offset, (0x120, 0x238, 0x0, 0x280, 0x1390, 0x0))

        if camera_component_address in (None, 0):
            return False

        aspect_ratio_address: int = camera_component_address + 0x208
        constraint_aspect_ratio_address: int = camera_component_address + 0x20C

        self.process.write_float(aspect_ratio_address, 5.0)

        bitfield_value: int = self.process.read_int(constraint_aspect_ratio_address)
        bitfield_value |= (1 << 0)

        self.process.write_int(constraint_aspect_ratio_address, bitfield_value)

        return True

    def disable_cinematic_trap(self) -> bool:
        if not self.is_process_running:
            return False

        camera_component_address: int = self._resolve_address(self.gworld_offset, (0x120, 0x238, 0x0, 0x280, 0x1390, 0x0))

        if camera_component_address in (None, 0):
            return False

        aspect_ratio_address: int = camera_component_address + 0x208
        constraint_aspect_ratio_address: int = camera_component_address + 0x20C

        self.process.write_float(aspect_ratio_address, 1.7778)

        bitfield_value: int = self.process.read_int(constraint_aspect_ratio_address)
        bitfield_value &= ~(1 << 0)

        self.process.write_int(constraint_aspect_ratio_address, bitfield_value)

        return True

    def enable_color_inversion_trap(self) -> bool:
        if not self.is_process_running:
            return False

        camera_component_address: int = self._resolve_address(self.gworld_offset, (0x120, 0x238, 0x0, 0x280, 0x1390, 0x0))

        if camera_component_address in (None, 0):
            return False

        override_color_saturation_address: int = camera_component_address + 0x270
        color_saturation_base_address: int = camera_component_address + 0x2A0

        bitfield_value: int = self.process.read_int(override_color_saturation_address)
        bitfield_value |= (1 << 3)

        self.process.write_int(override_color_saturation_address, bitfield_value)

        self.process.write_float(color_saturation_base_address, -1.0)
        self.process.write_float(color_saturation_base_address + 0x4, -1.0)
        self.process.write_float(color_saturation_base_address + 0x8, -1.0)
        self.process.write_float(color_saturation_base_address + 0xC, 3.0)

        return True

    def disable_color_inversion_trap(self) -> bool:
        if not self.is_process_running:
            return False

        camera_component_address: int = self._resolve_address(self.gworld_offset, (0x120, 0x238, 0x0, 0x280, 0x1390, 0x0))

        if camera_component_address in (None, 0):
            return False

        override_color_saturation_address: int = camera_component_address + 0x270
        color_saturation_base_address: int = camera_component_address + 0x2A0

        bitfield_value: int = self.process.read_int(override_color_saturation_address)
        bitfield_value &= ~(1 << 3)

        self.process.write_int(override_color_saturation_address, bitfield_value)

        self.process.write_float(color_saturation_base_address, 1.0)
        self.process.write_float(color_saturation_base_address + 0x4, 1.0)
        self.process.write_float(color_saturation_base_address + 0x8, 1.0)
        self.process.write_float(color_saturation_base_address + 0xC, 1.0)

        return True

    def enable_fast_mo_trap(self) -> bool:
        if not self.is_process_running:
            return False

        pawn_address: int = self._resolve_address(self.gworld_offset, (0x120, 0x238, 0x0, 0x280, 0x0))

        if pawn_address in [0, None]:
            return False

        in_stunt_dilation_address: int = pawn_address + 0x11B8
        default_dilation_address: int = pawn_address + 0x11BC
        reduced_dilation_address: int = pawn_address + 0x11C0

        self.process.write_float(in_stunt_dilation_address, 3.0)
        self.process.write_float(default_dilation_address, 3.0)
        self.process.write_float(reduced_dilation_address, 3.0)

        return True

    def disable_fast_mo_trap(self) -> bool:
        if not self.is_process_running:
            return False

        pawn_address: int = self._resolve_address(self.gworld_offset, (0x120, 0x238, 0x0, 0x280, 0x0))

        if pawn_address in [0, None]:
            return False

        in_stunt_dilation_address: int = pawn_address + 0x11B8
        default_dilation_address: int = pawn_address + 0x11BC
        reduced_dilation_address: int = pawn_address + 0x11C0

        self.process.write_float(in_stunt_dilation_address, 0.3)
        self.process.write_float(default_dilation_address, 0.3)
        self.process.write_float(reduced_dilation_address, 0.5)

        return True

    def enable_mobile_game_trap(self) -> bool:
        if not self.is_process_running:
            return False

        camera_component_address: int = self._resolve_address(self.gworld_offset, (0x120, 0x238, 0x0, 0x280, 0x1390, 0x0))

        if camera_component_address in (None, 0):
            return False

        aspect_ratio_address: int = camera_component_address + 0x208
        constraint_aspect_ratio_address: int = camera_component_address + 0x20C

        self.process.write_float(aspect_ratio_address, 0.5)

        bitfield_value: int = self.process.read_int(constraint_aspect_ratio_address)
        bitfield_value |= (1 << 0)

        self.process.write_int(constraint_aspect_ratio_address, bitfield_value)

        return True

    def disable_mobile_game_trap(self) -> bool:
        if not self.is_process_running:
            return False

        camera_component_address: int = self._resolve_address(self.gworld_offset, (0x120, 0x238, 0x0, 0x280, 0x1390, 0x0))

        if camera_component_address in (None, 0):
            return False

        aspect_ratio_address: int = camera_component_address + 0x208
        constraint_aspect_ratio_address: int = camera_component_address + 0x20C

        self.process.write_float(aspect_ratio_address, 1.7778)

        bitfield_value: int = self.process.read_int(constraint_aspect_ratio_address)
        bitfield_value &= ~(1 << 0)

        self.process.write_int(constraint_aspect_ratio_address, bitfield_value)

        return True

    def enable_tunnel_vision_trap(self) -> bool:
        if not self.is_process_running:
            return False

        camera_component_address: int = self._resolve_address(self.gworld_offset, (0x120, 0x238, 0x0, 0x280, 0x1390, 0x0))

        if camera_component_address in (None, 0):
            return False

        override_vignette_intensity_address: int = camera_component_address + 0x27C
        vignette_intensity_address: int = camera_component_address + 0x670

        bitfield_value: int = self.process.read_int(override_vignette_intensity_address)
        bitfield_value |= (1 << 3)

        self.process.write_int(override_vignette_intensity_address, bitfield_value)

        self.process.write_float(vignette_intensity_address, 7.0)

        return True

    def disable_tunnel_vision_trap(self) -> bool:
        if not self.is_process_running:
            return False

        camera_component_address: int = self._resolve_address(self.gworld_offset, (0x120, 0x238, 0x0, 0x280, 0x1390, 0x0))

        if camera_component_address in (None, 0):
            return False

        override_vignette_intensity_address: int = camera_component_address + 0x27C
        vignette_intensity_address: int = camera_component_address + 0x670

        bitfield_value: int = self.process.read_int(override_vignette_intensity_address)
        bitfield_value &= ~(1 << 3)

        self.process.write_int(override_vignette_intensity_address, bitfield_value)

        self.process.write_float(vignette_intensity_address, 0.4)

        return True

    def _determine_game_state(self) -> GameState:
        if not self.is_process_running:
            return GameState(is_valid=False)

        pawn_address: int = self._resolve_address(self.gworld_offset, (0x120, 0x238, 0x0, 0x280, 0x0))

        if pawn_address in [0, None]:
            return GameState(is_valid=False)

        try:
            pawn_name_index: int = self.process.read_int(pawn_address + 0x18)
            pawn_name: str = self.gnames_mapping[pawn_name_index]
        except Exception:
            return GameState(is_valid=False)

        if pawn_name not in ["BP_MenuPawn_C", "PlayerCharacter_BP_Manny_C"]:
            return GameState(is_valid=False)

        if pawn_name == "BP_MenuPawn_C":
            is_in_menu: bool = True
            is_in_level: bool = False

            if is_in_menu != self.last_seen_is_in_menu:
                self._refresh_gobjects_mapping()

                self.last_seen_is_in_menu = is_in_menu
                self.last_seen_is_in_level = is_in_level

            self.has_seen_mirrored = False
            self.has_seen_victory_widget = False

            return GameState(
                is_valid=True,
                is_in_menu=is_in_menu,
                is_in_level=is_in_level,
            )
        elif pawn_name == "PlayerCharacter_BP_Manny_C":
            is_in_menu: bool = False
            is_in_level: bool = True

            if is_in_level != self.last_seen_is_in_level:
                self._refresh_gobjects_mapping()

                self.last_seen_is_in_menu = is_in_menu
                self.last_seen_is_in_level = is_in_level

            is_valid = True

            try:
                game_mode_address: int = self._resolve_address(self.gworld_offset, (0x118, 0x0))

                game_type: int = self.process.read_bytes(game_mode_address + 0x1440, 1)[0]

                if game_type != 0:
                    is_valid = False

                level_address: int = self._resolve_address(self.gworld_offset, (0x118, 0x1418, 0x0))

                level_internal_name_index: int = self.process.read_int(level_address + 0x90)
                level_internal_name: str = self.gnames_mapping[level_internal_name_index].lower()

                level: SeveredSteelLevels = level_internal_name_to_level[level_internal_name]

                difficulty_internal_index: int = self.process.read_bytes(game_mode_address + 0x6E0, 1)[0]

                difficulty: SeveredSteelDifficulties = difficulty_internal_index_to_difficulty[difficulty_internal_index]

                mutator_count: int = self.process.read_int(game_mode_address + 0xAC0)

                mutators_array_address: int = self._resolve_address(self.gworld_offset, (0x118, 0xAB8, 0x0))
                mutators: List[SeveredSteelMutators] = list()

                if mutator_count > 0:
                    mutator_internal_indices: List[int] = list(bytearray(self.process.read_bytes(mutators_array_address, mutator_count)))

                    mutator_internal_index: int
                    for mutator_internal_index in mutator_internal_indices:
                        mutators.append(mutator_internal_index_to_mutator.get(mutator_internal_index))

                is_mirrored: bool
                if self.has_seen_mirrored:
                    is_mirrored = True
                else:
                    is_mirrored: bool = self.process.read_bool(game_mode_address + 0xB60)

                    if is_mirrored:
                        self.has_seen_mirrored = True

                speedrun_time: float = self.process.read_float(game_mode_address + 0xB64)

                if self.has_seen_victory_widget and speedrun_time <= 5.0:
                    self.has_seen_victory_widget = False

                is_level_complete: bool = False
                score: int = 0

                victory_widget_address: int = self._resolve_address(self.gworld_offset, (0x118, 0x1368, 0x0))

                if victory_widget_address not in [0, None]:
                    self.has_seen_victory_widget = True
                    is_level_complete = True

                    score_widget_ftext_address: int = self._resolve_address(self.gworld_offset, (0x118, 0x1368, 0x368, 0x128, 0x0))

                    if score_widget_ftext_address not in [0, None]:
                        score = self.process.read_int(score_widget_ftext_address + 0x30)

                npc_array_size: int = self.process.read_int(game_mode_address + 0x13A0)
                kill_count: int = 0

                npc_array_address: int = self._resolve_address(self.gworld_offset, (0x118, 0x1398, 0x0))

                if npc_array_address not in [0, None]:
                    i: int
                    for i in range(npc_array_size):
                        npc_address: int = self._resolve_address(self.gworld_offset, (0x118, 0x1398, 0x8 * i, 0x0))

                        if npc_address not in [0, None]:
                            is_dead: bool = self.process.read_bool(npc_address + 0xE78)

                            if is_dead:
                                kill_count += 1

                stats_manager_address: int = self._resolve_address(self.gworld_offset, (0x118, 0x1470, 0x0))

                if stats_manager_address not in [0, None]:
                    stats_manager_address_feat_map_size: int = self.process.read_int(stats_manager_address + 0x368)
                    stylish_action_counts: Dict[SeveredSteelStylishActions, int] = dict()

                    stats_manager_feat_map_address: int = self._resolve_address(self.gworld_offset, (0x118, 0x1470, 0x360, 0x0))

                    stats_manager_feat_map_bytes: bytes = self.process.read_bytes(
                        stats_manager_feat_map_address, 0x10 * stats_manager_address_feat_map_size
                    )

                    i: int
                    for i in range(stats_manager_address_feat_map_size):
                        stylish_action_internal_index: int = stats_manager_feat_map_bytes[0x10 * i]
                        stylish_action: Optional[SeveredSteelStylishActions] = stylish_action_internal_index_to_stylish_action.get(stylish_action_internal_index)

                        if stylish_action is None:
                            continue

                        stylish_action_count: int = struct.unpack("<I", stats_manager_feat_map_bytes[0x4 + 0x10 * i:0x8 + 0x10 * i])[0]

                        stylish_action_counts[stylish_action] = stylish_action_count

                    completed_challenge_count: int = self.process.read_int(stats_manager_address + 0x510)
            except Exception:
                is_valid = False

            if not is_valid:
                return GameState(is_valid=False)

            return GameState(
                is_valid=True,
                is_in_menu=is_in_menu,
                is_in_level=is_in_level,
                level=level,
                difficulty=difficulty,
                mutator_count=mutator_count,
                mutators=mutators,
                is_mirrored=is_mirrored,
                time=speedrun_time,
                is_level_complete=is_level_complete,
                was_level_completed_recently=self.has_seen_victory_widget,
                score=score,
                kill_count=kill_count,
                stylish_action_counts=stylish_action_counts,
                completed_challenge_count=completed_challenge_count,
            )

        return GameState(is_valid=False)

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
                chunk_data: bytes = self.process.read_bytes(block_pointer, 0x20000)
            except:
                continue

            offset: int = 0
            while offset < 0x20000 - 2:
                header: int = int.from_bytes(chunk_data[offset: offset + 2], "little")

                if header == 0:
                    break

                is_wide: bool = header & 0x1
                length: int = header >> 6

                if length <= 0:
                    break

                name_index: int = (block_index << 16) | (offset // 2)

                start: int = offset + 2

                if is_wide:
                    end: int = start + (length * 2)
                    name = chunk_data[start:end].decode("utf-16", errors="ignore")
                    entry_size = 2 + (length * 2)
                else:
                    end: int = start + length
                    name = chunk_data[start:end].decode("utf-8", errors="ignore")
                    entry_size = 2 + length

                mapping[name_index] = name

                offset += (entry_size + 1) & ~1

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
                        header_bytes: bytes = self.process.read_bytes(object_pointer + 0x8, 32)

                        object_flags: int
                        class_pointer: int
                        name_index: int
                        name_number: int
                        outer_pointer: int

                        object_flags, _, class_pointer, name_index, name_number, outer_pointer = struct.unpack("<IIQIIQ", header_bytes)

                        object_flags_exclude_mask: int = 0x60018000  # RF_Garbage | RF_PendingKill | RF_BeginDestroyed | RF_FinishDestroyed

                        if object_flags & object_flags_exclude_mask:
                            continue

                        display_name: str = self.gnames_mapping.get(name_index, "Unknown Object")

                        if name_number > 0:
                            display_name = f"{display_name}_{name_number - 1}"

                        if display_name not in self.gobjects_name_to_object:
                            self.gobjects_name_to_object[display_name] = list()

                        self.gobjects_name_to_object[display_name].append({
                            "address": object_pointer,
                            "outer": outer_pointer,
                            "class": class_pointer,
                        })

                        self.gobjects_address_to_object[object_pointer] = {
                            "name": display_name,
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

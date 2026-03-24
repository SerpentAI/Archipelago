from typing import Any, Dict, List, NamedTuple, Optional, Set, Tuple, Union

import ctypes
import functools
import struct

from pymem import Pymem
from pymem.process import close_handle

from .data.game_data import (
    gap_to_internal_names_reverse,
    level_to_internal_names_reverse,
    skater_to_internal_names,
    skater_to_internal_names_reverse,
    skater_to_internal_class_names_reverse,
    skater_to_specials,
    special_to_game_variable_name,
)

from .enums import (
    TonyHawksProSkater12Contexts,
    TonyHawksProSkater12Gaps,
    TonyHawksProSkater12Levels,
    TonyHawksProSkater12Skaters,
    TonyHawksProSkater12Specials,
)


class GameState(NamedTuple):
    context: TonyHawksProSkater12Contexts
    level: Optional[TonyHawksProSkater12Levels]
    are_injected_sandbox_modifiers_present: Optional[bool]
    skater: Optional[TonyHawksProSkater12Skaters]
    score: Optional[int]
    best_combo_score: Optional[int]
    longest_grind: Optional[float]
    longest_lip: Optional[float]
    longest_manual: Optional[float]


class GameStateManager:
    process_name: str = "THPS12.exe"

    gnames_offset: int = 0x3CC9500
    gobjects_offset: int = 0x3CE0C00
    gworld_offset: int = 0x3DCA248

    process_event_offset: int = 0xC1F360
    process_event_vtable_offset: int = 0x42

    gmalloc_offset: int = 0x3CC38D8

    process: Optional[Pymem]
    is_process_running: bool

    gnames_mapping: Dict[int, str]
    gnames_mapping_reverse: Dict[str, int]

    gobjects_name_to_object: Dict[str, List[Dict[str, Any]]]
    gobjects_address_to_object: Dict[int, Dict[str, Any]]

    local_player_offset: int = 0x3B9B4C8
    player_profile_entry_point_offset: int = 0x38EFDB8

    get_game_variable_as_int_function_address: Optional[int] = None

    sandbox_modifier_states: Dict[TonyHawksProSkater12Skaters, Dict[str, float]]

    def __init__(self) -> None:
        self.process = None
        self.is_process_running = False

        self.gnames_mapping = dict()
        self.gnames_mapping_reverse = dict()

        self.gobjects_name_to_object = dict()
        self.gobjects_address_to_object = dict()

        self.sandbox_modifier_states = dict()

    @property
    def player_controller_address(self) -> int:
        return self._resolve_address(self.local_player_offset, (0x30, 0x0))

    @property
    def player_state_address(self) -> int:
        return self._resolve_address(self.local_player_offset, (0x30, 0x220, 0x0))

    @property
    def score_struct_address(self) -> int:
        return self._resolve_address(self.local_player_offset, (0x30, 0x220, 0x3A0, 0x0))

    @property
    def sandbox_modifier_system_address(self) -> int:
        return self._resolve_address(self.local_player_offset, (0x30, 0x220, 0x3A8, 0x0))

    @property
    def sandbox_stats_address(self) -> int:
        return self._resolve_address(self.local_player_offset, (0x30, 0x220, 0x3A8, 0x228, 0x0))

    @property
    def game_variable_system_address(self) -> int:
        return self._resolve_address(self.local_player_offset, (0x30, 0x220, 0x458, 0x0))

    @property
    def level_address(self) -> int:
        return self._resolve_address(self.local_player_offset, (0x30, 0x20, 0x0))

    @property
    def world_address(self) -> int:
        return self._resolve_address(self.local_player_offset, (0x30, 0x20, 0x20, 0x0))

    @property
    def pawn_address(self) -> int:
        return self._resolve_address(self.local_player_offset, (0x30, 0x248, 0x0))

    @property
    def skeletal_mesh_component_address(self) -> int:
        return self._resolve_address(self.local_player_offset, (0x30, 0x248, 0x278, 0x0))

    @property
    def camera_component_address(self) -> int:
        return self._resolve_address(self.local_player_offset, (0x30, 0x248, 0x730, 0x0))

    @property
    def player_profile_address(self) -> int:
        return self._resolve_address(self.player_profile_entry_point_offset, (0x30, 0x0))

    @property
    def saved_game_address(self) -> int:
        return self._resolve_address(self.player_profile_entry_point_offset, (0x30, 0x350, 0x0))

    @functools.cached_property
    def default_sandbox_modifiers(self):
        return {
            "SBXStat.AirGravity": 1.0,
            "SBXStat.GroundGravity": 1.0,
            "SBXStat.WallGravity": 1.0,
            "SBXStat.MaxMoveSpeed": 1.0,
            "SBXStat.CrouchingAcceleration": 1.0,
            "SBXStat.StandingAcceleration": 1.0,
            "SBXStat.AirRotationSpeed": 1.0,
            "SBXStat.GroundRotationSpeed": 1.0,
            "SBXStat.PerfectManualBalance": 0.0,
            "SBXStat.PerfectLipBalance": 0.0,
            "SBXStat.PerfectGrindBalance": 0.0,
            "SBXStat.NoBails": 0.0,
            "SBXStat.MirrorLeftRightInputs": 0.0,
            "SBXStat.DisableStanceSwitching": 0.0,
            "SBXStat.DisableNollieStance": 0.0,
            "SBXStat.DisableWallplants": 0.0,
            "SBXStat.Score.AlwaysSpecial": 0.0,
            "SBXStat.Score.DoubleBaseScore": 0.0,
            "SBXStat.Score.NoFlipTrickPoints": 0.0,
            "SBXStat.Score.NoGrabTrickPoints": 0.0,
            "SBXStat.Score.NoGrindTrickPoints": 0.0,
            "SBXStat.Score.NoLipTrickPoints": 0.0,
            "SBXStat.Score.NoSpecialMeter": 0.0,
            "SBXStat.Score.NoSpinMultiplier": 0.0,
            "SBXStat.Score.NoSustainTrickPoints": 0.0,
            "SBXStat.MaxHandlingStats": 0.0,
            "SBXStat.MinHandlingStats": 0.0,
            "SBXStat.SkaterScale": 1.0,
            "SBXStat.Graphics.BlackAndWhite": 0.0,
            "SBXStat.Graphics.InvertedColors": 0.0,
            "SBXStat.Graphics.Mirror": 0.0,
            "SBXStat.Graphics.MonochromeHandheld": 0.0,
            "SBXStat.Graphics.Sepia": 0.0,
            "SBXStat.DisableLevelOut": 0.0,
            "SBXStat.DisableQuickTurn": 0.0,
            "SBXStat.DisableGrindIntoVert": 0.0,
            "SBXStat.DisableExtraTricks": 0.0,
            "SBXStat.MirrorAudioListener": 0.0,
            "SBXStat.DisableGrindIntoVertInput": 0.0,
            "SBXStat.DisableOllieOutOfLip": 0.0,
            "SBXStat.DisableTransfers": 0.0,
            "SBXStat.DisableManuals": 0.0,
            "SBXStat.EnableSpinTaps": 0.0,
            "SBXStat.WallPlantRequiresDown": 0.0,
        }

    def open_process_handle(self) -> bool:
        try:
            self.process = Pymem(self.process_name)
            self.is_process_running = True

            self._generate_gnames_mapping()

            self.gnames_mapping_reverse = {v: k for k, v in self.gnames_mapping.items()}

            self._refresh_gobjects_mapping()

            self.get_game_variable_as_int_function_address = (
                self.gobjects_name_to_object.get("GetGameVariableAsInt", [dict()])[0].get("address", 0)
            )
        except Exception:
            return False

        return True

    def close_process_handle(self) -> bool:
        if close_handle(self.process.process_handle):
            self.is_process_running = False
            self.process = None

            self.gnames_mapping = dict()
            self.gnames_mapping_reverse = dict()

            self.gobjects_name_to_object = dict()
            self.gobjects_address_to_object = dict()

            self.sandbox_modifier_states = dict()

            self.get_game_variable_as_int_function_address = None

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

            self.sandbox_modifier_states = dict()

            self.get_game_variable_as_int_function_address = None

            return False

        return True

    def determine_game_state(self) -> GameState:
        if self.player_controller_address in (None, 0) or self.is_status_inactive():
            return GameState(
                context=TonyHawksProSkater12Contexts.INVALID,
                are_injected_sandbox_modifiers_present=None,
                level=None,
                skater=None,
                score=None,
                best_combo_score=None,
                longest_grind=None,
                longest_lip=None,
                longest_manual=None,
            )

        if self.is_in_main_menu():
            return GameState(
                context=TonyHawksProSkater12Contexts.MENU,
                are_injected_sandbox_modifiers_present=None,
                level=None,
                skater=None,
                score=None,
                best_combo_score=None,
                longest_grind=None,
                longest_lip=None,
                longest_manual=None,
            )
        elif self.is_status_playing():
            return GameState(
                context=TonyHawksProSkater12Contexts.LEVEL,
                are_injected_sandbox_modifiers_present=self.are_injected_sandbox_modifiers_present(),
                level=self.get_level(),
                skater=self.get_skater(),
                score=self.get_score(),
                best_combo_score=self.get_best_combo_score(),
                longest_grind=self.get_longest_grind(),
                longest_lip=self.get_longest_lip(),
                longest_manual=self.get_longest_manual(),
            )

        return GameState(
            context=TonyHawksProSkater12Contexts.INVALID,
            are_injected_sandbox_modifiers_present=None,
            level=None,
            skater=None,
            score=None,
            best_combo_score=None,
            longest_grind=None,
            longest_lip=None,
            longest_manual=None,
        )

    def get_score(self) -> Optional[int]:
        if not self.is_process_still_running():
            return None

        try:
            return self.process.read_int(self.score_struct_address + 0x300)
        except Exception:
            return None

    def get_longest_grind(self) -> Optional[float]:
        if not self.is_process_still_running():
            return None

        try:
            return self.process.read_float(self.score_struct_address + 0x390)
        except Exception:
            return None

    def get_longest_manual(self) -> Optional[float]:
        if not self.is_process_still_running():
            return None

        try:
            return self.process.read_float(self.score_struct_address + 0x394)
        except Exception:
            return None

    def get_longest_lip(self) -> Optional[float]:
        if not self.is_process_still_running():
            return None

        try:
            return self.process.read_float(self.score_struct_address + 0x398)
        except Exception:
            return None

    def get_best_combo_score(self) -> Optional[int]:
        if not self.is_process_still_running():
            return None

        try:
            return self.process.read_int(self.score_struct_address + 0x350)
        except Exception:
            return None

    def are_injected_sandbox_modifiers_present(self) -> Optional[bool]:
        if not self.is_process_still_running():
            return None

        try:
            rank_0_pointer: int = self.process.read_longlong(self.sandbox_stats_address + 0x0)
            rank_0_size: int = self.process.read_int(self.sandbox_stats_address + 0x8)

            if rank_0_pointer == 0 or rank_0_size == 0:
                return False

            return True
        except Exception:
            return None

    def get_game_status(self) -> Optional[str]:
        if not self.is_process_still_running():
            return None

        try:
            return self.gnames_mapping[self.process.read_int(self.player_controller_address + 0x240)]
        except Exception:
            return None

    def is_status_inactive(self) -> Optional[bool]:
        return self.get_game_status() == "Inactive"

    def is_status_playing(self) -> Optional[bool]:
        return self.get_game_status() == "Playing"

    def get_level(self) -> Optional[Union[str, TonyHawksProSkater12Levels]]:
        if not self.is_process_still_running():
            return None

        try:
            level_internal_name: str = self.gnames_mapping[self.process.read_int(self.world_address + 0x18)]

            return level_to_internal_names_reverse.get(level_internal_name, level_internal_name)
        except Exception:
            return None

    def is_in_main_menu(self) -> Optional[bool]:
        return self.get_level() == "FrontEnd"

    def get_skater(self) -> Optional[Union[str, TonyHawksProSkater12Contexts]]:
        if not self.is_process_still_running():
            return None

        try:
            skater_internal_name: str = self.gnames_mapping[self.process.read_int(self.pawn_address + 0x18)]
            return skater_to_internal_class_names_reverse.get(skater_internal_name, skater_internal_name)
        except Exception:
            return None

    def get_gap_data_from_save(self) -> Optional[Dict[TonyHawksProSkater12Skaters, Dict[TonyHawksProSkater12Gaps, int]]]:
        if not self.is_process_still_running():
            return None

        try:
            gap_data: Dict[TonyHawksProSkater12Skaters, Dict[TonyHawksProSkater12Gaps, int]] = dict()

            tmap_address: int = self.saved_game_address + 0x200

            data_address: int = self.process.read_longlong(tmap_address)
            bucket_count: int = self.process.read_int(tmap_address + 0xC)

            inner_stride: int = 0x18

            i: int
            for i in range(bucket_count):
                bucket_address: int = data_address + (i * 0x60)

                skater_name_index: int = self.process.read_int(bucket_address)
                skater_name: str = self.gnames_mapping.get(skater_name_index)
                skater: TonyHawksProSkater12Skaters = skater_to_internal_names_reverse.get(skater_name)

                if skater is not None:
                    seen_gap_names: Set[str] = set()

                    inner_data_address: int = self.process.read_longlong(bucket_address + 0x08)
                    inner_count: int = self.process.read_int(bucket_address + 0x10)

                    skater_gaps: Dict[TonyHawksProSkater12Gaps, int] = dict()

                    if inner_data_address > 0 and inner_count > 0:
                        ii: int
                        for ii in range(inner_count):
                            element_address: int = inner_data_address + (ii * inner_stride)
                            gap_data_object_address: int = self.process.read_longlong(element_address)

                            if gap_data_object_address < 1:
                                continue

                            landed_count: int = self.process.read_int(element_address + 0x8)

                            gap_name_index: int = self.process.read_int(gap_data_object_address + 0x18)
                            gap_name = self.gnames_mapping.get(gap_name_index)

                            if gap_name is None:
                                continue
                            elif gap_name in seen_gap_names:
                                gap_name += "_Alt"

                            seen_gap_names.add(gap_name)

                            gap: TonyHawksProSkater12Gaps = gap_to_internal_names_reverse.get(gap_name)

                            if gap is None:
                                continue

                            skater_gaps[gap] = landed_count

                    gap_data[skater] = skater_gaps

            return gap_data
        except Exception:
            return None

    def get_landed_gap_counts(
        self,
        gap_filter: Optional[Dict[TonyHawksProSkater12Skaters, List[TonyHawksProSkater12Gaps]]] = None
    ) -> Optional[Dict[TonyHawksProSkater12Skaters, Dict[TonyHawksProSkater12Gaps, int]]]:
        gap_data: Optional[Dict[TonyHawksProSkater12Skaters, Dict[TonyHawksProSkater12Gaps, int]]] = (
            self.get_gap_data_from_save()
        )

        if gap_data is None:
            return None

        if gap_filter is None:
            return gap_data

        landed_gap_counts: Dict[TonyHawksProSkater12Skaters, Dict[TonyHawksProSkater12Gaps, int]] = dict()

        skater: TonyHawksProSkater12Skaters
        gaps: List[TonyHawksProSkater12Gaps]
        for skater, gaps in gap_filter.items():
            skater_landed_gap_counts: Dict[TonyHawksProSkater12Gaps, int] = dict()

            gap: TonyHawksProSkater12Gaps
            for gap in gaps:
                skater_landed_gap_counts[gap] = gap_data.get(skater, dict()).get(gap, 0)

            landed_gap_counts[skater] = skater_landed_gap_counts

        return landed_gap_counts

    def find_goal_level_manager_address(self) -> Optional[int]:
        if not self.is_process_still_running():
            return None

        self._refresh_gobjects_mapping()

        return self.gobjects_name_to_object.get("BP_Goal_Level_Manager_2", [dict()])[0].get("address", None)

    # Goal Level Manager address needs to be found in GObjects once when loading / restarting a level first
    def get_collected_skate_letters(self, goal_level_manager_address: int) -> Optional[Dict[str, bool]]:
        if not self.is_process_still_running():
            return None

        # Check if the level is in Speed Run mode
        if self.process.read_int(goal_level_manager_address + 0x438) != 10:
            return None

        goal_skate_address: int = self.process.read_longlong(goal_level_manager_address + 0x280)

        letters_found_count: int = self.process.read_int(goal_skate_address + 0x1B0)

        goal_target_count: int = self.process.read_int(goal_skate_address + 0x170)
        active_target_count: int = self.process.read_int(goal_skate_address + 0x180)

        if goal_target_count != 5 or active_target_count < 0 or active_target_count > 5:
            return None

        goal_target_array_address: int = self.process.read_longlong(goal_skate_address + 0x168)

        letter_s_pointer: int = self.process.read_longlong(goal_target_array_address + 0x0)
        letter_k_pointer: int = self.process.read_longlong(goal_target_array_address + 0x8)
        letter_a_pointer: int = self.process.read_longlong(goal_target_array_address + 0x10)
        letter_t_pointer: int = self.process.read_longlong(goal_target_array_address + 0x18)
        letter_e_pointer: int = self.process.read_longlong(goal_target_array_address + 0x20)

        active_target_array_address: int = self.process.read_longlong(goal_skate_address + 0x178)
        active_target_pointers: List[int] = list()

        i: int
        for i in range(active_target_count):
            active_target_pointers.append(self.process.read_longlong(active_target_array_address + (i * 0x8)))

        return {
            "S": letter_s_pointer not in active_target_pointers or letters_found_count == 5,
            "K": letter_k_pointer not in active_target_pointers or letters_found_count == 5,
            "A": letter_a_pointer not in active_target_pointers or letters_found_count == 5,
            "T": letter_t_pointer not in active_target_pointers or letters_found_count == 5,
            "E": letter_e_pointer not in active_target_pointers or letters_found_count == 5,
        }

    # Goal Level Manager address needs to be found in GObjects once when loading / restarting a level first
    def get_collected_secret_tape(self, goal_level_manager_address: int) -> Optional[bool]:
        if not self.is_process_still_running():
            return None

        # Check if the level is in Speed Run mode
        if self.process.read_int(goal_level_manager_address + 0x438) != 10:
            return None

        goal_secret_tape_address: int = self.process.read_longlong(goal_level_manager_address + 0x278)

        goal_target_count: int = self.process.read_int(goal_secret_tape_address + 0x170)
        active_target_count: int = self.process.read_int(goal_secret_tape_address + 0x180)

        if goal_target_count != 1 or active_target_count not in (0, 1):
            return None

        return active_target_count == 0

    def get_game_variable_as_int(self, game_variable_name: str, skater_internal_name: str) -> Optional[int]:
        if not self.is_process_still_running():
            return None

        if self.get_game_variable_as_int_function_address is None:
            return None

        game_variable_id: int = self.gnames_mapping_reverse.get(game_variable_name)
        skater_tag_id: int = self.gnames_mapping_reverse.get(skater_internal_name)

        if game_variable_id is None or skater_tag_id is None:
            return None

        args_bytes: bytes = struct.pack(
            "=IIIIQI",
            game_variable_id,
            0,
            skater_tag_id,
            0,
            0,
            0,
        )

        return self._call_process_event(
            self.game_variable_system_address,
            self.get_game_variable_as_int_function_address,
            args_bytes,
            0x18,
            "int"
        )

    def get_landed_special_counts(self, skaters: List[TonyHawksProSkater12Skaters],) -> Optional[
        Dict[TonyHawksProSkater12Skaters, Dict[TonyHawksProSkater12Specials, int]]
    ]:
        landed_special_counts: Dict[TonyHawksProSkater12Skaters, Dict[TonyHawksProSkater12Specials, int]] = dict()

        skater: TonyHawksProSkater12Skaters
        for skater in skaters:
            landed_special_counts[skater] = dict()

            specials: List[TonyHawksProSkater12Specials] = skater_to_specials[skater]

            special: TonyHawksProSkater12Specials
            for special in specials:
                landed_count: int = self.get_game_variable_as_int(
                    special_to_game_variable_name[special],
                    skater_to_internal_names[skater],
                )

                landed_special_counts[skater][special] = landed_count

        return landed_special_counts

    def update_sandbox_modifier_value(self, skater: TonyHawksProSkater12Skaters, modifier_key: str, value: float) -> bool:
        if skater not in self.sandbox_modifier_states:
            self.sandbox_modifier_states[skater] = self.default_sandbox_modifiers.copy()

        if modifier_key not in self.sandbox_modifier_states[skater]:
            return False
        elif self.sandbox_modifier_states[skater][modifier_key] == value:
            return False

        self.sandbox_modifier_states[skater][modifier_key] = value

        return True

    def enable_low_gravity(self, skater: TonyHawksProSkater12Skaters) -> bool:
        return self.update_sandbox_modifier_value(skater, "SBXStat.AirGravity", 0.4)

    def enable_high_gravity(self, skater: TonyHawksProSkater12Skaters) -> bool:
        return self.update_sandbox_modifier_value(skater, "SBXStat.AirGravity", 2.0)

    def reset_gravity(self, skater: TonyHawksProSkater12Skaters) -> bool:
        return self.update_sandbox_modifier_value(skater, "SBXStat.AirGravity", 1.0)

    def enable_super_speed(self, skater: TonyHawksProSkater12Skaters) -> bool:
        return self.update_sandbox_modifier_value(skater, "SBXStat.MaxMoveSpeed", 10.0)

    def disable_super_speed(self, skater: TonyHawksProSkater12Skaters) -> bool:
        return self.update_sandbox_modifier_value(skater, "SBXStat.MaxMoveSpeed", 1.0)

    def enable_perfect_manual_balance(self, skater: TonyHawksProSkater12Skaters) -> bool:
        return self.update_sandbox_modifier_value(skater, "SBXStat.PerfectManualBalance", 1.0)

    def disable_perfect_manual_balance(self, skater: TonyHawksProSkater12Skaters) -> bool:
        return self.update_sandbox_modifier_value(skater, "SBXStat.PerfectManualBalance", 0.0)

    def enable_perfect_lip_balance(self, skater: TonyHawksProSkater12Skaters) -> bool:
        return self.update_sandbox_modifier_value(skater, "SBXStat.PerfectLipBalance", 1.0)

    def disable_perfect_lip_balance(self, skater: TonyHawksProSkater12Skaters) -> bool:
        return self.update_sandbox_modifier_value(skater, "SBXStat.PerfectLipBalance", 0.0)

    def enable_perfect_grind_balance(self, skater: TonyHawksProSkater12Skaters) -> bool:
        return self.update_sandbox_modifier_value(skater, "SBXStat.PerfectGrindBalance", 1.0)

    def disable_perfect_grind_balance(self, skater: TonyHawksProSkater12Skaters) -> bool:
        return self.update_sandbox_modifier_value(skater, "SBXStat.PerfectGrindBalance", 0.0)

    def enable_no_bails(self, skater: TonyHawksProSkater12Skaters) -> bool:
        return self.update_sandbox_modifier_value(skater, "SBXStat.NoBails", 1.0)

    def disable_no_bails(self, skater: TonyHawksProSkater12Skaters) -> bool:
        return self.update_sandbox_modifier_value(skater, "SBXStat.NoBails", 0.0)

    def enable_reverse_controls(self, skater: TonyHawksProSkater12Skaters) -> bool:
        return self.update_sandbox_modifier_value(skater, "SBXStat.MirrorLeftRightInputs", 1.0)

    def disable_reverse_controls(self, skater: TonyHawksProSkater12Skaters) -> bool:
        return self.update_sandbox_modifier_value(skater, "SBXStat.MirrorLeftRightInputs", 0.0)

    def enable_stance_switching(self, skater: TonyHawksProSkater12Skaters) -> bool:
        self.update_sandbox_modifier_value(skater, "SBXStat.DisableStanceSwitching", 0.0)
        return self.update_sandbox_modifier_value(skater, "SBXStat.DisableNollieStance", 0.0)

    def disable_stance_switching(self, skater: TonyHawksProSkater12Skaters) -> bool:
        self.update_sandbox_modifier_value(skater, "SBXStat.DisableStanceSwitching", 1.0)
        return self.update_sandbox_modifier_value(skater, "SBXStat.DisableNollieStance", 1.0)

    def enable_wallplants(self, skater: TonyHawksProSkater12Skaters) -> bool:
        return self.update_sandbox_modifier_value(skater, "SBXStat.DisableWallplants", 0.0)

    def disable_wallplants(self, skater: TonyHawksProSkater12Skaters) -> bool:
        return self.update_sandbox_modifier_value(skater, "SBXStat.DisableWallplants", 1.0)

    def enable_always_special(self, skater: TonyHawksProSkater12Skaters) -> bool:
        return self.update_sandbox_modifier_value(skater, "SBXStat.Score.AlwaysSpecial", 1.0)

    def disable_always_special(self, skater: TonyHawksProSkater12Skaters) -> bool:
        return self.update_sandbox_modifier_value(skater, "SBXStat.Score.AlwaysSpecial", 0.0)

    def enable_double_base_score(self, skater: TonyHawksProSkater12Skaters) -> bool:
        return self.update_sandbox_modifier_value(skater, "SBXStat.Score.DoubleBaseScore", 1.0)

    def disable_double_base_score(self, skater: TonyHawksProSkater12Skaters) -> bool:
        return self.update_sandbox_modifier_value(skater, "SBXStat.Score.DoubleBaseScore", 0.0)

    def enable_flip_trick_points(self, skater: TonyHawksProSkater12Skaters) -> bool:
        return self.update_sandbox_modifier_value(skater, "SBXStat.Score.NoFlipTrickPoints", 0.0)

    def disable_flip_trick_points(self, skater: TonyHawksProSkater12Skaters) -> bool:
        return self.update_sandbox_modifier_value(skater, "SBXStat.Score.NoFlipTrickPoints", 1.0)

    def enable_grab_trick_points(self, skater: TonyHawksProSkater12Skaters) -> bool:
        return self.update_sandbox_modifier_value(skater, "SBXStat.Score.NoGrabTrickPoints", 0.0)

    def disable_grab_trick_points(self, skater: TonyHawksProSkater12Skaters) -> bool:
        return self.update_sandbox_modifier_value(skater, "SBXStat.Score.NoGrabTrickPoints", 1.0)

    def enable_grind_trick_points(self, skater: TonyHawksProSkater12Skaters) -> bool:
        return self.update_sandbox_modifier_value(skater, "SBXStat.Score.NoGrindTrickPoints", 0.0)

    def disable_grind_trick_points(self, skater: TonyHawksProSkater12Skaters) -> bool:
        return self.update_sandbox_modifier_value(skater, "SBXStat.Score.NoGrindTrickPoints", 1.0)

    def enable_lip_trick_points(self, skater: TonyHawksProSkater12Skaters) -> bool:
        return self.update_sandbox_modifier_value(skater, "SBXStat.Score.NoLipTrickPoints", 0.0)

    def disable_lip_trick_points(self, skater: TonyHawksProSkater12Skaters) -> bool:
        return self.update_sandbox_modifier_value(skater, "SBXStat.Score.NoLipTrickPoints", 1.0)

    def enable_special_meter(self, skater: TonyHawksProSkater12Skaters) -> bool:
        return self.update_sandbox_modifier_value(skater, "SBXStat.Score.NoSpecialMeter", 0.0)

    def disable_special_meter(self, skater: TonyHawksProSkater12Skaters) -> bool:
        return self.update_sandbox_modifier_value(skater, "SBXStat.Score.NoSpecialMeter", 1.0)

    def enable_spin_multiplier(self, skater: TonyHawksProSkater12Skaters) -> bool:
        return self.update_sandbox_modifier_value(skater, "SBXStat.Score.NoSpinMultiplier", 0.0)

    def disable_spin_multiplier(self, skater: TonyHawksProSkater12Skaters) -> bool:
        return self.update_sandbox_modifier_value(skater, "SBXStat.Score.NoSpinMultiplier", 1.0)

    def enable_sustain_trick_points(self, skater: TonyHawksProSkater12Skaters) -> bool:
        return self.update_sandbox_modifier_value(skater, "SBXStat.Score.NoSustainTrickPoints", 0.0)

    def disable_sustain_trick_points(self, skater: TonyHawksProSkater12Skaters) -> bool:
        return self.update_sandbox_modifier_value(skater, "SBXStat.Score.NoSustainTrickPoints", 1.0)

    def enable_max_stats(self, skater: TonyHawksProSkater12Skaters) -> bool:
        return self.update_sandbox_modifier_value(skater, "SBXStat.MaxHandlingStats", 1.0)

    def disable_max_stats(self, skater: TonyHawksProSkater12Skaters) -> bool:
        return self.update_sandbox_modifier_value(skater, "SBXStat.MaxHandlingStats", 0.0)

    def enable_min_stats(self, skater: TonyHawksProSkater12Skaters) -> bool:
        return self.update_sandbox_modifier_value(skater, "SBXStat.MinHandlingStats", 1.0)

    def disable_min_stats(self, skater: TonyHawksProSkater12Skaters) -> bool:
        return self.update_sandbox_modifier_value(skater, "SBXStat.MinHandlingStats", 0.0)

    def enable_extra_tricks(self, skater: TonyHawksProSkater12Skaters) -> bool:
        return self.update_sandbox_modifier_value(skater, "SBXStat.DisableExtraTricks", 0.0)

    def disable_extra_tricks(self, skater: TonyHawksProSkater12Skaters) -> bool:
        return self.update_sandbox_modifier_value(skater, "SBXStat.DisableExtraTricks", 1.0)

    def enable_transfers(self, skater: TonyHawksProSkater12Skaters) -> bool:
        return self.update_sandbox_modifier_value(skater, "SBXStat.DisableTransfers", 0.0)

    def disable_transfers(self, skater: TonyHawksProSkater12Skaters) -> bool:
        return self.update_sandbox_modifier_value(skater, "SBXStat.DisableTransfers", 1.0)

    def enable_manuals(self, skater: TonyHawksProSkater12Skaters) -> bool:
        return self.update_sandbox_modifier_value(skater, "SBXStat.DisableManuals", 0.0)

    def disable_manuals(self, skater: TonyHawksProSkater12Skaters) -> bool:
        return self.update_sandbox_modifier_value(skater, "SBXStat.DisableManuals", 1.0)

    def prepare_sandbox_modifier_bytes(self, skater: TonyHawksProSkater12Skaters) -> bytes:
        sandbox_modifier_bytes: bytearray = bytearray()

        tag_name: str
        value: float
        for tag_name, value in self.sandbox_modifier_states[skater].items():
            tag_index: int = self.gnames_mapping_reverse.get(tag_name, 0)

            if tag_index == 0:
                continue

            sandbox_modifier_bytes += struct.pack("<iif", tag_index, 0, float(value))

        return bytes(sandbox_modifier_bytes)

    def inject_sandbox_modifiers(self, skater: TonyHawksProSkater12Skaters) -> bool:
        if not self.is_process_still_running():
            return False

        sandbox_modifier_bytes: bytes = self.prepare_sandbox_modifier_bytes(skater)

        byte_count: int = len(sandbox_modifier_bytes)
        element_count: int = byte_count // 12

        allocation_address: int = self._call_malloc(byte_count)

        if allocation_address == 0:
            return False

        self.process.write_bytes(allocation_address, sandbox_modifier_bytes, byte_count)

        self.process.write_longlong(self.sandbox_stats_address + 0x0, allocation_address)
        self.process.write_int(self.sandbox_stats_address + 0x8, element_count)
        self.process.write_int(self.sandbox_stats_address + 0xC, element_count)

        return True

    def enable_mobile_game_trap(self) -> bool:
        if not self.is_process_still_running():
            return False

        if self.camera_component_address in (None, 0):
            return False

        aspect_ratio_address: int = self.camera_component_address + 0x200
        constraint_aspect_ratio_address: int = self.camera_component_address + 0x204

        self.process.write_float(aspect_ratio_address, 0.5)

        bitfield_value: int = self.process.read_int(constraint_aspect_ratio_address)
        bitfield_value |= 0x1

        self.process.write_int(constraint_aspect_ratio_address, bitfield_value)

        return True

    def disable_mobile_game_trap(self) -> bool:
        if not self.is_process_still_running():
            return False

        if self.camera_component_address in (None, 0):
            return False

        aspect_ratio_address: int = self.camera_component_address + 0x200
        constraint_aspect_ratio_address: int = self.camera_component_address + 0x204

        self.process.write_float(aspect_ratio_address, 1.777)

        bitfield_value: int = self.process.read_int(constraint_aspect_ratio_address)
        bitfield_value &= ~0x1

        self.process.write_int(constraint_aspect_ratio_address, bitfield_value)

        return True

    def enable_tunnel_vision_trap(self) -> bool:
        if not self.is_process_still_running():
            return False

        if self.camera_component_address in (None, 0):
            return False

        override_vignette_intensity_address: int = self.camera_component_address + 0x27B
        vignette_intensity_address: int = self.camera_component_address + 0x660

        bitfield_value: int = self.process.read_int(override_vignette_intensity_address)
        bitfield_value |= 0x80

        self.process.write_int(override_vignette_intensity_address, bitfield_value)

        self.process.write_float(vignette_intensity_address, 7.0)

        return True

    def disable_tunnel_vision_trap(self) -> bool:
        if not self.is_process_still_running():
            return False

        if self.camera_component_address in (None, 0):
            return False

        override_vignette_intensity_address: int = self.camera_component_address + 0x27B
        vignette_intensity_address: int = self.camera_component_address + 0x660

        bitfield_value: int = self.process.read_int(override_vignette_intensity_address)
        bitfield_value &= ~0x80

        self.process.write_int(override_vignette_intensity_address, bitfield_value)

        self.process.write_float(vignette_intensity_address, 0.4)

        return True

    def enable_color_inversion_trap(self) -> bool:
        if not self.is_process_still_running():
            return False

        if self.camera_component_address in (None, 0):
            return False

        override_color_saturation_address: int = self.camera_component_address + 0x270
        color_saturation_base_address: int = self.camera_component_address + 0x2B0

        bitfield_value: int = self.process.read_int(override_color_saturation_address)
        bitfield_value |= 0x4

        self.process.write_int(override_color_saturation_address, bitfield_value)

        self.process.write_float(color_saturation_base_address, -1.0)
        self.process.write_float(color_saturation_base_address + 0x4, -1.0)
        self.process.write_float(color_saturation_base_address + 0x8, -1.0)

        return True

    def disable_color_inversion_trap(self) -> bool:
        if not self.is_process_still_running():
            return False

        if self.camera_component_address in (None, 0):
            return False

        override_color_saturation_address: int = self.camera_component_address + 0x270
        color_saturation_base_address: int = self.camera_component_address + 0x2B0

        bitfield_value: int = self.process.read_int(override_color_saturation_address)
        bitfield_value &= ~0x4

        self.process.write_int(override_color_saturation_address, bitfield_value)

        self.process.write_float(color_saturation_base_address, 1.0)
        self.process.write_float(color_saturation_base_address + 0x4, 1.0)
        self.process.write_float(color_saturation_base_address + 0x8, 1.0)

        return True

    def enable_chromatic_trap(self) -> bool:
        if not self.is_process_still_running():
            return False

        if self.camera_component_address in (None, 0):
            return False

        override_color_saturation_address: int = self.camera_component_address + 0x270
        color_saturation_base_address: int = self.camera_component_address + 0x2B0

        bitfield_value: int = self.process.read_int(override_color_saturation_address)
        bitfield_value |= 0x4

        self.process.write_int(override_color_saturation_address, bitfield_value)

        self.process.write_float(color_saturation_base_address + 0xC, 18.0)

        return True

    def disable_chromatic_trap(self) -> bool:
        if not self.is_process_still_running():
            return False

        if self.camera_component_address in (None, 0):
            return False

        override_color_saturation_address: int = self.camera_component_address + 0x270
        color_saturation_base_address: int = self.camera_component_address + 0x2B0

        bitfield_value: int = self.process.read_int(override_color_saturation_address)
        bitfield_value &= ~0x4

        self.process.write_int(override_color_saturation_address, bitfield_value)

        self.process.write_float(color_saturation_base_address + 0xC, 1.0)

        return True

    def enable_black_and_white_trap(self) -> bool:
        if not self.is_process_still_running():
            return False

        if self.camera_component_address in (None, 0):
            return False

        override_color_saturation_address: int = self.camera_component_address + 0x270
        color_saturation_base_address: int = self.camera_component_address + 0x2B0
        color_contrast_base_address: int = self.camera_component_address + 0x2C0

        bitfield_value: int = self.process.read_int(override_color_saturation_address)

        bitfield_value |= 0x4
        bitfield_value |= 0x8

        self.process.write_int(override_color_saturation_address, bitfield_value)

        self.process.write_float(color_saturation_base_address + 0xC, 0.0)
        self.process.write_float(color_contrast_base_address + 0xC, 20.0)

        return True

    def disable_black_and_white_trap(self) -> bool:
        if not self.is_process_still_running():
            return False

        if self.camera_component_address in (None, 0):
            return False

        override_color_saturation_address: int = self.camera_component_address + 0x270
        color_saturation_base_address: int = self.camera_component_address + 0x2B0
        color_contrast_base_address: int = self.camera_component_address + 0x2C0

        bitfield_value: int = self.process.read_int(override_color_saturation_address)

        bitfield_value &= ~0x4
        bitfield_value &= ~0x8

        self.process.write_int(override_color_saturation_address, bitfield_value)

        self.process.write_float(color_saturation_base_address + 0xC, 1.0)
        self.process.write_float(color_contrast_base_address + 0xC, 1.0)

        return True

    def enable_bloom_trap(self) -> bool:
        if not self.is_process_still_running():
            return False

        if self.camera_component_address in (None, 0):
            return False

        override_color_gain_address: int = self.camera_component_address + 0x270
        override_bloom_intensity_address: int = self.camera_component_address + 0x276

        color_gain_base_address: int = self.camera_component_address + 0x2E0
        bloom_intensity_address: int = self.camera_component_address + 0x498

        bitfield_value: int = self.process.read_int(override_color_gain_address)
        bitfield_value |= 0x20

        self.process.write_int(override_color_gain_address, bitfield_value)

        bitfield_value: int = self.process.read_int(override_bloom_intensity_address)
        bitfield_value |= 0x2

        self.process.write_int(override_bloom_intensity_address, bitfield_value)

        self.process.write_float(color_gain_base_address + 0xC, 10.0)
        self.process.write_float(bloom_intensity_address, 8.0)

        return True

    def disable_bloom_trap(self) -> bool:
        if not self.is_process_still_running():
            return False

        if self.camera_component_address in (None, 0):
            return False

        override_color_gain_address: int = self.camera_component_address + 0x270
        override_bloom_intensity_address: int = self.camera_component_address + 0x276

        color_gain_base_address: int = self.camera_component_address + 0x2E0
        bloom_intensity_address: int = self.camera_component_address + 0x498

        bitfield_value: int = self.process.read_int(override_color_gain_address)
        bitfield_value &= ~0x20

        self.process.write_int(override_color_gain_address, bitfield_value)

        bitfield_value: int = self.process.read_int(override_bloom_intensity_address)
        bitfield_value &= ~0x2

        self.process.write_int(override_bloom_intensity_address, bitfield_value)

        self.process.write_float(color_gain_base_address + 0xC, 1.0)
        self.process.write_float(bloom_intensity_address, 0.675)

        return True

    def enable_retro_trap(self) -> bool:
        if not self.is_process_still_running():
            return False

        if self.camera_component_address in (None, 0):
            return False

        override_screen_percentage_address: int = self.camera_component_address + 0x290
        screen_percentage_address: int = self.camera_component_address + 0x790

        bitfield_value: int = self.process.read_int(override_screen_percentage_address)
        bitfield_value |= 0x10

        self.process.write_int(override_screen_percentage_address, bitfield_value)

        self.process.write_float(screen_percentage_address, 5.0)

        return True

    def disable_retro_trap(self) -> bool:
        if not self.is_process_still_running():
            return False

        if self.camera_component_address in (None, 0):
            return False

        override_screen_percentage_address: int = self.camera_component_address + 0x290
        screen_percentage_address: int = self.camera_component_address + 0x790

        bitfield_value: int = self.process.read_int(override_screen_percentage_address)
        bitfield_value &= ~0x10

        self.process.write_int(override_screen_percentage_address, bitfield_value)

        self.process.write_float(screen_percentage_address, 100.0)

        return True

    def enable_low_gravity_trap(self, skater: TonyHawksProSkater12Skaters) -> bool:
        if not self.is_process_still_running():
            return False

        self.enable_low_gravity(skater)

        return True

    def disable_low_gravity_trap(self, skater: TonyHawksProSkater12Skaters) -> bool:
        if not self.is_process_still_running():
            return False

        self.reset_gravity(skater)

        return True

    def enable_high_gravity_trap(self, skater: TonyHawksProSkater12Skaters) -> bool:
        if not self.is_process_still_running():
            return False

        self.enable_high_gravity(skater)

        return True

    def disable_high_gravity_trap(self, skater: TonyHawksProSkater12Skaters) -> bool:
        if not self.is_process_still_running():
            return False

        self.reset_gravity(skater)

        return True

    def enable_super_speed_trap(self, skater: TonyHawksProSkater12Skaters) -> bool:
        if not self.is_process_still_running():
            return False

        self.enable_super_speed(skater)

        return True

    def disable_super_speed_trap(self, skater: TonyHawksProSkater12Skaters) -> bool:
        if not self.is_process_still_running():
            return False

        self.disable_super_speed(skater)

        return True

    def enable_reverse_directional_controls_trap(self, skater: TonyHawksProSkater12Skaters) -> bool:
        if not self.is_process_still_running():
            return False

        self.enable_reverse_controls(skater)

        return True

    def disable_reverse_directional_controls_trap(self, skater: TonyHawksProSkater12Skaters) -> bool:
        if not self.is_process_still_running():
            return False

        self.disable_reverse_controls(skater)

        return True

    def enable_tiny_trap(self) -> bool:
        if not self.is_process_still_running():
            return False

        if self.skeletal_mesh_component_address in (None, 0):
            return False

        self.process.write_float(self.skeletal_mesh_component_address + 0x134, 0.2)
        self.process.write_float(self.skeletal_mesh_component_address + 0x138, 0.2)
        self.process.write_float(self.skeletal_mesh_component_address + 0x13C, 0.2)

        return True

    def enable_giant_trap(self) -> bool:
        if not self.is_process_still_running():
            return False

        if self.skeletal_mesh_component_address in (None, 0):
            return False

        self.process.write_float(self.skeletal_mesh_component_address + 0x134, 3.0)
        self.process.write_float(self.skeletal_mesh_component_address + 0x138, 3.0)
        self.process.write_float(self.skeletal_mesh_component_address + 0x13C, 3.0)

        return True

    def enable_wide_trap(self) -> bool:
        if not self.is_process_still_running():
            return False

        if self.skeletal_mesh_component_address in (None, 0):
            return False

        self.process.write_float(self.skeletal_mesh_component_address + 0x134, 10.0)

        return True

    def disable_size_traps(self) -> bool:
        if not self.is_process_still_running():
            return False

        if self.skeletal_mesh_component_address in (None, 0):
            return False

        self.process.write_float(self.skeletal_mesh_component_address + 0x134, 1.0)
        self.process.write_float(self.skeletal_mesh_component_address + 0x138, 1.0)
        self.process.write_float(self.skeletal_mesh_component_address + 0x13C, 1.0)

        return True

    def _generate_gnames_mapping(self) -> None:
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
                    name: str = chunk_data[start:end].decode("utf-16", errors="ignore")
                    entry_size: int = 2 + (length * 2)
                else:
                    end: int = start + length
                    name: str = chunk_data[start:end].decode("utf-8", errors="ignore")
                    entry_size: int = 2 + length

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

                        object_flags, _, class_pointer, name_index, name_number, outer_pointer = struct.unpack(
                            "<IIQIIQ", header_bytes)

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

    def _call_process_event(
        self,
        instance_address: int,
        function_object_address: int,
        args_bytes: bytes,
        result_offset: int,
        result_type: str
    ):
        args_address = None

        if args_bytes is not None:
            args_address = self.process.allocate(len(args_bytes))
            self.process.write_bytes(args_address, args_bytes, len(args_bytes))

        process_event_address = self.process.base_address + 0xC1F360

        shellcode = b"\x48\x83\xEC\x38"  # sub rsp, 38h
        shellcode += b"\x48\xB9" + struct.pack("<Q", instance_address)  # mov rcx, instance_address
        shellcode += b"\x48\xBA" + struct.pack("<Q", function_object_address)  # mov rdx, function_object_address

        # mov r8, args_address (if applicable)
        if args_bytes is not None:
            shellcode += b"\x49\xB8" + struct.pack("<Q", args_address)
        else:
            shellcode += b"\x4D\x31\xC0"

        shellcode += b"\x48\xB8" + struct.pack("<Q", process_event_address)  # mov rax, process_event_address

        shellcode += b"\xFF\xD0"  # call rax
        shellcode += b"\x48\x83\xC4\x38"  # add rsp, 38h
        shellcode += b"\xC3"  # ret

        execution_address = self.process.allocate(len(shellcode))
        self.process.write_bytes(execution_address, shellcode, len(shellcode))

        thread_handle = self.process.start_thread(execution_address)
        ctypes.windll.kernel32.WaitForSingleObject(thread_handle, -1)

        result = True

        if args_bytes is not None and result_offset is not None:
            if result_type == "bool":
                result = self.process.read_bool(args_address + result_offset)
            elif result_type == "int":
                result = self.process.read_int(args_address + result_offset)
            elif result_type == "float":
                result = self.process.read_float(args_address + result_offset)

        self.process.free(execution_address)

        if args_bytes is not None:
            self.process.free(args_address)

        ctypes.windll.kernel32.CloseHandle(thread_handle)

        return result

    def _call_malloc(self, allocation_size: int, alignment: int = 0x10) -> int:
        gmalloc_address: int = self.process.read_longlong(self.process.base_address + self.gmalloc_offset)
        vtable_address: int = self.process.read_longlong(gmalloc_address)
        malloc_internal_address: int = self.process.read_longlong(vtable_address + 0x18)

        result_buffer: int = self.process.allocate(8)

        shellcode: bytes = b""

        shellcode += b"\x55"  # push rbp
        shellcode += b"\x48\x89\xE5"  # mov rbp, rsp
        shellcode += b"\x48\x83\xE4\xF0"  # and rsp, -16
        shellcode += b"\x48\x83\xEC\x30"  # sub rsp, 30h

        shellcode += b"\x48\xB9" + struct.pack("<Q", gmalloc_address)  # mov rcx, gmalloc_address
        shellcode += b"\x48\x31\xD2"  # xor rdx, rdx
        shellcode += b"\x49\xB8" + struct.pack("<Q", allocation_size)  # mov r8, allocation_size
        shellcode += b"\x49\xC7\xC1" + struct.pack("<Q", alignment)  # mov r9, alignment

        shellcode += b"\x48\xB8" + struct.pack("<Q", malloc_internal_address)  # mov rax, malloc_internal_address
        shellcode += b"\xFF\xD0"  # call rax

        shellcode += b"\x48\xA3" + struct.pack("<Q", result_buffer)  # mov [result_buffer], rax

        shellcode += b"\x48\x89\xEC"  # mov rsp, rbp
        shellcode += b"\x5D"  # pop rbp
        shellcode += b"\xC3"  # ret

        execution_address: int = self.process.allocate(len(shellcode))

        self.process.write_bytes(execution_address, shellcode, len(shellcode))

        thread_handle = self.process.start_thread(execution_address)
        ctypes.windll.kernel32.WaitForSingleObject(thread_handle, -1)

        allocation_address: int = self.process.read_longlong(result_buffer)

        self.process.free(execution_address)
        self.process.free(result_buffer)

        ctypes.windll.kernel32.CloseHandle(thread_handle)

        return allocation_address

    def _resolve_address(self, base_offset: int, offsets: Tuple[int, ...]) -> Optional[int]:
        address: int = self.process.read_longlong(self.process.base_address + base_offset)

        for offset in offsets[:-1]:
            try:
                address = self.process.read_longlong(address + offset)
            except Exception:
                return None

        return address + offsets[-1]

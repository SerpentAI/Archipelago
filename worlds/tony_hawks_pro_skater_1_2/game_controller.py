from typing import Dict, List, Optional, Set, Tuple

import collections
import logging
import time

from .data.game_data import level_to_level_types

from .enums import (
    TonyHawksProSkater12APGoals,
    TonyHawksProSkater12APRequirementModes,
    TonyHawksProSkater12APTrapTypes,
    TonyHawksProSkater12Contexts,
    TonyHawksProSkater12Gaps,
    TonyHawksProSkater12Levels,
    TonyHawksProSkater12LevelTypes,
    TonyHawksProSkater12Skaters,
    TonyHawksProSkater12Specials,
)

from .game_state_manager import GameStateManager, GameState


class GameController:
    logger: Optional[logging.Logger]

    game_state_manager: GameStateManager

    received_items: Dict[str, int]
    completed_locations: Set[str]

    completed_locations_queue: collections.deque
    received_items_queue: collections.deque

    goal_completed: bool

    # Game State
    game_state_context: TonyHawksProSkater12Contexts
    game_state_are_injected_sandbox_modifiers_present: Optional[bool]
    game_state_level: Optional[TonyHawksProSkater12Levels]
    game_state_skater: Optional[TonyHawksProSkater12Skaters]
    game_state_score: Optional[int]
    game_state_best_combo_score: Optional[int]
    game_state_longest_grind: Optional[float]
    game_state_longest_lip: Optional[float]
    game_state_longest_manual: Optional[float]

    # Generation Options
    option_goal: Optional[TonyHawksProSkater12APGoals]
    option_secret_tapes_total: Optional[int]
    option_secret_tapes_required: Optional[int]
    option_skater_selection: Optional[Dict[TonyHawksProSkater12Skaters, bool]]
    option_skater_count: Optional[int]
    option_level_count: Optional[int]
    option_exclude_chopper_drop: Optional[bool]
    option_exclude_skate_heaven: Optional[bool]
    option_include_platinum_scores: Optional[bool]
    option_include_platinum_combo_scores: Optional[bool]
    option_include_signature_specials: Optional[bool]
    option_include_gaps: Optional[bool]
    option_gap_count_per_level: Optional[int]
    option_score_requirement_mode: Optional[TonyHawksProSkater12APRequirementModes]
    option_score_requirement_percentage: Optional[int]
    option_combo_score_requirement_mode: Optional[TonyHawksProSkater12APRequirementModes]
    option_combo_score_requirement_percentage: Optional[int]
    option_starting_trick_type_weights: Optional[Dict[str, int]]
    option_trap_percentage: Optional[int]
    option_trap_weights: Optional[Dict[TonyHawksProSkater12APTrapTypes, int]]

    # Generation Data
    selected_skaters: Optional[List[TonyHawksProSkater12Skaters]]
    selected_starting_skater: Optional[TonyHawksProSkater12Skaters]
    selected_levels: Optional[List[TonyHawksProSkater12Levels]]
    selected_starting_levels: Optional[List[TonyHawksProSkater12Levels]]
    selected_goal_level: Optional[TonyHawksProSkater12Levels]
    target_scores: Optional[Dict[TonyHawksProSkater12Levels, Dict[TonyHawksProSkater12Skaters, List[int]]]]
    target_combo_scores: Optional[Dict[TonyHawksProSkater12Levels, Dict[TonyHawksProSkater12Skaters, List[int]]]]
    target_gaps: Optional[Dict[TonyHawksProSkater12Levels, Dict[TonyHawksProSkater12Skaters, List[TonyHawksProSkater12Gaps]]]]
    target_long_tricks: Optional[Dict[TonyHawksProSkater12Levels, Dict[TonyHawksProSkater12Skaters, List[float]]]]
    starting_trick_types: Optional[Dict[TonyHawksProSkater12Skaters, str]]
    target_score_ratios: Optional[Dict[TonyHawksProSkater12Levels, Dict[TonyHawksProSkater12Skaters, float]]]
    target_combo_score_ratios: Optional[Dict[TonyHawksProSkater12Levels, Dict[TonyHawksProSkater12Skaters, float]]]

    # Data
    target_score_locations_by_level_skater: Optional[Dict[TonyHawksProSkater12Levels, Dict[TonyHawksProSkater12Skaters,  Dict[int, str]]]]
    target_combo_score_locations_by_level_skater: Optional[Dict[TonyHawksProSkater12Levels, Dict[TonyHawksProSkater12Skaters, Dict[int, str]]]]
    target_long_trick_locations_by_level_skater: Optional[Dict[TonyHawksProSkater12Levels, Dict[TonyHawksProSkater12Skaters, Dict[str, Tuple[int, str]]]]]
    target_gap_locations_by_level_skater: Optional[Dict[TonyHawksProSkater12Levels, Dict[TonyHawksProSkater12Skaters, Dict[TonyHawksProSkater12Gaps, str]]]]

    gap_counts_by_level_skater: Optional[Dict[TonyHawksProSkater12Levels, Dict[TonyHawksProSkater12Skaters, Dict[TonyHawksProSkater12Gaps, int]]]]
    special_counts_by_skater: Optional[Dict[TonyHawksProSkater12Skaters, Dict[TonyHawksProSkater12Specials, int]]]

    goal_level_manager_address: Optional[int]

    # State
    should_perform_menu_routine: bool
    menu_routine_timestamp: Optional[int]

    should_prepare_processed_trap_counters: bool
    processed_trap_counters: Dict[TonyHawksProSkater12APTrapTypes, int]
    active_trap_timestamps: Dict[TonyHawksProSkater12APTrapTypes, Optional[int]]

    def __init__(self, logger: logging.Logger = None) -> None:
        self.logger = logger

        self.game_state_manager = GameStateManager()

        self.received_items = dict()
        self.completed_locations = set()

        self.completed_locations_queue = collections.deque()
        self.received_items_queue = collections.deque()

        self.goal_completed = False

        self.game_state_context = None
        self.game_state_are_injected_sandbox_modifiers_present = None
        self.game_state_level = None
        self.game_state_skater = None
        self.game_state_score = None
        self.game_state_best_combo_score = None
        self.game_state_longest_grind = None
        self.game_state_longest_lip = None
        self.game_state_longest_manual = None

        self.option_goal = None
        self.option_secret_tapes_total = None
        self.option_secret_tapes_required = None
        self.option_skater_selection = None
        self.option_skater_count = None
        self.option_level_count = None
        self.option_exclude_chopper_drop = None
        self.option_exclude_skate_heaven = None
        self.option_include_platinum_scores = None
        self.option_include_platinum_combo_scores = None
        self.option_include_signature_specials = None
        self.option_include_gaps = None
        self.option_gap_count_per_level = None
        self.option_score_requirement_mode = None
        self.option_score_requirement_percentage = None
        self.option_combo_score_requirement_mode = None
        self.option_combo_score_requirement_percentage = None
        self.option_starting_trick_type_weights = None
        self.option_trap_percentage = None
        self.option_trap_weights = None

        self.selected_skaters = None
        self.selected_starting_skater = None
        self.selected_levels = None
        self.selected_starting_levels = None
        self.selected_goal_level = None
        self.target_scores = None
        self.target_combo_scores = None
        self.target_gaps = None
        self.target_long_tricks = None
        self.starting_trick_types = None
        self.target_score_ratios = None

        self.target_score_locations_by_level_skater = None
        self.target_combo_score_locations_by_level_skater = None
        self.target_long_trick_locations_by_level_skater = None
        self.target_gap_locations_by_level_skater = None

        self.gap_counts_by_level_skater = None
        self.special_counts_by_skater = None

        self.goal_level_manager_address = None

        self.should_perform_menu_routine = True
        self.menu_routine_timestamp = None

        self.should_prepare_processed_trap_counters = True

        self.processed_trap_counters = {
            TonyHawksProSkater12APTrapTypes.BLACK_AND_WHITE: 0,
            TonyHawksProSkater12APTrapTypes.BLOOM: 0,
            TonyHawksProSkater12APTrapTypes.CHROMATIC: 0,
            TonyHawksProSkater12APTrapTypes.COLOR_INVERSION: 0,
            TonyHawksProSkater12APTrapTypes.GIANT: 0,
            TonyHawksProSkater12APTrapTypes.HIGH_GRAVITY: 0,
            TonyHawksProSkater12APTrapTypes.LOW_GRAVITY: 0,
            TonyHawksProSkater12APTrapTypes.MOBILE_GAME: 0,
            TonyHawksProSkater12APTrapTypes.RETRO: 0,
            TonyHawksProSkater12APTrapTypes.REVERSE_DIRECTIONAL_CONTROLS: 0,
            TonyHawksProSkater12APTrapTypes.SUPER_SPEED: 0,
            TonyHawksProSkater12APTrapTypes.TINY: 0,
            TonyHawksProSkater12APTrapTypes.TUNNEL_VISION: 0,
            TonyHawksProSkater12APTrapTypes.WIDE: 0,
        }

        self.active_trap_timestamps = {
            TonyHawksProSkater12APTrapTypes.BLACK_AND_WHITE: None,
            TonyHawksProSkater12APTrapTypes.BLOOM: None,
            TonyHawksProSkater12APTrapTypes.CHROMATIC: None,
            TonyHawksProSkater12APTrapTypes.COLOR_INVERSION: None,
            TonyHawksProSkater12APTrapTypes.GIANT: None,
            TonyHawksProSkater12APTrapTypes.HIGH_GRAVITY: None,
            TonyHawksProSkater12APTrapTypes.LOW_GRAVITY: None,
            TonyHawksProSkater12APTrapTypes.MOBILE_GAME: None,
            TonyHawksProSkater12APTrapTypes.RETRO: None,
            TonyHawksProSkater12APTrapTypes.REVERSE_DIRECTIONAL_CONTROLS: None,
            TonyHawksProSkater12APTrapTypes.SUPER_SPEED: None,
            TonyHawksProSkater12APTrapTypes.TINY: None,
            TonyHawksProSkater12APTrapTypes.TUNNEL_VISION: None,
            TonyHawksProSkater12APTrapTypes.WIDE: None,
        }

    def log(self, message) -> None:
        if self.logger:
            self.logger.info(message)

    def log_debug(self, message) -> None:
        if self.logger:
            self.logger.debug(message)

    def open_process_handle(self) -> bool:
        return self.game_state_manager.open_process_handle()

    def close_process_handle(self) -> bool:
        return self.game_state_manager.close_process_handle()

    def is_process_running(self) -> bool:
        return self.game_state_manager.is_process_still_running()

    def assemble_target_score_locations(self) -> None:
        if self.target_scores is None:
            return

        locations: Dict[TonyHawksProSkater12Levels, Dict[TonyHawksProSkater12Skaters,  Dict[int, str]]] = dict()

        level: TonyHawksProSkater12Levels
        for level in self.selected_levels:
            locations[level] = dict()

            skater: TonyHawksProSkater12Skaters
            for skater in self.selected_skaters:
                locations[level][skater] = dict()

                locations[level][skater][self.target_scores[level][skater][0]] = f"{level.value} - {skater.value} - High Score"
                locations[level][skater][self.target_scores[level][skater][1]] = f"{level.value} - {skater.value} - Pro Score"
                locations[level][skater][self.target_scores[level][skater][2]] = f"{level.value} - {skater.value} - Sick Score"

                if self.option_include_platinum_scores:
                    locations[level][skater][self.target_scores[level][skater][3]] = f"{level.value} - {skater.value} - Platinum Score"

        self.target_score_locations_by_level_skater = locations

    def assemble_target_combo_score_locations(self) -> None:
        if self.target_combo_scores is None:
            return

        locations: Dict[TonyHawksProSkater12Levels, Dict[TonyHawksProSkater12Skaters, Dict[int, str]]] = dict()

        level: TonyHawksProSkater12Levels
        for level in self.selected_levels:
            locations[level] = dict()

            skater: TonyHawksProSkater12Skaters
            for skater in self.selected_skaters:
                locations[level][skater] = dict()

                locations[level][skater][self.target_combo_scores[level][skater][0]] = f"{level.value} - {skater.value} - High Combo"
                locations[level][skater][self.target_combo_scores[level][skater][1]] = f"{level.value} - {skater.value} - Pro Combo"
                locations[level][skater][self.target_combo_scores[level][skater][2]] = f"{level.value} - {skater.value} - Sick Combo"

                if self.option_include_platinum_combo_scores:
                    locations[level][skater][self.target_combo_scores[level][skater][3]] = f"{level.value} - {skater.value} - Platinum Combo"

        self.target_combo_score_locations_by_level_skater = locations

    def assemble_long_trick_locations(self) -> None:
        if self.target_long_tricks is None:
            return

        locations: Dict[TonyHawksProSkater12Levels, Dict[TonyHawksProSkater12Skaters, Dict[int, str]]] = dict()

        level: TonyHawksProSkater12Levels
        for level in self.selected_levels:
            locations[level] = dict()

            skater: TonyHawksProSkater12Skaters
            for skater in self.selected_skaters:
                locations[level][skater] = {
                    "grind": dict(),
                    "lip": dict(),
                    "manual": dict()
                }

                locations[level][skater]["grind"] = (int(self.target_long_tricks[level][skater][0] * 100), f"{level.value} - {skater.value} - Long Grind Trick")
                locations[level][skater]["lip"] = (int(self.target_long_tricks[level][skater][1] * 100), f"{level.value} - {skater.value} - Long Lip Trick")
                locations[level][skater]["manual"] = (int(self.target_long_tricks[level][skater][2] * 100), f"{level.value} - {skater.value} - Long Manual Trick")

        self.target_long_trick_locations_by_level_skater = locations

    def assemble_gap_locations(self) -> None:
        if self.target_gaps is None:
            return

        locations: Dict[TonyHawksProSkater12Levels, Dict[TonyHawksProSkater12Skaters, Dict[TonyHawksProSkater12Gaps, str]]] = dict()

        level: TonyHawksProSkater12Levels
        for level in self.selected_levels:
            locations[level] = dict()

            skater: TonyHawksProSkater12Skaters
            for skater in self.selected_skaters:
                locations[level][skater] = dict()

                i: int
                for i in range(len(self.target_gaps[level][skater])):
                    locations[level][skater][self.target_gaps[level][skater][i]] = f"{level.value} - {skater.value} - Gap #{i + 1}"

        self.target_gap_locations_by_level_skater = locations

    def update(self) -> None:
        if self.game_state_manager.is_process_still_running():
            try:
                self._refresh_game_state()

                if self.game_state_context == TonyHawksProSkater12Contexts.INVALID:
                    return

                self._apply_conditional_game_state()

                self._check_for_completed_locations()
                self._process_received_items()

                if (self.option_trap_percentage or 0) > 0:
                    self._manage_traps()

                self._check_for_victory()
            except Exception:
                import traceback

                with open("tony_hawks_pro_skater_1_2_errors.log", "a") as f:
                    f.write(traceback.format_exc() + "\n\n")

    def reset(self) -> None:
        self.received_items = dict()
        self.completed_locations = set()

        self.completed_locations_queue = collections.deque()
        self.received_items_queue = collections.deque()

        self.goal_completed = False

        self.game_state_context = None
        self.game_state_are_injected_sandbox_modifiers_present = None
        self.game_state_level = None
        self.game_state_skater = None
        self.game_state_score = None
        self.game_state_best_combo_score = None
        self.game_state_longest_grind = None
        self.game_state_longest_lip = None
        self.game_state_longest_manual = None

        self.option_goal = None
        self.option_secret_tapes_total = None
        self.option_secret_tapes_required = None
        self.option_skater_selection = None
        self.option_skater_count = None
        self.option_level_count = None
        self.option_exclude_chopper_drop = None
        self.option_exclude_skate_heaven = None
        self.option_include_platinum_scores = None
        self.option_include_platinum_combo_scores = None
        self.option_include_signature_specials = None
        self.option_include_gaps = None
        self.option_gap_count_per_level = None
        self.option_score_requirement_mode = None
        self.option_score_requirement_percentage = None
        self.option_combo_score_requirement_mode = None
        self.option_combo_score_requirement_percentage = None
        self.option_starting_trick_type_weights = None
        self.option_trap_percentage = None
        self.option_trap_weights = None

        self.selected_skaters = None
        self.selected_starting_skater = None
        self.selected_levels = None
        self.selected_starting_levels = None
        self.selected_goal_level = None
        self.target_scores = None
        self.target_combo_scores = None
        self.target_gaps = None
        self.target_long_tricks = None
        self.starting_trick_types = None
        self.target_score_ratios = None

        self.target_score_locations_by_level_skater = None
        self.target_combo_score_locations_by_level_skater = None
        self.target_long_trick_locations_by_level_skater = None
        self.target_gap_locations_by_level_skater = None

        self.gap_counts_by_level_skater = None
        self.special_counts_by_skater = None

        self.goal_level_manager_address = None

        self.should_perform_menu_routine = True
        self.menu_routine_timestamp = None

        self.should_prepare_processed_trap_counters = True

        self.processed_trap_counters = {
            TonyHawksProSkater12APTrapTypes.BLACK_AND_WHITE: 0,
            TonyHawksProSkater12APTrapTypes.BLOOM: 0,
            TonyHawksProSkater12APTrapTypes.CHROMATIC: 0,
            TonyHawksProSkater12APTrapTypes.COLOR_INVERSION: 0,
            TonyHawksProSkater12APTrapTypes.GIANT: 0,
            TonyHawksProSkater12APTrapTypes.HIGH_GRAVITY: 0,
            TonyHawksProSkater12APTrapTypes.LOW_GRAVITY: 0,
            TonyHawksProSkater12APTrapTypes.MOBILE_GAME: 0,
            TonyHawksProSkater12APTrapTypes.RETRO: 0,
            TonyHawksProSkater12APTrapTypes.REVERSE_DIRECTIONAL_CONTROLS: 0,
            TonyHawksProSkater12APTrapTypes.SUPER_SPEED: 0,
            TonyHawksProSkater12APTrapTypes.TINY: 0,
            TonyHawksProSkater12APTrapTypes.TUNNEL_VISION: 0,
            TonyHawksProSkater12APTrapTypes.WIDE: 0,
        }

        self.active_trap_timestamps = {
            TonyHawksProSkater12APTrapTypes.BLACK_AND_WHITE: None,
            TonyHawksProSkater12APTrapTypes.BLOOM: None,
            TonyHawksProSkater12APTrapTypes.CHROMATIC: None,
            TonyHawksProSkater12APTrapTypes.COLOR_INVERSION: None,
            TonyHawksProSkater12APTrapTypes.GIANT: None,
            TonyHawksProSkater12APTrapTypes.HIGH_GRAVITY: None,
            TonyHawksProSkater12APTrapTypes.LOW_GRAVITY: None,
            TonyHawksProSkater12APTrapTypes.MOBILE_GAME: None,
            TonyHawksProSkater12APTrapTypes.RETRO: None,
            TonyHawksProSkater12APTrapTypes.REVERSE_DIRECTIONAL_CONTROLS: None,
            TonyHawksProSkater12APTrapTypes.SUPER_SPEED: None,
            TonyHawksProSkater12APTrapTypes.TINY: None,
            TonyHawksProSkater12APTrapTypes.TUNNEL_VISION: None,
            TonyHawksProSkater12APTrapTypes.WIDE: None,
        }

    def _refresh_game_state(self) -> None:
        game_state: GameState = self.game_state_manager.determine_game_state()

        self.game_state_context = game_state.context
        self.game_state_are_injected_sandbox_modifiers_present = game_state.are_injected_sandbox_modifiers_present
        self.game_state_level = game_state.level
        self.game_state_skater = game_state.skater
        self.game_state_score = game_state.score
        self.game_state_best_combo_score = game_state.best_combo_score
        self.game_state_longest_grind = game_state.longest_grind
        self.game_state_longest_lip = game_state.longest_lip
        self.game_state_longest_manual = game_state.longest_manual

    def _apply_conditional_game_state(self) -> None:
        # Update Skater Sandbox Modifiers
        skater: TonyHawksProSkater12Skaters
        for skater in self.selected_skaters:
            self._update_skater_sandbox_modifiers(skater)

        if self.game_state_context == TonyHawksProSkater12Contexts.LEVEL and self.game_state_level is not None:
            if self.game_state_level in self.selected_levels or self.game_state_level in ([self.selected_goal_level] or list()):
                # Per-Skater Sandbox Modifiers
                if self.game_state_skater is not None and self.game_state_skater in self.selected_skaters:
                    skater_unlock_item_name = f"Skater Unlock: {self.game_state_skater.value}"
                    skater_unlock_item_count: int = self.received_items.get(skater_unlock_item_name, 0)

                    if skater_unlock_item_count >= 1:
                        if not self.game_state_are_injected_sandbox_modifiers_present:
                            self.game_state_manager.inject_sandbox_modifiers(self.game_state_skater)

                            self.goal_level_manager_address = None

                            if level_to_level_types[self.game_state_level] == TonyHawksProSkater12LevelTypes.OBJECTIVES:
                                while self.goal_level_manager_address in (None, 0):
                                    self.goal_level_manager_address = self.game_state_manager.find_goal_level_manager_address()

    def _check_for_completed_locations(self) -> None:
        checked_locations: List[str] = list()

        if self.game_state_context == TonyHawksProSkater12Contexts.MENU:
            if self.should_perform_menu_routine:
                if self.menu_routine_timestamp is None:
                    self.menu_routine_timestamp = int(time.time()) + 7

                if int(time.time()) >= self.menu_routine_timestamp:
                    self.menu_routine_timestamp = None
                    self.should_perform_menu_routine = False

                    if self.option_include_gaps:
                        checked_locations.extend(self._check_for_completed_gaps())

                    if self.option_include_signature_specials:
                        checked_locations.extend(self._check_for_completed_specials())
        elif self.game_state_context == TonyHawksProSkater12Contexts.LEVEL:
            self.should_perform_menu_routine = True

            if self.game_state_level is None or self.game_state_level not in self.selected_levels:
                return

            level_unlock_item: str = f"Level Unlock: {self.game_state_level.value}"
            level_unlock_item_count: int = self.received_items.get(level_unlock_item, 0)

            if level_unlock_item_count < 1:
                return

            if self.game_state_skater is None:
                return

            skater_unlock_item: str = f"Skater Unlock: {self.game_state_skater.value}"
            skater_unlock_item_count: int = self.received_items.get(skater_unlock_item, 0)

            if skater_unlock_item_count < 1:
                return

            # Scores
            if self.game_state_score is not None:
                target_score: int
                location_name: str
                for target_score, location_name in self.target_score_locations_by_level_skater[self.game_state_level][self.game_state_skater].items():
                    if self.game_state_score >= target_score:
                        checked_locations.append(location_name)

            # Combo Scores
            if self.game_state_best_combo_score is not None:
                target_combo_score: int
                location_name: str
                for target_combo_score, location_name in self.target_combo_score_locations_by_level_skater[self.game_state_level][self.game_state_skater].items():
                    if self.game_state_best_combo_score >= target_combo_score:
                        checked_locations.append(location_name)

            # Long Tricks
            if self.game_state_longest_grind is not None:
                progressive_grind_tricks_name: str = f"Progressive Grind Tricks: {self.game_state_skater.value}"
                progressive_grind_tricks_count: int = self.received_items.get(progressive_grind_tricks_name, 0)

                if progressive_grind_tricks_count > 0:
                    if int(self.game_state_longest_grind * 100) > self.target_long_trick_locations_by_level_skater[self.game_state_level][self.game_state_skater]["grind"][0]:
                        checked_locations.append(self.target_long_trick_locations_by_level_skater[self.game_state_level][self.game_state_skater]["grind"][1])

            if self.game_state_longest_lip is not None:
                progressive_lip_tricks_name: str = f"Progressive Lip Tricks: {self.game_state_skater.value}"
                progressive_lip_tricks_count: int = self.received_items.get(progressive_lip_tricks_name, 0)

                if progressive_lip_tricks_count > 0:
                    if int(self.game_state_longest_lip * 100) > self.target_long_trick_locations_by_level_skater[self.game_state_level][self.game_state_skater]["lip"][0]:
                        checked_locations.append(self.target_long_trick_locations_by_level_skater[self.game_state_level][self.game_state_skater]["lip"][1])

            if self.game_state_longest_manual is not None:
                progressive_manual_tricks_name: str = f"Progressive Manual Tricks: {self.game_state_skater.value}"
                progressive_manual_tricks_count: int = self.received_items.get(progressive_manual_tricks_name, 0)

                if progressive_manual_tricks_count > 0:
                    if int(self.game_state_longest_manual * 100) > self.target_long_trick_locations_by_level_skater[self.game_state_level][self.game_state_skater]["manual"][0]:
                        checked_locations.append(self.target_long_trick_locations_by_level_skater[self.game_state_level][self.game_state_skater]["manual"][1])

            # Collectibles
            if level_to_level_types[self.game_state_level] == TonyHawksProSkater12LevelTypes.OBJECTIVES:
                if self.goal_level_manager_address not in (None, 0):
                    # S-K-A-T-E
                    collected_skate_letters: Optional[Dict[str, bool]] = self.game_state_manager.get_collected_skate_letters(self.goal_level_manager_address)

                    if collected_skate_letters is not None:
                        letter: str
                        is_collected: bool
                        for letter, is_collected in collected_skate_letters.items():
                            if is_collected:
                                checked_locations.append(f"{self.game_state_level.value} - {self.game_state_skater.value} - SKATE Letter {letter}")

                    # Secret Tape
                    collected_secret_tape: Optional[bool] = self.game_state_manager.get_collected_secret_tape(self.goal_level_manager_address)

                    if collected_secret_tape is not None:
                        if collected_secret_tape:
                            checked_locations.append(f"{self.game_state_level.value} - {self.game_state_skater.value} - Secret Tape")

        location: str
        for location in checked_locations:
            if location not in self.completed_locations and location not in self.completed_locations_queue:
                self.completed_locations.add(location)
                self.completed_locations_queue.append(location)

    def _process_received_items(self) -> None:
        while len(self.received_items_queue) > 0:
            item: str = self.received_items_queue.popleft()

            if item not in self.received_items:
                self.received_items[item] = 0

            self.received_items[item] += 1

        if self.should_prepare_processed_trap_counters:
            self.should_prepare_processed_trap_counters = False

            item_name: str
            item_count: int
            for item_name, item_count in self.received_items.items():
                if item_name.endswith(" Trap"):
                    self.processed_trap_counters[TonyHawksProSkater12APTrapTypes(item_name)] = item_count

    def _manage_traps(self) -> None:
        if not self.game_state_context == TonyHawksProSkater12Contexts.LEVEL:
            return

        if self.game_state_level is None:
            return

        if self.game_state_level not in self.selected_levels + [self.selected_goal_level or list()]:
            return

        if self.game_state_skater is None:
            return

        if self.game_state_skater not in self.selected_skaters:
            return

        should_reinject_sandbox_modifiers: bool = False

        now_timestamp: int = int(time.time())

        trap_type: TonyHawksProSkater12APTrapTypes
        expiry_timestamp: int
        for trap_type, expiry_timestamp in self.active_trap_timestamps.items():
            if expiry_timestamp is not None:
                if now_timestamp >= expiry_timestamp:
                    if trap_type == TonyHawksProSkater12APTrapTypes.BLACK_AND_WHITE:
                        self.game_state_manager.disable_black_and_white_trap()
                    elif trap_type == TonyHawksProSkater12APTrapTypes.BLOOM:
                        self.game_state_manager.disable_bloom_trap()
                    elif trap_type == TonyHawksProSkater12APTrapTypes.CHROMATIC:
                        self.game_state_manager.disable_chromatic_trap()
                    elif trap_type == TonyHawksProSkater12APTrapTypes.COLOR_INVERSION:
                        self.game_state_manager.disable_color_inversion_trap()
                    elif trap_type == TonyHawksProSkater12APTrapTypes.GIANT:
                        self.game_state_manager.disable_size_traps()
                    elif trap_type == TonyHawksProSkater12APTrapTypes.HIGH_GRAVITY:
                        should_reinject_sandbox_modifiers = True

                        skater: TonyHawksProSkater12Skaters
                        for skater in self.selected_skaters:
                            self.game_state_manager.disable_high_gravity_trap(skater)
                    elif trap_type == TonyHawksProSkater12APTrapTypes.LOW_GRAVITY:
                        should_reinject_sandbox_modifiers = True

                        skater: TonyHawksProSkater12Skaters
                        for skater in self.selected_skaters:
                            self.game_state_manager.disable_low_gravity_trap(skater)
                    elif trap_type == TonyHawksProSkater12APTrapTypes.MOBILE_GAME:
                        self.game_state_manager.disable_mobile_game_trap()
                    elif trap_type == TonyHawksProSkater12APTrapTypes.RETRO:
                        self.game_state_manager.disable_retro_trap()
                    elif trap_type == TonyHawksProSkater12APTrapTypes.REVERSE_DIRECTIONAL_CONTROLS:
                        should_reinject_sandbox_modifiers = True

                        skater: TonyHawksProSkater12Skaters
                        for skater in self.selected_skaters:
                            self.game_state_manager.disable_reverse_directional_controls_trap(skater)
                    elif trap_type == TonyHawksProSkater12APTrapTypes.SUPER_SPEED:
                        should_reinject_sandbox_modifiers = True

                        skater: TonyHawksProSkater12Skaters
                        for skater in self.selected_skaters:
                            self.game_state_manager.disable_super_speed_trap(skater)
                    elif trap_type == TonyHawksProSkater12APTrapTypes.TINY:
                        self.game_state_manager.disable_size_traps()
                    elif trap_type == TonyHawksProSkater12APTrapTypes.TUNNEL_VISION:
                        self.game_state_manager.disable_tunnel_vision_trap()
                    elif trap_type == TonyHawksProSkater12APTrapTypes.WIDE:
                        self.game_state_manager.disable_size_traps()

                    self.active_trap_timestamps[trap_type] = None

        item_name: str
        item_count: int
        for item_name, item_count in self.received_items.items():
            if item_name.endswith(" Trap"):
                trap_type: TonyHawksProSkater12APTrapTypes = TonyHawksProSkater12APTrapTypes(item_name)

                if item_count > self.processed_trap_counters[trap_type]:
                    expiry_timestamp: int = int(time.time()) + 20

                    if trap_type == TonyHawksProSkater12APTrapTypes.BLACK_AND_WHITE:
                        if self.active_trap_timestamps[trap_type] is None:
                            if self.game_state_manager.enable_black_and_white_trap():
                                self.active_trap_timestamps[trap_type] = expiry_timestamp
                                self.processed_trap_counters[trap_type] = item_count
                    elif trap_type == TonyHawksProSkater12APTrapTypes.BLOOM:
                        if self.active_trap_timestamps[trap_type] is None:
                            if self.game_state_manager.enable_bloom_trap():
                                self.active_trap_timestamps[trap_type] = expiry_timestamp
                                self.processed_trap_counters[trap_type] = item_count
                    elif trap_type == TonyHawksProSkater12APTrapTypes.CHROMATIC:
                        if self.active_trap_timestamps[trap_type] is None:
                            if self.game_state_manager.enable_chromatic_trap():
                                self.active_trap_timestamps[trap_type] = expiry_timestamp
                                self.processed_trap_counters[trap_type] = item_count
                    elif trap_type == TonyHawksProSkater12APTrapTypes.COLOR_INVERSION:
                        if self.active_trap_timestamps[trap_type] is None:
                            if self.game_state_manager.enable_color_inversion_trap():
                                self.active_trap_timestamps[trap_type] = expiry_timestamp
                                self.processed_trap_counters[trap_type] = item_count
                    elif trap_type == TonyHawksProSkater12APTrapTypes.GIANT:
                        if self.active_trap_timestamps[trap_type] is None:
                            if self.game_state_manager.enable_giant_trap():
                                self.active_trap_timestamps[trap_type] = expiry_timestamp
                                self.processed_trap_counters[trap_type] = item_count
                    elif trap_type == TonyHawksProSkater12APTrapTypes.HIGH_GRAVITY:
                        if self.active_trap_timestamps[trap_type] is None:
                            if self.game_state_manager.enable_high_gravity_trap(self.game_state_skater):
                                should_reinject_sandbox_modifiers = True

                                self.active_trap_timestamps[trap_type] = expiry_timestamp
                                self.processed_trap_counters[trap_type] = item_count
                    elif trap_type == TonyHawksProSkater12APTrapTypes.LOW_GRAVITY:
                        if self.active_trap_timestamps[trap_type] is None:
                            if self.game_state_manager.enable_low_gravity_trap(self.game_state_skater):
                                should_reinject_sandbox_modifiers = True

                                self.active_trap_timestamps[trap_type] = expiry_timestamp
                                self.processed_trap_counters[trap_type] = item_count
                    elif trap_type == TonyHawksProSkater12APTrapTypes.MOBILE_GAME:
                        if self.active_trap_timestamps[trap_type] is None:
                            if self.game_state_manager.enable_mobile_game_trap():
                                self.active_trap_timestamps[trap_type] = expiry_timestamp
                                self.processed_trap_counters[trap_type] = item_count
                    elif trap_type == TonyHawksProSkater12APTrapTypes.RETRO:
                        if self.active_trap_timestamps[trap_type] is None:
                            if self.game_state_manager.enable_retro_trap():
                                self.active_trap_timestamps[trap_type] = expiry_timestamp
                                self.processed_trap_counters[trap_type] = item_count
                    elif trap_type == TonyHawksProSkater12APTrapTypes.REVERSE_DIRECTIONAL_CONTROLS:
                        if self.active_trap_timestamps[trap_type] is None:
                            if self.game_state_manager.enable_reverse_directional_controls_trap(self.game_state_skater):
                                should_reinject_sandbox_modifiers = True

                                self.active_trap_timestamps[trap_type] = expiry_timestamp
                                self.processed_trap_counters[trap_type] = item_count
                    elif trap_type == TonyHawksProSkater12APTrapTypes.SUPER_SPEED:
                        if self.active_trap_timestamps[trap_type] is None:
                            if self.game_state_manager.enable_super_speed_trap(self.game_state_skater):
                                should_reinject_sandbox_modifiers = True

                                self.active_trap_timestamps[trap_type] = expiry_timestamp
                                self.processed_trap_counters[trap_type] = item_count
                    elif trap_type == TonyHawksProSkater12APTrapTypes.TINY:
                        if self.active_trap_timestamps[trap_type] is None:
                            if self.game_state_manager.enable_tiny_trap():
                                self.active_trap_timestamps[trap_type] = expiry_timestamp
                                self.processed_trap_counters[trap_type] = item_count
                    elif trap_type == TonyHawksProSkater12APTrapTypes.TUNNEL_VISION:
                        if self.active_trap_timestamps[trap_type] is None:
                            if self.game_state_manager.enable_tunnel_vision_trap():
                                self.active_trap_timestamps[trap_type] = expiry_timestamp
                                self.processed_trap_counters[trap_type] = item_count
                    elif trap_type == TonyHawksProSkater12APTrapTypes.WIDE:
                        if self.active_trap_timestamps[trap_type] is None:
                            if self.game_state_manager.enable_wide_trap():
                                self.active_trap_timestamps[trap_type] = expiry_timestamp
                                self.processed_trap_counters[trap_type] = item_count

        if should_reinject_sandbox_modifiers:
            self.game_state_manager.inject_sandbox_modifiers(self.game_state_skater)

    def _check_for_victory(self) -> None:
        if "Secret Tape" in self.received_items:
            if self.received_items["Secret Tape"] >= self.option_secret_tapes_required:
                if self.option_goal == TonyHawksProSkater12APGoals.SECRET_TAPES_FINAL_LEVEL:
                    if self.game_state_level == self.selected_goal_level and f"Level Unlock: {self.selected_goal_level.value}" in self.received_items:
                        if (self.game_state_score or 0) >= 1000000:
                            self.goal_completed = True
                elif self.option_goal == TonyHawksProSkater12APGoals.SECRET_TAPE_HUNT:
                    self.goal_completed = True

    def _update_skater_sandbox_modifiers(self, skater: TonyHawksProSkater12Skaters) -> None:
        # Progressive Stats
        progressive_stats_item_name: str = f"Progressive Stats: {skater.value}"
        progressive_stats_item_count: int = self.received_items.get(progressive_stats_item_name, 0)

        if progressive_stats_item_count == 0:
            self.game_state_manager.enable_min_stats(skater)

            self.game_state_manager.disable_max_stats(skater)
            self.game_state_manager.disable_no_bails(skater)
        elif progressive_stats_item_count == 1:
            self.game_state_manager.disable_min_stats(skater)
            self.game_state_manager.disable_max_stats(skater)
            self.game_state_manager.disable_no_bails(skater)
        elif progressive_stats_item_count == 2:
            self.game_state_manager.enable_max_stats(skater)

            self.game_state_manager.disable_min_stats(skater)
            self.game_state_manager.disable_no_bails(skater)
        elif progressive_stats_item_count >= 3:
            self.game_state_manager.enable_max_stats(skater)
            self.game_state_manager.enable_no_bails(skater)

            self.game_state_manager.disable_min_stats(skater)

        # Flip Tricks
        flip_tricks_name: str = f"Flip Tricks: {skater.value}"
        flip_tricks_count: int = self.received_items.get(flip_tricks_name, 0)

        if flip_tricks_count == 0:
            self.game_state_manager.disable_flip_trick_points(skater)
        elif flip_tricks_count >= 1:
            self.game_state_manager.enable_flip_trick_points(skater)

        # Grab Tricks
        grab_tricks_name: str = f"Grab Tricks: {skater.value}"
        grab_tricks_count: int = self.received_items.get(grab_tricks_name, 0)

        if grab_tricks_count == 0:
            self.game_state_manager.disable_grab_trick_points(skater)
        elif grab_tricks_count >= 1:
            self.game_state_manager.enable_grab_trick_points(skater)

        # Progressive Grind Tricks
        progressive_grind_tricks_name: str = f"Progressive Grind Tricks: {skater.value}"
        progressive_grind_tricks_count: int = self.received_items.get(progressive_grind_tricks_name, 0)

        if progressive_grind_tricks_count == 0:
            self.game_state_manager.disable_grind_trick_points(skater)
            self.game_state_manager.disable_perfect_grind_balance(skater)
        elif progressive_grind_tricks_count == 1:
            self.game_state_manager.enable_grind_trick_points(skater)
            self.game_state_manager.disable_perfect_grind_balance(skater)
        elif progressive_grind_tricks_count >= 2:
            self.game_state_manager.enable_grind_trick_points(skater)
            self.game_state_manager.enable_perfect_grind_balance(skater)

        # Progressive Lip Tricks
        progressive_lip_tricks_name: str = f"Progressive Lip Tricks: {skater.value}"
        progressive_lip_tricks_count: int = self.received_items.get(progressive_lip_tricks_name, 0)

        if progressive_lip_tricks_count == 0:
            self.game_state_manager.disable_lip_trick_points(skater)
            self.game_state_manager.disable_perfect_lip_balance(skater)
        elif progressive_lip_tricks_count == 1:
            self.game_state_manager.enable_lip_trick_points(skater)
            self.game_state_manager.disable_perfect_lip_balance(skater)
        elif progressive_lip_tricks_count >= 2:
            self.game_state_manager.enable_lip_trick_points(skater)
            self.game_state_manager.enable_perfect_lip_balance(skater)

        # Progressive Manual Tricks
        progressive_manual_tricks_name: str = f"Progressive Manual Tricks: {skater.value}"
        progressive_manual_tricks_count: int = self.received_items.get(progressive_manual_tricks_name, 0)

        if progressive_manual_tricks_count == 0:
            self.game_state_manager.disable_manuals(skater)
            self.game_state_manager.disable_perfect_manual_balance(skater)
        elif progressive_manual_tricks_count == 1:
            self.game_state_manager.enable_manuals(skater)
            self.game_state_manager.disable_perfect_manual_balance(skater)
        elif progressive_manual_tricks_count >= 2:
            self.game_state_manager.enable_manuals(skater)
            self.game_state_manager.enable_perfect_manual_balance(skater)

        # Progressive Special Meter
        progressive_special_meter_name: str = f"Progressive Special Meter: {skater.value}"
        progressive_special_meter_count: int = self.received_items.get(progressive_special_meter_name, 0)

        if progressive_special_meter_count == 0:
            self.game_state_manager.disable_special_meter(skater)
            self.game_state_manager.disable_always_special(skater)
        elif progressive_special_meter_count == 1:
            self.game_state_manager.enable_special_meter(skater)
            self.game_state_manager.disable_always_special(skater)
        elif progressive_special_meter_count >= 2:
            self.game_state_manager.enable_special_meter(skater)
            self.game_state_manager.enable_always_special(skater)

        # Spin Tricks
        spin_tricks_name: str = f"Spin Tricks: {skater.value}"
        spin_tricks_count: int = self.received_items.get(spin_tricks_name, 0)

        if spin_tricks_count == 0:
            self.game_state_manager.disable_spin_multiplier(skater)
        elif spin_tricks_count >= 1:
            self.game_state_manager.enable_spin_multiplier(skater)

        # Transfers
        transfers_name: str = f"Transfers: {skater.value}"
        transfers_count: int = self.received_items.get(transfers_name, 0)

        if transfers_count == 0:
            self.game_state_manager.disable_transfers(skater)
        elif transfers_count >= 1:
            self.game_state_manager.enable_transfers(skater)

        # Wallplants
        wallplants_name: str = f"Wallplants: {skater.value}"
        wallplants_count: int = self.received_items.get(wallplants_name, 0)

        if wallplants_count == 0:
            self.game_state_manager.disable_wallplants(skater)
        elif wallplants_count >= 1:
            self.game_state_manager.enable_wallplants(skater)

        # Extra Tricks
        extra_tricks_name: str = f"Extra Tricks: {skater.value}"
        extra_tricks_count: int = self.received_items.get(extra_tricks_name, 0)

        if extra_tricks_count == 0:
            self.game_state_manager.disable_extra_tricks(skater)
        elif extra_tricks_count >= 1:
            self.game_state_manager.enable_extra_tricks(skater)

        # Stance Switching
        stance_switching_name: str = f"Stance Switching: {skater.value}"
        stance_switching_count: int = self.received_items.get(stance_switching_name, 0)

        if stance_switching_count == 0:
            self.game_state_manager.disable_stance_switching(skater)
        elif stance_switching_count >= 1:
            self.game_state_manager.enable_stance_switching(skater)

        # Double Score
        double_score_name: str = f"Double Score: {skater.value}"
        double_score_count: int = self.received_items.get(double_score_name, 0)

        if double_score_count == 0:
            self.game_state_manager.disable_double_base_score(skater)
        elif double_score_count >= 1:
            self.game_state_manager.enable_double_base_score(skater)

    def _check_for_completed_gaps(self) -> List[str]:
        checked_locations: List[str] = list()

        gap_filter: Dict[TonyHawksProSkater12Skaters, List[TonyHawksProSkater12Gaps]] = dict()
        gap_to_level: Dict[TonyHawksProSkater12Gaps, TonyHawksProSkater12Levels] = dict()

        skater: TonyHawksProSkater12Skaters
        for skater in self.selected_skaters:
            gap_filter[skater] = list()

        level: TonyHawksProSkater12Levels
        skater_data: Dict[TonyHawksProSkater12Skaters, Dict[TonyHawksProSkater12Gaps, str]]
        for level, skater_data in self.target_gap_locations_by_level_skater.items():
            skater: TonyHawksProSkater12Skaters
            gap_data: Dict[TonyHawksProSkater12Gaps, str]
            for skater, gap_data in skater_data.items():
                gap: TonyHawksProSkater12Gaps
                for gap in gap_data.keys():
                    gap_filter[skater].append(gap)
                    gap_to_level[gap] = level

        landed_gap_counts: Optional[Dict[TonyHawksProSkater12Skaters, Dict[TonyHawksProSkater12Gaps, int]]]
        landed_gap_counts = self.game_state_manager.get_landed_gap_counts(gap_filter)

        new_gap_counts_by_level_skater: Dict[TonyHawksProSkater12Levels, Dict[TonyHawksProSkater12Skaters, Dict[TonyHawksProSkater12Gaps, int]]] = dict()

        skater: TonyHawksProSkater12Skaters
        gap_data: Dict[TonyHawksProSkater12Gaps, int]
        for skater, gap_data in landed_gap_counts.items():
            gap: TonyHawksProSkater12Gaps
            landed_count: int
            for gap, landed_count in gap_data.items():
                level: TonyHawksProSkater12Levels = gap_to_level[gap]

                if level not in new_gap_counts_by_level_skater:
                    new_gap_counts_by_level_skater[level] = dict()

                if skater not in new_gap_counts_by_level_skater[level]:
                    new_gap_counts_by_level_skater[level][skater] = dict()

                new_gap_counts_by_level_skater[level][skater][gap] = landed_count

                if self.gap_counts_by_level_skater is not None:
                    if landed_count > self.gap_counts_by_level_skater[level][skater][gap]:
                        checked_locations.append(self.target_gap_locations_by_level_skater[level][skater][gap])

        self.gap_counts_by_level_skater = new_gap_counts_by_level_skater

        return checked_locations

    def _check_for_completed_specials(self) -> List[str]:
        checked_locations: List[str] = list()

        landed_special_counts: Optional[Dict[TonyHawksProSkater12Skaters, Dict[TonyHawksProSkater12Specials, int]]]
        landed_special_counts = self.game_state_manager.get_landed_special_counts(self.selected_skaters)

        if landed_special_counts is not None:
            skater: TonyHawksProSkater12Skaters
            special_data: Dict[TonyHawksProSkater12Specials, int]
            for skater, special_data in landed_special_counts.items():
                special: TonyHawksProSkater12Specials
                landed_count: int
                for special, landed_count in special_data.items():
                    if self.special_counts_by_skater is not None:
                        if landed_count > self.special_counts_by_skater[skater][special]:
                            checked_locations.append(f"{skater.value} - Special - {special.value}")

            self.special_counts_by_skater = landed_special_counts

        return checked_locations

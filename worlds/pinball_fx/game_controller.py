from typing import Dict, List, Optional, Set

import collections
import logging
import time

from .enums import (
    PinballFXAPGoals,
    PinballFXAPRequirementModes,
    PinballFXAPTrapTypes,
    PinballFXTables,
    PinballFXGameModes,
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
    game_state: GameState

    # Generation Options
    option_goal: Optional[PinballFXAPGoals]
    option_shiny_quarters_total: Optional[int]
    option_shiny_quarters_required: Optional[int]
    option_pinball_table_selection: Optional[Dict[PinballFXTables, bool]]
    option_pinball_table_count: Optional[int]
    option_include_very_high_tier_scores: Optional[bool]
    option_include_one_ball_challenges: Optional[bool]
    option_include_flips_challenges: Optional[bool]
    option_include_distance_challenges: Optional[bool]
    option_target_score_requirement_mode: Optional[PinballFXAPRequirementModes]
    option_target_score_requirement_percentage: Optional[int]
    option_useful_item_percentage: Optional[int]
    option_trap_percentage: Optional[int]
    option_trap_weights: Optional[Dict[PinballFXAPTrapTypes, int]]
    option_trap_duration: Optional[int]

    # Generation Data
    selected_tables: Optional[List[PinballFXTables]]
    selected_starter_table_modes: Optional[Dict[PinballFXTables, List[PinballFXGameModes]]]
    selected_goal_table: Optional[PinballFXTables]

    target_scores: Optional[Dict[PinballFXTables, Dict[PinballFXGameModes, List[int]]]]
    target_score_ratios: Optional[Dict[PinballFXTables, float]]

    # State
    should_prepare_processed_trap_counters: bool
    processed_trap_counters: Dict[PinballFXAPTrapTypes, int]
    active_trap_timestamps: Dict[PinballFXAPTrapTypes, Optional[int]]

    def __init__(self, logger: logging.Logger = None) -> None:
        self.logger = logger

        self.game_state_manager = GameStateManager()

        self.received_items = dict()
        self.completed_locations = set()

        self.completed_locations_queue = collections.deque()
        self.received_items_queue = collections.deque()

        self.goal_item_count = 0
        self.goal_completed = False

        self.game_state = None

        self.option_goal = None
        self.option_shiny_quarters_total = None
        self.option_shiny_quarters_required = None
        self.option_pinball_table_selection = None
        self.option_pinball_table_count = None
        self.option_include_very_high_tier_scores = None
        self.option_include_one_ball_challenges = None
        self.option_include_flips_challenges = None
        self.option_include_distance_challenges = None
        self.option_target_score_requirement_mode = None
        self.option_target_score_requirement_percentage = None
        self.option_useful_item_percentage = None
        self.option_trap_percentage = None
        self.option_trap_weights = None
        self.option_trap_duration = None

        self.selected_tables = None
        self.selected_starter_table_modes = None
        self.selected_goal_table = None

        self.target_scores = None
        self.target_score_ratios = None

        self.should_prepare_processed_trap_counters = True

        self.processed_trap_counters = {
            PinballFXAPTrapTypes.BLACK_AND_WHITE: 0,
            PinballFXAPTrapTypes.BLOOM: 0,
            PinballFXAPTrapTypes.CHROMATIC: 0,
            PinballFXAPTrapTypes.COLOR_INVERSION: 0,
            PinballFXAPTrapTypes.GRAINY: 0,
            PinballFXAPTrapTypes.TUNNEL_VISION: 0,
        }

        self.active_trap_timestamps = {
            PinballFXAPTrapTypes.BLACK_AND_WHITE: None,
            PinballFXAPTrapTypes.BLOOM: None,
            PinballFXAPTrapTypes.CHROMATIC: None,
            PinballFXAPTrapTypes.COLOR_INVERSION: None,
            PinballFXAPTrapTypes.GRAINY: None,
            PinballFXAPTrapTypes.TUNNEL_VISION: None,
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

    def update(self) -> None:
        if self.game_state_manager.is_process_still_running():
            try:
                self._refresh_game_state()

                if not self.game_state.is_valid:
                    return

                if (self.option_trap_percentage or 0) > 0:
                    self._manage_traps()

                self._check_for_completed_locations()
                self._process_received_items()

                self._check_for_victory()
            except Exception:
                import traceback

                with open("pinball_fx_errors.log", "a") as f:
                    f.write(traceback.format_exc() + "\n\n")

    def reset(self) -> None:
        self.received_items = dict()
        self.completed_locations = set()

        self.completed_locations_queue = collections.deque()
        self.received_items_queue = collections.deque()

        self.goal_item_count = 0
        self.goal_completed = False

        self.game_state = None

        self.option_goal = None
        self.option_shiny_quarters_total = None
        self.option_shiny_quarters_required = None
        self.option_pinball_table_selection = None
        self.option_pinball_table_count = None
        self.option_include_very_high_tier_scores = None
        self.option_include_one_ball_challenges = None
        self.option_include_flips_challenges = None
        self.option_include_distance_challenges = None
        self.option_target_score_requirement_mode = None
        self.option_target_score_requirement_percentage = None
        self.option_useful_item_percentage = None
        self.option_trap_percentage = None
        self.option_trap_weights = None
        self.option_trap_duration = None

        self.selected_tables = None
        self.selected_starter_table_modes = None
        self.selected_goal_table = None

        self.target_scores = None
        self.target_score_ratios = None

        self.should_prepare_processed_trap_counters = True

        self.processed_trap_counters = {
            PinballFXAPTrapTypes.BLACK_AND_WHITE: 0,
            PinballFXAPTrapTypes.BLOOM: 0,
            PinballFXAPTrapTypes.CHROMATIC: 0,
            PinballFXAPTrapTypes.COLOR_INVERSION: 0,
            PinballFXAPTrapTypes.GRAINY: 0,
            PinballFXAPTrapTypes.TUNNEL_VISION: 0,
        }

        self.active_trap_timestamps = {
            PinballFXAPTrapTypes.BLACK_AND_WHITE: None,
            PinballFXAPTrapTypes.BLOOM: None,
            PinballFXAPTrapTypes.CHROMATIC: None,
            PinballFXAPTrapTypes.COLOR_INVERSION: None,
            PinballFXAPTrapTypes.GRAINY: None,
            PinballFXAPTrapTypes.TUNNEL_VISION: None,
        }

    def _refresh_game_state(self) -> None:
        self.game_state = self.game_state_manager.determine_game_state()

    def _check_for_completed_locations(self) -> None:
        if not self.game_state.is_on_table:
            return

        if self.game_state.table not in self.selected_tables:
            return

        if self.game_state.game_mode is None:
            return

        unlock_item_name: str = f"{self.game_state.game_mode.value} Unlock: {self.game_state.table.value}"
        item_count: int = self.received_items.get(unlock_item_name, 0)

        if item_count < 1:
            return

        if self.game_state.game_mode == PinballFXGameModes.ONE_BALL and not self.option_include_one_ball_challenges:
            return
        elif self.game_state.game_mode == PinballFXGameModes.FLIPS and not self.option_include_flips_challenges:
            return
        elif self.game_state.game_mode == PinballFXGameModes.DISTANCE and not self.option_include_distance_challenges:
            return

        checked_locations: List[str] = list()

        index_mapping: Dict[int, str] = {
            0: "(Low)",
            1: "(Mid)",
            2: "(High)",
            3: "(Very High)",
        }

        target_scores: List[int] = self.target_scores[self.game_state.table][self.game_state.game_mode]

        multiplier_item_name: str = f"{self.game_state.table.value} - {self.game_state.game_mode.value}: Score Multiplier"
        item_count_multiplier: int = self.received_items.get(multiplier_item_name, 0)

        discount_item_name: str = f"{self.game_state.table.value} - {self.game_state.game_mode.value}: Target Score Discount"
        item_count_discount: int = self.received_items.get(discount_item_name, 0)

        modified_score: int = int(self.game_state.score * (1.0 + (0.05 * item_count_multiplier)))

        i: int
        target_score: int
        for i, target_score in enumerate(target_scores):
            if i == 3 and not self.option_include_very_high_tier_scores:
                break

            modified_target_score: int = int(target_score * (1.0 - (0.05 * item_count_discount)))

            if modified_score >= modified_target_score:
                checked_locations.append(f"{self.game_state.table.value} - {self.game_state.game_mode.value}: Target Score {index_mapping[i]}")

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
                    self.processed_trap_counters[PinballFXAPTrapTypes(item_name)] = item_count

    def _manage_traps(self) -> None:
        if not self.game_state.is_on_table:
            return

        if self.game_state.table not in (self.selected_tables + [self.selected_goal_table]):
            return

        now_timestamp: int = int(time.time())

        trap_type: PinballFXAPTrapTypes
        expiry_timestamp: int
        for trap_type, expiry_timestamp in self.active_trap_timestamps.items():
            if expiry_timestamp is not None:
                if now_timestamp >= expiry_timestamp:
                    if trap_type == PinballFXAPTrapTypes.BLACK_AND_WHITE:
                        self.game_state_manager.disable_black_and_white_trap()
                    elif trap_type == PinballFXAPTrapTypes.BLOOM:
                        self.game_state_manager.disable_bloom_trap()
                    elif trap_type == PinballFXAPTrapTypes.CHROMATIC:
                        self.game_state_manager.disable_chromatic_trap()
                    elif trap_type == PinballFXAPTrapTypes.COLOR_INVERSION:
                        self.game_state_manager.disable_color_inversion_trap()
                    elif trap_type == PinballFXAPTrapTypes.GRAINY:
                        self.game_state_manager.disable_grainy_trap()
                    elif trap_type == PinballFXAPTrapTypes.TUNNEL_VISION:
                        self.game_state_manager.disable_tunnel_vision_trap()

                    self.active_trap_timestamps[trap_type] = None

        item_name: str
        item_count: int
        for item_name, item_count in self.received_items.items():
            if item_name.endswith(" Trap"):
                trap_type: PinballFXAPTrapTypes = PinballFXAPTrapTypes(item_name)

                if item_count > self.processed_trap_counters[trap_type]:
                    expiry_timestamp: int = int(time.time()) + self.option_trap_duration

                    if trap_type == PinballFXAPTrapTypes.BLACK_AND_WHITE:
                        if self.active_trap_timestamps[trap_type] is None:
                            if self.game_state_manager.enable_black_and_white_trap():
                                self.active_trap_timestamps[trap_type] = expiry_timestamp
                                self.processed_trap_counters[trap_type] += 1
                    elif trap_type == PinballFXAPTrapTypes.BLOOM:
                        if self.active_trap_timestamps[trap_type] is None:
                            if self.game_state_manager.enable_bloom_trap():
                                self.active_trap_timestamps[trap_type] = expiry_timestamp
                                self.processed_trap_counters[trap_type] += 1
                    elif trap_type == PinballFXAPTrapTypes.CHROMATIC:
                        if self.active_trap_timestamps[trap_type] is None:
                            if self.game_state_manager.enable_chromatic_trap():
                                self.active_trap_timestamps[trap_type] = expiry_timestamp
                                self.processed_trap_counters[trap_type] += 1
                    elif trap_type == PinballFXAPTrapTypes.COLOR_INVERSION:
                        if self.active_trap_timestamps[trap_type] is None:
                            if self.game_state_manager.enable_color_inversion_trap():
                                self.active_trap_timestamps[trap_type] = expiry_timestamp
                                self.processed_trap_counters[trap_type] += 1
                    elif trap_type == PinballFXAPTrapTypes.GRAINY:
                        if self.active_trap_timestamps[trap_type] is None:
                            if self.game_state_manager.enable_grainy_trap():
                                self.active_trap_timestamps[trap_type] = expiry_timestamp
                                self.processed_trap_counters[trap_type] += 1
                    elif trap_type == PinballFXAPTrapTypes.TUNNEL_VISION:
                        if self.active_trap_timestamps[trap_type] is None:
                            if self.game_state_manager.enable_tunnel_vision_trap():
                                self.active_trap_timestamps[trap_type] = expiry_timestamp
                                self.processed_trap_counters[trap_type] += 1

    def _check_for_victory(self) -> None:
        if "Shiny Quarter" in self.received_items:
            if self.received_items["Shiny Quarter"] >= self.option_shiny_quarters_required:
                if self.option_goal == PinballFXAPGoals.SHINY_QUARTERS_FINAL_TABLE:
                    if self.game_state.table == self.selected_goal_table:
                        unlock_item_name: str = f"{PinballFXGameModes.CLASSIC.value} Unlock: {self.selected_goal_table.value}"

                        if unlock_item_name in self.received_items and self.received_items[unlock_item_name] > 0:
                            goal_score: int = self.target_scores[self.selected_goal_table][PinballFXGameModes.CLASSIC][2]

                            if self.game_state.score >= goal_score:
                                self.goal_completed = True
                elif self.option_goal == PinballFXAPGoals.SHINY_QUARTERS_HUNT:
                    self.goal_completed = True

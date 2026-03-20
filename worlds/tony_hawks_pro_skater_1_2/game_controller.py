from typing import Dict, List, Optional, Set, Tuple, Union

import collections
import logging

from .enums import (
    TonyHawksProSkater12APGoals,
    TonyHawksProSkater12APRequirementModes,
    TonyHawksProSkater12APTrapTypes,
    TonyHawksProSkater12Gaps,
    TonyHawksProSkater12Levels,
    TonyHawksProSkater12Skaters,
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
    # ...

    # Generation Options
    option_goal: Optional[TonyHawksProSkater12APGoals]
    option_secret_tapes_total: Optional[int]
    option_secret_tapes_required: Optional[int]
    option_skater_selection: Optional[Dict[TonyHawksProSkater12Skaters, bool]]
    option_skater_count: Optional[int]
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
    # ...

    def __init__(self, logger: logging.Logger = None) -> None:
        self.logger = logger

        self.game_state_manager = GameStateManager()

        self.received_items = dict()
        self.completed_locations = set()

        self.completed_locations_queue = collections.deque()
        self.received_items_queue = collections.deque()

        self.goal_completed = False

        # Game State...

        self.option_goal = None
        self.option_secret_tapes_total = None
        self.option_secret_tapes_required = None
        self.option_skater_selection = None
        self.option_skater_count = None
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

        # Data...

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

    # ...

    def update(self) -> None:
        pass

    def reset(self) -> None:
        self.received_items = dict()
        self.completed_locations = set()

        self.completed_locations_queue = collections.deque()
        self.received_items_queue = collections.deque()

        self.goal_completed = False

        # Game State...

        self.option_goal = None
        self.option_secret_tapes_total = None
        self.option_secret_tapes_required = None
        self.option_skater_selection = None
        self.option_skater_count = None
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

        # Data...

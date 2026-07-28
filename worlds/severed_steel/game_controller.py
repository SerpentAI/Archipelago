from typing import Dict, List, Optional, Set, Tuple

import collections
import logging
import time

from .enums import (
    SeveredSteelAPGoals,
    SeveredSteelAPMutatorPoolTypes,
    SeveredSteelAPRequirementModes,
    SeveredSteelAPTrapTypes,
    SeveredSteelLevels,
    SeveredSteelMutators,
    SeveredSteelStylishActions,
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
    option_goal: Optional[SeveredSteelAPGoals]
    option_edensys_root_keys_total: Optional[int]
    option_edensys_root_keys_required: Optional[int]
    option_level_selection: Optional[Dict[SeveredSteelLevels, bool]]
    option_level_count: Optional[int]
    option_mutator_percentage: Optional[int]
    option_mutator_pool_type: Optional[SeveredSteelAPMutatorPoolTypes]
    option_mirrored_percentage: Optional[int]
    option_include_target_times: Optional[bool]
    option_include_challenges: Optional[bool]
    option_include_stylish_action_challenges: Optional[bool]
    option_stylish_action_challenge_count_per_level: Optional[int]
    option_rank_score_requirement_mode: Optional[SeveredSteelAPRequirementModes]
    option_rank_score_requirement_percentage: Optional[int]
    option_target_time_requirement_mode: Optional[SeveredSteelAPRequirementModes]
    option_target_time_requirement_percentage: Optional[int]
    option_include_overpowered_items: Optional[bool]
    option_invincible_mode: Optional[bool]
    option_trap_percentage: Optional[int]
    option_trap_weights: Optional[Dict[SeveredSteelAPTrapTypes, int]]
    option_trap_duration: Optional[int]

    # Generation Data
    selected_levels: Optional[List[SeveredSteelLevels]]
    selected_starting_levels: Optional[List[SeveredSteelLevels]]
    selected_goal_level: Optional[SeveredSteelLevels]
    level_to_mutator: Optional[Dict[SeveredSteelLevels, Optional[SeveredSteelMutators]]]
    level_to_is_mirrored: Optional[Dict[SeveredSteelLevels, bool]]
    level_to_stylish_action_challenges: Optional[Dict[SeveredSteelLevels, Optional[List[Tuple[SeveredSteelStylishActions, int]]]]]
    target_rank_scores: Optional[Dict[SeveredSteelLevels, List[int]]]
    target_times: Optional[Dict[SeveredSteelLevels, Optional[int]]]
    target_rank_score_ratios: Optional[Dict[SeveredSteelLevels, float]]
    target_time_ratios: Optional[Dict[SeveredSteelLevels, Optional[float]]]

    # State
    should_prepare_processed_trap_counters: bool
    processed_trap_counters: Dict[SeveredSteelAPTrapTypes, int]
    active_trap_timestamps: Dict[SeveredSteelAPTrapTypes, Optional[int]]

    def __init__(self, logger: logging.Logger = None) -> None:
        self.logger = logger

        self.game_state_manager = GameStateManager()

        self.received_items = dict()
        self.completed_locations = set()

        self.completed_locations_queue = collections.deque()
        self.received_items_queue = collections.deque()

        self.goal_completed = False

        self.game_state = None

        self.option_goal = None
        self.option_edensys_root_keys_total = None
        self.option_edensys_root_keys_required = None
        self.option_level_selection = None
        self.option_level_count = None
        self.option_mutator_percentage = None
        self.option_mutator_pool_type = None
        self.option_mirrored_percentage = None
        self.option_include_target_times = None
        self.option_include_challenges = None
        self.option_include_stylish_action_challenges = None
        self.option_stylish_action_challenge_count_per_level = None
        self.option_rank_score_requirement_mode = None
        self.option_rank_score_requirement_percentage = None
        self.option_target_time_requirement_mode = None
        self.option_target_time_requirement_percentage = None
        self.option_include_overpowered_items = None
        self.option_invincible_mode = None
        self.option_trap_percentage = None
        self.option_trap_weights = None
        self.option_trap_duration = None

        self.selected_levels = None
        self.selected_starting_levels = None
        self.selected_goal_level = None
        self.level_to_mutator = None
        self.level_to_is_mirrored = None
        self.level_to_stylish_action_challenges = None
        self.target_rank_scores = None
        self.target_times = None
        self.target_rank_score_ratios = None
        self.target_time_ratios = None

        self.should_prepare_processed_trap_counters = True

        self.processed_trap_counters = {
            SeveredSteelAPTrapTypes.BLACK_AND_WHITE: 0,
            SeveredSteelAPTrapTypes.BLOOM: 0,
            SeveredSteelAPTrapTypes.CHROMATIC: 0,
            SeveredSteelAPTrapTypes.CINEMATIC: 0,
            SeveredSteelAPTrapTypes.COLOR_INVERSION: 0,
            SeveredSteelAPTrapTypes.FAST_MO: 0,
            SeveredSteelAPTrapTypes.MOBILE_GAME: 0,
            SeveredSteelAPTrapTypes.TUNNEL_VISION: 0,
        }

        self.active_trap_timestamps = {
            SeveredSteelAPTrapTypes.BLACK_AND_WHITE: None,
            SeveredSteelAPTrapTypes.BLOOM: None,
            SeveredSteelAPTrapTypes.CHROMATIC: None,
            SeveredSteelAPTrapTypes.CINEMATIC: None,
            SeveredSteelAPTrapTypes.COLOR_INVERSION: None,
            SeveredSteelAPTrapTypes.FAST_MO: None,
            SeveredSteelAPTrapTypes.MOBILE_GAME: None,
            SeveredSteelAPTrapTypes.TUNNEL_VISION: None,
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

                self._apply_permanent_game_state()
                self._apply_conditional_game_state()

                if (self.option_trap_percentage or 0) > 0:
                    self._manage_traps()

                self._check_for_completed_locations()
                self._process_received_items()

                self._check_for_victory()
            except Exception:
                import traceback

                with open("severed_steel_errors.log", "a") as f:
                    f.write(traceback.format_exc() + "\n\n")

    def reset(self) -> None:
        self.received_items = dict()
        self.completed_locations = set()

        self.completed_locations_queue = collections.deque()
        self.received_items_queue = collections.deque()

        self.goal_completed = False

        self.game_state = None

        self.option_goal = None
        self.option_edensys_root_keys_total = None
        self.option_edensys_root_keys_required = None
        self.option_level_selection = None
        self.option_level_count = None
        self.option_mutator_percentage = None
        self.option_mutator_pool_type = None
        self.option_mirrored_percentage = None
        self.option_include_target_times = None
        self.option_include_challenges = None
        self.option_include_stylish_action_challenges = None
        self.option_stylish_action_challenge_count_per_level = None
        self.option_rank_score_requirement_mode = None
        self.option_rank_score_requirement_percentage = None
        self.option_target_time_requirement_mode = None
        self.option_target_time_requirement_percentage = None
        self.option_include_overpowered_items = None
        self.option_invincible_mode = None
        self.option_trap_percentage = None
        self.option_trap_weights = None
        self.option_trap_duration = None

        self.selected_levels = None
        self.selected_starting_levels = None
        self.selected_goal_level = None
        self.level_to_mutator = None
        self.level_to_is_mirrored = None
        self.level_to_stylish_action_challenges = None
        self.target_rank_scores = None
        self.target_times = None
        self.target_rank_score_ratios = None
        self.target_time_ratios = None

        self.should_prepare_processed_trap_counters = True

        self.processed_trap_counters = {
            SeveredSteelAPTrapTypes.BLACK_AND_WHITE: 0,
            SeveredSteelAPTrapTypes.BLOOM: 0,
            SeveredSteelAPTrapTypes.CHROMATIC: 0,
            SeveredSteelAPTrapTypes.CINEMATIC: 0,
            SeveredSteelAPTrapTypes.COLOR_INVERSION: 0,
            SeveredSteelAPTrapTypes.FAST_MO: 0,
            SeveredSteelAPTrapTypes.MOBILE_GAME: 0,
            SeveredSteelAPTrapTypes.TUNNEL_VISION: 0,
        }

        self.active_trap_timestamps = {
            SeveredSteelAPTrapTypes.BLACK_AND_WHITE: None,
            SeveredSteelAPTrapTypes.BLOOM: None,
            SeveredSteelAPTrapTypes.CHROMATIC: None,
            SeveredSteelAPTrapTypes.CINEMATIC: None,
            SeveredSteelAPTrapTypes.COLOR_INVERSION: None,
            SeveredSteelAPTrapTypes.FAST_MO: None,
            SeveredSteelAPTrapTypes.MOBILE_GAME: None,
            SeveredSteelAPTrapTypes.TUNNEL_VISION: None,
        }

    def _refresh_game_state(self) -> None:
        self.game_state = self.game_state_manager.determine_game_state()

    def _apply_permanent_game_state(self) -> None:
        self.game_state_manager.disable_upload_to_leaderboard()
        self.game_state_manager.enable_unlock_all()

        if self.option_invincible_mode:
            self.game_state_manager.enable_god_mode()

    def _apply_conditional_game_state(self) -> None:
        if self.game_state.is_in_level and self.game_state.level == self.selected_goal_level:
            self.game_state_manager.disable_unlimited_ammo()
            self.game_state_manager.disable_unlimited_cannon_ammo()

            if not self.option_invincible_mode:
                self.game_state_manager.disable_god_mode()

            return

        if not self.game_state.is_in_level or self.game_state.level not in self.selected_levels:
            return

        base_multiplier_burn_rate: float = 15.0
        item_count: int = self.received_items.get("Progressive Multiplier Burn Rate Reduction", 0)

        self.game_state_manager.set_multiplier_burn_rate(
            max(base_multiplier_burn_rate - (3.0 * item_count), 1.0)
        )

        base_fresh_cooldown: float = 7.0
        item_count: int = self.received_items.get("Progressive Fresh Cooldown Reduction", 0)

        self.game_state_manager.set_fresh_cooldown(
            max(base_fresh_cooldown - (1.0 * item_count), 1.0)
        )

        if self.option_include_overpowered_items:
            item_name: str = f"{self.game_state.level.value}: Unlimited Ammo Unlocked"
            item_count: int = self.received_items.get(item_name, 0)

            if item_count > 0:
                self.game_state_manager.enable_unlimited_ammo()
            else:
                self.game_state_manager.disable_unlimited_ammo()

            item_name: str = f"{self.game_state.level.value}: Unlimited Cannon Ammo Unlocked"
            item_count: int = self.received_items.get(item_name, 0)

            if item_count > 0:
                self.game_state_manager.enable_unlimited_cannon_ammo()
            else:
                self.game_state_manager.disable_unlimited_cannon_ammo()

            item_name: str = f"{self.game_state.level.value}: Invincibility Unlocked"
            item_count: int = self.received_items.get(item_name, 0)

            if item_count > 0:
                self.game_state_manager.enable_god_mode()
            else:
                if not self.option_invincible_mode:
                    self.game_state_manager.disable_god_mode()

    def _check_for_completed_locations(self) -> None:
        if not self.game_state.is_in_level or self.game_state.level not in self.selected_levels:
            return

        level: SeveredSteelLevels = self.game_state.level
        level_name: str = self.game_state.level.value

        item_count: int = self.received_items.get(f"Level Unlock: {level_name}", 0)

        if item_count < 1:
            return

        if self.option_mutator_percentage > 0:
            mutator: Optional[SeveredSteelMutators] = self.level_to_mutator[level]

            if mutator is not None and mutator not in self.game_state.mutators:
                return

        if self.option_mirrored_percentage > 0:
            is_mirrored: bool = self.level_to_is_mirrored[level]

            if self.game_state.is_mirrored != is_mirrored:
                return

        checked_locations: List[str] = list()

        if self.game_state.kill_count >= 10:
            checked_locations.append(f"{level_name} - Kill 10 Enemies")

        if self.game_state.is_level_complete:
            checked_locations.append(f"{level_name} - Kill All Enemies")

        has_stylish_action_counts: bool = self.game_state.stylish_action_counts is not None

        if has_stylish_action_counts:
            if self.game_state.stylish_action_counts[SeveredSteelStylishActions.HEADSHOT] >= 7:
                checked_locations.append(f"{level_name} - Kill 7 Enemies with Headshots")

        if self.game_state.is_level_complete:
            item_count: int = self.received_items.get(f"{level_name}: Double Score", 0)
            modified_score: int = self.game_state.score * min(1 + item_count, 2)

            if modified_score >= self.target_rank_scores[level][0]:
                checked_locations.append(f"{level_name} - Obtain a B Rank")

            if modified_score >= self.target_rank_scores[level][1]:
                checked_locations.append(f"{level_name} - Obtain an A Rank")

            if modified_score >= self.target_rank_scores[level][2]:
                checked_locations.append(f"{level_name} - Obtain an S Rank")

            if modified_score >= self.target_rank_scores[level][3]:
                checked_locations.append(f"{level_name} - Obtain an S+ Rank")

            if modified_score >= self.target_rank_scores[level][4]:
                checked_locations.append(f"{level_name} - Obtain an S++ Rank")

            item_count: int = self.received_items.get(f"{level_name}: 10% Target Time Discount", 0)

            if self.option_include_target_times:
                target_time: int = self.target_times[level]
                modified_time: int = self.game_state.time

                if item_count > 0:
                    modified_time = round(modified_time * 0.9)

                if modified_time <= target_time:
                    checked_locations.append(f"{level_name} - Beat the Target Time")

        if self.option_include_challenges:
            if self.game_state.completed_challenge_count >= 2:
                checked_locations.append(f"{level_name} - Complete 2 Challenges")

        if self.option_include_stylish_action_challenges and has_stylish_action_counts:
            i: int
            challenge: Tuple[SeveredSteelStylishActions, int]
            for i, challenge in enumerate(self.level_to_stylish_action_challenges[level]):
                item_count: int = self.received_items.get(f"Stylish Action License: {challenge[0].value}", 0)

                if item_count < 1:
                    continue

                if self.game_state.stylish_action_counts[challenge[0]] >= challenge[1]:
                    checked_locations.append(f"{level_name} - Complete Stylish Action Challenge #{i + 1}")

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
                    self.processed_trap_counters[SeveredSteelAPTrapTypes(item_name)] = item_count

    def _manage_traps(self) -> None:
        if not self.game_state.is_in_level:
            return

        if self.game_state.is_level_complete or self.game_state.was_level_completed_recently:
            return

        if self.game_state.level not in (self.selected_levels + [self.selected_goal_level]):
            return

        now_timestamp: int = int(time.time())

        trap_type: SeveredSteelAPTrapTypes
        expiry_timestamp: int
        for trap_type, expiry_timestamp in self.active_trap_timestamps.items():
            if expiry_timestamp is not None:
                if now_timestamp >= expiry_timestamp:
                    if trap_type == SeveredSteelAPTrapTypes.BLACK_AND_WHITE:
                        self.game_state_manager.disable_black_and_white_trap()
                    elif trap_type == SeveredSteelAPTrapTypes.BLOOM:
                        self.game_state_manager.disable_bloom_trap()
                    elif trap_type == SeveredSteelAPTrapTypes.CHROMATIC:
                        self.game_state_manager.disable_chromatic_trap()
                    elif trap_type == SeveredSteelAPTrapTypes.CINEMATIC:
                        self.game_state_manager.disable_cinematic_trap()
                    elif trap_type == SeveredSteelAPTrapTypes.COLOR_INVERSION:
                        self.game_state_manager.disable_color_inversion_trap()
                    elif trap_type == SeveredSteelAPTrapTypes.FAST_MO:
                        self.game_state_manager.disable_fast_mo_trap()
                    elif trap_type == SeveredSteelAPTrapTypes.MOBILE_GAME:
                        self.game_state_manager.disable_mobile_game_trap()
                    elif trap_type == SeveredSteelAPTrapTypes.TUNNEL_VISION:
                        self.game_state_manager.disable_tunnel_vision_trap()

                    self.active_trap_timestamps[trap_type] = None

        item_name: str
        item_count: int
        for item_name, item_count in self.received_items.items():
            if item_name.endswith(" Trap"):
                trap_type: SeveredSteelAPTrapTypes = SeveredSteelAPTrapTypes(item_name)

                if item_count > self.processed_trap_counters[trap_type]:
                    expiry_timestamp: int = int(time.time()) + self.option_trap_duration

                    if trap_type == SeveredSteelAPTrapTypes.BLACK_AND_WHITE:
                        if self.active_trap_timestamps[trap_type] is None:
                            if self.game_state_manager.enable_black_and_white_trap():
                                self.active_trap_timestamps[trap_type] = expiry_timestamp
                                self.processed_trap_counters[trap_type] += 1
                    elif trap_type == SeveredSteelAPTrapTypes.BLOOM:
                        if self.active_trap_timestamps[trap_type] is None:
                            if self.game_state_manager.enable_bloom_trap():
                                self.active_trap_timestamps[trap_type] = expiry_timestamp
                                self.processed_trap_counters[trap_type] += 1
                    elif trap_type == SeveredSteelAPTrapTypes.CHROMATIC:
                        if self.active_trap_timestamps[trap_type] is None:
                            if self.game_state_manager.enable_chromatic_trap():
                                self.active_trap_timestamps[trap_type] = expiry_timestamp
                                self.processed_trap_counters[trap_type] += 1
                    elif trap_type == SeveredSteelAPTrapTypes.CINEMATIC:
                        if self.active_trap_timestamps[trap_type] is None:
                            if self.game_state_manager.enable_cinematic_trap():
                                self.active_trap_timestamps[trap_type] = expiry_timestamp
                                self.processed_trap_counters[trap_type] += 1
                    elif trap_type == SeveredSteelAPTrapTypes.COLOR_INVERSION:
                        if self.active_trap_timestamps[trap_type] is None:
                            if self.game_state_manager.enable_color_inversion_trap():
                                self.active_trap_timestamps[trap_type] = expiry_timestamp
                                self.processed_trap_counters[trap_type] += 1
                    elif trap_type == SeveredSteelAPTrapTypes.FAST_MO:
                        if self.active_trap_timestamps[trap_type] is None:
                            if self.game_state_manager.enable_fast_mo_trap():
                                self.active_trap_timestamps[trap_type] = expiry_timestamp
                                self.processed_trap_counters[trap_type] += 1
                    elif trap_type == SeveredSteelAPTrapTypes.MOBILE_GAME:
                        if self.active_trap_timestamps[trap_type] is None:
                            if self.game_state_manager.enable_mobile_game_trap():
                                self.active_trap_timestamps[trap_type] = expiry_timestamp
                                self.processed_trap_counters[trap_type] += 1
                    elif trap_type == SeveredSteelAPTrapTypes.TUNNEL_VISION:
                        if self.active_trap_timestamps[trap_type] is None:
                            if self.game_state_manager.enable_tunnel_vision_trap():
                                self.active_trap_timestamps[trap_type] = expiry_timestamp
                                self.processed_trap_counters[trap_type] += 1

    def _check_for_victory(self) -> None:
        if "EdenSys Root Key" in self.received_items:
            if self.received_items["EdenSys Root Key"] >= self.option_edensys_root_keys_required:
                if self.option_goal == SeveredSteelAPGoals.EDENSYS_ROOT_KEYS_FINAL_LEVEL:
                    if self.game_state.level == self.selected_goal_level and f"Level Unlock: {self.selected_goal_level.value}" in self.received_items:
                        if self.game_state.is_level_complete:
                            self.goal_completed = True
                elif self.option_goal == SeveredSteelAPGoals.EDENSYS_ROOT_KEY_HUNT:
                    self.goal_completed = True

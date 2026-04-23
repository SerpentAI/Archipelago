from typing import Dict, List, Optional, Set, Union

import collections
import logging
import time

from .data.game_data import level_to_checkpoints, level_to_internal_index

from .enums import (
    MirrorsEdgeAPGoals,
    MirrorsEdgeAPLogic,
    MirrorsEdgeAPTrapTypes,
    MirrorsEdgeAbilities,
    MirrorsEdgeContexts,
    MirrorsEdgeLevels,
    MirrorsEdgeLevelCheckpoints,
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
    game_state_context: MirrorsEdgeContexts
    game_state_level: Optional[MirrorsEdgeLevels]

    # Generation Options
    option_goal: Optional[MirrorsEdgeAPGoals]
    option_runner_bags_total: Optional[int]
    option_runner_bags_required: Optional[int]
    option_logic: Optional[MirrorsEdgeAPLogic]
    option_open_world: Optional[bool]
    option_starting_ability_count: Optional[int]
    option_include_pure_time_trial_pack_dlc: Optional[bool]
    option_include_2_star_ratings: Optional[bool]
    option_include_3_star_ratings: Optional[bool]
    option_target_time_adjustment_percentage: Optional[int]
    option_useful_item_percentage: Optional[int]
    option_trap_percentage: Optional[int]
    option_trap_weights: Optional[Dict[MirrorsEdgeAPTrapTypes, int]]
    option_fov_adjustment: Optional[int]

    # Generation Data
    starting_levels: Optional[List[MirrorsEdgeLevels]]
    levels: Optional[List[MirrorsEdgeLevels]]
    goal_level: Optional[MirrorsEdgeLevels]
    starting_abilities: Optional[List[MirrorsEdgeAbilities]]
    abilities: Optional[List[MirrorsEdgeAbilities]]
    target_times: Optional[Dict[MirrorsEdgeLevels, List[int]]]

    # Data
    checkpoint_locations_by_level: Optional[Dict[MirrorsEdgeLevels, Dict[int, str]]]
    star_rating_locations_by_level: Optional[Dict[MirrorsEdgeLevels, Dict[float, str]]]

    # State
    previous_context: Optional[MirrorsEdgeContexts]
    previous_level: Optional[MirrorsEdgeLevels]

    menu_routine_timestamp: Optional[int]

    should_prepare_processed_trap_counters: bool
    processed_trap_counters: Dict[MirrorsEdgeAPTrapTypes, int]
    active_trap_timestamps: Dict[MirrorsEdgeAPTrapTypes, Optional[int]]

    def __init__(self, logger: logging.Logger = None) -> None:
        self.logger = logger

        self.game_state_manager = GameStateManager()

        self.received_items = dict()
        self.completed_locations = set()

        self.completed_locations_queue = collections.deque()
        self.received_items_queue = collections.deque()

        self.goal_completed = False

        self.game_state_context = None
        self.game_state_level = None

        self.option_goal = None
        self.option_runner_bags_total = None
        self.option_runner_bags_required = None
        self.option_logic = None
        self.option_open_world = None
        self.option_starting_ability_count = None
        self.option_include_pure_time_trial_pack_dlc = None
        self.option_include_2_star_ratings = None
        self.option_include_3_star_ratings = None
        self.option_target_time_adjustment_percentage = None
        self.option_useful_item_percentage = None
        self.option_trap_percentage = None
        self.option_trap_weights = None
        self.option_fov_adjustment = None

        self.starting_levels = None
        self.levels = None
        self.goal_level = None
        self.starting_abilities = None
        self.abilities = None
        self.target_times = None

        self.checkpoint_locations_by_level = None
        self.star_rating_locations_by_level = None

        self.previous_context = None
        self.previous_level = None

        self.menu_routine_timestamp = None

        self.should_prepare_processed_trap_counters = True

        self.processed_trap_counters = {
            MirrorsEdgeAPTrapTypes.INJURY_TRAP: 0,
            MirrorsEdgeAPTrapTypes.SLIPPERY_TRAP: 0,
            MirrorsEdgeAPTrapTypes.SLOW_TRAP: 0,
            MirrorsEdgeAPTrapTypes.WIDE_FOV_TRAP: 0,
        }

        self.active_trap_timestamps = {
            MirrorsEdgeAPTrapTypes.INJURY_TRAP: None,
            MirrorsEdgeAPTrapTypes.SLIPPERY_TRAP: None,
            MirrorsEdgeAPTrapTypes.SLOW_TRAP: None,
            MirrorsEdgeAPTrapTypes.WIDE_FOV_TRAP: None,
        }

    def log(self, message) -> None:
        if self.logger:
            self.logger.info(message)

    def log_debug(self, message) -> None:
        if self.logger:
            self.logger.debug(message)

    def open_process_handle(self) -> bool:
        return_value: bool = self.game_state_manager.open_process_handle()

        self.game_state_manager.disable_all_moves()

        return return_value

    def close_process_handle(self) -> bool:
        return self.game_state_manager.close_process_handle()

    def is_process_running(self) -> bool:
        return self.game_state_manager.is_process_still_running()

    def assemble_checkpoint_locations(self) -> None:
        if self.levels is None:
            return None

        locations: Dict[MirrorsEdgeLevels, Dict[int, str]] = dict()

        level: MirrorsEdgeLevels
        for level in self.levels:
            if level == self.goal_level:
                continue

            locations[level] = dict()

            i: int
            checkpoint: MirrorsEdgeLevelCheckpoints
            for i, checkpoint in enumerate(level_to_checkpoints[level]):
                locations[level][i + 1] = checkpoint.value

        self.checkpoint_locations_by_level = locations

        return None

    def assemble_target_time_locations(self) -> None:
        if self.target_times is None:
            return None

        locations: Dict[MirrorsEdgeLevels, Dict[float, str]] = dict()

        level: MirrorsEdgeLevels
        for level in self.levels:
            if level == self.goal_level:
                continue

            locations[level] = dict()

            locations[level][float(self.target_times[level][0])] = f"{level.value} - 1 Star Rating"

            if self.option_include_2_star_ratings:
                locations[level][float(self.target_times[level][1])] = f"{level.value} - 2 Star Rating"

            if self.option_include_3_star_ratings:
                locations[level][float(self.target_times[level][2])] = f"{level.value} - 3 Star Rating"

        self.star_rating_locations_by_level = locations

        return None

    def update(self) -> None:
        if self.game_state_manager.is_process_still_running():
            try:
                self._refresh_game_state()

                if self.game_state_context == MirrorsEdgeContexts.INVALID:
                    return None

                self._process_received_items()
                self._apply_conditional_game_state()
                self._check_for_completed_locations()

                if (self.option_trap_percentage or 0) > 0:
                    self._manage_traps()

                self._check_for_victory()
            except Exception:
                import traceback

                with open("mirrors_edge_errors.log", "a") as f:
                    f.write(traceback.format_exc() + "\n\n")

        return None

    def reset(self) -> None:
        self.received_items = dict()
        self.completed_locations = set()

        self.completed_locations_queue = collections.deque()
        self.received_items_queue = collections.deque()

        self.goal_completed = False

        self.game_state_context = None
        self.game_state_level = None

        self.option_goal = None
        self.option_runner_bags_total = None
        self.option_runner_bags_required = None
        self.option_logic = None
        self.option_open_world = None
        self.option_starting_ability_count = None
        self.option_include_pure_time_trial_pack_dlc = None
        self.option_include_2_star_ratings = None
        self.option_include_3_star_ratings = None
        self.option_target_time_adjustment_percentage = None
        self.option_useful_item_percentage = None
        self.option_trap_percentage = None
        self.option_trap_weights = None
        self.option_fov_adjustment = None

        self.starting_levels = None
        self.levels = None
        self.goal_level = None
        self.starting_abilities = None
        self.abilities = None
        self.target_times = None

        self.checkpoint_locations_by_level = None
        self.star_rating_locations_by_level = None

        self.previous_context = None
        self.previous_level = None

        self.menu_routine_timestamp = None

        self.should_prepare_processed_trap_counters = True

        self.processed_trap_counters = {
            MirrorsEdgeAPTrapTypes.INJURY_TRAP: 0,
            MirrorsEdgeAPTrapTypes.SLIPPERY_TRAP: 0,
            MirrorsEdgeAPTrapTypes.SLOW_TRAP: 0,
            MirrorsEdgeAPTrapTypes.WIDE_FOV_TRAP: 0,
        }

        self.active_trap_timestamps = {
            MirrorsEdgeAPTrapTypes.INJURY_TRAP: None,
            MirrorsEdgeAPTrapTypes.SLIPPERY_TRAP: None,
            MirrorsEdgeAPTrapTypes.SLOW_TRAP: None,
            MirrorsEdgeAPTrapTypes.WIDE_FOV_TRAP: None,
        }

    def _refresh_game_state(self) -> None:
        game_state: GameState = self.game_state_manager.determine_game_state()

        if game_state.context != MirrorsEdgeContexts.INVALID:
            self.previous_context = self.game_state_context
            self.previous_level = self.game_state_level

        self.game_state_context = game_state.context
        self.game_state_level = game_state.level

    def _apply_conditional_game_state(self) -> None:
        now: int = int(time.time())

        if self.game_state_context == MirrorsEdgeContexts.MENU:
            if self.previous_context != MirrorsEdgeContexts.MENU:
                self.menu_routine_timestamp = now + 3
                return None

            if self.menu_routine_timestamp is not None and now >= self.menu_routine_timestamp:
                try:
                    self.game_state_manager.prepare_for_menu_routine()

                    statuses: List[Union[bool, None]] = list()

                    statuses.append(self.game_state_manager.lock_all_levels())
                    statuses.append(self.game_state_manager.lock_all_time_trials())

                    level: MirrorsEdgeLevels
                    for level in self.levels:
                        level_unlock_item_name = f"Level Unlock: {level.value}"
                        level_unlock_item_count = self.received_items.get(level_unlock_item_name, 0)

                        if level_unlock_item_count > 0:
                            statuses.append(self.game_state_manager.unlock_time_trial(level_to_internal_index[level]))

                    if self.goal_level is not None:
                        level_unlock_item_name = f"Level Unlock: {self.goal_level.value}"
                        level_unlock_item_count = self.received_items.get(level_unlock_item_name, 0)

                        runner_bag_item_count = self.received_items.get("Runner Bag", 0)

                        if level_unlock_item_count > 0 and runner_bag_item_count >= self.option_runner_bags_required:
                            statuses.append(self.game_state_manager.unlock_time_trial(level_to_internal_index[self.goal_level]))

                    if not all(statuses):
                        self.game_state_context = MirrorsEdgeContexts.INVALID
                        return None
                except Exception:
                    self.game_state_context = MirrorsEdgeContexts.INVALID
                    return None

                self.menu_routine_timestamp = None

        if self.game_state_context == MirrorsEdgeContexts.LEVEL and self.previous_context != MirrorsEdgeContexts.LEVEL:
            self.game_state_manager.prepare_for_level_routine()

        if self.game_state_context == MirrorsEdgeContexts.LEVEL:
            if self.active_trap_timestamps[MirrorsEdgeAPTrapTypes.WIDE_FOV_TRAP] is None:
                self.game_state_manager.set_fov(float(self.option_fov_adjustment))

            no_slippery_trap_active: bool = self.active_trap_timestamps[MirrorsEdgeAPTrapTypes.SLIPPERY_TRAP] is None
            no_slow_trap_active: bool = self.active_trap_timestamps[MirrorsEdgeAPTrapTypes.SLOW_TRAP] is None

            if no_slippery_trap_active and no_slow_trap_active:
                ability_sprint_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.SPRINT.value}"
                ability_sprint_item_count = self.received_items.get(ability_sprint_item_name, 0)

                if ability_sprint_item_count > 0:
                    self.game_state_manager.set_running_speed_regular()
                else:
                    self.game_state_manager.set_running_speed_slow()

        ability_airborne_180_turn_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.AIRBORNE_ONE_EIGHTY_TURN.value}"
        ability_airborne_180_turn_item_count = self.received_items.get(ability_airborne_180_turn_item_name, 0)

        if ability_airborne_180_turn_item_count > 0:
            self.game_state_manager.enable_airborne_180_turn()

        ability_balance_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.BALANCE.value}"
        ability_balance_item_count = self.received_items.get(ability_balance_item_name, 0)

        if ability_balance_item_count > 0:
            self.game_state_manager.enable_balance()

        ability_barge_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.BARGE.value}"
        ability_barge_item_count = self.received_items.get(ability_barge_item_name, 0)

        if ability_barge_item_count > 0:
            self.game_state_manager.enable_barge()

        ability_climb_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.CLIMB.value}"
        ability_climb_item_count = self.received_items.get(ability_climb_item_name, 0)

        if ability_climb_item_count > 0:
            self.game_state_manager.enable_climb()

        ability_coil_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.COIL.value}"
        ability_coil_item_count = self.received_items.get(ability_coil_item_name, 0)

        if ability_coil_item_count > 0:
            self.game_state_manager.enable_coil()

        ability_dodge_jump_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.DODGE_JUMP.value}"
        ability_dodge_jump_item_count = self.received_items.get(ability_dodge_jump_item_name, 0)

        if ability_dodge_jump_item_count > 0:
            self.game_state_manager.enable_dodge_jump()

        ability_grab_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"
        ability_grab_item_count = self.received_items.get(ability_grab_item_name, 0)

        if ability_grab_item_count > 0:
            self.game_state_manager.enable_grab()

        ability_grab_jump_item_name: str = f"Ability Extension Unlock: {MirrorsEdgeAbilities.GRAB_JUMP.value}"
        ability_grab_jump_item_count = self.received_items.get(ability_grab_jump_item_name, 0)

        if ability_grab_jump_item_count > 0:
            self.game_state_manager.enable_grab_jump()

        ability_melee_attack_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.MELEE_ATTACK.value}"
        ability_melee_attack_item_count = self.received_items.get(ability_melee_attack_item_name, 0)

        if ability_melee_attack_item_count > 0:
            self.game_state_manager.enable_melee_attack()

        ability_180_turn_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.ONE_EIGHTY_TURN.value}"
        ability_180_turn_item_count = self.received_items.get(ability_180_turn_item_name, 0)

        if ability_180_turn_item_count > 0:
            self.game_state_manager.enable_180_turn()

        ability_springboard_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.SPRINGBOARD.value}"
        ability_springboard_item_count = self.received_items.get(ability_springboard_item_name, 0)

        if ability_springboard_item_count > 0:
            self.game_state_manager.enable_springboard()

        ability_swing_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.SWING.value}"
        ability_swing_item_count = self.received_items.get(ability_swing_item_name, 0)

        if ability_swing_item_count > 0:
            self.game_state_manager.enable_swing()

        ability_vault_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"
        ability_vault_item_count = self.received_items.get(ability_vault_item_name, 0)

        if ability_vault_item_count > 0:
            self.game_state_manager.enable_vault()

        ability_wall_climb_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.WALL_CLIMB.value}"
        ability_wall_climb_item_count = self.received_items.get(ability_wall_climb_item_name, 0)

        if ability_wall_climb_item_count > 0:
            self.game_state_manager.enable_wall_climb()

        ability_wall_climb_180_turn_jump_item_name: str = f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_CLIMB_ONE_EIGHTY_TURN_JUMP.value}"
        ability_wall_climb_180_turn_jump_item_count = self.received_items.get(ability_wall_climb_180_turn_jump_item_name, 0)

        if ability_wall_climb_180_turn_jump_item_count > 0:
            self.game_state_manager.enable_wall_climb_180_turn_jump()

        ability_wall_run_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.WALL_RUN.value}"
        ability_wall_run_item_count = self.received_items.get(ability_wall_run_item_name, 0)

        if ability_wall_run_item_count > 0:
            self.game_state_manager.enable_wall_run()

        ability_wall_run_jump_item_name: str = f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_RUN_JUMP.value}"
        ability_wall_run_jump_item_count = self.received_items.get(ability_wall_run_jump_item_name, 0)

        if ability_wall_run_jump_item_count > 0:
            self.game_state_manager.enable_wall_run_jump()

        ability_zipline_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.ZIPLINE.value}"
        ability_zipline_item_count = self.received_items.get(ability_zipline_item_name, 0)

        if ability_zipline_item_count > 0:
            self.game_state_manager.enable_zipline()

        return None

    def _check_for_completed_locations(self) -> None:
        checked_locations: List[str] = list()

        if self.game_state_context != MirrorsEdgeContexts.LEVEL:
            return

        if self.goal_level is not None and self.game_state_level == self.goal_level:
            level_unlock_item_name: str = f"Level Unlock: {self.goal_level.value}"
            level_unlock_item_count: int = self.received_items.get(level_unlock_item_name, 0)

            runner_bags_item_count: int = self.received_items.get("Runner Bag", 0)

            if level_unlock_item_count < 1 or runner_bags_item_count < self.option_runner_bags_required:
                return

        if self.game_state_level in self.levels:
            level_unlock_item_name: str = f"Level Unlock: {self.game_state_level.value}"
            level_unlock_item_count: int = self.received_items.get(level_unlock_item_name, 0)

            if level_unlock_item_count < 1:
                return

            if (self.game_state_manager.get_total_checkpoints() or 0) > 0:
                # Checkpoints
                passed_checkpoints: int = self.game_state_manager.get_passed_checkpoints() or 0

                if passed_checkpoints >= 0:
                    checkpoint_count: int
                    location_name: str
                    for checkpoint_count, location_name in self.checkpoint_locations_by_level[self.game_state_level].items():
                        if checkpoint_count <= passed_checkpoints:
                            checked_locations.append(location_name)

                # Star Ratings
                timestamp_start: float = self.game_state_manager.get_start_timestamp() or -1
                timestamp_end: float = self.game_state_manager.get_end_timestamp() or -1

                if timestamp_end > 0:
                    final_time: float = timestamp_end - timestamp_start

                    discount_1_second_item_name: str = f"{self.game_state_level.value}: 1 Second Time Bonus"
                    discount_1_second_item_count: int = self.received_items.get(discount_1_second_item_name, 0)

                    discount_3_seconds_item_name: str = f"{self.game_state_level.value}: 3 Seconds Time Bonus"
                    discount_3_seconds_item_count: int = self.received_items.get(discount_3_seconds_item_name, 0)

                    discount_5_seconds_item_name: str = f"{self.game_state_level.value}: 5 Seconds Time Bonus"
                    discount_5_seconds_item_count: int = self.received_items.get(discount_5_seconds_item_name, 0)

                    discount: float = 0.0

                    discount += discount_1_second_item_count * 1.0
                    discount += discount_3_seconds_item_count * 3.0
                    discount += discount_5_seconds_item_count * 5.0

                    final_time -= float(discount)

                    target_time: float
                    location_name: str
                    for target_time, location_name in self.star_rating_locations_by_level[self.game_state_level].items():
                        if final_time <= target_time:
                            checked_locations.append(location_name)

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
                    self.processed_trap_counters[MirrorsEdgeAPTrapTypes(item_name)] = item_count

    def _manage_traps(self) -> None:
        if not self.game_state_context == MirrorsEdgeContexts.LEVEL:
            return

        if self.game_state_level is None:
            return

        ability_sprint_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.SPRINT.value}"
        ability_sprint_item_count: int = self.received_items.get(ability_sprint_item_name, 0)

        has_sprint_ability: bool = ability_sprint_item_count > 0

        now_timestamp: int = int(time.time())

        trap_type: MirrorsEdgeAPTrapTypes
        expiry_timestamp: int
        for trap_type, expiry_timestamp in self.active_trap_timestamps.items():
            if expiry_timestamp is not None:
                if now_timestamp >= expiry_timestamp:
                    if trap_type == MirrorsEdgeAPTrapTypes.INJURY_TRAP:
                        self.game_state_manager.set_health_trap_injury_restore()
                    elif trap_type == MirrorsEdgeAPTrapTypes.SLIPPERY_TRAP:
                        if has_sprint_ability:
                            self.game_state_manager.set_running_speed_regular()
                        else:
                            self.game_state_manager.set_running_speed_slow()
                    elif trap_type == MirrorsEdgeAPTrapTypes.SLOW_TRAP:
                        if has_sprint_ability:
                            self.game_state_manager.set_running_speed_regular()
                        else:
                            self.game_state_manager.set_running_speed_slow()
                    elif trap_type == MirrorsEdgeAPTrapTypes.WIDE_FOV_TRAP:
                        self.game_state_manager.set_fov(float(self.option_fov_adjustment))

                    self.active_trap_timestamps[trap_type] = None

        item_name: str
        item_count: int
        for item_name, item_count in self.received_items.items():
            if item_name.endswith(" Trap"):
                trap_type: MirrorsEdgeAPTrapTypes = MirrorsEdgeAPTrapTypes(item_name)

                if item_count > self.processed_trap_counters[trap_type]:
                    expiry_timestamp: int = int(time.time()) + 20

                    if trap_type == MirrorsEdgeAPTrapTypes.INJURY_TRAP:
                        if self.active_trap_timestamps[trap_type] is None:
                            if self.game_state_manager.set_health_trap_injury():
                                self.active_trap_timestamps[trap_type] = expiry_timestamp
                                self.processed_trap_counters[trap_type] = item_count
                    elif trap_type == MirrorsEdgeAPTrapTypes.SLIPPERY_TRAP:
                        if self.active_trap_timestamps[trap_type] is None:
                            if self.game_state_manager.set_running_speed_trap_slippery():
                                self.active_trap_timestamps[trap_type] = expiry_timestamp
                                self.processed_trap_counters[trap_type] = item_count
                    elif trap_type == MirrorsEdgeAPTrapTypes.SLOW_TRAP:
                        if self.active_trap_timestamps[trap_type] is None:
                            if self.game_state_manager.set_running_speed_trap_slow():
                                self.active_trap_timestamps[trap_type] = expiry_timestamp
                                self.processed_trap_counters[trap_type] = item_count
                    elif trap_type == MirrorsEdgeAPTrapTypes.WIDE_FOV_TRAP:
                        if self.active_trap_timestamps[trap_type] is None:
                            if self.game_state_manager.set_fov_trap_wide():
                                self.active_trap_timestamps[trap_type] = expiry_timestamp
                                self.processed_trap_counters[trap_type] = item_count

    def _check_for_victory(self) -> None:
        if "Runner Bag" in self.received_items:
            if self.received_items["Runner Bag"] >= self.option_runner_bags_required:
                if self.option_goal == MirrorsEdgeAPGoals.RUNNER_BAGS_FINAL_LEVEL:
                    if self.game_state_level == self.goal_level and f"Level Unlock: {self.goal_level.value}" in self.received_items:
                        total_checkpoints: int = self.game_state_manager.get_total_checkpoints() or 0
                        passed_checkpoints: int = self.game_state_manager.get_passed_checkpoints() or 0

                        if total_checkpoints > 0:
                            if passed_checkpoints == total_checkpoints:
                                self.goal_completed = True
                elif self.option_goal == MirrorsEdgeAPGoals.RUNNER_BAG_HUNT:
                    self.goal_completed = True

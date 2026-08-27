from typing import Dict, List, Optional, Set, Tuple

import collections
import logging
import math
import time

from .enums import (
    PoolsGoals,
    PoolsItems,
    PoolsLevels,
    PoolsLocations,
    PoolsTags,
    PoolsTrapTypes,
)

from .data.game_data import (
    chair_coordinates_by_level,
    discriminators_by_level,
    pool_collisions_by_level,
    progress_collisions_by_level,
    progress_flags_by_level,
    progress_zoom_ins_by_level,
    prop_collisions_by_level,
    slide_collisions_by_level,
)

from .data.location_data import PoolsLocationData, location_data

from .data_funcs import locations_with_tag
from .game_state_manager import GameStateManager, GameState


class GameController:
    logger: Optional[logging.Logger]

    game_state_manager: GameStateManager

    received_items: Dict[PoolsItems, int]
    completed_locations: Set[PoolsLocations]

    completed_locations_queue: collections.deque
    received_items_queue: collections.deque

    goal_completed: bool

    # Game State
    game_state: Optional[GameState]

    # Generation Options
    option_goal: Optional[PoolsGoals]
    option_rubber_ducks_total: Optional[int]
    option_rubber_ducks_required: Optional[int]
    option_include_level_0: Optional[bool]
    option_include_chairs: Optional[bool]
    option_trap_percentage: Optional[int]
    option_trap_weights: Optional[Dict[PoolsTrapTypes, int]]
    option_trap_duration: Optional[int]

    # Generation Data
    selected_starting_level: Optional[PoolsLevels]

    # State
    should_prepare_processed_trap_counters: bool
    processed_trap_counters: Dict[PoolsTrapTypes, int]
    active_trap_timestamps: Dict[PoolsTrapTypes, Optional[int]]

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
        self.option_rubber_ducks_total = None
        self.option_rubber_ducks_required = None
        self.option_include_level_0 = None
        self.option_include_chairs = None
        self.option_trap_percentage = None
        self.option_trap_weights = None
        self.option_trap_duration = None

        self.selected_starting_level = None

        self.should_prepare_processed_trap_counters = True

        self.processed_trap_counters = {
            PoolsTrapTypes.NO_LOOK: 0,
            PoolsTrapTypes.REWIND: 0,
            PoolsTrapTypes.SLOW: 0,
            PoolsTrapTypes.WET: 0,
        }

        self.active_trap_timestamps = {
            PoolsTrapTypes.NO_LOOK: None,
            PoolsTrapTypes.REWIND: None,
            PoolsTrapTypes.SLOW: None,
            PoolsTrapTypes.WET: None,
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

                self._apply_conditional_game_state()

                self._check_for_completed_locations()
                self._process_received_items()

                if (self.option_trap_percentage or 0) > 0:
                    self._manage_traps()

                self._check_for_victory()
            except Exception:
                import traceback

                with open("pools_errors.log", "a") as f:
                    f.write(traceback.format_exc() + "\n\n")

    def reset(self) -> None:
        self.received_items = dict()
        self.completed_locations = set()

        self.completed_locations_queue = collections.deque()
        self.received_items_queue = collections.deque()

        self.goal_completed = False

        self.game_state = None

        self.option_goal = None
        self.option_rubber_ducks_total = None
        self.option_rubber_ducks_required = None
        self.option_include_level_0 = None
        self.option_include_chairs = None
        self.option_trap_percentage = None
        self.option_trap_weights = None
        self.option_trap_duration = None

        self.selected_starting_level = None

        self.should_prepare_processed_trap_counters = True

        self.processed_trap_counters = {
            PoolsTrapTypes.NO_LOOK: 0,
            PoolsTrapTypes.REWIND: 0,
            PoolsTrapTypes.SLOW: 0,
            PoolsTrapTypes.WET: 0,
        }

        self.active_trap_timestamps = {
            PoolsTrapTypes.NO_LOOK: None,
            PoolsTrapTypes.REWIND: None,
            PoolsTrapTypes.SLOW: None,
            PoolsTrapTypes.WET: None,
        }

    def _refresh_game_state(self) -> None:
        self.game_state = self.game_state_manager.determine_game_state()

    def _apply_conditional_game_state(self) -> None:
        if self.active_trap_timestamps[PoolsTrapTypes.SLOW] is None:
            movement_speed_item_count: int = self.received_items.get(PoolsItems.PROGRESSIVE_MOVEMENT_SPEED, 0)
            water_speed_item_count: int = self.received_items.get(PoolsItems.PROGRESSIVE_WATER_SPEED, 0)

            run_item_count: int = self.received_items.get(PoolsItems.RUN, 0)

            base_speed: float = 6.0

            run_multiplier: float = 1.0

            if run_item_count > 0:
                run_multiplier = 1.5

            walk_speed: float
            run_speed: float

            if self.game_state.is_in_water:
                walk_speed = base_speed + (1.0 * water_speed_item_count)
                run_speed = float(round(walk_speed * run_multiplier))
            else:
                walk_speed = base_speed + (1.0 * movement_speed_item_count)
                run_speed = float(round(walk_speed * run_multiplier))

            self.game_state_manager.set_walk_speed(min(walk_speed, 24.0))
            self.game_state_manager.set_run_speed(min(run_speed, 36.0))

    def _check_for_completed_locations(self) -> None:
        checked_locations: List[PoolsLocations] = list()
        has_already_found_chair: bool = False

        if not self.game_state.is_in_level:
            return
        elif self.game_state.level == PoolsLevels.LEVEL_0 and not self.option_include_level_0:
            return
        elif self.game_state.level == PoolsLevels.ENDING:
            return

        level_unlock_item: PoolsItems = getattr(PoolsItems, f"{self.game_state.level.name}_UNLOCK")
        level_unlock_item_count: int = self.received_items.get(level_unlock_item, 0)

        if level_unlock_item_count < 1:
            return

        level_tag: PoolsTags = getattr(PoolsTags, f"{self.game_state.level.name}_LOCATION")

        level_locations: List[PoolsLocations] = locations_with_tag(level_tag)

        level_location: PoolsLocations
        for level_location in level_locations:
            data: PoolsLocationData = location_data[level_location]

            if not self.option_include_chairs and PoolsTags.CHAIR_LOCATION in data.tags:
                continue

            if PoolsTags.POOL_LOCATION in data.tags and PoolsTags.SPECIAL_HANDLING not in data.tags:
                if self.game_state.is_in_water:
                    if level_location in pool_collisions_by_level[self.game_state.level]:
                        collider_name: str = pool_collisions_by_level[self.game_state.level][level_location]

                        if collider_name in self.game_state.collisions:
                            item_required: Optional[PoolsItems] = None

                            if level_location.value.endswith(" 1T"):
                                item_required = PoolsItems.POOLS_1T
                            elif level_location.value.endswith(" 2T"):
                                item_required = PoolsItems.POOLS_2T
                            elif level_location.value.endswith(" 3T"):
                                item_required = PoolsItems.POOLS_3T
                            elif level_location.value.endswith(" 4T"):
                                item_required = PoolsItems.POOLS_4T
                            elif level_location.value.endswith(" 5T"):
                                item_required = PoolsItems.POOLS_5T
                            elif level_location.value.endswith(" 6T"):
                                item_required = PoolsItems.POOLS_6T
                            elif level_location.value.endswith(" 7T"):
                                item_required = PoolsItems.POOLS_7T
                            elif level_location.value.endswith(" 8T"):
                                item_required = PoolsItems.POOLS_8T
                            elif level_location.value.endswith(" 9T"):
                                item_required = PoolsItems.POOLS_9T
                            elif level_location.value.endswith(" 10T"):
                                item_required = PoolsItems.POOLS_10T
                            elif level_location.value.endswith(" 11T"):
                                item_required = PoolsItems.POOLS_11T

                            if item_required is None:
                                checked_locations.append(level_location)
                            else:
                                item_required_count: int = self.received_items.get(item_required, 0)

                                if item_required_count > 0:
                                    checked_locations.append(level_location)
            elif PoolsTags.SLIDE_LOCATION in data.tags and PoolsTags.SPECIAL_HANDLING not in data.tags:
                if level_location in slide_collisions_by_level[self.game_state.level]:
                    collider_name: str = slide_collisions_by_level[self.game_state.level][level_location]

                    if collider_name in self.game_state.collisions:
                        item_required: Optional[PoolsItems] = None

                        if " Red" in level_location.value:
                            item_required = PoolsItems.SLIDES_RED
                        elif " Yellow" in level_location.value:
                            item_required = PoolsItems.SLIDES_YELLOW
                        elif " Green" in level_location.value:
                            item_required = PoolsItems.SLIDES_GREEN
                        elif " Blue" in level_location.value:
                            item_required = PoolsItems.SLIDES_BLUE
                        elif " Purple" in level_location.value or " Pink" in level_location.value:
                            item_required = PoolsItems.SLIDES_EXTRA

                        if item_required is None:
                            checked_locations.append(level_location)
                        else:
                            item_required_count: int = self.received_items.get(item_required, 0)

                            if item_required_count > 0:
                                checked_locations.append(level_location)
            elif PoolsTags.PROGRESS_LOCATION in data.tags and PoolsTags.SPECIAL_HANDLING not in data.tags:
                if level_location in progress_collisions_by_level[self.game_state.level]:
                    collider_name: str = progress_collisions_by_level[self.game_state.level][level_location]

                    if collider_name in self.game_state.collisions:
                        checked_locations.append(level_location)
                elif level_location in progress_flags_by_level[self.game_state.level]:
                    flag_name: str = progress_flags_by_level[self.game_state.level][level_location]

                    if flag_name in self.game_state.level_progress_flags:
                        checked_locations.append(level_location)
                elif level_location in progress_zoom_ins_by_level[self.game_state.level]:
                    collider_name: str = progress_zoom_ins_by_level[self.game_state.level][level_location]

                    if collider_name in self.game_state.collisions and self.game_state.is_zoomed_in:
                        checked_locations.append(level_location)
            elif PoolsTags.PROP_LOCATION in data.tags and PoolsTags.SPECIAL_HANDLING not in data.tags:
                if level_location in prop_collisions_by_level[self.game_state.level]:
                    collider_name: str = prop_collisions_by_level[self.game_state.level][level_location]

                    if collider_name in self.game_state.collisions:
                        checked_locations.append(level_location)
            elif PoolsTags.SPECIAL_HANDLING in data.tags and PoolsTags.DISCRIMINATOR_HANDLING not in data.tags:
                has_sauna_chairs: bool = self.received_items.get(PoolsItems.CHAIRS_SAUNA, 0) > 0
                has_diving_boards: bool = self.received_items.get(PoolsItems.DIVING_BOARDS, 0) > 0

                if level_location == PoolsLocations.LEVEL_2_PROGRESS_1:
                    if "stairs convex.032" in self.game_state.collisions and self.game_state.coordinates[1] <= -2.36:
                        checked_locations.append(level_location)
                elif level_location == PoolsLocations.LEVEL_3_CHAIR_1:
                    if "Plane.055" in self.game_state.collisions and self.game_state.is_sitting:
                        has_already_found_chair = True

                        if has_sauna_chairs:
                            checked_locations.append(level_location)
                elif level_location == PoolsLocations.LEVEL_3_CHAIR_2:
                    if "Plane.064" in self.game_state.collisions and self.game_state.is_sitting:
                        has_already_found_chair = True

                        if has_sauna_chairs:
                            checked_locations.append(level_location)
                elif level_location == PoolsLocations.LEVEL_3_CHAIR_3:
                    if "Plane.036" in self.game_state.collisions and self.game_state.is_sitting:
                        has_already_found_chair = True

                        if has_sauna_chairs:
                            checked_locations.append(level_location)
                elif level_location == PoolsLocations.LEVEL_3_CHAIR_4:
                    if "Plane.054" in self.game_state.collisions and self.game_state.is_sitting:
                        has_already_found_chair = True

                        if has_sauna_chairs:
                            checked_locations.append(level_location)
                elif level_location == PoolsLocations.LEVEL_3_CHAIR_5:
                    if "Plane.047" in self.game_state.collisions and self.game_state.is_sitting:
                        has_already_found_chair = True

                        if has_sauna_chairs:
                            checked_locations.append(level_location)
                elif level_location == PoolsLocations.LEVEL_3_CHAIR_7:
                    if "Plane.075" in self.game_state.collisions and self.game_state.is_sitting:
                        has_already_found_chair = True

                        if has_sauna_chairs:
                            checked_locations.append(level_location)
                elif level_location == PoolsLocations.LEVEL_3_CHAIR_8:
                    if "Plane.082" in self.game_state.collisions and self.game_state.is_sitting:
                        has_already_found_chair = True

                        if has_sauna_chairs:
                            checked_locations.append(level_location)
                elif level_location == PoolsLocations.LEVEL_3_CHAIR_9:
                    if "Plane.065" in self.game_state.collisions and self.game_state.is_sitting:
                        has_already_found_chair = True

                        if has_sauna_chairs:
                            checked_locations.append(level_location)
                elif level_location == PoolsLocations.LEVEL_4_BOARD_1:
                    if "tile-pilar.043 box.015" in self.game_state.collisions and self.game_state.coordinates[0] > 3.0 and has_diving_boards:
                        checked_locations.append(level_location)
                elif level_location == PoolsLocations.LEVEL_6_PROP_8:
                    if "granite-plane.002" in self.game_state.collisions and "chair_LOD0" in self.game_state.collisions:
                        checked_locations.append(level_location)
                elif level_location == PoolsLocations.LEVEL_6_PROP_9:
                    if "danger fall hazard sign" in self.game_state.collisions or "danger fall hazard sign_2" in self.game_state.collisions or "danger fall hazard sign_3" in self.game_state.collisions:
                        checked_locations.append(level_location)
                elif level_location == PoolsLocations.LEVEL_0_PROP_5:
                    if "plastic chair_LOD0" in self.game_state.collisions and self.game_state.coordinates[1] < 6.0:
                        checked_locations.append(level_location)
                elif level_location == PoolsLocations.LEVEL_0_PROP_9:
                    if "duck_LOD0" in self.game_state.collisions and 0.0 < self.game_state.coordinates[1] < 1.0:
                        checked_locations.append(level_location)

        # Chairs
        if self.option_include_chairs and self.game_state.is_sitting and not has_already_found_chair:
            best_distance: float = 999999.0
            best_location_candidate: Optional[PoolsLocations] = None

            chair_location: PoolsLocations
            coordinates: Tuple[float, float, float]
            for chair_location, coordinates in chair_coordinates_by_level[self.game_state.level].items():
                distance: float = abs(math.dist(self.game_state.coordinates, coordinates))

                if distance < best_distance:
                    best_distance = distance
                    best_location_candidate = chair_location

            if best_location_candidate is not None:
                item_required: Optional[PoolsItems] = None

                if "Plastic Chair" in best_location_candidate.value:
                    item_required = PoolsItems.CHAIRS_PLASTIC
                elif "Armchair" in best_location_candidate.value:
                    item_required = PoolsItems.CHAIRS_ARMCHAIR
                elif "Wooden Chair" in best_location_candidate.value:
                    item_required = PoolsItems.CHAIRS_WOODEN
                elif "Subway Chairs" in best_location_candidate.value:
                    item_required = PoolsItems.CHAIRS_SUBWAY
                elif "Park Bench" in best_location_candidate.value:
                    item_required = PoolsItems.CHAIRS_PARK
                elif "Sofa" in best_location_candidate.value:
                    item_required = PoolsItems.CHAIRS_SOFA

                if item_required is not None:
                    if self.received_items.get(item_required, 0) < 1:
                        best_location_candidate = None

                if best_location_candidate is not None:
                    checked_locations.append(best_location_candidate)

        # Discriminators
        collider_name: str
        for collider_name in self.game_state.collisions:
            if collider_name in discriminators_by_level[self.game_state.level]:
                best_distance: float = 999999.0
                best_location_candidate: Optional[PoolsLocations] = None
                best_location_item_required: Optional[PoolsItems] = None

                location_candidate: Tuple[PoolsLocations, str, float, Optional[PoolsItems]]
                for location_candidate in discriminators_by_level[self.game_state.level][collider_name]:
                    location: PoolsLocations = location_candidate[0]
                    operator: str = location_candidate[1]
                    value: float = location_candidate[2]
                    item_required: Optional[PoolsItems] = location_candidate[3]

                    comparison_value: float

                    if operator == "X":
                        comparison_value = self.game_state.coordinates[0]
                    elif operator == "Y":
                        comparison_value = self.game_state.coordinates[1]
                    elif operator == "Z":
                        comparison_value = self.game_state.coordinates[2]

                    distance: float = abs(comparison_value - value)

                    if distance < best_distance:
                        best_distance = distance
                        best_location_candidate = location
                        best_location_item_required = item_required

                if best_location_item_required is not None:
                    is_in_water_required: List[PoolsItems] = [
                        PoolsItems.POOLS_2T,
                        PoolsItems.POOLS_3T,
                        PoolsItems.POOLS_4T,
                        PoolsItems.POOLS_6T,
                    ]

                    if self.received_items.get(best_location_item_required, 0) < 1:
                        best_location_candidate = None
                    elif best_location_item_required in is_in_water_required and not self.game_state.is_in_water:
                        best_location_candidate = None

                if best_location_candidate is not None:
                    checked_locations.append(best_location_candidate)

        location: PoolsLocations
        for location in checked_locations:
            if location not in self.completed_locations and location not in self.completed_locations_queue:
                self.completed_locations.add(location)
                self.completed_locations_queue.append(location)

    def _process_received_items(self) -> None:
        while len(self.received_items_queue) > 0:
            item: PoolsItems = self.received_items_queue.popleft()

            if item not in self.received_items:
                self.received_items[item] = 0

            self.received_items[item] += 1

        if self.should_prepare_processed_trap_counters:
            self.should_prepare_processed_trap_counters = False

            item: PoolsItems
            item_count: int
            for item, item_count in self.received_items.items():
                if item.value.endswith(" Trap"):
                    self.processed_trap_counters[PoolsTrapTypes(item.value)] = item_count

    def _manage_traps(self) -> None:
        if not self.game_state.is_valid:
            return

        if not self.game_state.is_in_level:
            return

        now_timestamp: int = int(time.time())

        trap_type: PoolsTrapTypes
        expiry_timestamp: int
        for trap_type, expiry_timestamp in self.active_trap_timestamps.items():
            if expiry_timestamp is not None:
                if now_timestamp >= expiry_timestamp:
                    if trap_type == PoolsTrapTypes.NO_LOOK:
                        self.game_state_manager.disable_no_look_trap()
                    elif trap_type == PoolsTrapTypes.REWIND:
                        self.game_state_manager.disable_rewind_trap()
                    elif trap_type == PoolsTrapTypes.SLOW:
                        self.game_state_manager.disable_slow_trap()
                    elif trap_type == PoolsTrapTypes.WET:
                        self.game_state_manager.disable_wet_trap()

                    self.active_trap_timestamps[trap_type] = None

        item: PoolsItems
        item_count: int
        for item, item_count in self.received_items.items():
            if item.value.endswith(" Trap"):
                trap_type: PoolsTrapTypes = PoolsTrapTypes(item.value)

                if item_count > self.processed_trap_counters[trap_type]:
                    expiry_timestamp: int = int(time.time()) + self.option_trap_duration

                    if trap_type == PoolsTrapTypes.NO_LOOK:
                        if self.active_trap_timestamps[trap_type] is None:
                            if self.game_state_manager.enable_no_look_trap():
                                self.active_trap_timestamps[trap_type] = expiry_timestamp
                                self.processed_trap_counters[trap_type] += 1
                    elif trap_type == PoolsTrapTypes.REWIND:
                        if self.active_trap_timestamps[trap_type] is None:
                            if self.game_state_manager.enable_rewind_trap():
                                expiry_timestamp -= self.option_trap_duration // 2

                                self.active_trap_timestamps[trap_type] = expiry_timestamp
                                self.processed_trap_counters[trap_type] += 1
                    elif trap_type == PoolsTrapTypes.SLOW:
                        if self.active_trap_timestamps[trap_type] is None:
                            if self.game_state_manager.enable_slow_trap():
                                self.active_trap_timestamps[trap_type] = expiry_timestamp
                                self.processed_trap_counters[trap_type] += 1
                    elif trap_type == PoolsTrapTypes.WET:
                        if self.active_trap_timestamps[trap_type] is None:
                            if self.game_state_manager.enable_wet_trap():
                                self.active_trap_timestamps[trap_type] = expiry_timestamp
                                self.processed_trap_counters[trap_type] += 1

        if self.active_trap_timestamps[PoolsTrapTypes.WET] is not None:
            self.game_state_manager.enable_wet_trap()

    def _check_for_victory(self) -> None:
        if PoolsItems.RUBBER_DUCK in self.received_items:
            if self.received_items[PoolsItems.RUBBER_DUCK] >= self.option_rubber_ducks_required:
                if self.option_goal == PoolsGoals.RUBBER_DUCKS_COMPLETE_LEVEL_6:
                    if self.game_state.level == PoolsLevels.ENDING:
                        self.goal_completed = True

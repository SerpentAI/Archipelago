from typing import Dict, List, Optional, Set, Tuple

import collections
import logging
import time


from .data_funcs import items_with_tag
from .data.game_data import TwentyMinutesWeaponData
from .data.location_data import kill_count_checkpoints_by_chunk, level_checkpoints_by_chunk, survival_minutes_by_chunk


from .enums import (
    TwentyMinutesCharacters,
    TwentyMinutesGoalOptions,
    TwentyMinutesMapOptions,
    TwentyMinutesMaps,
    TwentyMinutesRunes,
    TwentyMinutesTags,
    TwentyMinutesTrapTypes,
    TwentyMinutesWeapons,
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
    game_state: Optional[GameState]

    # Generation Options
    option_goal: Optional[TwentyMinutesGoalOptions]
    option_forbidden_tomes_total: Optional[int]
    option_forbidden_tomes_required: Optional[int]
    option_character_selection: Optional[Dict[TwentyMinutesCharacters, bool]]
    option_character_count: Optional[int]
    option_weapon_selection: Optional[Dict[TwentyMinutesWeapons, bool]]
    option_weapon_count: Optional[int]
    option_starting_map: Optional[TwentyMinutesMapOptions]
    option_starting_darkness: Optional[int]
    option_maximum_survivable_darkness: Optional[int]
    option_randomize_weapon_attributes: Optional[bool]
    option_weapon_attribute_randomization_chance: Optional[int]
    option_trap_percentage: Optional[int]
    option_trap_weights: Optional[Dict[TwentyMinutesTrapTypes, int]]
    option_death_link: Optional[bool]

    # Generation Data
    selected_characters: Optional[List[TwentyMinutesCharacters]]
    selected_starting_character: Optional[TwentyMinutesCharacters]
    selected_weapons: Optional[List[TwentyMinutesWeapons]]
    selected_starting_weapon: Optional[TwentyMinutesWeapons]
    selected_starting_map: Optional[TwentyMinutesMaps]
    selected_full_run_map: Optional[TwentyMinutesMaps]
    weapon_data: Optional[Dict[TwentyMinutesWeapons, TwentyMinutesWeaponData]]

    # State
    previous_is_in_menu: bool
    previous_is_in_run: bool

    menu_entry_pending: bool
    run_entry_pending: bool

    previous_unlocked_characters: Optional[List[TwentyMinutesCharacters]]
    previous_unlocked_weapons: Optional[List[TwentyMinutesWeapons]]
    previous_available_maps: Optional[List[TwentyMinutesMaps]]
    previous_darkness_level: Optional[int]
    previous_rune_levels: Optional[Dict[TwentyMinutesRunes, int]]
    previous_run_time_elapsed: Optional[float]

    run_survival_locations: List[Tuple[str, float]]
    run_survive_the_run_locations: List[str]
    run_level_locations: List[Tuple[str, int]]
    run_kill_count_locations: List[Tuple[str, int]]

    run_applied_heart_containers: int
    run_applied_soul_heart_capacity: int
    run_horde_trap_pre_multiplier: Optional[float]

    pending_death_link: Tuple[bool, Optional[str], Optional[str]]
    outgoing_death_link: Tuple[bool, Optional[str]]
    pause_death_monitoring: bool

    should_prepare_processed_filler_counters: bool
    processed_filler_counters: Dict[str, int]

    should_prepare_processed_trap_counters: bool
    processed_trap_counters: Dict[TwentyMinutesTrapTypes, int]
    active_trap_timestamps: Dict[TwentyMinutesTrapTypes, Optional[int]]

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
        self.option_forbidden_tomes_total = None
        self.option_forbidden_tomes_required = None
        self.option_character_selection = None
        self.option_character_count = None
        self.option_weapon_selection = None
        self.option_weapon_count = None
        self.option_starting_map = None
        self.option_starting_darkness = None
        self.option_maximum_survivable_darkness = None
        self.option_randomize_weapon_attributes = None
        self.option_weapon_attribute_randomization_chance = None
        self.option_trap_percentage = None
        self.option_trap_weights = None
        self.option_death_link = None

        self.selected_characters = None
        self.selected_starting_character = None
        self.selected_weapons = None
        self.selected_starting_weapon = None
        self.selected_starting_map = None
        self.selected_full_run_map = None
        self.weapon_data = None

        self.previous_is_in_menu = False
        self.previous_is_in_run = False

        self.menu_entry_pending = False
        self.run_entry_pending = False

        self.previous_unlocked_characters = None
        self.previous_unlocked_weapons = None
        self.previous_available_maps = None
        self.previous_darkness_level = None
        self.previous_rune_levels = None
        self.previous_run_time_elapsed = None

        self.run_survival_locations = list()
        self.run_survive_the_run_locations = list()
        self.run_level_locations = list()
        self.run_kill_count_locations = list()

        self.run_applied_heart_containers = 0
        self.run_applied_soul_heart_capacity = 0
        self.run_horde_trap_pre_multiplier = None

        self.pending_death_link = (False, None, None)
        self.outgoing_death_link = (False, None)
        self.pause_death_monitoring = False

        self.should_prepare_processed_filler_counters = True

        self.processed_filler_counters = {
            filler_item_name: 0 for filler_item_name in items_with_tag(TwentyMinutesTags.FILLER_ITEM)
        }

        self.should_prepare_processed_trap_counters = True

        self.processed_trap_counters = {
            TwentyMinutesTrapTypes.HORDE: 0,
            TwentyMinutesTrapTypes.PARALYSIS: 0,
            TwentyMinutesTrapTypes.WEAPON_MALFUNCTION: 0,
            TwentyMinutesTrapTypes.WOUND: 0,
        }

        self.active_trap_timestamps = {
            TwentyMinutesTrapTypes.HORDE: None,
            TwentyMinutesTrapTypes.PARALYSIS: None,
            TwentyMinutesTrapTypes.WEAPON_MALFUNCTION: None,
            TwentyMinutesTrapTypes.WOUND: None,
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
                if not self.game_state_manager.install_main_thread_dispatcher():
                    return

                self._refresh_game_state()

                if self.game_state is None or not self.game_state.is_valid:
                    self.previous_is_in_menu = False
                    self.previous_is_in_run = False

                    return

                self._apply_conditional_game_state()

                self._check_for_completed_locations()
                self._process_received_items()

                if (self.option_trap_percentage or 0) > 0:
                    self._manage_traps()

                self._manage_filler()

                if self.option_death_link:
                    self._handle_death_link()

                self._check_for_victory()
            except Exception:
                import traceback

                with open("20_minutes_till_dawn_errors.log", "a") as f:
                    f.write(traceback.format_exc() + "\n\n")

    def reset(self) -> None:
        self.received_items = dict()
        self.completed_locations = set()

        self.completed_locations_queue = collections.deque()
        self.received_items_queue = collections.deque()

        self.goal_completed = False

        self.game_state = None

        self.option_goal = None
        self.option_forbidden_tomes_total = None
        self.option_forbidden_tomes_required = None
        self.option_character_selection = None
        self.option_character_count = None
        self.option_weapon_selection = None
        self.option_weapon_count = None
        self.option_starting_map = None
        self.option_starting_darkness = None
        self.option_maximum_survivable_darkness = None
        self.option_randomize_weapon_attributes = None
        self.option_weapon_attribute_randomization_chance = None
        self.option_trap_percentage = None
        self.option_trap_weights = None
        self.option_death_link = None

        self.selected_characters = None
        self.selected_starting_character = None
        self.selected_weapons = None
        self.selected_starting_weapon = None
        self.selected_starting_map = None
        self.selected_full_run_map = None
        self.weapon_data = None

        self.previous_is_in_menu = False
        self.previous_is_in_run = False

        self.menu_entry_pending = False
        self.run_entry_pending = False

        self.previous_unlocked_characters = None
        self.previous_unlocked_weapons = None
        self.previous_available_maps = None
        self.previous_darkness_level = None
        self.previous_rune_levels = None
        self.previous_run_time_elapsed = None

        self.run_survival_locations = list()
        self.run_survive_the_run_locations = list()
        self.run_level_locations = list()
        self.run_kill_count_locations = list()

        self.run_applied_heart_containers = 0
        self.run_applied_soul_heart_capacity = 0
        self.run_horde_trap_pre_multiplier = None

        self.pending_death_link = (False, None, None)
        self.outgoing_death_link = (False, None)
        self.pause_death_monitoring = False

        self.should_prepare_processed_filler_counters = True

        self.processed_filler_counters = {
            filler_item_name: 0 for filler_item_name in items_with_tag(TwentyMinutesTags.FILLER_ITEM)
        }

        self.should_prepare_processed_trap_counters = True

        self.processed_trap_counters = {
            TwentyMinutesTrapTypes.HORDE: 0,
            TwentyMinutesTrapTypes.PARALYSIS: 0,
            TwentyMinutesTrapTypes.WEAPON_MALFUNCTION: 0,
            TwentyMinutesTrapTypes.WOUND: 0,
        }

        self.active_trap_timestamps = {
            TwentyMinutesTrapTypes.HORDE: None,
            TwentyMinutesTrapTypes.PARALYSIS: None,
            TwentyMinutesTrapTypes.WEAPON_MALFUNCTION: None,
            TwentyMinutesTrapTypes.WOUND: None,
        }

    def _refresh_game_state(self) -> None:
        if self.game_state is not None:
            self.previous_is_in_menu = bool(self.game_state.is_in_menu)
            self.previous_is_in_run = bool(self.game_state.is_in_run)
        else:
            self.previous_is_in_menu = False
            self.previous_is_in_run = False

        self.game_state = self.game_state_manager.determine_game_state()

    def _apply_conditional_game_state(self) -> None:
        if self.game_state.is_in_menu:
            if not self.previous_is_in_menu:
                self.menu_entry_pending = True

            # Characters
            unlocked_characters: List[TwentyMinutesCharacters] = list()

            character: TwentyMinutesCharacters
            for character in self.selected_characters:
                character_unlock_item_name: str = f"Character Unlock: {character.value}"

                if self.received_items.get(character_unlock_item_name, 0) >= 1:
                    unlocked_characters.append(character)

            # Weapons
            unlocked_weapons: List[TwentyMinutesWeapons] = list()

            weapon: TwentyMinutesWeapons
            for weapon in self.selected_weapons:
                weapon_unlock_item_name: str = f"Weapon Unlock: {weapon.value}"

                if self.received_items.get(weapon_unlock_item_name, 0) >= 1:
                    unlocked_weapons.append(weapon)

            # Maps
            available_maps: List[TwentyMinutesMaps] = list()

            map_: TwentyMinutesMaps
            for map_ in TwentyMinutesMaps:
                map_unlock_item_name: str = f"Map Unlock: {map_.value}"

                if self.received_items.get(map_unlock_item_name, 0) >= 1:
                    available_maps.append(map_)

            # Darkness
            darkness_reduction_count: int = self.received_items.get("Progressive Darkness Reduction", 0)
            darkness_level: int = max(0, (self.option_starting_darkness or 0) - darkness_reduction_count)

            # Runes
            rune_levels: Dict[TwentyMinutesRunes, int] = dict()

            rune: TwentyMinutesRunes
            for rune in TwentyMinutesRunes:
                three_point_count: int = self.received_items.get(f"3 Rune Points: {rune.value}", 0)
                one_point_count: int = self.received_items.get(f"1 Rune Point: {rune.value}", 0)

                rune_levels[rune] = min(5, (three_point_count * 3) + one_point_count)

            if self.menu_entry_pending:
                self.game_state_manager.create_archipelago_label()
                self.game_state_manager.hide_unsupported_game_modes()

                self.game_state_manager.set_unlocked_characters(list(TwentyMinutesCharacters))
                self.game_state_manager.set_unlocked_weapons(list(TwentyMinutesWeapons))

                if self.weapon_data is not None:
                    self.game_state_manager.set_all_weapon_data(self.weapon_data)

                self.menu_entry_pending = False

            if unlocked_characters != self.previous_unlocked_characters:
                if self.game_state_manager.set_unlocked_characters(unlocked_characters):
                    self.previous_unlocked_characters = unlocked_characters

            if unlocked_weapons != self.previous_unlocked_weapons:
                if self.game_state_manager.set_unlocked_weapons(unlocked_weapons):
                    self.previous_unlocked_weapons = unlocked_weapons

            if available_maps != self.previous_available_maps:
                if self.game_state_manager.set_available_maps(available_maps):
                    self.previous_available_maps = available_maps

            if darkness_level != self.previous_darkness_level:
                if self.game_state_manager.set_darkness_level(darkness_level):
                    self.previous_darkness_level = darkness_level

            if rune_levels != self.previous_rune_levels:
                if self.game_state_manager.set_rune_levels(rune_levels):
                    self.previous_rune_levels = rune_levels
        elif self.game_state.is_in_run:
            time_elapsed: Optional[float] = self.game_state.time_elapsed

            is_new_run: bool = not self.previous_is_in_run

            if (
                not is_new_run
                and time_elapsed is not None
                and self.previous_run_time_elapsed is not None
                and time_elapsed < self.previous_run_time_elapsed
            ):
                is_new_run = True

            self.previous_run_time_elapsed = time_elapsed

            if is_new_run:
                self.run_entry_pending = True

                self.previous_unlocked_characters = None
                self.previous_unlocked_weapons = None
                self.previous_available_maps = None
                self.previous_darkness_level = None
                self.previous_rune_levels = None

                self.game_state_manager.disable_paralysis_trap()
                self.game_state_manager.disable_weapon_malfunction_trap()
                self.game_state_manager.disable_wound_trap()

            if self.run_entry_pending:
                self.run_applied_heart_containers = 0
                self.run_applied_soul_heart_capacity = 0
                self.run_horde_trap_pre_multiplier = None
                self.pause_death_monitoring = False

                self.active_trap_timestamps = {
                    TwentyMinutesTrapTypes.HORDE: None,
                    TwentyMinutesTrapTypes.PARALYSIS: None,
                    TwentyMinutesTrapTypes.WEAPON_MALFUNCTION: None,
                    TwentyMinutesTrapTypes.WOUND: None,
                }

                self.run_survival_locations = list()
                self.run_survive_the_run_locations = list()
                self.run_level_locations = list()
                self.run_kill_count_locations = list()

                if self.game_state.current_map is not None:
                    map_name: str = self.game_state.current_map.value
                    is_full_run_map: bool = self.game_state.current_map == self.selected_full_run_map
                    included_segment_count: int = 5 if is_full_run_map else 3

                    chunk_index: int
                    chunk_kill_counts: Tuple[int, int, int]
                    for chunk_index, chunk_kill_counts in enumerate(kill_count_checkpoints_by_chunk[:included_segment_count]):
                        kill_count: int
                        for kill_count in chunk_kill_counts:
                            self.run_kill_count_locations.append((f"{map_name} - {kill_count} Kills", kill_count))

                    unit_names: List[str] = list()

                    if self.game_state.character is not None:
                        unit_names.append(self.game_state.character.value)

                    if self.game_state.weapon is not None:
                        unit_names.append(self.game_state.weapon.value)

                    unit_name: str
                    for unit_name in unit_names:
                        chunk_minutes: List[int]
                        for chunk_index, chunk_minutes in enumerate(survival_minutes_by_chunk[:included_segment_count]):
                            minutes: int
                            for minutes in chunk_minutes:
                                if not is_full_run_map and chunk_index == 2 and minutes == 11:
                                    self.run_survive_the_run_locations.append(f"{map_name} - {unit_name} - Survive the Run")
                                    continue

                                minute_word: str = "Minute" if minutes == 1 else "Minutes"

                                self.run_survival_locations.append((f"{map_name} - {unit_name} - Survive {minutes} {minute_word}", minutes * 60.0))

                        chunk_levels: List[int]
                        for chunk_levels in level_checkpoints_by_chunk[:included_segment_count]:
                            level: int
                            for level in chunk_levels:
                                self.run_level_locations.append((f"{map_name} - {unit_name} - Reach Level {level}", level))

                    progressive_timer_count: int = self.received_items.get(f"Progressive Timer: {map_name}", 0)
                    self.game_state_manager.set_time_limit(240.0 * (1 + progressive_timer_count))

                    self.run_entry_pending = False

            if self.game_state.character is not None:
                # Powerup Choices
                progressive_powerup_choices_count: int = self.received_items.get(f"Progressive Powerup Choices: {self.game_state.character.value}", 0)
                self.game_state_manager.set_number_of_powerup_choices(1 + progressive_powerup_choices_count)

                # Heart Containers
                heart_container_count: int = self.received_items.get(f"Heart Container: {self.game_state.character.value}", 0)
                heart_container_delta: int = heart_container_count - self.run_applied_heart_containers

                if heart_container_delta > 0:
                    self.game_state_manager.set_maximum_health_base(self.game_state.maximum_health_base + heart_container_delta)
                    self.game_state_manager.set_maximum_health(self.game_state.maximum_health + heart_container_delta)
                    self.game_state_manager.set_current_health(self.game_state.current_health + heart_container_delta)

                    self.run_applied_heart_containers = heart_container_count

                # Soul Heart Capacity
                soul_heart_capacity_count: int = self.received_items.get(f"Soul Heart Capacity: {self.game_state.character.value}", 0)
                soul_heart_capacity_delta: int = soul_heart_capacity_count - self.run_applied_soul_heart_capacity

                if soul_heart_capacity_delta > 0:
                    self.game_state_manager.set_maximum_temporary_health(self.game_state.maximum_temporary_health + soul_heart_capacity_delta)

                    self.run_applied_soul_heart_capacity = soul_heart_capacity_count

    def _check_for_completed_locations(self) -> None:
        if not self.game_state.is_in_run:
            return

        checked_locations: List[str] = list()

        if self.game_state.time_elapsed is not None:
            survival_location_name: str
            seconds: float
            for survival_location_name, seconds in self.run_survival_locations:
                if self.game_state.time_elapsed >= seconds:
                    checked_locations.append(survival_location_name)

            if self.game_state.time_elapsed >= 720.0:
                checked_locations.extend(self.run_survive_the_run_locations)

        if self.game_state.player_level is not None:
            level_location_name: str
            level: int
            for level_location_name, level in self.run_level_locations:
                if self.game_state.player_level >= level:
                    checked_locations.append(level_location_name)

        if self.game_state.enemy_kill_count is not None:
            kill_count_location_name: str
            kill_count: int
            for kill_count_location_name, kill_count in self.run_kill_count_locations:
                if self.game_state.enemy_kill_count >= kill_count:
                    checked_locations.append(kill_count_location_name)

        location_name: str
        for location_name in checked_locations:
            if location_name in self.completed_locations:
                continue

            self.completed_locations.add(location_name)
            self.completed_locations_queue.append(location_name)

    def _process_received_items(self) -> None:
        while len(self.received_items_queue) > 0:
            item: str = self.received_items_queue.popleft()

            if item not in self.received_items:
                self.received_items[item] = 0

            self.received_items[item] += 1

        if self.should_prepare_processed_filler_counters:
            self.should_prepare_processed_filler_counters = False

            item: str
            item_count: int
            for item, item_count in self.received_items.items():
                if item in self.processed_filler_counters:
                    self.processed_filler_counters[item] = item_count

        if self.should_prepare_processed_trap_counters:
            self.should_prepare_processed_trap_counters = False

            item: str
            item_count: int
            for item, item_count in self.received_items.items():
                if item.endswith(" Trap"):
                    self.processed_trap_counters[TwentyMinutesTrapTypes(item)] = item_count

    def _manage_filler(self) -> None:
        if not self.game_state.is_in_run:
            return

        if self.game_state.current_health is None or self.game_state.current_health <= 0:
            return

        heal_one_heart_delta: int = self.received_items.get("Heal 1 Heart", 0) - self.processed_filler_counters.get("Heal 1 Heart", 0)
        full_heal_delta: int = self.received_items.get("Full Heal", 0) - self.processed_filler_counters.get("Full Heal", 0)
        soul_heart_delta: int = self.received_items.get("Soul Heart", 0) - self.processed_filler_counters.get("Soul Heart", 0)

        if heal_one_heart_delta > 0 or full_heal_delta > 0:
            target_health: int = self.game_state.current_health + heal_one_heart_delta

            if full_heal_delta > 0:
                target_health = self.game_state.maximum_health

            target_health = min(target_health, self.game_state.maximum_health)

            if self.game_state_manager.set_current_health(target_health):
                self.processed_filler_counters["Heal 1 Heart"] = self.received_items.get("Heal 1 Heart", 0)
                self.processed_filler_counters["Full Heal"] = self.received_items.get("Full Heal", 0)

        if soul_heart_delta > 0:
            target_temporary_health: int = min(
                self.game_state.current_temporary_health + soul_heart_delta,
                self.game_state.maximum_temporary_health,
            )

            if self.game_state_manager.set_current_temporary_health(target_temporary_health):
                self.processed_filler_counters["Soul Heart"] = self.received_items.get("Soul Heart", 0)

    def _manage_traps(self) -> None:
        if not self.game_state.is_in_run:
            return

        if self.game_state.current_health is None or self.game_state.current_health <= 0:
            return

        now_timestamp: int = int(time.time())

        trap_type: TwentyMinutesTrapTypes
        expiry_timestamp: Optional[int]
        for trap_type, expiry_timestamp in self.active_trap_timestamps.items():
            if expiry_timestamp is not None:
                if now_timestamp >= expiry_timestamp:
                    if trap_type == TwentyMinutesTrapTypes.HORDE:
                        if self.run_horde_trap_pre_multiplier is not None:
                            self.game_state_manager.disable_horde_trap(self.run_horde_trap_pre_multiplier)
                            self.run_horde_trap_pre_multiplier = None
                    elif trap_type == TwentyMinutesTrapTypes.PARALYSIS:
                        self.game_state_manager.disable_paralysis_trap()
                    elif trap_type == TwentyMinutesTrapTypes.WEAPON_MALFUNCTION:
                        self.game_state_manager.disable_weapon_malfunction_trap()
                    elif trap_type == TwentyMinutesTrapTypes.WOUND:
                        self.game_state_manager.disable_wound_trap()

                    self.active_trap_timestamps[trap_type] = None

        item: str
        item_count: int
        for item, item_count in self.received_items.items():
            if not item.endswith(" Trap"):
                continue

            trap_type = TwentyMinutesTrapTypes(item)

            if item_count <= self.processed_trap_counters.get(trap_type, 0):
                continue

            if self.active_trap_timestamps[trap_type] is not None:
                continue

            if trap_type == TwentyMinutesTrapTypes.HORDE:
                pre_trap_multiplier: Optional[float] = self.game_state_manager.get_spawn_rate_multiplier()

                if pre_trap_multiplier is None:
                    continue

                if self.game_state_manager.enable_horde_trap(pre_trap_multiplier * 10.0):
                    self.run_horde_trap_pre_multiplier = pre_trap_multiplier

                    self.active_trap_timestamps[trap_type] = now_timestamp + 15
                    self.processed_trap_counters[trap_type] = item_count
            elif trap_type == TwentyMinutesTrapTypes.PARALYSIS:
                if self.game_state_manager.enable_paralysis_trap():
                    self.active_trap_timestamps[trap_type] = now_timestamp + 5
                    self.processed_trap_counters[trap_type] = item_count
            elif trap_type == TwentyMinutesTrapTypes.WEAPON_MALFUNCTION:
                if self.game_state_manager.enable_weapon_malfunction_trap():
                    self.active_trap_timestamps[trap_type] = now_timestamp + 5
                    self.processed_trap_counters[trap_type] = item_count
            elif trap_type == TwentyMinutesTrapTypes.WOUND:
                if self.game_state_manager.enable_wound_trap():
                    self.active_trap_timestamps[trap_type] = now_timestamp
                    self.processed_trap_counters[trap_type] = item_count

    def _handle_death_link(self) -> None:
        if not self.game_state.is_in_run:
            return

        if self.game_state.current_health is None:
            return

        is_dead: bool = self.game_state.current_health <= 0

        # Pause Monitoring Flag
        if self.pause_death_monitoring and not is_dead:
            self.pause_death_monitoring = False

        # Incoming Death Link
        if not is_dead and self.pending_death_link[0]:
            if self.game_state_manager.kill_player():
                self.pending_death_link = (False, None, None)
                self.pause_death_monitoring = True

        # Outgoing Death Link
        if not self.pause_death_monitoring:
            if is_dead:
                death_cause: Optional[str] = None

                if self.game_state.character is not None:
                    death_cause = f"{self.game_state.character.value} died"

                self.outgoing_death_link = (True, death_cause)
                self.pause_death_monitoring = True

    def _check_for_victory(self) -> None:
        if "Forbidden Tome" in self.received_items:
            if self.received_items["Forbidden Tome"] >= (self.option_forbidden_tomes_required or 0):
                if self.option_goal == TwentyMinutesGoalOptions.FORBIDDEN_TOME_HUNT:
                    self.goal_completed = True
                elif self.option_goal == TwentyMinutesGoalOptions.FORBIDDEN_TOMES_FINAL_MAP:
                    if self.game_state.is_in_run:
                        if self.game_state.current_map == self.selected_full_run_map:
                            map_name: str = self.selected_full_run_map.value
                            progressive_timer_count: int = self.received_items.get(f"Progressive Timer: {map_name}", 0)

                            if progressive_timer_count >= 4:
                                if self.game_state.time_elapsed is not None and self.game_state.time_elapsed >= 1200.0:
                                    self.goal_completed = True

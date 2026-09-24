from typing import Dict, List, Optional, Set

import collections
import logging

from .enums import (
    DayOfTheTentacleCharacterOptions,
    DayOfTheTentacleCharacters,
    DayOfTheTentacleEvents,
    DayOfTheTentacleGoalOptions,
    DayOfTheTentacleItems,
    DayOfTheTentacleLocations,
    DayOfTheTentacleRooms,
    DayOfTheTentacleTags,
    DayOfTheTentacleVoiceLines,
)

from .data.game_data import (
    character_item_to_character,
    item_to_internal_object_and_room_id,
    items_hidden_during_the_intro,
    items_removed_when_a_save_is_set_up,
    location_to_event,
    location_to_picked_up_item,
    location_to_visited_room,
    location_to_voice_line,
    locations_removed_under_the_heist_goal,
    room_to_character,
)

from .data.location_data import DayOfTheTentacleLocationData, location_data

from .game_state_manager import GameStateManager, GameState


class GameController:
    logger: Optional[logging.Logger]

    game_state_manager: GameStateManager

    received_items: Dict[DayOfTheTentacleItems, int]
    completed_locations: Set[DayOfTheTentacleLocations]

    completed_locations_queue: collections.deque
    received_items_queue: collections.deque

    goal_completed: bool

    logged_errors: Set[str]

    # Game State
    game_state: Optional[GameState]

    # Generation Options
    option_goal: Optional[DayOfTheTentacleGoalOptions]
    option_swiss_deposits_total: Optional[int]
    option_swiss_deposits_required: Optional[int]
    option_starting_character: Optional[DayOfTheTentacleCharacterOptions]
    option_include_room_visits: Optional[bool]
    option_include_voice_lines: Optional[bool]

    def __init__(self, logger: logging.Logger = None) -> None:
        self.logger = logger

        self.game_state_manager = GameStateManager()

        self.received_items = dict()
        self.completed_locations = set()

        self.completed_locations_queue = collections.deque()
        self.received_items_queue = collections.deque()

        self.goal_completed = False

        self.logged_errors = set()

        self.game_state = None

        self.option_goal = None
        self.option_swiss_deposits_total = None
        self.option_swiss_deposits_required = None
        self.option_starting_character = None
        self.option_include_room_visits = None
        self.option_include_voice_lines = None

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
        if self.game_state_manager.is_process_still_running():
            return True

        self.game_state = None

        return False

    def update(self) -> None:
        if self.game_state_manager.is_process_still_running():
            try:
                self._refresh_game_state()

                if not self.game_state.is_valid:
                    return

                if self.option_goal is None:
                    return

                self._apply_permanent_game_state()
                self._set_up_save()

                self._check_for_completed_locations()
                self._process_received_items()
                self._check_for_victory()
            except Exception:
                import traceback

                error: str = traceback.format_exc()

                if error not in self.logged_errors:
                    self.logged_errors.add(error)

                    with open("day_of_the_tentacle_errors.log", "a") as f:
                        f.write(error + "\n\n")

    def reset(self) -> None:
        self.received_items = dict()
        self.completed_locations = set()

        self.completed_locations_queue = collections.deque()
        self.received_items_queue = collections.deque()

        self.goal_completed = False

        self.game_state = None

        self.option_goal = None
        self.option_swiss_deposits_total = None
        self.option_swiss_deposits_required = None
        self.option_starting_character = None
        self.option_include_room_visits = None
        self.option_include_voice_lines = None

    def _refresh_game_state(self) -> None:
        self.game_state = self.game_state_manager.determine_game_state()

    def _apply_permanent_game_state(self) -> None:
        if self.game_state.is_in_intro:
            self.game_state_manager.hide_items(list(items_hidden_during_the_intro))

            self.game_state_manager.block_leaving_the_basement_lab()

            return

        items_to_show: List[DayOfTheTentacleItems] = list()

        location: DayOfTheTentacleLocations
        item: DayOfTheTentacleItems
        for location, item in location_to_picked_up_item.items():
            if item in items_hidden_during_the_intro and location not in self.completed_locations:
                items_to_show.append(item)

        self.game_state_manager.show_items(items_to_show)

        released_items: List[DayOfTheTentacleItems] = list()

        for item in self.game_state.granted_items:
            if item not in location_to_picked_up_item.values():
                released_items.append(item)

        for location, item in location_to_picked_up_item.items():
            if location in self.completed_locations and item in self.game_state.granted_items:
                released_items.append(item)

        self.game_state_manager.intercept_item_pickups(released_items)
        self.game_state_manager.restore_consumed_items()
        self.game_state_manager.return_retaken_items()

        self.game_state_manager.block_guarded_sentences()
        self.game_state_manager.complete_blocked_sentences()
        self.game_state_manager.keep_laverne_disguised()
        self.game_state_manager.bring_back_the_name_tag_tentacle()
        self.game_state_manager.show_the_attic_rope_under_a_raised_ted()
        self.game_state_manager.check_pickups_left_unreachable()
        self.game_state_manager.keep_the_battery_charged()
        self.game_state_manager.keep_the_coffee_pots_paired()

        unlocked_characters: List[DayOfTheTentacleCharacters] = [DayOfTheTentacleCharacters[self.option_starting_character.name]]

        item: DayOfTheTentacleItems
        character: DayOfTheTentacleCharacters
        for item, character in character_item_to_character.items():
            if item in self.received_items:
                unlocked_characters.append(character)

        self.game_state_manager.set_unlocked_characters(unlocked_characters)

        if DayOfTheTentacleCharacters.LAVERNE in unlocked_characters:
            self.game_state_manager.free_laverne_from_the_tree()

        diamond_order_refusal: Optional[bytes] = None

        if self.option_goal == DayOfTheTentacleGoalOptions.SWISS_BANK_HEIST:
            diamond_order_refusal = b"Why buy a diamond when I could just keep the money?"
        elif self.received_items.get(DayOfTheTentacleItems.SWISS_DEPOSIT, 0) < self.option_swiss_deposits_required:
            diamond_order_refusal = b"I'd better wait until there's more money in that Swiss account."

        self.game_state_manager.block_guarded_scripts(diamond_order_refusal)
        self.game_state_manager.complete_refused_scripts()

    def _set_up_save(self) -> None:
        if self.game_state.is_in_intro or self.game_state.is_save_set_up:
            return

        results: List[bool] = list()

        item: DayOfTheTentacleItems
        for item in items_removed_when_a_save_is_set_up:
            results.append(self.game_state_manager.remove_item(item))

        starting_character: DayOfTheTentacleCharacters = DayOfTheTentacleCharacters[self.option_starting_character.name]

        if starting_character == DayOfTheTentacleCharacters.LAVERNE:
            results.append(self.game_state_manager.free_laverne_from_the_tree())

        if self.game_state.character != starting_character:
            results.append(self.game_state_manager.switch_character(starting_character))

        if all(results):
            self.game_state_manager.mark_save_as_set_up()

    def _check_for_completed_locations(self) -> None:
        if self.game_state.is_in_intro:
            return

        checked_locations: List[DayOfTheTentacleLocations] = list()

        location: DayOfTheTentacleLocations

        event: DayOfTheTentacleEvents
        for location, event in location_to_event.items():
            if event in self.game_state.events:
                checked_locations.append(location)

        item: DayOfTheTentacleItems
        for location, item in location_to_picked_up_item.items():
            if item in self.game_state.picked_up_items:
                checked_locations.append(location)

        room: DayOfTheTentacleRooms
        for location, room in location_to_visited_room.items():
            if room == self.game_state.room and room_to_character[room] == self.game_state.character:
                checked_locations.append(location)

        voice_line: DayOfTheTentacleVoiceLines
        for location, voice_line in location_to_voice_line.items():
            if voice_line in self.game_state.spoken_voice_lines:
                checked_locations.append(location)

        for location in checked_locations:
            data: DayOfTheTentacleLocationData = location_data[location]

            if not self.option_include_room_visits and DayOfTheTentacleTags.VISITED_LOCATION in data.tags:
                continue

            if not self.option_include_voice_lines and DayOfTheTentacleTags.VOICE_LINE_LOCATION in data.tags:
                continue

            if self.option_goal == DayOfTheTentacleGoalOptions.SWISS_BANK_HEIST:
                if location in locations_removed_under_the_heist_goal:
                    continue

            if location not in self.completed_locations and location not in self.completed_locations_queue:
                self.completed_locations.add(location)
                self.completed_locations_queue.append(location)

    def _process_received_items(self) -> None:
        while len(self.received_items_queue) > 0:
            received_item: DayOfTheTentacleItems = self.received_items_queue.popleft()

            if received_item not in self.received_items:
                self.received_items[received_item] = 0

            self.received_items[received_item] += 1

        if self.game_state.is_in_intro or not self.game_state.is_save_set_up:
            return

        item: DayOfTheTentacleItems
        for item in self.received_items:
            if item not in item_to_internal_object_and_room_id:
                continue

            if item not in self.game_state.granted_items:
                self.game_state_manager.receive_item(item)

    def _check_for_victory(self) -> None:
        if self.option_goal == DayOfTheTentacleGoalOptions.STOP_PURPLE_TENTACLE:
            if DayOfTheTentacleEvents.COMPLETED_GAME in self.game_state.events:
                self.goal_completed = True
        elif self.option_goal == DayOfTheTentacleGoalOptions.SWISS_BANK_HEIST:
            if self.game_state.is_in_intro:
                return

            if self.received_items.get(DayOfTheTentacleItems.SWISS_DEPOSIT, 0) < self.option_swiss_deposits_required:
                return

            if DayOfTheTentacleItems.SWISS_BANKBOOK not in self.game_state.held_items:
                return

            if self.game_state.room == DayOfTheTentacleRooms.PRESENT_FRONT_YARD:
                if self.game_state.character == DayOfTheTentacleCharacters.BERNARD:
                    self.goal_completed = True

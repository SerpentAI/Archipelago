from typing import Any, Dict, List

import copy

from .data.item_data import DayOfTheTentacleItemData, item_data
from .data.location_data import DayOfTheTentacleLocationData, location_data

from .enums import (
    DayOfTheTentacleCharacterOptions,
    DayOfTheTentacleGoalOptions,
    DayOfTheTentacleItems,
    DayOfTheTentacleLocations,
    DayOfTheTentacleTags,
)


def id_to_goals() -> Dict[int, DayOfTheTentacleGoalOptions]:
    return {goal.value: goal for goal in DayOfTheTentacleGoalOptions}


def id_to_starting_characters() -> Dict[int, DayOfTheTentacleCharacterOptions]:
    return {character.value: character for character in DayOfTheTentacleCharacterOptions}


def id_to_items() -> Dict[int, DayOfTheTentacleItems]:
    return {data.archipelago_id: item for item, data in item_data.items()}


def id_to_locations() -> Dict[int, DayOfTheTentacleLocations]:
    return {data.archipelago_id: location for location, data in location_data.items()}


def item_groups() -> Dict[str, List[str]]:
    groups: Dict[str, List[str]] = dict()

    item: DayOfTheTentacleItems
    data: DayOfTheTentacleItemData
    for item, data in item_data.items():
        tag: DayOfTheTentacleTags
        for tag in data.tags:
            groups.setdefault(tag.value, list()).append(item.value)

    return groups


def item_names_to_id() -> Dict[str, int]:
    return {item.value: data.archipelago_id for item, data in item_data.items()}


def items_with_tag(tag: DayOfTheTentacleTags) -> List[DayOfTheTentacleItems]:
    return [item for item, data in item_data.items() if tag in data.tags]


def location_groups() -> Dict[str, List[str]]:
    groups: Dict[str, List[str]] = dict()

    location: DayOfTheTentacleLocations
    data: DayOfTheTentacleLocationData
    for location, data in location_data.items():
        tag: DayOfTheTentacleTags
        for tag in data.tags:
            groups.setdefault(tag.value, list()).append(location.value)

    return groups


def location_names_to_id() -> Dict[str, int]:
    return {location.value: data.archipelago_id for location, data in location_data.items()}


def locations_with_tag(tag: DayOfTheTentacleTags) -> List[DayOfTheTentacleLocations]:
    return [location for location, data in location_data.items() if tag in data.tags]


def process_slot_data(slot_data: Dict[str, Any]) -> Dict[str, Any]:
    slot_data_processed: Dict[str, Any] = copy.deepcopy(slot_data)

    slot_data_processed["goal"] = id_to_goals()[slot_data["goal"]]
    slot_data_processed["starting_character"] = id_to_starting_characters()[slot_data["starting_character"]]

    slot_data_processed["include_room_visits"] = bool(slot_data["include_room_visits"])
    slot_data_processed["include_voice_lines"] = bool(slot_data["include_voice_lines"])

    return slot_data_processed

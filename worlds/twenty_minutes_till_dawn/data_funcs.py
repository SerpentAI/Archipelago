from typing import Any, Dict, List

import copy

from .data.game_data import TwentyMinutesWeaponData
from .data.item_data import TwentyMinutesItemData, item_data
from .data.location_data import TwentyMinutesLocationData, location_data

from .enums import (
    TwentyMinutesCharacters,
    TwentyMinutesGoalOptions,
    TwentyMinutesMapOptions,
    TwentyMinutesMaps,
    TwentyMinutesTags,
    TwentyMinutesTrapTypes,
    TwentyMinutesWeapons,
)


def id_to_goals() -> Dict[int, TwentyMinutesGoalOptions]:
    return {goal.value: goal for goal in TwentyMinutesGoalOptions}


def id_to_starting_maps() -> Dict[int, TwentyMinutesMapOptions]:
    return {map_option.value: map_option for map_option in TwentyMinutesMapOptions}


def id_to_items() -> Dict[int, str]:
    return {data.archipelago_id: item for item, data in item_data.items()}


def id_to_locations() -> Dict[int, str]:
    return {
        data.archipelago_id: location
        for location, data in location_data.items()
        if data.archipelago_id is not None
    }


def item_groups() -> Dict[str, List[str]]:
    groups: Dict[str, List[str]] = dict()

    item: str
    data: TwentyMinutesItemData
    for item, data in item_data.items():
        if data.tags is not None:
            tag: TwentyMinutesTags
            for tag in data.tags:
                groups.setdefault(tag.value, list()).append(item)

    return {k: v for k, v in groups.items() if len(v)}


def item_names_to_id() -> Dict[str, int]:
    return {item: data.archipelago_id for item, data in item_data.items()}


def items_with_tag(tag: TwentyMinutesTags) -> List[str]:
    item: str
    data: TwentyMinutesItemData

    return [item for item, data in item_data.items() if data.tags is not None and tag in data.tags]


def location_groups() -> Dict[str, List[str]]:
    groups: Dict[str, List[str]] = dict()

    location: str
    data: TwentyMinutesLocationData
    for location, data in location_data.items():
        if data.tags is not None:
            tag: TwentyMinutesTags
            for tag in data.tags:
                groups.setdefault(tag.value, list()).append(location)

    return {k: v for k, v in groups.items() if len(v)}


def location_names_to_id() -> Dict[str, int]:
    return {
        location: data.archipelago_id
        for location, data in location_data.items()
        if data.archipelago_id is not None
    }


def locations_with_tag(tag: TwentyMinutesTags) -> List[str]:
    location: str
    data: TwentyMinutesLocationData

    return [location for location, data in location_data.items() if data.tags is not None and tag in data.tags]


def locations_with_tags(tags: List[TwentyMinutesTags]) -> List[str]:
    location: str
    data: TwentyMinutesLocationData

    return [
        location
        for location, data in location_data.items()
        if data.tags is not None and all(tag in data.tags for tag in tags)
    ]


def process_slot_data(slot_data: Dict[str, Any]) -> Dict[str, Any]:
    slot_data_processed: Dict[str, Any] = copy.deepcopy(slot_data)

    slot_data_processed["goal"] = id_to_goals()[slot_data["goal"]]
    slot_data_processed["starting_map"] = id_to_starting_maps()[slot_data["starting_map"]]

    slot_data_processed["character_selection"] = {
        TwentyMinutesCharacters(character_name): is_enabled
        for character_name, is_enabled in slot_data["character_selection"].items()
    }

    slot_data_processed["weapon_selection"] = {
        TwentyMinutesWeapons(weapon_name): is_enabled
        for weapon_name, is_enabled in slot_data["weapon_selection"].items()
    }

    trap_weights: Dict[TwentyMinutesTrapTypes, int] = dict()

    trap_type_name: str
    weight: int
    for trap_type_name, weight in slot_data["trap_weights"].items():
        trap_weights[TwentyMinutesTrapTypes(trap_type_name)] = weight

    slot_data_processed["trap_weights"] = trap_weights

    slot_data_processed["selected_characters"] = [
        TwentyMinutesCharacters(character_name) for character_name in slot_data["selected_characters"]
    ]

    slot_data_processed["selected_starting_character"] = TwentyMinutesCharacters(slot_data["selected_starting_character"])

    slot_data_processed["selected_weapons"] = [
        TwentyMinutesWeapons(weapon_name) for weapon_name in slot_data["selected_weapons"]
    ]

    slot_data_processed["selected_starting_weapon"] = TwentyMinutesWeapons(slot_data["selected_starting_weapon"])

    slot_data_processed["selected_starting_map"] = TwentyMinutesMaps(slot_data["selected_starting_map"])
    slot_data_processed["selected_full_run_map"] = TwentyMinutesMaps(slot_data["selected_full_run_map"])

    if slot_data["weapon_data"] is not None:
        weapon_data: Dict[TwentyMinutesWeapons, TwentyMinutesWeaponData] = dict()

        weapon_name: str
        field_dict: Dict[str, Any]
        for weapon_name, field_dict in slot_data["weapon_data"].items():
            weapon_data[TwentyMinutesWeapons(weapon_name)] = TwentyMinutesWeaponData(**field_dict)

        slot_data_processed["weapon_data"] = weapon_data

    return slot_data_processed

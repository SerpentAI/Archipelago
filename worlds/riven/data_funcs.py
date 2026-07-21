from typing import Any, Dict, List

import copy

from .data.item_data import RivenItemData, item_data
from .data.location_data import RivenLocationData, location_data

from .enums import (
    RivenAPGoals,
    RivenAPStartingMovementSpeeds,
    RivenAPStartingRoutes,
    RivenAPTags,
    RivenAPTrapTypes,
    RivenItems,
    RivenLocations,
)


def id_to_goals() -> Dict[int, RivenAPGoals]:
    return {goal.value: goal for goal in RivenAPGoals}


def id_to_starting_movement_speeds() -> Dict[int, RivenAPStartingMovementSpeeds]:
    return {speed.value: speed for speed in RivenAPStartingMovementSpeeds}


def id_to_items() -> Dict[int, RivenItems]:
    return {data.archipelago_id: item for item, data in item_data.items()}


def id_to_locations() -> Dict[int, RivenLocations]:
    return {
        data.archipelago_id: location
        for location, data in location_data.items()
        if data.archipelago_id is not None
    }


def item_groups() -> Dict[str, List[str]]:
    groups: Dict[str, List[str]] = dict()

    item: str
    data: RivenItemData
    for item, data in item_data.items():
        if data.tags is not None:
            tag: RivenAPTags
            for tag in data.tags:
                groups.setdefault(tag.value, list()).append(item.value)

    return {k: v for k, v in groups.items() if len(v)}


def item_names_to_id() -> Dict[str, int]:
    return {item.value: data.archipelago_id for item, data in item_data.items()}


def items_with_tag(tag: RivenAPTags) -> List[RivenItems]:
    item: str
    data: RivenItemData

    return [item for item, data in item_data.items() if data.tags is not None and tag in data.tags]


def location_groups() -> Dict[str, List[str]]:
    groups: Dict[str, List[str]] = dict()

    location: str
    data: RivenLocationData
    for location, data in location_data.items():
        if data.tags is not None:
            tag: RivenAPTags
            for tag in data.tags:
                groups.setdefault(tag.value, list()).append(location.value)

    return {k: v for k, v in groups.items() if len(v)}


def location_names_to_id() -> Dict[str, int]:
    return {
        location.value: data.archipelago_id
        for location, data in location_data.items()
        if data.archipelago_id is not None
    }


def locations_with_tag(tag: RivenAPTags) -> List[RivenLocations]:
    location: str
    data: RivenLocationData

    return [location for location, data in location_data.items() if data.tags is not None and tag in data.tags]


def process_slot_data(slot_data: Dict[str, Any]) -> Dict[str, Any]:
    slot_data_processed: Dict[str, Any] = copy.deepcopy(slot_data)

    slot_data_processed["goal"] = id_to_goals()[slot_data["goal"]]
    slot_data_processed["starting_movement_speed"] = id_to_starting_movement_speeds()[slot_data["starting_movement_speed"]]

    trap_weights: Dict[RivenAPTrapTypes, int] = dict()

    trap_type_name: str
    weight: int
    for trap_type_name, weight in slot_data["trap_weights"].items():
        trap_weights[RivenAPTrapTypes(trap_type_name)] = weight

    slot_data_processed["trap_weights"] = trap_weights

    slot_data_processed["selected_starting_route"] = RivenAPStartingRoutes(slot_data["selected_starting_route"])

    return slot_data_processed

from typing import Any, Dict, List

from .data.item_data import MirrorsEdgeItemData, item_data
from .data.location_data import MirrorsEdgeLocationData, location_data

from .enums import (
    MirrorsEdgeAPGoals,
    MirrorsEdgeAPLogic,
    MirrorsEdgeAPTags,
    MirrorsEdgeAPTrapTypes,
    MirrorsEdgeAbilities,
    MirrorsEdgeLevels,
)


def id_to_goals() -> Dict[int, MirrorsEdgeAPGoals]:
    return {goal.value: goal for goal in MirrorsEdgeAPGoals}


def id_to_items() -> Dict[int, str]:
    return {data.archipelago_id: item for item, data in item_data.items()}


def id_to_locations() -> Dict[int, str]:
    return {
        data.archipelago_id: location
        for location, data in location_data.items()
        if data.archipelago_id is not None
    }


def id_to_logic() -> Dict[int, MirrorsEdgeAPLogic]:
    return {logic.value: logic for logic in MirrorsEdgeAPLogic}


def item_groups() -> Dict[str, List[str]]:
    groups: Dict[str, List[str]] = dict()

    item: str
    data: MirrorsEdgeItemData
    for item, data in item_data.items():
        if data.tags is not None:
            tag: MirrorsEdgeAPTags
            for tag in data.tags:
                groups.setdefault(tag.value, list()).append(item)

    return {k: v for k, v in groups.items() if len(v)}


def item_names_to_id() -> Dict[str, int]:
    return {item: data.archipelago_id for item, data in item_data.items()}


def items_with_tag(tag: MirrorsEdgeAPTags) -> List[str]:
    item: str
    data: MirrorsEdgeItemData

    return [item for item, data in item_data.items() if data.tags is not None and tag in data.tags]


def location_groups() -> Dict[str, List[str]]:
    groups: Dict[str, List[str]] = dict()

    location: str
    data: MirrorsEdgeLocationData
    for location, data in location_data.items():
        if data.tags is not None:
            tag: MirrorsEdgeAPTags
            for tag in data.tags:
                groups.setdefault(tag.value, list()).append(location)

    return {k: v for k, v in groups.items() if len(v)}


def location_names_to_id() -> Dict[str, int]:
    return {
        location: data.archipelago_id
        for location, data in location_data.items()
        if data.archipelago_id is not None
    }


def locations_with_tag(tag: MirrorsEdgeAPTags) -> List[str]:
    location: str
    data: MirrorsEdgeLocationData

    return [location for location, data in location_data.items() if data.tags is not None and tag in data.tags]


def locations_with_tags(tags: List[MirrorsEdgeAPTags]) -> List[str]:
    location: str
    data: MirrorsEdgeLocationData

    return [
        location
        for location, data in location_data.items()
        if data.tags is not None and all(tag in data.tags for tag in tags)
    ]


def process_slot_data(slot_data: Dict[str, Any]) -> Dict[str, Any]:
    slot_data["goal"] = id_to_goals()[slot_data["goal"]]
    slot_data["logic"] = id_to_logic()[slot_data["logic"]]

    trap_weights: Dict[MirrorsEdgeAPTrapTypes, int] = dict()

    trap_type_name: str
    weight: int
    for trap_type_name, weight in slot_data["trap_weights"].items():
        trap_weights[MirrorsEdgeAPTrapTypes(trap_type_name)] = weight

    slot_data["trap_weights"] = trap_weights

    slot_data["starting_levels"] = [MirrorsEdgeLevels(level_name) for level_name in slot_data["starting_levels"]]
    slot_data["levels"] = [MirrorsEdgeLevels(level_name) for level_name in slot_data["levels"]]

    if slot_data["goal_level"] is not None:
        slot_data["goal_level"] = MirrorsEdgeLevels(slot_data["goal_level"])

    slot_data["starting_abilities"] = [MirrorsEdgeAbilities(ability_name) for ability_name in slot_data["starting_abilities"]]
    slot_data["abilities"] = [MirrorsEdgeAbilities(ability_name) for ability_name in slot_data["abilities"]]

    target_times: Dict[MirrorsEdgeLevels, List[int]] = dict()

    level_name: str
    level_target_times: List[int]
    for level_name, level_target_times in slot_data["target_times"].items():
        target_times[MirrorsEdgeLevels(level_name)] = level_target_times

    slot_data["target_times"] = target_times

    return slot_data

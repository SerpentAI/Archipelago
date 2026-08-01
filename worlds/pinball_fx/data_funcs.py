from typing import Any, Dict, List

import copy

from .data.item_data import PinballFXItemData, item_data
from .data.location_data import PinballFXLocationData, location_data
from .data.game_data import dlc_to_tables

from .enums import (
    PinballFXAPGoals,
    PinballFXAPRequirementModes,
    PinballFXAPTags,
    PinballFXAPTrapTypes,
    PinballFXDLC,
    PinballFXGameModes,
    PinballFXTables,
)


def generate_dlc_table_strings() -> List[str]:
    table_strings = list()

    dlc: PinballFXDLC
    tables: List[PinballFXTables]
    for dlc, tables in dlc_to_tables.items():
        table: PinballFXTables
        for table in tables:
            table_strings.append(f"[{dlc.value}] {table.value}")

    return table_strings


def id_to_goals() -> Dict[int, PinballFXAPGoals]:
    return {goal.value: goal for goal in PinballFXAPGoals}


def id_to_requirement_modes() -> Dict[int, PinballFXAPRequirementModes]:
    return {mode.value: mode for mode in PinballFXAPRequirementModes}


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
    data: PinballFXItemData
    for item, data in item_data.items():
        if data.tags is not None:
            tag: PinballFXAPTags
            for tag in data.tags:
                groups.setdefault(tag.value, list()).append(item)

    return {k: v for k, v in groups.items() if len(v)}


def item_names_to_id() -> Dict[str, int]:
    return {item: data.archipelago_id for item, data in item_data.items()}


def items_with_tag(tag: PinballFXAPTags) -> List[str]:
    item: str
    data: PinballFXItemData

    return [item for item, data in item_data.items() if data.tags is not None and tag in data.tags]


def location_groups() -> Dict[str, List[str]]:
    groups: Dict[str, List[str]] = dict()

    location: str
    data: PinballFXLocationData
    for location, data in location_data.items():
        if data.tags is not None:
            tag: PinballFXAPTags
            for tag in data.tags:
                groups.setdefault(tag.value, list()).append(location)

    return {k: v for k, v in groups.items() if len(v)}


def location_names_to_id() -> Dict[str, int]:
    return {
        location: data.archipelago_id
        for location, data in location_data.items()
        if data.archipelago_id is not None
    }


def locations_with_tag(tag: PinballFXAPTags) -> List[str]:
    location: str
    data: PinballFXLocationData

    return [location for location, data in location_data.items() if data.tags is not None and tag in data.tags]


def locations_with_tags(tags: List[PinballFXAPTags]) -> List[str]:
    location: str
    data: PinballFXLocationData

    return [
        location
        for location, data in location_data.items()
        if data.tags is not None and all(tag in data.tags for tag in tags)
    ]


def process_slot_data(slot_data: Dict[str, Any]) -> Dict[str, Any]:
    slot_data_processed: Dict[str, Any] = copy.deepcopy(slot_data)

    slot_data_processed["goal"] = id_to_goals()[slot_data["goal"]]

    slot_data_processed["pinball_table_selection"] = dict()

    table_name: str
    is_enabled: bool
    for table_name, is_enabled in slot_data["pinball_table_selection"].items():
        if table_name.startswith("[Free"):
            table_name = table_name.split("Tables] ")[1]
        else:
            table_name = table_name.split("DLC] ")[1]

        slot_data_processed["pinball_table_selection"][PinballFXTables(table_name)] = is_enabled

    slot_data_processed["target_score_requirement_mode"] = id_to_requirement_modes()[slot_data["target_score_requirement_mode"]]

    trap_weights: Dict[PinballFXAPTrapTypes, int] = dict()

    trap_type_name: str
    weight: int
    for trap_type_name, weight in slot_data["trap_weights"].items():
        trap_weights[PinballFXAPTrapTypes(trap_type_name)] = weight

    slot_data_processed["trap_weights"] = trap_weights

    slot_data_processed["selected_tables"] = [
        PinballFXTables(table_name) for table_name in slot_data["selected_tables"]
    ]

    slot_data_processed["selected_starter_table_modes"] = dict()

    table_name: str
    game_mode_names: List[str]
    for table_name, game_mode_names in slot_data["selected_starter_table_modes"].items():
        slot_data_processed["selected_starter_table_modes"][PinballFXTables(table_name)] = [
            PinballFXGameModes(game_mode_name) for game_mode_name in game_mode_names
        ]

    if slot_data["selected_goal_table"] is not None:
        slot_data_processed["selected_goal_table"] = PinballFXTables(slot_data["selected_goal_table"])

    slot_data_processed["target_scores"] = dict()

    table_name: str
    game_mode_scores: Dict[str, List[int]]
    for table_name, game_mode_scores in slot_data["target_scores"].items():
        slot_data_processed["target_scores"][PinballFXTables(table_name)] = dict()

        game_mode_name: str
        scores: List[int]
        for game_mode_name, scores in game_mode_scores.items():
            slot_data_processed["target_scores"][PinballFXTables(table_name)][PinballFXGameModes(game_mode_name)] = scores

    slot_data_processed["target_score_ratios"] = dict()

    table_name: str
    ratio: float
    for table_name, ratio in slot_data["target_score_ratios"].items():
        slot_data_processed["target_score_ratios"][PinballFXTables(table_name)] = ratio

    return slot_data_processed

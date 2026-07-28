from typing import Any, Dict, List, Optional, Tuple

import copy

from .data.item_data import SeveredSteelItemData, item_data
from .data.location_data import SeveredSteelLocationData, location_data

from .enums import (
    SeveredSteelAPGoals,
    SeveredSteelAPMutatorPoolTypes,
    SeveredSteelAPRequirementModes,
    SeveredSteelAPTags,
    SeveredSteelAPTrapTypes,
    SeveredSteelLevels,
    SeveredSteelMutators,
    SeveredSteelStylishActions,
)


def id_to_items() -> Dict[int, str]:
    return {data.archipelago_id: item for item, data in item_data.items()}


def id_to_locations() -> Dict[int, str]:
    return {
        data.archipelago_id: location
        for location, data in location_data.items()
        if data.archipelago_id is not None
    }


def id_to_goals() -> Dict[int, SeveredSteelAPGoals]:
    return {goal.value: goal for goal in SeveredSteelAPGoals}


def id_to_mutator_pool_types() -> Dict[int, SeveredSteelAPMutatorPoolTypes]:
    return {pool_type.value: pool_type for pool_type in SeveredSteelAPMutatorPoolTypes}


def id_to_requirement_modes() -> Dict[int, SeveredSteelAPRequirementModes]:
    return {
        mode.value: mode for mode in SeveredSteelAPRequirementModes
    }


def item_groups() -> Dict[str, List[str]]:
    groups: Dict[str, List[str]] = dict()

    item: str
    data: SeveredSteelItemData
    for item, data in item_data.items():
        if data.tags is not None:
            tag: SeveredSteelAPTags
            for tag in data.tags:
                groups.setdefault(tag.value, list()).append(item)

    return {k: v for k, v in groups.items() if len(v)}


def item_names_to_id() -> Dict[str, int]:
    return {item: data.archipelago_id for item, data in item_data.items()}


def items_with_tag(tag: SeveredSteelAPTags) -> List[str]:
    item: str
    data: SeveredSteelItemData

    return [item for item, data in item_data.items() if data.tags is not None and tag in data.tags]


def location_groups() -> Dict[str, List[str]]:
    groups: Dict[str, List[str]] = dict()

    location: str
    data: SeveredSteelLocationData
    for location, data in location_data.items():
        if data.tags is not None:
            tag: SeveredSteelAPTags
            for tag in data.tags:
                groups.setdefault(tag.value, list()).append(location)

    return {k: v for k, v in groups.items() if len(v)}


def location_names_to_id() -> Dict[str, int]:
    return {
        location: data.archipelago_id
        for location, data in location_data.items()
        if data.archipelago_id is not None
    }


def locations_with_tag(tag: SeveredSteelAPTags) -> List[str]:
    location: str
    data: SeveredSteelLocationData

    return [location for location, data in location_data.items() if data.tags is not None and tag in data.tags]


def process_slot_data(slot_data: Dict[str, Any]) -> Dict[str, Any]:
    slot_data_processed: Dict[str, Any] = copy.deepcopy(slot_data)

    slot_data_processed["goal"] = id_to_goals()[slot_data["goal"]]

    slot_data_processed["level_selection"] = dict()

    level_name: str
    is_enabled: bool
    for level_name, is_enabled in slot_data["level_selection"].items():
        slot_data_processed["level_selection"][SeveredSteelLevels(level_name)] = is_enabled

    slot_data_processed["mutator_pool_type"] = id_to_mutator_pool_types()[slot_data["mutator_pool_type"]]
    slot_data_processed["rank_score_requirement_mode"] = id_to_requirement_modes()[slot_data["rank_score_requirement_mode"]]
    slot_data_processed["target_time_requirement_mode"] = id_to_requirement_modes()[slot_data["target_time_requirement_mode"]]

    trap_weights: Dict[SeveredSteelAPTrapTypes, int] = dict()

    trap_type_name: str
    weight: int
    for trap_type_name, weight in slot_data["trap_weights"].items():
        trap_weights[SeveredSteelAPTrapTypes(trap_type_name)] = weight

    slot_data_processed["trap_weights"] = trap_weights

    slot_data_processed["selected_levels"] = [
        SeveredSteelLevels(level_name) for level_name in slot_data["selected_levels"]
    ]

    slot_data_processed["selected_starting_levels"] = [
        SeveredSteelLevels(level_name) for level_name in slot_data["selected_starting_levels"]
    ]

    if slot_data["selected_goal_level"] is not None:
        slot_data_processed["selected_goal_level"] = SeveredSteelLevels(slot_data["selected_goal_level"])

    slot_data_processed["level_to_mutator"] = dict()

    level_name: str
    mutator_name: Optional[str]
    for level_name, mutator_name in slot_data["level_to_mutator"].items():
        slot_data_processed["level_to_mutator"][SeveredSteelLevels(level_name)] = None

        if mutator_name is not None:
            slot_data_processed["level_to_mutator"][SeveredSteelLevels(level_name)] = SeveredSteelMutators(mutator_name)

    slot_data_processed["level_to_is_mirrored"] = dict()

    level_name: str
    is_mirrored: bool
    for level_name, is_mirrored in slot_data["level_to_is_mirrored"].items():
        slot_data_processed["level_to_is_mirrored"][SeveredSteelLevels(level_name)] = is_mirrored

    slot_data_processed["level_to_stylish_action_challenges"] = dict()

    level_name: str
    challenge_data: Optional[List[Tuple[str, int]]]
    for level_name, challenge_data in slot_data["level_to_stylish_action_challenges"].items():
        slot_data_processed["level_to_stylish_action_challenges"][SeveredSteelLevels(level_name)] = None

        if challenge_data is not None:
            slot_data_processed["level_to_stylish_action_challenges"][SeveredSteelLevels(level_name)] = list()

            challenge: Tuple[str, int]
            for challenge in challenge_data:
                slot_data_processed["level_to_stylish_action_challenges"][SeveredSteelLevels(level_name)].append(
                    (SeveredSteelStylishActions(challenge[0]), challenge[1])
                )

    slot_data_processed["target_rank_scores"] = dict()

    level_name: str
    rank_scores: List[int]
    for level_name, rank_scores in slot_data["target_rank_scores"].items():
        slot_data_processed["target_rank_scores"][SeveredSteelLevels(level_name)] = rank_scores

    slot_data_processed["target_times"] = dict()

    level_name: str
    time: Optional[int]
    for level_name, time in slot_data["target_times"].items():
        slot_data_processed["target_times"][SeveredSteelLevels(level_name)] = time

    slot_data_processed["target_rank_score_ratios"] = dict()

    level_name: str
    ratio: float
    for level_name, ratio in slot_data["target_rank_score_ratios"].items():
        slot_data_processed["target_rank_score_ratios"][SeveredSteelLevels(level_name)] = ratio

    slot_data_processed["target_time_ratios"] = dict()

    level_name: str
    ratio: Optional[float]
    for level_name, ratio in slot_data["target_time_ratios"].items():
        slot_data_processed["target_time_ratios"][SeveredSteelLevels(level_name)] = ratio

    return slot_data_processed

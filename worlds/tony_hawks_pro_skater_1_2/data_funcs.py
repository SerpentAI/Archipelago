from typing import Any, Dict, List, Tuple

from .data.item_data import TonyHawksProSkater12ItemData, item_data
from .data.location_data import TonyHawksProSkater12LocationData, location_data

from .enums import (
    TonyHawksProSkater12APGoals,
    TonyHawksProSkater12APRequirementModes,
    TonyHawksProSkater12APTags,
    TonyHawksProSkater12APTrapTypes,
    TonyHawksProSkater12Gaps,
    TonyHawksProSkater12Levels,
    TonyHawksProSkater12Skaters,
)


def id_to_goals() -> Dict[int, TonyHawksProSkater12APGoals]:
    return {goal.value: goal for goal in TonyHawksProSkater12APGoals}


def id_to_items() -> Dict[int, str]:
    return {data.archipelago_id: item for item, data in item_data.items()}


def id_to_locations() -> Dict[int, str]:
    return {
        data.archipelago_id: location
        for location, data in location_data.items()
        if data.archipelago_id is not None
    }


def id_to_requirement_modes() -> Dict[int, TonyHawksProSkater12APRequirementModes]:
    return {
        mode.value: mode for mode in TonyHawksProSkater12APRequirementModes
    }


def item_groups() -> Dict[str, List[str]]:
    groups: Dict[str, List[str]] = dict()

    item: str
    data: TonyHawksProSkater12ItemData
    for item, data in item_data.items():
        if data.tags is not None:
            tag: TonyHawksProSkater12APTags
            for tag in data.tags:
                groups.setdefault(tag.value, list()).append(item)

    return {k: v for k, v in groups.items() if len(v)}


def item_names_to_id() -> Dict[str, int]:
    return {item: data.archipelago_id for item, data in item_data.items()}


def items_with_tag(tag: TonyHawksProSkater12APTags) -> List[str]:
    item: str
    data: TonyHawksProSkater12ItemData

    return [item for item, data in item_data.items() if data.tags is not None and tag in data.tags]


def location_groups() -> Dict[str, List[str]]:
    groups: Dict[str, List[str]] = dict()

    location: str
    data: TonyHawksProSkater12LocationData
    for location, data in location_data.items():
        if data.tags is not None:
            tag: TonyHawksProSkater12APTags
            for tag in data.tags:
                groups.setdefault(tag.value, list()).append(location)

    return {k: v for k, v in groups.items() if len(v)}


def location_names_to_id() -> Dict[str, int]:
    return {
        location: data.archipelago_id
        for location, data in location_data.items()
        if data.archipelago_id is not None
    }


def locations_with_tag(tag: TonyHawksProSkater12APTags) -> List[str]:
    location: str
    data: TonyHawksProSkater12LocationData

    return [location for location, data in location_data.items() if data.tags is not None and tag in data.tags]


def locations_with_tags(tags: List[TonyHawksProSkater12APTags]) -> List[str]:
    location: str
    data: TonyHawksProSkater12LocationData

    return [
        location
        for location, data in location_data.items()
        if data.tags is not None and all(tag in data.tags for tag in tags)
    ]


def location_access_rule_for(location: str, player: int) -> str:
    data: TonyHawksProSkater12LocationData = location_data[location]

    if data.requirements is None:
        return "lambda state: True"

    lambda_string: str = "lambda state: "

    i: int
    requirement: Tuple[Any]
    for i, requirement in enumerate(data.requirements):
        if isinstance(requirement[0], str):
            lambda_string += f"state.has(\"{requirement[0]}\", {player}, {requirement[1]})"
        elif isinstance(requirement[0], tuple):
            lambda_string += "("

            ii: int
            sub_requirement: tuple[Any]
            for ii, sub_requirement in enumerate(requirement):
                lambda_string += f"state.has(\"{sub_requirement[0]}\", {player}, {sub_requirement[1]})"

                if ii < len(requirement) - 1:
                    lambda_string += " or "

            lambda_string += ")"

        if i < len(data.requirements) - 1:
            lambda_string += " and "

    return lambda_string


def process_slot_data(slot_data: Dict[str, Any]) -> Dict[str, Any]:
    slot_data["goal"] = id_to_goals()[slot_data["goal"]]
    slot_data["score_requirement_mode"] = id_to_requirement_modes()[slot_data["score_requirement_mode"]]
    slot_data["combo_score_requirement_mode"] = id_to_requirement_modes()[slot_data["combo_score_requirement_mode"]]

    trap_weights: Dict[TonyHawksProSkater12APTrapTypes, int] = dict()

    trap_type_name: str
    weight: int
    for trap_type_name, weight in slot_data["trap_weights"].items():
        trap_weights[TonyHawksProSkater12APTrapTypes(trap_type_name)] = weight

    slot_data["trap_weights"] = trap_weights

    slot_data["selected_skaters"] = [
        TonyHawksProSkater12Skaters(skater_name) for skater_name in slot_data["selected_skaters"]
    ]

    slot_data["selected_starting_skater"] = TonyHawksProSkater12Skaters(slot_data["selected_starting_skater"])

    slot_data["selected_levels"] = [
        TonyHawksProSkater12Levels(level_name) for level_name in slot_data["selected_levels"]
    ]

    slot_data["selected_starting_levels"] = [
        TonyHawksProSkater12Levels(level_name) for level_name in slot_data["selected_starting_levels"]
    ]

    if slot_data["selected_goal_level"] is not None:
        slot_data["selected_goal_level"] = TonyHawksProSkater12Levels(slot_data["selected_goal_level"])

    target_scores: Dict[TonyHawksProSkater12Levels, Dict[TonyHawksProSkater12Skaters, List[int]]] = dict()

    level_name: str
    skater_data: Dict[str, List[int]]
    for level_name, skater_data in slot_data["target_scores"].items():
        target_scores[TonyHawksProSkater12Levels(level_name)] = dict()

        skater_name: str
        scores: List[int]
        for skater_name, scores in skater_data.items():
            target_scores[TonyHawksProSkater12Levels(level_name)][TonyHawksProSkater12Skaters(skater_name)] = scores

    slot_data["target_scores"] = target_scores

    target_combo_scores: Dict[TonyHawksProSkater12Levels, Dict[TonyHawksProSkater12Skaters, List[int]]] = dict()

    level_name: str
    skater_data: Dict[str, List[int]]
    for level_name, skater_data in slot_data["target_combo_scores"].items():
        target_combo_scores[TonyHawksProSkater12Levels(level_name)] = dict()

        skater_name: str
        scores: List[int]
        for skater_name, scores in skater_data.items():
            target_combo_scores[TonyHawksProSkater12Levels(level_name)][
                TonyHawksProSkater12Skaters(skater_name)] = scores

    slot_data["target_combo_scores"] = target_combo_scores

    target_gaps: Dict[
        TonyHawksProSkater12Levels, Dict[TonyHawksProSkater12Skaters, List[TonyHawksProSkater12Gaps]]] = dict()

    level_name: str
    skater_data: Dict[str, List[TonyHawksProSkater12Gaps]]
    for level_name, skater_data in slot_data["target_gaps"].items():
        target_gaps[TonyHawksProSkater12Levels(level_name)] = dict()

        skater_name: str
        gaps: List[TonyHawksProSkater12Gaps]
        for skater_name, gaps in skater_data.items():
            target_gaps[TonyHawksProSkater12Levels(level_name)][TonyHawksProSkater12Skaters(skater_name)] = [
                TonyHawksProSkater12Gaps(gap) for gap in gaps
            ]

    slot_data["target_gaps"] = target_gaps

    target_long_tricks: Dict[TonyHawksProSkater12Levels, Dict[TonyHawksProSkater12Skaters, List[float]]] = dict()

    level_name: str
    skater_data: Dict[str, List[float]]
    for level_name, skater_data in slot_data["target_long_tricks"].items():
        target_long_tricks[TonyHawksProSkater12Levels(level_name)] = dict()

        skater_name: str
        durations: List[float]
        for skater_name, durations in skater_data.items():
            target_long_tricks[TonyHawksProSkater12Levels(level_name)][
                TonyHawksProSkater12Skaters(skater_name)] = durations

    slot_data["target_long_tricks"] = target_long_tricks

    slot_data["starting_trick_types"] = {
        TonyHawksProSkater12Skaters(skater_name): trick_type_name for skater_name, trick_type_name in
        slot_data["starting_trick_types"].items()
    }

    target_score_ratios: Dict[TonyHawksProSkater12Levels, Dict[TonyHawksProSkater12Skaters, float]] = dict()

    level_name: str
    skater_data: Dict[str, float]
    for level_name, skater_data in slot_data["target_score_ratios"].items():
        target_score_ratios[TonyHawksProSkater12Levels(level_name)] = dict()

        skater_name: str
        ratio: float
        for skater_name, ratio in skater_data.items():
            target_score_ratios[TonyHawksProSkater12Levels(level_name)][
                TonyHawksProSkater12Skaters(skater_name)] = ratio

    slot_data["target_score_ratios"] = target_score_ratios

    target_combo_score_ratios: Dict[TonyHawksProSkater12Levels, Dict[TonyHawksProSkater12Skaters, float]] = dict()

    level_name: str
    skater_data: Dict[str, float]
    for level_name, skater_data in slot_data["target_combo_score_ratios"].items():
        target_combo_score_ratios[TonyHawksProSkater12Levels(level_name)] = dict()

        skater_name: str
        ratio: float
        for skater_name, ratio in skater_data.items():
            target_combo_score_ratios[TonyHawksProSkater12Levels(level_name)][
                TonyHawksProSkater12Skaters(skater_name)] = ratio

    slot_data["target_combo_score_ratios"] = target_combo_score_ratios

    return slot_data

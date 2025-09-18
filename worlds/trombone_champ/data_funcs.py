from typing import Any, Dict, List, Set, Tuple, Union

from .data.item_data import item_data, TromboneChampItemData
from .data.location_data import location_data, TromboneChampLocationData

from .enums import TromboneChampGoals, TromboneChampGoalSongs, TromboneChampItems, TromboneChampTags


def item_groups() -> Dict[str, List[str]]:
    groups: Dict[str, List[str]] = dict()

    item: str
    data: TromboneChampItemData
    for item, data in item_data.items():
        if data.tags is not None:
            tag: TromboneChampTags
            for tag in data.tags:
                groups.setdefault(tag.value, list()).append(item)

    return {k: v for k, v in groups.items() if len(v)}


def item_names_to_id() -> Dict[str, int]:
    return {item: data.archipelago_id for item, data in item_data.items()}


def location_groups() -> Dict[str, List[str]]:
    groups: Dict[str, List[str]] = dict()

    location: str
    data: TromboneChampLocationData
    for location, data in location_data.items():
        if data.tags is not None:
            tag: TromboneChampTags
            for tag in data.tags:
                groups.setdefault(tag.value, list()).append(location)

    return {k: v for k, v in groups.items() if len(v)}


def location_names_to_id() -> Dict[Any, int]:
    return {
        location: data.archipelago_id
        for location, data in location_data.items()
        if data.archipelago_id is not None
    }

def id_to_goals() -> Dict[int, TromboneChampGoals]:
    return {goal.value: goal for goal in TromboneChampGoals}


def id_to_goal_songs() -> Dict[int, TromboneChampGoalSongs]:
    return {goal_song.value: goal_song for goal_song in TromboneChampGoalSongs}


def location_access_rule_for(location: str, player: int) -> str:
    data: TromboneChampLocationData = location_data[location]

    if data.requirements is None:
        return "lambda state: True"

    lambda_string: str = "lambda state: "

    i: int
    requirement: Union[
        Tuple[
            Union[str, TromboneChampItems],
            ...,
        ],
        Union[str, TromboneChampItems],
    ]

    for i, requirement in enumerate(data.requirements):
        if isinstance(requirement, tuple):
            lambda_string += "("

            ii: int
            sub_requirement: Union[str, TromboneChampItems]
            for ii, sub_requirement in enumerate(requirement):
                if isinstance(sub_requirement, TromboneChampItems):
                    sub_requirement = sub_requirement.value

                lambda_string += f"state.has(\"{sub_requirement}\", {player})"

                if ii < len(requirement) - 1:
                    lambda_string += " or "

            lambda_string += ")"
        else:
            if isinstance(requirement, TromboneChampItems):
                requirement = requirement.value

            lambda_string += f"state.has(\"{requirement}\", {player})"

        if i < len(data.requirements) - 1:
            lambda_string += " and "

    return lambda_string


def location_goal_access_rule_for(location: str, player: int, baboons_required: int) -> str:
    access_rule: str = location_access_rule_for(location, player)
    return access_rule + f" and state.has(\"{TromboneChampItems.GOLDEN_BABOON.value}\", {player}, {baboons_required})"

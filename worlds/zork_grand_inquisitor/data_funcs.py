from typing import Any, Dict, List, Set, Tuple, Union

from BaseClasses import ItemClassification

from .data.entrance_data import Entrance, EntranceRule, EntranceRuleData, endgame_entrance_data_by_goal
from .data.item_data import item_data, ZorkGrandInquisitorItemData
from .data.location_data import location_data, ZorkGrandInquisitorLocationData
from .data.transform_data import item_data_transforms, location_data_transforms

from .enums import (
    ZorkGrandInquisitorClientSeedInformation,
    ZorkGrandInquisitorCraftableSpellBehaviors,
    ZorkGrandInquisitorDeathsanity,
    ZorkGrandInquisitorEntranceRandomizer,
    ZorkGrandInquisitorEvents,
    ZorkGrandInquisitorGoals,
    ZorkGrandInquisitorHotspots,
    ZorkGrandInquisitorItems,
    ZorkGrandInquisitorItemTransforms,
    ZorkGrandInquisitorLandmarksanity,
    ZorkGrandInquisitorLocations,
    ZorkGrandInquisitorLocationTransforms,
    ZorkGrandInquisitorRegions,
    ZorkGrandInquisitorStartingLocations,
    ZorkGrandInquisitorTags,
)


def item_names_to_id() -> Dict[str, int]:
    return {item.value: data.archipelago_id for item, data in item_data.items()}


def item_names_to_item() -> Dict[str, ZorkGrandInquisitorItems]:
    return {item.value: item for item in item_data}


def location_names_to_id() -> Dict[Any, int]:
    return {
        location.value: data.archipelago_id
        for location, data in location_data.items()
        if data.archipelago_id is not None
    }


def location_names_to_location() -> Dict[Any, ZorkGrandInquisitorLocations]:
    return {
        location.value: location
        for location, data in location_data.items()
        if data.archipelago_id is not None
    }


def id_to_client_seed_information() -> Dict[int, ZorkGrandInquisitorClientSeedInformation]:
    return {info.value: info for info in ZorkGrandInquisitorClientSeedInformation}


def id_to_craftable_spell_behaviors() -> Dict[int, ZorkGrandInquisitorCraftableSpellBehaviors]:
    return {behavior.value: behavior for behavior in ZorkGrandInquisitorCraftableSpellBehaviors}


def id_to_deathsanity() -> Dict[int, ZorkGrandInquisitorDeathsanity]:
    return {deathsanity.value: deathsanity for deathsanity in ZorkGrandInquisitorDeathsanity}


def id_to_entrance_randomizer() -> Dict[int, ZorkGrandInquisitorEntranceRandomizer]:
    return {er.value: er for er in ZorkGrandInquisitorEntranceRandomizer}


def id_to_goals() -> Dict[int, ZorkGrandInquisitorGoals]:
    return {goal.value: goal for goal in ZorkGrandInquisitorGoals}


def id_to_hotspots() -> Dict[int, ZorkGrandInquisitorHotspots]:
    return {hotspot.value: hotspot for hotspot in ZorkGrandInquisitorHotspots}


def id_to_items() -> Dict[int, ZorkGrandInquisitorItems]:
    return {data.archipelago_id: item for item, data in item_data.items()}


def id_to_landmarksanity() -> Dict[int, ZorkGrandInquisitorLandmarksanity]:
    return {landmarksanity.value: landmarksanity for landmarksanity in ZorkGrandInquisitorLandmarksanity}


def id_to_locations() -> Dict[int, ZorkGrandInquisitorLocations]:
    return {
        data.archipelago_id: location
        for location, data in location_data.items()
        if data.archipelago_id is not None
    }


def id_to_starting_locations() -> Dict[int, ZorkGrandInquisitorStartingLocations]:
    return {
        starting_location.value: starting_location
        for starting_location in ZorkGrandInquisitorStartingLocations
    }


def item_groups() -> Dict[str, List[str]]:
    groups: Dict[str, List[str]] = dict()

    item: ZorkGrandInquisitorItems
    data: ZorkGrandInquisitorItemData
    for item, data in item_data.items():
        if data.tags is not None:
            for tag in data.tags:
                groups.setdefault(tag.value, list()).append(item.value)

    return {k: v for k, v in groups.items() if len(v)}


def items_with_tag(tag: ZorkGrandInquisitorTags) -> Set[ZorkGrandInquisitorItems]:
    items: Set[ZorkGrandInquisitorItems] = set()

    item: ZorkGrandInquisitorItems
    data: ZorkGrandInquisitorItemData
    for item, data in item_data.items():
        if data.tags is not None and tag in data.tags:
            items.add(item)

    return items


def game_id_to_items() -> Dict[int, ZorkGrandInquisitorItems]:
    mapping: Dict[int, ZorkGrandInquisitorItems] = dict()

    item: ZorkGrandInquisitorItems
    data: ZorkGrandInquisitorItemData
    for item, data in item_data.items():
        if data.statemap_keys is not None:
            for key in data.statemap_keys:
                mapping[key] = item

    return mapping


def location_groups() -> Dict[str, List[str]]:
    groups: Dict[str, List[str]] = dict()

    tag: ZorkGrandInquisitorTags
    for tag in ZorkGrandInquisitorTags:
        groups[tag.value] = list()

    location: ZorkGrandInquisitorLocations
    data: ZorkGrandInquisitorLocationData
    for location, data in location_data.items():
        if data.tags is not None:
            for tag in data.tags:
                groups[tag.value].append(location.value)

    return {k: v for k, v in groups.items() if len(v)}


def locations_by_region_for_world(
    world_location_data: Dict[
        Union[ZorkGrandInquisitorLocations, ZorkGrandInquisitorEvents],
        ZorkGrandInquisitorLocationData,
    ]
) -> Dict[ZorkGrandInquisitorRegions, List[ZorkGrandInquisitorLocations]]:
    mapping: Dict[ZorkGrandInquisitorRegions, List[ZorkGrandInquisitorLocations]] = dict()

    region: ZorkGrandInquisitorRegions
    for region in ZorkGrandInquisitorRegions:
        mapping[region] = list()

    location: ZorkGrandInquisitorLocations
    data: ZorkGrandInquisitorLocationData
    for location, data in world_location_data.items():
        mapping[data.region].append(location)

    return mapping


def locations_with_tag(tag: ZorkGrandInquisitorTags) -> Set[ZorkGrandInquisitorLocations]:
    location: ZorkGrandInquisitorLocations
    data: ZorkGrandInquisitorLocationData

    return {location for location, data in location_data.items() if data.tags is not None and tag in data.tags}


def prepare_item_data(
    starting_location: ZorkGrandInquisitorStartingLocations,
    goal: ZorkGrandInquisitorGoals,
    deathsanity: ZorkGrandInquisitorDeathsanity,
    landmarksanity: ZorkGrandInquisitorLandmarksanity,
    entrance_randomizer: ZorkGrandInquisitorEntranceRandomizer,
) -> Dict[ZorkGrandInquisitorItems, ZorkGrandInquisitorItemData]:
    transformed_item_data: Dict[ZorkGrandInquisitorItems, ZorkGrandInquisitorItemData] = dict()

    # Filter items
    item: ZorkGrandInquisitorItems
    data: ZorkGrandInquisitorItemData
    for item, data in item_data.items():
        # Filter here...
        transformed_item_data[item] = data

    # Apply transformations
    items_to_make_filler: Set[ZorkGrandInquisitorItems] = set()

    for context in (starting_location, goal, deathsanity, landmarksanity):
        if item_data_transforms[context] is not None:
            transform: ZorkGrandInquisitorItemTransforms
            items: Tuple[ZorkGrandInquisitorItems, ...]
            for transform, items in item_data_transforms[context].items():
                if transform == ZorkGrandInquisitorItemTransforms.MAKE_FILLER:
                    if context == starting_location:
                        if entrance_randomizer != ZorkGrandInquisitorEntranceRandomizer.DISABLED:
                            continue

                    item: ZorkGrandInquisitorItems
                    for item in items:
                        items_to_make_filler.add(item)

    item: ZorkGrandInquisitorItems
    for item in items_to_make_filler:
        transformed_item_data[item] = transformed_item_data[item]._replace(
            classification=ItemClassification.filler
        )

    return transformed_item_data


def prepare_location_data(
    starting_location: ZorkGrandInquisitorStartingLocations,
    goal: ZorkGrandInquisitorGoals,
    deathsanity: ZorkGrandInquisitorDeathsanity,
    landmarksanity: ZorkGrandInquisitorLandmarksanity,
) -> Dict[
    Union[ZorkGrandInquisitorLocations, ZorkGrandInquisitorEvents], ZorkGrandInquisitorLocationData
]:
    transformed_location_data: Dict[
        Union[ZorkGrandInquisitorLocations, ZorkGrandInquisitorEvents], ZorkGrandInquisitorLocationData
    ] = dict()

    # Filter locations
    location: Union[ZorkGrandInquisitorLocations, ZorkGrandInquisitorEvents]
    data: ZorkGrandInquisitorLocationData
    for location, data in location_data.items():
        # Filter here...
        transformed_location_data[location] = data

    # Apply transformations
    locations_to_remove: List[ZorkGrandInquisitorLocations] = list()

    for context in (starting_location, goal, deathsanity, landmarksanity):
        if location_data_transforms[context] is not None:
            transform: ZorkGrandInquisitorLocationTransforms
            locations: Tuple[ZorkGrandInquisitorLocations, ...]
            for transform, locations in location_data_transforms[context].items():
                if transform == ZorkGrandInquisitorLocationTransforms.REMOVE:
                    location: ZorkGrandInquisitorLocations
                    for location in locations:
                        locations_to_remove.append(location)

    location: ZorkGrandInquisitorLocations
    for location in locations_to_remove:
        if location in transformed_location_data:
            del transformed_location_data[location]

    return transformed_location_data


def location_access_rule_for(location: ZorkGrandInquisitorLocations, player: int) -> str:
    data: ZorkGrandInquisitorLocationData = location_data[location]

    if data.requirements is None:
        return "lambda state: True"

    lambda_string: str = "lambda state: "

    i: int
    requirement: Union[
        Tuple[
            Union[
                ZorkGrandInquisitorEvents,
                ZorkGrandInquisitorItems,
            ],
            ...,
        ],
        ZorkGrandInquisitorEvents,
        ZorkGrandInquisitorItems
    ]

    for i, requirement in enumerate(data.requirements):
        if isinstance(requirement, tuple):
            lambda_string += "("

            ii: int
            sub_requirement: Union[ZorkGrandInquisitorEvents, ZorkGrandInquisitorItems]
            for ii, sub_requirement in enumerate(requirement):
                lambda_string += f"state.has(\"{sub_requirement.value}\", {player})"

                if ii < len(requirement) - 1:
                    lambda_string += " or "

            lambda_string += ")"
        else:
            lambda_string += f"state.has(\"{requirement.value}\", {player})"

        if i < len(data.requirements) - 1:
            lambda_string += " and "

    return lambda_string


def entrances_by_region_for_world(
    entrance_rule_data: EntranceRuleData
) -> Dict[ZorkGrandInquisitorRegions, List[Entrance]]:
    entrances_by_region: Dict[ZorkGrandInquisitorRegions, List[Entrance]] = {
        ZorkGrandInquisitorRegions.ANYWHERE: list(),
        ZorkGrandInquisitorRegions.ENDGAME: list(),
    }

    region_from: ZorkGrandInquisitorRegions
    region_to: ZorkGrandInquisitorRegions
    for region_from, region_to in entrance_rule_data.keys():
        if region_from not in entrances_by_region:
            entrances_by_region[region_from] = list()

        entrances_by_region[region_from].append((region_from, region_to))

    return entrances_by_region


def entrance_access_rule_for(
    region_origin: ZorkGrandInquisitorRegions,
    region_destination: ZorkGrandInquisitorRegions,
    player: int,
    dataset: EntranceRuleData
) -> str:
    data: EntranceRule = dataset[(region_origin, region_destination)]

    if data is None:
        return "lambda state: True"

    lambda_string: str = "lambda state: "

    i: int
    requirement_group: Tuple[
        Union[
            ZorkGrandInquisitorEvents,
            ZorkGrandInquisitorItems,
            ZorkGrandInquisitorRegions,
        ],
        ...,
    ]
    for i, requirement_group in enumerate(data):
        lambda_string += "("

        ii: int
        requirement: Union[
            ZorkGrandInquisitorEvents,
            ZorkGrandInquisitorItems,
            ZorkGrandInquisitorRegions,
        ]
        for ii, requirement in enumerate(requirement_group):
            requirement_type: Union[
                ZorkGrandInquisitorEvents,
                ZorkGrandInquisitorItems,
                ZorkGrandInquisitorRegions,
            ] = type(requirement)

            if requirement_type in (ZorkGrandInquisitorEvents, ZorkGrandInquisitorItems):
                lambda_string += f"state.has(\"{requirement.value}\", {player})"
            elif requirement_type == ZorkGrandInquisitorRegions:
                lambda_string += f"state.can_reach(\"{requirement.value}\", \"Region\", {player})"
            elif isinstance(requirement, list):
                lambda_string += f"state.has(\"{requirement[0].value}\", {player}, {requirement[1]})"
            elif isinstance(requirement, tuple):
                lambda_string += "("

                iii: int
                sub_requirement: ZorkGrandInquisitorItems
                for iii, sub_requirement in enumerate(requirement):
                    lambda_string += f"state.has(\"{sub_requirement.value}\", {player})"

                    if iii < len(requirement) - 1:
                        lambda_string += " or "

                lambda_string += ")"

            if ii < len(requirement_group) - 1:
                lambda_string += " and "

        lambda_string += ")"

        if i < len(data) - 1:
            lambda_string += " or "

    return lambda_string


def goal_access_rule_for(
    region: ZorkGrandInquisitorRegions,
    goal: ZorkGrandInquisitorGoals,
    player: int,
    artifacts_of_magic_required: int,
    landmarks_required: int,
    deaths_required: int,
) -> str:
    dataset: Dict[
        Tuple[
            ZorkGrandInquisitorRegions,
            ZorkGrandInquisitorRegions,
        ],
        Union[
            Tuple[
                Tuple[
                    Union[
                        ZorkGrandInquisitorEvents,
                        ZorkGrandInquisitorItems,
                        ZorkGrandInquisitorRegions,
                        List[Union[ZorkGrandInquisitorItems, int]],
                    ],
                    ...,
                ],
                ...,
            ],
            None,
        ],
    ] = endgame_entrance_data_by_goal[goal]

    # Replace placeholder with actual number of goal items required
    if goal == ZorkGrandInquisitorGoals.ARTIFACT_OF_MAGIC_HUNT:
        dataset[
            (
                ZorkGrandInquisitorRegions.WALKING_CASTLE,
                ZorkGrandInquisitorRegions.ENDGAME
            )
        ][0][0][1] = artifacts_of_magic_required
    elif goal == ZorkGrandInquisitorGoals.ZORK_TOUR:
        dataset[
            (
                ZorkGrandInquisitorRegions.OUTSIDE_PORT_FOOZLE_SIGNPOST,
                ZorkGrandInquisitorRegions.ENDGAME
            )
        ][0][0][1] = landmarks_required
    elif goal == ZorkGrandInquisitorGoals.GRIM_JOURNEY:
        dataset[
            (
                ZorkGrandInquisitorRegions.HADES_BEYOND_GATES,
                ZorkGrandInquisitorRegions.ENDGAME
            )
        ][0][0][1] = deaths_required

    return entrance_access_rule_for(
        region,
        ZorkGrandInquisitorRegions.ENDGAME,
        player,
        dataset=dataset,
    )

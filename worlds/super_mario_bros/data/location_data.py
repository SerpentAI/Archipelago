from typing import Dict, Optional, NamedTuple, Tuple, Union

from ..enums import (
    SuperMarioBrosAPItems,
    SuperMarioBrosAPLocations,
    SuperMarioBrosAPRegions,
    SuperMarioBrosAPTags,
)


class SuperMarioBrosLocationData(NamedTuple):
    archipelago_id: int
    original_region: SuperMarioBrosAPRegions
    tags: Optional[Tuple[SuperMarioBrosAPTags, ...]]
    requirements: Optional[
        Tuple[
            Union[
                SuperMarioBrosAPItems,
                Tuple[SuperMarioBrosAPItems, int],
                Tuple[
                    Tuple[SuperMarioBrosAPItems, int],
                    ...,
                ]
            ],
            ...,
        ]
    ]


location_data: Dict[SuperMarioBrosAPLocations, SuperMarioBrosLocationData] = dict()

location_offset: int = 1000

location_data[SuperMarioBrosAPLocations.W_1_1_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 1,
    original_region=SuperMarioBrosAPRegions.W_1_1,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_1_1_HIDDEN_1_UP] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 2,
    original_region=SuperMarioBrosAPRegions.W_1_1,
    tags=(
        SuperMarioBrosAPTags.HIDDEN_1_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_1_1_POWER_UP_2] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 3,
    original_region=SuperMarioBrosAPRegions.W_1_1,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_1_1_STARMAN] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 4,
    original_region=SuperMarioBrosAPRegions.W_1_1,
    tags=(
        SuperMarioBrosAPTags.STARMAN_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_1_1_POWER_UP_3] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 5,
    original_region=SuperMarioBrosAPRegions.W_1_1,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_1_1_6_ENEMY_COMBO] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 6,
    original_region=SuperMarioBrosAPRegions.W_1_1,
    tags=(
        SuperMarioBrosAPTags.ENEMY_COMBO_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_1_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.W_1_1_SUB_LEVEL] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 7,
    original_region=SuperMarioBrosAPRegions.W_1_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_1_1_SUB_LEVEL_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 8,
    original_region=SuperMarioBrosAPRegions.W_1_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_1_1_SUB_LEVEL_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 9,
    original_region=SuperMarioBrosAPRegions.W_1_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_1_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.W_1_1_SUB_LEVEL_COIN_TARGET_19] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 10,
    original_region=SuperMarioBrosAPRegions.W_1_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_1_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.W_1_1_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 11,
    original_region=SuperMarioBrosAPRegions.W_1_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_1_1_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 12,
    original_region=SuperMarioBrosAPRegions.W_1_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_1_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.W_1_1_COIN_TARGET_20] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 13,
    original_region=SuperMarioBrosAPRegions.W_1_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_1_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.W_1_1_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 14,
    original_region=SuperMarioBrosAPRegions.W_1_1,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_1_1_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 15,
    original_region=SuperMarioBrosAPRegions.W_1_1,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_1_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.W_1_2_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 16,
    original_region=SuperMarioBrosAPRegions.W_1_2,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_1_2_STARMAN] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 17,
    original_region=SuperMarioBrosAPRegions.W_1_2,
    tags=(
        SuperMarioBrosAPTags.STARMAN_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_2_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.MAGIC_MUSHROOM,
    ),
)

location_data[SuperMarioBrosAPLocations.W_1_2_POWER_UP_2] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 18,
    original_region=SuperMarioBrosAPRegions.W_1_2,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_2_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.MAGIC_MUSHROOM,
    ),
)

location_data[SuperMarioBrosAPLocations.W_1_2_HIDDEN_1_UP] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 19,
    original_region=SuperMarioBrosAPRegions.W_1_2,
    tags=(
        SuperMarioBrosAPTags.HIDDEN_1_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_1_2_POWER_UP_3] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 20,
    original_region=SuperMarioBrosAPRegions.W_1_2,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_1_2_4_ENEMY_COMBO] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 21,
    original_region=SuperMarioBrosAPRegions.W_1_2,
    tags=(
        SuperMarioBrosAPTags.ENEMY_COMBO_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_2_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.W_1_2_SUB_LEVEL] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 22,
    original_region=SuperMarioBrosAPRegions.W_1_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_1_2_SUB_LEVEL_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 23,
    original_region=SuperMarioBrosAPRegions.W_1_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_1_2_SUB_LEVEL_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 24,
    original_region=SuperMarioBrosAPRegions.W_1_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_2_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.W_1_2_SUB_LEVEL_20_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 25,
    original_region=SuperMarioBrosAPRegions.W_1_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_2_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.W_1_2_SUB_LEVEL_COIN_TARGET_27] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 26,
    original_region=SuperMarioBrosAPRegions.W_1_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_2_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 3),
    ),
)

location_data[SuperMarioBrosAPLocations.W_1_2_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 27,
    original_region=SuperMarioBrosAPRegions.W_1_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_1_2_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 28,
    original_region=SuperMarioBrosAPRegions.W_1_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_2_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.W_1_2_20_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 29,
    original_region=SuperMarioBrosAPRegions.W_1_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_2_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2)
    ),
)

location_data[SuperMarioBrosAPLocations.W_1_2_COIN_TARGET_41] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 30,
    original_region=SuperMarioBrosAPRegions.W_1_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_2_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 3),
        SuperMarioBrosAPItems.MAGIC_MUSHROOM,
    ),
)

location_data[SuperMarioBrosAPLocations.W_1_2_WARP_ZONE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 31,
    original_region=SuperMarioBrosAPRegions.W_1_2,
    tags=(
        SuperMarioBrosAPTags.WARP_ZONE_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_1_2_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 32,
    original_region=SuperMarioBrosAPRegions.W_1_2,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_1_2_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 33,
    original_region=SuperMarioBrosAPRegions.W_1_2,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_2_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.W_1_3_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 34,
    original_region=SuperMarioBrosAPRegions.W_1_3,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_3_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_1_3_1_ENEMY_COMBO] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 35,
    original_region=SuperMarioBrosAPRegions.W_1_3,
    tags=(
        SuperMarioBrosAPTags.ENEMY_COMBO_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_3_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_1_3_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 36,
    original_region=SuperMarioBrosAPRegions.W_1_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_3_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_1_3_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 37,
    original_region=SuperMarioBrosAPRegions.W_1_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_3_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.W_1_3_20_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 38,
    original_region=SuperMarioBrosAPRegions.W_1_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_3_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.W_1_3_COIN_TARGET_23] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 39,
    original_region=SuperMarioBrosAPRegions.W_1_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_3_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 3),
    ),
)

location_data[SuperMarioBrosAPLocations.W_1_3_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 40,
    original_region=SuperMarioBrosAPRegions.W_1_3,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_3_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_1_3_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 41,
    original_region=SuperMarioBrosAPRegions.W_1_3,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_3_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.W_1_4_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 42,
    original_region=SuperMarioBrosAPRegions.W_1_4,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_4_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_1_4_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 43,
    original_region=SuperMarioBrosAPRegions.W_1_4,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_4_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_1_4_COIN_TARGET_6] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 44,
    original_region=SuperMarioBrosAPRegions.W_1_4,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_4_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.W_1_4_DEFEAT_BOWSER] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 45,
    original_region=SuperMarioBrosAPRegions.W_1_4,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_4_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_1_4_KILL_BOWSER] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 46,
    original_region=SuperMarioBrosAPRegions.W_1_4,
    tags=(
        SuperMarioBrosAPTags.KILL_BOWSER_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_4_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.MAGIC_MUSHROOM,
        SuperMarioBrosAPItems.FIRE_FLOWER,
    ),
)

location_data[SuperMarioBrosAPLocations.W_2_1_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 47,
    original_region=SuperMarioBrosAPRegions.W_2_1,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_2_1_HIDDEN_1_UP] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 48,
    original_region=SuperMarioBrosAPRegions.W_2_1,
    tags=(
        SuperMarioBrosAPTags.HIDDEN_1_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_2_1_POWER_UP_2] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 49,
    original_region=SuperMarioBrosAPRegions.W_2_1,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_2_1_STARMAN] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 50,
    original_region=SuperMarioBrosAPRegions.W_2_1,
    tags=(
        SuperMarioBrosAPTags.STARMAN_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_2_1_POWER_UP_3] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 51,
    original_region=SuperMarioBrosAPRegions.W_2_1,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_2_1_POWER_UP_4] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 52,
    original_region=SuperMarioBrosAPRegions.W_2_1,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_2_1_5_ENEMY_COMBO] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 53,
    original_region=SuperMarioBrosAPRegions.W_2_1,
    tags=(
        SuperMarioBrosAPTags.ENEMY_COMBO_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_1_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.W_2_1_SUB_LEVEL] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 54,
    original_region=SuperMarioBrosAPRegions.W_2_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_2_1_SUB_LEVEL_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 55,
    original_region=SuperMarioBrosAPRegions.W_2_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_2_1_SUB_LEVEL_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 56,
    original_region=SuperMarioBrosAPRegions.W_2_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_1_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.W_2_1_SUB_LEVEL_COIN_TARGET_19] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 57,
    original_region=SuperMarioBrosAPRegions.W_2_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_1_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.W_2_1_COIN_HEAVEN] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 58,
    original_region=SuperMarioBrosAPRegions.W_2_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_2_1_COIN_HEAVEN_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 59,
    original_region=SuperMarioBrosAPRegions.W_2_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_2_1_COIN_HEAVEN_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 60,
    original_region=SuperMarioBrosAPRegions.W_2_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_1_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.W_2_1_COIN_HEAVEN_20_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 61,
    original_region=SuperMarioBrosAPRegions.W_2_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_1_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.W_2_1_COIN_HEAVEN_COIN_TARGET_40] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 62,
    original_region=SuperMarioBrosAPRegions.W_2_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_1_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 3),
        SuperMarioBrosAPItems.MAGIC_MUSHROOM,
    ),
)

location_data[SuperMarioBrosAPLocations.W_2_1_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 63,
    original_region=SuperMarioBrosAPRegions.W_2_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_2_1_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 64,
    original_region=SuperMarioBrosAPRegions.W_2_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_1_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.W_2_1_20_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 65,
    original_region=SuperMarioBrosAPRegions.W_2_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_1_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.W_2_1_COIN_TARGET_29] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 66,
    original_region=SuperMarioBrosAPRegions.W_2_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_1_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 3),
    ),
)

location_data[SuperMarioBrosAPLocations.W_2_1_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 67,
    original_region=SuperMarioBrosAPRegions.W_2_1,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_2_1_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 68,
    original_region=SuperMarioBrosAPRegions.W_2_1,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_1_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.W_2_2_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 69,
    original_region=SuperMarioBrosAPRegions.W_2_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_2_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.SWIM,
    ),
)

location_data[SuperMarioBrosAPLocations.W_2_2_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 70,
    original_region=SuperMarioBrosAPRegions.W_2_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_2_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.SWIM,
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1)
    ),
)

location_data[SuperMarioBrosAPLocations.W_2_2_20_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 71,
    original_region=SuperMarioBrosAPRegions.W_2_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_2_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.SWIM,
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.W_2_2_COIN_TARGET_28] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 72,
    original_region=SuperMarioBrosAPRegions.W_2_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_2_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.SWIM,
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 3),
    ),
)

location_data[SuperMarioBrosAPLocations.W_2_2_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 73,
    original_region=SuperMarioBrosAPRegions.W_2_2,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_2_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.SWIM,
    ),
)

location_data[SuperMarioBrosAPLocations.W_2_2_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 74,
    original_region=SuperMarioBrosAPRegions.W_2_2,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_2_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.SWIM,
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.W_2_3_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 75,
    original_region=SuperMarioBrosAPRegions.W_2_3,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_3_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_2_3_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 76,
    original_region=SuperMarioBrosAPRegions.W_2_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_3_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_2_3_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 77,
    original_region=SuperMarioBrosAPRegions.W_2_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_3_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.W_2_3_20_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 78,
    original_region=SuperMarioBrosAPRegions.W_2_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_3_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.W_2_3_COIN_TARGET_35] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 79,
    original_region=SuperMarioBrosAPRegions.W_2_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_3_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 3),
    ),
)

location_data[SuperMarioBrosAPLocations.W_2_3_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 80,
    original_region=SuperMarioBrosAPRegions.W_2_3,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_3_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_2_3_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 81,
    original_region=SuperMarioBrosAPRegions.W_2_3,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_3_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.W_2_4_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 82,
    original_region=SuperMarioBrosAPRegions.W_2_4,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_4_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_2_4_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 83,
    original_region=SuperMarioBrosAPRegions.W_2_4,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_4_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_2_4_COIN_TARGET_6] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 84,
    original_region=SuperMarioBrosAPRegions.W_2_4,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_4_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.W_2_4_DEFEAT_BOWSER] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 85,
    original_region=SuperMarioBrosAPRegions.W_2_4,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_4_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_2_4_KILL_BOWSER] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 86,
    original_region=SuperMarioBrosAPRegions.W_2_4,
    tags=(
        SuperMarioBrosAPTags.KILL_BOWSER_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_4_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.MAGIC_MUSHROOM,
        SuperMarioBrosAPItems.FIRE_FLOWER,
    ),
)

location_data[SuperMarioBrosAPLocations.W_3_1_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 87,
    original_region=SuperMarioBrosAPRegions.W_3_1,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_3_1_HIDDEN_1_UP] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 88,
    original_region=SuperMarioBrosAPRegions.W_3_1,
    tags=(
        SuperMarioBrosAPTags.HIDDEN_1_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_3_1_STARMAN] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 89,
    original_region=SuperMarioBrosAPRegions.W_3_1,
    tags=(
        SuperMarioBrosAPTags.STARMAN_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_1_LOCATION,
    ),
    requirements=(
        (
            SuperMarioBrosAPItems.RUN,
            SuperMarioBrosAPItems.MAGIC_MUSHROOM,
        ),
    ),
)

location_data[SuperMarioBrosAPLocations.W_3_1_POWER_UP_2] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 90,
    original_region=SuperMarioBrosAPRegions.W_3_1,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_3_1_POWER_UP_3] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 91,
    original_region=SuperMarioBrosAPRegions.W_3_1,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_3_1_5_ENEMY_COMBO] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 92,
    original_region=SuperMarioBrosAPRegions.W_3_1,
    tags=(
        SuperMarioBrosAPTags.ENEMY_COMBO_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_1_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.W_3_1_SUB_LEVEL] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 93,
    original_region=SuperMarioBrosAPRegions.W_3_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_3_1_SUB_LEVEL_POWER_UP] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 94,
    original_region=SuperMarioBrosAPRegions.W_3_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_3_1_SUB_LEVEL_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 95,
    original_region=SuperMarioBrosAPRegions.W_3_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_3_1_SUB_LEVEL_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 96,
    original_region=SuperMarioBrosAPRegions.W_3_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_1_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
        SuperMarioBrosAPItems.MAGIC_MUSHROOM,
    ),
)

location_data[SuperMarioBrosAPLocations.W_3_1_SUB_LEVEL_COIN_TARGET_12] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 97,
    original_region=SuperMarioBrosAPRegions.W_3_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_1_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
        SuperMarioBrosAPItems.MAGIC_MUSHROOM,
    ),
)

location_data[SuperMarioBrosAPLocations.W_3_1_COIN_HEAVEN] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 98,
    original_region=SuperMarioBrosAPRegions.W_3_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_3_1_COIN_HEAVEN_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 99,
    original_region=SuperMarioBrosAPRegions.W_3_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_3_1_COIN_HEAVEN_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 100,
    original_region=SuperMarioBrosAPRegions.W_3_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_1_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.W_3_1_COIN_HEAVEN_20_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 101,
    original_region=SuperMarioBrosAPRegions.W_3_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_1_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.W_3_1_COIN_HEAVEN_COIN_TARGET_51] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 102,
    original_region=SuperMarioBrosAPRegions.W_3_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_1_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 3),
        SuperMarioBrosAPItems.MAGIC_MUSHROOM,
    ),
)

location_data[SuperMarioBrosAPLocations.W_3_1_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 103,
    original_region=SuperMarioBrosAPRegions.W_3_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_3_1_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 104,
    original_region=SuperMarioBrosAPRegions.W_3_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_1_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.W_3_1_COIN_TARGET_16] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 105,
    original_region=SuperMarioBrosAPRegions.W_3_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_1_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.W_3_1_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 106,
    original_region=SuperMarioBrosAPRegions.W_3_1,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_3_1_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 107,
    original_region=SuperMarioBrosAPRegions.W_3_1,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_1_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.W_3_2_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 108,
    original_region=SuperMarioBrosAPRegions.W_3_2,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_3_2_STARMAN] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 109,
    original_region=SuperMarioBrosAPRegions.W_3_2,
    tags=(
        SuperMarioBrosAPTags.STARMAN_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_3_2_8_ENEMY_COMBO] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 110,
    original_region=SuperMarioBrosAPRegions.W_3_2,
    tags=(
        SuperMarioBrosAPTags.ENEMY_COMBO_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_2_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.W_3_2_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 111,
    original_region=SuperMarioBrosAPRegions.W_3_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_3_2_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 112,
    original_region=SuperMarioBrosAPRegions.W_3_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_2_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.W_3_2_COIN_TARGET_17] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 113,
    original_region=SuperMarioBrosAPRegions.W_3_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_2_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
        (SuperMarioBrosAPItems.FIRE_FLOWER, SuperMarioBrosAPItems.STARMAN),
    ),
)

location_data[SuperMarioBrosAPLocations.W_3_2_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 114,
    original_region=SuperMarioBrosAPRegions.W_3_2,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_3_2_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 115,
    original_region=SuperMarioBrosAPRegions.W_3_2,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_2_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.W_3_3_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 116,
    original_region=SuperMarioBrosAPRegions.W_3_3,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_3_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_3_3_1_ENEMY_COMBO] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 117,
    original_region=SuperMarioBrosAPRegions.W_3_3,
    tags=(
        SuperMarioBrosAPTags.ENEMY_COMBO_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_3_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_3_3_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 118,
    original_region=SuperMarioBrosAPRegions.W_3_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_3_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_3_3_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 119,
    original_region=SuperMarioBrosAPRegions.W_3_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_3_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.W_3_3_20_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 120,
    original_region=SuperMarioBrosAPRegions.W_3_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_3_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.W_3_3_COIN_TARGET_22] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 121,
    original_region=SuperMarioBrosAPRegions.W_3_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_3_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 3),
    ),
)

location_data[SuperMarioBrosAPLocations.W_3_3_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 122,
    original_region=SuperMarioBrosAPRegions.W_3_3,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_3_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_3_3_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 123,
    original_region=SuperMarioBrosAPRegions.W_3_3,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_3_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.W_3_4_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 124,
    original_region=SuperMarioBrosAPRegions.W_3_4,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_4_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_3_4_COIN_TARGET_5] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 125,
    original_region=SuperMarioBrosAPRegions.W_3_4,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_4_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_3_4_DEFEAT_BOWSER] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 126,
    original_region=SuperMarioBrosAPRegions.W_3_4,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_4_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_3_4_KILL_BOWSER] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 127,
    original_region=SuperMarioBrosAPRegions.W_3_4,
    tags=(
        SuperMarioBrosAPTags.KILL_BOWSER_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_4_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.MAGIC_MUSHROOM,
        SuperMarioBrosAPItems.FIRE_FLOWER,
    ),
)

location_data[SuperMarioBrosAPLocations.W_4_1_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 128,
    original_region=SuperMarioBrosAPRegions.W_4_1,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_4_1_HIDDEN_1_UP] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 129,
    original_region=SuperMarioBrosAPRegions.W_4_1,
    tags=(
        SuperMarioBrosAPTags.HIDDEN_1_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_4_1_POWER_UP_2] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 130,
    original_region=SuperMarioBrosAPRegions.W_4_1,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_4_1_SUB_LEVEL] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 131,
    original_region=SuperMarioBrosAPRegions.W_4_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_4_1_SUB_LEVEL_POWER_UP] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 132,
    original_region=SuperMarioBrosAPRegions.W_4_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_4_1_SUB_LEVEL_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 133,
    original_region=SuperMarioBrosAPRegions.W_4_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_4_1_SUB_LEVEL_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 134,
    original_region=SuperMarioBrosAPRegions.W_4_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_1_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.W_4_1_SUB_LEVEL_COIN_TARGET_18] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 135,
    original_region=SuperMarioBrosAPRegions.W_4_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_1_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.W_4_1_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 136,
    original_region=SuperMarioBrosAPRegions.W_4_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_4_1_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 137,
    original_region=SuperMarioBrosAPRegions.W_4_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_1_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.W_4_1_20_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 138,
    original_region=SuperMarioBrosAPRegions.W_4_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_1_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.W_4_1_COIN_TARGET_44] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 139,
    original_region=SuperMarioBrosAPRegions.W_4_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_1_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 3),
    ),
)

location_data[SuperMarioBrosAPLocations.W_4_1_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 140,
    original_region=SuperMarioBrosAPRegions.W_4_1,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_4_1_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 141,
    original_region=SuperMarioBrosAPRegions.W_4_1,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_1_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.W_4_2_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 142,
    original_region=SuperMarioBrosAPRegions.W_4_2,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_4_2_POWER_UP_2] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 143,
    original_region=SuperMarioBrosAPRegions.W_4_2,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_4_2_STARMAN] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 144,
    original_region=SuperMarioBrosAPRegions.W_4_2,
    tags=(
        SuperMarioBrosAPTags.STARMAN_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_4_2_POWER_UP_3] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 145,
    original_region=SuperMarioBrosAPRegions.W_4_2,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_4_2_POWER_UP_4] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 146,
    original_region=SuperMarioBrosAPRegions.W_4_2,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_4_2_1_ENEMY_COMBO] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 147,
    original_region=SuperMarioBrosAPRegions.W_4_2,
    tags=(
        SuperMarioBrosAPTags.ENEMY_COMBO_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_4_2_SUB_LEVEL] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 148,
    original_region=SuperMarioBrosAPRegions.W_4_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_4_2_SUB_LEVEL_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 149,
    original_region=SuperMarioBrosAPRegions.W_4_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_4_2_SUB_LEVEL_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 150,
    original_region=SuperMarioBrosAPRegions.W_4_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_2_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.W_4_2_SUB_LEVEL_COIN_TARGET_20] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 151,
    original_region=SuperMarioBrosAPRegions.W_4_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_2_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.W_4_2_MUSHROOM_AREA_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 152,
    original_region=SuperMarioBrosAPRegions.W_4_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_4_2_MUSHROOM_AREA_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 153,
    original_region=SuperMarioBrosAPRegions.W_4_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_2_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.W_4_2_MUSHROOM_AREA_COIN_TARGET_19] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 154,
    original_region=SuperMarioBrosAPRegions.W_4_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_2_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.W_4_2_MUSHROOM_AREA_WARP_ZONE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 155,
    original_region=SuperMarioBrosAPRegions.W_4_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.WARP_ZONE_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_4_2_WARP_ZONE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 156,
    original_region=SuperMarioBrosAPRegions.W_4_2,
    tags=(
        SuperMarioBrosAPTags.WARP_ZONE_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_4_2_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 157,
    original_region=SuperMarioBrosAPRegions.W_4_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_4_2_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 158,
    original_region=SuperMarioBrosAPRegions.W_4_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_2_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.W_4_2_20_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 159,
    original_region=SuperMarioBrosAPRegions.W_4_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_2_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.W_4_2_COIN_TARGET_43] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 160,
    original_region=SuperMarioBrosAPRegions.W_4_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_2_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 3),
        SuperMarioBrosAPItems.MAGIC_MUSHROOM,
        SuperMarioBrosAPItems.FIRE_FLOWER,
    ),
)

location_data[SuperMarioBrosAPLocations.W_4_2_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 161,
    original_region=SuperMarioBrosAPRegions.W_4_2,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_4_2_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 162,
    original_region=SuperMarioBrosAPRegions.W_4_2,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_2_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.W_4_3_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 163,
    original_region=SuperMarioBrosAPRegions.W_4_3,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_3_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.W_4_3_1_ENEMY_COMBO] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 164,
    original_region=SuperMarioBrosAPRegions.W_4_3,
    tags=(
        SuperMarioBrosAPTags.ENEMY_COMBO_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_3_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_4_3_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 165,
    original_region=SuperMarioBrosAPRegions.W_4_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_3_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_4_3_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 166,
    original_region=SuperMarioBrosAPRegions.W_4_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_3_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.W_4_3_20_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 167,
    original_region=SuperMarioBrosAPRegions.W_4_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_3_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.W_4_3_COIN_TARGET_27] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 168,
    original_region=SuperMarioBrosAPRegions.W_4_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_3_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 3),
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.W_4_3_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 169,
    original_region=SuperMarioBrosAPRegions.W_4_3,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_3_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.W_4_3_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 170,
    original_region=SuperMarioBrosAPRegions.W_4_3,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_3_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.W_4_4_DEFEAT_BOWSER] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 171,
    original_region=SuperMarioBrosAPRegions.W_4_4,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_4_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_4_4_KILL_BOWSER] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 172,
    original_region=SuperMarioBrosAPRegions.W_4_4,
    tags=(
        SuperMarioBrosAPTags.KILL_BOWSER_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_4_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.MAGIC_MUSHROOM,
        SuperMarioBrosAPItems.FIRE_FLOWER,
    ),
)

location_data[SuperMarioBrosAPLocations.W_5_1_STARMAN] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 173,
    original_region=SuperMarioBrosAPRegions.W_5_1,
    tags=(
        SuperMarioBrosAPTags.STARMAN_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_5_1_HIDDEN_1_UP] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 174,
    original_region=SuperMarioBrosAPRegions.W_5_1,
    tags=(
        SuperMarioBrosAPTags.HIDDEN_1_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_5_1_8_ENEMY_COMBO] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 175,
    original_region=SuperMarioBrosAPRegions.W_5_1,
    tags=(
        SuperMarioBrosAPTags.ENEMY_COMBO_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_1_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.W_5_1_SUB_LEVEL] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 176,
    original_region=SuperMarioBrosAPRegions.W_5_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_5_1_SUB_LEVEL_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 177,
    original_region=SuperMarioBrosAPRegions.W_5_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_5_1_SUB_LEVEL_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 178,
    original_region=SuperMarioBrosAPRegions.W_5_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_1_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.W_5_1_SUB_LEVEL_COIN_TARGET_20] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 179,
    original_region=SuperMarioBrosAPRegions.W_5_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_1_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.W_5_1_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 180,
    original_region=SuperMarioBrosAPRegions.W_5_1,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_5_1_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 181,
    original_region=SuperMarioBrosAPRegions.W_5_1,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_1_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.W_5_2_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 182,
    original_region=SuperMarioBrosAPRegions.W_5_2,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_5_2_STARMAN] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 183,
    original_region=SuperMarioBrosAPRegions.W_5_2,
    tags=(
        SuperMarioBrosAPTags.STARMAN_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_5_2_POWER_UP_2] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 184,
    original_region=SuperMarioBrosAPRegions.W_5_2,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_5_2_POWER_UP_3] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 185,
    original_region=SuperMarioBrosAPRegions.W_5_2,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_5_2_2_ENEMY_COMBO] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 186,
    original_region=SuperMarioBrosAPRegions.W_5_2,
    tags=(
        SuperMarioBrosAPTags.ENEMY_COMBO_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_5_2_SUB_LEVEL] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 187,
    original_region=SuperMarioBrosAPRegions.W_5_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_5_2_SUB_LEVEL_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 188,
    original_region=SuperMarioBrosAPRegions.W_5_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_2_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.SWIM,
    ),
)

location_data[SuperMarioBrosAPLocations.W_5_2_SUB_LEVEL_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 189,
    original_region=SuperMarioBrosAPRegions.W_5_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_2_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.SWIM,
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.W_5_2_SUB_LEVEL_COIN_TARGET_20] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 190,
    original_region=SuperMarioBrosAPRegions.W_5_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_2_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.SWIM,
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.W_5_2_COIN_HEAVEN] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 191,
    original_region=SuperMarioBrosAPRegions.W_5_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_5_2_COIN_HEAVEN_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 192,
    original_region=SuperMarioBrosAPRegions.W_5_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_5_2_COIN_HEAVEN_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 193,
    original_region=SuperMarioBrosAPRegions.W_5_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_2_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.W_5_2_COIN_HEAVEN_20_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 194,
    original_region=SuperMarioBrosAPRegions.W_5_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_2_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.W_5_2_COIN_HEAVEN_COIN_TARGET_40] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 195,
    original_region=SuperMarioBrosAPRegions.W_5_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_2_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 3),
        SuperMarioBrosAPItems.MAGIC_MUSHROOM,
    ),
)

location_data[SuperMarioBrosAPLocations.W_5_2_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 196,
    original_region=SuperMarioBrosAPRegions.W_5_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_5_2_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 197,
    original_region=SuperMarioBrosAPRegions.W_5_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_2_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.W_5_2_20_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 198,
    original_region=SuperMarioBrosAPRegions.W_5_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_2_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.W_5_2_COIN_TARGET_28] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 199,
    original_region=SuperMarioBrosAPRegions.W_5_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_2_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 3),
    ),
)

location_data[SuperMarioBrosAPLocations.W_5_2_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 200,
    original_region=SuperMarioBrosAPRegions.W_5_2,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_5_2_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 201,
    original_region=SuperMarioBrosAPRegions.W_5_2,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_2_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.W_5_3_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 202,
    original_region=SuperMarioBrosAPRegions.W_5_3,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_3_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_5_3_1_ENEMY_COMBO] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 203,
    original_region=SuperMarioBrosAPRegions.W_5_3,
    tags=(
        SuperMarioBrosAPTags.ENEMY_COMBO_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_3_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_5_3_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 204,
    original_region=SuperMarioBrosAPRegions.W_5_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_3_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_5_3_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 205,
    original_region=SuperMarioBrosAPRegions.W_5_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_3_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.W_5_3_20_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 206,
    original_region=SuperMarioBrosAPRegions.W_5_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_3_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.W_5_3_COIN_TARGET_23] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 207,
    original_region=SuperMarioBrosAPRegions.W_5_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_3_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 3),
    ),
)

location_data[SuperMarioBrosAPLocations.W_5_3_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 208,
    original_region=SuperMarioBrosAPRegions.W_5_3,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_3_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_5_3_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 209,
    original_region=SuperMarioBrosAPRegions.W_5_3,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_3_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.W_5_4_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 210,
    original_region=SuperMarioBrosAPRegions.W_5_4,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_4_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_5_4_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 211,
    original_region=SuperMarioBrosAPRegions.W_5_4,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_4_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_5_4_COIN_TARGET_6] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 212,
    original_region=SuperMarioBrosAPRegions.W_5_4,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_4_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.W_5_4_DEFEAT_BOWSER] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 213,
    original_region=SuperMarioBrosAPRegions.W_5_4,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_4_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_5_4_KILL_BOWSER] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 214,
    original_region=SuperMarioBrosAPRegions.W_5_4,
    tags=(
        SuperMarioBrosAPTags.KILL_BOWSER_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_4_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.MAGIC_MUSHROOM,
        SuperMarioBrosAPItems.FIRE_FLOWER,
    ),
)

location_data[SuperMarioBrosAPLocations.W_6_1_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 215,
    original_region=SuperMarioBrosAPRegions.W_6_1,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_6_1_HIDDEN_1_UP] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 216,
    original_region=SuperMarioBrosAPRegions.W_6_1,
    tags=(
        SuperMarioBrosAPTags.HIDDEN_1_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_6_1_POWER_UP_2] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 217,
    original_region=SuperMarioBrosAPRegions.W_6_1,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_6_1_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 218,
    original_region=SuperMarioBrosAPRegions.W_6_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_6_1_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 219,
    original_region=SuperMarioBrosAPRegions.W_6_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_1_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.W_6_1_20_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 220,
    original_region=SuperMarioBrosAPRegions.W_6_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_1_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.W_6_1_COIN_TARGET_33] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 221,
    original_region=SuperMarioBrosAPRegions.W_6_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_1_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 3),
    ),
)

location_data[SuperMarioBrosAPLocations.W_6_1_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 222,
    original_region=SuperMarioBrosAPRegions.W_6_1,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_6_1_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 223,
    original_region=SuperMarioBrosAPRegions.W_6_1,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_1_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.W_6_2_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 224,
    original_region=SuperMarioBrosAPRegions.W_6_2,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_6_2_STARMAN] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 225,
    original_region=SuperMarioBrosAPRegions.W_6_2,
    tags=(
        SuperMarioBrosAPTags.STARMAN_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_6_2_1_ENEMY_COMBO] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 226,
    original_region=SuperMarioBrosAPRegions.W_6_2,
    tags=(
        SuperMarioBrosAPTags.ENEMY_COMBO_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_6_2_SUB_LEVEL_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 227,
    original_region=SuperMarioBrosAPRegions.W_6_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_6_2_SUB_LEVEL_1_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 228,
    original_region=SuperMarioBrosAPRegions.W_6_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_6_2_SUB_LEVEL_1_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 229,
    original_region=SuperMarioBrosAPRegions.W_6_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.W_6_2_SUB_LEVEL_1_COIN_TARGET_20] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 230,
    original_region=SuperMarioBrosAPRegions.W_6_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.W_6_2_SUB_LEVEL_2] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 231,
    original_region=SuperMarioBrosAPRegions.W_6_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_6_2_SUB_LEVEL_2_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 232,
    original_region=SuperMarioBrosAPRegions.W_6_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.SWIM,
    ),
)

location_data[SuperMarioBrosAPLocations.W_6_2_SUB_LEVEL_2_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 233,
    original_region=SuperMarioBrosAPRegions.W_6_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.SWIM,
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.W_6_2_SUB_LEVEL_2_COIN_TARGET_20] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 234,
    original_region=SuperMarioBrosAPRegions.W_6_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.SWIM,
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.W_6_2_SUB_LEVEL_3] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 235,
    original_region=SuperMarioBrosAPRegions.W_6_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_6_2_SUB_LEVEL_3_POWER_UP] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 236,
    original_region=SuperMarioBrosAPRegions.W_6_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_6_2_SUB_LEVEL_3_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 237,
    original_region=SuperMarioBrosAPRegions.W_6_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_6_2_SUB_LEVEL_3_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 238,
    original_region=SuperMarioBrosAPRegions.W_6_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.W_6_2_SUB_LEVEL_3_COIN_TARGET_18] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 239,
    original_region=SuperMarioBrosAPRegions.W_6_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.W_6_2_COIN_HEAVEN] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 240,
    original_region=SuperMarioBrosAPRegions.W_6_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_6_2_COIN_HEAVEN_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 241,
    original_region=SuperMarioBrosAPRegions.W_6_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_6_2_COIN_HEAVEN_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 242,
    original_region=SuperMarioBrosAPRegions.W_6_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.W_6_2_COIN_HEAVEN_20_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 243,
    original_region=SuperMarioBrosAPRegions.W_6_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.W_6_2_COIN_HEAVEN_COIN_TARGET_51] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 244,
    original_region=SuperMarioBrosAPRegions.W_6_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 3),
        SuperMarioBrosAPItems.MAGIC_MUSHROOM,
    ),
)

location_data[SuperMarioBrosAPLocations.W_6_2_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 245,
    original_region=SuperMarioBrosAPRegions.W_6_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_6_2_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 246,
    original_region=SuperMarioBrosAPRegions.W_6_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.W_6_2_COIN_TARGET_12] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 247,
    original_region=SuperMarioBrosAPRegions.W_6_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.W_6_2_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 248,
    original_region=SuperMarioBrosAPRegions.W_6_2,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_6_2_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 249,
    original_region=SuperMarioBrosAPRegions.W_6_2,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.W_6_3_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 250,
    original_region=SuperMarioBrosAPRegions.W_6_3,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_3_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_6_3_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 251,
    original_region=SuperMarioBrosAPRegions.W_6_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_3_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_6_3_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 252,
    original_region=SuperMarioBrosAPRegions.W_6_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_3_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.W_6_3_20_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 253,
    original_region=SuperMarioBrosAPRegions.W_6_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_3_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.W_6_3_COIN_TARGET_24] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 254,
    original_region=SuperMarioBrosAPRegions.W_6_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_3_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 3),
    ),
)

location_data[SuperMarioBrosAPLocations.W_6_3_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 255,
    original_region=SuperMarioBrosAPRegions.W_6_3,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_3_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_6_3_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 256,
    original_region=SuperMarioBrosAPRegions.W_6_3,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_3_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.W_6_4_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 257,
    original_region=SuperMarioBrosAPRegions.W_6_4,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_4_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_6_4_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 258,
    original_region=SuperMarioBrosAPRegions.W_6_4,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_4_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_6_4_COIN_TARGET_6] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 259,
    original_region=SuperMarioBrosAPRegions.W_6_4,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_4_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.W_6_4_DEFEAT_BOWSER] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 260,
    original_region=SuperMarioBrosAPRegions.W_6_4,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_4_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_6_4_KILL_BOWSER] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 261,
    original_region=SuperMarioBrosAPRegions.W_6_4,
    tags=(
        SuperMarioBrosAPTags.KILL_BOWSER_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_4_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.MAGIC_MUSHROOM,
        SuperMarioBrosAPItems.FIRE_FLOWER,
    ),
)

location_data[SuperMarioBrosAPLocations.W_7_1_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 262,
    original_region=SuperMarioBrosAPRegions.W_7_1,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_7_1_HIDDEN_1_UP] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 263,
    original_region=SuperMarioBrosAPRegions.W_7_1,
    tags=(
        SuperMarioBrosAPTags.HIDDEN_1_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_7_1_POWER_UP_2] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 264,
    original_region=SuperMarioBrosAPRegions.W_7_1,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_7_1_SUB_LEVEL] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 265,
    original_region=SuperMarioBrosAPRegions.W_7_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_7_1_SUB_LEVEL_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 266,
    original_region=SuperMarioBrosAPRegions.W_7_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_7_1_SUB_LEVEL_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 267,
    original_region=SuperMarioBrosAPRegions.W_7_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_1_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.W_7_1_SUB_LEVEL_COIN_TARGET_19] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 268,
    original_region=SuperMarioBrosAPRegions.W_7_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_1_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.W_7_1_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 269,
    original_region=SuperMarioBrosAPRegions.W_7_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_7_1_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 270,
    original_region=SuperMarioBrosAPRegions.W_7_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_1_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.W_7_1_COIN_TARGET_13] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 271,
    original_region=SuperMarioBrosAPRegions.W_7_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_1_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.W_7_1_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 272,
    original_region=SuperMarioBrosAPRegions.W_7_1,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_7_1_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 273,
    original_region=SuperMarioBrosAPRegions.W_7_1,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_1_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.W_7_2_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 274,
    original_region=SuperMarioBrosAPRegions.W_7_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_2_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.SWIM,
    ),
)

location_data[SuperMarioBrosAPLocations.W_7_2_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 275,
    original_region=SuperMarioBrosAPRegions.W_7_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_2_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.SWIM,
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.W_7_2_20_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 276,
    original_region=SuperMarioBrosAPRegions.W_7_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_2_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.SWIM,
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.W_7_2_COIN_TARGET_28] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 277,
    original_region=SuperMarioBrosAPRegions.W_7_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_2_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.SWIM,
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 3),
        SuperMarioBrosAPItems.MAGIC_MUSHROOM,
    ),
)

location_data[SuperMarioBrosAPLocations.W_7_2_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 278,
    original_region=SuperMarioBrosAPRegions.W_7_2,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_2_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.SWIM,
    ),
)

location_data[SuperMarioBrosAPLocations.W_7_2_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 279,
    original_region=SuperMarioBrosAPRegions.W_7_2,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_2_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.SWIM,
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.W_7_3_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 280,
    original_region=SuperMarioBrosAPRegions.W_7_3,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_3_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_7_3_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 281,
    original_region=SuperMarioBrosAPRegions.W_7_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_3_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_7_3_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 282,
    original_region=SuperMarioBrosAPRegions.W_7_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_3_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.W_7_3_20_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 283,
    original_region=SuperMarioBrosAPRegions.W_7_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_3_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.W_7_3_COIN_TARGET_35] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 284,
    original_region=SuperMarioBrosAPRegions.W_7_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_3_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 3),
    ),
)

location_data[SuperMarioBrosAPLocations.W_7_3_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 285,
    original_region=SuperMarioBrosAPRegions.W_7_3,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_3_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_7_3_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 286,
    original_region=SuperMarioBrosAPRegions.W_7_3,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_3_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.W_7_4_DEFEAT_BOWSER] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 287,
    original_region=SuperMarioBrosAPRegions.W_7_4,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_4_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_7_4_KILL_BOWSER] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 288,
    original_region=SuperMarioBrosAPRegions.W_7_4,
    tags=(
        SuperMarioBrosAPTags.KILL_BOWSER_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_4_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.MAGIC_MUSHROOM,
        SuperMarioBrosAPItems.FIRE_FLOWER,
    ),
)

location_data[SuperMarioBrosAPLocations.W_8_1_HIDDEN_1_UP] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 289,
    original_region=SuperMarioBrosAPRegions.W_8_1,
    tags=(
        SuperMarioBrosAPTags.HIDDEN_1_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_8_1_STARMAN] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 290,
    original_region=SuperMarioBrosAPRegions.W_8_1,
    tags=(
        SuperMarioBrosAPTags.STARMAN_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_8_1_8_ENEMY_COMBO] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 291,
    original_region=SuperMarioBrosAPRegions.W_8_1,
    tags=(
        SuperMarioBrosAPTags.ENEMY_COMBO_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_1_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.W_8_1_SUB_LEVEL] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 292,
    original_region=SuperMarioBrosAPRegions.W_8_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_8_1_SUB_LEVEL_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 293,
    original_region=SuperMarioBrosAPRegions.W_8_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_8_1_SUB_LEVEL_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 294,
    original_region=SuperMarioBrosAPRegions.W_8_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_1_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.W_8_1_SUB_LEVEL_20_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 295,
    original_region=SuperMarioBrosAPRegions.W_8_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_1_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.W_8_1_SUB_LEVEL_COIN_TARGET_27] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 296,
    original_region=SuperMarioBrosAPRegions.W_8_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_1_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 3),
    ),
)

location_data[SuperMarioBrosAPLocations.W_8_1_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 297,
    original_region=SuperMarioBrosAPRegions.W_8_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_1_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_8_1_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 298,
    original_region=SuperMarioBrosAPRegions.W_8_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_1_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.W_8_1_20_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 299,
    original_region=SuperMarioBrosAPRegions.W_8_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_1_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.W_8_1_COIN_TARGET_26] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 300,
    original_region=SuperMarioBrosAPRegions.W_8_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_1_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 3),
    ),
)

location_data[SuperMarioBrosAPLocations.W_8_1_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 301,
    original_region=SuperMarioBrosAPRegions.W_8_1,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_1_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.W_8_1_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 302,
    original_region=SuperMarioBrosAPRegions.W_8_1,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_1_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.W_8_2_HIDDEN_1_UP] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 303,
    original_region=SuperMarioBrosAPRegions.W_8_2,
    tags=(
        SuperMarioBrosAPTags.HIDDEN_1_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_8_2_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 304,
    original_region=SuperMarioBrosAPRegions.W_8_2,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_8_2_1_ENEMY_COMBO] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 305,
    original_region=SuperMarioBrosAPRegions.W_8_2,
    tags=(
        SuperMarioBrosAPTags.ENEMY_COMBO_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_8_2_SUB_LEVEL] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 306,
    original_region=SuperMarioBrosAPRegions.W_8_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_2_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.W_8_2_SUB_LEVEL_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 307,
    original_region=SuperMarioBrosAPRegions.W_8_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_2_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.W_8_2_SUB_LEVEL_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 308,
    original_region=SuperMarioBrosAPRegions.W_8_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_2_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.W_8_2_SUB_LEVEL_COIN_TARGET_20] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 309,
    original_region=SuperMarioBrosAPRegions.W_8_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_2_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.W_8_2_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 310,
    original_region=SuperMarioBrosAPRegions.W_8_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_2_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_8_2_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 311,
    original_region=SuperMarioBrosAPRegions.W_8_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_2_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.W_8_2_COIN_TARGET_12] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 312,
    original_region=SuperMarioBrosAPRegions.W_8_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_2_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.W_8_2_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 313,
    original_region=SuperMarioBrosAPRegions.W_8_2,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_2_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.W_8_2_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 314,
    original_region=SuperMarioBrosAPRegions.W_8_2,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_2_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.W_8_3_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 315,
    original_region=SuperMarioBrosAPRegions.W_8_3,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_3_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_8_3_POWER_UP_2] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 316,
    original_region=SuperMarioBrosAPRegions.W_8_3,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_3_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_8_3_1_ENEMY_COMBO] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 317,
    original_region=SuperMarioBrosAPRegions.W_8_3,
    tags=(
        SuperMarioBrosAPTags.ENEMY_COMBO_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_3_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.W_8_3_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 318,
    original_region=SuperMarioBrosAPRegions.W_8_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_3_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.MAGIC_MUSHROOM,
    ),
)

location_data[SuperMarioBrosAPLocations.W_8_3_COIN_TARGET_10] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 319,
    original_region=SuperMarioBrosAPRegions.W_8_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_3_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.MAGIC_MUSHROOM,
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.W_8_3_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 320,
    original_region=SuperMarioBrosAPRegions.W_8_3,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_3_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.MAGIC_MUSHROOM,
    ),
)

location_data[SuperMarioBrosAPLocations.W_8_3_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 321,
    original_region=SuperMarioBrosAPRegions.W_8_3,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_3_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.MAGIC_MUSHROOM,
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.W_8_4_SUB_LEVEL] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 322,
    original_region=SuperMarioBrosAPRegions.W_8_4,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_4_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.W_8_4_DEFEAT_BOWSER] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 323,
    original_region=SuperMarioBrosAPRegions.W_8_4,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_4_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.SWIM,
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.W_8_4_KILL_BOWSER] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 324,
    original_region=SuperMarioBrosAPRegions.W_8_4,
    tags=(
        SuperMarioBrosAPTags.KILL_BOWSER_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_4_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.SWIM,
        SuperMarioBrosAPItems.RUN,
        SuperMarioBrosAPItems.MAGIC_MUSHROOM,
        SuperMarioBrosAPItems.FIRE_FLOWER,
    ),
)

location_offset = 2000

location_data[SuperMarioBrosAPLocations.WSQ_1_1_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 1,
    original_region=SuperMarioBrosAPRegions.WSQ_1_1,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_1_1_HIDDEN_1_UP] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 2,
    original_region=SuperMarioBrosAPRegions.WSQ_1_1,
    tags=(
        SuperMarioBrosAPTags.HIDDEN_1_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_1_1_POWER_UP_2] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 3,
    original_region=SuperMarioBrosAPRegions.WSQ_1_1,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_1_1_STARMAN] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 4,
    original_region=SuperMarioBrosAPRegions.WSQ_1_1,
    tags=(
        SuperMarioBrosAPTags.STARMAN_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_1_1_POWER_UP_3] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 5,
    original_region=SuperMarioBrosAPRegions.WSQ_1_1,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_1_1_6_ENEMY_COMBO] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 6,
    original_region=SuperMarioBrosAPRegions.WSQ_1_1,
    tags=(
        SuperMarioBrosAPTags.ENEMY_COMBO_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_1_1_SUB_LEVEL] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 7,
    original_region=SuperMarioBrosAPRegions.WSQ_1_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_1_1_SUB_LEVEL_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 8,
    original_region=SuperMarioBrosAPRegions.WSQ_1_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_1_1_SUB_LEVEL_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 9,
    original_region=SuperMarioBrosAPRegions.WSQ_1_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_1_1_SUB_LEVEL_COIN_TARGET_19] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 10,
    original_region=SuperMarioBrosAPRegions.WSQ_1_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_1_1_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 11,
    original_region=SuperMarioBrosAPRegions.WSQ_1_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_1_1_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 12,
    original_region=SuperMarioBrosAPRegions.WSQ_1_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_1_1_COIN_TARGET_20] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 13,
    original_region=SuperMarioBrosAPRegions.WSQ_1_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_1_1_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 14,
    original_region=SuperMarioBrosAPRegions.WSQ_1_1,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_1_1_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 15,
    original_region=SuperMarioBrosAPRegions.WSQ_1_1,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_1_2_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 16,
    original_region=SuperMarioBrosAPRegions.WSQ_1_2,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_1_2_STARMAN] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 17,
    original_region=SuperMarioBrosAPRegions.WSQ_1_2,
    tags=(
        SuperMarioBrosAPTags.STARMAN_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.MAGIC_MUSHROOM,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_1_2_POWER_UP_2] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 18,
    original_region=SuperMarioBrosAPRegions.WSQ_1_2,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.MAGIC_MUSHROOM,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_1_2_HIDDEN_1_UP] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 19,
    original_region=SuperMarioBrosAPRegions.WSQ_1_2,
    tags=(
        SuperMarioBrosAPTags.HIDDEN_1_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_1_2_POWER_UP_3] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 20,
    original_region=SuperMarioBrosAPRegions.WSQ_1_2,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_1_2_4_ENEMY_COMBO] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 21,
    original_region=SuperMarioBrosAPRegions.WSQ_1_2,
    tags=(
        SuperMarioBrosAPTags.ENEMY_COMBO_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_1_2_SUB_LEVEL] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 22,
    original_region=SuperMarioBrosAPRegions.WSQ_1_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_1_2_SUB_LEVEL_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 23,
    original_region=SuperMarioBrosAPRegions.WSQ_1_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_1_2_SUB_LEVEL_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 24,
    original_region=SuperMarioBrosAPRegions.WSQ_1_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_1_2_SUB_LEVEL_20_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 25,
    original_region=SuperMarioBrosAPRegions.WSQ_1_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_1_2_SUB_LEVEL_COIN_TARGET_27] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 26,
    original_region=SuperMarioBrosAPRegions.WSQ_1_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 3),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_1_2_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 27,
    original_region=SuperMarioBrosAPRegions.WSQ_1_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_1_2_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 28,
    original_region=SuperMarioBrosAPRegions.WSQ_1_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_1_2_20_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 29,
    original_region=SuperMarioBrosAPRegions.WSQ_1_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2)
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_1_2_COIN_TARGET_41] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 30,
    original_region=SuperMarioBrosAPRegions.WSQ_1_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 3),
        SuperMarioBrosAPItems.MAGIC_MUSHROOM,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_1_2_WARP_ZONE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 31,
    original_region=SuperMarioBrosAPRegions.WSQ_1_2,
    tags=(
        SuperMarioBrosAPTags.WARP_ZONE_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_1_2_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 32,
    original_region=SuperMarioBrosAPRegions.WSQ_1_2,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_1_2_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 33,
    original_region=SuperMarioBrosAPRegions.WSQ_1_2,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_1_3_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 34,
    original_region=SuperMarioBrosAPRegions.WSQ_1_3,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_1_3_1_ENEMY_COMBO] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 35,
    original_region=SuperMarioBrosAPRegions.WSQ_1_3,
    tags=(
        SuperMarioBrosAPTags.ENEMY_COMBO_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_1_3_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 36,
    original_region=SuperMarioBrosAPRegions.WSQ_1_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_1_3_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 37,
    original_region=SuperMarioBrosAPRegions.WSQ_1_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_1_3_20_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 38,
    original_region=SuperMarioBrosAPRegions.WSQ_1_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_1_3_COIN_TARGET_23] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 39,
    original_region=SuperMarioBrosAPRegions.WSQ_1_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 3),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_1_3_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 40,
    original_region=SuperMarioBrosAPRegions.WSQ_1_3,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_1_3_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 41,
    original_region=SuperMarioBrosAPRegions.WSQ_1_3,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_1_4_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 42,
    original_region=SuperMarioBrosAPRegions.WSQ_1_4,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_4_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_1_4_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 43,
    original_region=SuperMarioBrosAPRegions.WSQ_1_4,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_4_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_1_4_COIN_TARGET_6] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 44,
    original_region=SuperMarioBrosAPRegions.WSQ_1_4,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_4_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_1_4_DEFEAT_BOWSER] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 45,
    original_region=SuperMarioBrosAPRegions.WSQ_1_4,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_4_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_1_4_KILL_BOWSER] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 46,
    original_region=SuperMarioBrosAPRegions.WSQ_1_4,
    tags=(
        SuperMarioBrosAPTags.KILL_BOWSER_LOCATION,
        SuperMarioBrosAPTags.WORLD_1_4_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.MAGIC_MUSHROOM,
        SuperMarioBrosAPItems.FIRE_FLOWER,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_2_1_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 47,
    original_region=SuperMarioBrosAPRegions.WSQ_2_1,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_2_1_HIDDEN_1_UP] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 48,
    original_region=SuperMarioBrosAPRegions.WSQ_2_1,
    tags=(
        SuperMarioBrosAPTags.HIDDEN_1_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_2_1_POWER_UP_2] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 49,
    original_region=SuperMarioBrosAPRegions.WSQ_2_1,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_2_1_STARMAN] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 50,
    original_region=SuperMarioBrosAPRegions.WSQ_2_1,
    tags=(
        SuperMarioBrosAPTags.STARMAN_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_2_1_POWER_UP_3] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 51,
    original_region=SuperMarioBrosAPRegions.WSQ_2_1,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_2_1_POWER_UP_4] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 52,
    original_region=SuperMarioBrosAPRegions.WSQ_2_1,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_2_1_5_ENEMY_COMBO] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 53,
    original_region=SuperMarioBrosAPRegions.WSQ_2_1,
    tags=(
        SuperMarioBrosAPTags.ENEMY_COMBO_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_2_1_SUB_LEVEL] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 54,
    original_region=SuperMarioBrosAPRegions.WSQ_2_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_2_1_SUB_LEVEL_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 55,
    original_region=SuperMarioBrosAPRegions.WSQ_2_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_2_1_SUB_LEVEL_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 56,
    original_region=SuperMarioBrosAPRegions.WSQ_2_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_2_1_SUB_LEVEL_COIN_TARGET_19] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 57,
    original_region=SuperMarioBrosAPRegions.WSQ_2_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_2_1_COIN_HEAVEN] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 58,
    original_region=SuperMarioBrosAPRegions.WSQ_2_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_2_1_COIN_HEAVEN_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 59,
    original_region=SuperMarioBrosAPRegions.WSQ_2_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_2_1_COIN_HEAVEN_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 60,
    original_region=SuperMarioBrosAPRegions.WSQ_2_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_2_1_COIN_HEAVEN_20_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 61,
    original_region=SuperMarioBrosAPRegions.WSQ_2_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_2_1_COIN_HEAVEN_COIN_TARGET_40] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 62,
    original_region=SuperMarioBrosAPRegions.WSQ_2_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 3),
        SuperMarioBrosAPItems.MAGIC_MUSHROOM,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_2_1_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 63,
    original_region=SuperMarioBrosAPRegions.WSQ_2_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_2_1_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 64,
    original_region=SuperMarioBrosAPRegions.WSQ_2_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_2_1_20_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 65,
    original_region=SuperMarioBrosAPRegions.WSQ_2_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_2_1_COIN_TARGET_29] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 66,
    original_region=SuperMarioBrosAPRegions.WSQ_2_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 3),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_2_1_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 67,
    original_region=SuperMarioBrosAPRegions.WSQ_2_1,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_2_1_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 68,
    original_region=SuperMarioBrosAPRegions.WSQ_2_1,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_2_2_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 69,
    original_region=SuperMarioBrosAPRegions.WSQ_2_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.SWIM,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_2_2_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 70,
    original_region=SuperMarioBrosAPRegions.WSQ_2_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.SWIM,
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1)
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_2_2_20_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 71,
    original_region=SuperMarioBrosAPRegions.WSQ_2_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.SWIM,
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_2_2_COIN_TARGET_28] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 72,
    original_region=SuperMarioBrosAPRegions.WSQ_2_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.SWIM,
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 3),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_2_2_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 73,
    original_region=SuperMarioBrosAPRegions.WSQ_2_2,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.SWIM,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_2_2_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 74,
    original_region=SuperMarioBrosAPRegions.WSQ_2_2,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.SWIM,
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_2_3_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 75,
    original_region=SuperMarioBrosAPRegions.WSQ_2_3,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_2_3_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 76,
    original_region=SuperMarioBrosAPRegions.WSQ_2_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_2_3_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 77,
    original_region=SuperMarioBrosAPRegions.WSQ_2_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_2_3_20_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 78,
    original_region=SuperMarioBrosAPRegions.WSQ_2_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_2_3_COIN_TARGET_35] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 79,
    original_region=SuperMarioBrosAPRegions.WSQ_2_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 3),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_2_3_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 80,
    original_region=SuperMarioBrosAPRegions.WSQ_2_3,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_2_3_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 81,
    original_region=SuperMarioBrosAPRegions.WSQ_2_3,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_2_4_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 82,
    original_region=SuperMarioBrosAPRegions.WSQ_2_4,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_4_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_2_4_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 83,
    original_region=SuperMarioBrosAPRegions.WSQ_2_4,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_4_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_2_4_COIN_TARGET_6] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 84,
    original_region=SuperMarioBrosAPRegions.WSQ_2_4,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_4_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_2_4_DEFEAT_BOWSER] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 85,
    original_region=SuperMarioBrosAPRegions.WSQ_2_4,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_4_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_2_4_KILL_BOWSER] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 86,
    original_region=SuperMarioBrosAPRegions.WSQ_2_4,
    tags=(
        SuperMarioBrosAPTags.KILL_BOWSER_LOCATION,
        SuperMarioBrosAPTags.WORLD_2_4_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.MAGIC_MUSHROOM,
        SuperMarioBrosAPItems.FIRE_FLOWER,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_3_1_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 87,
    original_region=SuperMarioBrosAPRegions.WSQ_3_1,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_3_1_HIDDEN_1_UP] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 88,
    original_region=SuperMarioBrosAPRegions.WSQ_3_1,
    tags=(
        SuperMarioBrosAPTags.HIDDEN_1_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_3_1_STARMAN] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 89,
    original_region=SuperMarioBrosAPRegions.WSQ_3_1,
    tags=(
        SuperMarioBrosAPTags.STARMAN_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (
            SuperMarioBrosAPItems.RUN,
            SuperMarioBrosAPItems.MAGIC_MUSHROOM,
        ),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_3_1_POWER_UP_2] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 90,
    original_region=SuperMarioBrosAPRegions.WSQ_3_1,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_3_1_POWER_UP_3] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 91,
    original_region=SuperMarioBrosAPRegions.WSQ_3_1,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_3_1_5_ENEMY_COMBO] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 92,
    original_region=SuperMarioBrosAPRegions.WSQ_3_1,
    tags=(
        SuperMarioBrosAPTags.ENEMY_COMBO_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_3_1_SUB_LEVEL] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 93,
    original_region=SuperMarioBrosAPRegions.WSQ_3_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_3_1_SUB_LEVEL_POWER_UP] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 94,
    original_region=SuperMarioBrosAPRegions.WSQ_3_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_3_1_SUB_LEVEL_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 95,
    original_region=SuperMarioBrosAPRegions.WSQ_3_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_3_1_SUB_LEVEL_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 96,
    original_region=SuperMarioBrosAPRegions.WSQ_3_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
        SuperMarioBrosAPItems.MAGIC_MUSHROOM,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_3_1_SUB_LEVEL_COIN_TARGET_12] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 97,
    original_region=SuperMarioBrosAPRegions.WSQ_3_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
        SuperMarioBrosAPItems.MAGIC_MUSHROOM,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_3_1_COIN_HEAVEN] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 98,
    original_region=SuperMarioBrosAPRegions.WSQ_3_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_3_1_COIN_HEAVEN_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 99,
    original_region=SuperMarioBrosAPRegions.WSQ_3_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_3_1_COIN_HEAVEN_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 100,
    original_region=SuperMarioBrosAPRegions.WSQ_3_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_3_1_COIN_HEAVEN_20_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 101,
    original_region=SuperMarioBrosAPRegions.WSQ_3_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_3_1_COIN_HEAVEN_COIN_TARGET_51] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 102,
    original_region=SuperMarioBrosAPRegions.WSQ_3_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 3),
        SuperMarioBrosAPItems.MAGIC_MUSHROOM,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_3_1_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 103,
    original_region=SuperMarioBrosAPRegions.WSQ_3_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_3_1_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 104,
    original_region=SuperMarioBrosAPRegions.WSQ_3_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_3_1_COIN_TARGET_16] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 105,
    original_region=SuperMarioBrosAPRegions.WSQ_3_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_3_1_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 106,
    original_region=SuperMarioBrosAPRegions.WSQ_3_1,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_3_1_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 107,
    original_region=SuperMarioBrosAPRegions.WSQ_3_1,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_3_2_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 108,
    original_region=SuperMarioBrosAPRegions.WSQ_3_2,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_3_2_STARMAN] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 109,
    original_region=SuperMarioBrosAPRegions.WSQ_3_2,
    tags=(
        SuperMarioBrosAPTags.STARMAN_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_3_2_8_ENEMY_COMBO] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 110,
    original_region=SuperMarioBrosAPRegions.WSQ_3_2,
    tags=(
        SuperMarioBrosAPTags.ENEMY_COMBO_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_3_2_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 111,
    original_region=SuperMarioBrosAPRegions.WSQ_3_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_3_2_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 112,
    original_region=SuperMarioBrosAPRegions.WSQ_3_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_3_2_COIN_TARGET_17] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 113,
    original_region=SuperMarioBrosAPRegions.WSQ_3_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
        (SuperMarioBrosAPItems.FIRE_FLOWER, SuperMarioBrosAPItems.STARMAN),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_3_2_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 114,
    original_region=SuperMarioBrosAPRegions.WSQ_3_2,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_3_2_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 115,
    original_region=SuperMarioBrosAPRegions.WSQ_3_2,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_3_3_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 116,
    original_region=SuperMarioBrosAPRegions.WSQ_3_3,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_3_3_1_ENEMY_COMBO] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 117,
    original_region=SuperMarioBrosAPRegions.WSQ_3_3,
    tags=(
        SuperMarioBrosAPTags.ENEMY_COMBO_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_3_3_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 118,
    original_region=SuperMarioBrosAPRegions.WSQ_3_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_3_3_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 119,
    original_region=SuperMarioBrosAPRegions.WSQ_3_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_3_3_20_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 120,
    original_region=SuperMarioBrosAPRegions.WSQ_3_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_3_3_COIN_TARGET_22] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 121,
    original_region=SuperMarioBrosAPRegions.WSQ_3_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 3),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_3_3_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 122,
    original_region=SuperMarioBrosAPRegions.WSQ_3_3,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_3_3_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 123,
    original_region=SuperMarioBrosAPRegions.WSQ_3_3,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_3_4_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 124,
    original_region=SuperMarioBrosAPRegions.WSQ_3_4,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_4_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_3_4_COIN_TARGET_5] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 125,
    original_region=SuperMarioBrosAPRegions.WSQ_3_4,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_4_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_3_4_DEFEAT_BOWSER] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 126,
    original_region=SuperMarioBrosAPRegions.WSQ_3_4,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_4_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_3_4_KILL_BOWSER] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 127,
    original_region=SuperMarioBrosAPRegions.WSQ_3_4,
    tags=(
        SuperMarioBrosAPTags.KILL_BOWSER_LOCATION,
        SuperMarioBrosAPTags.WORLD_3_4_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.MAGIC_MUSHROOM,
        SuperMarioBrosAPItems.FIRE_FLOWER,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_4_1_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 128,
    original_region=SuperMarioBrosAPRegions.WSQ_4_1,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_4_1_HIDDEN_1_UP] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 129,
    original_region=SuperMarioBrosAPRegions.WSQ_4_1,
    tags=(
        SuperMarioBrosAPTags.HIDDEN_1_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_4_1_POWER_UP_2] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 130,
    original_region=SuperMarioBrosAPRegions.WSQ_4_1,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_4_1_SUB_LEVEL] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 131,
    original_region=SuperMarioBrosAPRegions.WSQ_4_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_4_1_SUB_LEVEL_POWER_UP] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 132,
    original_region=SuperMarioBrosAPRegions.WSQ_4_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_4_1_SUB_LEVEL_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 133,
    original_region=SuperMarioBrosAPRegions.WSQ_4_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_4_1_SUB_LEVEL_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 134,
    original_region=SuperMarioBrosAPRegions.WSQ_4_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_4_1_SUB_LEVEL_COIN_TARGET_18] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 135,
    original_region=SuperMarioBrosAPRegions.WSQ_4_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_4_1_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 136,
    original_region=SuperMarioBrosAPRegions.WSQ_4_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_4_1_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 137,
    original_region=SuperMarioBrosAPRegions.WSQ_4_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_4_1_20_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 138,
    original_region=SuperMarioBrosAPRegions.WSQ_4_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_4_1_COIN_TARGET_44] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 139,
    original_region=SuperMarioBrosAPRegions.WSQ_4_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 3),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_4_1_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 140,
    original_region=SuperMarioBrosAPRegions.WSQ_4_1,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_4_1_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 141,
    original_region=SuperMarioBrosAPRegions.WSQ_4_1,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_4_2_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 142,
    original_region=SuperMarioBrosAPRegions.WSQ_4_2,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_4_2_POWER_UP_2] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 143,
    original_region=SuperMarioBrosAPRegions.WSQ_4_2,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_4_2_STARMAN] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 144,
    original_region=SuperMarioBrosAPRegions.WSQ_4_2,
    tags=(
        SuperMarioBrosAPTags.STARMAN_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_4_2_POWER_UP_3] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 145,
    original_region=SuperMarioBrosAPRegions.WSQ_4_2,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_4_2_POWER_UP_4] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 146,
    original_region=SuperMarioBrosAPRegions.WSQ_4_2,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_4_2_1_ENEMY_COMBO] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 147,
    original_region=SuperMarioBrosAPRegions.WSQ_4_2,
    tags=(
        SuperMarioBrosAPTags.ENEMY_COMBO_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_4_2_SUB_LEVEL] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 148,
    original_region=SuperMarioBrosAPRegions.WSQ_4_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_4_2_SUB_LEVEL_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 149,
    original_region=SuperMarioBrosAPRegions.WSQ_4_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_4_2_SUB_LEVEL_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 150,
    original_region=SuperMarioBrosAPRegions.WSQ_4_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_4_2_SUB_LEVEL_COIN_TARGET_20] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 151,
    original_region=SuperMarioBrosAPRegions.WSQ_4_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_4_2_MUSHROOM_AREA_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 152,
    original_region=SuperMarioBrosAPRegions.WSQ_4_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_4_2_MUSHROOM_AREA_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 153,
    original_region=SuperMarioBrosAPRegions.WSQ_4_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_4_2_MUSHROOM_AREA_COIN_TARGET_19] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 154,
    original_region=SuperMarioBrosAPRegions.WSQ_4_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_4_2_MUSHROOM_AREA_WARP_ZONE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 155,
    original_region=SuperMarioBrosAPRegions.WSQ_4_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.WARP_ZONE_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_4_2_WARP_ZONE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 156,
    original_region=SuperMarioBrosAPRegions.WSQ_4_2,
    tags=(
        SuperMarioBrosAPTags.WARP_ZONE_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_4_2_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 157,
    original_region=SuperMarioBrosAPRegions.WSQ_4_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_4_2_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 158,
    original_region=SuperMarioBrosAPRegions.WSQ_4_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_4_2_20_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 159,
    original_region=SuperMarioBrosAPRegions.WSQ_4_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_4_2_COIN_TARGET_43] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 160,
    original_region=SuperMarioBrosAPRegions.WSQ_4_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 3),
        SuperMarioBrosAPItems.MAGIC_MUSHROOM,
        SuperMarioBrosAPItems.FIRE_FLOWER,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_4_2_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 161,
    original_region=SuperMarioBrosAPRegions.WSQ_4_2,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_4_2_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 162,
    original_region=SuperMarioBrosAPRegions.WSQ_4_2,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_4_3_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 163,
    original_region=SuperMarioBrosAPRegions.WSQ_4_3,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_4_3_1_ENEMY_COMBO] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 164,
    original_region=SuperMarioBrosAPRegions.WSQ_4_3,
    tags=(
        SuperMarioBrosAPTags.ENEMY_COMBO_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_4_3_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 165,
    original_region=SuperMarioBrosAPRegions.WSQ_4_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_4_3_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 166,
    original_region=SuperMarioBrosAPRegions.WSQ_4_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_4_3_20_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 167,
    original_region=SuperMarioBrosAPRegions.WSQ_4_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_4_3_COIN_TARGET_27] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 168,
    original_region=SuperMarioBrosAPRegions.WSQ_4_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 3),
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_4_3_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 169,
    original_region=SuperMarioBrosAPRegions.WSQ_4_3,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_4_3_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 170,
    original_region=SuperMarioBrosAPRegions.WSQ_4_3,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_4_4_DEFEAT_BOWSER] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 171,
    original_region=SuperMarioBrosAPRegions.WSQ_4_4,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_4_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_4_4_KILL_BOWSER] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 172,
    original_region=SuperMarioBrosAPRegions.WSQ_4_4,
    tags=(
        SuperMarioBrosAPTags.KILL_BOWSER_LOCATION,
        SuperMarioBrosAPTags.WORLD_4_4_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.MAGIC_MUSHROOM,
        SuperMarioBrosAPItems.FIRE_FLOWER,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_5_1_STARMAN] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 173,
    original_region=SuperMarioBrosAPRegions.WSQ_5_1,
    tags=(
        SuperMarioBrosAPTags.STARMAN_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_5_1_HIDDEN_1_UP] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 174,
    original_region=SuperMarioBrosAPRegions.WSQ_5_1,
    tags=(
        SuperMarioBrosAPTags.HIDDEN_1_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_5_1_8_ENEMY_COMBO] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 175,
    original_region=SuperMarioBrosAPRegions.WSQ_5_1,
    tags=(
        SuperMarioBrosAPTags.ENEMY_COMBO_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_5_1_SUB_LEVEL] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 176,
    original_region=SuperMarioBrosAPRegions.WSQ_5_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_5_1_SUB_LEVEL_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 177,
    original_region=SuperMarioBrosAPRegions.WSQ_5_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_5_1_SUB_LEVEL_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 178,
    original_region=SuperMarioBrosAPRegions.WSQ_5_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_5_1_SUB_LEVEL_COIN_TARGET_20] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 179,
    original_region=SuperMarioBrosAPRegions.WSQ_5_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_5_1_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 180,
    original_region=SuperMarioBrosAPRegions.WSQ_5_1,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_5_1_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 181,
    original_region=SuperMarioBrosAPRegions.WSQ_5_1,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_5_2_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 182,
    original_region=SuperMarioBrosAPRegions.WSQ_5_2,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_5_2_STARMAN] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 183,
    original_region=SuperMarioBrosAPRegions.WSQ_5_2,
    tags=(
        SuperMarioBrosAPTags.STARMAN_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_5_2_POWER_UP_2] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 184,
    original_region=SuperMarioBrosAPRegions.WSQ_5_2,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_5_2_POWER_UP_3] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 185,
    original_region=SuperMarioBrosAPRegions.WSQ_5_2,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_5_2_2_ENEMY_COMBO] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 186,
    original_region=SuperMarioBrosAPRegions.WSQ_5_2,
    tags=(
        SuperMarioBrosAPTags.ENEMY_COMBO_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_5_2_SUB_LEVEL] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 187,
    original_region=SuperMarioBrosAPRegions.WSQ_5_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_5_2_SUB_LEVEL_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 188,
    original_region=SuperMarioBrosAPRegions.WSQ_5_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.SWIM,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_5_2_SUB_LEVEL_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 189,
    original_region=SuperMarioBrosAPRegions.WSQ_5_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.SWIM,
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_5_2_SUB_LEVEL_COIN_TARGET_20] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 190,
    original_region=SuperMarioBrosAPRegions.WSQ_5_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.SWIM,
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_5_2_COIN_HEAVEN] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 191,
    original_region=SuperMarioBrosAPRegions.WSQ_5_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_5_2_COIN_HEAVEN_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 192,
    original_region=SuperMarioBrosAPRegions.WSQ_5_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_5_2_COIN_HEAVEN_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 193,
    original_region=SuperMarioBrosAPRegions.WSQ_5_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_5_2_COIN_HEAVEN_20_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 194,
    original_region=SuperMarioBrosAPRegions.WSQ_5_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_5_2_COIN_HEAVEN_COIN_TARGET_40] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 195,
    original_region=SuperMarioBrosAPRegions.WSQ_5_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 3),
        SuperMarioBrosAPItems.MAGIC_MUSHROOM,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_5_2_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 196,
    original_region=SuperMarioBrosAPRegions.WSQ_5_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_5_2_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 197,
    original_region=SuperMarioBrosAPRegions.WSQ_5_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_5_2_20_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 198,
    original_region=SuperMarioBrosAPRegions.WSQ_5_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_5_2_COIN_TARGET_28] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 199,
    original_region=SuperMarioBrosAPRegions.WSQ_5_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 3),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_5_2_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 200,
    original_region=SuperMarioBrosAPRegions.WSQ_5_2,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_5_2_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 201,
    original_region=SuperMarioBrosAPRegions.WSQ_5_2,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_5_3_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 202,
    original_region=SuperMarioBrosAPRegions.WSQ_5_3,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_5_3_1_ENEMY_COMBO] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 203,
    original_region=SuperMarioBrosAPRegions.WSQ_5_3,
    tags=(
        SuperMarioBrosAPTags.ENEMY_COMBO_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_5_3_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 204,
    original_region=SuperMarioBrosAPRegions.WSQ_5_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_5_3_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 205,
    original_region=SuperMarioBrosAPRegions.WSQ_5_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_5_3_20_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 206,
    original_region=SuperMarioBrosAPRegions.WSQ_5_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_5_3_COIN_TARGET_23] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 207,
    original_region=SuperMarioBrosAPRegions.WSQ_5_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 3),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_5_3_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 208,
    original_region=SuperMarioBrosAPRegions.WSQ_5_3,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_5_3_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 209,
    original_region=SuperMarioBrosAPRegions.WSQ_5_3,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_5_4_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 210,
    original_region=SuperMarioBrosAPRegions.WSQ_5_4,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_4_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_5_4_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 211,
    original_region=SuperMarioBrosAPRegions.WSQ_5_4,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_4_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_5_4_COIN_TARGET_6] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 212,
    original_region=SuperMarioBrosAPRegions.WSQ_5_4,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_4_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_5_4_DEFEAT_BOWSER] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 213,
    original_region=SuperMarioBrosAPRegions.WSQ_5_4,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_4_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_5_4_KILL_BOWSER] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 214,
    original_region=SuperMarioBrosAPRegions.WSQ_5_4,
    tags=(
        SuperMarioBrosAPTags.KILL_BOWSER_LOCATION,
        SuperMarioBrosAPTags.WORLD_5_4_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.MAGIC_MUSHROOM,
        SuperMarioBrosAPItems.FIRE_FLOWER,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_6_1_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 215,
    original_region=SuperMarioBrosAPRegions.WSQ_6_1,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_6_1_HIDDEN_1_UP] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 216,
    original_region=SuperMarioBrosAPRegions.WSQ_6_1,
    tags=(
        SuperMarioBrosAPTags.HIDDEN_1_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_6_1_POWER_UP_2] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 217,
    original_region=SuperMarioBrosAPRegions.WSQ_6_1,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_6_1_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 218,
    original_region=SuperMarioBrosAPRegions.WSQ_6_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_6_1_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 219,
    original_region=SuperMarioBrosAPRegions.WSQ_6_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_6_1_20_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 220,
    original_region=SuperMarioBrosAPRegions.WSQ_6_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_6_1_COIN_TARGET_33] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 221,
    original_region=SuperMarioBrosAPRegions.WSQ_6_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 3),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_6_1_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 222,
    original_region=SuperMarioBrosAPRegions.WSQ_6_1,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_6_1_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 223,
    original_region=SuperMarioBrosAPRegions.WSQ_6_1,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_6_2_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 224,
    original_region=SuperMarioBrosAPRegions.WSQ_6_2,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_6_2_STARMAN] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 225,
    original_region=SuperMarioBrosAPRegions.WSQ_6_2,
    tags=(
        SuperMarioBrosAPTags.STARMAN_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_6_2_1_ENEMY_COMBO] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 226,
    original_region=SuperMarioBrosAPRegions.WSQ_6_2,
    tags=(
        SuperMarioBrosAPTags.ENEMY_COMBO_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_6_2_SUB_LEVEL_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 227,
    original_region=SuperMarioBrosAPRegions.WSQ_6_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_6_2_SUB_LEVEL_1_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 228,
    original_region=SuperMarioBrosAPRegions.WSQ_6_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_6_2_SUB_LEVEL_1_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 229,
    original_region=SuperMarioBrosAPRegions.WSQ_6_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_6_2_SUB_LEVEL_1_COIN_TARGET_20] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 230,
    original_region=SuperMarioBrosAPRegions.WSQ_6_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_6_2_SUB_LEVEL_2] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 231,
    original_region=SuperMarioBrosAPRegions.WSQ_6_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_6_2_SUB_LEVEL_2_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 232,
    original_region=SuperMarioBrosAPRegions.WSQ_6_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.SWIM,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_6_2_SUB_LEVEL_2_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 233,
    original_region=SuperMarioBrosAPRegions.WSQ_6_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.SWIM,
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_6_2_SUB_LEVEL_2_COIN_TARGET_20] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 234,
    original_region=SuperMarioBrosAPRegions.WSQ_6_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.SWIM,
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_6_2_SUB_LEVEL_3] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 235,
    original_region=SuperMarioBrosAPRegions.WSQ_6_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_6_2_SUB_LEVEL_3_POWER_UP] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 236,
    original_region=SuperMarioBrosAPRegions.WSQ_6_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_6_2_SUB_LEVEL_3_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 237,
    original_region=SuperMarioBrosAPRegions.WSQ_6_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_6_2_SUB_LEVEL_3_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 238,
    original_region=SuperMarioBrosAPRegions.WSQ_6_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_6_2_SUB_LEVEL_3_COIN_TARGET_18] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 239,
    original_region=SuperMarioBrosAPRegions.WSQ_6_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_6_2_COIN_HEAVEN] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 240,
    original_region=SuperMarioBrosAPRegions.WSQ_6_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_6_2_COIN_HEAVEN_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 241,
    original_region=SuperMarioBrosAPRegions.WSQ_6_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_6_2_COIN_HEAVEN_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 242,
    original_region=SuperMarioBrosAPRegions.WSQ_6_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_6_2_COIN_HEAVEN_20_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 243,
    original_region=SuperMarioBrosAPRegions.WSQ_6_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_6_2_COIN_HEAVEN_COIN_TARGET_51] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 244,
    original_region=SuperMarioBrosAPRegions.WSQ_6_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 3),
        SuperMarioBrosAPItems.MAGIC_MUSHROOM,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_6_2_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 245,
    original_region=SuperMarioBrosAPRegions.WSQ_6_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_6_2_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 246,
    original_region=SuperMarioBrosAPRegions.WSQ_6_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_6_2_COIN_TARGET_12] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 247,
    original_region=SuperMarioBrosAPRegions.WSQ_6_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_6_2_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 248,
    original_region=SuperMarioBrosAPRegions.WSQ_6_2,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_6_2_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 249,
    original_region=SuperMarioBrosAPRegions.WSQ_6_2,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_6_3_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 250,
    original_region=SuperMarioBrosAPRegions.WSQ_6_3,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_6_3_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 251,
    original_region=SuperMarioBrosAPRegions.WSQ_6_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_6_3_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 252,
    original_region=SuperMarioBrosAPRegions.WSQ_6_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_6_3_20_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 253,
    original_region=SuperMarioBrosAPRegions.WSQ_6_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_6_3_COIN_TARGET_24] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 254,
    original_region=SuperMarioBrosAPRegions.WSQ_6_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 3),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_6_3_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 255,
    original_region=SuperMarioBrosAPRegions.WSQ_6_3,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_6_3_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 256,
    original_region=SuperMarioBrosAPRegions.WSQ_6_3,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_6_4_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 257,
    original_region=SuperMarioBrosAPRegions.WSQ_6_4,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_4_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_6_4_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 258,
    original_region=SuperMarioBrosAPRegions.WSQ_6_4,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_4_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_6_4_COIN_TARGET_6] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 259,
    original_region=SuperMarioBrosAPRegions.WSQ_6_4,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_4_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_6_4_DEFEAT_BOWSER] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 260,
    original_region=SuperMarioBrosAPRegions.WSQ_6_4,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_4_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_6_4_KILL_BOWSER] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 261,
    original_region=SuperMarioBrosAPRegions.WSQ_6_4,
    tags=(
        SuperMarioBrosAPTags.KILL_BOWSER_LOCATION,
        SuperMarioBrosAPTags.WORLD_6_4_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.MAGIC_MUSHROOM,
        SuperMarioBrosAPItems.FIRE_FLOWER,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_7_1_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 262,
    original_region=SuperMarioBrosAPRegions.WSQ_7_1,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_7_1_HIDDEN_1_UP] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 263,
    original_region=SuperMarioBrosAPRegions.WSQ_7_1,
    tags=(
        SuperMarioBrosAPTags.HIDDEN_1_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_7_1_POWER_UP_2] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 264,
    original_region=SuperMarioBrosAPRegions.WSQ_7_1,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_7_1_SUB_LEVEL] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 265,
    original_region=SuperMarioBrosAPRegions.WSQ_7_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_7_1_SUB_LEVEL_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 266,
    original_region=SuperMarioBrosAPRegions.WSQ_7_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_7_1_SUB_LEVEL_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 267,
    original_region=SuperMarioBrosAPRegions.WSQ_7_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_7_1_SUB_LEVEL_COIN_TARGET_19] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 268,
    original_region=SuperMarioBrosAPRegions.WSQ_7_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_7_1_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 269,
    original_region=SuperMarioBrosAPRegions.WSQ_7_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_7_1_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 270,
    original_region=SuperMarioBrosAPRegions.WSQ_7_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_7_1_COIN_TARGET_13] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 271,
    original_region=SuperMarioBrosAPRegions.WSQ_7_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_7_1_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 272,
    original_region=SuperMarioBrosAPRegions.WSQ_7_1,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_7_1_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 273,
    original_region=SuperMarioBrosAPRegions.WSQ_7_1,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_7_2_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 274,
    original_region=SuperMarioBrosAPRegions.WSQ_7_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.SWIM,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_7_2_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 275,
    original_region=SuperMarioBrosAPRegions.WSQ_7_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.SWIM,
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_7_2_20_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 276,
    original_region=SuperMarioBrosAPRegions.WSQ_7_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.SWIM,
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_7_2_COIN_TARGET_28] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 277,
    original_region=SuperMarioBrosAPRegions.WSQ_7_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.SWIM,
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 3),
        SuperMarioBrosAPItems.MAGIC_MUSHROOM,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_7_2_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 278,
    original_region=SuperMarioBrosAPRegions.WSQ_7_2,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.SWIM,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_7_2_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 279,
    original_region=SuperMarioBrosAPRegions.WSQ_7_2,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.SWIM,
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_7_3_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 280,
    original_region=SuperMarioBrosAPRegions.WSQ_7_3,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_7_3_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 281,
    original_region=SuperMarioBrosAPRegions.WSQ_7_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_7_3_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 282,
    original_region=SuperMarioBrosAPRegions.WSQ_7_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_7_3_20_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 283,
    original_region=SuperMarioBrosAPRegions.WSQ_7_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_7_3_COIN_TARGET_35] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 284,
    original_region=SuperMarioBrosAPRegions.WSQ_7_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 3),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_7_3_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 285,
    original_region=SuperMarioBrosAPRegions.WSQ_7_3,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_7_3_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 286,
    original_region=SuperMarioBrosAPRegions.WSQ_7_3,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_7_4_DEFEAT_BOWSER] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 287,
    original_region=SuperMarioBrosAPRegions.WSQ_7_4,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_4_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_7_4_KILL_BOWSER] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 288,
    original_region=SuperMarioBrosAPRegions.WSQ_7_4,
    tags=(
        SuperMarioBrosAPTags.KILL_BOWSER_LOCATION,
        SuperMarioBrosAPTags.WORLD_7_4_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.MAGIC_MUSHROOM,
        SuperMarioBrosAPItems.FIRE_FLOWER,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_8_1_HIDDEN_1_UP] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 289,
    original_region=SuperMarioBrosAPRegions.WSQ_8_1,
    tags=(
        SuperMarioBrosAPTags.HIDDEN_1_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_8_1_STARMAN] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 290,
    original_region=SuperMarioBrosAPRegions.WSQ_8_1,
    tags=(
        SuperMarioBrosAPTags.STARMAN_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_8_1_8_ENEMY_COMBO] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 291,
    original_region=SuperMarioBrosAPRegions.WSQ_8_1,
    tags=(
        SuperMarioBrosAPTags.ENEMY_COMBO_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_8_1_SUB_LEVEL] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 292,
    original_region=SuperMarioBrosAPRegions.WSQ_8_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_8_1_SUB_LEVEL_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 293,
    original_region=SuperMarioBrosAPRegions.WSQ_8_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_8_1_SUB_LEVEL_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 294,
    original_region=SuperMarioBrosAPRegions.WSQ_8_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_8_1_SUB_LEVEL_20_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 295,
    original_region=SuperMarioBrosAPRegions.WSQ_8_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_8_1_SUB_LEVEL_COIN_TARGET_27] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 296,
    original_region=SuperMarioBrosAPRegions.WSQ_8_1,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 3),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_8_1_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 297,
    original_region=SuperMarioBrosAPRegions.WSQ_8_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_8_1_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 298,
    original_region=SuperMarioBrosAPRegions.WSQ_8_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_8_1_20_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 299,
    original_region=SuperMarioBrosAPRegions.WSQ_8_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_8_1_COIN_TARGET_26] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 300,
    original_region=SuperMarioBrosAPRegions.WSQ_8_1,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 3),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_8_1_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 301,
    original_region=SuperMarioBrosAPRegions.WSQ_8_1,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_8_1_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 302,
    original_region=SuperMarioBrosAPRegions.WSQ_8_1,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_1_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_8_2_HIDDEN_1_UP] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 303,
    original_region=SuperMarioBrosAPRegions.WSQ_8_2,
    tags=(
        SuperMarioBrosAPTags.HIDDEN_1_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_8_2_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 304,
    original_region=SuperMarioBrosAPRegions.WSQ_8_2,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_8_2_1_ENEMY_COMBO] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 305,
    original_region=SuperMarioBrosAPRegions.WSQ_8_2,
    tags=(
        SuperMarioBrosAPTags.ENEMY_COMBO_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_8_2_SUB_LEVEL] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 306,
    original_region=SuperMarioBrosAPRegions.WSQ_8_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_8_2_SUB_LEVEL_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 307,
    original_region=SuperMarioBrosAPRegions.WSQ_8_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_8_2_SUB_LEVEL_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 308,
    original_region=SuperMarioBrosAPRegions.WSQ_8_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_8_2_SUB_LEVEL_COIN_TARGET_20] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 309,
    original_region=SuperMarioBrosAPRegions.WSQ_8_2,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_8_2_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 310,
    original_region=SuperMarioBrosAPRegions.WSQ_8_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_8_2_10_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 311,
    original_region=SuperMarioBrosAPRegions.WSQ_8_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_8_2_COIN_TARGET_12] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 312,
    original_region=SuperMarioBrosAPRegions.WSQ_8_2,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 2),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_8_2_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 313,
    original_region=SuperMarioBrosAPRegions.WSQ_8_2,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_8_2_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 314,
    original_region=SuperMarioBrosAPRegions.WSQ_8_2,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_2_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_8_3_POWER_UP_1] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 315,
    original_region=SuperMarioBrosAPRegions.WSQ_8_3,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_8_3_POWER_UP_2] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 316,
    original_region=SuperMarioBrosAPRegions.WSQ_8_3,
    tags=(
        SuperMarioBrosAPTags.POWER_UP_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_8_3_1_ENEMY_COMBO] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 317,
    original_region=SuperMarioBrosAPRegions.WSQ_8_3,
    tags=(
        SuperMarioBrosAPTags.ENEMY_COMBO_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_8_3_5_COINS] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 318,
    original_region=SuperMarioBrosAPRegions.WSQ_8_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.MAGIC_MUSHROOM,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_8_3_COIN_TARGET_10] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 319,
    original_region=SuperMarioBrosAPRegions.WSQ_8_3,
    tags=(
        SuperMarioBrosAPTags.COINS_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.MAGIC_MUSHROOM,
        (SuperMarioBrosAPItems.PROGRESSIVE_COIN_TRACKING, 1),
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_8_3_LEVEL_CLEAR] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 320,
    original_region=SuperMarioBrosAPRegions.WSQ_8_3,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.MAGIC_MUSHROOM,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_8_3_TOP_OF_THE_FLAGPOLE] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 321,
    original_region=SuperMarioBrosAPRegions.WSQ_8_3,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_3_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.MAGIC_MUSHROOM,
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_8_4_SUB_LEVEL] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 322,
    original_region=SuperMarioBrosAPRegions.WSQ_8_4,
    tags=(
        SuperMarioBrosAPTags.SUB_LEVEL_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_4_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=None,
)

location_data[SuperMarioBrosAPLocations.WSQ_8_4_DEFEAT_BOWSER] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 323,
    original_region=SuperMarioBrosAPRegions.WSQ_8_4,
    tags=(
        SuperMarioBrosAPTags.LEVEL_CLEAR_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_4_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.SWIM,
        SuperMarioBrosAPItems.RUN,
    ),
)

location_data[SuperMarioBrosAPLocations.WSQ_8_4_KILL_BOWSER] = SuperMarioBrosLocationData(
    archipelago_id=location_offset + 324,
    original_region=SuperMarioBrosAPRegions.WSQ_8_4,
    tags=(
        SuperMarioBrosAPTags.KILL_BOWSER_LOCATION,
        SuperMarioBrosAPTags.WORLD_8_4_LOCATION,
        SuperMarioBrosAPTags.SECOND_QUEST_LOCATION,
    ),
    requirements=(
        SuperMarioBrosAPItems.SWIM,
        SuperMarioBrosAPItems.RUN,
        SuperMarioBrosAPItems.MAGIC_MUSHROOM,
        SuperMarioBrosAPItems.FIRE_FLOWER,
    ),
)

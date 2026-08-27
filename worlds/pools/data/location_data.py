from typing import Dict, NamedTuple, Optional, Tuple

from ..enums import (
    PoolsLevels,
    PoolsLocations,
    PoolsTags,
)


class PoolsLocationData(NamedTuple):
    archipelago_id: Optional[int]
    region: str
    tags: Optional[Tuple[PoolsTags, ...]] = None


location_offset: int = 10000

location_data: Dict[PoolsLocations, PoolsLocationData] = {
    PoolsLocations.LEVEL_1_CHAIR_1: PoolsLocationData(
        archipelago_id=location_offset + 1,
        region=PoolsLevels.LEVEL_1,
        tags=(
            PoolsTags.LEVEL_1_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_1_POOL_1: PoolsLocationData(
        archipelago_id=location_offset + 2,
        region=PoolsLevels.LEVEL_1,
        tags=(
            PoolsTags.LEVEL_1_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_1_POOL_2: PoolsLocationData(
        archipelago_id=location_offset + 3,
        region=PoolsLevels.LEVEL_1,
        tags=(
            PoolsTags.LEVEL_1_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_1_POOL_3: PoolsLocationData(
        archipelago_id=location_offset + 4,
        region=PoolsLevels.LEVEL_1,
        tags=(
            PoolsTags.LEVEL_1_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_1_POOL_4: PoolsLocationData(
        archipelago_id=location_offset + 5,
        region=PoolsLevels.LEVEL_1,
        tags=(
            PoolsTags.LEVEL_1_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_1_POOL_5: PoolsLocationData(
        archipelago_id=location_offset + 6,
        region=PoolsLevels.LEVEL_1,
        tags=(
            PoolsTags.LEVEL_1_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_1_PROGRESS_1: PoolsLocationData(
        archipelago_id=location_offset + 7,
        region=PoolsLevels.LEVEL_1,
        tags=(
            PoolsTags.LEVEL_1_LOCATION,
            PoolsTags.PROGRESS_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_1_CHAIR_2: PoolsLocationData(
        archipelago_id=location_offset + 8,
        region=PoolsLevels.LEVEL_1,
        tags=(
            PoolsTags.LEVEL_1_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_1_PROGRESS_2: PoolsLocationData(
        archipelago_id=location_offset + 9,
        region=PoolsLevels.LEVEL_1,
        tags=(
            PoolsTags.LEVEL_1_LOCATION,
            PoolsTags.PROGRESS_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_1_POOL_6: PoolsLocationData(
        archipelago_id=location_offset + 10,
        region=PoolsLevels.LEVEL_1,
        tags=(
            PoolsTags.LEVEL_1_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_1_POOL_7: PoolsLocationData(
        archipelago_id=location_offset + 11,
        region=PoolsLevels.LEVEL_1,
        tags=(
            PoolsTags.LEVEL_1_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_1_POOL_8: PoolsLocationData(
        archipelago_id=location_offset + 12,
        region=PoolsLevels.LEVEL_1,
        tags=(
            PoolsTags.LEVEL_1_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_1_CHAIR_3: PoolsLocationData(
        archipelago_id=location_offset + 13,
        region=PoolsLevels.LEVEL_1,
        tags=(
            PoolsTags.LEVEL_1_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_1_BOARD_1: PoolsLocationData(
        archipelago_id=location_offset + 14,
        region=PoolsLevels.LEVEL_1,
        tags=(
            PoolsTags.LEVEL_1_LOCATION,
            PoolsTags.BOARD_LOCATION,
            PoolsTags.SPECIAL_HANDLING,
            PoolsTags.DISCRIMINATOR_HANDLING,
        ),
    ),
    PoolsLocations.LEVEL_1_POOL_9: PoolsLocationData(
        archipelago_id=location_offset + 15,
        region=PoolsLevels.LEVEL_1,
        tags=(
            PoolsTags.LEVEL_1_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_1_CHAIR_4: PoolsLocationData(
        archipelago_id=location_offset + 16,
        region=PoolsLevels.LEVEL_1,
        tags=(
            PoolsTags.LEVEL_1_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_1_POOL_10: PoolsLocationData(
        archipelago_id=location_offset + 17,
        region=PoolsLevels.LEVEL_1,
        tags=(
            PoolsTags.LEVEL_1_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_1_POOL_11: PoolsLocationData(
        archipelago_id=location_offset + 18,
        region=PoolsLevels.LEVEL_1,
        tags=(
            PoolsTags.LEVEL_1_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_1_SLIDE_1: PoolsLocationData(
        archipelago_id=location_offset + 19,
        region=PoolsLevels.LEVEL_1,
        tags=(
            PoolsTags.LEVEL_1_LOCATION,
            PoolsTags.SLIDE_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_1_POOL_12: PoolsLocationData(
        archipelago_id=location_offset + 20,
        region=PoolsLevels.LEVEL_1,
        tags=(
            PoolsTags.LEVEL_1_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_1_POOL_13: PoolsLocationData(
        archipelago_id=location_offset + 21,
        region=PoolsLevels.LEVEL_1,
        tags=(
            PoolsTags.LEVEL_1_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_1_PROP_1: PoolsLocationData(
        archipelago_id=location_offset + 22,
        region=PoolsLevels.LEVEL_1,
        tags=(
            PoolsTags.LEVEL_1_LOCATION,
            PoolsTags.PROP_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_1_CHAIR_5: PoolsLocationData(
        archipelago_id=location_offset + 23,
        region=PoolsLevels.LEVEL_1,
        tags=(
            PoolsTags.LEVEL_1_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_1_CHAIR_6: PoolsLocationData(
        archipelago_id=location_offset + 24,
        region=PoolsLevels.LEVEL_1,
        tags=(
            PoolsTags.LEVEL_1_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_1_BOARD_2: PoolsLocationData(
        archipelago_id=location_offset + 25,
        region=PoolsLevels.LEVEL_1,
        tags=(
            PoolsTags.LEVEL_1_LOCATION,
            PoolsTags.BOARD_LOCATION,
            PoolsTags.SPECIAL_HANDLING,
            PoolsTags.DISCRIMINATOR_HANDLING,
        ),
    ),
    PoolsLocations.LEVEL_2_POOL_1: PoolsLocationData(
        archipelago_id=location_offset + 26,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_POOL_2: PoolsLocationData(
        archipelago_id=location_offset + 27,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_POOL_3: PoolsLocationData(
        archipelago_id=location_offset + 28,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_POOL_4: PoolsLocationData(
        archipelago_id=location_offset + 29,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_POOL_5: PoolsLocationData(
        archipelago_id=location_offset + 30,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_POOL_6: PoolsLocationData(
        archipelago_id=location_offset + 31,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_POOL_7: PoolsLocationData(
        archipelago_id=location_offset + 32,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_PROGRESS_1: PoolsLocationData(
        archipelago_id=location_offset + 33,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.PROGRESS_LOCATION,
            PoolsTags.SPECIAL_HANDLING,
        ),
    ),
    PoolsLocations.LEVEL_2_POOL_8: PoolsLocationData(
        archipelago_id=location_offset + 34,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_CHAIR_1: PoolsLocationData(
        archipelago_id=location_offset + 35,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_CHAIR_2: PoolsLocationData(
        archipelago_id=location_offset + 36,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_POOL_9: PoolsLocationData(
        archipelago_id=location_offset + 37,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_PROP_1: PoolsLocationData(
        archipelago_id=location_offset + 38,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.PROP_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_POOL_10: PoolsLocationData(
        archipelago_id=location_offset + 39,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_PROGRESS_2: PoolsLocationData(
        archipelago_id=location_offset + 40,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.PROGRESS_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_PROGRESS_3: PoolsLocationData(
        archipelago_id=location_offset + 41,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.PROGRESS_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_POOL_11: PoolsLocationData(
        archipelago_id=location_offset + 42,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_PROGRESS_4: PoolsLocationData(
        archipelago_id=location_offset + 43,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.PROGRESS_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_POOL_12: PoolsLocationData(
        archipelago_id=location_offset + 44,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_POOL_13: PoolsLocationData(
        archipelago_id=location_offset + 45,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_CHAIR_3: PoolsLocationData(
        archipelago_id=location_offset + 46,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_POOL_14: PoolsLocationData(
        archipelago_id=location_offset + 47,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_POOL_15: PoolsLocationData(
        archipelago_id=location_offset + 48,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_PROGRESS_5: PoolsLocationData(
        archipelago_id=location_offset + 49,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.PROGRESS_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_POOL_16: PoolsLocationData(
        archipelago_id=location_offset + 50,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_POOL_17: PoolsLocationData(
        archipelago_id=location_offset + 51,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_SLIDE_1: PoolsLocationData(
        archipelago_id=location_offset + 52,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.SLIDE_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_POOL_18: PoolsLocationData(
        archipelago_id=location_offset + 53,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_POOL_19: PoolsLocationData(
        archipelago_id=location_offset + 54,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_POOL_20: PoolsLocationData(
        archipelago_id=location_offset + 55,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_POOL_21: PoolsLocationData(
        archipelago_id=location_offset + 56,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_PROGRESS_6: PoolsLocationData(
        archipelago_id=location_offset + 57,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.PROGRESS_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_POOL_22: PoolsLocationData(
        archipelago_id=location_offset + 58,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_POOL_23: PoolsLocationData(
        archipelago_id=location_offset + 59,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_PROGRESS_7: PoolsLocationData(
        archipelago_id=location_offset + 60,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.PROGRESS_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_POOL_24: PoolsLocationData(
        archipelago_id=location_offset + 61,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_PROP_2: PoolsLocationData(
        archipelago_id=location_offset + 62,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.PROP_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_PROGRESS_8: PoolsLocationData(
        archipelago_id=location_offset + 63,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.PROGRESS_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_POOL_25: PoolsLocationData(
        archipelago_id=location_offset + 64,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_PROGRESS_9: PoolsLocationData(
        archipelago_id=location_offset + 65,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.PROGRESS_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_CHAIR_4: PoolsLocationData(
        archipelago_id=location_offset + 66,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_CHAIR_5: PoolsLocationData(
        archipelago_id=location_offset + 67,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_CHAIR_6: PoolsLocationData(
        archipelago_id=location_offset + 68,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_CHAIR_7: PoolsLocationData(
        archipelago_id=location_offset + 69,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_CHAIR_8: PoolsLocationData(
        archipelago_id=location_offset + 70,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_CHAIR_9: PoolsLocationData(
        archipelago_id=location_offset + 71,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_CHAIR_10: PoolsLocationData(
        archipelago_id=location_offset + 72,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_CHAIR_11: PoolsLocationData(
        archipelago_id=location_offset + 73,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_CHAIR_12: PoolsLocationData(
        archipelago_id=location_offset + 74,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_CHAIR_13: PoolsLocationData(
        archipelago_id=location_offset + 75,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_CHAIR_14: PoolsLocationData(
        archipelago_id=location_offset + 76,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_CHAIR_15: PoolsLocationData(
        archipelago_id=location_offset + 77,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_CHAIR_16: PoolsLocationData(
        archipelago_id=location_offset + 78,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_CHAIR_17: PoolsLocationData(
        archipelago_id=location_offset + 79,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_CHAIR_18: PoolsLocationData(
        archipelago_id=location_offset + 80,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_CHAIR_19: PoolsLocationData(
        archipelago_id=location_offset + 81,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_PROP_3: PoolsLocationData(
        archipelago_id=location_offset + 82,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.PROP_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_CHAIR_20: PoolsLocationData(
        archipelago_id=location_offset + 83,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_CHAIR_21: PoolsLocationData(
        archipelago_id=location_offset + 84,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_CHAIR_22: PoolsLocationData(
        archipelago_id=location_offset + 85,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_CHAIR_23: PoolsLocationData(
        archipelago_id=location_offset + 86,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_CHAIR_24: PoolsLocationData(
        archipelago_id=location_offset + 87,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_SLIDE_2: PoolsLocationData(
        archipelago_id=location_offset + 88,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.SLIDE_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_POOL_26: PoolsLocationData(
        archipelago_id=location_offset + 89,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_POOL_27: PoolsLocationData(
        archipelago_id=location_offset + 90,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_2_SLIDE_3: PoolsLocationData(
        archipelago_id=location_offset + 91,
        region=PoolsLevels.LEVEL_2,
        tags=(
            PoolsTags.LEVEL_2_LOCATION,
            PoolsTags.SLIDE_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_3_POOL_1: PoolsLocationData(
        archipelago_id=location_offset + 92,
        region=PoolsLevels.LEVEL_3,
        tags=(
            PoolsTags.LEVEL_3_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_3_POOL_2: PoolsLocationData(
        archipelago_id=location_offset + 93,
        region=PoolsLevels.LEVEL_3,
        tags=(
            PoolsTags.LEVEL_3_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_3_POOL_3: PoolsLocationData(
        archipelago_id=location_offset + 94,
        region=PoolsLevels.LEVEL_3,
        tags=(
            PoolsTags.LEVEL_3_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_3_POOL_4: PoolsLocationData(
        archipelago_id=location_offset + 95,
        region=PoolsLevels.LEVEL_3,
        tags=(
            PoolsTags.LEVEL_3_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_3_POOL_5: PoolsLocationData(
        archipelago_id=location_offset + 96,
        region=PoolsLevels.LEVEL_3,
        tags=(
            PoolsTags.LEVEL_3_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_3_POOL_6: PoolsLocationData(
        archipelago_id=location_offset + 97,
        region=PoolsLevels.LEVEL_3,
        tags=(
            PoolsTags.LEVEL_3_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_3_CHAIR_1: PoolsLocationData(
        archipelago_id=location_offset + 98,
        region=PoolsLevels.LEVEL_3,
        tags=(
            PoolsTags.LEVEL_3_LOCATION,
            PoolsTags.CHAIR_LOCATION,
            PoolsTags.SPECIAL_HANDLING,
        ),
    ),
    PoolsLocations.LEVEL_3_CHAIR_2: PoolsLocationData(
        archipelago_id=location_offset + 99,
        region=PoolsLevels.LEVEL_3,
        tags=(
            PoolsTags.LEVEL_3_LOCATION,
            PoolsTags.CHAIR_LOCATION,
            PoolsTags.SPECIAL_HANDLING,
        ),
    ),
    PoolsLocations.LEVEL_3_CHAIR_3: PoolsLocationData(
        archipelago_id=location_offset + 100,
        region=PoolsLevels.LEVEL_3,
        tags=(
            PoolsTags.LEVEL_3_LOCATION,
            PoolsTags.CHAIR_LOCATION,
            PoolsTags.SPECIAL_HANDLING,
        ),
    ),
    PoolsLocations.LEVEL_3_CHAIR_4: PoolsLocationData(
        archipelago_id=location_offset + 101,
        region=PoolsLevels.LEVEL_3,
        tags=(
            PoolsTags.LEVEL_3_LOCATION,
            PoolsTags.CHAIR_LOCATION,
            PoolsTags.SPECIAL_HANDLING,
        ),
    ),
    PoolsLocations.LEVEL_3_CHAIR_5: PoolsLocationData(
        archipelago_id=location_offset + 102,
        region=PoolsLevels.LEVEL_3,
        tags=(
            PoolsTags.LEVEL_3_LOCATION,
            PoolsTags.CHAIR_LOCATION,
            PoolsTags.SPECIAL_HANDLING,
        ),
    ),
    PoolsLocations.LEVEL_3_PROP_1: PoolsLocationData(
        archipelago_id=location_offset + 103,
        region=PoolsLevels.LEVEL_3,
        tags=(
            PoolsTags.LEVEL_3_LOCATION,
            PoolsTags.PROP_LOCATION,
            PoolsTags.SPECIAL_HANDLING,
            PoolsTags.DISCRIMINATOR_HANDLING,
        ),
    ),
    PoolsLocations.LEVEL_3_POOL_7: PoolsLocationData(
        archipelago_id=location_offset + 104,
        region=PoolsLevels.LEVEL_3,
        tags=(
            PoolsTags.LEVEL_3_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_3_POOL_8: PoolsLocationData(
        archipelago_id=location_offset + 105,
        region=PoolsLevels.LEVEL_3,
        tags=(
            PoolsTags.LEVEL_3_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_3_SLIDE_1: PoolsLocationData(
        archipelago_id=location_offset + 106,
        region=PoolsLevels.LEVEL_3,
        tags=(
            PoolsTags.LEVEL_3_LOCATION,
            PoolsTags.SLIDE_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_3_POOL_9: PoolsLocationData(
        archipelago_id=location_offset + 107,
        region=PoolsLevels.LEVEL_3,
        tags=(
            PoolsTags.LEVEL_3_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_3_SLIDE_2: PoolsLocationData(
        archipelago_id=location_offset + 108,
        region=PoolsLevels.LEVEL_3,
        tags=(
            PoolsTags.LEVEL_3_LOCATION,
            PoolsTags.SLIDE_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_3_POOL_10: PoolsLocationData(
        archipelago_id=location_offset + 109,
        region=PoolsLevels.LEVEL_3,
        tags=(
            PoolsTags.LEVEL_3_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_3_CHAIR_6: PoolsLocationData(
        archipelago_id=location_offset + 110,
        region=PoolsLevels.LEVEL_3,
        tags=(
            PoolsTags.LEVEL_3_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_3_PROP_2: PoolsLocationData(
        archipelago_id=location_offset + 111,
        region=PoolsLevels.LEVEL_3,
        tags=(
            PoolsTags.LEVEL_3_LOCATION,
            PoolsTags.PROP_LOCATION,
            PoolsTags.SPECIAL_HANDLING,
            PoolsTags.DISCRIMINATOR_HANDLING,
        ),
    ),
    PoolsLocations.LEVEL_3_SLIDE_3: PoolsLocationData(
        archipelago_id=location_offset + 112,
        region=PoolsLevels.LEVEL_3,
        tags=(
            PoolsTags.LEVEL_3_LOCATION,
            PoolsTags.SLIDE_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_3_POOL_11: PoolsLocationData(
        archipelago_id=location_offset + 113,
        region=PoolsLevels.LEVEL_3,
        tags=(
            PoolsTags.LEVEL_3_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_3_CHAIR_7: PoolsLocationData(
        archipelago_id=location_offset + 114,
        region=PoolsLevels.LEVEL_3,
        tags=(
            PoolsTags.LEVEL_3_LOCATION,
            PoolsTags.CHAIR_LOCATION,
            PoolsTags.SPECIAL_HANDLING,
        ),
    ),
    PoolsLocations.LEVEL_3_CHAIR_8: PoolsLocationData(
        archipelago_id=location_offset + 115,
        region=PoolsLevels.LEVEL_3,
        tags=(
            PoolsTags.LEVEL_3_LOCATION,
            PoolsTags.CHAIR_LOCATION,
            PoolsTags.SPECIAL_HANDLING,
        ),
    ),
    PoolsLocations.LEVEL_3_CHAIR_9: PoolsLocationData(
        archipelago_id=location_offset + 116,
        region=PoolsLevels.LEVEL_3,
        tags=(
            PoolsTags.LEVEL_3_LOCATION,
            PoolsTags.CHAIR_LOCATION,
            PoolsTags.SPECIAL_HANDLING,
        ),
    ),
    PoolsLocations.LEVEL_3_POOL_12: PoolsLocationData(
        archipelago_id=location_offset + 117,
        region=PoolsLevels.LEVEL_3,
        tags=(
            PoolsTags.LEVEL_3_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_3_POOL_13: PoolsLocationData(
        archipelago_id=location_offset + 118,
        region=PoolsLevels.LEVEL_3,
        tags=(
            PoolsTags.LEVEL_3_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_3_PROP_3: PoolsLocationData(
        archipelago_id=location_offset + 119,
        region=PoolsLevels.LEVEL_3,
        tags=(
            PoolsTags.LEVEL_3_LOCATION,
            PoolsTags.PROP_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_3_PROP_4: PoolsLocationData(
        archipelago_id=location_offset + 120,
        region=PoolsLevels.LEVEL_3,
        tags=(
            PoolsTags.LEVEL_3_LOCATION,
            PoolsTags.PROP_LOCATION,
            PoolsTags.SPECIAL_HANDLING,
            PoolsTags.DISCRIMINATOR_HANDLING,
        ),
    ),
    PoolsLocations.LEVEL_3_SLIDE_4: PoolsLocationData(
        archipelago_id=location_offset + 121,
        region=PoolsLevels.LEVEL_3,
        tags=(
            PoolsTags.LEVEL_3_LOCATION,
            PoolsTags.SLIDE_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_3_PROP_5: PoolsLocationData(
        archipelago_id=location_offset + 122,
        region=PoolsLevels.LEVEL_3,
        tags=(
            PoolsTags.LEVEL_3_LOCATION,
            PoolsTags.PROP_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_3_POOL_14: PoolsLocationData(
        archipelago_id=location_offset + 123,
        region=PoolsLevels.LEVEL_3,
        tags=(
            PoolsTags.LEVEL_3_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_3_POOL_15: PoolsLocationData(
        archipelago_id=location_offset + 124,
        region=PoolsLevels.LEVEL_3,
        tags=(
            PoolsTags.LEVEL_3_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_3_POOL_16: PoolsLocationData(
        archipelago_id=location_offset + 125,
        region=PoolsLevels.LEVEL_3,
        tags=(
            PoolsTags.LEVEL_3_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_3_CHAIR_10: PoolsLocationData(
        archipelago_id=location_offset + 126,
        region=PoolsLevels.LEVEL_3,
        tags=(
            PoolsTags.LEVEL_3_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_4_POOL_1: PoolsLocationData(
        archipelago_id=location_offset + 127,
        region=PoolsLevels.LEVEL_4,
        tags=(
            PoolsTags.LEVEL_4_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_4_PROGRESS_1: PoolsLocationData(
        archipelago_id=location_offset + 128,
        region=PoolsLevels.LEVEL_4,
        tags=(
            PoolsTags.LEVEL_4_LOCATION,
            PoolsTags.PROGRESS_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_4_POOL_2: PoolsLocationData(
        archipelago_id=location_offset + 129,
        region=PoolsLevels.LEVEL_4,
        tags=(
            PoolsTags.LEVEL_4_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_4_PROP_1: PoolsLocationData(
        archipelago_id=location_offset + 130,
        region=PoolsLevels.LEVEL_4,
        tags=(
            PoolsTags.LEVEL_4_LOCATION,
            PoolsTags.PROP_LOCATION,
            PoolsTags.SPECIAL_HANDLING,
            PoolsTags.DISCRIMINATOR_HANDLING,
        ),
    ),
    PoolsLocations.LEVEL_4_PROGRESS_2: PoolsLocationData(
        archipelago_id=location_offset + 131,
        region=PoolsLevels.LEVEL_4,
        tags=(
            PoolsTags.LEVEL_4_LOCATION,
            PoolsTags.PROGRESS_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_4_POOL_3: PoolsLocationData(
        archipelago_id=location_offset + 132,
        region=PoolsLevels.LEVEL_4,
        tags=(
            PoolsTags.LEVEL_4_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_4_POOL_4: PoolsLocationData(
        archipelago_id=location_offset + 133,
        region=PoolsLevels.LEVEL_4,
        tags=(
            PoolsTags.LEVEL_4_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_4_PROP_2: PoolsLocationData(
        archipelago_id=location_offset + 134,
        region=PoolsLevels.LEVEL_4,
        tags=(
            PoolsTags.LEVEL_4_LOCATION,
            PoolsTags.PROP_LOCATION,
            PoolsTags.SPECIAL_HANDLING,
            PoolsTags.DISCRIMINATOR_HANDLING,
        ),
    ),
    PoolsLocations.LEVEL_4_POOL_5: PoolsLocationData(
        archipelago_id=location_offset + 135,
        region=PoolsLevels.LEVEL_4,
        tags=(
            PoolsTags.LEVEL_4_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_4_SLIDE_1: PoolsLocationData(
        archipelago_id=location_offset + 136,
        region=PoolsLevels.LEVEL_4,
        tags=(
            PoolsTags.LEVEL_4_LOCATION,
            PoolsTags.SLIDE_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_4_POOL_6: PoolsLocationData(
        archipelago_id=location_offset + 137,
        region=PoolsLevels.LEVEL_4,
        tags=(
            PoolsTags.LEVEL_4_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_4_POOL_7: PoolsLocationData(
        archipelago_id=location_offset + 138,
        region=PoolsLevels.LEVEL_4,
        tags=(
            PoolsTags.LEVEL_4_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_4_POOL_8: PoolsLocationData(
        archipelago_id=location_offset + 139,
        region=PoolsLevels.LEVEL_4,
        tags=(
            PoolsTags.LEVEL_4_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_4_PROP_3: PoolsLocationData(
        archipelago_id=location_offset + 140,
        region=PoolsLevels.LEVEL_4,
        tags=(
            PoolsTags.LEVEL_4_LOCATION,
            PoolsTags.PROP_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_4_POOL_9: PoolsLocationData(
        archipelago_id=location_offset + 141,
        region=PoolsLevels.LEVEL_4,
        tags=(
            PoolsTags.LEVEL_4_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_4_PROGRESS_3: PoolsLocationData(
        archipelago_id=location_offset + 142,
        region=PoolsLevels.LEVEL_4,
        tags=(
            PoolsTags.LEVEL_4_LOCATION,
            PoolsTags.PROGRESS_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_4_SLIDE_2: PoolsLocationData(
        archipelago_id=location_offset + 143,
        region=PoolsLevels.LEVEL_4,
        tags=(
            PoolsTags.LEVEL_4_LOCATION,
            PoolsTags.SLIDE_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_4_BOARD_1: PoolsLocationData(
        archipelago_id=location_offset + 144,
        region=PoolsLevels.LEVEL_4,
        tags=(
            PoolsTags.LEVEL_4_LOCATION,
            PoolsTags.BOARD_LOCATION,
            PoolsTags.SPECIAL_HANDLING,
        ),
    ),
    PoolsLocations.LEVEL_4_SLIDE_3: PoolsLocationData(
        archipelago_id=location_offset + 145,
        region=PoolsLevels.LEVEL_4,
        tags=(
            PoolsTags.LEVEL_4_LOCATION,
            PoolsTags.SLIDE_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_4_PROP_4: PoolsLocationData(
        archipelago_id=location_offset + 146,
        region=PoolsLevels.LEVEL_4,
        tags=(
            PoolsTags.LEVEL_4_LOCATION,
            PoolsTags.PROP_LOCATION,
            PoolsTags.SPECIAL_HANDLING,
            PoolsTags.DISCRIMINATOR_HANDLING,
        ),
    ),
    PoolsLocations.LEVEL_4_POOL_10: PoolsLocationData(
        archipelago_id=location_offset + 147,
        region=PoolsLevels.LEVEL_4,
        tags=(
            PoolsTags.LEVEL_4_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_4_POOL_11: PoolsLocationData(
        archipelago_id=location_offset + 148,
        region=PoolsLevels.LEVEL_4,
        tags=(
            PoolsTags.LEVEL_4_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_4_POOL_12: PoolsLocationData(
        archipelago_id=location_offset + 149,
        region=PoolsLevels.LEVEL_4,
        tags=(
            PoolsTags.LEVEL_4_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_4_POOL_13: PoolsLocationData(
        archipelago_id=location_offset + 150,
        region=PoolsLevels.LEVEL_4,
        tags=(
            PoolsTags.LEVEL_4_LOCATION,
            PoolsTags.POOL_LOCATION,
            PoolsTags.SPECIAL_HANDLING,
            PoolsTags.DISCRIMINATOR_HANDLING,
        ),
    ),
    PoolsLocations.LEVEL_4_POOL_14: PoolsLocationData(
        archipelago_id=location_offset + 151,
        region=PoolsLevels.LEVEL_4,
        tags=(
            PoolsTags.LEVEL_4_LOCATION,
            PoolsTags.POOL_LOCATION,
            PoolsTags.SPECIAL_HANDLING,
            PoolsTags.DISCRIMINATOR_HANDLING,
        ),
    ),
    PoolsLocations.LEVEL_4_POOL_15: PoolsLocationData(
        archipelago_id=location_offset + 152,
        region=PoolsLevels.LEVEL_4,
        tags=(
            PoolsTags.LEVEL_4_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_4_PROP_5: PoolsLocationData(
        archipelago_id=location_offset + 153,
        region=PoolsLevels.LEVEL_4,
        tags=(
            PoolsTags.LEVEL_4_LOCATION,
            PoolsTags.PROP_LOCATION,
            PoolsTags.SPECIAL_HANDLING,
            PoolsTags.DISCRIMINATOR_HANDLING,
        ),
    ),
    PoolsLocations.LEVEL_4_POOL_16: PoolsLocationData(
        archipelago_id=location_offset + 154,
        region=PoolsLevels.LEVEL_4,
        tags=(
            PoolsTags.LEVEL_4_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_4_PROGRESS_4: PoolsLocationData(
        archipelago_id=location_offset + 155,
        region=PoolsLevels.LEVEL_4,
        tags=(
            PoolsTags.LEVEL_4_LOCATION,
            PoolsTags.PROGRESS_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_4_POOL_17: PoolsLocationData(
        archipelago_id=location_offset + 156,
        region=PoolsLevels.LEVEL_4,
        tags=(
            PoolsTags.LEVEL_4_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_4_POOL_18: PoolsLocationData(
        archipelago_id=location_offset + 157,
        region=PoolsLevels.LEVEL_4,
        tags=(
            PoolsTags.LEVEL_4_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_4_PROP_6: PoolsLocationData(
        archipelago_id=location_offset + 158,
        region=PoolsLevels.LEVEL_4,
        tags=(
            PoolsTags.LEVEL_4_LOCATION,
            PoolsTags.PROP_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_4_SLIDE_4: PoolsLocationData(
        archipelago_id=location_offset + 159,
        region=PoolsLevels.LEVEL_4,
        tags=(
            PoolsTags.LEVEL_4_LOCATION,
            PoolsTags.SLIDE_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_5_POOL_1: PoolsLocationData(
        archipelago_id=location_offset + 160,
        region=PoolsLevels.LEVEL_5,
        tags=(
            PoolsTags.LEVEL_5_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_5_PROP_1: PoolsLocationData(
        archipelago_id=location_offset + 161,
        region=PoolsLevels.LEVEL_5,
        tags=(
            PoolsTags.LEVEL_5_LOCATION,
            PoolsTags.PROP_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_5_PROP_2: PoolsLocationData(
        archipelago_id=location_offset + 162,
        region=PoolsLevels.LEVEL_5,
        tags=(
            PoolsTags.LEVEL_5_LOCATION,
            PoolsTags.PROP_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_5_POOL_2: PoolsLocationData(
        archipelago_id=location_offset + 163,
        region=PoolsLevels.LEVEL_5,
        tags=(
            PoolsTags.LEVEL_5_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_5_POOL_3: PoolsLocationData(
        archipelago_id=location_offset + 164,
        region=PoolsLevels.LEVEL_5,
        tags=(
            PoolsTags.LEVEL_5_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_5_SLIDE_1: PoolsLocationData(
        archipelago_id=location_offset + 165,
        region=PoolsLevels.LEVEL_5,
        tags=(
            PoolsTags.LEVEL_5_LOCATION,
            PoolsTags.SLIDE_LOCATION,
            PoolsTags.SPECIAL_HANDLING,
            PoolsTags.DISCRIMINATOR_HANDLING,
        ),
    ),
    PoolsLocations.LEVEL_5_SLIDE_2: PoolsLocationData(
        archipelago_id=location_offset + 166,
        region=PoolsLevels.LEVEL_5,
        tags=(
            PoolsTags.LEVEL_5_LOCATION,
            PoolsTags.SLIDE_LOCATION,
            PoolsTags.SPECIAL_HANDLING,
            PoolsTags.DISCRIMINATOR_HANDLING,
        ),
    ),
    PoolsLocations.LEVEL_5_SLIDE_3: PoolsLocationData(
        archipelago_id=location_offset + 167,
        region=PoolsLevels.LEVEL_5,
        tags=(
            PoolsTags.LEVEL_5_LOCATION,
            PoolsTags.SLIDE_LOCATION,
            PoolsTags.SPECIAL_HANDLING,
            PoolsTags.DISCRIMINATOR_HANDLING,
        ),
    ),
    PoolsLocations.LEVEL_5_POOL_4: PoolsLocationData(
        archipelago_id=location_offset + 168,
        region=PoolsLevels.LEVEL_5,
        tags=(
            PoolsTags.LEVEL_5_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_5_CHAIR_1: PoolsLocationData(
        archipelago_id=location_offset + 169,
        region=PoolsLevels.LEVEL_5,
        tags=(
            PoolsTags.LEVEL_5_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_5_POOL_5: PoolsLocationData(
        archipelago_id=location_offset + 170,
        region=PoolsLevels.LEVEL_5,
        tags=(
            PoolsTags.LEVEL_5_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_5_BOARD_1: PoolsLocationData(
        archipelago_id=location_offset + 171,
        region=PoolsLevels.LEVEL_5,
        tags=(
            PoolsTags.LEVEL_5_LOCATION,
            PoolsTags.BOARD_LOCATION,
            PoolsTags.SPECIAL_HANDLING,
            PoolsTags.DISCRIMINATOR_HANDLING,
        ),
    ),
    PoolsLocations.LEVEL_5_BOARD_2: PoolsLocationData(
        archipelago_id=location_offset + 172,
        region=PoolsLevels.LEVEL_5,
        tags=(
            PoolsTags.LEVEL_5_LOCATION,
            PoolsTags.BOARD_LOCATION,
            PoolsTags.SPECIAL_HANDLING,
            PoolsTags.DISCRIMINATOR_HANDLING,
        ),
    ),
    PoolsLocations.LEVEL_5_POOL_6: PoolsLocationData(
        archipelago_id=location_offset + 173,
        region=PoolsLevels.LEVEL_5,
        tags=(
            PoolsTags.LEVEL_5_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_5_PROP_3: PoolsLocationData(
        archipelago_id=location_offset + 174,
        region=PoolsLevels.LEVEL_5,
        tags=(
            PoolsTags.LEVEL_5_LOCATION,
            PoolsTags.PROP_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_5_POOL_7: PoolsLocationData(
        archipelago_id=location_offset + 175,
        region=PoolsLevels.LEVEL_5,
        tags=(
            PoolsTags.LEVEL_5_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_5_POOL_8: PoolsLocationData(
        archipelago_id=location_offset + 176,
        region=PoolsLevels.LEVEL_5,
        tags=(
            PoolsTags.LEVEL_5_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_5_PROGRESS_1: PoolsLocationData(
        archipelago_id=location_offset + 177,
        region=PoolsLevels.LEVEL_5,
        tags=(
            PoolsTags.LEVEL_5_LOCATION,
            PoolsTags.PROGRESS_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_5_POOL_9: PoolsLocationData(
        archipelago_id=location_offset + 178,
        region=PoolsLevels.LEVEL_5,
        tags=(
            PoolsTags.LEVEL_5_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_5_SLIDE_4: PoolsLocationData(
        archipelago_id=location_offset + 179,
        region=PoolsLevels.LEVEL_5,
        tags=(
            PoolsTags.LEVEL_5_LOCATION,
            PoolsTags.SLIDE_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_5_POOL_10: PoolsLocationData(
        archipelago_id=location_offset + 180,
        region=PoolsLevels.LEVEL_5,
        tags=(
            PoolsTags.LEVEL_5_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_5_POOL_11: PoolsLocationData(
        archipelago_id=location_offset + 181,
        region=PoolsLevels.LEVEL_5,
        tags=(
            PoolsTags.LEVEL_5_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_5_PROP_4: PoolsLocationData(
        archipelago_id=location_offset + 182,
        region=PoolsLevels.LEVEL_5,
        tags=(
            PoolsTags.LEVEL_5_LOCATION,
            PoolsTags.PROP_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_5_POOL_12: PoolsLocationData(
        archipelago_id=location_offset + 183,
        region=PoolsLevels.LEVEL_5,
        tags=(
            PoolsTags.LEVEL_5_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_5_SLIDE_5: PoolsLocationData(
        archipelago_id=location_offset + 184,
        region=PoolsLevels.LEVEL_5,
        tags=(
            PoolsTags.LEVEL_5_LOCATION,
            PoolsTags.SLIDE_LOCATION,
            PoolsTags.SPECIAL_HANDLING,
            PoolsTags.DISCRIMINATOR_HANDLING,
        ),
    ),
    PoolsLocations.LEVEL_5_SLIDE_6: PoolsLocationData(
        archipelago_id=location_offset + 185,
        region=PoolsLevels.LEVEL_5,
        tags=(
            PoolsTags.LEVEL_5_LOCATION,
            PoolsTags.SLIDE_LOCATION,
            PoolsTags.SPECIAL_HANDLING,
            PoolsTags.DISCRIMINATOR_HANDLING,
        ),
    ),
    PoolsLocations.LEVEL_5_SLIDE_7: PoolsLocationData(
        archipelago_id=location_offset + 186,
        region=PoolsLevels.LEVEL_5,
        tags=(
            PoolsTags.LEVEL_5_LOCATION,
            PoolsTags.SLIDE_LOCATION,
            PoolsTags.SPECIAL_HANDLING,
            PoolsTags.DISCRIMINATOR_HANDLING,
        ),
    ),
    PoolsLocations.LEVEL_5_SLIDE_8: PoolsLocationData(
        archipelago_id=location_offset + 187,
        region=PoolsLevels.LEVEL_5,
        tags=(
            PoolsTags.LEVEL_5_LOCATION,
            PoolsTags.SLIDE_LOCATION,
            PoolsTags.SPECIAL_HANDLING,
            PoolsTags.DISCRIMINATOR_HANDLING,
        ),
    ),
    PoolsLocations.LEVEL_5_POOL_13: PoolsLocationData(
        archipelago_id=location_offset + 188,
        region=PoolsLevels.LEVEL_5,
        tags=(
            PoolsTags.LEVEL_5_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_5_CHAIR_2: PoolsLocationData(
        archipelago_id=location_offset + 189,
        region=PoolsLevels.LEVEL_5,
        tags=(
            PoolsTags.LEVEL_5_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_5_POOL_14: PoolsLocationData(
        archipelago_id=location_offset + 190,
        region=PoolsLevels.LEVEL_5,
        tags=(
            PoolsTags.LEVEL_5_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_5_POOL_15: PoolsLocationData(
        archipelago_id=location_offset + 191,
        region=PoolsLevels.LEVEL_5,
        tags=(
            PoolsTags.LEVEL_5_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_5_SLIDE_9: PoolsLocationData(
        archipelago_id=location_offset + 192,
        region=PoolsLevels.LEVEL_5,
        tags=(
            PoolsTags.LEVEL_5_LOCATION,
            PoolsTags.SLIDE_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_5_POOL_16: PoolsLocationData(
        archipelago_id=location_offset + 193,
        region=PoolsLevels.LEVEL_5,
        tags=(
            PoolsTags.LEVEL_5_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_5_POOL_17: PoolsLocationData(
        archipelago_id=location_offset + 194,
        region=PoolsLevels.LEVEL_5,
        tags=(
            PoolsTags.LEVEL_5_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_5_PROGRESS_2: PoolsLocationData(
        archipelago_id=location_offset + 195,
        region=PoolsLevels.LEVEL_5,
        tags=(
            PoolsTags.LEVEL_5_LOCATION,
            PoolsTags.PROGRESS_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_5_POOL_18: PoolsLocationData(
        archipelago_id=location_offset + 196,
        region=PoolsLevels.LEVEL_5,
        tags=(
            PoolsTags.LEVEL_5_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_5_PROP_5: PoolsLocationData(
        archipelago_id=location_offset + 197,
        region=PoolsLevels.LEVEL_5,
        tags=(
            PoolsTags.LEVEL_5_LOCATION,
            PoolsTags.PROP_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_PROP_1: PoolsLocationData(
        archipelago_id=location_offset + 198,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.PROP_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_PROP_2: PoolsLocationData(
        archipelago_id=location_offset + 199,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.PROP_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_CHAIR_1: PoolsLocationData(
        archipelago_id=location_offset + 200,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_CHAIR_2: PoolsLocationData(
        archipelago_id=location_offset + 201,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_POOL_1: PoolsLocationData(
        archipelago_id=location_offset + 202,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_POOL_2: PoolsLocationData(
        archipelago_id=location_offset + 203,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_POOL_3: PoolsLocationData(
        archipelago_id=location_offset + 204,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_SLIDE_1: PoolsLocationData(
        archipelago_id=location_offset + 205,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.SLIDE_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_POOL_4: PoolsLocationData(
        archipelago_id=location_offset + 206,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_PROGRESS_1: PoolsLocationData(
        archipelago_id=location_offset + 207,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.PROGRESS_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_SLIDE_2: PoolsLocationData(
        archipelago_id=location_offset + 208,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.SLIDE_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_POOL_5: PoolsLocationData(
        archipelago_id=location_offset + 209,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_POOL_6: PoolsLocationData(
        archipelago_id=location_offset + 210,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_POOL_7: PoolsLocationData(
        archipelago_id=location_offset + 211,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_PROP_3: PoolsLocationData(
        archipelago_id=location_offset + 212,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.PROP_LOCATION,
            PoolsTags.SPECIAL_HANDLING,
            PoolsTags.DISCRIMINATOR_HANDLING,
        ),
    ),
    PoolsLocations.LEVEL_6_PROP_4: PoolsLocationData(
        archipelago_id=location_offset + 213,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.PROP_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_POOL_8: PoolsLocationData(
        archipelago_id=location_offset + 214,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_POOL_9: PoolsLocationData(
        archipelago_id=location_offset + 215,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_PROP_5: PoolsLocationData(
        archipelago_id=location_offset + 216,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.PROP_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_POOL_10: PoolsLocationData(
        archipelago_id=location_offset + 217,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_PROGRESS_2: PoolsLocationData(
        archipelago_id=location_offset + 218,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.PROGRESS_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_POOL_11: PoolsLocationData(
        archipelago_id=location_offset + 219,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_POOL_12: PoolsLocationData(
        archipelago_id=location_offset + 220,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_POOL_13: PoolsLocationData(
        archipelago_id=location_offset + 221,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_CHAIR_3: PoolsLocationData(
        archipelago_id=location_offset + 222,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_POOL_14: PoolsLocationData(
        archipelago_id=location_offset + 223,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_POOL_15: PoolsLocationData(
        archipelago_id=location_offset + 224,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_PROP_6: PoolsLocationData(
        archipelago_id=location_offset + 225,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.PROP_LOCATION,
            PoolsTags.SPECIAL_HANDLING,
            PoolsTags.DISCRIMINATOR_HANDLING,
        ),
    ),
    PoolsLocations.LEVEL_6_CHAIR_4: PoolsLocationData(
        archipelago_id=location_offset + 226,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_CHAIR_5: PoolsLocationData(
        archipelago_id=location_offset + 227,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_POOL_16: PoolsLocationData(
        archipelago_id=location_offset + 228,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_POOL_17: PoolsLocationData(
        archipelago_id=location_offset + 229,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_POOL_18: PoolsLocationData(
        archipelago_id=location_offset + 230,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_CHAIR_6: PoolsLocationData(
        archipelago_id=location_offset + 231,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_POOL_19: PoolsLocationData(
        archipelago_id=location_offset + 232,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_CHAIR_7: PoolsLocationData(
        archipelago_id=location_offset + 233,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_CHAIR_8: PoolsLocationData(
        archipelago_id=location_offset + 234,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_CHAIR_9: PoolsLocationData(
        archipelago_id=location_offset + 235,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_PROP_7: PoolsLocationData(
        archipelago_id=location_offset + 236,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.PROP_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_PROGRESS_3: PoolsLocationData(
        archipelago_id=location_offset + 237,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.PROGRESS_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_PROGRESS_4: PoolsLocationData(
        archipelago_id=location_offset + 238,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.PROGRESS_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_POOL_20: PoolsLocationData(
        archipelago_id=location_offset + 239,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.POOL_LOCATION,
            PoolsTags.SPECIAL_HANDLING,
            PoolsTags.DISCRIMINATOR_HANDLING,
        ),
    ),
    PoolsLocations.LEVEL_6_POOL_21: PoolsLocationData(
        archipelago_id=location_offset + 240,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.POOL_LOCATION,
            PoolsTags.SPECIAL_HANDLING,
            PoolsTags.DISCRIMINATOR_HANDLING,
        ),
    ),
    PoolsLocations.LEVEL_6_POOL_22: PoolsLocationData(
        archipelago_id=location_offset + 241,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_CHAIR_10: PoolsLocationData(
        archipelago_id=location_offset + 242,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_PROP_8: PoolsLocationData(
        archipelago_id=location_offset + 243,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.PROP_LOCATION,
            PoolsTags.SPECIAL_HANDLING,
        ),
    ),
    PoolsLocations.LEVEL_6_POOL_23: PoolsLocationData(
        archipelago_id=location_offset + 244,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_CHAIR_11: PoolsLocationData(
        archipelago_id=location_offset + 245,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_CHAIR_12: PoolsLocationData(
        archipelago_id=location_offset + 246,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_CHAIR_13: PoolsLocationData(
        archipelago_id=location_offset + 247,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_CHAIR_14: PoolsLocationData(
        archipelago_id=location_offset + 248,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_CHAIR_15: PoolsLocationData(
        archipelago_id=location_offset + 249,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_POOL_24: PoolsLocationData(
        archipelago_id=location_offset + 250,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_CHAIR_16: PoolsLocationData(
        archipelago_id=location_offset + 251,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_CHAIR_17: PoolsLocationData(
        archipelago_id=location_offset + 252,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_POOL_25: PoolsLocationData(
        archipelago_id=location_offset + 253,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_CHAIR_18: PoolsLocationData(
        archipelago_id=location_offset + 254,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_PROP_9: PoolsLocationData(
        archipelago_id=location_offset + 255,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.PROP_LOCATION,
            PoolsTags.SPECIAL_HANDLING,
        ),
    ),
    PoolsLocations.LEVEL_6_POOL_26: PoolsLocationData(
        archipelago_id=location_offset + 256,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_PROP_10: PoolsLocationData(
        archipelago_id=location_offset + 257,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.PROP_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_6_POOL_27: PoolsLocationData(
        archipelago_id=location_offset + 258,
        region=PoolsLevels.LEVEL_6,
        tags=(
            PoolsTags.LEVEL_6_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_CHAIR_1: PoolsLocationData(
        archipelago_id=location_offset + 259,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_CHAIR_2: PoolsLocationData(
        archipelago_id=location_offset + 260,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_CHAIR_3: PoolsLocationData(
        archipelago_id=location_offset + 261,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_CHAIR_4: PoolsLocationData(
        archipelago_id=location_offset + 262,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_CHAIR_5: PoolsLocationData(
        archipelago_id=location_offset + 263,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_CHAIR_6: PoolsLocationData(
        archipelago_id=location_offset + 264,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_POOL_1: PoolsLocationData(
        archipelago_id=location_offset + 265,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_CHAIR_7: PoolsLocationData(
        archipelago_id=location_offset + 266,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_CHAIR_8: PoolsLocationData(
        archipelago_id=location_offset + 267,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_CHAIR_9: PoolsLocationData(
        archipelago_id=location_offset + 268,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_CHAIR_10: PoolsLocationData(
        archipelago_id=location_offset + 269,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_CHAIR_11: PoolsLocationData(
        archipelago_id=location_offset + 270,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_SLIDE_1: PoolsLocationData(
        archipelago_id=location_offset + 271,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.SLIDE_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_PROGRESS_1: PoolsLocationData(
        archipelago_id=location_offset + 272,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.PROGRESS_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_CHAIR_12: PoolsLocationData(
        archipelago_id=location_offset + 273,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_CHAIR_13: PoolsLocationData(
        archipelago_id=location_offset + 274,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_CHAIR_14: PoolsLocationData(
        archipelago_id=location_offset + 275,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_CHAIR_15: PoolsLocationData(
        archipelago_id=location_offset + 276,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_CHAIR_16: PoolsLocationData(
        archipelago_id=location_offset + 277,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_CHAIR_17: PoolsLocationData(
        archipelago_id=location_offset + 278,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_CHAIR_18: PoolsLocationData(
        archipelago_id=location_offset + 279,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_CHAIR_19: PoolsLocationData(
        archipelago_id=location_offset + 280,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_CHAIR_20: PoolsLocationData(
        archipelago_id=location_offset + 281,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_CHAIR_21: PoolsLocationData(
        archipelago_id=location_offset + 282,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_CHAIR_22: PoolsLocationData(
        archipelago_id=location_offset + 283,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_CHAIR_23: PoolsLocationData(
        archipelago_id=location_offset + 284,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_CHAIR_24: PoolsLocationData(
        archipelago_id=location_offset + 285,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_PROP_1: PoolsLocationData(
        archipelago_id=location_offset + 286,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.PROP_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_CHAIR_25: PoolsLocationData(
        archipelago_id=location_offset + 287,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_CHAIR_26: PoolsLocationData(
        archipelago_id=location_offset + 288,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_CHAIR_27: PoolsLocationData(
        archipelago_id=location_offset + 289,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_CHAIR_28: PoolsLocationData(
        archipelago_id=location_offset + 290,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_CHAIR_29: PoolsLocationData(
        archipelago_id=location_offset + 291,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_CHAIR_30: PoolsLocationData(
        archipelago_id=location_offset + 292,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_CHAIR_31: PoolsLocationData(
        archipelago_id=location_offset + 293,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_PROP_2: PoolsLocationData(
        archipelago_id=location_offset + 294,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.PROP_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_CHAIR_32: PoolsLocationData(
        archipelago_id=location_offset + 295,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_PROP_3: PoolsLocationData(
        archipelago_id=location_offset + 296,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.PROP_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_CHAIR_33: PoolsLocationData(
        archipelago_id=location_offset + 297,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_CHAIR_34: PoolsLocationData(
        archipelago_id=location_offset + 298,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_CHAIR_35: PoolsLocationData(
        archipelago_id=location_offset + 299,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_POOL_2: PoolsLocationData(
        archipelago_id=location_offset + 300,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_POOL_3: PoolsLocationData(
        archipelago_id=location_offset + 301,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_POOL_4: PoolsLocationData(
        archipelago_id=location_offset + 302,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_CHAIR_36: PoolsLocationData(
        archipelago_id=location_offset + 303,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_CHAIR_37: PoolsLocationData(
        archipelago_id=location_offset + 304,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_PROGRESS_2: PoolsLocationData(
        archipelago_id=location_offset + 305,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.PROGRESS_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_PROGRESS_3: PoolsLocationData(
        archipelago_id=location_offset + 306,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.PROGRESS_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_PROP_4: PoolsLocationData(
        archipelago_id=location_offset + 307,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.PROP_LOCATION,
            PoolsTags.SPECIAL_HANDLING,
            PoolsTags.DISCRIMINATOR_HANDLING,
        ),
    ),
    PoolsLocations.LEVEL_0_POOL_5: PoolsLocationData(
        archipelago_id=location_offset + 308,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_POOL_6: PoolsLocationData(
        archipelago_id=location_offset + 309,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_POOL_7: PoolsLocationData(
        archipelago_id=location_offset + 310,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_POOL_8: PoolsLocationData(
        archipelago_id=location_offset + 311,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.POOL_LOCATION,
            PoolsTags.SPECIAL_HANDLING,
            PoolsTags.DISCRIMINATOR_HANDLING,
        ),
    ),
    PoolsLocations.LEVEL_0_POOL_9: PoolsLocationData(
        archipelago_id=location_offset + 312,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_PROGRESS_4: PoolsLocationData(
        archipelago_id=location_offset + 313,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.PROGRESS_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_CHAIR_38: PoolsLocationData(
        archipelago_id=location_offset + 314,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_CHAIR_39: PoolsLocationData(
        archipelago_id=location_offset + 315,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_PROP_5: PoolsLocationData(
        archipelago_id=location_offset + 316,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.PROP_LOCATION,
            PoolsTags.SPECIAL_HANDLING,
        ),
    ),
    PoolsLocations.LEVEL_0_PROGRESS_5: PoolsLocationData(
        archipelago_id=location_offset + 317,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.PROGRESS_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_PROP_6: PoolsLocationData(
        archipelago_id=location_offset + 318,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.PROP_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_PROP_7: PoolsLocationData(
        archipelago_id=location_offset + 319,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.PROP_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_PROP_8: PoolsLocationData(
        archipelago_id=location_offset + 320,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.PROP_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_SLIDE_2: PoolsLocationData(
        archipelago_id=location_offset + 321,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.SLIDE_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_POOL_10: PoolsLocationData(
        archipelago_id=location_offset + 322,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.POOL_LOCATION,
            PoolsTags.SPECIAL_HANDLING,
            PoolsTags.DISCRIMINATOR_HANDLING,
        ),
    ),
    PoolsLocations.LEVEL_0_POOL_11: PoolsLocationData(
        archipelago_id=location_offset + 323,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_CHAIR_40: PoolsLocationData(
        archipelago_id=location_offset + 324,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_PROGRESS_6: PoolsLocationData(
        archipelago_id=location_offset + 325,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.PROGRESS_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_PROP_9: PoolsLocationData(
        archipelago_id=location_offset + 326,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.PROP_LOCATION,
            PoolsTags.SPECIAL_HANDLING,
        ),
    ),
    PoolsLocations.LEVEL_0_PROP_10: PoolsLocationData(
        archipelago_id=location_offset + 327,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.PROP_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_CHAIR_41: PoolsLocationData(
        archipelago_id=location_offset + 328,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_CHAIR_42: PoolsLocationData(
        archipelago_id=location_offset + 329,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_PROP_11: PoolsLocationData(
        archipelago_id=location_offset + 330,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.PROP_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_CHAIR_43: PoolsLocationData(
        archipelago_id=location_offset + 331,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.CHAIR_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_POOL_12: PoolsLocationData(
        archipelago_id=location_offset + 332,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.POOL_LOCATION,
        ),
    ),
    PoolsLocations.LEVEL_0_PROP_12: PoolsLocationData(
        archipelago_id=location_offset + 333,
        region=PoolsLevels.LEVEL_0,
        tags=(
            PoolsTags.LEVEL_0_LOCATION,
            PoolsTags.PROP_LOCATION,
            PoolsTags.SPECIAL_HANDLING,
            PoolsTags.DISCRIMINATOR_HANDLING,
        ),
    ),
}

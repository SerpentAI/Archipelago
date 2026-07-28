from typing import Dict, NamedTuple, Optional, Tuple

from ..enums import SeveredSteelAPTags, SeveredSteelLevels


class SeveredSteelLocationData(NamedTuple):
    archipelago_id: Optional[int]
    region: str
    tags: Optional[Tuple[SeveredSteelAPTags, ...]] = None


location_offset: int = 1000000

location_data: Dict[str, SeveredSteelLocationData] = dict()

i: int
level: SeveredSteelLevels
for i, level in enumerate(SeveredSteelLevels):
    level_offset: int = i * 10000

    location_data[f"{level.value} - Kill 10 Enemies"] = SeveredSteelLocationData(
        archipelago_id=location_offset + level_offset + 1,
        region=f"{level.value}",
        tags=(
            SeveredSteelAPTags.KILL_LOCATION,
            SeveredSteelAPTags.KILL_10_LOCATION,
            getattr(SeveredSteelAPTags, f"{level.name}_LOCATION"),
        ),
    )

    location_data[f"{level.value} - Kill All Enemies"] = SeveredSteelLocationData(
        archipelago_id=location_offset + level_offset + 2,
        region=f"{level.value}",
        tags=(
            SeveredSteelAPTags.KILL_LOCATION,
            SeveredSteelAPTags.KILL_ALL_LOCATION,
            getattr(SeveredSteelAPTags, f"{level.name}_LOCATION"),
        ),
    )

    location_data[f"{level.value} - Kill 7 Enemies with Headshots"] = SeveredSteelLocationData(
        archipelago_id=location_offset + level_offset + 3,
        region=f"{level.value}",
        tags=(
            SeveredSteelAPTags.KILL_LOCATION,
            SeveredSteelAPTags.KILL_7_HEADSHOTS_LOCATION,
            getattr(SeveredSteelAPTags, f"{level.name}_LOCATION"),
        ),
    )

    location_data[f"{level.value} - Obtain a B Rank"] = SeveredSteelLocationData(
        archipelago_id=location_offset + level_offset + 4,
        region=f"{level.value}",
        tags=(
            SeveredSteelAPTags.RANK_LOCATION,
            SeveredSteelAPTags.RANK_B_LOCATION,
            getattr(SeveredSteelAPTags, f"{level.name}_LOCATION"),
        ),
    )

    location_data[f"{level.value} - Obtain an A Rank"] = SeveredSteelLocationData(
        archipelago_id=location_offset + level_offset + 5,
        region=f"{level.value}",
        tags=(
            SeveredSteelAPTags.RANK_LOCATION,
            SeveredSteelAPTags.RANK_A_LOCATION,
            getattr(SeveredSteelAPTags, f"{level.name}_LOCATION"),
        ),
    )

    location_data[f"{level.value} - Obtain an S Rank"] = SeveredSteelLocationData(
        archipelago_id=location_offset + level_offset + 6,
        region=f"{level.value}",
        tags=(
            SeveredSteelAPTags.RANK_LOCATION,
            SeveredSteelAPTags.RANK_S_LOCATION,
            getattr(SeveredSteelAPTags, f"{level.name}_LOCATION"),
        ),
    )

    location_data[f"{level.value} - Obtain an S+ Rank"] = SeveredSteelLocationData(
        archipelago_id=location_offset + level_offset + 7,
        region=f"{level.value}",
        tags=(
            SeveredSteelAPTags.RANK_LOCATION,
            SeveredSteelAPTags.RANK_S_PLUS_LOCATION,
            getattr(SeveredSteelAPTags, f"{level.name}_LOCATION"),
        ),
    )

    location_data[f"{level.value} - Obtain an S++ Rank"] = SeveredSteelLocationData(
        archipelago_id=location_offset + level_offset + 8,
        region=f"{level.value}",
        tags=(
            SeveredSteelAPTags.RANK_LOCATION,
            SeveredSteelAPTags.RANK_S_PLUS_PLUS_LOCATION,
            getattr(SeveredSteelAPTags, f"{level.name}_LOCATION"),
        ),
    )

    location_data[f"{level.value} - Beat the Target Time"] = SeveredSteelLocationData(
        archipelago_id=location_offset + level_offset + 9,
        region=f"{level.value}",
        tags=(
            SeveredSteelAPTags.TARGET_TIME_LOCATION,
            SeveredSteelAPTags.TARGET_TIME_BEAT_LOCATION,
            getattr(SeveredSteelAPTags, f"{level.name}_LOCATION"),
        ),
    )

    location_data[f"{level.value} - Complete 2 Challenges"] = SeveredSteelLocationData(
        archipelago_id=location_offset + level_offset + 10,
        region=f"{level.value}",
        tags=(
            SeveredSteelAPTags.CHALLENGE_LOCATION,
            SeveredSteelAPTags.CHALLENGE_BASE_LOCATION,
            getattr(SeveredSteelAPTags, f"{level.name}_LOCATION"),
        ),
    )

    ii: int
    for ii in range(5):
        location_data[f"{level.value} - Complete Stylish Action Challenge #{ii + 1}"] = SeveredSteelLocationData(
            archipelago_id=location_offset + level_offset + 100 + ii + 1,
            region=f"{level.value}",
            tags=(
                SeveredSteelAPTags.CHALLENGE_LOCATION,
                SeveredSteelAPTags.CHALLENGE_STYLISH_ACTION_LOCATION,
                getattr(SeveredSteelAPTags, f"{level.name}_LOCATION"),
            ),
        )

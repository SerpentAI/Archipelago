from typing import Dict, NamedTuple, Optional, Tuple

from ..enums import DrMarioColors, DrMarioLevels, DrMarioSpeeds, DrMarioTags


class DrMarioLocationData(NamedTuple):
    archipelago_id: Optional[int]
    region: str
    tags: Optional[Tuple[DrMarioTags, ...]] = None


location_offset: int = 1000000

location_data: Dict[str, DrMarioLocationData] = dict()

i: int
level: DrMarioLevels
for i, level in enumerate(DrMarioLevels):
    level_offset: int = i * 10000

    ii: int
    speed: DrMarioSpeeds
    for ii, speed in enumerate((DrMarioSpeeds.LOW, DrMarioSpeeds.MEDIUM, DrMarioSpeeds.HIGH)):
        location_data[f"{level.value} - Clear the Level on {speed.value} Speed"] = DrMarioLocationData(
            archipelago_id=location_offset + level_offset + ii + 1,
            region=level.value,
            tags=(
                DrMarioTags.LEVEL_CLEAR_LOCATION,
                getattr(DrMarioTags, f"LEVEL_CLEAR_{speed.name}_SPEED_LOCATION"),
                getattr(DrMarioTags, f"{level.name}_LOCATION"),
            ),
        )

    location_data[f"{level.value} - Eliminate a Quarter of the Viruses"] = DrMarioLocationData(
        archipelago_id=location_offset + level_offset + 11,
        region=level.value,
        tags=(
            DrMarioTags.VIRUS_ELIMINATION_LOCATION,
            DrMarioTags.VIRUS_ELIMINATION_QUARTER_LOCATION,
            getattr(DrMarioTags, f"{level.name}_LOCATION"),
        ),
    )

    location_data[f"{level.value} - Eliminate Half of the Viruses"] = DrMarioLocationData(
        archipelago_id=location_offset + level_offset + 12,
        region=level.value,
        tags=(
            DrMarioTags.VIRUS_ELIMINATION_LOCATION,
            DrMarioTags.VIRUS_ELIMINATION_HALF_LOCATION,
            getattr(DrMarioTags, f"{level.name}_LOCATION"),
        ),
    )

    ii: int
    color: DrMarioColors
    for ii, color in enumerate(DrMarioColors):
        location_data[f"{level.value} - Eliminate All {color.value} Viruses"] = DrMarioLocationData(
            archipelago_id=location_offset + level_offset + 21 + ii,
            region=level.value,
            tags=(
                DrMarioTags.COLOR_ELIMINATION_LOCATION,
                getattr(DrMarioTags, f"COLOR_ELIMINATION_{color.name}_LOCATION"),
                getattr(DrMarioTags, f"{level.name}_LOCATION"),
            ),
        )

    ii: int
    for ii in range(1, 4):
        iii: int
        color: DrMarioColors
        for iii, color in enumerate(DrMarioColors):
            location_data[f"{level.value} - Eliminate {ii} {color.value} {'Virus' if ii == 1 else 'Viruses'}"] = DrMarioLocationData(
                archipelago_id=location_offset + level_offset + 70 + (ii - 1) * 3 + iii + 1,
                region=level.value,
                tags=(
                    DrMarioTags.COLOR_VIRUS_COUNT_LOCATION,
                    getattr(DrMarioTags, f"COLOR_VIRUS_COUNT_{ii}_LOCATION"),
                    getattr(DrMarioTags, f"{level.name}_LOCATION"),
                ),
            )

    ii: int
    for ii in range(2, 4):
        location_data[f"{level.value} - Destroy {ii} Viruses with One Pill"] = DrMarioLocationData(
            archipelago_id=location_offset + level_offset + 30 + ii,
            region=level.value,
            tags=(
                DrMarioTags.MULTI_VIRUS_LOCATION,
                getattr(DrMarioTags, f"MULTI_VIRUS_{ii}_LOCATION"),
                getattr(DrMarioTags, f"{level.name}_LOCATION"),
            ),
        )

    ii: int
    for ii in range(2, 4):
        location_data[f"{level.value} - Clear {ii} Lines with One Pill"] = DrMarioLocationData(
            archipelago_id=location_offset + level_offset + 40 + ii,
            region=level.value,
            tags=(
                DrMarioTags.MULTI_LINE_LOCATION,
                getattr(DrMarioTags, f"MULTI_LINE_{ii}_LOCATION"),
                getattr(DrMarioTags, f"{level.name}_LOCATION"),
            ),
        )

    ii: int
    color: DrMarioColors
    for ii, color in enumerate(DrMarioColors):
        location_data[f"{level.value} - Clear 2 {color.value} Lines with One Pill"] = DrMarioLocationData(
            archipelago_id=location_offset + level_offset + 51 + ii,
            region=level.value,
            tags=(
                DrMarioTags.COLOR_LINE_LOCATION,
                getattr(DrMarioTags, f"COLOR_LINE_{color.name}_LOCATION"),
                getattr(DrMarioTags, f"{level.name}_LOCATION"),
            ),
        )

    location_data[f"{level.value} - Trigger a 2-Chain"] = DrMarioLocationData(
        archipelago_id=location_offset + level_offset + 62,
        region=level.value,
        tags=(
            DrMarioTags.CHAIN_LOCATION,
            DrMarioTags.CHAIN_2_LOCATION,
            getattr(DrMarioTags, f"{level.name}_LOCATION"),
        ),
    )

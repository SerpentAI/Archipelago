from typing import Dict, NamedTuple, Optional, Tuple

from ..enums import PinballFXTables, PinballFXAPTags


class PinballFXLocationData(NamedTuple):
    archipelago_id: Optional[int]
    region: PinballFXTables
    tags: Optional[Tuple[PinballFXAPTags, ...]] = None


location_offset: int = 1000000

location_data: Dict[str, PinballFXLocationData] = dict()

i: int
table: PinballFXTables
for i, table in enumerate(PinballFXTables):
    table_offset: int = 1000 * i

    location_data[f"{table.value} - Classic Mode: Target Score (Low)"] = PinballFXLocationData(
        archipelago_id=location_offset + table_offset + 1,
        region=table,
        tags=(
            PinballFXAPTags.TARGET_SCORE_LOCATION,
            PinballFXAPTags.TARGET_SCORE_LOW_LOCATION,
            PinballFXAPTags.CLASSIC_MODE_LOCATION,
            getattr(PinballFXAPTags, f"{table.name}_LOCATION"),
        ),
    )

    location_data[f"{table.value} - Classic Mode: Target Score (Mid)"] = PinballFXLocationData(
        archipelago_id=location_offset + table_offset + 2,
        region=table,
        tags=(
            PinballFXAPTags.TARGET_SCORE_LOCATION,
            PinballFXAPTags.TARGET_SCORE_MID_LOCATION,
            PinballFXAPTags.CLASSIC_MODE_LOCATION,
            getattr(PinballFXAPTags, f"{table.name}_LOCATION"),
        ),
    )

    location_data[f"{table.value} - Classic Mode: Target Score (High)"] = PinballFXLocationData(
        archipelago_id=location_offset + table_offset + 3,
        region=table,
        tags=(
            PinballFXAPTags.TARGET_SCORE_LOCATION,
            PinballFXAPTags.TARGET_SCORE_HIGH_LOCATION,
            PinballFXAPTags.CLASSIC_MODE_LOCATION,
            getattr(PinballFXAPTags, f"{table.name}_LOCATION"),
        ),
    )

    location_data[f"{table.value} - Classic Mode: Target Score (Very High)"] = PinballFXLocationData(
        archipelago_id=location_offset + table_offset + 4,
        region=table,
        tags=(
            PinballFXAPTags.TARGET_SCORE_LOCATION,
            PinballFXAPTags.TARGET_SCORE_VERY_HIGH_LOCATION,
            PinballFXAPTags.CLASSIC_MODE_LOCATION,
            getattr(PinballFXAPTags, f"{table.name}_LOCATION"),
        ),
    )

    location_data[f"{table.value} - 1 Ball Challenge: Target Score (Low)"] = PinballFXLocationData(
        archipelago_id=location_offset + table_offset + 5,
        region=table,
        tags=(
            PinballFXAPTags.TARGET_SCORE_LOCATION,
            PinballFXAPTags.TARGET_SCORE_LOW_LOCATION,
            PinballFXAPTags.ONE_BALL_CHALLENGE_LOCATION,
            getattr(PinballFXAPTags, f"{table.name}_LOCATION"),
        ),
    )

    location_data[f"{table.value} - 1 Ball Challenge: Target Score (Mid)"] = PinballFXLocationData(
        archipelago_id=location_offset + table_offset + 6,
        region=table,
        tags=(
            PinballFXAPTags.TARGET_SCORE_LOCATION,
            PinballFXAPTags.TARGET_SCORE_MID_LOCATION,
            PinballFXAPTags.ONE_BALL_CHALLENGE_LOCATION,
            getattr(PinballFXAPTags, f"{table.name}_LOCATION"),
        ),
    )

    location_data[f"{table.value} - 1 Ball Challenge: Target Score (High)"] = PinballFXLocationData(
        archipelago_id=location_offset + table_offset + 7,
        region=table,
        tags=(
            PinballFXAPTags.TARGET_SCORE_LOCATION,
            PinballFXAPTags.TARGET_SCORE_HIGH_LOCATION,
            PinballFXAPTags.ONE_BALL_CHALLENGE_LOCATION,
            getattr(PinballFXAPTags, f"{table.name}_LOCATION"),
        ),
    )

    location_data[f"{table.value} - 1 Ball Challenge: Target Score (Very High)"] = PinballFXLocationData(
        archipelago_id=location_offset + table_offset + 8,
        region=table,
        tags=(
            PinballFXAPTags.TARGET_SCORE_LOCATION,
            PinballFXAPTags.TARGET_SCORE_VERY_HIGH_LOCATION,
            PinballFXAPTags.ONE_BALL_CHALLENGE_LOCATION,
            getattr(PinballFXAPTags, f"{table.name}_LOCATION"),
        ),
    )

    location_data[f"{table.value} - Flips Challenge: Target Score (Low)"] = PinballFXLocationData(
        archipelago_id=location_offset + table_offset + 9,
        region=table,
        tags=(
            PinballFXAPTags.TARGET_SCORE_LOCATION,
            PinballFXAPTags.TARGET_SCORE_LOW_LOCATION,
            PinballFXAPTags.FLIPS_CHALLENGE_LOCATION,
            getattr(PinballFXAPTags, f"{table.name}_LOCATION"),
        ),
    )

    location_data[f"{table.value} - Flips Challenge: Target Score (Mid)"] = PinballFXLocationData(
        archipelago_id=location_offset + table_offset + 10,
        region=table,
        tags=(
            PinballFXAPTags.TARGET_SCORE_LOCATION,
            PinballFXAPTags.TARGET_SCORE_MID_LOCATION,
            PinballFXAPTags.FLIPS_CHALLENGE_LOCATION,
            getattr(PinballFXAPTags, f"{table.name}_LOCATION"),
        ),
    )

    location_data[f"{table.value} - Flips Challenge: Target Score (High)"] = PinballFXLocationData(
        archipelago_id=location_offset + table_offset + 11,
        region=table,
        tags=(
            PinballFXAPTags.TARGET_SCORE_LOCATION,
            PinballFXAPTags.TARGET_SCORE_HIGH_LOCATION,
            PinballFXAPTags.FLIPS_CHALLENGE_LOCATION,
            getattr(PinballFXAPTags, f"{table.name}_LOCATION"),
        ),
    )

    location_data[f"{table.value} - Flips Challenge: Target Score (Very High)"] = PinballFXLocationData(
        archipelago_id=location_offset + table_offset + 12,
        region=table,
        tags=(
            PinballFXAPTags.TARGET_SCORE_LOCATION,
            PinballFXAPTags.TARGET_SCORE_VERY_HIGH_LOCATION,
            PinballFXAPTags.FLIPS_CHALLENGE_LOCATION,
            getattr(PinballFXAPTags, f"{table.name}_LOCATION"),
        ),
    )

    location_data[f"{table.value} - Time Challenge: Target Score (Low)"] = PinballFXLocationData(
        archipelago_id=location_offset + table_offset + 13,
        region=table,
        tags=(
            PinballFXAPTags.TARGET_SCORE_LOCATION,
            PinballFXAPTags.TARGET_SCORE_LOW_LOCATION,
            PinballFXAPTags.TIME_CHALLENGE_LOCATION,
            getattr(PinballFXAPTags, f"{table.name}_LOCATION"),
        ),
    )

    location_data[f"{table.value} - Time Challenge: Target Score (Mid)"] = PinballFXLocationData(
        archipelago_id=location_offset + table_offset + 14,
        region=table,
        tags=(
            PinballFXAPTags.TARGET_SCORE_LOCATION,
            PinballFXAPTags.TARGET_SCORE_MID_LOCATION,
            PinballFXAPTags.TIME_CHALLENGE_LOCATION,
            getattr(PinballFXAPTags, f"{table.name}_LOCATION"),
        ),
    )

    location_data[f"{table.value} - Time Challenge: Target Score (High)"] = PinballFXLocationData(
        archipelago_id=location_offset + table_offset + 15,
        region=table,
        tags=(
            PinballFXAPTags.TARGET_SCORE_LOCATION,
            PinballFXAPTags.TARGET_SCORE_HIGH_LOCATION,
            PinballFXAPTags.TIME_CHALLENGE_LOCATION,
            getattr(PinballFXAPTags, f"{table.name}_LOCATION"),
        ),
    )

    location_data[f"{table.value} - Time Challenge: Target Score (Very High)"] = PinballFXLocationData(
        archipelago_id=location_offset + table_offset + 16,
        region=table,
        tags=(
            PinballFXAPTags.TARGET_SCORE_LOCATION,
            PinballFXAPTags.TARGET_SCORE_VERY_HIGH_LOCATION,
            PinballFXAPTags.TIME_CHALLENGE_LOCATION,
            getattr(PinballFXAPTags, f"{table.name}_LOCATION"),
        ),
    )

    location_data[f"{table.value} - Distance Challenge: Target Score (Low)"] = PinballFXLocationData(
        archipelago_id=location_offset + table_offset + 17,
        region=table,
        tags=(
            PinballFXAPTags.TARGET_SCORE_LOCATION,
            PinballFXAPTags.TARGET_SCORE_LOW_LOCATION,
            PinballFXAPTags.DISTANCE_CHALLENGE_LOCATION,
            getattr(PinballFXAPTags, f"{table.name}_LOCATION"),
        ),
    )

    location_data[f"{table.value} - Distance Challenge: Target Score (Mid)"] = PinballFXLocationData(
        archipelago_id=location_offset + table_offset + 18,
        region=table,
        tags=(
            PinballFXAPTags.TARGET_SCORE_LOCATION,
            PinballFXAPTags.TARGET_SCORE_MID_LOCATION,
            PinballFXAPTags.DISTANCE_CHALLENGE_LOCATION,
            getattr(PinballFXAPTags, f"{table.name}_LOCATION"),
        ),
    )

    location_data[f"{table.value} - Distance Challenge: Target Score (High)"] = PinballFXLocationData(
        archipelago_id=location_offset + table_offset + 19,
        region=table,
        tags=(
            PinballFXAPTags.TARGET_SCORE_LOCATION,
            PinballFXAPTags.TARGET_SCORE_HIGH_LOCATION,
            PinballFXAPTags.DISTANCE_CHALLENGE_LOCATION,
            getattr(PinballFXAPTags, f"{table.name}_LOCATION"),
        ),
    )

    location_data[f"{table.value} - Distance Challenge: Target Score (Very High)"] = PinballFXLocationData(
        archipelago_id=location_offset + table_offset + 20,
        region=table,
        tags=(
            PinballFXAPTags.TARGET_SCORE_LOCATION,
            PinballFXAPTags.TARGET_SCORE_VERY_HIGH_LOCATION,
            PinballFXAPTags.DISTANCE_CHALLENGE_LOCATION,
            getattr(PinballFXAPTags, f"{table.name}_LOCATION"),
        ),
    )

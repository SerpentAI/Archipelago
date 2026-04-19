from typing import Dict, NamedTuple, Optional, Tuple

from .game_data import level_to_checkpoints

from ..enums import (
    MirrorsEdgeAPTags,
    MirrorsEdgeLevels,
    MirrorsEdgeLevelCheckpoints,
)


class MirrorsEdgeLocationData(NamedTuple):
    archipelago_id: Optional[int]
    region: str
    tags: Optional[Tuple[MirrorsEdgeAPTags, ...]] = None


location_offset: int = 1000000

location_data: Dict[str, MirrorsEdgeLocationData] = dict()

i: int
level: MirrorsEdgeLevels
for i, level in enumerate(MirrorsEdgeLevels):
    level_offset: int = i * 10000

    ii: int
    checkpoint: MirrorsEdgeLevelCheckpoints
    for ii, checkpoint in enumerate(level_to_checkpoints[level]):
        location_data[checkpoint.value] = MirrorsEdgeLocationData(
            archipelago_id=location_offset + level_offset + ii,
            region=f"{checkpoint.value}",
            tags=(
                MirrorsEdgeAPTags.CHECKPOINT_LOCATION,
                getattr(MirrorsEdgeAPTags, f"{level.name}_LOCATION"),
            ),
        )

    location_data[f"{level.value} - 1 Star Rating"] = MirrorsEdgeLocationData(
        archipelago_id=location_offset + level_offset + 25,
        region=f"{level.value} - 1 Star Rating",
        tags=(
            MirrorsEdgeAPTags.STAR_RATING_LOCATION,
            MirrorsEdgeAPTags.STAR_RATING_ONE_STAR_LOCATION,
            getattr(MirrorsEdgeAPTags, f"{level.name}_LOCATION"),
        ),
    )

    location_data[f"{level.value} - 2 Star Rating"] = MirrorsEdgeLocationData(
        archipelago_id=location_offset + level_offset + 26,
        region=f"{level.value} - 2 Star Rating",
        tags=(
            MirrorsEdgeAPTags.STAR_RATING_LOCATION,
            MirrorsEdgeAPTags.STAR_RATING_TWO_STAR_LOCATION,
            getattr(MirrorsEdgeAPTags, f"{level.name}_LOCATION"),
        ),
    )

    location_data[f"{level.value} - 3 Star Rating"] = MirrorsEdgeLocationData(
        archipelago_id=location_offset + level_offset + 27,
        region=f"{level.value} - 3 Star Rating",
        tags=(
            MirrorsEdgeAPTags.STAR_RATING_LOCATION,
            MirrorsEdgeAPTags.STAR_RATING_THREE_STAR_LOCATION,
            getattr(MirrorsEdgeAPTags, f"{level.name}_LOCATION"),
        ),
    )

from typing import Dict, NamedTuple, Optional, Tuple

from BaseClasses import ItemClassification

from ..enums import (
    DrMarioColors,
    DrMarioFillerTypes,
    DrMarioLevels,
    DrMarioMusicTypes,
    DrMarioTags,
    DrMarioTrapTypes,
)


class DrMarioItemData(NamedTuple):
    archipelago_id: Optional[int]
    classification: ItemClassification
    tags: Tuple[DrMarioTags, ...]


item_base_offset: int = 1000000

item_data: Dict[str, DrMarioItemData] = {
    "Antiviral Serum": DrMarioItemData(
        archipelago_id=item_base_offset + 1,
        classification=ItemClassification.progression_deprioritized_skip_balancing,
        tags=(DrMarioTags.GOAL_ITEM,),
    ),
    "Progressive Level Unlock": DrMarioItemData(
        archipelago_id=item_base_offset + 2,
        classification=ItemClassification.progression,
        tags=(DrMarioTags.LEVEL_UNLOCK_ITEM,),
    ),
    "Progressive Speed Unlock": DrMarioItemData(
        archipelago_id=item_base_offset + 3,
        classification=ItemClassification.progression,
        tags=(DrMarioTags.SPEED_UNLOCK_ITEM,),
    ),
    "Progressive Match Length Reduction": DrMarioItemData(
        archipelago_id=item_base_offset + 4,
        classification=ItemClassification.progression,
        tags=(DrMarioTags.MATCH_LENGTH_REDUCTION_ITEM,),
    ),
    "OOL": DrMarioItemData(
        archipelago_id=item_base_offset + 5,
        classification=ItemClassification.progression,
        tags=(DrMarioTags.OOL_ITEM,),
    ),
}

item_offset: int = 100

i: int
music_type: DrMarioMusicTypes
for i, music_type in enumerate((DrMarioMusicTypes.FEVER, DrMarioMusicTypes.CHILL)):
    item_data[f"Music Unlock: {music_type.value}"] = DrMarioItemData(
        archipelago_id=item_base_offset + item_offset + i,
        classification=ItemClassification.filler,
        tags=(DrMarioTags.MUSIC_UNLOCK_ITEM,),
    )

item_offset = 1000

i: int
level: DrMarioLevels
for i, level in enumerate(DrMarioLevels):
    item_data[f"Level Unlock: {level.value}"] = DrMarioItemData(
        archipelago_id=item_base_offset + item_offset + i,
        classification=ItemClassification.progression,
        tags=(
            DrMarioTags.LEVEL_UNLOCK_ITEM,
            getattr(DrMarioTags, f"{level.name}_ITEM"),
        ),
    )

item_offset = 10000

pill_color_order: Tuple[DrMarioColors, ...] = (DrMarioColors.RED, DrMarioColors.BLUE, DrMarioColors.YELLOW)

i: int
level: DrMarioLevels
for i, level in enumerate(DrMarioLevels):
    level_offset: int = item_offset + (i * 100)

    ii: int
    left_color: DrMarioColors
    right_color: DrMarioColors
    for ii, (left_color, right_color) in enumerate((left, right) for index, left in enumerate(pill_color_order) for right in pill_color_order[index:]):
        item_data[f"{level.value}: {left_color.value}-{right_color.value} Pill"] = DrMarioItemData(
            archipelago_id=item_base_offset + level_offset + ii + 1,
            classification=ItemClassification.progression,
            tags=(
                DrMarioTags.PILL_ITEM,
                getattr(DrMarioTags, f"{level.name}_ITEM"),
            ),
        )

    item_data[f"{level.value}: Clockwise Rotation"] = DrMarioItemData(
        archipelago_id=item_base_offset + level_offset + 11,
        classification=ItemClassification.progression,
        tags=(
            DrMarioTags.ROTATION_ITEM,
            getattr(DrMarioTags, f"{level.name}_ITEM"),
        ),
    )

    item_data[f"{level.value}: Counterclockwise Rotation"] = DrMarioItemData(
        archipelago_id=item_base_offset + level_offset + 12,
        classification=ItemClassification.progression,
        tags=(
            DrMarioTags.ROTATION_ITEM,
            getattr(DrMarioTags, f"{level.name}_ITEM"),
        ),
    )

    item_data[f"{level.value}: Next Pill Preview"] = DrMarioItemData(
        archipelago_id=item_base_offset + level_offset + 13,
        classification=ItemClassification.useful,
        tags=(
            DrMarioTags.NEXT_PILL_PREVIEW_ITEM,
            getattr(DrMarioTags, f"{level.name}_ITEM"),
        ),
    )

    item_data[f"{level.value}: Progressive Starting Garbage Reduction"] = DrMarioItemData(
        archipelago_id=item_base_offset + level_offset + 14,
        classification=ItemClassification.progression,
        tags=(
            DrMarioTags.GARBAGE_REDUCTION_ITEM,
            getattr(DrMarioTags, f"{level.name}_ITEM"),
        ),
    )

item_offset = 100000

i: int
filler_type: DrMarioFillerTypes
for i, filler_type in enumerate(DrMarioFillerTypes):
    item_data[filler_type.value] = DrMarioItemData(
        archipelago_id=item_base_offset + item_offset + i,
        classification=ItemClassification.filler,
        tags=(DrMarioTags.FILLER_ITEM,),
    )

i: int
trap_type: DrMarioTrapTypes
for i, trap_type in enumerate(DrMarioTrapTypes):
    item_data[trap_type.value] = DrMarioItemData(
        archipelago_id=item_base_offset + item_offset + 100 + i,
        classification=ItemClassification.trap,
        tags=(DrMarioTags.TRAP_ITEM,),
    )

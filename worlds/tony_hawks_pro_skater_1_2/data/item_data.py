from typing import Dict, NamedTuple, Optional, Tuple

from BaseClasses import ItemClassification

from ..enums import (
    TonyHawksProSkater12APTags,
    TonyHawksProSkater12Levels,
    TonyHawksProSkater12Skaters,
    TonyHawksProSkater12APTrapTypes,
)


class TonyHawksProSkater12ItemData(NamedTuple):
    archipelago_id: Optional[int]
    classification: ItemClassification
    tags: Tuple[TonyHawksProSkater12APTags, ...]


item_base_offset: int = 1000000

item_data: Dict[str, TonyHawksProSkater12ItemData] = {
    # Goal Items
    "Secret Tape": TonyHawksProSkater12ItemData(
        archipelago_id=item_base_offset + 1,
        classification=ItemClassification.progression_deprioritized_skip_balancing,
        tags=(TonyHawksProSkater12APTags.GOAL_ITEM,),
    ),
}

# Level Unlock Items
item_offset: int = 100

i: int
level: TonyHawksProSkater12Levels
for i, level in enumerate(TonyHawksProSkater12Levels):
    if level in [TonyHawksProSkater12Levels.ANYWHERE, TonyHawksProSkater12Levels.MAIN_MENU]:
        continue

    item_data[f"Level Unlock: {level.value}"] = TonyHawksProSkater12ItemData(
        archipelago_id=item_base_offset + item_offset + i,
        classification=ItemClassification.progression,
        tags=(TonyHawksProSkater12APTags.LEVEL_UNLOCK_ITEM,),
    )

# Skater Unlock Items
item_offset = 1000

i: int
skater: TonyHawksProSkater12Skaters
for i, skater in enumerate(TonyHawksProSkater12Skaters):
    item_data[f"Skater Unlock: {skater.value}"] = TonyHawksProSkater12ItemData(
        archipelago_id=item_base_offset + item_offset + i,
        classification=ItemClassification.progression,
        tags=(TonyHawksProSkater12APTags.SKATER_UNLOCK_ITEM,),
    )

# Per-Skater Items
item_offset = 10000

i: int
skater: TonyHawksProSkater12Skaters
for i, skater in enumerate(TonyHawksProSkater12Skaters):
    skater_offset = item_offset + (i * 100)

    # Progressive Stats
    item_data[f"Progressive Stats: {skater.value}"] = TonyHawksProSkater12ItemData(
        archipelago_id=item_base_offset + skater_offset + 1,
        classification=ItemClassification.progression,
        tags=(
            TonyHawksProSkater12APTags.PROGRESSIVE_STATS_ITEM,
            eval(f"TonyHawksProSkater12APTags.{skater.name}_ITEM"),
        ),
    )

    # Flip Tricks
    item_data[f"Flip Tricks: {skater.value}"] = TonyHawksProSkater12ItemData(
        archipelago_id=item_base_offset + skater_offset + 2,
        classification=ItemClassification.progression,
        tags=(
            TonyHawksProSkater12APTags.FLIP_TRICKS_ITEM,
            eval(f"TonyHawksProSkater12APTags.{skater.name}_ITEM"),
        ),
    )

    # Grab Tricks
    item_data[f"Grab Tricks: {skater.value}"] = TonyHawksProSkater12ItemData(
        archipelago_id=item_base_offset + skater_offset + 3,
        classification=ItemClassification.progression,
        tags=(
            TonyHawksProSkater12APTags.GRAB_TRICKS_ITEM,
            eval(f"TonyHawksProSkater12APTags.{skater.name}_ITEM"),
        ),
    )

    # Progressive Grind Tricks
    item_data[f"Progressive Grind Tricks: {skater.value}"] = TonyHawksProSkater12ItemData(
        archipelago_id=item_base_offset + skater_offset + 4,
        classification=ItemClassification.progression,
        tags=(
            TonyHawksProSkater12APTags.PROGRESSIVE_GRIND_TRICKS_ITEM,
            eval(f"TonyHawksProSkater12APTags.{skater.name}_ITEM"),
        ),
    )

    # Progressive Lip Tricks
    item_data[f"Progressive Lip Tricks: {skater.value}"] = TonyHawksProSkater12ItemData(
        archipelago_id=item_base_offset + skater_offset + 5,
        classification=ItemClassification.progression,
        tags=(
            TonyHawksProSkater12APTags.PROGRESSIVE_LIP_TRICKS_ITEM,
            eval(f"TonyHawksProSkater12APTags.{skater.name}_ITEM"),
        ),
    )

    # Progressive Manual Tricks
    item_data[f"Progressive Manual Tricks: {skater.value}"] = TonyHawksProSkater12ItemData(
        archipelago_id=item_base_offset + skater_offset + 6,
        classification=ItemClassification.progression,
        tags=(
            TonyHawksProSkater12APTags.PROGRESSIVE_MANUAL_TRICKS_ITEM,
            eval(f"TonyHawksProSkater12APTags.{skater.name}_ITEM"),
        ),
    )

    # Progressive Special Meter
    item_data[f"Progressive Special Meter: {skater.value}"] = TonyHawksProSkater12ItemData(
        archipelago_id=item_base_offset + skater_offset + 7,
        classification=ItemClassification.progression,
        tags=(
            TonyHawksProSkater12APTags.PROGRESSIVE_SPECIAL_METER_ITEM,
            eval(f"TonyHawksProSkater12APTags.{skater.name}_ITEM"),
        ),
    )

    # Spin Tricks
    item_data[f"Spin Tricks: {skater.value}"] = TonyHawksProSkater12ItemData(
        archipelago_id=item_base_offset + skater_offset + 8,
        classification=ItemClassification.progression,
        tags=(
            TonyHawksProSkater12APTags.SPIN_TRICKS_ITEM,
            eval(f"TonyHawksProSkater12APTags.{skater.name}_ITEM"),
        ),
    )

    # Transfers
    item_data[f"Transfers: {skater.value}"] = TonyHawksProSkater12ItemData(
        archipelago_id=item_base_offset + skater_offset + 9,
        classification=ItemClassification.progression,
        tags=(
            TonyHawksProSkater12APTags.TRANSFERS_ITEM,
            eval(f"TonyHawksProSkater12APTags.{skater.name}_ITEM"),
        ),
    )

    # Wallplants
    item_data[f"Wallplants: {skater.value}"] = TonyHawksProSkater12ItemData(
        archipelago_id=item_base_offset + skater_offset + 10,
        classification=ItemClassification.progression,
        tags=(
            TonyHawksProSkater12APTags.WALLPLANTS_ITEM,
            eval(f"TonyHawksProSkater12APTags.{skater.name}_ITEM"),
        ),
    )

    # Extra Tricks
    item_data[f"Extra Tricks: {skater.value}"] = TonyHawksProSkater12ItemData(
        archipelago_id=item_base_offset + skater_offset + 11,
        classification=ItemClassification.progression,
        tags=(
            TonyHawksProSkater12APTags.EXTRA_TRICKS_ITEM,
            eval(f"TonyHawksProSkater12APTags.{skater.name}_ITEM"),
        ),
    )

    # Stance Switching
    item_data[f"Stance Switching: {skater.value}"] = TonyHawksProSkater12ItemData(
        archipelago_id=item_base_offset + skater_offset + 12,
        classification=ItemClassification.progression,
        tags=(
            TonyHawksProSkater12APTags.STANCE_SWITCHING_ITEM,
            eval(f"TonyHawksProSkater12APTags.{skater.name}_ITEM"),
        ),
    )

    # Double Score
    item_data[f"Double Score: {skater.value}"] = TonyHawksProSkater12ItemData(
        archipelago_id=item_base_offset + skater_offset + 13,
        classification=ItemClassification.progression,
        tags=(
            TonyHawksProSkater12APTags.DOUBLE_SCORE_ITEM,
            eval(f"TonyHawksProSkater12APTags.{skater.name}_ITEM"),
        ),
    )

# Filler & Trap Items
item_offset = 100000

i: int
skater: TonyHawksProSkater12Skaters
for i, skater in enumerate(TonyHawksProSkater12Skaters):
    item_data[f"{skater.value} Bobblehead"] = TonyHawksProSkater12ItemData(
        archipelago_id=item_base_offset + item_offset + i,
        classification=ItemClassification.filler,
        tags=(TonyHawksProSkater12APTags.FILLER_ITEM,),
    )

i: int
trap_type: TonyHawksProSkater12APTrapTypes
for i, trap_type in enumerate(TonyHawksProSkater12APTrapTypes):
    item_data[trap_type.value] = TonyHawksProSkater12ItemData(
        archipelago_id=item_base_offset + item_offset + 100 + i,
        classification=ItemClassification.trap,
        tags=(TonyHawksProSkater12APTags.TRAP_ITEM,),
    )

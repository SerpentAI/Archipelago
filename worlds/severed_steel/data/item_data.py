from typing import Dict, NamedTuple, Optional, Tuple

from BaseClasses import ItemClassification

from .game_data import stylish_actions_pool

from ..enums import (
    SeveredSteelAPTags,
    SeveredSteelAPTrapTypes,
    SeveredSteelLevels,
    SeveredSteelStylishActions,
)


class SeveredSteelItemData(NamedTuple):
    archipelago_id: Optional[int]
    classification: ItemClassification
    tags: Tuple[SeveredSteelAPTags, ...]


item_base_offset: int = 1000000

item_data: Dict[str, SeveredSteelItemData] = {
    # Goal Items
    "EdenSys Root Key": SeveredSteelItemData(
        archipelago_id=item_base_offset + 1,
        classification=ItemClassification.progression_deprioritized_skip_balancing,
        tags=(SeveredSteelAPTags.GOAL_ITEM,),
    ),
    # Rank-Boosting Items
    "Progressive Multiplier Burn Rate Reduction": SeveredSteelItemData(
        archipelago_id=item_base_offset + 5,
        classification=ItemClassification.progression,
        tags=(SeveredSteelAPTags.RANK_BOOSTING_ITEM,),
    ),
    "Progressive Fresh Cooldown Reduction": SeveredSteelItemData(
        archipelago_id=item_base_offset + 6,
        classification=ItemClassification.progression,
        tags=(SeveredSteelAPTags.RANK_BOOSTING_ITEM,),
    ),
}

# Level Unlock Items
item_offset: int = 100

i: int
level: SeveredSteelLevels
for i, level in enumerate(SeveredSteelLevels):
    item_data[f"Level Unlock: {level.value}"] = SeveredSteelItemData(
        archipelago_id=item_base_offset + item_offset + i,
        classification=ItemClassification.progression,
        tags=(SeveredSteelAPTags.LEVEL_UNLOCK_ITEM,),
    )

# Stylish Action License Items
item_offset = 1000

i: int
stylish_action: SeveredSteelStylishActions
for i, stylish_action in enumerate(stylish_actions_pool):
    item_data[f"Stylish Action License: {stylish_action.value}"] = SeveredSteelItemData(
        archipelago_id=item_base_offset + item_offset + i + 1,
        classification=ItemClassification.progression,
        tags=(SeveredSteelAPTags.STYLISH_ACTION_LICENSE_ITEM,),
    )

# Per-Level Items
item_offset = 10000

i: int
level: SeveredSteelLevels
for i, level in enumerate(SeveredSteelLevels):
    level_offset: int = item_offset + (i * 100)

    item_data[f"{level.value}: 10% Target Time Discount"] = SeveredSteelItemData(
        archipelago_id=item_base_offset + level_offset + 1,
        classification=ItemClassification.useful,
        tags=(
            SeveredSteelAPTags.TARGET_TIME_DISCOUNT_ITEM,
            getattr(SeveredSteelAPTags, f"{level.name}_ITEM"),
        ),
    )

    item_data[f"{level.value}: Double Score"] = SeveredSteelItemData(
        archipelago_id=item_base_offset + level_offset + 2,
        classification=ItemClassification.useful,
        tags=(
            SeveredSteelAPTags.DOUBLE_SCORE_ITEM,
            getattr(SeveredSteelAPTags, f"{level.name}_ITEM"),
        ),
    )

    item_data[f"{level.value}: Unlimited Ammo Unlocked"] = SeveredSteelItemData(
        archipelago_id=item_base_offset + level_offset + 3,
        classification=ItemClassification.useful,
        tags=(
            SeveredSteelAPTags.UNLIMITED_AMMO_ITEM,
            getattr(SeveredSteelAPTags, f"{level.name}_ITEM"),
        ),
    )

    item_data[f"{level.value}: Unlimited Cannon Ammo Unlocked"] = SeveredSteelItemData(
        archipelago_id=item_base_offset + level_offset + 4,
        classification=ItemClassification.useful,
        tags=(
            SeveredSteelAPTags.UNLIMITED_CANNON_AMMO_ITEM,
            getattr(SeveredSteelAPTags, f"{level.name}_ITEM"),
        ),
    )

    item_data[f"{level.value}: Invincibility Unlocked"] = SeveredSteelItemData(
        archipelago_id=item_base_offset + level_offset + 5,
        classification=ItemClassification.useful,
        tags=(
            SeveredSteelAPTags.INVINCIBILITY_ITEM,
            getattr(SeveredSteelAPTags, f"{level.name}_ITEM"),
        ),
    )

# Filler & Trap Items
item_offset = 100000

i: int
level: SeveredSteelLevels
for i, level in enumerate(SeveredSteelLevels):
    item_data[f"Schematic: {level.value}"] = SeveredSteelItemData(
        archipelago_id=item_base_offset + item_offset + i,
        classification=ItemClassification.filler,
        tags=(SeveredSteelAPTags.FILLER_ITEM,),
    )

i: int
trap_type: SeveredSteelAPTrapTypes
for i, trap_type in enumerate(SeveredSteelAPTrapTypes):
    item_data[trap_type.value] = SeveredSteelItemData(
        archipelago_id=item_base_offset + item_offset + 100 + i,
        classification=ItemClassification.trap,
        tags=(SeveredSteelAPTags.TRAP_ITEM,),
    )

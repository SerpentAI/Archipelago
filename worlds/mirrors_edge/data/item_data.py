from typing import Dict, NamedTuple, Optional, Tuple

from BaseClasses import ItemClassification

from ..enums import (
    MirrorsEdgeAPTags,
    MirrorsEdgeAbilities,
    MirrorsEdgeLevels,
    MirrorsEdgeAPTrapTypes,
)


class MirrorsEdgeItemData(NamedTuple):
    archipelago_id: Optional[int]
    classification: ItemClassification
    tags: Tuple[MirrorsEdgeAPTags, ...]


item_base_offset: int = 1000000

item_data: Dict[str, MirrorsEdgeItemData] = {
    # Goal Items
    "Runner Bag": MirrorsEdgeItemData(
        archipelago_id=item_base_offset + 1,
        classification=ItemClassification.progression_deprioritized_skip_balancing,
        tags=(MirrorsEdgeAPTags.GOAL_ITEM,),
    ),
    # Logic Items
    "Advanced Logic": MirrorsEdgeItemData(
        archipelago_id=item_base_offset + 2,
        classification=ItemClassification.progression,
        tags=(MirrorsEdgeAPTags.LOGIC_ITEM,),
    )
}

# Level Unlock Items
item_offset: int = 100

i: int
level: MirrorsEdgeLevels
for i, level in enumerate(MirrorsEdgeLevels):
    item_data[f"Level Unlock: {level.value}"] = MirrorsEdgeItemData(
        archipelago_id=item_base_offset + item_offset + i,
        classification=ItemClassification.progression,
        tags=(MirrorsEdgeAPTags.LEVEL_UNLOCK_ITEM,),
    )

# Ability Unlock Items
item_offset = 1000

item_data[f"Ability Unlock: {MirrorsEdgeAbilities.AIRBORNE_ONE_EIGHTY_TURN.value}"] = MirrorsEdgeItemData(
    archipelago_id=item_base_offset + item_offset + 1,
    classification=ItemClassification.useful,
    tags=(MirrorsEdgeAPTags.ABILITY_UNLOCK_ITEM,),
)

item_data[f"Ability Unlock: {MirrorsEdgeAbilities.BALANCE.value}"] = MirrorsEdgeItemData(
    archipelago_id=item_base_offset + item_offset + 2,
    classification=ItemClassification.progression,
    tags=(MirrorsEdgeAPTags.ABILITY_UNLOCK_ITEM,),
)

item_data[f"Ability Unlock: {MirrorsEdgeAbilities.BARGE.value}"] = MirrorsEdgeItemData(
    archipelago_id=item_base_offset + item_offset + 3,
    classification=ItemClassification.progression,
    tags=(MirrorsEdgeAPTags.ABILITY_UNLOCK_ITEM,),
)

item_data[f"Ability Unlock: {MirrorsEdgeAbilities.CLIMB.value}"] = MirrorsEdgeItemData(
    archipelago_id=item_base_offset + item_offset + 4,
    classification=ItemClassification.progression,
    tags=(MirrorsEdgeAPTags.ABILITY_UNLOCK_ITEM,),
)

item_data[f"Ability Unlock: {MirrorsEdgeAbilities.COIL.value}"] = MirrorsEdgeItemData(
    archipelago_id=item_base_offset + item_offset + 5,
    classification=ItemClassification.progression,
    tags=(MirrorsEdgeAPTags.ABILITY_UNLOCK_ITEM,),
)

item_data[f"Ability Unlock: {MirrorsEdgeAbilities.DODGE_JUMP.value}"] = MirrorsEdgeItemData(
    archipelago_id=item_base_offset + item_offset + 6,
    classification=ItemClassification.useful,
    tags=(MirrorsEdgeAPTags.ABILITY_UNLOCK_ITEM,),
)

item_data[f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"] = MirrorsEdgeItemData(
    archipelago_id=item_base_offset + item_offset + 7,
    classification=ItemClassification.progression,
    tags=(MirrorsEdgeAPTags.ABILITY_UNLOCK_ITEM,),
)

item_data[f"Ability Extension Unlock: {MirrorsEdgeAbilities.GRAB_JUMP.value}"] = MirrorsEdgeItemData(
    archipelago_id=item_base_offset + item_offset + 8,
    classification=ItemClassification.progression,
    tags=(MirrorsEdgeAPTags.ABILITY_UNLOCK_ITEM,),
)

item_data[f"Ability Unlock: {MirrorsEdgeAbilities.MELEE_ATTACK.value}"] = MirrorsEdgeItemData(
    archipelago_id=item_base_offset + item_offset + 9,
    classification=ItemClassification.progression,
    tags=(MirrorsEdgeAPTags.ABILITY_UNLOCK_ITEM,),
)

item_data[f"Ability Unlock: {MirrorsEdgeAbilities.ONE_EIGHTY_TURN.value}"] = MirrorsEdgeItemData(
    archipelago_id=item_base_offset + item_offset + 10,
    classification=ItemClassification.useful,
    tags=(MirrorsEdgeAPTags.ABILITY_UNLOCK_ITEM,),
)

item_data[f"Ability Unlock: {MirrorsEdgeAbilities.SPRINGBOARD.value}"] = MirrorsEdgeItemData(
    archipelago_id=item_base_offset + item_offset + 11,
    classification=ItemClassification.progression,
    tags=(MirrorsEdgeAPTags.ABILITY_UNLOCK_ITEM,),
)

item_data[f"Ability Unlock: {MirrorsEdgeAbilities.SPRINT.value}"] = MirrorsEdgeItemData(
    archipelago_id=item_base_offset + item_offset + 12,
    classification=ItemClassification.progression,
    tags=(MirrorsEdgeAPTags.ABILITY_UNLOCK_ITEM,),
)

item_data[f"Ability Unlock: {MirrorsEdgeAbilities.SWING.value}"] = MirrorsEdgeItemData(
    archipelago_id=item_base_offset + item_offset + 13,
    classification=ItemClassification.progression,
    tags=(MirrorsEdgeAPTags.ABILITY_UNLOCK_ITEM,),
)

item_data[f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"] = MirrorsEdgeItemData(
    archipelago_id=item_base_offset + item_offset + 14,
    classification=ItemClassification.progression,
    tags=(MirrorsEdgeAPTags.ABILITY_UNLOCK_ITEM,),
)

item_data[f"Ability Unlock: {MirrorsEdgeAbilities.WALL_CLIMB.value}"] = MirrorsEdgeItemData(
    archipelago_id=item_base_offset + item_offset + 15,
    classification=ItemClassification.progression,
    tags=(MirrorsEdgeAPTags.ABILITY_UNLOCK_ITEM,),
)

item_data[f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_CLIMB_ONE_EIGHTY_TURN_JUMP.value}"] = MirrorsEdgeItemData(
    archipelago_id=item_base_offset + item_offset + 16,
    classification=ItemClassification.progression,
    tags=(MirrorsEdgeAPTags.ABILITY_UNLOCK_ITEM,),
)

item_data[f"Ability Unlock: {MirrorsEdgeAbilities.WALL_RUN.value}"] = MirrorsEdgeItemData(
    archipelago_id=item_base_offset + item_offset + 17,
    classification=ItemClassification.progression,
    tags=(MirrorsEdgeAPTags.ABILITY_UNLOCK_ITEM,),
)

item_data[f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_RUN_JUMP.value}"] = MirrorsEdgeItemData(
    archipelago_id=item_base_offset + item_offset + 18,
    classification=ItemClassification.progression,
    tags=(MirrorsEdgeAPTags.ABILITY_UNLOCK_ITEM,),
)

item_data[f"Ability Unlock: {MirrorsEdgeAbilities.ZIPLINE.value}"] = MirrorsEdgeItemData(
    archipelago_id=item_base_offset + item_offset + 19,
    classification=ItemClassification.progression,
    tags=(MirrorsEdgeAPTags.ABILITY_UNLOCK_ITEM,),
)

# Per-Level Items
item_offset = 10000

i: int
level: MirrorsEdgeLevels
for i, level in enumerate(MirrorsEdgeLevels):
    level_offset: int = item_offset + (i * 100)

    item_data[f"{level.value}: 1 Second Time Bonus"] = MirrorsEdgeItemData(
        archipelago_id=item_base_offset + level_offset + 1,
        classification=ItemClassification.useful,
        tags=(
            MirrorsEdgeAPTags.TIME_BONUS_ITEM,
            MirrorsEdgeAPTags.TIME_BONUS_ONE_SECOND_ITEM,
            getattr(MirrorsEdgeAPTags, f"{level.name}_ITEM"),
        ),
    )

    item_data[f"{level.value}: 3 Seconds Time Bonus"] = MirrorsEdgeItemData(
        archipelago_id=item_base_offset + level_offset + 2,
        classification=ItemClassification.useful,
        tags=(
            MirrorsEdgeAPTags.TIME_BONUS_ITEM,
            MirrorsEdgeAPTags.TIME_BONUS_THREE_SECONDS_ITEM,
            getattr(MirrorsEdgeAPTags, f"{level.name}_ITEM"),
        ),
    )

    item_data[f"{level.value}: 5 Seconds Time Bonus"] = MirrorsEdgeItemData(
        archipelago_id=item_base_offset + level_offset + 3,
        classification=ItemClassification.useful,
        tags=(
            MirrorsEdgeAPTags.TIME_BONUS_ITEM,
            MirrorsEdgeAPTags.TIME_BONUS_FIVE_SECONDS_ITEM,
            getattr(MirrorsEdgeAPTags, f"{level.name}_ITEM"),
        ),
    )

# Filler & Trap Items
item_offset = 100000

i: int
level: MirrorsEdgeLevels
for i, level in enumerate(MirrorsEdgeLevels):
    item_data[f"Schematic: {level.value}"] = MirrorsEdgeItemData(
        archipelago_id=item_base_offset + item_offset + i,
        classification=ItemClassification.filler,
        tags=(MirrorsEdgeAPTags.FILLER_ITEM,),
    )

    item_data[f"Classified Schematic: {level.value}"] = MirrorsEdgeItemData(
        archipelago_id=item_base_offset + item_offset + 50 + i,
        classification=ItemClassification.filler,
        tags=(MirrorsEdgeAPTags.RARE_FILLER_ITEM,),
    )

i: int
trap_type: MirrorsEdgeAPTrapTypes
for i, trap_type in enumerate(MirrorsEdgeAPTrapTypes):
    item_data[trap_type.value] = MirrorsEdgeItemData(
        archipelago_id=item_base_offset + item_offset + 100 + i,
        classification=ItemClassification.trap,
        tags=(MirrorsEdgeAPTags.TRAP_ITEM,),
    )

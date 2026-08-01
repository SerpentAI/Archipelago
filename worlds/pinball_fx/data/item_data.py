from typing import Dict, NamedTuple, Optional, Tuple

from BaseClasses import ItemClassification

from ..enums import PinballFXAPTags, PinballFXAPTrapTypes, PinballFXTables


class PinballFXItemData(NamedTuple):
    archipelago_id: Optional[int]
    classification: ItemClassification
    tags: Tuple[PinballFXAPTags, ...]


item_offset: int = 1000000

item_data: Dict[str, PinballFXItemData] = {
    # Goal Items
    "Shiny Quarter": PinballFXItemData(
        archipelago_id=item_offset + 1,
        classification=ItemClassification.progression_deprioritized_skip_balancing,
        tags=(PinballFXAPTags.GOAL_ITEM,),
    ),
    # Trap Items
    PinballFXAPTrapTypes.BLACK_AND_WHITE.value: PinballFXItemData(
        archipelago_id=item_offset + 50 + 1,
        classification=ItemClassification.trap,
        tags=(PinballFXAPTags.TRAP_ITEM,),
    ),
    PinballFXAPTrapTypes.BLOOM.value: PinballFXItemData(
        archipelago_id=item_offset + 50 + 2,
        classification=ItemClassification.trap,
        tags=(PinballFXAPTags.TRAP_ITEM,),
    ),
    PinballFXAPTrapTypes.CHROMATIC.value: PinballFXItemData(
        archipelago_id=item_offset + 50 + 3,
        classification=ItemClassification.trap,
        tags=(PinballFXAPTags.TRAP_ITEM,),
    ),
    PinballFXAPTrapTypes.COLOR_INVERSION.value: PinballFXItemData(
        archipelago_id=item_offset + 50 + 4,
        classification=ItemClassification.trap,
        tags=(PinballFXAPTags.TRAP_ITEM,),
    ),
    PinballFXAPTrapTypes.GRAINY.value: PinballFXItemData(
        archipelago_id=item_offset + 50 + 5,
        classification=ItemClassification.trap,
        tags=(PinballFXAPTags.TRAP_ITEM,),
    ),
    PinballFXAPTrapTypes.TUNNEL_VISION.value: PinballFXItemData(
        archipelago_id=item_offset + 50 + 6,
        classification=ItemClassification.trap,
        tags=(PinballFXAPTags.TRAP_ITEM,),
    ),
    # Filler Items
    "Cracked Quarter": PinballFXItemData(
        archipelago_id=item_offset + 100 + 1,
        classification=ItemClassification.filler,
        tags=(PinballFXAPTags.FILLER_ITEM,),
    ),
    "Dirty Quarter": PinballFXItemData(
        archipelago_id=item_offset + 100 + 2,
        classification=ItemClassification.filler,
        tags=(PinballFXAPTags.FILLER_ITEM,),
    ),
    "Dull Quarter": PinballFXItemData(
        archipelago_id=item_offset + 100 + 3,
        classification=ItemClassification.filler,
        tags=(PinballFXAPTags.FILLER_ITEM,),
    ),
    "Faded Quarter": PinballFXItemData(
        archipelago_id=item_offset + 100 + 4,
        classification=ItemClassification.filler,
        tags=(PinballFXAPTags.FILLER_ITEM,),
    ),
    "Worn Quarter": PinballFXItemData(
        archipelago_id=item_offset + 100 + 5,
        classification=ItemClassification.filler,
        tags=(PinballFXAPTags.FILLER_ITEM,),
    ),
}

# Table Items
item_offset = 100000

i: int
table: PinballFXTables
for i, table in enumerate(PinballFXTables):
    table_offset: int = 100 * i

    # Table Game Mode / Challenge Unlocks
    item_data[f"Classic Mode Unlock: {table.value}"] = PinballFXItemData(
        archipelago_id=item_offset + table_offset + 1,
        classification=ItemClassification.progression,
        tags=(
            PinballFXAPTags.CLASSIC_MODE_UNLOCK_ITEM,
            getattr(PinballFXAPTags, f"{table.name}_ITEM"),
        ),
    )

    item_data[f"1 Ball Challenge Unlock: {table.value}"] = PinballFXItemData(
        archipelago_id=item_offset + table_offset + 2,
        classification=ItemClassification.progression,
        tags=(
            PinballFXAPTags.ONE_BALL_CHALLENGE_UNLOCK_ITEM,
            getattr(PinballFXAPTags, f"{table.name}_ITEM"),
        ),
    )

    item_data[f"Flips Challenge Unlock: {table.value}"] = PinballFXItemData(
        archipelago_id=item_offset + table_offset + 3,
        classification=ItemClassification.progression,
        tags=(
            PinballFXAPTags.FLIPS_CHALLENGE_UNLOCK_ITEM,
            getattr(PinballFXAPTags, f"{table.name}_ITEM"),
        ),
    )

    item_data[f"Time Challenge Unlock: {table.value}"] = PinballFXItemData(
        archipelago_id=item_offset + table_offset + 4,
        classification=ItemClassification.progression,
        tags=(
            PinballFXAPTags.TIME_CHALLENGE_UNLOCK_ITEM,
            getattr(PinballFXAPTags, f"{table.name}_ITEM"),
        ),
    )

    item_data[f"Distance Challenge Unlock: {table.value}"] = PinballFXItemData(
        archipelago_id=item_offset + table_offset + 5,
        classification=ItemClassification.progression,
        tags=(
            PinballFXAPTags.DISTANCE_CHALLENGE_UNLOCK_ITEM,
            getattr(PinballFXAPTags, f"{table.name}_ITEM"),
        ),
    )

    # Useful Items
    item_data[f"{table.value} - Classic Mode: Score Multiplier"] = PinballFXItemData(
        archipelago_id=item_offset + table_offset + 11,
        classification=ItemClassification.useful,
        tags=(
            PinballFXAPTags.USEFUL_ITEM,
            getattr(PinballFXAPTags, f"{table.name}_ITEM"),
        ),
    )

    item_data[f"{table.value} - Classic Mode: Target Score Discount"] = PinballFXItemData(
        archipelago_id=item_offset + table_offset + 12,
        classification=ItemClassification.useful,
        tags=(
            PinballFXAPTags.USEFUL_ITEM,
            getattr(PinballFXAPTags, f"{table.name}_ITEM"),
        ),
    )

    item_data[f"{table.value} - 1 Ball Challenge: Score Multiplier"] = PinballFXItemData(
        archipelago_id=item_offset + table_offset + 13,
        classification=ItemClassification.useful,
        tags=(
            PinballFXAPTags.USEFUL_ITEM,
            getattr(PinballFXAPTags, f"{table.name}_ITEM"),
        ),
    )

    item_data[f"{table.value} - 1 Ball Challenge: Target Score Discount"] = PinballFXItemData(
        archipelago_id=item_offset + table_offset + 14,
        classification=ItemClassification.useful,
        tags=(
            PinballFXAPTags.USEFUL_ITEM,
            getattr(PinballFXAPTags, f"{table.name}_ITEM"),
        ),
    )

    item_data[f"{table.value} - Flips Challenge: Score Multiplier"] = PinballFXItemData(
        archipelago_id=item_offset + table_offset + 15,
        classification=ItemClassification.useful,
        tags=(
            PinballFXAPTags.USEFUL_ITEM,
            getattr(PinballFXAPTags, f"{table.name}_ITEM"),
        ),
    )

    item_data[f"{table.value} - Flips Challenge: Target Score Discount"] = PinballFXItemData(
        archipelago_id=item_offset + table_offset + 16,
        classification=ItemClassification.useful,
        tags=(
            PinballFXAPTags.USEFUL_ITEM,
            getattr(PinballFXAPTags, f"{table.name}_ITEM"),
        ),
    )

    item_data[f"{table.value} - Time Challenge: Score Multiplier"] = PinballFXItemData(
        archipelago_id=item_offset + table_offset + 17,
        classification=ItemClassification.useful,
        tags=(
            PinballFXAPTags.USEFUL_ITEM,
            getattr(PinballFXAPTags, f"{table.name}_ITEM"),
        ),
    )

    item_data[f"{table.value} - Time Challenge: Target Score Discount"] = PinballFXItemData(
        archipelago_id=item_offset + table_offset + 18,
        classification=ItemClassification.useful,
        tags=(
            PinballFXAPTags.USEFUL_ITEM,
            getattr(PinballFXAPTags, f"{table.name}_ITEM"),
        ),
    )

    item_data[f"{table.value} - Distance Challenge: Score Multiplier"] = PinballFXItemData(
        archipelago_id=item_offset + table_offset + 19,
        classification=ItemClassification.useful,
        tags=(
            PinballFXAPTags.USEFUL_ITEM,
            getattr(PinballFXAPTags, f"{table.name}_ITEM"),
        ),
    )

    item_data[f"{table.value} - Distance Challenge: Target Score Discount"] = PinballFXItemData(
        archipelago_id=item_offset + table_offset + 20,
        classification=ItemClassification.useful,
        tags=(
            PinballFXAPTags.USEFUL_ITEM,
            getattr(PinballFXAPTags, f"{table.name}_ITEM"),
        ),
    )

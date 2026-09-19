from typing import Dict, NamedTuple, Optional, Tuple

from BaseClasses import ItemClassification

from ..enums import (
    TwentyMinutesCharacters,
    TwentyMinutesMaps,
    TwentyMinutesRunes,
    TwentyMinutesTags,
    TwentyMinutesTrapTypes,
    TwentyMinutesWeapons,
)


class TwentyMinutesItemData(NamedTuple):
    archipelago_id: Optional[int]
    classification: ItemClassification
    tags: Tuple[TwentyMinutesTags, ...]


item_base_offset: int = 1000000

item_data: Dict[str, TwentyMinutesItemData] = {
    # Goal Items
    "Forbidden Tome": TwentyMinutesItemData(
        archipelago_id=item_base_offset + 1,
        classification=ItemClassification.progression_deprioritized_skip_balancing,
        tags=(TwentyMinutesTags.GOAL_ITEM,),
    ),
    # OOL Item
    "OOL": TwentyMinutesItemData(
        archipelago_id=item_base_offset + 5,
        classification=ItemClassification.progression,
        tags=(TwentyMinutesTags.OOL_ITEM,),
    ),
}

# Character Unlock Items
item_offset: int = 100

i: int
character: TwentyMinutesCharacters
for i, character in enumerate(TwentyMinutesCharacters):
    item_data[f"Character Unlock: {character.value}"] = TwentyMinutesItemData(
        archipelago_id=item_base_offset + item_offset + i,
        classification=ItemClassification.progression,
        tags=(TwentyMinutesTags.CHARACTER_UNLOCK_ITEM,),
    )

# Weapon Unlock Items
item_offset = 1000

i: int
weapon: TwentyMinutesWeapons
for i, weapon in enumerate(TwentyMinutesWeapons):
    item_data[f"Weapon Unlock: {weapon.value}"] = TwentyMinutesItemData(
        archipelago_id=item_base_offset + item_offset + i,
        classification=ItemClassification.progression,
        tags=(TwentyMinutesTags.WEAPON_UNLOCK_ITEM,),
    )

# Map Unlock Items
item_offset = 2000

i: int
map_: TwentyMinutesMaps
for i, map_ in enumerate(TwentyMinutesMaps):
    item_data[f"Map Unlock: {map_.value}"] = TwentyMinutesItemData(
        archipelago_id=item_base_offset + item_offset + i,
        classification=ItemClassification.progression,
        tags=(TwentyMinutesTags.MAP_UNLOCK_ITEM,),
    )

# Darkness Reduction Items
item_offset = 3000

item_data["Progressive Darkness Reduction"] = TwentyMinutesItemData(
    archipelago_id=item_base_offset + item_offset + 1,
    classification=ItemClassification.progression,
    tags=(TwentyMinutesTags.DARKNESS_REDUCTION_ITEM,),
)

# Progressive Timer Items
item_offset = 4000

i: int
map_: TwentyMinutesMaps
for i, map_ in enumerate(TwentyMinutesMaps):
    item_data[f"Progressive Timer: {map_.value}"] = TwentyMinutesItemData(
        archipelago_id=item_base_offset + item_offset + i,
        classification=ItemClassification.progression,
        tags=(
            TwentyMinutesTags.PROGRESSIVE_TIMER_ITEM,
            getattr(TwentyMinutesTags, f"{map_.name}_ITEM"),
        ),
    )

# Progressive Powerup Choice Items
item_offset = 5000

i: int
character: TwentyMinutesCharacters
for i, character in enumerate(TwentyMinutesCharacters):
    item_data[f"Progressive Powerup Choices: {character.value}"] = TwentyMinutesItemData(
        archipelago_id=item_base_offset + item_offset + i,
        classification=ItemClassification.useful,
        tags=(
            TwentyMinutesTags.PROGRESSIVE_POWERUP_CHOICES_ITEM,
            getattr(TwentyMinutesTags, f"{character.name}_ITEM"),
        ),
    )

# Rune Items
item_offset = 10000

i: int
rune: TwentyMinutesRunes
for i, rune in enumerate(TwentyMinutesRunes):
    rune_offset = item_offset + (i * 10)

    item_data[f"3 Rune Points: {rune.value}"] = TwentyMinutesItemData(
        archipelago_id=item_base_offset + rune_offset + 1,
        classification=ItemClassification.useful,
        tags=(TwentyMinutesTags.RUNE_ITEM,),
    )

    item_data[f"1 Rune Point: {rune.value}"] = TwentyMinutesItemData(
        archipelago_id=item_base_offset + rune_offset + 2,
        classification=ItemClassification.useful,
        tags=(TwentyMinutesTags.RUNE_ITEM,),
    )

# Useful Items
item_offset = 30000

i: int
character: TwentyMinutesCharacters
for i, character in enumerate(TwentyMinutesCharacters):
    character_offset = item_offset + (i * 10)

    item_data[f"Heart Container: {character.value}"] = TwentyMinutesItemData(
        archipelago_id=item_base_offset + character_offset + 1,
        classification=ItemClassification.useful,
        tags=(
            TwentyMinutesTags.USEFUL_ITEM,
            getattr(TwentyMinutesTags, f"{character.name}_ITEM"),
        ),
    )

    item_data[f"Soul Heart Capacity: {character.value}"] = TwentyMinutesItemData(
        archipelago_id=item_base_offset + character_offset + 2,
        classification=ItemClassification.useful,
        tags=(
            TwentyMinutesTags.USEFUL_ITEM,
            getattr(TwentyMinutesTags, f"{character.name}_ITEM"),
        ),
    )

# Trap Items
item_offset = 40000

i: int
trap_type: TwentyMinutesTrapTypes
for i, trap_type in enumerate(TwentyMinutesTrapTypes):
    item_data[trap_type.value] = TwentyMinutesItemData(
        archipelago_id=item_base_offset + item_offset + i,
        classification=ItemClassification.trap,
        tags=(TwentyMinutesTags.TRAP_ITEM,),
    )

# Filler Items
item_offset = 50000

item_data["Heal 1 Heart"] = TwentyMinutesItemData(
    archipelago_id=item_base_offset + item_offset + 1,
    classification=ItemClassification.filler,
    tags=(TwentyMinutesTags.FILLER_ITEM,),
)

item_data["Full Heal"] = TwentyMinutesItemData(
    archipelago_id=item_base_offset + item_offset + 2,
    classification=ItemClassification.filler,
    tags=(TwentyMinutesTags.FILLER_ITEM,),
)

item_data["Soul Heart"] = TwentyMinutesItemData(
    archipelago_id=item_base_offset + item_offset + 3,
    classification=ItemClassification.filler,
    tags=(TwentyMinutesTags.FILLER_ITEM,),
)

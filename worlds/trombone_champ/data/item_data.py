from typing import Dict, NamedTuple, Optional, Tuple

from BaseClasses import ItemClassification

from .mapping_data import ability_tag_for_tromboner, music_note_tag_for_tromboner, song_tag_for_tromboner

from ..enums import (
    TromboneChampItems,
    TromboneChampNotes,
    TromboneChampSongs,
    TromboneChampTags,
    TromboneChampTromboners,
)


class TromboneChampItemData(NamedTuple):
    archipelago_id: Optional[int]
    classification: ItemClassification
    tags: Tuple[TromboneChampTags, ...]


item_offset: int = 0

item_data: Dict[str, TromboneChampItemData] = {
    # Victory and Goal Items
    TromboneChampItems.GOOD_JOB.value: TromboneChampItemData(
        archipelago_id=item_offset + 1,
        classification=ItemClassification.progression,
        tags=(TromboneChampTags.GOAL,),
    ),
    TromboneChampItems.GOLDEN_BABOON.value: TromboneChampItemData(
        archipelago_id=item_offset + 2,
        classification=ItemClassification.progression,
        tags=(TromboneChampTags.GOAL_GOLDEN_BABOONS_GOAL_SONG,),
    ),
    # Abilities
    TromboneChampItems.TURD_CRAFTING.value: TromboneChampItemData(
        archipelago_id=item_offset + 100 + 1,
        classification=ItemClassification.progression,
        tags=(TromboneChampTags.ABILITIES,),
    ),
    TromboneChampItems.TURDING.value: TromboneChampItemData(
        archipelago_id=item_offset + 100 + 2,
        classification=ItemClassification.progression,
        tags=(TromboneChampTags.ABILITIES,),
    ),
    TromboneChampItems.ENGOLDENATING.value: TromboneChampItemData(
        archipelago_id=item_offset + 100 + 3,
        classification=ItemClassification.progression,
        tags=(TromboneChampTags.ABILITIES,),
    ),
    # Filler
    TromboneChampItems.TOOTS_1.value: TromboneChampItemData(
        archipelago_id=item_offset + 1000 + 1,
        classification=ItemClassification.filler,
        tags=(TromboneChampTags.FILLER,),
    ),
    TromboneChampItems.TOOTS_5.value: TromboneChampItemData(
        archipelago_id=item_offset + 1000 + 2,
        classification=ItemClassification.filler,
        tags=(TromboneChampTags.FILLER,),
    ),
    TromboneChampItems.TOOTS_10.value: TromboneChampItemData(
        archipelago_id=item_offset + 1000 + 3,
        classification=ItemClassification.filler,
        tags=(TromboneChampTags.FILLER,),
    ),
    TromboneChampItems.TOOTS_20.value: TromboneChampItemData(
        archipelago_id=item_offset + 1000 + 4,
        classification=ItemClassification.filler,
        tags=(TromboneChampTags.FILLER,),
    ),
    TromboneChampItems.TOOTS_50.value: TromboneChampItemData(
        archipelago_id=item_offset + 1000 + 5,
        classification=ItemClassification.filler,
        tags=(TromboneChampTags.FILLER,),
    ),
    TromboneChampItems.TOOTS_100.value: TromboneChampItemData(
        archipelago_id=item_offset + 1000 + 6,
        classification=ItemClassification.filler,
        tags=(TromboneChampTags.FILLER,),
    ),
    TromboneChampItems.TOOTS_200.value: TromboneChampItemData(
        archipelago_id=item_offset + 1000 + 7,
        classification=ItemClassification.filler,
        tags=(TromboneChampTags.FILLER,),
    ),
    TromboneChampItems.TURDS_1.value: TromboneChampItemData(
        archipelago_id=item_offset + 1000 + 8,
        classification=ItemClassification.filler,
        tags=(TromboneChampTags.FILLER,),
    ),
    TromboneChampItems.TURDS_5.value: TromboneChampItemData(
        archipelago_id=item_offset + 1000 + 9,
        classification=ItemClassification.filler,
        tags=(TromboneChampTags.FILLER,),
    ),
    TromboneChampItems.TURDS_10.value: TromboneChampItemData(
        archipelago_id=item_offset + 1000 + 10,
        classification=ItemClassification.filler,
        tags=(TromboneChampTags.FILLER,),
    ),
    TromboneChampItems.TURDS_20.value: TromboneChampItemData(
        archipelago_id=item_offset + 1000 + 11,
        classification=ItemClassification.filler,
        tags=(TromboneChampTags.FILLER,),
    ),
    TromboneChampItems.TURDS_50.value: TromboneChampItemData(
        archipelago_id=item_offset + 1000 + 12,
        classification=ItemClassification.filler,
        tags=(TromboneChampTags.FILLER,),
    ),
    TromboneChampItems.TURDS_100.value: TromboneChampItemData(
        archipelago_id=item_offset + 1000 + 13,
        classification=ItemClassification.filler,
        tags=(TromboneChampTags.FILLER,),
    ),
    TromboneChampItems.TURDS_200.value: TromboneChampItemData(
        archipelago_id=item_offset + 1000 + 14,
        classification=ItemClassification.filler,
        tags=(TromboneChampTags.FILLER,),
    ),
}

# Tromboners
i: int
tromboner: TromboneChampTromboners
for i, tromboner in enumerate(TromboneChampTromboners):
    item_data[f"TROMBONER - {tromboner.value}"] = TromboneChampItemData(
        archipelago_id=item_offset + 500 + i,
        classification=ItemClassification.progression,
        tags=(TromboneChampTags.TROMBONERS,)
    )

# Items per Tromboner
item_offset = 1000000

i: int
tromboner: TromboneChampTromboners
for i, tromboner in enumerate(TromboneChampTromboners):
    tromboner_offset: int = 100000 * i

    # Songs
    song_offset: int = 10000

    ii: int
    song: TromboneChampSongs
    for ii, song in enumerate(TromboneChampSongs):
        item_data[f"SONG - {tromboner.value}: {song.value}"] = TromboneChampItemData(
            archipelago_id=item_offset + tromboner_offset + song_offset + ii,
            classification=ItemClassification.progression,
            tags=(
                TromboneChampTags.SONGS,
                song_tag_for_tromboner[tromboner],
            )
        )

    # Notes
    note_offset: int = 20000

    ii: int
    note: TromboneChampNotes
    for ii, note in enumerate(TromboneChampNotes):
        item_data[f"MUSIC NOTE - {tromboner.value}: {note.value}"] = TromboneChampItemData(
            archipelago_id=item_offset + tromboner_offset + note_offset + ii,
            classification=ItemClassification.progression,
            tags=(
                TromboneChampTags.MUSIC_NOTES,
                music_note_tag_for_tromboner[tromboner],
            )
        )

    # Abilities
    ability_offset: int = 30000

    item_data[f"{TromboneChampItems.TURBO_MODE} - {tromboner.value}"] = TromboneChampItemData(
        archipelago_id=item_offset + tromboner_offset + ability_offset + 0,
        classification=ItemClassification.progression,
        tags=(
            TromboneChampTags.ABILITIES,
            ability_tag_for_tromboner[tromboner],
        )
    )

    item_data[f"{TromboneChampItems.LICENSE_TO_TOOT.value} - {tromboner.value}"] = TromboneChampItemData(
        archipelago_id=item_offset + tromboner_offset + ability_offset + 1,
        classification=ItemClassification.progression,
        tags=(
            TromboneChampTags.ABILITIES,
            ability_tag_for_tromboner[tromboner],
        )
    )

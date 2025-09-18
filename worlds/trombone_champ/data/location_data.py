from typing import Dict, NamedTuple, Optional, Tuple, Union

from .mapping_data import (
    region_for_tromboner,
    song_clear_tag_for_tromboner,
    song_a_rank_tag_for_tromboner,
    song_b_rank_tag_for_tromboner,
    song_c_rank_tag_for_tromboner,
    song_s_rank_tag_for_tromboner,
    song_turbo_mode_tag_for_tromboner,
)

from ..song_funcs import notes_required_for_rank_and_tromboner

from ..enums import (
    TromboneChampItems,
    TromboneChampRegions,
    TromboneChampSongs,
    TromboneChampTags,
    TromboneChampTromboners,
    TromboneChampTrombonerCards,
)


class TromboneChampLocationData(NamedTuple):
    archipelago_id: Optional[int]
    region: TromboneChampRegions
    tags: Optional[Tuple[TromboneChampTags, ...]] = None
    requirements: Optional[
        Union[
            str,
            Tuple[str, ...],
        ]
    ] = None


location_offset: int = 1000000

location_data: Dict[str, TromboneChampLocationData] = dict()

# Locations per Tromboner
i: int
tromboner: TromboneChampTromboners
for i, tromboner in enumerate(TromboneChampTromboners):
    tromboner_offset: int = 100000 * i

    # Song Clears
    song_clear_offset: int = 1000

    ii: int
    song: TromboneChampSongs
    for ii, song in enumerate(TromboneChampSongs):
        location_data[f"{tromboner.value} - {song.value} Clear!"] = TromboneChampLocationData(
            archipelago_id=location_offset + tromboner_offset + song_clear_offset + ii,
            region=region_for_tromboner[tromboner],
            tags=(
                TromboneChampTags.SONG_CLEARS,
                song_clear_tag_for_tromboner[tromboner],
            ),
            requirements=(
                f"SONG - {tromboner.value}: {song.value}",
            )
        )

    # Song Clears (Extra)
    song_clear_offset: int = 2000

    ii: int
    song: TromboneChampSongs
    for ii, song in enumerate(TromboneChampSongs):
        location_data[f"{tromboner.value} - {song.value} Clear! (Extra)"] = TromboneChampLocationData(
            archipelago_id=location_offset + tromboner_offset + song_clear_offset + ii,
            region=region_for_tromboner[tromboner],
            tags=(
                TromboneChampTags.SONG_CLEARS,
                song_clear_tag_for_tromboner[tromboner],
            ),
            requirements=(
                f"SONG - {tromboner.value}: {song.value}",
            )
        )

    # Song C Ranks
    song_c_ranks_offset: int = 3000

    ii: int
    song: TromboneChampSongs
    for ii, song in enumerate(TromboneChampSongs):
        location_data[f"{tromboner.value} - {song.value} C Rank!"] = TromboneChampLocationData(
            archipelago_id=location_offset + tromboner_offset + song_c_ranks_offset + ii,
            region=region_for_tromboner[tromboner],
            tags=(
                TromboneChampTags.SONG_C_RANKS,
                song_c_rank_tag_for_tromboner[tromboner],
            ),
            requirements=tuple(
                [
                    f"SONG - {tromboner.value}: {song.value}",
                    *notes_required_for_rank_and_tromboner("C", song, tromboner)
                ]
            )
        )

    # Song B Ranks
    song_b_ranks_offset: int = 4000

    ii: int
    song: TromboneChampSongs
    for ii, song in enumerate(TromboneChampSongs):
        location_data[f"{tromboner.value} - {song.value} B Rank!"] = TromboneChampLocationData(
            archipelago_id=location_offset + tromboner_offset + song_b_ranks_offset + ii,
            region=region_for_tromboner[tromboner],
            tags=(
                TromboneChampTags.SONG_B_RANKS,
                song_b_rank_tag_for_tromboner[tromboner],
            ),
            requirements=tuple(
                [
                    f"SONG - {tromboner.value}: {song.value}",
                    *notes_required_for_rank_and_tromboner("B", song, tromboner)
                ]
            )
        )

    # Song A Ranks
    song_a_ranks_offset: int = 5000

    ii: int
    song: TromboneChampSongs
    for ii, song in enumerate(TromboneChampSongs):
        location_data[f"{tromboner.value} - {song.value} A Rank!"] = TromboneChampLocationData(
            archipelago_id=location_offset + tromboner_offset + song_a_ranks_offset + ii,
            region=region_for_tromboner[tromboner],
            tags=(
                TromboneChampTags.SONG_A_RANKS,
                song_a_rank_tag_for_tromboner[tromboner],
            ),
            requirements=tuple(
                [
                    f"SONG - {tromboner.value}: {song.value}",
                    *notes_required_for_rank_and_tromboner("A", song, tromboner)
                ]
            )
        )

    # Song S Ranks
    song_s_ranks_offset: int = 6000

    ii: int
    song: TromboneChampSongs
    for ii, song in enumerate(TromboneChampSongs):
        location_data[f"{tromboner.value} - {song.value} S Rank!"] = TromboneChampLocationData(
            archipelago_id=location_offset + tromboner_offset + song_s_ranks_offset + ii,
            region=region_for_tromboner[tromboner],
            tags=(
                TromboneChampTags.SONG_S_RANKS,
                song_s_rank_tag_for_tromboner[tromboner],
            ),
            requirements=tuple(
                [
                    f"SONG - {tromboner.value}: {song.value}",
                    *notes_required_for_rank_and_tromboner("S", song, tromboner)
                ]
            )
        )

    # Song Turbo Modes
    song_turbo_modes_offset: int = 7000

    ii: int
    song: TromboneChampSongs
    for ii, song in enumerate(TromboneChampSongs):
        location_data[f"{tromboner.value} - {song.value} Turbo Mode!"] = TromboneChampLocationData(
            archipelago_id=location_offset + tromboner_offset + song_turbo_modes_offset + ii,
            region=region_for_tromboner[tromboner],
            tags=(
                TromboneChampTags.SONG_TURBO_MODES,
                song_turbo_mode_tag_for_tromboner[tromboner],
            ),
            requirements=(
                f"SONG - {tromboner.value}: {song.value}",
                f"{TromboneChampItems.TURBO_MODE.value} - {tromboner.value}"
            )
        )

# Tromboner Card Locations
location_offset = 2000000

license_to_toot_items: Tuple[str, ...] = tuple(sorted([
    f"{TromboneChampItems.LICENSE_TO_TOOT.value} - {tromboner.value}" for tromboner in TromboneChampTromboners
]))

# Cardsanity
collecting_offset: int = 1000

i: int
tromboner_card: TromboneChampTrombonerCards
for i, tromboner_card in enumerate(TromboneChampTrombonerCards):
    location_data[f"Collect Tromboner Card: {tromboner_card.value}"] = TromboneChampLocationData(
        archipelago_id=location_offset + collecting_offset + i,
        region=TromboneChampRegions.CARD_COLLECTION,
        tags=(TromboneChampTags.CARDSANITY,),
        requirements=(license_to_toot_items,),
    )

# Turdsanity
turding_offset: int = 2000

i: int
tromboner_card: TromboneChampTrombonerCards
for i, tromboner_card in enumerate(TromboneChampTrombonerCards):
    location_data[f"Turd Tromboner Card: {tromboner_card.value}"] = TromboneChampLocationData(
        archipelago_id=location_offset + turding_offset + i,
        region=TromboneChampRegions.CARD_COLLECTION,
        tags=(TromboneChampTags.TURDSANITY,),
        requirements=(
            license_to_toot_items,
            TromboneChampItems.TURDING,
        ),
    )

# Craftsanity
crafting_offset: int = 3000

i: int
tromboner_card: TromboneChampTrombonerCards
for i, tromboner_card in enumerate(TromboneChampTrombonerCards):
    location_data[f"Craft Tromboner Card: {tromboner_card.value}"] = TromboneChampLocationData(
        archipelago_id=location_offset + crafting_offset + i,
        region=TromboneChampRegions.CARD_COLLECTION,
        tags=(TromboneChampTags.CRAFTSANITY,),
        requirements=(
            license_to_toot_items,
            TromboneChampItems.TURD_CRAFTING,
        ),
    )

# Engoldenatesanity
engoldenating_offset: int = 4000

i: int
tromboner_card: TromboneChampTrombonerCards
for i, tromboner_card in enumerate(TromboneChampTrombonerCards):
    location_data[f"Engoldenate Tromboner Card: {tromboner_card.value}"] = TromboneChampLocationData(
        archipelago_id=location_offset + engoldenating_offset + i,
        region=TromboneChampRegions.CARD_COLLECTION,
        tags=(TromboneChampTags.ENGOLDENATESANITY,),
        requirements=(
            license_to_toot_items,
            TromboneChampItems.ENGOLDENATING,
        ),
    )

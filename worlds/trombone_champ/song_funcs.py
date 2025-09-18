from typing import List, Set, Tuple

from .data.song_data import TromboneChampSongData, song_data
from .data.mapping_data import note_requirement_for_rank

from .enums import TromboneChampNotes, TromboneChampSongs, TromboneChampTromboners


def notes_required_for_rank(rank: str, song: TromboneChampSongs) -> List[TromboneChampNotes]:
    note_requirement: float = note_requirement_for_rank.get(rank, 1.0)

    note_data: TromboneChampSongData = song_data[song]

    total_note_count: int = sum(note_data.note_counts.values())
    required_note_count: int = round(note_requirement * total_note_count)

    running_note_count: int = 0
    required_notes: List[TromboneChampNotes] = list()

    note: TromboneChampNotes
    count: int
    for note, count in sorted(note_data.note_counts.items(), key=lambda x: (-x[1], x[0].value)):
        running_note_count += count
        required_notes.append(note)

        if running_note_count >= required_note_count:
            break

    return required_notes


def notes_required_for_rank_and_tromboner(
    rank: str, song: TromboneChampSongs, tromboner: TromboneChampTromboners
) -> List[str]:
    notes: List[TromboneChampNotes] = notes_required_for_rank(rank, song)

    return sorted([f"MUSIC NOTE - {tromboner.value}: {note.value}" for note in notes])


def notes_required_for_starting_songs(
    starting_songs: List[Tuple[TromboneChampTromboners, TromboneChampSongs]]
) -> List[str]:
    required_notes: Set[str] = set()

    tromboner: TromboneChampTromboners
    song: TromboneChampSongs
    for tromboner, song in starting_songs:
        required_note: str
        for required_note in notes_required_for_rank_and_tromboner("B", song, tromboner):
            required_notes.add(required_note)

    return sorted(list(required_notes))

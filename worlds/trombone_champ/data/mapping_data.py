from typing import Dict

from ..enums import TromboneChampRegions, TromboneChampTags, TromboneChampTromboners


ability_tag_for_tromboner: Dict[TromboneChampTromboners, TromboneChampTags] = {
    TromboneChampTromboners.APPALOOSA: TromboneChampTags.ABILITIES_APPALOOSA,
    TromboneChampTromboners.BEEZERLY: TromboneChampTags.ABILITIES_BEEZERLY,
    TromboneChampTromboners.HORN_LORD: TromboneChampTags.ABILITIES_HORN_LORD,
    TromboneChampTromboners.JERMAJESTY: TromboneChampTags.ABILITIES_JERMAJESTY,
    TromboneChampTromboners.KAIZYLE_II: TromboneChampTags.ABILITIES_KAIZYLE_II,
    TromboneChampTromboners.MELDOR: TromboneChampTags.ABILITIES_MELDOR,
    TromboneChampTromboners.POLYGON: TromboneChampTags.ABILITIES_POLYGON,
    TromboneChampTromboners.SERVANT_OF_BABI: TromboneChampTags.ABILITIES_SERVANT_OF_BABI,
    TromboneChampTromboners.SODA: TromboneChampTags.ABILITIES_SODA,
    TromboneChampTromboners.TRIXIEBELL: TromboneChampTags.ABILITIES_TRIXIEBELL,
}

music_note_tag_for_tromboner: Dict[TromboneChampTromboners, TromboneChampTags] = {
    TromboneChampTromboners.APPALOOSA: TromboneChampTags.MUSIC_NOTES_APPALOOSA,
    TromboneChampTromboners.BEEZERLY: TromboneChampTags.MUSIC_NOTES_BEEZERLY,
    TromboneChampTromboners.HORN_LORD: TromboneChampTags.MUSIC_NOTES_HORN_LORD,
    TromboneChampTromboners.JERMAJESTY: TromboneChampTags.MUSIC_NOTES_JERMAJESTY,
    TromboneChampTromboners.KAIZYLE_II: TromboneChampTags.MUSIC_NOTES_KAIZYLE_II,
    TromboneChampTromboners.MELDOR: TromboneChampTags.MUSIC_NOTES_MELDOR,
    TromboneChampTromboners.POLYGON: TromboneChampTags.MUSIC_NOTES_POLYGON,
    TromboneChampTromboners.SERVANT_OF_BABI: TromboneChampTags.MUSIC_NOTES_SERVANT_OF_BABI,
    TromboneChampTromboners.SODA: TromboneChampTags.MUSIC_NOTES_SODA,
    TromboneChampTromboners.TRIXIEBELL: TromboneChampTags.MUSIC_NOTES_TRIXIEBELL,
}

note_requirement_for_rank: Dict[str, float] = {
    "C": 0.5,
    "B": 0.7,
    "A": 0.85,
    "S": 0.95,
}

region_for_tromboner: Dict[TromboneChampTromboners, TromboneChampRegions] = {
    TromboneChampTromboners.APPALOOSA: TromboneChampRegions.TROMBONER_APPALOOSA,
    TromboneChampTromboners.BEEZERLY: TromboneChampRegions.TROMBONER_BEEZERLY,
    TromboneChampTromboners.HORN_LORD: TromboneChampRegions.TROMBONER_HORN_LORD,
    TromboneChampTromboners.JERMAJESTY: TromboneChampRegions.TROMBONER_JERMAJESTY,
    TromboneChampTromboners.KAIZYLE_II: TromboneChampRegions.TROMBONER_KAIZYLE_II,
    TromboneChampTromboners.MELDOR: TromboneChampRegions.TROMBONER_MELDOR,
    TromboneChampTromboners.POLYGON: TromboneChampRegions.TROMBONER_POLYGON,
    TromboneChampTromboners.SERVANT_OF_BABI: TromboneChampRegions.TROMBONER_SERVANT_OF_BABI,
    TromboneChampTromboners.SODA: TromboneChampRegions.TROMBONER_SODA,
    TromboneChampTromboners.TRIXIEBELL: TromboneChampRegions.TROMBONER_TRIXIEBELL,
}

song_a_rank_tag_for_tromboner: Dict[TromboneChampTromboners, TromboneChampTags] = {
    TromboneChampTromboners.APPALOOSA: TromboneChampTags.SONG_A_RANKS_APPALOOSA,
    TromboneChampTromboners.BEEZERLY: TromboneChampTags.SONG_A_RANKS_BEEZERLY,
    TromboneChampTromboners.HORN_LORD: TromboneChampTags.SONG_A_RANKS_HORN_LORD,
    TromboneChampTromboners.JERMAJESTY: TromboneChampTags.SONG_A_RANKS_JERMAJESTY,
    TromboneChampTromboners.KAIZYLE_II: TromboneChampTags.SONG_A_RANKS_KAIZYLE_II,
    TromboneChampTromboners.MELDOR: TromboneChampTags.SONG_A_RANKS_MELDOR,
    TromboneChampTromboners.POLYGON: TromboneChampTags.SONG_A_RANKS_POLYGON,
    TromboneChampTromboners.SERVANT_OF_BABI: TromboneChampTags.SONG_A_RANKS_SERVANT_OF_BABI,
    TromboneChampTromboners.SODA: TromboneChampTags.SONG_A_RANKS_SODA,
    TromboneChampTromboners.TRIXIEBELL: TromboneChampTags.SONG_A_RANKS_TRIXIEBELL,
}

song_b_rank_tag_for_tromboner: Dict[TromboneChampTromboners, TromboneChampTags] = {
    TromboneChampTromboners.APPALOOSA: TromboneChampTags.SONG_B_RANKS_APPALOOSA,
    TromboneChampTromboners.BEEZERLY: TromboneChampTags.SONG_B_RANKS_BEEZERLY,
    TromboneChampTromboners.HORN_LORD: TromboneChampTags.SONG_B_RANKS_HORN_LORD,
    TromboneChampTromboners.JERMAJESTY: TromboneChampTags.SONG_B_RANKS_JERMAJESTY,
    TromboneChampTromboners.KAIZYLE_II: TromboneChampTags.SONG_B_RANKS_KAIZYLE_II,
    TromboneChampTromboners.MELDOR: TromboneChampTags.SONG_B_RANKS_MELDOR,
    TromboneChampTromboners.POLYGON: TromboneChampTags.SONG_B_RANKS_POLYGON,
    TromboneChampTromboners.SERVANT_OF_BABI: TromboneChampTags.SONG_B_RANKS_SERVANT_OF_BABI,
    TromboneChampTromboners.SODA: TromboneChampTags.SONG_B_RANKS_SODA,
    TromboneChampTromboners.TRIXIEBELL: TromboneChampTags.SONG_B_RANKS_TRIXIEBELL,
}

song_c_rank_tag_for_tromboner: Dict[TromboneChampTromboners, TromboneChampTags] = {
    TromboneChampTromboners.APPALOOSA: TromboneChampTags.SONG_C_RANKS_APPALOOSA,
    TromboneChampTromboners.BEEZERLY: TromboneChampTags.SONG_C_RANKS_BEEZERLY,
    TromboneChampTromboners.HORN_LORD: TromboneChampTags.SONG_C_RANKS_HORN_LORD,
    TromboneChampTromboners.JERMAJESTY: TromboneChampTags.SONG_C_RANKS_JERMAJESTY,
    TromboneChampTromboners.KAIZYLE_II: TromboneChampTags.SONG_C_RANKS_KAIZYLE_II,
    TromboneChampTromboners.MELDOR: TromboneChampTags.SONG_C_RANKS_MELDOR,
    TromboneChampTromboners.POLYGON: TromboneChampTags.SONG_C_RANKS_POLYGON,
    TromboneChampTromboners.SERVANT_OF_BABI: TromboneChampTags.SONG_C_RANKS_SERVANT_OF_BABI,
    TromboneChampTromboners.SODA: TromboneChampTags.SONG_C_RANKS_SODA,
    TromboneChampTromboners.TRIXIEBELL: TromboneChampTags.SONG_C_RANKS_TRIXIEBELL,
}

song_s_rank_tag_for_tromboner: Dict[TromboneChampTromboners, TromboneChampTags] = {
    TromboneChampTromboners.APPALOOSA: TromboneChampTags.SONG_S_RANKS_APPALOOSA,
    TromboneChampTromboners.BEEZERLY: TromboneChampTags.SONG_S_RANKS_BEEZERLY,
    TromboneChampTromboners.HORN_LORD: TromboneChampTags.SONG_S_RANKS_HORN_LORD,
    TromboneChampTromboners.JERMAJESTY: TromboneChampTags.SONG_S_RANKS_JERMAJESTY,
    TromboneChampTromboners.KAIZYLE_II: TromboneChampTags.SONG_S_RANKS_KAIZYLE_II,
    TromboneChampTromboners.MELDOR: TromboneChampTags.SONG_S_RANKS_MELDOR,
    TromboneChampTromboners.POLYGON: TromboneChampTags.SONG_S_RANKS_POLYGON,
    TromboneChampTromboners.SERVANT_OF_BABI: TromboneChampTags.SONG_S_RANKS_SERVANT_OF_BABI,
    TromboneChampTromboners.SODA: TromboneChampTags.SONG_S_RANKS_SODA,
    TromboneChampTromboners.TRIXIEBELL: TromboneChampTags.SONG_S_RANKS_TRIXIEBELL,
}

song_clear_tag_for_tromboner: Dict[TromboneChampTromboners, TromboneChampTags] = {
    TromboneChampTromboners.APPALOOSA: TromboneChampTags.SONG_CLEARS_APPALOOSA,
    TromboneChampTromboners.BEEZERLY: TromboneChampTags.SONG_CLEARS_BEEZERLY,
    TromboneChampTromboners.HORN_LORD: TromboneChampTags.SONG_CLEARS_HORN_LORD,
    TromboneChampTromboners.JERMAJESTY: TromboneChampTags.SONG_CLEARS_JERMAJESTY,
    TromboneChampTromboners.KAIZYLE_II: TromboneChampTags.SONG_CLEARS_KAIZYLE_II,
    TromboneChampTromboners.MELDOR: TromboneChampTags.SONG_CLEARS_MELDOR,
    TromboneChampTromboners.POLYGON: TromboneChampTags.SONG_CLEARS_POLYGON,
    TromboneChampTromboners.SERVANT_OF_BABI: TromboneChampTags.SONG_CLEARS_SERVANT_OF_BABI,
    TromboneChampTromboners.SODA: TromboneChampTags.SONG_CLEARS_SODA,
    TromboneChampTromboners.TRIXIEBELL: TromboneChampTags.SONG_CLEARS_TRIXIEBELL,
}

song_tag_for_tromboner: Dict[TromboneChampTromboners, TromboneChampTags] = {
    TromboneChampTromboners.APPALOOSA: TromboneChampTags.SONGS_APPALOOSA,
    TromboneChampTromboners.BEEZERLY: TromboneChampTags.SONGS_BEEZERLY,
    TromboneChampTromboners.HORN_LORD: TromboneChampTags.SONGS_HORN_LORD,
    TromboneChampTromboners.JERMAJESTY: TromboneChampTags.SONGS_JERMAJESTY,
    TromboneChampTromboners.KAIZYLE_II: TromboneChampTags.SONGS_KAIZYLE_II,
    TromboneChampTromboners.MELDOR: TromboneChampTags.SONGS_MELDOR,
    TromboneChampTromboners.POLYGON: TromboneChampTags.SONGS_POLYGON,
    TromboneChampTromboners.SERVANT_OF_BABI: TromboneChampTags.SONGS_SERVANT_OF_BABI,
    TromboneChampTromboners.SODA: TromboneChampTags.SONGS_SODA,
    TromboneChampTromboners.TRIXIEBELL: TromboneChampTags.SONGS_TRIXIEBELL,
}

song_turbo_mode_tag_for_tromboner: Dict[TromboneChampTromboners, TromboneChampTags] = {
    TromboneChampTromboners.APPALOOSA: TromboneChampTags.SONG_TURBO_MODES_APPALOOSA,
    TromboneChampTromboners.BEEZERLY: TromboneChampTags.SONG_TURBO_MODES_BEEZERLY,
    TromboneChampTromboners.HORN_LORD: TromboneChampTags.SONG_TURBO_MODES_HORN_LORD,
    TromboneChampTromboners.JERMAJESTY: TromboneChampTags.SONG_TURBO_MODES_JERMAJESTY,
    TromboneChampTromboners.KAIZYLE_II: TromboneChampTags.SONG_TURBO_MODES_KAIZYLE_II,
    TromboneChampTromboners.MELDOR: TromboneChampTags.SONG_TURBO_MODES_MELDOR,
    TromboneChampTromboners.POLYGON: TromboneChampTags.SONG_TURBO_MODES_POLYGON,
    TromboneChampTromboners.SERVANT_OF_BABI: TromboneChampTags.SONG_TURBO_MODES_SERVANT_OF_BABI,
    TromboneChampTromboners.SODA: TromboneChampTags.SONG_TURBO_MODES_SODA,
    TromboneChampTromboners.TRIXIEBELL: TromboneChampTags.SONG_TURBO_MODES_TRIXIEBELL,
}

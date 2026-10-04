from typing import Dict

from ..enums import DrMarioColors, DrMarioModes, DrMarioMusicTracks, DrMarioMusicTypes, DrMarioSpeeds


ram_addresses: Dict[str, int] = {
    "buttons_held_player_1": 0x00F7,
    "buttons_held_player_2": 0x00F8,
    "buttons_pressed_player_1": 0x00F5,
    "buttons_pressed_player_2": 0x00F6,
    "demo_flag": 0x0741,
    "frame_animation_enabled": 0x005D,
    "frame_counter": 0x0043,
    "last_pill_chains": 0x03B0,
    "mode": 0x0046,
    "music_track": 0x06FD,
    "music_type": 0x0731,
    "number_of_players": 0x0727,
    "options_cursor_row": 0x0065,
    "options_redraw_flags": 0x0068,
    "pause_enabled": 0x0054,
    "pill_list": 0x0780,
    "ppu_mask": 0x00FE,
    "saved_level": 0x073C,
    "saved_music_type": 0x073F,
    "saved_number_of_players": 0x073E,
    "saved_speed": 0x073D,
    "score_digits": 0x0729,
    "secondary_sound_request": 0x06F5,
    "sound_effect_request": 0x06F1,
    "status_redraw_flags": 0x0052,
    "tamper_flag": 0x0740,
    "top_score_digits": 0x0700,
    "virus_color_animation_frames": 0x0078,
    "virus_color_counts": 0x0072,
    "virus_color_states": 0x0075,
}

player_block_addresses: Dict[str, int] = {
    "active": 0x0080,
    "player_1": 0x0300,
    "player_2": 0x0380,
}

player_block_offsets: Dict[str, int] = {
    "garbage_count": 0x18,
    "last_line_extra_cells": 0x0E,
    "last_pill_cells_cleared": 0x21,
    "last_pill_line_colors": 0x29,
    "last_pill_lines_cleared": 0x0F,
    "last_pill_viruses_destroyed": 0x2D,
    "level": 0x16,
    "next_pill_left_color": 0x1A,
    "next_pill_right_color": 0x1B,
    "pill_count": 0x10,
    "pill_count_hundreds": 0x11,
    "pill_left_color": 0x01,
    "pill_list_index": 0x27,
    "pill_phase": 0x17,
    "pill_right_color": 0x02,
    "pill_rotation": 0x25,
    "pill_x": 0x05,
    "pill_y": 0x06,
    "playfield_redraw_row": 0x00,
    "speed": 0x0B,
    "speed_ups": 0x0A,
    "topped_out": 0x09,
    "viruses_remaining": 0x24,
    "viruses_to_place": 0x28,
}

playfield_addresses: Dict[str, int] = {
    "player_1": 0x0400,
    "player_2": 0x0500,
}

playfield_tiles: Dict[str, int] = {
    "empty": 0xFF,
    "garbage": 0x90,
    "single": 0x80,
    "virus_blue": 0xD2,
    "virus_red": 0xD1,
    "virus_yellow": 0xD0,
}

mode_to_internal_mode_id: Dict[DrMarioModes, int] = {
    DrMarioModes.GAME_OVER: 7,
    DrMarioModes.LEVEL_SETUP: 2,
    DrMarioModes.OPTIONS: 1,
    DrMarioModes.PLAYER_SETUP: 3,
    DrMarioModes.PLAYING: 4,
    DrMarioModes.ROUND_END: 5,
    DrMarioModes.TITLE: 0,
    DrMarioModes.VIRUS_PLACEMENT: 8,
}

internal_mode_id_to_mode: Dict[int, DrMarioModes] = {
    internal_mode_id: mode for mode, internal_mode_id in mode_to_internal_mode_id.items()
}

speed_to_internal_speed_id: Dict[DrMarioSpeeds, int] = {
    DrMarioSpeeds.HIGH: 2,
    DrMarioSpeeds.LOW: 0,
    DrMarioSpeeds.MEDIUM: 1,
}

internal_speed_id_to_speed: Dict[int, DrMarioSpeeds] = {
    internal_speed_id: speed for speed, internal_speed_id in speed_to_internal_speed_id.items()
}

music_type_to_internal_music_type_id: Dict[DrMarioMusicTypes, int] = {
    DrMarioMusicTypes.CHILL: 1,
    DrMarioMusicTypes.FEVER: 0,
    DrMarioMusicTypes.OFF: 2,
}

internal_music_type_id_to_music_type: Dict[int, DrMarioMusicTypes] = {
    internal_music_type_id: music_type for music_type, internal_music_type_id in music_type_to_internal_music_type_id.items()
}

music_track_to_internal_music_track_id: Dict[DrMarioMusicTracks, int] = {
    DrMarioMusicTracks.CHILL: 2,
    DrMarioMusicTracks.CHILL_LEVEL_CLEAR: 10,
    DrMarioMusicTracks.CUTSCENE: 1,
    DrMarioMusicTracks.FEVER: 4,
    DrMarioMusicTracks.GAME_OVER: 5,
    DrMarioMusicTracks.LEVEL_CLEAR: 9,
    DrMarioMusicTracks.LEVEL_TWENTY_LOW_CLEAR: 8,
    DrMarioMusicTracks.OPTIONS: 7,
    DrMarioMusicTracks.SILENCE: 3,
    DrMarioMusicTracks.TITLE: 6,
    DrMarioMusicTracks.TWO_PLAYER_VICTORY: 11,
}

color_to_internal_color_id: Dict[DrMarioColors, int] = {
    DrMarioColors.BLUE: 2,
    DrMarioColors.RED: 1,
    DrMarioColors.YELLOW: 0,
}

internal_color_id_to_color: Dict[int, DrMarioColors] = {
    internal_color_id: color for color, internal_color_id in color_to_internal_color_id.items()
}

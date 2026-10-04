from typing import Dict, Tuple


rom_addresses: Dict[str, int] = {
    "checkerboard_speed_colors": 0xA244,
    "clear_check": 0xB269,
    "clear_level_up": 0xB2D9,
    "clear_music_table": 0xA27B,
    "clear_start_wait": 0xB2FE,
    "cutscene_selection": 0x9E66,
    "cutscene_table": 0xA012,
    "demo_pill_list": 0xCF80,
    "fix_up_middle_segment": 0x9392,
    "frame_wait": 0xB66E,
    "frame_wait_sound_call": 0xB675,
    "landing_resolve_loop": 0x941E,
    "landing_start": 0x8C9C,
    "garbage_drop": 0x9C1B,
    "garbage_drop_player_count_check": 0x9BEE,
    "gameplay_magnifier_lower_tile": 0xC40A,
    "gameplay_magnifier_upper_tiles": 0xC3E8,
    "match_length_horizontal": 0x9251,
    "match_length_vertical": 0x94B7,
    "match_start_column_limit": 0x92C6,
    "match_start_row_limit": 0x952A,
    "mode_dispatch": 0x8167,
    "mode_handler_table": 0x816C,
    "music_track_header_offsets": 0xE261,
    "next_pill_preview_call": 0x87DC,
    "next_pill_selection": 0x8EB1,
    "nmi_handler": 0x8005,
    "options_level_adjust": 0x9B0C,
    "options_level_bar_lower_tiles": 0xBF49,
    "options_level_bar_tiles": 0xBF26,
    "options_level_clamp": 0x999C,
    "options_level_row_attributes": 0xA2D2,
    "options_music_adjust": 0x9A51,
    "options_music_row_attributes": 0xA360,
    "options_palette": 0xA5D0,
    "options_speed_adjust": 0x9B37,
    "options_speed_row_attributes": 0xA319,
    "pause_routine": 0x97B3,
    "pause_start_check": 0x97E5,
    "pill_phase_dispatch": 0x9BD3,
    "pill_left_color_table": 0xA817,
    "pill_right_color_table": 0xA820,
    "player_2_virus_count_setup": 0x8294,
    "playing_palette": 0xA588,
    "playing_palette_copy": 0xA5F4,
    "read_controllers": 0xB7AD,
    "reset_handler": 0xFF00,
    "score_add": 0x9004,
    "sound_update": 0xFFD0,
    "spawn_or_top_out": 0x9FE7,
    "speed_up_cap": 0x8F45,
    "splash_palette": 0xA5AC,
    "tamper_checksum": 0x91E0,
    "tamper_trap": 0x8DBF,
    "virus_count_setup": 0x827D,
    "virus_destroyed": 0x9441,
    "virus_placement": 0x9D19,
    "virus_placement_max_rows": 0xA3F8,
}

gameplay_chr_banks: Tuple[int, ...] = (0x0000, 0x1000)

relocated_magnifier_tiles: Tuple[int, ...] = (0x68, 0x89, 0x9C)

garbage_drop_pellet_operands: Tuple[int, ...] = (0x9C37, 0x9C42, 0x9C55, 0x9C5E, 0x9C67, 0x9C76, 0x9C7F, 0x9C88, 0x9C91)

options_chr_bank: int = 0x5000

options_chr_tile_allocations: Dict[str, int] = {
    "level_bar_tiles": 0xC0,
}

free_space_allocations: Dict[str, int] = {
    "last_pill_chains_code": 0xFBC2,
    "level_unlock_table": 0xFB20,
    "music_type_unlock_table": 0xFB38,
    "option_step_code": 0xFB40,
    "pause_select_code": 0xFBD2,
    "speed_unlock_table": 0xFB35,
    "virus_count_table": 0xFBF1,
}

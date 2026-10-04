from typing import Dict, List, NamedTuple, Optional, Set, Tuple

import random
import struct

from pymem import Pymem
from pymem.process import close_handle, list_processes
from pymem.ressources.structure import ProcessEntry32

from .data.ram_data import (
    color_to_internal_color_id,
    internal_color_id_to_color,
    internal_mode_id_to_mode,
    internal_music_type_id_to_music_type,
    internal_speed_id_to_speed,
    music_track_to_internal_music_track_id,
    music_type_to_internal_music_type_id,
    player_block_addresses,
    player_block_offsets,
    playfield_addresses,
    playfield_tiles,
    ram_addresses,
    speed_to_internal_speed_id,
)

from .data.rom_data import (
    free_space_allocations,
    gameplay_chr_banks,
    garbage_drop_pellet_operands,
    options_chr_bank,
    options_chr_tile_allocations,
    relocated_magnifier_tiles,
    rom_addresses,
)

from .enums import DrMarioColors, DrMarioInputEffects, DrMarioModes, DrMarioMusicTracks, DrMarioMusicTypes, DrMarioNesColors, DrMarioPaletteRegions, DrMarioSpeeds

from .mesen import ARGUMENT_BUFFER_SIZE, MEMORY_TYPES, WRITE_DATA_SIZE, WRITE_RECORD_CAPACITY, MesenNesProcess, assemble_6502


def build_option_step_code(address: int, value_address: int, table_address: int, value_count: int, is_right: bool, redraws_level_digits: bool) -> bytes:
    is_zero_page: bool = value_address < 0x100

    step: List = [
        b"\xE8",  # inx
        b"\xE0" + bytes([value_count]),  # cpx #value count
        ("branch", b"\xB0", "done"),  # bcs done
    ] if is_right else [
        b"\xCA",  # dex
        ("branch", b"\x30", "done"),  # bmi done
    ]

    redraw: List = [
        b"\xA5\x68",  # lda $68
        b"\x09\x04",  # ora #$04
        b"\x85\x68",  # sta $68
    ] if redraws_level_digits else []

    return assemble_6502([
        b"\xA6" + bytes([value_address]) if is_zero_page else b"\xAE" + struct.pack("<H", value_address),  # ldx value
        ("label", "next"),
        *step,
        b"\xBD" + struct.pack("<H", table_address),  # lda unlock table,x
        ("branch", b"\xF0", "next"),  # beq next
        b"\x86" + bytes([value_address]) if is_zero_page else b"\x8E" + struct.pack("<H", value_address),  # stx value
        b"\xA9\x03",  # lda #$03
        b"\x8D\xF1\x06",  # sta $06F1  ; click
        *redraw,
        ("label", "done"),
        b"\x60",  # rts
    ], address)


class GameState(NamedTuple):
    is_valid: bool

    mode: Optional[DrMarioModes] = None

    is_on_splash: Optional[bool] = None
    is_in_demo: Optional[bool] = None
    is_paused: Optional[bool] = None
    is_between_levels: Optional[bool] = None
    is_pill_falling: Optional[bool] = None
    is_before_first_pill: Optional[bool] = None

    level: Optional[int] = None
    speed: Optional[DrMarioSpeeds] = None
    speed_ups: Optional[int] = None
    music_type: Optional[DrMarioMusicTypes] = None

    viruses_remaining: Optional[int] = None
    virus_counts: Optional[Dict[DrMarioColors, int]] = None
    is_topped_out: Optional[bool] = None
    pills_used: Optional[int] = None

    last_pill_viruses_destroyed: Optional[int] = None
    last_pill_lines_cleared: Optional[int] = None
    last_pill_line_colors: Optional[Tuple[DrMarioColors, ...]] = None
    last_pill_chains: Optional[int] = None


class GameStateManager:
    process_name: str = "mesen.exe"
    prg_chr_crc32: int = 0xDE581355
    smiley_cells: Tuple[Tuple[int, int], ...] = ((0, 2), (0, 5), (2, 0), (2, 7), (3, 1), (3, 6), (4, 2), (4, 3), (4, 4), (4, 5))

    process: Optional[Pymem]
    is_process_running: bool

    mesen: Optional[MesenNesProcess]

    pending_writes: List[Tuple[int, int, bytes]]
    applied_input_effects: List[DrMarioInputEffects]

    original_pill_list: Optional[bytes]
    restricted_pill_list: Optional[bytes]

    game_state: Optional[GameState]

    def __init__(self) -> None:
        self.process = None
        self.is_process_running = False

        self.mesen = None

        self.pending_writes = list()
        self.applied_input_effects = list()

        self.original_pill_list = None
        self.restricted_pill_list = None

        self.game_state = GameState(is_valid=False)

    def open_process_handle(self) -> bool:
        try:
            candidate_process_ids: List[int] = list()

            process_entry: ProcessEntry32
            for process_entry in list_processes():
                if process_entry.szExeFile.decode("utf-8", errors="replace").lower() == self.process_name:
                    candidate_process_ids.append(process_entry.th32ProcessID)

            if not len(candidate_process_ids):
                return False

            process_id: int
            for process_id in candidate_process_ids:
                try:
                    process: Pymem = Pymem(process_id)
                except Exception:
                    continue

                try:
                    mesen: MesenNesProcess = MesenNesProcess(process)

                    if mesen.is_nes_game_running() and mesen.read_rom_hashes()["PrgChrCrc32"] == self.prg_chr_crc32:
                        self.process = process
                        self.mesen = mesen

                        break
                except Exception:
                    pass

                close_handle(process.process_handle)

            if self.process is None:
                return False

            self.mesen.install_hooks()
            self.mesen.set_watched_memory([(MEMORY_TYPES["NesInternalRam"], 0, 0x800)])
            self.mesen.read_new_events()
            self.mesen.clear_controller_input(0)

            self.applied_input_effects = list()

            self.is_process_running = True
        except Exception:
            if self.process is not None:
                close_handle(self.process.process_handle)

            self.process = None
            self.mesen = None

            return False

        return True

    def close_process_handle(self) -> bool:
        try:
            self.mesen.clear_controller_input(0)
        except Exception:
            pass

        if close_handle(self.process.process_handle):
            self.is_process_running = False
            self.process = None

            self.mesen = None

            self.pending_writes = list()
            self.applied_input_effects = list()

            self.original_pill_list = None
            self.restricted_pill_list = None

            self.game_state = GameState(is_valid=False)

            return True

        return False

    def is_process_still_running(self) -> bool:
        try:
            self.process.read_int(self.process.base_address)
        except Exception:
            self.is_process_running = False
            self.process = None

            self.mesen = None

            self.pending_writes = list()
            self.applied_input_effects = list()

            self.original_pill_list = None
            self.restricted_pill_list = None

            self.game_state = GameState(is_valid=False)

            return False

        return True

    def determine_game_state(self) -> GameState:
        self.game_state = self._determine_game_state()
        return self.game_state

    def end_tick(self) -> bool:
        if not self.is_process_running:
            return False

        if not len(self.pending_writes):
            return True

        writes: List[Tuple[int, int, bytes]] = list()
        data_size: int = 0

        write: Tuple[int, int, bytes]
        for write in self.pending_writes:
            if len(writes) == WRITE_RECORD_CAPACITY or data_size + len(write[2]) > WRITE_DATA_SIZE:
                break

            writes.append(write)
            data_size += len(write[2])

        try:
            if self.mesen.is_memory_write_pending():
                return False

            self.mesen.queue_memory_writes(writes)
        except Exception:
            return False

        self.pending_writes = self.pending_writes[len(writes):]

        return True

    def apply_base_patches(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid:
            return False

        splash_text: bytes = bytes.fromhex("ff040a161718090507040619ff")

        option_step_routines: Dict[str, Tuple[int, int, int, bool, bool]] = {
            "level_right": (0x96, free_space_allocations["level_unlock_table"], 21, True, True),
            "level_left": (0x96, free_space_allocations["level_unlock_table"], 21, False, True),
            "speed_right": (0x8B, free_space_allocations["speed_unlock_table"], 3, True, False),
            "speed_left": (0x8B, free_space_allocations["speed_unlock_table"], 3, False, False),
            "music_type_right": (ram_addresses["music_type"], free_space_allocations["music_type_unlock_table"], 3, True, False),
            "music_type_left": (ram_addresses["music_type"], free_space_allocations["music_type_unlock_table"], 3, False, False),
        }

        option_step_code: bytes = bytes()
        option_step_addresses: Dict[str, int] = dict()

        name: str
        value_address: int
        table_address: int
        value_count: int
        is_right: bool
        redraws_level_digits: bool
        for name, (value_address, table_address, value_count, is_right, redraws_level_digits) in option_step_routines.items():
            option_step_addresses[name] = free_space_allocations["option_step_code"] + len(option_step_code)
            option_step_code += build_option_step_code(option_step_addresses[name], value_address, table_address, value_count, is_right, redraws_level_digits)

        last_pill_chains_address: bytes = struct.pack("<H", ram_addresses["last_pill_chains"])
        last_pill_chains_code: bytes = assemble_6502([
            b"\xEE" + last_pill_chains_address,  # inc landing chains
            b"\xA9\x01",  # lda #$01
            b"\x85\x87",  # sta $87
            b"\x60",  # rts
            b"\x85\xAD",  # sta $AD
            b"\x8D" + last_pill_chains_address,  # sta landing chains
            b"\xE6\x87",  # inc $87
            b"\x60",  # rts
        ], free_space_allocations["last_pill_chains_code"])

        pause_select_code: bytes = assemble_6502([
            b"\xA5\xF5",  # lda $F5
            b"\xC9\x20",  # cmp #$20  ; select
            ("branch", b"\xD0", "start_check"),  # bne start check
            b"\xA9\xFF",  # lda #$FF
            b"\x85\x5D",  # sta $5D
            b"\xA9\x1E",  # lda #$1E
            b"\x85\xFE",  # sta $FE
            b"\xA9\x00",  # lda #$00
            b"\x8D\x8D\x06",  # sta $068D
            b"\xA9\x01",  # lda #$01
            b"\x85\x46",  # sta $46  ; options
            b"\x68",  # pla
            b"\x68",  # pla
            b"\x60",  # rts
            ("label", "start_check"),
            b"\xA5\xF5",  # lda $F5
            b"\xC9\x10",  # cmp #$10  ; start
            b"\x60",  # rts
        ], free_space_allocations["pause_select_code"])

        level_bar_tile: int = options_chr_tile_allocations["level_bar_tiles"]

        prg_patches: Dict[int, bytes] = {
            rom_addresses["virus_count_setup"]: b"\xAE" + struct.pack("<H", player_block_addresses["player_1"] + player_block_offsets["level"]) + b"\xBD" + struct.pack("<H", free_space_allocations["virus_count_table"]) + b"\x8D" + struct.pack("<H", player_block_addresses["player_1"] + player_block_offsets["viruses_to_place"]) + b"\x4C" + struct.pack("<H", rom_addresses["player_2_virus_count_setup"]),
            rom_addresses["landing_start"]: b"\x20" + struct.pack("<H", free_space_allocations["last_pill_chains_code"] + 8) + b"\x60",
            0x8F46: bytes.fromhex("b0"),
            0x9207: bytes.fromhex("eaeaea"),
            rom_addresses["fix_up_middle_segment"]: bytes.fromhex("4c0994"),
            rom_addresses["landing_resolve_loop"]: b"\x20" + struct.pack("<H", free_space_allocations["last_pill_chains_code"]) + b"\xEA",
            rom_addresses["pause_start_check"]: b"\x20" + struct.pack("<H", free_space_allocations["pause_select_code"]) + bytes.fromhex("f00dea"),
            0x981D: bytes.fromhex("a901ea"),
            0x9843: bytes.fromhex("a901ea"),
            0x98BF: bytes.fromhex("a9018d27074cef98"),
            0x9912: bytes.fromhex("eaea"),
            0x9A57: b"\x20" + struct.pack("<H", option_step_addresses["music_type_right"]) + bytes.fromhex("4c669a"),
            0x9A6C: b"\x20" + struct.pack("<H", option_step_addresses["music_type_left"]) + bytes.fromhex("4c799a"),
            rom_addresses["options_level_adjust"]: b"\x20" + struct.pack("<H", option_step_addresses["level_right"]) + bytes.fromhex("4c1f9b"),
            0x9B25: b"\x4C" + struct.pack("<H", option_step_addresses["level_left"]),
            0x9B3D: b"\x20" + struct.pack("<H", option_step_addresses["speed_right"]) + bytes.fromhex("4c4a9b"),
            0x9B50: b"\x4C" + struct.pack("<H", option_step_addresses["speed_left"]),
            0x9BF4: bytes.fromhex("03"),
            **{operand: bytes([playfield_tiles["garbage"]]) for operand in garbage_drop_pellet_operands},
            rom_addresses["options_level_row_attributes"] + 21: bytes.fromhex("c0f0f0b8"),
            rom_addresses["options_level_row_attributes"] + 29: bytes.fromhex("5c5f1f8b"),
            rom_addresses["options_speed_row_attributes"] + 21: bytes.fromhex("c5f5f1b8"),
            rom_addresses["options_speed_row_attributes"] + 29: bytes.fromhex("0c0f0f8b"),
            rom_addresses["options_music_row_attributes"] + 21: bytes.fromhex("c5f5f1b8"),
            rom_addresses["options_music_row_attributes"] + 29: bytes.fromhex("5c5f1f8b"),
            rom_addresses["options_palette"] + 13: bytes.fromhex("003015"),
            0xB32C: bytes.fromhex("a901"),
            0xBC68: splash_text,
            rom_addresses["options_level_bar_tiles"]: bytes(range(level_bar_tile, level_bar_tile + 11)),
            rom_addresses["options_level_bar_lower_tiles"]: bytes(range(level_bar_tile + 11, level_bar_tile + 22)),
            rom_addresses["gameplay_magnifier_upper_tiles"]: bytes(relocated_magnifier_tiles[:2]),
            rom_addresses["gameplay_magnifier_lower_tile"]: bytes(relocated_magnifier_tiles[2:]),
            free_space_allocations["option_step_code"]: option_step_code,
            free_space_allocations["last_pill_chains_code"]: last_pill_chains_code,
            free_space_allocations["pause_select_code"]: pause_select_code,
        }

        splash_glyph_tile_to_font_tile: Dict[int, int] = {
            0x16: 0x0C,
            0x17: 0x11,
            0x18: 0x12,
            0x19: 0x18,
        }

        try:
            current_bytes: Dict[int, bytes] = {
                address: self.mesen.read_memory(MEMORY_TYPES["NesPrgRom"], address - 0x8000, len(patched))
                for address, patched in prg_patches.items()
            }

            if not all(current_bytes[address] == patched for address, patched in prg_patches.items()):
                original_prg_rom: bytes = self.mesen.read_original_prg_rom()

                if any(current_bytes[address] not in (original_prg_rom[address - 0x8000:address - 0x8000 + len(patched)], patched) for address, patched in prg_patches.items()):
                    return False

                glyph_tile: int
                font_tile: int
                for glyph_tile, font_tile in splash_glyph_tile_to_font_tile.items():
                    glyph: bytes = self.mesen.read_memory(MEMORY_TYPES["NesChrRom"], options_chr_bank + font_tile * 16, 16)

                    self.pending_writes.append((MEMORY_TYPES["NesChrRom"], 0x3000 + glyph_tile * 16, glyph))
                    self.pending_writes.append((MEMORY_TYPES["NesChrRom"], 0x4000 + glyph_tile * 16, glyph))

                self.pending_writes.append((MEMORY_TYPES["NesChrRom"], options_chr_bank + level_bar_tile * 16, self._build_level_bar_tiles(list(range(21)))))

                original_chr_rom: bytes = self.mesen.read_original_chr_rom()

                gameplay_chr_bank: int
                for gameplay_chr_bank in gameplay_chr_banks:
                    index: int
                    relocated_tile: int
                    for index, relocated_tile in enumerate(relocated_magnifier_tiles):
                        self.pending_writes.append((MEMORY_TYPES["NesChrRom"], gameplay_chr_bank + relocated_tile * 16, original_chr_rom[gameplay_chr_bank + (playfield_tiles["garbage"] + index) * 16:][:16]))

                    self.pending_writes.append((MEMORY_TYPES["NesChrRom"], gameplay_chr_bank + playfield_tiles["garbage"] * 16, original_chr_rom[gameplay_chr_bank + playfield_tiles["single"] * 16:][:48]))

                self.pending_writes.append((MEMORY_TYPES["NesPrgRom"], free_space_allocations["level_unlock_table"] - 0x8000, bytes([1] * 21)))
                self.pending_writes.append((MEMORY_TYPES["NesPrgRom"], free_space_allocations["virus_count_table"] - 0x8000, bytes((level + 1) * 4 for level in range(21))))
                self.pending_writes.append((MEMORY_TYPES["NesPrgRom"], free_space_allocations["speed_unlock_table"] - 0x8000, bytes([1] * 3)))
                self.pending_writes.append((MEMORY_TYPES["NesPrgRom"], free_space_allocations["music_type_unlock_table"] - 0x8000, bytes([1] * 3)))

                address: int
                patched: bytes
                for address, patched in prg_patches.items():
                    self.pending_writes.append((MEMORY_TYPES["NesPrgRom"], address - 0x8000, patched))

            if self.mesen.read_memory(MEMORY_TYPES["NesInternalRam"], ram_addresses["tamper_flag"], 1)[0] != 0:
                self.pending_writes.append((MEMORY_TYPES["NesInternalRam"], ram_addresses["tamper_flag"], bytes([0])))

            if self.game_state.is_on_splash and self.mesen.read_memory(MEMORY_TYPES["NesInternalRam"], ram_addresses["number_of_players"], 1)[0] != 1:
                self.pending_writes.append((MEMORY_TYPES["NesInternalRam"], ram_addresses["number_of_players"], bytes([1])))

            if self.game_state.is_on_splash and self.mesen.read_ppu_memory(0x22EA, len(splash_text)) != splash_text:
                splash_text_row: Tuple[int, int] = self.mesen.translate_ppu_address(0x22EA)
                self.pending_writes.append((splash_text_row[0], splash_text_row[1], splash_text))
        except Exception:
            return False

        return True

    def return_to_splash(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid:
            return False

        if self.game_state.is_on_splash:
            return True

        try:
            if self.game_state.is_in_demo:
                self.mesen.set_controller_input(0, pressed_buttons=["Start"], frame_count=1)
            else:
                self.mesen.reset()
        except Exception:
            return False

        return True

    def set_unlocked_levels(self, unlocked_levels: List[int]) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid:
            return False

        level_unlock_table: bytes = bytes(int(level in unlocked_levels) for level in range(21))

        try:
            if self.mesen.read_memory(MEMORY_TYPES["NesPrgRom"], free_space_allocations["level_unlock_table"] - 0x8000, len(level_unlock_table)) == level_unlock_table:
                return True

            level_bar_tiles_offset: int = options_chr_bank + options_chr_tile_allocations["level_bar_tiles"] * 16
            level_bar_tiles: bytes = self._build_level_bar_tiles(unlocked_levels)

            if self.mesen.read_memory(MEMORY_TYPES["NesChrRom"], level_bar_tiles_offset, len(level_bar_tiles)) != level_bar_tiles:
                self.pending_writes.append((MEMORY_TYPES["NesChrRom"], level_bar_tiles_offset, level_bar_tiles))
        except Exception:
            return False

        return self._set_prg_rom_bytes(free_space_allocations["level_unlock_table"], level_unlock_table)

    def set_unlocked_speeds(self, unlocked_speeds: List[DrMarioSpeeds]) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid:
            return False

        speed_word_cells: Dict[DrMarioSpeeds, Tuple[int, range]] = {
            DrMarioSpeeds.HIGH: (18, range(21, 23)),
            DrMarioSpeeds.LOW: (18, range(11, 14)),
            DrMarioSpeeds.MEDIUM: (18, range(16, 19)),
        }

        if not self._set_options_word_palettes({cells: speed not in unlocked_speeds for speed, cells in speed_word_cells.items()}):
            return False

        return self._set_prg_rom_bytes(free_space_allocations["speed_unlock_table"], bytes(int(speed in unlocked_speeds) for speed in sorted(DrMarioSpeeds, key=speed_to_internal_speed_id.get)))

    def set_unlocked_music_types(self, unlocked_music_types: List[DrMarioMusicTypes]) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid:
            return False

        music_type_word_cells: Dict[DrMarioMusicTypes, Tuple[int, range]] = {
            DrMarioMusicTypes.CHILL: (24, range(15, 20)),
            DrMarioMusicTypes.FEVER: (24, range(8, 13)),
            DrMarioMusicTypes.OFF: (24, range(22, 25)),
        }

        if not self._set_options_word_palettes({cells: music_type not in unlocked_music_types for music_type, cells in music_type_word_cells.items()}):
            return False

        return self._set_prg_rom_bytes(free_space_allocations["music_type_unlock_table"], bytes(int(music_type in unlocked_music_types) for music_type in sorted(DrMarioMusicTypes, key=music_type_to_internal_music_type_id.get)))

    def set_options(self, level: int, speed: DrMarioSpeeds, music_type: DrMarioMusicTypes) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid:
            return False

        if (self.game_state.level, self.game_state.speed, self.game_state.music_type) == (level, speed, music_type):
            return True

        player_block: int = player_block_addresses["player_1"]
        active_block: int = player_block_addresses["active"]

        self.pending_writes.append((MEMORY_TYPES["NesInternalRam"], player_block + player_block_offsets["level"], bytes([level])))
        self.pending_writes.append((MEMORY_TYPES["NesInternalRam"], player_block + player_block_offsets["speed"], bytes([speed_to_internal_speed_id[speed]])))
        self.pending_writes.append((MEMORY_TYPES["NesInternalRam"], ram_addresses["music_type"], bytes([music_type_to_internal_music_type_id[music_type]])))

        if self.game_state.mode == DrMarioModes.OPTIONS:
            try:
                redraw_flags: int = self.mesen.read_memory(MEMORY_TYPES["NesInternalRam"], ram_addresses["options_redraw_flags"], 1)[0]
            except Exception:
                return False

            self.pending_writes.append((MEMORY_TYPES["NesInternalRam"], active_block + player_block_offsets["level"], bytes([level])))
            self.pending_writes.append((MEMORY_TYPES["NesInternalRam"], active_block + player_block_offsets["speed"], bytes([speed_to_internal_speed_id[speed]])))
            self.pending_writes.append((MEMORY_TYPES["NesInternalRam"], ram_addresses["options_redraw_flags"], bytes([redraw_flags | 0x04])))

        return True

    def set_level_virus_counts(self, counts: Dict[int, int]) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid:
            return False

        try:
            max_rows: bytes = self.mesen.read_memory(MEMORY_TYPES["NesPrgRom"], rom_addresses["virus_placement_max_rows"] - 0x8000, 21)
        except Exception:
            return False

        if any(not 0 <= level <= 20 or not 4 <= count <= min(99, (max_rows[level] + 1) * 8 * 84 // 104) for level, count in counts.items()):
            return False

        level: int
        count: int
        for level, count in counts.items():
            if not self._set_prg_rom_bytes(free_space_allocations["virus_count_table"] + level, bytes([count])):
                return False

        return True

    def set_level_virus_rows(self, rows: Dict[int, int]) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid:
            return False

        if any(not 0 <= level <= 20 or not 1 <= row_count <= 16 for level, row_count in rows.items()):
            return False

        level: int
        row_count: int
        for level, row_count in rows.items():
            if not self._set_prg_rom_bytes(rom_addresses["virus_placement_max_rows"] + level, bytes([row_count - 1])):
                return False

        return True

    def set_speed_up_cap(self, cap: int) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid:
            return False

        if not self._set_prg_rom_bytes(rom_addresses["speed_up_cap"], bytes([cap])):
            return False

        if self.game_state.mode == DrMarioModes.PLAYING and not self.game_state.is_between_levels and self.game_state.speed_ups > cap:
            return self.set_speed_ups(cap)

        return True

    def set_speed_ups(self, count: int) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid or self.game_state.mode != DrMarioModes.PLAYING or self.game_state.is_between_levels:
            return False

        block: int
        for block in (player_block_addresses["active"], player_block_addresses["player_1"]):
            self.pending_writes.append((MEMORY_TYPES["NesInternalRam"], block + player_block_offsets["speed_ups"], bytes([count])))

        return True

    def set_next_pill_visible(self, is_visible: bool) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid:
            return False

        return self._set_prg_rom_bytes(rom_addresses["next_pill_preview_call"], bytes([0x20 if is_visible else 0x2C]))

    def set_match_length(self, length: int) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid or not 3 <= length <= 8:
            return False

        return (
            self._set_prg_rom_bytes(rom_addresses["match_length_horizontal"], bytes([length - 1]))
            and self._set_prg_rom_bytes(rom_addresses["match_start_column_limit"], bytes([9 - length]))
            and self._set_prg_rom_bytes(rom_addresses["match_length_vertical"], bytes([length - 1]))
            and self._set_prg_rom_bytes(rom_addresses["match_start_row_limit"], bytes([(17 - length) * 8]))
        )

    def set_color_blind(self, is_enabled: bool) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid or self.game_state.mode != DrMarioModes.PLAYING:
            return False

        pill_color_palette_indices: Tuple[int, ...] = (9, 10, 11, 21, 22, 25, 26, 27, 29, 30)

        try:
            playing_palette: bytes = self.mesen.read_memory(MEMORY_TYPES["NesPrgRom"], rom_addresses["playing_palette"] - 0x8000, 32)
            palette: bytes = self.mesen.read_memory(MEMORY_TYPES["NesPaletteRam"], 0, 32)
        except Exception:
            return False

        color_blind_palette: bytearray = bytearray(palette)

        index: int
        for index in pill_color_palette_indices:
            color_blind_palette[index] = 0x10 if is_enabled else playing_palette[index]

        if color_blind_palette != palette:
            self.pending_writes.append((MEMORY_TYPES["NesPaletteRam"], 0, bytes(color_blind_palette)))

        return True

    def set_input_effects(self, effects: List[DrMarioInputEffects]) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid:
            return False

        active_effects: List[DrMarioInputEffects] = effects if self.game_state.mode == DrMarioModes.PLAYING else list()

        if set(active_effects) == set(self.applied_input_effects):
            return True

        try:
            if not len(active_effects):
                self.mesen.clear_controller_input(0)
            else:
                self.mesen.set_controller_input(
                    0,
                    released_buttons=[button for effect, button in ((DrMarioInputEffects.CLOCKWISE_ROTATION_DISABLED, "A"), (DrMarioInputEffects.COUNTERCLOCKWISE_ROTATION_DISABLED, "B")) if effect in active_effects],
                    swapped_buttons=[("Left", "Right")] if DrMarioInputEffects.REVERSED_CONTROLS in active_effects else [],
                )
        except Exception:
            return False

        self.applied_input_effects = list(active_effects)

        return True

    def set_virus_colors(self, colors: Dict[DrMarioColors, DrMarioNesColors]) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid:
            return False

        color_palette_indices: Dict[DrMarioColors, Tuple[int, ...]] = {
            DrMarioColors.BLUE: (11, 27, 30),
            DrMarioColors.RED: (10, 22, 26),
            DrMarioColors.YELLOW: (9, 21, 25, 29),
        }

        return self._set_palette_colors({index: nes_color.value for color, nes_color in colors.items() for index in color_palette_indices[color]}, dict()) and self._set_splash_palette_colors({30: nes_color.value for color, nes_color in colors.items() if color == DrMarioColors.BLUE})

    def set_mario_color(self, nes_color: DrMarioNesColors) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid:
            return False

        return self._set_palette_colors({19: nes_color.value}, dict()) and self._set_splash_palette_colors({19: nes_color.value})

    def set_background_colors(self, colors: Dict[DrMarioPaletteRegions, DrMarioNesColors]) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid:
            return False

        region_palette_indices: Dict[DrMarioPaletteRegions, Tuple[int, ...]] = {
            DrMarioPaletteRegions.BACKDROP: (0, 16),
            DrMarioPaletteRegions.BORDERS: (6,),
            DrMarioPaletteRegions.BOTTLE: (2,),
            DrMarioPaletteRegions.CLIPBOARD: (5,),
            DrMarioPaletteRegions.HIGHLIGHTS: (1,),
            DrMarioPaletteRegions.MAGNIFIER_FRAME: (13,),
            DrMarioPaletteRegions.MAGNIFIER_LENS: (14,),
        }

        checkerboard_speeds: Dict[DrMarioPaletteRegions, DrMarioSpeeds] = {
            DrMarioPaletteRegions.CHECKERBOARD_HIGH: DrMarioSpeeds.HIGH,
            DrMarioPaletteRegions.CHECKERBOARD_LOW: DrMarioSpeeds.LOW,
            DrMarioPaletteRegions.CHECKERBOARD_MEDIUM: DrMarioSpeeds.MEDIUM,
        }

        if DrMarioPaletteRegions.SPLASH_CHECKERBOARD in colors:
            splash_checkerboard_color: int = colors[DrMarioPaletteRegions.SPLASH_CHECKERBOARD].value

            if not self._set_splash_palette_colors({1: splash_checkerboard_color, 2: splash_checkerboard_color + 0x10, 9: splash_checkerboard_color, 10: splash_checkerboard_color + 0x10}):
                return False

        return self._set_palette_colors(
            {index: nes_color.value for region, nes_color in colors.items() if region in region_palette_indices for index in region_palette_indices[region]},
            {checkerboard_speeds[region]: nes_color.value for region, nes_color in colors.items() if region in checkerboard_speeds},
        )

    def set_music_tracks(self, music_tracks: Dict[DrMarioMusicTracks, DrMarioMusicTracks]) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid:
            return False

        try:
            original_prg_rom: bytes = self.mesen.read_original_prg_rom()
        except Exception:
            return False

        header_offsets_start: int = rom_addresses["music_track_header_offsets"] - 0x8000
        original_header_offsets: bytes = original_prg_rom[header_offsets_start:header_offsets_start + 12]
        header_offsets: bytearray = bytearray(original_header_offsets)

        music_track: DrMarioMusicTracks
        selected_music_track: DrMarioMusicTracks
        for music_track, selected_music_track in music_tracks.items():
            header_offsets[music_track_to_internal_music_track_id[music_track] - 1] = original_header_offsets[music_track_to_internal_music_track_id[selected_music_track] - 1]

        return self._set_prg_rom_bytes(rom_addresses["music_track_header_offsets"], bytes(header_offsets))

    def remove_random_viruses(self, count: int) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid or self.game_state.mode != DrMarioModes.PLAYING or self.game_state.is_paused or self.game_state.is_between_levels or not self.game_state.is_pill_falling:
            return False

        try:
            playfield: bytes = self.mesen.read_memory(MEMORY_TYPES["NesInternalRam"], playfield_addresses["player_1"], 0x80)
        except Exception:
            return False

        virus_cells: List[int] = [cell for cell, value in enumerate(playfield) if value >> 4 == 0xD]

        return self._change_viruses(playfield, {cell: 0xFF for cell in random.sample(virus_cells, min(count, len(virus_cells)))})

    def add_random_viruses(self, count: int, colors: List[DrMarioColors]) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid or self.game_state.mode != DrMarioModes.PLAYING or self.game_state.is_paused or self.game_state.is_between_levels or not self.game_state.is_pill_falling:
            return False

        try:
            playfield: bytes = self.mesen.read_memory(MEMORY_TYPES["NesInternalRam"], playfield_addresses["player_1"], 0x80)
            max_row: int = self.mesen.read_memory(MEMORY_TYPES["NesPrgRom"], rom_addresses["virus_placement_max_rows"] - 0x8000 + self.game_state.level, 1)[0]
        except Exception:
            return False

        allowed: List[int] = [color_to_internal_color_id[color] for color in colors]
        placed_playfield: bytearray = bytearray(playfield)
        cell_changes: Dict[int, int] = dict()

        pill_area: Optional[Set[int]] = self._read_falling_pill_area()

        if pill_area is None:
            return False

        cells: List[int] = [cell for cell in range((15 - max_row) * 8, 0x80) if playfield[cell] == 0xFF and cell not in pill_area]
        random.shuffle(cells)

        cell: int
        for cell in cells:
            if len(cell_changes) == count:
                break

            spaced_color: Optional[int] = self._choose_spaced_color(placed_playfield, cell, allowed)

            if spaced_color is None:
                continue

            placed_playfield[cell] = 0xD0 | spaced_color
            cell_changes[cell] = placed_playfield[cell]

        return self._change_viruses(playfield, cell_changes)

    def add_filled_smiley_viruses(self, colors: List[DrMarioColors]) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid or self.game_state.mode != DrMarioModes.PLAYING or self.game_state.is_paused or self.game_state.is_between_levels or not self.game_state.is_pill_falling:
            return False

        if len(colors) < 2:
            return False

        try:
            playfield: bytes = self.mesen.read_memory(MEMORY_TYPES["NesInternalRam"], playfield_addresses["player_1"], 0x80)
        except Exception:
            return False

        face_colors: List[int] = random.sample([color_to_internal_color_id[color] for color in colors], 2)
        gap_cells: List[int] = [(9 + row) * 8 + column for row, column in self.smiley_cells]
        face_cells: List[int] = [8 * 8 + column for column in range(1, 7)] + [row * 8 + column for row in range(9, 14) for column in range(8)] + [14 * 8 + column for column in range(1, 7)]
        corner_cells: List[int] = [8 * 8, 8 * 8 + 7, 14 * 8, 14 * 8 + 7]

        pill_area: Optional[Set[int]] = self._read_falling_pill_area()

        if pill_area is None or not pill_area.isdisjoint(gap_cells + face_cells + corner_cells):
            return False

        placed_playfield: bytearray = bytearray(playfield)
        cell_changes: Dict[int, int] = dict()

        owned_cells: List[int] = [cell for cell in gap_cells + corner_cells + face_cells if playfield[cell] == 0xFF or playfield[cell] >> 4 == 0xD]

        cell: int
        for cell in owned_cells:
            placed_playfield[cell] = 0xFF

        for cell in face_cells:
            if cell not in gap_cells and cell in owned_cells:
                placed_playfield[cell] = 0xD0 | face_colors[((cell // 8) // 2 + (cell % 8) // 2) % 2]

        for cell in owned_cells:
            if placed_playfield[cell] != playfield[cell]:
                cell_changes[cell] = placed_playfield[cell]

        return self._change_viruses(playfield, cell_changes)

    def scramble_viruses(self, colors: List[DrMarioColors]) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid or self.game_state.mode != DrMarioModes.PLAYING or self.game_state.is_paused or self.game_state.is_between_levels or not self.game_state.is_pill_falling:
            return False

        if not len(colors):
            return False

        try:
            playfield: bytes = self.mesen.read_memory(MEMORY_TYPES["NesInternalRam"], playfield_addresses["player_1"], 0x80)
        except Exception:
            return False

        return self._change_viruses(playfield, {cell: 0xD0 | color_to_internal_color_id[random.choice(colors)] for cell, value in enumerate(playfield) if value >> 4 == 0xD})

    def set_pill_types(self, allowed_pill_types: List[Tuple[DrMarioColors, DrMarioColors]]) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid or self.game_state.mode not in (DrMarioModes.PLAYING, DrMarioModes.VIRUS_PLACEMENT) or self.game_state.is_paused or self.game_state.is_between_levels:
            return False

        if not len(allowed_pill_types):
            return False

        allowed: List[int] = sorted({
            color_to_internal_color_id[first] * 3 + color_to_internal_color_id[second]
            for pill_type in allowed_pill_types
            for first, second in (pill_type, pill_type[::-1])
        })

        active_block: int = player_block_addresses["active"]

        try:
            pill_list: bytes = self.mesen.read_memory(MEMORY_TYPES["NesInternalRam"], ram_addresses["pill_list"], 0x80)
            current_colors: bytes = self.mesen.read_memory(MEMORY_TYPES["NesInternalRam"], active_block + player_block_offsets["pill_left_color"], 2)
            next_colors: bytes = self.mesen.read_memory(MEMORY_TYPES["NesInternalRam"], active_block + player_block_offsets["next_pill_left_color"], 2)
        except Exception:
            return False

        if pill_list != self.restricted_pill_list:
            self.original_pill_list = pill_list

        allowed_pill_list: bytes = bytes(
            pill_type if pill_type in allowed else allowed[index % len(allowed)]
            for index, pill_type in enumerate(self.original_pill_list)
        )

        self.restricted_pill_list = allowed_pill_list

        current_type: int = current_colors[0] * 3 + current_colors[1]
        next_type: int = next_colors[0] * 3 + next_colors[1]

        allowed_current_colors: bytes = bytes(divmod(current_type if current_type in allowed else allowed[current_type % len(allowed)], 3))
        allowed_next_colors: bytes = bytes(divmod(next_type if next_type in allowed else allowed[next_type % len(allowed)], 3))

        if allowed_pill_list != pill_list:
            self.pending_writes.append((MEMORY_TYPES["NesInternalRam"], ram_addresses["pill_list"], allowed_pill_list))

        block: int
        for block in (active_block, player_block_addresses["player_1"]):
            if allowed_next_colors != next_colors:
                self.pending_writes.append((MEMORY_TYPES["NesInternalRam"], block + player_block_offsets["next_pill_left_color"], allowed_next_colors))

            if allowed_current_colors != current_colors and (self.game_state.is_pill_falling or self.game_state.mode == DrMarioModes.VIRUS_PLACEMENT):
                self.pending_writes.append((MEMORY_TYPES["NesInternalRam"], block + player_block_offsets["pill_left_color"], allowed_current_colors))

        return True

    def drop_garbage(self, colors: List[DrMarioColors]) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid or self.game_state.mode != DrMarioModes.PLAYING or self.game_state.is_paused or self.game_state.is_between_levels:
            return False

        if not 2 <= len(colors) <= 4:
            return False

        garbage_block: int = player_block_addresses["player_2"]

        self.pending_writes.append((MEMORY_TYPES["NesInternalRam"], garbage_block + player_block_offsets["last_pill_line_colors"], bytes(color_to_internal_color_id[color] for color in colors)))
        self.pending_writes.append((MEMORY_TYPES["NesInternalRam"], garbage_block + player_block_offsets["garbage_count"], bytes([len(colors)])))

        return True

    def add_garbage(self, pellets: Dict[int, DrMarioColors]) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid or self.game_state.mode not in (DrMarioModes.PLAYING, DrMarioModes.VIRUS_PLACEMENT) or self.game_state.is_paused or self.game_state.is_between_levels or not (self.game_state.is_pill_falling or self.game_state.is_before_first_pill):
            return False

        try:
            playfield: bytes = self.mesen.read_memory(MEMORY_TYPES["NesInternalRam"], playfield_addresses["player_1"], 0x80)
        except Exception:
            return False

        pill_area: Optional[Set[int]] = self._read_falling_pill_area()

        if pill_area is None:
            return False

        cell: int
        color: DrMarioColors
        for cell, color in pellets.items():
            if playfield[cell] == 0xFF and cell not in pill_area:
                self.pending_writes.append((MEMORY_TYPES["NesInternalRam"], playfield_addresses["player_1"] + cell, bytes([playfield_tiles["garbage"] | color_to_internal_color_id[color]])))

        block: int
        for block in (player_block_addresses["active"], player_block_addresses["player_1"]):
            self.pending_writes.append((MEMORY_TYPES["NesInternalRam"], block + player_block_offsets["playfield_redraw_row"], bytes([0x0F])))

        return True

    def add_random_garbage(self, round_count: int, colors: List[DrMarioColors]) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid or self.game_state.mode not in (DrMarioModes.PLAYING, DrMarioModes.VIRUS_PLACEMENT) or self.game_state.is_paused or self.game_state.is_between_levels or not (self.game_state.is_pill_falling or self.game_state.is_before_first_pill):
            return False

        try:
            playfield: bytes = self.mesen.read_memory(MEMORY_TYPES["NesInternalRam"], playfield_addresses["player_1"], 0x80)
        except Exception:
            return False

        allowed: List[int] = [color_to_internal_color_id[color] for color in colors]
        placed_playfield: bytearray = bytearray(playfield)
        pellets: Dict[int, DrMarioColors] = dict()

        column_depths: List[int] = [next((row for row in range(16) if playfield[row * 8 + column] != 0xFF), 16) for column in range(8)]
        pill_area: Optional[Set[int]] = self._read_falling_pill_area()

        if pill_area is None:
            return False

        garbage_round: int
        for garbage_round in range(round_count):
            column: int
            for column in range(random.randrange(2), 8, 2):
                if column_depths[column] <= (3 if column in (3, 4) else 0):
                    continue

                cell: int = (column_depths[column] - 1) * 8 + column

                if cell in pill_area:
                    continue

                spaced_color: Optional[int] = self._choose_spaced_color(placed_playfield, cell, allowed)

                if spaced_color is None:
                    continue

                placed_playfield[cell] = playfield_tiles["garbage"] | spaced_color
                pellets[cell] = internal_color_id_to_color[spaced_color]
                column_depths[column] -= 1

        return self.add_garbage(pellets)

    def clear_garbage(self, count: int) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid or self.game_state.mode != DrMarioModes.PLAYING or self.game_state.is_paused or self.game_state.is_between_levels or not self.game_state.is_pill_falling:
            return False

        try:
            playfield: bytes = self.mesen.read_memory(MEMORY_TYPES["NesInternalRam"], playfield_addresses["player_1"], 0x80)
        except Exception:
            return False

        garbage_cells: List[int] = [cell for cell, value in enumerate(playfield) if value >> 4 == playfield_tiles["garbage"] >> 4][:count]

        if not len(garbage_cells):
            return True

        cell: int
        for cell in garbage_cells:
            self.pending_writes.append((MEMORY_TYPES["NesInternalRam"], playfield_addresses["player_1"] + cell, bytes([playfield_tiles["empty"]])))

        block: int
        for block in (player_block_addresses["active"], player_block_addresses["player_1"]):
            self.pending_writes.append((MEMORY_TYPES["NesInternalRam"], block + player_block_offsets["playfield_redraw_row"], bytes([0x0F])))

        return True

    def display_message(self, message: str) -> bool:
        if not self.is_process_running:
            return False

        try:
            self.mesen.display_message("AP", message.encode("utf-8")[:ARGUMENT_BUFFER_SIZE - 4].decode("utf-8", errors="ignore"))
        except Exception:
            return False

        return True

    def play_item_received_sound(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid:
            return False

        self.pending_writes.append((MEMORY_TYPES["NesInternalRam"], ram_addresses["sound_effect_request"], bytes([6])))

        return True

    def set_hud_text(self, lines: List[str]) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid or self.game_state.mode not in (DrMarioModes.PLAYING, DrMarioModes.VIRUS_PLACEMENT) or len(lines) > 2:
            return False

        character_tiles: Dict[str, int] = {
            **{str(digit): digit for digit in range(10)},
            **{chr(ord("A") + index): 0x0A + index for index in range(26)},
            " ": 0xFE,
            "-": 0x24,
            ",": 0x25,
            ".": 0x2A,
        }

        if any(len(line) > 7 or any(character not in character_tiles for character in line.upper()) for line in lines):
            return False

        try:
            hud_rows: List[bytes] = [bytes(character_tiles[character] for character in line.upper().ljust(7)) for line in (lines + [""])[:2]]

            row: int
            hud_row: bytes
            for row, hud_row in enumerate(hud_rows):
                if self.mesen.read_ppu_memory(0x20E2 + row * 0x20, 7) != hud_row:
                    nametable_address: Tuple[int, int] = self.mesen.translate_ppu_address(0x20E2 + row * 0x20)
                    self.pending_writes.append((nametable_address[0], nametable_address[1], hud_row))
        except Exception:
            return False

        return True

    def kill_player(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_valid or self.game_state.mode != DrMarioModes.PLAYING or self.game_state.is_paused or self.game_state.is_between_levels or self.game_state.is_topped_out:
            return False

        block: int
        for block in (player_block_addresses["active"], player_block_addresses["player_1"]):
            self.pending_writes.append((MEMORY_TYPES["NesInternalRam"], block + player_block_offsets["topped_out"], bytes([1])))

        self.pending_writes.append((MEMORY_TYPES["NesInternalRam"], ram_addresses["secondary_sound_request"], bytes([5])))

        return True

    def _read_falling_pill_area(self) -> Optional[Set[int]]:
        if not self.game_state.is_pill_falling:
            return set()

        try:
            pill: bytes = self.mesen.read_memory(MEMORY_TYPES["NesInternalRam"], player_block_addresses["active"], player_block_offsets["pill_y"] + 1)
        except Exception:
            return None

        pill_row: int = 15 - pill[player_block_offsets["pill_y"]]
        pill_column: int = pill[player_block_offsets["pill_x"]]

        return {row * 8 + column for row in range(max(pill_row - 2, 0), min(pill_row + 3, 16)) for column in range(max(pill_column - 1, 0), min(pill_column + 3, 8))}

    def _choose_spaced_color(self, playfield: bytearray, cell: int, allowed: List[int]) -> Optional[int]:
        neighbors: List[int] = [neighbor for neighbor in (cell - 16, cell + 16) if 0 <= neighbor < 0x80] + [cell + offset for offset in (-2, 2) if 0 <= cell % 8 + offset < 8]
        choices: List[int] = [color for color in allowed if color not in {playfield[neighbor] & 0x03 for neighbor in neighbors if playfield[neighbor] < 0xF0}]

        if not choices:
            return None

        return random.choice(choices)

    def _change_viruses(self, playfield: bytes, cell_changes: Dict[int, int]) -> bool:
        if not len(cell_changes):
            return True

        try:
            virus_counts: List[int] = list(self.mesen.read_memory(MEMORY_TYPES["NesInternalRam"], ram_addresses["virus_color_counts"], 3))
            redraw_flags: int = self.mesen.read_memory(MEMORY_TYPES["NesInternalRam"], ram_addresses["status_redraw_flags"], 1)[0]
        except Exception:
            return False

        original_virus_counts: List[int] = list(virus_counts)

        cell: int
        value: int
        for cell, value in cell_changes.items():
            if playfield[cell] >> 4 == 0xD:
                virus_counts[playfield[cell] & 0x03] -= 1

            if value >> 4 == 0xD:
                virus_counts[value & 0x03] += 1

        total: int = sum(virus_counts)

        if total > 99:
            return False

        for cell, value in cell_changes.items():
            self.pending_writes.append((MEMORY_TYPES["NesInternalRam"], playfield_addresses["player_1"] + cell, bytes([value])))

        total_bcd: bytes = bytes([((total // 10) << 4) | (total % 10)])

        self.pending_writes.append((MEMORY_TYPES["NesInternalRam"], ram_addresses["virus_color_counts"], bytes(virus_counts)))
        self.pending_writes.append((MEMORY_TYPES["NesInternalRam"], player_block_addresses["active"] + player_block_offsets["viruses_remaining"], total_bcd))
        self.pending_writes.append((MEMORY_TYPES["NesInternalRam"], player_block_addresses["player_1"] + player_block_offsets["viruses_remaining"], total_bcd))
        self.pending_writes.append((MEMORY_TYPES["NesInternalRam"], ram_addresses["status_redraw_flags"], bytes([redraw_flags | 0x10])))

        block: int
        for block in (player_block_addresses["active"], player_block_addresses["player_1"]):
            self.pending_writes.append((MEMORY_TYPES["NesInternalRam"], block + player_block_offsets["playfield_redraw_row"], bytes([0x0F])))

        color: int
        for color in range(3):
            if virus_counts[color] < original_virus_counts[color]:
                self.pending_writes.append((MEMORY_TYPES["NesInternalRam"], ram_addresses["virus_color_states"] + color, bytes([1])))
                self.pending_writes.append((MEMORY_TYPES["NesInternalRam"], ram_addresses["virus_color_animation_frames"] + color, bytes([0])))
            elif original_virus_counts[color] == 0 and virus_counts[color] > 0:
                self.pending_writes.append((MEMORY_TYPES["NesInternalRam"], ram_addresses["virus_color_states"] + color, bytes([0])))

        return True

    def _set_palette_colors(self, palette_colors: Dict[int, int], checkerboard_colors: Dict[DrMarioSpeeds, int]) -> bool:
        try:
            playing_palette: bytes = self.mesen.read_memory(MEMORY_TYPES["NesPrgRom"], rom_addresses["playing_palette"] - 0x8000, 32)
            palette: bytes = self.mesen.read_memory(MEMORY_TYPES["NesPaletteRam"], 0, 32)
        except Exception:
            return False

        live_colors: Dict[int, int] = dict()

        index: int
        nes_color: int
        for index, nes_color in palette_colors.items():
            if not self._set_prg_rom_bytes(rom_addresses["playing_palette"] + index, bytes([nes_color])) or not self._set_prg_rom_bytes(rom_addresses["playing_palette_copy"] + index, bytes([nes_color])):
                return False

            if palette[index] == playing_palette[index]:
                live_colors[index] = nes_color

        speed: DrMarioSpeeds
        for speed, nes_color in checkerboard_colors.items():
            if not self._set_prg_rom_bytes(rom_addresses["checkerboard_speed_colors"] + speed_to_internal_speed_id[speed], bytes([nes_color])):
                return False

            if speed == self.game_state.speed:
                live_colors.update({index: nes_color for index in (3, 7, 15)})

        if self.game_state.mode in (DrMarioModes.PLAYING, DrMarioModes.VIRUS_PLACEMENT):
            for index, nes_color in live_colors.items():
                if palette[index] != nes_color:
                    self.pending_writes.append((MEMORY_TYPES["NesPaletteRam"], index, bytes([nes_color])))

        return True

    def _set_splash_palette_colors(self, palette_colors: Dict[int, int]) -> bool:
        try:
            splash_palette: bytes = self.mesen.read_memory(MEMORY_TYPES["NesPrgRom"], rom_addresses["splash_palette"] - 0x8000, 32)
            palette: bytes = self.mesen.read_memory(MEMORY_TYPES["NesPaletteRam"], 0, 32)
        except Exception:
            return False

        index: int
        nes_color: int
        for index, nes_color in palette_colors.items():
            if not self._set_prg_rom_bytes(rom_addresses["splash_palette"] + index, bytes([nes_color])):
                return False

            if self.game_state.is_on_splash and palette[index] == splash_palette[index] and palette[index] != nes_color:
                self.pending_writes.append((MEMORY_TYPES["NesPaletteRam"], index, bytes([nes_color])))

        return True

    def _build_level_bar_tiles(self, unlocked_levels: List[int]) -> bytes:
        original_chr_rom: bytes = self.mesen.read_original_chr_rom()
        original_prg_rom: bytes = self.mesen.read_original_prg_rom()

        bar_tiles: bytes = bytes()

        is_lower: bool
        for is_lower in (False, True):
            row_address: int = rom_addresses["options_level_bar_lower_tiles" if is_lower else "options_level_bar_tiles"] - 0x8000

            cell: int
            for cell in range(11):
                tile: bytes = original_chr_rom[options_chr_bank + original_prg_rom[row_address + cell] * 16:][:16]
                low_plane: bytearray = bytearray(16)

                y: int
                for y in range(8):
                    x: int
                    for x in range(8):
                        color: int = ((tile[y] >> (7 - x)) & 1) | (((tile[y + 8] >> (7 - x)) & 1) << 1)

                        if color == 1:
                            is_line: bool = not is_lower and y == 7
                            color = 2 if is_line or cell * 2 + int(x >= 4) in unlocked_levels else 1

                        low_plane[y] |= (color & 1) << (7 - x)
                        low_plane[y + 8] |= (color >> 1) << (7 - x)

                bar_tiles += bytes(low_plane)

        return bar_tiles

    def _set_options_word_palettes(self, words: Dict[Tuple[int, range], bool]) -> bool:
        quadrant_palettes: Dict[Tuple[int, int], int] = dict()

        row: int
        columns: range
        is_locked: bool
        for (row, columns), is_locked in words.items():
            column: int
            for column in columns:
                quadrant_palettes[((row // 4) * 8 + column // 4, ((row % 4) // 2) * 4 + ((column % 4) // 2) * 2)] = 3 if is_locked else 0

        list_names: Tuple[str, ...] = ("options_level_row_attributes", "options_speed_row_attributes", "options_music_row_attributes")

        try:
            cursor_row: int = self.mesen.read_memory(MEMORY_TYPES["NesInternalRam"], ram_addresses["options_cursor_row"], 1)[0]

            row_index: int
            list_name: str
            for row_index, list_name in enumerate(list_names):
                list_address: int = rom_addresses[list_name] - 0x8000
                list_bytes: bytes = self.mesen.read_memory(MEMORY_TYPES["NesPrgRom"], list_address, 70)
                attributes: bytearray = bytearray(list_bytes[3:35] + list_bytes[38:70])

                index: int
                shift: int
                palette: int
                for (index, shift), palette in quadrant_palettes.items():
                    attributes[index] = (attributes[index] & ~(3 << shift)) | (palette << shift)

                for index in sorted({index for index, shift in quadrant_palettes}):
                    if not self._set_prg_rom_bytes(rom_addresses[list_name] + (3 if index < 32 else 6) + index, attributes[index:index + 1]):
                        return False

                    if self.game_state.mode == DrMarioModes.OPTIONS and cursor_row == row_index:
                        attribute_address: Tuple[int, int] = self.mesen.translate_ppu_address(0x23C0 + index)

                        if self.mesen.read_memory(attribute_address[0], attribute_address[1], 1) != attributes[index:index + 1]:
                            self.pending_writes.append((attribute_address[0], attribute_address[1], attributes[index:index + 1]))
        except Exception:
            return False

        return True

    def _set_prg_rom_bytes(self, address: int, patched: bytes) -> bool:
        try:
            if self.mesen.read_memory(MEMORY_TYPES["NesPrgRom"], address - 0x8000, len(patched)) == patched:
                return True
        except Exception:
            return False

        self.pending_writes.append((MEMORY_TYPES["NesPrgRom"], address - 0x8000, patched))

        return True

    def _determine_game_state(self) -> GameState:
        if not self.is_process_running:
            return GameState(is_valid=False)

        try:
            if not self.mesen.is_nes_game_running() or self.mesen.read_rom_hashes()["PrgChrCrc32"] != self.prg_chr_crc32:
                self.close_process_handle()
                self.open_process_handle()

                return GameState(is_valid=False)

            if not self.mesen.is_hooked():
                self.mesen.install_hooks()
                self.mesen.set_watched_memory([(MEMORY_TYPES["NesInternalRam"], 0, 0x800)])

                self.applied_input_effects = list()

            snapshot: Optional[Tuple[int, List[bytes]]] = self.mesen.read_watched_memory()
        except Exception:
            return GameState(is_valid=False)

        if snapshot is None:
            return GameState(is_valid=False)

        ram: bytes = snapshot[1][0]
        player_block: int = player_block_addresses["player_1"]

        mode: Optional[DrMarioModes] = internal_mode_id_to_mode.get(ram[ram_addresses["mode"]])
        is_in_demo: bool = ram[ram_addresses["demo_flag"]] == 0xFE
        viruses_remaining_bcd: int = ram[player_block + player_block_offsets["viruses_remaining"]]
        viruses_remaining: int = (viruses_remaining_bcd >> 4) * 10 + (viruses_remaining_bcd & 0x0F)
        pill_count_bcd: int = ram[player_block + player_block_offsets["pill_count"]]
        pill_count_hundreds_bcd: int = ram[player_block + player_block_offsets["pill_count_hundreds"]]
        last_pill_lines_cleared: int = ram[player_block + player_block_offsets["last_pill_lines_cleared"]]

        return GameState(
            is_valid=True,
            mode=mode,
            is_on_splash=mode == DrMarioModes.TITLE and not is_in_demo,
            is_in_demo=is_in_demo,
            is_paused=mode == DrMarioModes.PLAYING and ram[ram_addresses["frame_animation_enabled"]] == 0 and ram[ram_addresses["ppu_mask"]] == 0x16,
            is_between_levels=mode == DrMarioModes.PLAYING and viruses_remaining == 0,
            is_pill_falling=mode == DrMarioModes.PLAYING and ram[player_block_addresses["active"] + player_block_offsets["pill_phase"]] == 0,
            is_before_first_pill=(
                (mode == DrMarioModes.PLAYING or (mode == DrMarioModes.VIRUS_PLACEMENT and ram[player_block_addresses["active"] + player_block_offsets["viruses_to_place"]] == 0))
                and ram[player_block_addresses["active"] + player_block_offsets["pill_phase"]] == 6
                and ram[player_block_addresses["active"] + player_block_offsets["pill_count"]] == 1
                and ram[player_block_addresses["active"] + player_block_offsets["pill_count_hundreds"]] == 0
            ),
            level=ram[player_block + player_block_offsets["level"]],
            speed=internal_speed_id_to_speed.get(ram[player_block + player_block_offsets["speed"]]),
            speed_ups=ram[player_block_addresses["active"] + player_block_offsets["speed_ups"]],
            music_type=internal_music_type_id_to_music_type.get(ram[ram_addresses["music_type"]]),
            viruses_remaining=viruses_remaining,
            virus_counts={color: ram[ram_addresses["virus_color_counts"] + internal_color_id] for color, internal_color_id in color_to_internal_color_id.items()},
            is_topped_out=bool(ram[player_block + player_block_offsets["topped_out"]]),
            pills_used=max((pill_count_hundreds_bcd >> 4) * 1000 + (pill_count_hundreds_bcd & 0x0F) * 100 + (pill_count_bcd >> 4) * 10 + (pill_count_bcd & 0x0F) - 1, 0),
            last_pill_viruses_destroyed=ram[player_block + player_block_offsets["last_pill_viruses_destroyed"]],
            last_pill_lines_cleared=last_pill_lines_cleared,
            last_pill_line_colors=tuple(internal_color_id_to_color[ram[player_block + player_block_offsets["last_pill_line_colors"] + index] & 0x03] for index in range(min(last_pill_lines_cleared, 4))),
            last_pill_chains=ram[ram_addresses["last_pill_chains"]],
        )

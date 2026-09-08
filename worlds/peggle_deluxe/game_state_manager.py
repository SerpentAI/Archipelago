from typing import List, NamedTuple, Optional, Tuple

import ctypes
import struct

from pymem import Pymem
from pymem.process import close_handle, list_processes
from pymem.ressources.kernel32 import VirtualProtectEx
from pymem.ressources.structure import ProcessEntry32

from .data.mapping_data import id_to_characters, level_to_peg_count, level_to_stage_levels, stage_level_to_levels

from .enums import (
    PeggleDeluxeCharacters,
    PeggleDeluxeContexts,
    PeggleDeluxeGameModes,
    PeggleDeluxeLevels,
    PeggleDeluxeLevelStates,
)


class GameState(NamedTuple):
    context: PeggleDeluxeContexts = PeggleDeluxeContexts.INVALID
    current_game_mode: Optional[PeggleDeluxeGameModes] = None
    current_level: Optional[PeggleDeluxeLevels] = None
    level_state: Optional[PeggleDeluxeLevelStates] = None
    current_character: Optional[PeggleDeluxeCharacters] = None
    current_ball_count: Optional[int] = None
    current_score: Optional[int] = None
    current_shot_score: Optional[int] = None
    current_orange_peg_combo: Optional[int] = None
    current_peg_combo: Optional[int] = None
    current_fever_meter_multiplier: Optional[int] = None
    orange_pegs_remaining: Optional[int] = None
    pegs_cleared: Optional[int] = None
    has_achieved_fever_meter_multiplier_2x: Optional[bool] = None
    has_achieved_fever_meter_multiplier_3x: Optional[bool] = None
    has_achieved_fever_meter_multiplier_5x: Optional[bool] = None
    has_achieved_fever_meter_multiplier_10x: Optional[bool] = None
    has_cleared_level: Optional[bool] = None
    has_achieved_style_shot: Optional[bool] = None
    has_achieved_3_orange_peg_combo: Optional[bool] = None
    has_achieved_5_orange_peg_combo: Optional[bool] = None
    has_achieved_7_peg_combo: Optional[bool] = None
    has_achieved_15_peg_combo: Optional[bool] = None
    has_achieved_full_clear: Optional[bool] = None


class GameStateManager:
    process_name: str = "popcapgame"

    signature_address: int = 0x288BCC
    signature_string: str = "Peggle"

    process: Optional[Pymem]
    is_process_running: bool

    thunderball_app_address: Optional[int]
    player_info_address: Optional[int]
    global_edit_val_address: Optional[int]
    logic_manager_address: Optional[int]

    level_lock_function_address: Optional[int]
    level_lock_mask_address: Optional[int]

    def __init__(self) -> None:
        self.process = None
        self.is_process_running = False

        self.thunderball_app_address = None
        self.player_info_address = None
        self.global_edit_val_address = None
        self.logic_manager_address = None

        self.level_lock_function_address = None
        self.level_lock_mask_address = None

    @property
    def thunderball_app_struct_address(self) -> Optional[int]:
        return self._resolve_address(0x2873AC, (0x0,))

    @property
    def current_game_mode_address(self) -> Optional[int]:
        if self.thunderball_app_struct_address is None:
            return None

        return self.thunderball_app_struct_address + 0x760

    @property
    def current_stage_address(self) -> Optional[int]:
        if self.thunderball_app_struct_address is None:
            return None

        return self.thunderball_app_struct_address + 0x764

    @property
    def current_level_address(self) -> Optional[int]:
        if self.thunderball_app_struct_address is None:
            return None

        return self.thunderball_app_struct_address + 0x768

    @property
    def player_info_struct_address(self) -> Optional[int]:
        return self._resolve_address(0x2873AC, (0x878, 0x0))

    @property
    def maximum_stage_cleared_address(self) -> Optional[int]:
        if self.player_info_struct_address is None:
            return None

        return self.player_info_struct_address + 0x28

    @property
    def maximum_level_cleared_address(self) -> Optional[int]:
        if self.player_info_struct_address is None:
            return None

        return self.player_info_struct_address + 0x2C

    @property
    def challenge_mode_unlocked_address(self) -> Optional[int]:
        if self.player_info_struct_address is None:
            return None

        return self.player_info_struct_address + 0x48

    @property
    def global_edit_val_struct_address(self) -> Optional[int]:
        return self._resolve_address(0x2873AC, (0x320, 0x88, 0x150, 0x90, 0x0))

    @property
    def logic_manager_struct_address(self) -> Optional[int]:
        return self._resolve_address(0x2873AC, (0x320, 0x88, 0x154, 0x0))

    @property
    def level_state_address(self) -> Optional[int]:
        if self.logic_manager_struct_address is None:
            return None

        return self.logic_manager_struct_address + 0x4

    @property
    def instant_replay_address(self) -> Optional[int]:
        if self.logic_manager_struct_address is None:
            return None

        return self.logic_manager_struct_address + 0xF4

    @property
    def current_ball_count_address(self) -> Optional[int]:
        if self.logic_manager_struct_address is None:
            return None

        return self.logic_manager_struct_address + 0x17C

    @property
    def current_character_address(self) -> Optional[int]:
        if self.logic_manager_struct_address is None:
            return None

        return self.logic_manager_struct_address + 0x184

    @property
    def current_score_address(self) -> Optional[int]:
        if self.logic_manager_struct_address is None:
            return None

        return self.logic_manager_struct_address + 0x174

    @property
    def current_shot_green_pegs_hit_address(self) -> Optional[int]:
        if self.logic_manager_struct_address is None:
            return None

        return self.logic_manager_struct_address + 0x50

    @property
    def current_shot_orange_pegs_hit_address(self) -> Optional[int]:
        if self.logic_manager_struct_address is None:
            return None

        return self.logic_manager_struct_address + 0x4C

    @property
    def current_shot_score_multiplied_address(self) -> Optional[int]:
        if self.logic_manager_struct_address is None:
            return None

        return self.logic_manager_struct_address + 0x108

    @property
    def current_shot_score_raw_address(self) -> Optional[int]:
        if self.logic_manager_struct_address is None:
            return None

        return self.logic_manager_struct_address + 0x10C

    @property
    def current_shot_style_score_address(self) -> Optional[int]:
        if self.logic_manager_struct_address is None:
            return None

        return self.logic_manager_struct_address + 0x110

    @property
    def current_shot_total_pegs_hit_address(self) -> Optional[int]:
        if self.logic_manager_struct_address is None:
            return None

        return self.logic_manager_struct_address + 0x12C

    @property
    def current_fever_score_address(self) -> Optional[int]:
        if self.logic_manager_struct_address is None:
            return None

        return self.logic_manager_struct_address + 0x164

    @property
    def current_fever_meter_multiplier_address(self) -> Optional[int]:
        if self.logic_manager_struct_address is None:
            return None

        return self.logic_manager_struct_address + 0x114

    @property
    def orange_pegs_remaining_address(self) -> Optional[int]:
        if self.logic_manager_struct_address is None:
            return None

        return self.logic_manager_struct_address + 0x360

    @property
    def pegs_cleared_address(self) -> Optional[int]:
        if self.logic_manager_struct_address is None:
            return None

        return self.logic_manager_struct_address + 0x120

    def get_current_game_mode(self) -> Optional[PeggleDeluxeGameModes]:
        if self.current_game_mode_address is None:
            return None

        try:
            current_game_mode_value: int = self.process.read_int(self.current_game_mode_address)

            return PeggleDeluxeGameModes(current_game_mode_value)
        except Exception:
            return PeggleDeluxeGameModes.OTHER

    def get_current_stage_level(self) -> Optional[Tuple[int, int]]:
        if self.current_stage_address is None or self.current_level_address is None:
            return None

        try:
            current_stage: int = self.process.read_int(self.current_stage_address)
            current_level: int = self.process.read_int(self.current_level_address)

            return current_stage, current_level
        except Exception:
            return None

    def get_current_stage_level_string(self) -> Optional[str]:
        stage_level: Optional[Tuple[int, int]] = self.get_current_stage_level()

        if stage_level is None:
            return None

        return f"{stage_level[0] + 1}-{stage_level[1] + 1}"

    def get_current_level(self) -> Optional[PeggleDeluxeLevels]:
        stage_level: Optional[Tuple[int, int]] = self.get_current_stage_level()

        if stage_level is None:
            return None

        return stage_level_to_levels.get(stage_level)

    def are_quick_play_levels_unlocked(self) -> bool:
        if self.maximum_stage_cleared_address is None or self.maximum_level_cleared_address is None:
            return False

        try:
            maximum_stage_cleared: int = self.process.read_int(self.maximum_stage_cleared_address)
            maximum_level_cleared: int = self.process.read_int(self.maximum_level_cleared_address)

            return (maximum_stage_cleared, maximum_level_cleared) == (10, 5)
        except Exception:
            return False

    def unlock_quick_play_levels(self) -> bool:
        if self.maximum_stage_cleared_address is None or self.maximum_level_cleared_address is None:
            return False

        try:
            self.process.write_int(self.maximum_stage_cleared_address, 10)
            self.process.write_int(self.maximum_level_cleared_address, 5)

            return True
        except Exception:
            return False

    def is_challenge_mode_unlocked(self) -> bool:
        if self.challenge_mode_unlocked_address is None:
            return False

        try:
            challenge_mode_unlocked: int = self.process.read_int(self.challenge_mode_unlocked_address)

            return challenge_mode_unlocked == 1
        except Exception:
            return False

    def unlock_challenge_mode(self) -> bool:
        if self.challenge_mode_unlocked_address is None:
            return False

        try:
            self.process.write_int(self.challenge_mode_unlocked_address, 1)

            return True
        except Exception:
            return False

    def is_playing_a_level(self) -> bool:
        try:
            self.process.read_int(self.global_edit_val_struct_address)
            return True
        except Exception:
            return False

    def get_level_state(self) -> Optional[PeggleDeluxeLevelStates]:
        if self.level_state_address is None:
            return None

        try:
            level_state_value: int = self.process.read_int(self.level_state_address)

            return PeggleDeluxeLevelStates(level_state_value)
        except Exception:
            return PeggleDeluxeLevelStates.OTHER

    def is_instant_replay(self) -> bool:
        if self.instant_replay_address is None:
            return False

        try:
            instant_replay: int = self.process.read_int(self.instant_replay_address)

            return instant_replay == 256
        except Exception:
            return False

    def get_current_ball_count(self) -> Optional[int]:
        if self.current_ball_count_address is None:
            return None

        try:
            return self.process.read_int(self.current_ball_count_address)
        except Exception:
            return None

    def set_current_ball_count(self, ball_count: int) -> bool:
        if self.current_ball_count_address is None:
            return False

        try:
            self.process.write_int(self.current_ball_count_address, ball_count)
            return True
        except Exception:
            return False

    def get_current_character(self) -> Optional[PeggleDeluxeCharacters]:
        if self.current_character_address is None:
            return None

        try:
            character_id: int = self.process.read_int(self.current_character_address)

            return id_to_characters.get(character_id)
        except Exception:
            return None

    def get_current_score(self) -> Optional[int]:
        if self.current_score_address is None:
            return None

        try:
            return self.process.read_int(self.current_score_address)
        except Exception:
            return None

    def get_current_shot_green_pegs_hit(self) -> Optional[int]:
        if self.current_shot_green_pegs_hit_address is None:
            return None

        try:
            return self.process.read_int(self.current_shot_green_pegs_hit_address)
        except Exception:
            return None

    def get_current_shot_orange_pegs_hit(self) -> Optional[int]:
        if self.current_shot_orange_pegs_hit_address is None:
            return None

        try:
            return self.process.read_int(self.current_shot_orange_pegs_hit_address)
        except Exception:
            return None

    def has_achieved_3_orange_peg_combo(self) -> bool:
        orange_pegs_hit: Optional[int] = self.get_current_shot_orange_pegs_hit()

        if orange_pegs_hit is None:
            return False

        return orange_pegs_hit >= 3

    def has_achieved_5_orange_peg_combo(self) -> bool:
        orange_pegs_hit: Optional[int] = self.get_current_shot_orange_pegs_hit()

        if orange_pegs_hit is None:
            return False

        return orange_pegs_hit >= 5

    def get_current_shot_score_multiplied(self) -> Optional[int]:
        if self.current_shot_score_multiplied_address is None:
            return None

        try:
            return self.process.read_int(self.current_shot_score_multiplied_address)
        except Exception:
            return None

    def get_current_shot_score_raw(self) -> Optional[int]:
        if self.current_shot_score_raw_address is None:
            return None

        try:
            return self.process.read_int(self.current_shot_score_raw_address)
        except Exception:
            return None

    def get_current_shot_style_score(self) -> Optional[int]:
        if self.current_shot_style_score_address is None:
            return None

        try:
            return self.process.read_int(self.current_shot_style_score_address)
        except Exception:
            return None

    def has_achieved_style_shot(self) -> bool:
        style_score: Optional[int] = self.get_current_shot_style_score()

        if style_score is None:
            return False

        return style_score >= 25000

    def get_current_shot_total_pegs_hit(self) -> Optional[int]:
        if self.current_shot_total_pegs_hit_address is None:
            return None

        try:
            return self.process.read_int(self.current_shot_total_pegs_hit_address)
        except Exception:
            return None

    def has_achieved_7_peg_combo(self) -> bool:
        total_pegs_hit: Optional[int] = self.get_current_shot_total_pegs_hit()

        if total_pegs_hit is None:
            return False

        return total_pegs_hit >= 7

    def has_achieved_15_peg_combo(self) -> bool:
        total_pegs_hit: Optional[int] = self.get_current_shot_total_pegs_hit()

        if total_pegs_hit is None:
            return False

        return total_pegs_hit >= 15

    def get_current_fever_score(self) -> Optional[int]:
        if self.current_fever_score_address is None:
            return None

        try:
            return self.process.read_int(self.current_fever_score_address)
        except Exception:
            return None

    def has_cleared_level(self) -> bool:
        current_fever_score: Optional[int] = self.get_current_fever_score()

        if current_fever_score is None:
            return False
        elif self.get_orange_pegs_remaining() != 0:
            return False

        return current_fever_score > 0

    def get_current_fever_meter_multiplier(self) -> Optional[int]:
        if self.current_fever_meter_multiplier_address is None:
            return None

        try:
            return self.process.read_int(self.current_fever_meter_multiplier_address)
        except Exception:
            return None

    def set_current_fever_meter_multiplier(self, multiplier: int) -> None:
        if self.current_fever_meter_multiplier_address is None:
            return

        try:
            self.process.write_int(self.current_fever_meter_multiplier_address, multiplier)
        except Exception:
            return

    def has_achieved_fever_meter_multiplier(self, multiplier: int) -> bool:
        current_multiplier: Optional[int] = self.get_current_fever_meter_multiplier()

        if current_multiplier is None:
            return False

        return current_multiplier >= multiplier

    def get_orange_pegs_remaining(self) -> Optional[int]:
        if self.orange_pegs_remaining_address is None:
            return None

        try:
            return self.process.read_int(self.orange_pegs_remaining_address)
        except Exception:
            return None

    def set_orange_pegs_remaining(self, remaining: int) -> None:
        if self.orange_pegs_remaining_address is None:
            return

        try:
            self.process.write_int(self.orange_pegs_remaining_address, remaining)
        except Exception:
            return

    def get_pegs_cleared(self) -> Optional[int]:
        if self.pegs_cleared_address is None:
            return None

        try:
            return self.process.read_int(self.pegs_cleared_address)
        except Exception:
            return None

    def has_achieved_full_clear(self) -> bool:
        level: PeggleDeluxeLevels = self.get_current_level()
        pegs_cleared: Optional[int] = self.get_pegs_cleared()

        if pegs_cleared is None:
            return False

        return pegs_cleared >= level_to_peg_count.get(level, 999999)

    def open_process_handle(self) -> bool:
        # The system could have multiple PopCap games running at once, and they all share the same executable name
        # so we need to look for a signature to know which one is the right process to open a handle to.
        try:
            candidate_pids: List[int] = list()

            process: ProcessEntry32
            for process in list_processes():
                if self.process_name.lower() in process.szExeFile.decode("utf-8").lower():
                    candidate_pids.append(process.th32ProcessID)

            if not len(candidate_pids):
                return False

            pid: int
            for pid in candidate_pids:
                try:
                    process: Pymem = Pymem(pid)
                    address: int = process.base_address + self.signature_address

                    if process.read_string(address, len(self.signature_string)) == self.signature_string:
                        self.process = process
                        self.is_process_running = True

                        break
                except Exception:
                    pass

            if not self.is_process_running:
                return False

            self.thunderball_app_address = self.thunderball_app_struct_address
            self.player_info_address = self.player_info_struct_address
            self.global_edit_val_address = self.global_edit_val_struct_address
            self.logic_manager_address = self.logic_manager_struct_address
        except Exception:
            return False

        return True

    def close_process_handle(self) -> bool:
        if close_handle(self.process.process_handle):
            self.is_process_running = False
            self.process = None

            self.thunderball_app_address = None
            self.player_info_address = None
            self.global_edit_val_address = None
            self.logic_manager_address = None

            return True

        return False

    def is_process_still_running(self) -> bool:
        try:
            self.process.read_int(self.process.base_address)
        except Exception:
            self.is_process_running = False
            self.process = None

            self.thunderball_app_address = None
            self.player_info_address = None
            self.global_edit_val_address = None
            self.logic_manager_address = None

            return False

        return True

    def determine_game_state(self) -> GameState:
        self.thunderball_app_address = self.thunderball_app_struct_address
        self.player_info_address = self.player_info_struct_address
        self.global_edit_val_address = self.global_edit_val_struct_address
        self.logic_manager_address = self.logic_manager_struct_address

        game_mode: PeggleDeluxeGameModes = self.get_current_game_mode()
        is_quick_play: bool = game_mode == PeggleDeluxeGameModes.QUICK_PLAY

        if not is_quick_play or not self.is_playing_a_level() or self.is_instant_replay():
            return GameState(context=PeggleDeluxeContexts.INVALID, current_game_mode=game_mode)

        return GameState(
            context=PeggleDeluxeContexts.VALID,
            current_game_mode=game_mode,
            current_level=self.get_current_level(),
            level_state=self.get_level_state(),
            current_character=self.get_current_character(),
            current_ball_count=self.get_current_ball_count(),
            current_score=self.get_current_score(),
            current_shot_score=self.get_current_shot_score_multiplied(),
            current_orange_peg_combo=self.get_current_shot_orange_pegs_hit(),
            current_peg_combo=self.get_current_shot_total_pegs_hit(),
            current_fever_meter_multiplier=self.get_current_fever_meter_multiplier(),
            orange_pegs_remaining=self.get_orange_pegs_remaining(),
            pegs_cleared=self.get_pegs_cleared(),
            has_achieved_fever_meter_multiplier_2x=self.has_achieved_fever_meter_multiplier(2),
            has_achieved_fever_meter_multiplier_3x=self.has_achieved_fever_meter_multiplier(3),
            has_achieved_fever_meter_multiplier_5x=self.has_achieved_fever_meter_multiplier(5),
            has_achieved_fever_meter_multiplier_10x=self.has_achieved_fever_meter_multiplier(10),
            has_cleared_level=self.has_cleared_level(),
            has_achieved_style_shot=self.has_achieved_style_shot(),
            has_achieved_3_orange_peg_combo=self.has_achieved_3_orange_peg_combo(),
            has_achieved_5_orange_peg_combo=self.has_achieved_5_orange_peg_combo(),
            has_achieved_7_peg_combo=self.has_achieved_7_peg_combo(),
            has_achieved_15_peg_combo=self.has_achieved_15_peg_combo(),
            has_achieved_full_clear=self.has_achieved_full_clear(),
        )

    def set_unlocked_levels(self, unlocked_levels: List[PeggleDeluxeLevels]) -> bool:
        if not self.is_process_running or self.level_lock_mask_address is None:
            return False

        try:
            mask: int = 0

            level: PeggleDeluxeLevels
            for level in unlocked_levels:
                stage_level: Optional[Tuple[int, int]] = level_to_stage_levels.get(level)

                if stage_level is None:
                    continue

                stage: int
                level_index: int
                stage, level_index = stage_level

                bit_index: int = stage * 5 + level_index

                if 0 <= bit_index < 64:
                    mask |= 1 << bit_index

            self.process.write_bytes(self.level_lock_mask_address, struct.pack("<Q", mask), 8)

            return True
        except Exception:
            return False

    def install_level_lock_hook(self) -> bool:
        if not self.is_process_running:
            return False

        if self.level_lock_function_address is not None:
            return True

        try:
            function_address: int = self.process.base_address + 0x93600

            existing_prologue: bytes = self.process.read_bytes(function_address, 5)

            if existing_prologue[0] == 0xE9:
                return False

            if existing_prologue != b"\x55\x8B\xEC\x56\x57":
                return False

            return_address: int = function_address + 0x5

            mask_address: int = self.process.allocate(8)
            cave_address: int = self.process.allocate(256)

            self.process.write_bytes(mask_address, struct.pack("<Q", 0), 8)

            cave_bytes: bytes = self._build_level_lock_cave_bytes(cave_address, mask_address, return_address)
            self.process.write_bytes(cave_address, cave_bytes, len(cave_bytes))

            relative_target: int = cave_address - (function_address + 0x5)
            hook_bytes: bytes = b"\xE9" + struct.pack("<i", relative_target)

            if not self._write_executable_bytes(function_address, hook_bytes):
                return False

            if self.process.read_bytes(function_address, 5) != hook_bytes:
                return False

            self.level_lock_function_address = function_address
            self.level_lock_mask_address = mask_address

            return True
        except Exception:
            return False

    @staticmethod
    def _build_level_lock_cave_bytes(cave_address: int, mask_address: int, return_address: int) -> bytes:
        instruction_bytes: List[bytes] = list()

        instruction_bytes.append(b"\x8B\x81\xA8\x00\x00\x00")  # mov eax, [ecx+0xA8]
        instruction_bytes.append(b"\x8B\x54\x24\x04")  # mov edx, [esp+4]
        instruction_bytes.append(b"\x8D\x04\x80")  # lea eax, [eax+eax*4]
        instruction_bytes.append(b"\x03\xC2")  # add eax, edx
        instruction_bytes.append(b"\x0F\xA3\x05" + struct.pack("<I", mask_address))  # bt [mask], eax
        instruction_bytes.append(b"\x72\x05")  # jc +5

        instruction_bytes.append(b"\x31\xC0")  # xor eax, eax
        instruction_bytes.append(b"\xC2\x04\x00")  # ret 4

        instruction_bytes.append(b"\x55")  # push ebp
        instruction_bytes.append(b"\x8B\xEC")  # mov ebp, esp
        instruction_bytes.append(b"\x56")  # push esi
        instruction_bytes.append(b"\x57")  # push edi

        bytes_before_jump: int = sum(len(chunk) for chunk in instruction_bytes)
        jump_instruction_address: int = cave_address + bytes_before_jump
        relative_target: int = return_address - (jump_instruction_address + 5)

        instruction_bytes.append(b"\xE9" + struct.pack("<i", relative_target))  # jmp return_address

        return b"".join(instruction_bytes)

    def _write_executable_bytes(self, address: int, data: bytes) -> bool:
        previous_protection: ctypes.c_ulong = ctypes.c_ulong(0)

        did_change_protection: bool = bool(
            VirtualProtectEx(
                self.process.process_handle,
                ctypes.c_void_p(address),
                len(data),
                0x40,
                ctypes.byref(previous_protection),
            )
        )

        if not did_change_protection:
            return False

        self.process.write_bytes(address, data, len(data))

        VirtualProtectEx(
            self.process.process_handle,
            ctypes.c_void_p(address),
            len(data),
            previous_protection.value,
            ctypes.byref(previous_protection),
        )

        return True

    # Use readuint for 32-bit processes, readlonglong for 64-bit processes
    def _resolve_address(self, base_offset: int, offsets: Tuple[int, ...]) -> Optional[int]:
        address: int = self.process.read_uint(self.process.base_address + base_offset)

        for offset in offsets[:-1]:
            try:
                address = self.process.read_uint(address + offset)
            except Exception:
                return None

        return address + offsets[-1]

from typing import Any, Dict, List, NamedTuple, Optional, Tuple, Union

import ctypes
import struct

from pymem import Pymem
from pymem.process import close_handle

from .data.game_data import level_to_internal_name_reverse

from .enums import MirrorsEdgeContexts, MirrorsEdgeLevels


class GameState(NamedTuple):
    context: MirrorsEdgeContexts
    level: Optional[MirrorsEdgeLevels]


class GameStateManager:
    process_name: str = "MirrorsEdge.exe"

    gnames_offset: int = 0x1C4E7D8
    gobjects_offset: int = 0x1C4A344
    gworld_offset: int = 0x1C3F80C  # Likely wrong, but went unused since we have a solid pointer to TdGameEngine

    process_event_proxy_offset: int = 0x78E5D0

    process: Optional[Pymem]
    is_process_running: bool

    gnames_mapping: Dict[int, str]
    gnames_mapping_reverse: Dict[str, int]

    gobjects_name_to_object: Dict[str, List[Dict[str, Any]]]
    gobjects_address_to_object: Dict[int, Dict[str, Any]]

    game_engine_offset: int = 0x1BF8B20

    move_cdo_addresses: Optional[Dict[str, int]]
    sp_time_trial_game_address: Optional[int]

    def __init__(self) -> None:
        self.process = None
        self.is_process_running = False

        self.gnames_mapping = dict()
        self.gnames_mapping_reverse = dict()

        self.gobjects_name_to_object = dict()
        self.gobjects_address_to_object = dict()

        self.move_cdo_addresses = None
        self.sp_time_trial_game_address = None

    def open_process_handle(self) -> bool:
        try:
            self.process = Pymem(self.process_name)
            self.is_process_running = True

            self._generate_gnames_mapping()

            self.gnames_mapping_reverse = {v: k for k, v in self.gnames_mapping.items()}

            self._refresh_gobjects_mapping()

            self.discover_move_cdo_addresses()
        except Exception:
            return False

        return True

    def close_process_handle(self) -> bool:
        if close_handle(self.process.process_handle):
            self.is_process_running = False
            self.process = None

            self.gnames_mapping = dict()
            self.gnames_mapping_reverse = dict()

            self.gobjects_name_to_object = dict()
            self.gobjects_address_to_object = dict()

            self.move_cdo_addresses = None
            self.sp_time_trial_game_address = None

            return True

        return False

    def is_process_still_running(self) -> bool:
        try:
            self.process.read_int(self.process.base_address)
        except Exception:
            self.is_process_running = False
            self.process = None

            self.gnames_mapping = dict()
            self.gnames_mapping_reverse = dict()

            self.gobjects_name_to_object = dict()
            self.gobjects_address_to_object = dict()

            self.move_cdo_addresses = None
            self.sp_time_trial_game_address = None

            return False

        return True

    def determine_game_state(self) -> GameState:
        player_controller_address: int = self._resolve_address(self.game_engine_offset, (0x2BC, 0x0, 0x40, 0x0)) or 0

        if player_controller_address == 0:
            return GameState(
                context=MirrorsEdgeContexts.INVALID,
                level=None,
            )

        level_internal_name: str = self.get_level_internal_name()

        if level_internal_name == "TdMainMenu":
            return GameState(
                context=MirrorsEdgeContexts.MENU,
                level=None,
            )
        elif level_internal_name in level_to_internal_name_reverse:
            return GameState(
                context=MirrorsEdgeContexts.LEVEL,
                level=level_to_internal_name_reverse[level_internal_name],
            )

        return GameState(
            context=MirrorsEdgeContexts.INVALID,
            level=None,
        )

    def prepare_for_menu_routine(self) -> None:
        self._refresh_gobjects_mapping()

    def prepare_for_level_routine(self) -> None:
        self._refresh_gobjects_mapping()

        self.discover_sp_time_trial_game_address()

    def discover_move_cdo_addresses(self) -> None:
        move_cdo_addresses: Dict[str, int] = dict()

        move_class_names: List[str] = [
            "TdMove_Balance",
            "TdMove_IntoClimb",
            "TdMove_Coil",
            "TdMove_DodgeJump",
            "TdMove_180Turn",
            "TdMove_180TurnInAir",
            "TdMove_Barge",
            "TdMove_AirBarge",
            "TdMove_Grab",
            "TdMove_GrabJump",
            "TdMove_Melee",
            "TdMove_MeleeAir",
            "TdMove_MeleeWallrun",
            "TdMove_WallClimb",
            "TdMove_WallClimb180TurnJump",
            "TdMove_WallRun",
            "TdMove_WallrunJump",
            "TdMove_SpringBoard",
            "TdMove_Swing",
            "TdMove_VaultOver",
            "TdMove_IntoZipLine",
        ]

        move_class_name: str
        for move_class_name in move_class_names:
            instance_name: str
            instance_data: List[Dict[str, Any]]
            for instance_name, instance_data in self._find_instances_of_class(move_class_name).items():
                if instance_name.startswith("Default__"):
                    move_cdo_addresses[move_class_name] = instance_data[0]["address"]

        self.move_cdo_addresses = move_cdo_addresses

    def get_level_internal_name(self):
        if not self.is_process_still_running():
            return None

        internal_name_string_size: int = self.process.read_int(self._resolve_address(self.game_engine_offset, (0x0,)) + 0x3D0) * 2 - 2
        internal_name_string_address: int = self._resolve_address(self.game_engine_offset, (0x3CC, 0x0))

        internal_name_string_bytes: bytes = self.process.read_bytes(internal_name_string_address, internal_name_string_size)
        return internal_name_string_bytes.decode("utf-16-le", errors="ignore")

    def disable_all_moves(self) -> None:
        self.disable_balance()
        self.disable_climb()
        self.disable_coil()
        self.disable_dodge_jump()
        self.disable_180_turn()
        self.disable_airborne_180_turn()
        self.disable_barge()
        self.disable_grab()
        self.disable_grab_jump()
        self.disable_melee_attack()
        self.disable_wall_climb()
        self.disable_wall_climb_180_turn_jump()
        self.disable_wall_run()
        self.disable_wall_run_jump()
        self.disable_springboard()
        self.disable_swing()
        self.disable_vault()
        self.disable_zipline()

    def disable_balance(self) -> Optional[bool]:
        if not self.is_process_still_running():
            return None
        elif not self.move_cdo_addresses or "TdMove_Balance" not in self.move_cdo_addresses:
            return None

        balance_cdo_address: int = self.move_cdo_addresses["TdMove_Balance"]

        self.process.write_float(balance_cdo_address + 0x84, 1.0)
        self.process.write_float(balance_cdo_address + 0x8C, 999999999.0)

        return True

    def enable_balance(self) -> Optional[bool]:
        if not self.is_process_still_running():
            return None
        elif not self.move_cdo_addresses or "TdMove_Balance" not in self.move_cdo_addresses:
            return None

        balance_cdo_address: int = self.move_cdo_addresses["TdMove_Balance"]

        self.process.write_float(balance_cdo_address + 0x84, -10.0)
        self.process.write_float(balance_cdo_address + 0x8C, 0.5)

        return True

    def disable_climb(self) -> Optional[bool]:
        if not self.is_process_still_running():
            return None
        elif not self.move_cdo_addresses or "TdMove_IntoClimb" not in self.move_cdo_addresses:
            return None

        climb_cdo_address: int = self.move_cdo_addresses["TdMove_IntoClimb"]

        self.process.write_float(climb_cdo_address + 0x84, 1.0)
        self.process.write_float(climb_cdo_address + 0x8C, 999999999.0)

        return True

    def enable_climb(self) -> Optional[bool]:
        if not self.is_process_still_running():
            return None
        elif not self.move_cdo_addresses or "TdMove_IntoClimb" not in self.move_cdo_addresses:
            return None

        climb_cdo_address: int = self.move_cdo_addresses["TdMove_IntoClimb"]

        self.process.write_float(climb_cdo_address + 0x84, -10.0)
        self.process.write_float(climb_cdo_address + 0x8C, 0.5)

        return True

    def disable_coil(self) -> Optional[bool]:
        if not self.is_process_still_running():
            return None
        elif not self.move_cdo_addresses or "TdMove_Coil" not in self.move_cdo_addresses:
            return None

        coil_cdo_address: int = self.move_cdo_addresses["TdMove_Coil"]

        self.process.write_float(coil_cdo_address + 0x84, 1.0)
        self.process.write_float(coil_cdo_address + 0x8C, 999999999.0)

        return True

    def enable_coil(self) -> Optional[bool]:
        if not self.is_process_still_running():
            return None
        elif not self.move_cdo_addresses or "TdMove_Coil" not in self.move_cdo_addresses:
            return None

        coil_cdo_address: int = self.move_cdo_addresses["TdMove_Coil"]

        self.process.write_float(coil_cdo_address + 0x84, -10.0)
        self.process.write_float(coil_cdo_address + 0x8C, 0.0)

        return True

    def disable_dodge_jump(self) -> Optional[bool]:
        if not self.is_process_still_running():
            return None
        elif not self.move_cdo_addresses or "TdMove_DodgeJump" not in self.move_cdo_addresses:
            return None

        dodge_jump_cdo_address: int = self.move_cdo_addresses["TdMove_DodgeJump"]

        self.process.write_float(dodge_jump_cdo_address + 0x84, 1.0)
        self.process.write_float(dodge_jump_cdo_address + 0x8C, 999999999.0)

        return True

    def enable_dodge_jump(self) -> Optional[bool]:
        if not self.is_process_still_running():
            return None
        elif not self.move_cdo_addresses or "TdMove_DodgeJump" not in self.move_cdo_addresses:
            return None

        dodge_jump_cdo_address: int = self.move_cdo_addresses["TdMove_DodgeJump"]

        self.process.write_float(dodge_jump_cdo_address + 0x84, -10.0)
        self.process.write_float(dodge_jump_cdo_address + 0x8C, 0.3)

        return True

    def disable_180_turn(self) -> Optional[bool]:
        if not self.is_process_still_running():
            return None
        elif not self.move_cdo_addresses or "TdMove_180Turn" not in self.move_cdo_addresses:
            return None

        turn_cdo_address: int = self.move_cdo_addresses["TdMove_180Turn"]

        self.process.write_float(turn_cdo_address + 0x84, 1.0)
        self.process.write_float(turn_cdo_address + 0x8C, 999999999.0)

        return True

    def enable_180_turn(self) -> Optional[bool]:
        if not self.is_process_still_running():
            return None
        elif not self.move_cdo_addresses or "TdMove_180Turn" not in self.move_cdo_addresses:
            return None

        turn_cdo_address: int = self.move_cdo_addresses["TdMove_180Turn"]

        self.process.write_float(turn_cdo_address + 0x84, -10.0)
        self.process.write_float(turn_cdo_address + 0x8C, 0.5)

        return True

    def disable_airborne_180_turn(self) -> Optional[bool]:
        if not self.is_process_still_running():
            return None
        elif not self.move_cdo_addresses or "TdMove_180TurnInAir" not in self.move_cdo_addresses:
            return None

        turn_cdo_address: int = self.move_cdo_addresses["TdMove_180TurnInAir"]

        self.process.write_float(turn_cdo_address + 0x84, 1.0)
        self.process.write_float(turn_cdo_address + 0x8C, 999999999.0)

        return True

    def enable_airborne_180_turn(self) -> Optional[bool]:
        if not self.is_process_still_running():
            return None
        elif not self.move_cdo_addresses or "TdMove_180TurnInAir" not in self.move_cdo_addresses:
            return None

        turn_cdo_address: int = self.move_cdo_addresses["TdMove_180TurnInAir"]

        self.process.write_float(turn_cdo_address + 0x84, -10.0)
        self.process.write_float(turn_cdo_address + 0x8C, 0.0)

        return True

    def disable_barge(self) -> Optional[bool]:
        if not self.is_process_still_running():
            return None
        elif not self.move_cdo_addresses or "TdMove_Barge" not in self.move_cdo_addresses:
            return None
        elif not self.move_cdo_addresses or "TdMove_AirBarge" not in self.move_cdo_addresses:
            return None

        barge_cdo_address: int = self.move_cdo_addresses["TdMove_Barge"]

        self.process.write_float(barge_cdo_address + 0x84, 1.0)
        self.process.write_float(barge_cdo_address + 0x8C, 999999999.0)

        airborne_barge_cdo_address: int = self.move_cdo_addresses["TdMove_AirBarge"]

        self.process.write_float(airborne_barge_cdo_address + 0x84, 1.0)
        self.process.write_float(airborne_barge_cdo_address + 0x8C, 999999999.0)

        return True

    def enable_barge(self) -> Optional[bool]:
        if not self.is_process_still_running():
            return None
        elif not self.move_cdo_addresses or "TdMove_Barge" not in self.move_cdo_addresses:
            return None
        elif not self.move_cdo_addresses or "TdMove_AirBarge" not in self.move_cdo_addresses:
            return None

        barge_cdo_address: int = self.move_cdo_addresses["TdMove_Barge"]

        self.process.write_float(barge_cdo_address + 0x84, -10.0)
        self.process.write_float(barge_cdo_address + 0x8C, 0.1)

        airborne_barge_cdo_address: int = self.move_cdo_addresses["TdMove_AirBarge"]

        self.process.write_float(airborne_barge_cdo_address + 0x84, -10.0)
        self.process.write_float(airborne_barge_cdo_address + 0x8C, 0.1)

        return True

    def disable_grab(self) -> Optional[bool]:
        if not self.is_process_still_running():
            return None
        elif not self.move_cdo_addresses or "TdMove_Grab" not in self.move_cdo_addresses:
            return None

        grab_cdo_address: int = self.move_cdo_addresses["TdMove_Grab"]

        self.process.write_float(grab_cdo_address + 0x84, 1.0)
        self.process.write_float(grab_cdo_address + 0x8C, 999999999.0)

        return True

    def enable_grab(self) -> Optional[bool]:
        if not self.is_process_still_running():
            return None
        elif not self.move_cdo_addresses or "TdMove_Grab" not in self.move_cdo_addresses:
            return None

        grab_cdo_address: int = self.move_cdo_addresses["TdMove_Grab"]

        self.process.write_float(grab_cdo_address + 0x84, -10.0)
        self.process.write_float(grab_cdo_address + 0x8C, 0.15)

        return True

    def disable_grab_jump(self) -> Optional[bool]:
        if not self.is_process_still_running():
            return None
        elif not self.move_cdo_addresses or "TdMove_GrabJump" not in self.move_cdo_addresses:
            return None

        grab_jump_cdo_address: int = self.move_cdo_addresses["TdMove_GrabJump"]

        self.process.write_float(grab_jump_cdo_address + 0x84, 1.0)
        self.process.write_float(grab_jump_cdo_address + 0x8C, 999999999.0)

        return True

    def enable_grab_jump(self) -> Optional[bool]:
        if not self.is_process_still_running():
            return None
        elif not self.move_cdo_addresses or "TdMove_GrabJump" not in self.move_cdo_addresses:
            return None

        grab_jump_cdo_address: int = self.move_cdo_addresses["TdMove_GrabJump"]

        self.process.write_float(grab_jump_cdo_address + 0x84, -10.0)
        self.process.write_float(grab_jump_cdo_address + 0x8C, 0.0)

        return True

    def disable_melee_attack(self) -> Optional[bool]:
        if not self.is_process_still_running():
            return None
        elif not self.move_cdo_addresses or "TdMove_Melee" not in self.move_cdo_addresses:
            return None
        elif not self.move_cdo_addresses or "TdMove_MeleeAir" not in self.move_cdo_addresses:
            return None

        melee_cdo_address: int = self.move_cdo_addresses["TdMove_Melee"]

        self.process.write_float(melee_cdo_address + 0x84, 1.0)
        self.process.write_float(melee_cdo_address + 0x8C, 999999999.0)

        airborne_melee_cdo_address: int = self.move_cdo_addresses["TdMove_MeleeAir"]

        self.process.write_float(airborne_melee_cdo_address + 0x84, 1.0)
        self.process.write_float(airborne_melee_cdo_address + 0x8C, 999999999.0)

        return True

    def enable_melee_attack(self) -> Optional[bool]:
        if not self.is_process_still_running():
            return None
        elif not self.move_cdo_addresses or "TdMove_Melee" not in self.move_cdo_addresses:
            return None
        elif not self.move_cdo_addresses or "TdMove_MeleeAir" not in self.move_cdo_addresses:
            return None

        melee_cdo_address: int = self.move_cdo_addresses["TdMove_Melee"]

        self.process.write_float(melee_cdo_address + 0x84, -10.0)
        self.process.write_float(melee_cdo_address + 0x8C, 0.0)

        airborne_melee_cdo_address: int = self.move_cdo_addresses["TdMove_MeleeAir"]

        self.process.write_float(airborne_melee_cdo_address + 0x84, -10.0)
        self.process.write_float(airborne_melee_cdo_address + 0x8C, 0.3)

        return True

    def disable_wall_climb(self) -> Optional[bool]:
        if not self.is_process_still_running():
            return None
        elif not self.move_cdo_addresses or "TdMove_WallClimb" not in self.move_cdo_addresses:
            return None

        wall_climb_cdo_address: int = self.move_cdo_addresses["TdMove_WallClimb"]

        self.process.write_float(wall_climb_cdo_address + 0x84, 1.0)
        self.process.write_float(wall_climb_cdo_address + 0x8C, 999999999.0)
        self.process.write_float(wall_climb_cdo_address + 0x198, 0.0)

        return True

    def enable_wall_climb(self) -> Optional[bool]:
        if not self.is_process_still_running():
            return None
        elif not self.move_cdo_addresses or "TdMove_WallClimb" not in self.move_cdo_addresses:
            return None

        wall_climb_cdo_address: int = self.move_cdo_addresses["TdMove_WallClimb"]

        self.process.write_float(wall_climb_cdo_address + 0x84, -10.0)
        self.process.write_float(wall_climb_cdo_address + 0x8C, 0.0)
        self.process.write_float(wall_climb_cdo_address + 0x198, 120.0)

        return True

    def disable_wall_climb_180_turn_jump(self) -> Optional[bool]:
        if not self.is_process_still_running():
            return None
        elif not self.move_cdo_addresses or "TdMove_WallClimb180TurnJump" not in self.move_cdo_addresses:
            return None

        wall_climb_180_turn_jump_cdo_address: int = self.move_cdo_addresses["TdMove_WallClimb180TurnJump"]

        self.process.write_float(wall_climb_180_turn_jump_cdo_address + 0x84, 1.0)
        self.process.write_float(wall_climb_180_turn_jump_cdo_address + 0x8C, 999999999.0)

        return True

    def enable_wall_climb_180_turn_jump(self) -> Optional[bool]:
        if not self.is_process_still_running():
            return None
        elif not self.move_cdo_addresses or "TdMove_WallClimb180TurnJump" not in self.move_cdo_addresses:
            return None

        wall_climb_180_turn_jump_cdo_address: int = self.move_cdo_addresses["TdMove_WallClimb180TurnJump"]

        self.process.write_float(wall_climb_180_turn_jump_cdo_address + 0x84, -10.0)
        self.process.write_float(wall_climb_180_turn_jump_cdo_address + 0x8C, 1.0)

        return True

    def disable_wall_run(self) -> Optional[bool]:
        if not self.is_process_still_running():
            return None
        elif not self.move_cdo_addresses or "TdMove_WallRun" not in self.move_cdo_addresses:
            return None

        wall_run_cdo_address: int = self.move_cdo_addresses["TdMove_WallRun"]

        self.process.write_float(wall_run_cdo_address + 0x84, 1.0)
        self.process.write_float(wall_run_cdo_address + 0x8C, 999999999.0)

        return True

    def enable_wall_run(self) -> Optional[bool]:
        if not self.is_process_still_running():
            return None
        elif not self.move_cdo_addresses or "TdMove_WallRun" not in self.move_cdo_addresses:
            return None

        wall_run_cdo_address: int = self.move_cdo_addresses["TdMove_WallRun"]

        self.process.write_float(wall_run_cdo_address + 0x84, -10.0)
        self.process.write_float(wall_run_cdo_address + 0x8C, 0.15)

        return True

    def disable_wall_run_jump(self) -> Optional[bool]:
        if not self.is_process_still_running():
            return None
        elif not self.move_cdo_addresses or "TdMove_WallrunJump" not in self.move_cdo_addresses:
            return None
        elif not self.move_cdo_addresses or "TdMove_MeleeWallrun" not in self.move_cdo_addresses:
            return None

        wall_run_jump_cdo_address: int = self.move_cdo_addresses["TdMove_WallrunJump"]

        self.process.write_float(wall_run_jump_cdo_address + 0x84, 1.0)
        self.process.write_float(wall_run_jump_cdo_address + 0x8C, 999999999.0)

        melee_wallrun_cdo_address: int = self.move_cdo_addresses["TdMove_MeleeWallrun"]

        self.process.write_float(melee_wallrun_cdo_address + 0x84, 1.0)
        self.process.write_float(melee_wallrun_cdo_address + 0x8C, 999999999.0)

        return True

    def enable_wall_run_jump(self) -> Optional[bool]:
        if not self.is_process_still_running():
            return None
        elif not self.move_cdo_addresses or "TdMove_WallrunJump" not in self.move_cdo_addresses:
            return None
        elif not self.move_cdo_addresses or "TdMove_MeleeWallrun" not in self.move_cdo_addresses:
            return None

        wall_run_jump_cdo_address: int = self.move_cdo_addresses["TdMove_WallrunJump"]

        self.process.write_float(wall_run_jump_cdo_address + 0x84, -10.0)
        self.process.write_float(wall_run_jump_cdo_address + 0x8C, 0.0)

        melee_wallrun_cdo_address: int = self.move_cdo_addresses["TdMove_MeleeWallrun"]

        self.process.write_float(melee_wallrun_cdo_address + 0x84, -10.0)
        self.process.write_float(melee_wallrun_cdo_address + 0x8C, 0.0)

        return True

    def disable_springboard(self) -> Optional[bool]:
        if not self.is_process_still_running():
            return None
        elif not self.move_cdo_addresses or "TdMove_SpringBoard" not in self.move_cdo_addresses:
            return None

        springboard_cdo_address: int = self.move_cdo_addresses["TdMove_SpringBoard"]

        self.process.write_float(springboard_cdo_address + 0x84, 1.0)
        self.process.write_float(springboard_cdo_address + 0x8C, 999999999.0)

        return True

    def enable_springboard(self) -> Optional[bool]:
        if not self.is_process_still_running():
            return None
        elif not self.move_cdo_addresses or "TdMove_SpringBoard" not in self.move_cdo_addresses:
            return None

        springboard_cdo_address: int = self.move_cdo_addresses["TdMove_SpringBoard"]

        self.process.write_float(springboard_cdo_address + 0x84, -10.0)
        self.process.write_float(springboard_cdo_address + 0x8C, 0.0)

        return True

    def disable_swing(self) -> Optional[bool]:
        if not self.is_process_still_running():
            return None
        elif not self.move_cdo_addresses or "TdMove_Swing" not in self.move_cdo_addresses:
            return None

        swing_cdo_address: int = self.move_cdo_addresses["TdMove_Swing"]

        self.process.write_float(swing_cdo_address + 0x84, 1.0)
        self.process.write_float(swing_cdo_address + 0x8C, 999999999.0)

        return True

    def enable_swing(self) -> Optional[bool]:
        if not self.is_process_still_running():
            return None
        elif not self.move_cdo_addresses or "TdMove_Swing" not in self.move_cdo_addresses:
            return None

        swing_cdo_address: int = self.move_cdo_addresses["TdMove_Swing"]

        self.process.write_float(swing_cdo_address + 0x84, -10.0)
        self.process.write_float(swing_cdo_address + 0x8C, 0.0)

        return True

    def disable_vault(self) -> Optional[bool]:
        if not self.is_process_still_running():
            return None
        elif not self.move_cdo_addresses or "TdMove_VaultOver" not in self.move_cdo_addresses:
            return None

        vault_cdo_address: int = self.move_cdo_addresses["TdMove_VaultOver"]

        self.process.write_float(vault_cdo_address + 0x84, 1.0)
        self.process.write_float(vault_cdo_address + 0x8C, 999999999.0)

        return True

    def enable_vault(self) -> Optional[bool]:
        if not self.is_process_still_running():
            return None
        elif not self.move_cdo_addresses or "TdMove_VaultOver" not in self.move_cdo_addresses:
            return None

        vault_cdo_address: int = self.move_cdo_addresses["TdMove_VaultOver"]

        self.process.write_float(vault_cdo_address + 0x84, -10.0)
        self.process.write_float(vault_cdo_address + 0x8C, 0.0)

        return True

    def disable_zipline(self) -> Optional[bool]:
        if not self.is_process_still_running():
            return None
        elif not self.move_cdo_addresses or "TdMove_IntoZipLine" not in self.move_cdo_addresses:
            return None

        zipline_cdo_address: int = self.move_cdo_addresses["TdMove_IntoZipLine"]

        self.process.write_float(zipline_cdo_address + 0x84, 1.0)
        self.process.write_float(zipline_cdo_address + 0x8C, 999999999.0)

        return True

    def enable_zipline(self) -> Optional[bool]:
        if not self.is_process_still_running():
            return None
        elif not self.move_cdo_addresses or "TdMove_IntoZipLine" not in self.move_cdo_addresses:
            return None

        zipline_cdo_address: int = self.move_cdo_addresses["TdMove_IntoZipLine"]

        self.process.write_float(zipline_cdo_address + 0x84, -10.0)
        self.process.write_float(zipline_cdo_address + 0x8C, 0.5)

        return True

    def set_running_speed_slow(self) -> Optional[bool]:
        if not self.is_process_still_running():
            return None

        pawn_address: int = self._resolve_address(self.game_engine_offset, (0x2BC, 0x0, 0x40, 0x624, 0x0)) or 0

        if pawn_address == 0:
            return None

        self.process.write_float(pawn_address + 0x700, 2.4)
        self.process.write_float(pawn_address + 0x704, 12.0)

        return True

    def set_running_speed_regular(self) -> Optional[bool]:
        if not self.is_process_still_running():
            return None

        pawn_address: int = self._resolve_address(self.game_engine_offset, (0x2BC, 0x0, 0x40, 0x624, 0x0)) or 0

        if pawn_address == 0:
            return None

        self.process.write_float(pawn_address + 0x700, 0.4)
        self.process.write_float(pawn_address + 0x704, 2.0)

        return True

    def set_running_speed_trap_slow(self) -> Optional[bool]:
        if not self.is_process_still_running():
            return None

        pawn_address: int = self._resolve_address(self.game_engine_offset, (0x2BC, 0x0, 0x40, 0x624, 0x0)) or 0

        if pawn_address == 0:
            return None

        self.process.write_float(pawn_address + 0x700, 12.0)
        self.process.write_float(pawn_address + 0x704, 60.0)

        return True

    def set_running_speed_trap_slippery(self) -> Optional[bool]:
        if not self.is_process_still_running():
            return None

        pawn_address: int = self._resolve_address(self.game_engine_offset, (0x2BC, 0x0, 0x40, 0x624, 0x0)) or 0

        if pawn_address == 0:
            return None

        self.process.write_float(pawn_address + 0x700, 0.0)
        self.process.write_float(pawn_address + 0x704, 0.0)

        return True

    def set_fov_trap_wide(self) -> Optional[bool]:
        return self.set_fov(140.0)

    def set_fov(self, value: float) -> Optional[bool]:
        if not self.is_process_still_running():
            return None

        player_controller_address: int = self._resolve_address(self.game_engine_offset, (0x2BC, 0x0, 0x40, 0x0)) or 0

        if player_controller_address == 0:
            return None

        current_value: float = self.process.read_float(player_controller_address + 0x310)

        if current_value == value:
            return True

        self.process.write_float(player_controller_address + 0x310, value)
        self.process.write_float(player_controller_address + 0x314, value)

        return True

    def set_health_trap_injury(self) -> Optional[bool]:
        if not self.is_process_still_running():
            return None

        pawn_address: int = self._resolve_address(self.game_engine_offset, (0x2BC, 0x0, 0x40, 0x624, 0x0)) or 0

        if pawn_address == 0:
            return None

        self.process.write_int(pawn_address + 0x2B8, 1)
        self.process.write_float(pawn_address + 0x878, 1.0)

        return True

    def set_health_trap_injury_restore(self) -> Optional[bool]:
        if not self.is_process_still_running():
            return None

        pawn_address: int = self._resolve_address(self.game_engine_offset, (0x2BC, 0x0, 0x40, 0x624, 0x0)) or 0

        if pawn_address == 0:
            return None

        self.process.write_float(pawn_address + 0x878, 25.0)

        return True

    def discover_sp_time_trial_game_address(self) -> None:
        if not self.is_process_still_running():
            return None

        self.sp_time_trial_game_address = 0

        instance_name: str
        instance_data: Dict[str, Any]
        for instance_name, instance_data in self._find_instances_of_class("TdSPTimeTrialGame").items():
            if instance_name.startswith("TdSPTimeTrialGame"):
                self.sp_time_trial_game_address = instance_data[0]["address"]

        return None

    def get_total_checkpoints(self) -> Optional[int]:
        if not self.is_process_still_running() or self.sp_time_trial_game_address == 0:
            return None

        return self.process.read_int(self.sp_time_trial_game_address + 0x3D0)

    def get_passed_checkpoints(self) -> Optional[int]:
        if not self.is_process_still_running() or self.sp_time_trial_game_address == 0:
            return None

        return self.process.read_int(self.sp_time_trial_game_address + 0x3D4)

    def get_start_timestamp(self) -> Optional[float]:
        if not self.is_process_still_running() or self.sp_time_trial_game_address == 0:
            return None

        return self.process.read_float(self.sp_time_trial_game_address + 0x45C)

    def get_end_timestamp(self) -> Optional[float]:
        if not self.is_process_still_running() or self.sp_time_trial_game_address == 0:
            return None

        return self.process.read_float(self.sp_time_trial_game_address + 0x460)

    def lock_all_levels(self) -> Optional[bool]:
        if not self.is_process_still_running():
            return None

        function_object_address: int = 0
        function_object_address_candidates: List[Dict[str, Any]] = self.gobjects_name_to_object.get("LockAllLevels", list())

        function_object_address_candidate: Dict[str, Any]
        for function_object_address_candidate in function_object_address_candidates:
            if self.gobjects_address_to_object[function_object_address_candidate["outer"]]["name"] == "TdProfileSettings":
                function_object_address = function_object_address_candidate["address"]
                break

        if function_object_address == 0:
            return None

        profile_settings_address: int = 0
        profile_settings_address_candidates: Dict[str, Any] = self._find_instances_of_class("TdProfileSettings") or dict()

        instance_data: Dict[str, Any]
        for instance_data in profile_settings_address_candidates.values():
            if self.gobjects_address_to_object[instance_data[0]["outer"]]["name"] == "Transient":
                profile_settings_address = instance_data[0]["address"]
                break

        if profile_settings_address == 0:
            return None

        args_bytes: bytes = struct.pack("<I", 0)

        return self._call_process_event(
            profile_settings_address,
            function_object_address,
            args_bytes,
            "bool",
        )

    def lock_all_time_trials(self) -> None:
        if not self.is_process_still_running():
            return None

        function_object_address: int = 0
        function_object_address_candidates: List[Dict[str, Any]] = self.gobjects_name_to_object.get("LockAllTTStretches", list())

        function_object_address_candidate: Dict[str, Any]
        for function_object_address_candidate in function_object_address_candidates:
            if self.gobjects_address_to_object[function_object_address_candidate["outer"]]["name"] == "TdProfileSettings":
                function_object_address = function_object_address_candidate["address"]
                break

        if function_object_address == 0:
            return None

        profile_settings_address: int = 0
        profile_settings_address_candidates: Dict[str, Any] = self._find_instances_of_class("TdProfileSettings") or dict()

        instance_data: Dict[str, Any]
        for instance_data in profile_settings_address_candidates.values():
            if self.gobjects_address_to_object[instance_data[0]["outer"]]["name"] == "Transient":
                profile_settings_address = instance_data[0]["address"]
                break

        if profile_settings_address == 0:
            return None

        return self._call_process_event(
            profile_settings_address,
            function_object_address,
            None,
            None,
        )

    def unlock_time_trial(self, time_trial_index: int) -> Optional[bool]:
        if not self.is_process_still_running():
            return None

        function_object_address: int = 0
        function_object_address_candidates: List[Dict[str, Any]] = self.gobjects_name_to_object.get("UnlockTTStretch", list())

        function_object_address_candidate: Dict[str, Any]
        for function_object_address_candidate in function_object_address_candidates:
            if self.gobjects_address_to_object[function_object_address_candidate["outer"]]["name"] == "TdProfileSettings":
                function_object_address = function_object_address_candidate["address"]
                break

        if function_object_address == 0:
            return None

        profile_settings_address: int = 0
        profile_settings_address_candidates: Dict[str, Any] = self._find_instances_of_class("TdProfileSettings") or dict()

        instance_data: Dict[str, Any]
        for instance_data in profile_settings_address_candidates.values():
            if self.gobjects_address_to_object[instance_data[0]["outer"]]["name"] == "Transient":
                profile_settings_address = instance_data[0]["address"]
                break

        if profile_settings_address == 0:
            return None

        args_bytes: bytes = struct.pack("<IIII", time_trial_index, 0, 0, 0)

        return self._call_process_event(
            profile_settings_address,
            function_object_address,
            args_bytes,
            "bool",
            return_value_offset=0x4,
        )

    def _find_instances_of_class(self, class_name: str) -> Optional[Dict[str, Any]]:
        if not self.is_process_still_running():
            return None

        if class_name not in self.gobjects_name_to_object:
            return None

        class_addresses: List[int] = [object_data["address"] for object_data in self.gobjects_name_to_object[class_name]]

        instances: Dict[str, List[Dict[str, Any]]] = dict()

        name: str
        objects: List[Dict[str, Any]]
        for name, objects in self.gobjects_name_to_object.items():
            object_data: Dict[str, Any]
            for object_data in objects:
                if object_data["class"] in class_addresses:
                    if name not in instances:
                        instances[name] = list()

                    instances[name].append(object_data)

        if not len(instances):
            return None

        return instances

    def _generate_gnames_mapping(self):
        if not self.is_process_still_running():
            return

        mapping: Dict[int, str] = dict()

        gnames_structure_address: int = self.process.base_address + self.gnames_offset

        data_pointer: int = self.process.read_int(gnames_structure_address)
        name_count: int = self.process.read_int(gnames_structure_address + 0x4)

        try:
            array_size: int = name_count * 4
            array_data: bytes = self.process.read_bytes(data_pointer, array_size)
            name_pointers: Tuple[int, ...] = struct.unpack(f"<{name_count}I", array_data)
        except:
            return

        for name_index, entry_pointer in enumerate(name_pointers):
            if not entry_pointer:
                continue

            try:
                string_address: int = entry_pointer + 0x10

                raw_name_bytes: bytes = self.process.read_bytes(string_address, 128)

                decoded_name: str = raw_name_bytes.decode("utf-16", errors="ignore")
                clean_name: str = decoded_name.split("\x00")[0]

                if clean_name:
                    mapping[name_index] = clean_name

            except:
                continue

        self.gnames_mapping = mapping

    def _refresh_gobjects_mapping(self):
        if not self.is_process_still_running():
            return

        self.gobjects_name_to_object = dict()
        self.gobjects_address_to_object = dict()

        gobjects_header_address: int = self.process.base_address + self.gobjects_offset

        data_array_pointer: int = self.process.read_int(gobjects_header_address + 0x0)
        element_count: int = self.process.read_int(gobjects_header_address + 0x4)

        if not data_array_pointer or element_count <= 0:
            return

        array_bytes: bytes = self.process.read_bytes(data_array_pointer, element_count * 4)

        for i in range(element_count):
            object_pointer = struct.unpack("<I", array_bytes[i * 4: i * 4 + 4])[0]

            if object_pointer <= 0x10000:
                continue

            try:
                header_bytes: bytes = self.process.read_bytes(object_pointer + 0x28, 16)
                outer_ptr, name_index, name_number, class_ptr = struct.unpack("<IIII", header_bytes)

                base_name: str = self.gnames_mapping.get(name_index, "Unknown")

                display_name = f"{base_name}_{name_number}" if name_number > 0 else base_name

                object_data = {
                    "address": object_pointer,
                    "outer": outer_ptr,
                    "class": class_ptr,
                    "name": display_name,
                }

                if display_name not in self.gobjects_name_to_object:
                    self.gobjects_name_to_object[display_name] = list()

                self.gobjects_name_to_object[display_name].append(object_data)
                self.gobjects_address_to_object[object_pointer] = object_data
            except:
                continue

    def _call_process_event(
        self,
        instance_address: int,
        function_object_address: int,
        args_bytes: Optional[bytes],
        result_type: Optional[str],
        return_value_offset: int = 0x0,
    ) -> Union[bool, int, float]:
        instance_flags: int = self.process.read_int(instance_address + 0x8)

        if not (instance_flags & 0x200):
            self.process.write_int(instance_address + 0x8, instance_flags | 0x200)

        args_address: Optional[int] = None

        if args_bytes is not None:
            args_address = self.process.allocate(len(args_bytes))
            self.process.write_bytes(args_address, args_bytes, len(args_bytes))

        result_buffer_address: Optional[int] = None

        if result_type in ["bool", "int", "float"] or result_type is None:
            result_buffer_address = self.process.allocate(4)

        process_event_address: int = self.process.base_address + self.process_event_proxy_offset

        shellcode = b"\x68" + struct.pack("<I", result_buffer_address or 0)  # push result_buffer_address
        shellcode += b"\x68" + struct.pack("<I", args_address or 0)  # push args_address
        shellcode += b"\x68" + struct.pack("<I", function_object_address)  # push function_object_address
        shellcode += b"\xB9" + struct.pack("<I", instance_address)  # mov ecx, instance_address
        shellcode += b"\xB8" + struct.pack("<I", process_event_address)  # mov eax, process_event_address
        shellcode += b"\xFF\xD0"  # call eax
        shellcode += b"\xC3"  # ret

        execution_address: int = self.process.allocate(len(shellcode))
        self.process.write_bytes(execution_address, shellcode, len(shellcode))

        thread_handle = self.process.start_thread(execution_address)
        ctypes.windll.kernel32.WaitForSingleObject(thread_handle, -1)

        result: Any = True

        if result_type == "bool":
            result = self.process.read_int(args_address + return_value_offset) != 0
        elif result_type == "int":
            result = self.process.read_int(args_address + return_value_offset)
        elif result_type == "float":
            result = self.process.read_float(args_address + return_value_offset)

        self.process.free(execution_address)

        if args_address is not None:
            self.process.free(args_address)

        if result_buffer_address is not None:
            self.process.free(result_buffer_address)

        ctypes.windll.kernel32.CloseHandle(thread_handle)

        return result

    def _resolve_address(self, base_offset: int, offsets: Tuple[int, ...]) -> Optional[int]:
        address: int = self.process.read_int(self.process.base_address + base_offset)

        for offset in offsets[:-1]:
            try:
                address = self.process.read_int(address + offset)
            except Exception:
                return None

        return address + offsets[-1]

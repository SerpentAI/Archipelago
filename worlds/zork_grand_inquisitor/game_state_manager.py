from typing import Dict, List, Optional, Set, Tuple

from pymem import Pymem
from pymem.process import close_handle, list_processes
from pymem.ressources.structure import ProcessEntry32

from .scummvm_zvision import ScummVMZVisionProcess


class GameStateManager:
    process_name: str = "scummvm.exe"

    process: Optional[Pymem]
    is_process_running: bool

    zvision: Optional[ScummVMZVisionProcess]

    engine_address: int

    game_location: Optional[str]
    game_location_offset: Optional[int]
    arrivals: List[Tuple[str, str, int, bool]]

    state_values: Dict[int, int]
    state_changes: List[Tuple[int, int]]
    previous_state_changes: List[Tuple[int, int]]
    pending_state_values: Dict[int, int]
    pending_state_flags: Dict[int, bool]
    pending_state_flag_overrides: Dict[int, bool]

    state_value_journal: List[Tuple[int, int, int]]
    state_value_journal_start: int
    state_value_journal_valid_from: int
    suppressed_state_changes: Dict[Tuple[int, int], int]
    suppressed_state_changes_ticks: int

    needs_resynchronization: bool

    are_game_changes_active: bool
    state_value_overrides: Dict[int, int]
    state_value_remaps: List[Tuple[int, int, int, int]]
    state_value_read_overrides: List[Tuple[int, int, int]]
    blocked_actions: List[Tuple[Optional[int], Optional[str]]]
    state_flag_overrides: Dict[int, bool]
    location_redirects: List[Tuple[str, str, str, int]]
    are_location_redirects_suspended: bool

    zvision_trap_defaults: Optional[Tuple[float, float]]

    def __init__(self) -> None:
        self.process = None
        self.is_process_running = False

        self.zvision = None

        self.engine_address = 0

        self.game_location = None
        self.game_location_offset = None
        self.arrivals = list()

        self.state_values = dict()
        self.state_changes = list()
        self.previous_state_changes = list()

        self.state_value_journal = list()
        self.state_value_journal_start = 0
        self.state_value_journal_valid_from = 0
        self.suppressed_state_changes = dict()
        self.suppressed_state_changes_ticks = 0
        self.pending_state_values = dict()
        self.pending_state_flags = dict()
        self.pending_state_flag_overrides = dict()

        self.needs_resynchronization = True

        self.are_game_changes_active = False
        self.state_value_overrides = dict()
        self.state_value_remaps = list()
        self.state_value_read_overrides = list()
        self.blocked_actions = list()
        self.state_flag_overrides = dict()
        self.location_redirects = list()
        self.are_location_redirects_suspended = False

        self.zvision_trap_defaults = None

    def open_process_handle(self) -> bool:
        try:
            candidate_process_ids: List[int] = list()

            process_entry: ProcessEntry32
            for process_entry in list_processes():
                if process_entry.szExeFile.decode("utf-8").lower() == self.process_name:
                    candidate_process_ids.append(process_entry.th32ProcessID)

            process_id: int
            for process_id in candidate_process_ids:
                try:
                    process: Pymem = Pymem(process_id)
                except Exception:
                    continue

                try:
                    self.zvision = ScummVMZVisionProcess(process, self.process_name)
                    self.zvision.call_timeout_seconds = 0.5
                    self.process = process

                    break
                except Exception:
                    close_handle(process.process_handle)

            if self.process is None:
                return False

            try:
                self.zvision.install_hooks()
            except RuntimeError:
                pass

            self.is_process_running = True
        except Exception:
            if self.process is not None:
                close_handle(self.process.process_handle)

            self.process = None
            self.zvision = None

            return False

        return True

    def close_process_handle(self) -> bool:
        self.set_game_changes_active(False)

        if close_handle(self.process.process_handle):
            self.is_process_running = False
            self.process = None

            self.zvision = None

            self.engine_address = 0
            self.state_values = dict()
            self.pending_state_values = dict()
            self.pending_state_flags = dict()
            self.pending_state_flag_overrides = dict()
            self.arrivals = list()
            self.state_changes = list()
            self.previous_state_changes = list()
            self.needs_resynchronization = True
            self.are_game_changes_active = False
            self.state_value_overrides = dict()
            self.state_value_remaps = list()
            self.state_value_read_overrides = list()
            self.blocked_actions = list()
            self.state_flag_overrides = dict()
            self.location_redirects = list()
            self.are_location_redirects_suspended = False

            return True

        return False

    def is_process_still_running(self) -> bool:
        try:
            self.process.read_int(self.process.base_address)
        except Exception:
            self.is_process_running = False
            self.process = None

            self.zvision = None

            self.engine_address = 0
            self.state_values = dict()
            self.pending_state_values = dict()
            self.pending_state_flags = dict()
            self.pending_state_flag_overrides = dict()
            self.arrivals = list()
            self.state_changes = list()
            self.previous_state_changes = list()
            self.needs_resynchronization = True
            self.are_game_changes_active = False
            self.state_value_overrides = dict()
            self.state_value_remaps = list()
            self.state_value_read_overrides = list()
            self.blocked_actions = list()
            self.state_flag_overrides = dict()
            self.location_redirects = list()
            self.are_location_redirects_suspended = False

            return False

        return True

    def begin_tick(self) -> bool:
        if not self.is_process_running:
            return False

        try:
            if not self.zvision.is_zvision_running():
                return False

            if not self.zvision.is_hooked():
                self.zvision.install_hooks()
                self.zvision.set_state_value_overrides(self.state_value_overrides if self.are_game_changes_active else dict())
                self.zvision.set_state_value_remaps(self.state_value_remaps if self.are_game_changes_active else list())
                self.zvision.set_state_value_read_overrides(self.state_value_read_overrides if self.are_game_changes_active else list())
                self.zvision.block_actions(self.blocked_actions if self.are_game_changes_active else list())
                self.zvision.set_state_flag_overrides(self.state_flag_overrides if self.are_game_changes_active else dict())
                self.zvision.set_location_redirects(self.location_redirects if self.are_game_changes_active and not self.are_location_redirects_suspended else list())

            if not self.zvision.is_game_running():
                return False

            new_arrivals, are_arrivals_complete = self.zvision.read_new_arrivals()
            engine_address: int = self.zvision.read_engine_address()

            self.arrivals.extend(new_arrivals)

            if (
                engine_address != self.engine_address
                or not are_arrivals_complete
                or any(is_loading or destination == "gary" for _, destination, _, is_loading in new_arrivals)
            ):
                self.needs_resynchronization = True

            if not self.needs_resynchronization:
                changes, are_changes_complete = self.zvision.read_new_state_changes()

                change: Tuple[int, int]
                for change in changes:
                    if self.suppressed_state_changes.get(change, 0):
                        self.suppressed_state_changes[change] -= 1
                    else:
                        self.state_changes.append(change)

                if are_changes_complete:
                    key: int
                    value: int
                    for key, value in changes:
                        previous_value: int = self.state_values.get(key, 0)

                        if previous_value != value:
                            self.state_value_journal.append((key, previous_value, value))

                        self.state_values[key] = value
                else:
                    self.needs_resynchronization = True

            if self.needs_resynchronization:
                self.zvision.read_new_state_changes()

                self.state_values = self.zvision.read_state_values(list(range(21000)))
                self.pending_state_values = dict()
                self.pending_state_flags = dict()
                self.engine_address = engine_address
                self.needs_resynchronization = False

                self.state_value_journal_start += len(self.state_value_journal)
                self.state_value_journal = list()
                self.state_value_journal_valid_from = self.state_value_journal_start

                changes, _ = self.zvision.read_new_state_changes()

                self.state_changes.extend(changes)

                for key, value in changes:
                    self.state_values[key] = value

            if self.are_location_redirects_suspended and any(not is_loading for _, _, _, is_loading in self.arrivals):
                if self.are_game_changes_active:
                    self.zvision.set_location_redirects(self.location_redirects)

                self.are_location_redirects_suspended = False

            self.game_location, self.game_location_offset = self.zvision.read_current_location()
        except Exception:
            return False

        return True

    def end_tick(self) -> bool:
        if not self.is_process_running:
            return False

        try:
            if len(self.pending_state_values):
                self.zvision.write_state_values(self.pending_state_values)
                self.pending_state_values = dict()

            if len(self.pending_state_flags):
                self.zvision.write_state_flags([(key, 0x02, is_disabled) for key, is_disabled in self.pending_state_flags.items()])
                self.pending_state_flags = dict()

            if self.pending_state_flag_overrides != self.state_flag_overrides:
                if self.are_game_changes_active:
                    self.zvision.set_state_flag_overrides(self.pending_state_flag_overrides)

                self.state_flag_overrides = self.pending_state_flag_overrides
        except Exception:
            return False

        self.pending_state_flag_overrides = dict()
        self.arrivals = list()
        self.previous_state_changes = self.state_changes
        self.state_changes = list()

        if self.suppressed_state_changes_ticks:
            self.suppressed_state_changes_ticks -= 1

            if not self.suppressed_state_changes_ticks:
                self.suppressed_state_changes = dict()

        return True

    def set_game_changes_active(self, are_game_changes_active: bool) -> bool:
        if not self.is_process_running:
            return False

        if are_game_changes_active == self.are_game_changes_active:
            return True

        try:
            self.zvision.set_state_value_overrides(self.state_value_overrides if are_game_changes_active else dict())
            self.zvision.set_state_value_remaps(self.state_value_remaps if are_game_changes_active else list())
            self.zvision.set_state_value_read_overrides(self.state_value_read_overrides if are_game_changes_active else list())
            self.zvision.block_actions(self.blocked_actions if are_game_changes_active else list())
            self.zvision.set_state_flag_overrides(self.state_flag_overrides if are_game_changes_active else dict())
            self.zvision.set_location_redirects(self.location_redirects if are_game_changes_active and not self.are_location_redirects_suspended else list())
        except Exception:
            return False

        self.are_game_changes_active = are_game_changes_active

        return True

    def read_game_state_value_for(self, key: int) -> int:
        return self.state_values.get(key, 0)

    @property
    def state_value_journal_position(self) -> int:
        return self.state_value_journal_start + len(self.state_value_journal)

    def trim_state_value_journal(self, position: int) -> None:
        if position <= self.state_value_journal_start:
            return

        del self.state_value_journal[:position - self.state_value_journal_start]
        self.state_value_journal_start = position

    def rewind_state_value_journal(self, position: int) -> Optional[Dict[int, int]]:
        if not self.state_value_journal_valid_from <= position <= self.state_value_journal_position:
            return None

        if position < self.state_value_journal_start:
            return None

        index: int = position - self.state_value_journal_start

        previous_values: Dict[int, int] = dict()
        finished_keys: Set[int] = set()

        key: int
        previous_value: int
        value: int
        for key, previous_value, value in self.state_value_journal[index:]:
            previous_values.setdefault(key, previous_value)

            if previous_value == 1 and value == 2:
                finished_keys.add(key)

        del self.state_value_journal[index:]

        return {
            key: previous_value
            for key, previous_value in previous_values.items()
            if not (previous_value == 1 and key in finished_keys)
        }

    def find_expired_timer_start(self, position: int, timer_keys: Set[int]) -> Optional[int]:
        if not self.state_value_journal_start <= position <= self.state_value_journal_position:
            return None

        index: int = position - self.state_value_journal_start

        previous_values: Dict[int, int] = dict()

        key: int
        previous_value: int
        value: int
        for key, previous_value, _ in self.state_value_journal[index:]:
            previous_values.setdefault(key, previous_value)

        expired_timers: Set[int] = {
            key
            for key, previous_value, value in self.state_value_journal[index:]
            if key in timer_keys and previous_value == 1 and value == 2 and previous_values[key] == 1
        }

        start_index: int
        for start_index in range(index - 1, -1, -1):
            key, previous_value, value = self.state_value_journal[start_index]

            if key in expired_timers and value == 1:
                expired_timers.discard(key)

                if not expired_timers:
                    return self.state_value_journal_start + start_index

        return None

    def suppress_state_changes(self, values: Dict[int, int]) -> None:
        change: Tuple[int, int]
        for change in values.items():
            self.suppressed_state_changes[change] = self.suppressed_state_changes.get(change, 0) + 1

        self.suppressed_state_changes_ticks = 3

    def write_game_state_value_for(self, key: int, value: int) -> bool:
        if self.state_values.get(key, 0) == value:
            return True

        self.state_values[key] = value
        self.pending_state_values[key] = value

        return True

    def write_game_flags_value_for(self, key: int, value: int) -> bool:
        self.pending_state_flag_overrides[key] = value == 2

        return True

    def persist_game_flags_value_for(self, key: int, value: int) -> bool:
        self.pending_state_flags[key] = value == 2

        return True

    def set_game_location(self, game_location: str, offset: int, is_redirectable: bool = False) -> bool:
        if not self.is_process_running:
            return False

        try:
            if len(self.pending_state_values):
                self.zvision.write_state_values(self.pending_state_values)
                self.pending_state_values = dict()

            if not is_redirectable and len(self.location_redirects) and not self.are_location_redirects_suspended:
                if self.are_game_changes_active:
                    self.zvision.set_location_redirects(list())

                self.are_location_redirects_suspended = True

            self.zvision.change_location(game_location, offset)
        except Exception:
            return False

        return True

    def set_state_value_overrides(self, state_value_overrides: Dict[int, int]) -> bool:
        if not self.is_process_running:
            return False

        if state_value_overrides == self.state_value_overrides:
            return True

        try:
            if self.are_game_changes_active:
                self.zvision.set_state_value_overrides(state_value_overrides)
        except Exception:
            return False

        self.state_value_overrides = dict(state_value_overrides)

        return True

    def set_state_value_remaps(self, state_value_remaps: List[Tuple[int, int, int, int]]) -> bool:
        if not self.is_process_running:
            return False

        if state_value_remaps == self.state_value_remaps:
            return True

        try:
            if self.are_game_changes_active:
                self.zvision.set_state_value_remaps(state_value_remaps)
        except Exception:
            return False

        self.state_value_remaps = list(state_value_remaps)

        return True

    def set_state_value_read_overrides(self, state_value_read_overrides: List[Tuple[int, int, int]]) -> bool:
        if not self.is_process_running:
            return False

        if state_value_read_overrides == self.state_value_read_overrides:
            return True

        try:
            if self.are_game_changes_active:
                self.zvision.set_state_value_read_overrides(state_value_read_overrides)
        except Exception:
            return False

        self.state_value_read_overrides = list(state_value_read_overrides)

        return True

    def set_blocked_actions(self, blocked_actions: List[Tuple[Optional[int], Optional[str]]]) -> bool:
        if not self.is_process_running:
            return False

        if blocked_actions == self.blocked_actions:
            return True

        try:
            if self.are_game_changes_active:
                self.zvision.block_actions(blocked_actions)
        except Exception:
            return False

        self.blocked_actions = list(blocked_actions)

        return True

    def set_location_redirects(self, location_redirects: List[Tuple[str, str, str, int]]) -> bool:
        if not self.is_process_running:
            return False

        if location_redirects == self.location_redirects:
            return True

        try:
            if self.are_game_changes_active and not self.are_location_redirects_suspended:
                self.zvision.set_location_redirects(location_redirects)
        except Exception:
            return False

        self.location_redirects = location_redirects

        return True

    def set_panorama_reversed(self, is_reversed: bool) -> bool:
        if not self.is_process_running:
            return False

        try:
            render_table: Dict[str, object] = self.zvision.read_render_table()

            if render_table["render_state"] != "panorama" or render_table["panorama_reverse"] == is_reversed:
                return True

            self.zvision.set_view_options("panorama", reverse=is_reversed)
        except Exception:
            return False

        return True

    def set_zvision(self, is_zvision: bool) -> bool:
        if not self.is_process_running:
            return False

        try:
            render_table: Dict[str, object] = self.zvision.read_render_table()

            if render_table["render_state"] != "panorama":
                return True

            is_distorted: bool = abs(render_table["panorama_vertical_fov"] - 50.0) < 0.01 and abs(render_table["panorama_linear_scale"] - 0.5) < 0.01

            if is_zvision and not is_distorted:
                self.zvision_trap_defaults = (render_table["panorama_vertical_fov"], render_table["panorama_linear_scale"])
                self.zvision.set_view_options("panorama", vertical_fov=50.0, linear_scale=0.5)
            elif not is_zvision and is_distorted and self.zvision_trap_defaults is not None:
                self.zvision.set_view_options("panorama", vertical_fov=self.zvision_trap_defaults[0], linear_scale=self.zvision_trap_defaults[1])
                self.zvision_trap_defaults = None
        except Exception:
            return False

        return True

    def drop_inventory_item(self, item: int) -> bool:
        if not self.is_process_running:
            return False

        try:
            self.zvision.inventory_drop(item)
        except Exception:
            return False

        return True

    def kill_side_effect(self, key: int) -> bool:
        if not self.is_process_running:
            return False

        try:
            self.zvision.kill_side_effect(key)
        except Exception:
            return False

        return True

    def show_message(self, message: str) -> bool:
        if not self.is_process_running:
            return False

        try:
            self.zvision.show_message(message, 4000)
        except Exception:
            return False

        return True

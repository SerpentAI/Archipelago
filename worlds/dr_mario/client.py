import asyncio
import collections
import copy
import os
import subprocess
import sys
import urllib.parse

import CommonClient
import NetUtils
import Utils
import settings

from pymem.process import list_processes

from typing import Any, Dict, List, Optional, Set

from .data_funcs import (
    item_names_to_id,
    location_names_to_id,
    id_to_items,
    id_to_locations,
    process_slot_data,
)

from .game_controller import GameController
from .game_state_manager import GameStateManager

# UT Tab Integration
tracker_loaded: bool = False

try:
    from worlds.tracker.TrackerClient import TrackerGameContext as Context
    from worlds.tracker.TrackerClient import TrackerCommandProcessor as CommandProcessor

    tracker_loaded = True
except ModuleNotFoundError:
    from CommonClient import CommonContext as Context
    from CommonClient import ClientCommandProcessor as CommandProcessor


class DrMarioCommandProcessor(CommandProcessor):
    ctx: "DrMarioContext"

    def _cmd_deathlink(self) -> None:
        """Toggle death link status."""
        if not self.ctx.game_controller.option_death_link:
            return

        self.ctx.death_link_status = not self.ctx.death_link_status


class DrMarioContext(Context):
    tags: Set[str] = {"AP"}
    game: str = "Dr. Mario"
    command_processor: CommonClient.ClientCommandProcessor = DrMarioCommandProcessor
    items_handling: int = 0b111
    want_slot_data: bool = True

    item_name_to_id: Dict[str, int] = item_names_to_id()
    location_name_to_id: Dict[str, int] = location_names_to_id()

    id_to_items: Dict[int, str] = id_to_items()
    id_to_locations: Dict[int, str] = id_to_locations()

    game_controller: GameController
    data_storage_key: Optional[str]
    death_link_status: bool = False

    controller_task: Optional[asyncio.Task]

    seen_item_indices: Set[int] = set()

    can_display_process_found_message: bool
    can_display_process_not_found_message: bool

    is_goal_sent: bool

    tracker_loaded: bool

    locations_in_logic: List[str]
    locations_out_of_logic: List[str]

    item_messages: collections.deque

    def __init__(self, server_address: Optional[str], password: Optional[str]) -> None:
        super().__init__(server_address, password)

        self.game_controller = GameController(logger=CommonClient.logger)

        self.data_storage_key = None

        self.controller_task = None

        self.seen_item_indices = set()

        self.can_display_process_found_message = True
        self.can_display_process_not_found_message = True

        self.is_goal_sent = False

        self.tracker_loaded = tracker_loaded

        self.locations_in_logic = list()
        self.locations_out_of_logic = list()

        self.item_messages = collections.deque(maxlen=5)

        if self.tracker_loaded:
            def update_locations_in_logic(locations_in_logic: List[str]):
                self.locations_in_logic = locations_in_logic

            self.update_callback = update_locations_in_logic

            def update_locations_out_of_logic(locations_out_of_logic: List[str]):
                self.locations_out_of_logic = locations_out_of_logic

            self.glitches_callback = update_locations_out_of_logic

    def make_gui(self):
        from .client_gui.client_gui import bootstrap_client_gui
        return bootstrap_client_gui(super().make_gui())

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super().server_auth(password_requested)

        await self.get_username()
        await self.send_connect()

    async def disconnect(self, allow_autoreconnect: bool = False):
        try:
            self.game_controller.close_process_handle()
        except Exception:
            pass

        self.game_controller.reset()

        self.data_storage_key = None

        self.items_received = list()
        self.locations_info = dict()

        self.seen_item_indices = set()

        self.can_display_process_found_message = True
        self.can_display_process_not_found_message = True

        self.is_goal_sent = False

        self.locations_in_logic = list()
        self.locations_out_of_logic = list()

        self.item_messages.clear()

        if self.ui:
            self.ui.update_tabs()

        await super().disconnect(allow_autoreconnect)

    def on_package(self, cmd: str, _args: Any) -> None:
        if cmd == "Connected":
            self.game = self.slot_info[self.slot].game

            slot_data: Dict[str, Any] = process_slot_data(_args["slot_data"])

            # Options
            self.game_controller.option_goal = slot_data["goal"]
            self.game_controller.option_antiviral_serum_total = slot_data["antiviral_serum_total"]
            self.game_controller.option_antiviral_serum_required = slot_data["antiviral_serum_required"]
            self.game_controller.option_final_level = slot_data["final_level"]
            self.game_controller.option_final_level_speed = slot_data["final_level_speed"]
            self.game_controller.option_progressive_level_unlocks = slot_data["progressive_level_unlocks"]
            self.game_controller.option_starting_match_length = slot_data["starting_match_length"]
            self.game_controller.option_starting_garbage_levels = slot_data["starting_garbage_levels"]
            self.game_controller.option_restrict_rotations = slot_data["restrict_rotations"]
            self.game_controller.option_lock_next_pill_preview = slot_data["lock_next_pill_preview"]
            self.game_controller.option_speed_up_behavior = slot_data["speed_up_behavior"]
            self.game_controller.option_trap_percentage = slot_data["trap_percentage"]
            self.game_controller.option_trap_weights = slot_data["trap_weights"]
            self.game_controller.option_trap_duration = slot_data["trap_duration"]
            self.game_controller.option_randomize_music = slot_data["randomize_music"]
            self.game_controller.option_lock_music_choices = slot_data["lock_music_choices"]
            self.game_controller.option_randomize_mario_color = slot_data["randomize_mario_color"]
            self.game_controller.option_randomize_virus_colors = slot_data["randomize_virus_colors"]
            self.game_controller.option_randomize_checkerboard_colors = slot_data["randomize_checkerboard_colors"]

            is_death_link: bool = slot_data["death_link"] == 1

            self.game_controller.option_death_link = is_death_link
            self.death_link_status = is_death_link

            # Generation Data
            self.game_controller.selected_levels = slot_data["selected_levels"]
            self.game_controller.selected_starting_levels = slot_data["selected_starting_levels"]
            self.game_controller.selected_final_level = slot_data["selected_final_level"]
            self.game_controller.level_to_starting_pill = slot_data["level_to_starting_pill"]
            self.game_controller.level_to_starting_rotation = slot_data["level_to_starting_rotation"]
            self.game_controller.level_to_starting_garbage_levels = slot_data["level_to_starting_garbage_levels"]
            self.game_controller.level_to_virus_count_delta = slot_data["level_to_virus_count_delta"]
            self.game_controller.selected_music_tracks = slot_data["selected_music_tracks"]
            self.game_controller.selected_mario_color = slot_data["selected_mario_color"]
            self.game_controller.selected_virus_colors = slot_data["selected_virus_colors"]
            self.game_controller.level_to_checkerboard_colors = slot_data["level_to_checkerboard_colors"]
            self.game_controller.selected_splash_checkerboard_color = slot_data["selected_splash_checkerboard_color"]

            # Locations Checked
            if "checked_locations" in _args:
                self.game_controller.completed_locations |= {
                    self.id_to_locations[location_id] for location_id in _args["checked_locations"]
                }

            # Data Storage
            self.data_storage_key = f"dr_mario_{self.team}_{self.slot}"

            # Playing Status
            Utils.async_start(
                self.send_msgs([
                    {
                        "cmd": "StatusUpdate",
                        "status": CommonClient.ClientStatus.CLIENT_PLAYING
                    }
                ])
            )

            # UI Tabs
            if self.ui:
                self.ui.update_tabs()
        elif cmd == "RoomUpdate":
            if "checked_locations" in _args:
                self.game_controller.completed_locations |= {
                    self.id_to_locations[location_id] for location_id in _args["checked_locations"]
                }

        # UT Tab Integration
        super().on_package(cmd, _args)

    def on_print_json(self, args: Dict[str, Any]) -> None:
        if args.get("type") == "ItemSend" and isinstance(args.get("item"), NetUtils.NetworkItem):
            if args["item"].player == self.slot or args.get("receiving") == self.slot:
                self.item_messages.append(copy.deepcopy(args["data"]))

        if args.get("type") == "ItemSend" and self.game_controller.is_process_running():
            network_item: NetUtils.NetworkItem = args["item"]
            receiving: int = args["receiving"]
            item_name: str = self.item_names.lookup_in_slot(network_item.item, receiving)

            if network_item.player == self.slot and receiving == self.slot:
                self.game_controller.show_toast(f"Found {item_name}", True)
            elif receiving == self.slot:
                self.game_controller.show_toast(f"Received {item_name} from {self.player_names[network_item.player]}", True)
            elif network_item.player == self.slot:
                self.game_controller.show_toast(f"Sent {item_name} to {self.player_names[receiving]}")

        super().on_print_json(args)

    def on_deathlink(self, data: Dict[str, Any]) -> None:
        self.last_death_link = max(data["time"], self.last_death_link)
        self.game_controller.pending_death_link = (True, data.get("source"), data.get("cause"))

    async def controller(self):
        while not self.exit_event.is_set():
            await asyncio.sleep(0.2)

            # Enqueue Received Item Delta
            i: int
            network_item: NetUtils.NetworkItem
            for i, network_item in enumerate(self.items_received):
                if i in self.seen_item_indices:
                    continue

                item_name: str = self.id_to_items[network_item.item]

                self.game_controller.received_items_queue.append(item_name)
                self.seen_item_indices.add(i)

            # Network Operations
            if self.server and self.slot:
                # UT Logic
                if self.tracker_loaded:
                    self.game_controller.locations_in_logic = self.locations_in_logic

                # Game Controller Update
                if not self.game_controller.is_process_running():
                    if not self.game_controller.open_process_handle():
                        if self.can_display_process_not_found_message:
                            CommonClient.logger.info("Looking for Dr. Mario process (Mesen)...")

                            self.can_display_process_found_message = True
                            self.can_display_process_not_found_message = False

                if self.game_controller.is_process_running():
                    if self.can_display_process_found_message:
                        CommonClient.logger.info("Dr. Mario process found!")

                        self.can_display_process_found_message = False
                        self.can_display_process_not_found_message = True

                    self.game_controller.update()

                # Send Checked Locations
                checked_location_ids: List[int] = list()

                while len(self.game_controller.completed_locations_queue) > 0:
                    location_name: str = self.game_controller.completed_locations_queue.popleft()
                    location_id: int = self.location_name_to_id[location_name]

                    checked_location_ids.append(location_id)

                await self.check_locations(checked_location_ids)

                # Check for Goal Completion
                if self.game_controller.goal_completed and not self.is_goal_sent:
                    await self.send_msgs([
                        {
                            "cmd": "StatusUpdate",
                            "status": CommonClient.ClientStatus.CLIENT_GOAL
                        }
                    ])

                    self.is_goal_sent = True

                # Handle Death Link
                await self.update_death_link(self.death_link_status)

                if self.game_controller.outgoing_death_link[0]:
                    if self.death_link_status:
                        death_cause: str = self.game_controller.outgoing_death_link[1].replace("PLAYER", self.player_names[self.slot])

                        await self.send_death(death_cause)

                    self.game_controller.outgoing_death_link = (False, None)


async def _run_game() -> None:
    if settings.get_settings().dr_mario_options.rom_start is not True:
        return

    if any(process_entry.szExeFile.decode("utf-8", errors="replace").lower() == GameStateManager.process_name for process_entry in list_processes()):
        return

    mesen_path: str = settings.get_settings().dr_mario_options.mesen_path
    rom_file: str = settings.get_settings().dr_mario_options.rom_file

    subprocess.Popen(
        [
            mesen_path,
            os.path.realpath(rom_file),
        ],
        cwd=Utils.local_path("."),
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def main(*args) -> None:
    Utils.init_logging("DrMarioClient", exception_logger="Client")

    parser = CommonClient.get_base_parser(description="Dr. Mario Client")

    parser.add_argument("url", nargs="?", help="Archipelago Connection URL")
    parser.add_argument('--name', default=None, help="Archipelago Slot Name")

    args = parser.parse_args(args)

    if args.url:
        url = urllib.parse.urlparse(args.url)
        args.connect = url.netloc
        if url.username:
            args.name = urllib.parse.unquote(url.username)
        if url.password:
            args.password = urllib.parse.unquote(url.password)

    async def _main(_args):
        ctx: DrMarioContext = DrMarioContext(args.connect, args.password)

        ctx.server_task = asyncio.create_task(CommonClient.server_loop(ctx), name="server loop")
        ctx.controller_task = asyncio.create_task(ctx.controller(), name="DrMarioController")

        Utils.async_start(_run_game())

        # UT Tab Integration
        if tracker_loaded:
            ctx.run_generator()

        if CommonClient.gui_enabled:
            ctx.run_gui()

        ctx.run_cli()

        await ctx.exit_event.wait()
        await ctx.shutdown()

    import colorama

    colorama.just_fix_windows_console()

    asyncio.run(_main(args))

    colorama.deinit()


if __name__ == "__main__":
    main(*sys.argv[1:])

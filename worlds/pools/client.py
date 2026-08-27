import asyncio
import sys
import urllib.parse

import CommonClient
import NetUtils
import Utils

from typing import Any, Dict, List, Optional, Set

from .data_funcs import (
    item_names_to_id,
    location_names_to_id,
    id_to_items,
    id_to_locations,
    process_slot_data,
)

from .enums import PoolsItems, PoolsLocations

from .game_controller import GameController

# UT Tab Integration
tracker_loaded: bool = False

try:
    from worlds.tracker.TrackerClient import TrackerGameContext as Context
    from worlds.tracker.TrackerClient import TrackerCommandProcessor as CommandProcessor

    tracker_loaded = True
except ModuleNotFoundError:
    from CommonClient import CommonContext as Context
    from CommonClient import ClientCommandProcessor as CommandProcessor


class PoolsCommandProcessor(CommandProcessor):
    ctx: "PoolsContext"


class PoolsContext(Context):
    tags: Set[str] = {"AP"}
    game: str = "POOLS"
    command_processor: CommonClient.ClientCommandProcessor = PoolsCommandProcessor
    items_handling: int = 0b111
    want_slot_data: bool = True

    item_name_to_id: Dict[str, int] = item_names_to_id()
    location_name_to_id: Dict[str, int] = location_names_to_id()

    id_to_items: Dict[int, PoolsItems] = id_to_items()
    id_to_locations: Dict[int, PoolsLocations] = id_to_locations()

    game_controller: GameController
    data_storage_key: Optional[str]

    controller_task: Optional[asyncio.Task]

    seen_item_indices: Set[int] = set()

    can_display_process_found_message: bool
    can_display_process_not_found_message: bool

    def __init__(self, server_address: Optional[str], password: Optional[str]) -> None:
        super().__init__(server_address, password)

        self.game_controller = GameController(logger=CommonClient.logger)

        self.data_storage_key = None

        self.controller_task = None

        self.seen_item_indices = set()

        self.can_display_process_found_message = True
        self.can_display_process_not_found_message = True

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

        self.ui.update_tabs()

        await super().disconnect(allow_autoreconnect)

    def on_package(self, cmd: str, _args: Any) -> None:
        if cmd == "Connected":
            self.game = self.slot_info[self.slot].game

            slot_data: Dict[str, Any] = process_slot_data(_args["slot_data"])

            # Options
            self.game_controller.option_goal = slot_data["goal"]
            self.game_controller.option_rubber_ducks_total = slot_data["rubber_ducks_total"]
            self.game_controller.option_rubber_ducks_required = slot_data["rubber_ducks_required"]
            self.game_controller.option_include_level_0 = slot_data["include_level_0"]
            self.game_controller.option_include_chairs = slot_data["include_chairs"]
            self.game_controller.option_trap_percentage = slot_data["trap_percentage"]
            self.game_controller.option_trap_weights = slot_data["trap_weights"]
            self.game_controller.option_trap_duration = slot_data["trap_duration"]

            # Generation Data
            self.game_controller.selected_starting_level = slot_data["selected_starting_level"]

            # Data Storage
            self.data_storage_key = f"pools_{self.team}_{self.slot}"

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
            self.ui.update_tabs()

        # UT Tab Integration
        super().on_package(cmd, _args)

    async def controller(self):
        while not self.exit_event.is_set():
            await asyncio.sleep(0.2)

            # Enqueue Received Item Delta
            i: int
            network_item: NetUtils.NetworkItem
            for i, network_item in enumerate(self.items_received):
                if i in self.seen_item_indices:
                    continue

                item: PoolsItems = self.id_to_items[network_item.item]

                self.game_controller.received_items_queue.append(item)
                self.seen_item_indices.add(i)

            # Network Operations
            if self.server and self.slot:
                # Game Controller Update
                if not self.game_controller.is_process_running():
                    if not self.game_controller.open_process_handle():
                        if self.can_display_process_not_found_message:
                            CommonClient.logger.info("Looking for POOLS process...")

                            self.can_display_process_found_message = True
                            self.can_display_process_not_found_message = False

                if self.game_controller.is_process_running():
                    if self.can_display_process_found_message:
                        CommonClient.logger.info("POOLS process found!")

                        self.can_display_process_found_message = False
                        self.can_display_process_not_found_message = True

                    self.game_controller.update()

                # Send Checked Locations
                checked_location_ids: List[int] = list()

                while len(self.game_controller.completed_locations_queue) > 0:
                    location: PoolsLocations = self.game_controller.completed_locations_queue.popleft()
                    location_id: int = self.location_name_to_id[location.value]

                    checked_location_ids.append(location_id)

                await self.check_locations(checked_location_ids)

                # Check for Goal Completion
                if self.game_controller.goal_completed:
                    await self.send_msgs([
                        {
                            "cmd": "StatusUpdate",
                            "status": CommonClient.ClientStatus.CLIENT_GOAL
                        }
                    ])


def main(*args) -> None:
    Utils.init_logging("PoolsClient", exception_logger="Client")

    parser = CommonClient.get_base_parser(description="POOLS Client")

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
        ctx: PoolsContext = PoolsContext(args.connect, args.password)

        ctx.server_task = asyncio.create_task(CommonClient.server_loop(ctx), name="server loop")
        ctx.controller_task = asyncio.create_task(ctx.controller(), name="PoolsController")

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

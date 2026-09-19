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


class TwentyMinutesCommandProcessor(CommandProcessor):
    ctx: "TwentyMinutesContext"

    def _cmd_deathlink(self) -> None:
        """Toggle deathlink status."""
        if not self.ctx.game_controller.option_death_link:
            return

        self.ctx.death_link_status = not self.ctx.death_link_status


class TwentyMinutesContext(Context):
    tags: Set[str] = {"AP"}
    game: str = "20 Minutes Till Dawn"
    command_processor: CommonClient.ClientCommandProcessor = TwentyMinutesCommandProcessor
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

    tracker_loaded: bool

    locations_in_logic: List[str]
    locations_out_of_logic: List[str]

    def __init__(self, server_address: Optional[str], password: Optional[str]) -> None:
        super().__init__(server_address, password)

        self.game_controller = GameController(logger=CommonClient.logger)

        self.data_storage_key = None

        self.controller_task = None

        self.seen_item_indices = set()

        self.can_display_process_found_message = True
        self.can_display_process_not_found_message = True

        self.tracker_loaded = tracker_loaded

        self.locations_in_logic = list()
        self.locations_out_of_logic = list()

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

        self.ui.update_tabs()

        await super().disconnect(allow_autoreconnect)

    def on_package(self, cmd: str, _args: Any) -> None:
        if cmd == "Connected":
            self.game = self.slot_info[self.slot].game

            slot_data: Dict[str, Any] = process_slot_data(_args["slot_data"])

            # Options
            self.game_controller.option_goal = slot_data["goal"]
            self.game_controller.option_forbidden_tomes_total = slot_data["forbidden_tomes_total"]
            self.game_controller.option_forbidden_tomes_required = slot_data["forbidden_tomes_required"]
            self.game_controller.option_character_selection = slot_data["character_selection"]
            self.game_controller.option_character_count = slot_data["character_count"]
            self.game_controller.option_weapon_selection = slot_data["weapon_selection"]
            self.game_controller.option_weapon_count = slot_data["weapon_count"]
            self.game_controller.option_starting_map = slot_data["starting_map"]
            self.game_controller.option_starting_darkness = slot_data["starting_darkness"]
            self.game_controller.option_maximum_survivable_darkness = slot_data["maximum_survivable_darkness"]
            self.game_controller.option_randomize_weapon_attributes = slot_data["randomize_weapon_attributes"]
            self.game_controller.option_weapon_attribute_randomization_chance = slot_data["weapon_attribute_randomization_chance"]
            self.game_controller.option_trap_percentage = slot_data["trap_percentage"]
            self.game_controller.option_trap_weights = slot_data["trap_weights"]

            is_death_link: bool = slot_data["death_link"] == 1

            self.game_controller.option_death_link = is_death_link
            self.death_link_status = is_death_link

            # Generation Data
            self.game_controller.selected_characters = slot_data["selected_characters"]
            self.game_controller.selected_starting_character = slot_data["selected_starting_character"]
            self.game_controller.selected_weapons = slot_data["selected_weapons"]
            self.game_controller.selected_starting_weapon = slot_data["selected_starting_weapon"]
            self.game_controller.selected_starting_map = slot_data["selected_starting_map"]
            self.game_controller.selected_full_run_map = slot_data["selected_full_run_map"]
            self.game_controller.weapon_data = slot_data["weapon_data"]

            # Data Storage
            self.data_storage_key = f"twenty_minutes_till_dawn_{self.team}_{self.slot}"

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
                # Game Controller Update
                if not self.game_controller.is_process_running():
                    if not self.game_controller.open_process_handle():
                        if self.can_display_process_not_found_message:
                            CommonClient.logger.info("Looking for 20 Minutes Till Dawn process...")

                            self.can_display_process_found_message = True
                            self.can_display_process_not_found_message = False

                if self.game_controller.is_process_running():
                    if self.can_display_process_found_message:
                        CommonClient.logger.info("20 Minutes Till Dawn process found!")

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
                if self.game_controller.goal_completed:
                    await self.send_msgs([
                        {
                            "cmd": "StatusUpdate",
                            "status": CommonClient.ClientStatus.CLIENT_GOAL
                        }
                    ])

                # Handle Death Link
                await self.update_death_link(self.death_link_status)

                if self.game_controller.outgoing_death_link[0]:
                    if self.death_link_status:
                        death_cause: Optional[str] = self.game_controller.outgoing_death_link[1]

                        await self.send_death(death_cause or "")

                    self.game_controller.outgoing_death_link = (False, None)


def main(*args) -> None:
    Utils.init_logging("TwentyMinutesClient", exception_logger="Client")

    parser = CommonClient.get_base_parser(description="20 Minutes Till Dawn Client")

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
        ctx: TwentyMinutesContext = TwentyMinutesContext(args.connect, args.password)

        ctx.server_task = asyncio.create_task(CommonClient.server_loop(ctx), name="server loop")
        ctx.controller_task = asyncio.create_task(ctx.controller(), name="TwentyMinutesController")

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

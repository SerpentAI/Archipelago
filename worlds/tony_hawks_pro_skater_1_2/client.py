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

from .enums import TonyHawksProSkater12APGoals

from .game_controller import GameController


class TonyHawksProSkater12CommandProcessor(CommonClient.ClientCommandProcessor):
    ctx: "TonyHawksProSkater12Context"

    # Temporary until the custom client tab is implemented...
    def _cmd_goal(self) -> None:
        """Outputs the goal of the current seed."""
        if not self.ctx.server or not self.ctx.slot:
            self.output("You must be connected to an Archipelago server before using /goal.")
            return

        if self.ctx.game_controller.option_goal == TonyHawksProSkater12APGoals.SECRET_TAPES_FINAL_LEVEL:
            self.output(
                f"Collect {self.ctx.game_controller.option_secret_tapes_required} Secret Tapes, then score at least 1 million points on {self.ctx.game_controller.selected_goal_level.value}"
            )
        elif self.ctx.game_controller.option_goal == TonyHawksProSkater12APGoals.SECRET_TAPE_HUNT:
            self.output(
                f"Collect {self.ctx.game_controller.option_secret_tapes_required} Secret Tapes"
            )


class TonyHawksProSkater12Context(CommonClient.CommonContext):
    tags: Set[str] = {"AP"}
    game: str = "Tony Hawk's Pro Skater 1 + 2"
    command_processor: CommonClient.ClientCommandProcessor = TonyHawksProSkater12CommandProcessor
    items_handling: int = 0b111
    want_slot_data: bool = True

    item_name_to_id: Dict[str, int] = item_names_to_id()
    location_name_to_id: Dict[str, int] = location_names_to_id()

    id_to_items: Dict[int, str] = id_to_items()
    id_to_locations: Dict[int, str] = id_to_locations()

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
        from .client_gui.client_gui import TonyHawksProSkater12Manager
        return TonyHawksProSkater12Manager

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
            self.game_controller.option_secret_tapes_total = slot_data["secret_tapes_total"]
            self.game_controller.option_secret_tapes_required = slot_data["secret_tapes_required"]
            self.game_controller.option_skater_selection = slot_data["skater_selection"]
            self.game_controller.option_skater_count = slot_data["skater_count"]
            self.game_controller.option_level_selection = slot_data["level_selection"]
            self.game_controller.option_level_count = slot_data["level_count"]
            self.game_controller.option_include_platinum_scores = slot_data["include_platinum_scores"]
            self.game_controller.option_include_platinum_combo_scores = slot_data["include_platinum_combo_scores"]
            self.game_controller.option_include_signature_specials = slot_data["include_signature_specials"]
            self.game_controller.option_include_long_tricks = slot_data["include_long_tricks"]
            self.game_controller.option_include_gaps = slot_data["include_gaps"]
            self.game_controller.option_gap_count_per_level = slot_data["gap_count_per_level"]
            self.game_controller.option_score_requirement_mode = slot_data["score_requirement_mode"]
            self.game_controller.option_score_requirement_percentage = slot_data["score_requirement_percentage"]
            self.game_controller.option_combo_score_requirement_mode = slot_data["combo_score_requirement_mode"]
            self.game_controller.option_combo_score_requirement_percentage = slot_data["combo_score_requirement_percentage"]
            self.game_controller.option_starting_trick_type_weights = slot_data["starting_trick_type_weights"]
            self.game_controller.option_include_overpowered_abilities = slot_data["include_overpowered_abilities"]
            self.game_controller.option_trap_percentage = slot_data["trap_percentage"]
            self.game_controller.option_trap_weights = slot_data["trap_weights"]

            # Generation Data
            self.game_controller.selected_skaters = slot_data["selected_skaters"]
            self.game_controller.selected_starting_skater = slot_data["selected_starting_skater"]

            self.game_controller.selected_levels = slot_data["selected_levels"]
            self.game_controller.selected_starting_levels = slot_data["selected_starting_levels"]
            self.game_controller.selected_goal_level = slot_data["selected_goal_level"]

            self.game_controller.target_scores = slot_data["target_scores"]
            self.game_controller.target_combo_scores = slot_data["target_combo_scores"]

            self.game_controller.target_gaps = slot_data["target_gaps"]

            self.game_controller.target_long_tricks = slot_data["target_long_tricks"]

            self.game_controller.starting_trick_types = slot_data["starting_trick_types"]

            self.game_controller.target_score_ratios = slot_data["target_score_ratios"]
            self.game_controller.target_combo_score_ratios = slot_data["target_combo_score_ratios"]

            # Assemble Locations
            self.game_controller.assemble_target_score_locations()
            self.game_controller.assemble_target_combo_score_locations()

            if slot_data["include_long_tricks"]:
                self.game_controller.assemble_long_trick_locations()

            if slot_data["include_gaps"]:
                self.game_controller.assemble_gap_locations()

            # Data Storage
            self.data_storage_key = f"tony_hawks_pro_skater_1_2_{self.team}_{self.slot}"

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

    async def controller(self):
        while not self.exit_event.is_set():
            await asyncio.sleep(0.2)

            # Enqueue Received Item Delta
            i: int
            network_item: NetUtils.NetworkItem
            for i, network_item in enumerate(self.items_received):
                if i in self.seen_item_indices:
                    continue

                item: str = self.id_to_items[network_item.item]

                self.game_controller.received_items_queue.append(item)
                self.seen_item_indices.add(i)

            # Network Operations
            if self.server and self.slot:
                # Game Controller Update
                if not self.game_controller.is_process_running():
                    if not self.game_controller.open_process_handle():
                        if self.can_display_process_not_found_message:
                            CommonClient.logger.info("Looking for Tony Hawk's Pro Skater 1 + 2 process...")

                            self.can_display_process_found_message = True
                            self.can_display_process_not_found_message = False

                if self.game_controller.is_process_running():
                    if self.can_display_process_found_message:
                        CommonClient.logger.info("Tony Hawk's Pro Skater 1 + 2 process found!")

                        self.can_display_process_found_message = False
                        self.can_display_process_not_found_message = True

                    self.game_controller.update()

                # Send Checked Locations
                checked_location_ids: List[int] = list()

                while len(self.game_controller.completed_locations_queue) > 0:
                    location: str = self.game_controller.completed_locations_queue.popleft()
                    location_id: int = self.location_name_to_id[location]

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
    Utils.init_logging("TonyHawksProSkater12Client", exception_logger="Client")

    parser = CommonClient.get_base_parser(description="Tony Hawk's Pro Skater 1 + 2 Client")

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
        ctx: TonyHawksProSkater12Context = TonyHawksProSkater12Context(args.connect, args.password)

        ctx.server_task = asyncio.create_task(CommonClient.server_loop(ctx), name="server loop")
        ctx.controller_task = asyncio.create_task(ctx.controller(), name="TonyHawksProSkater12Controller")

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

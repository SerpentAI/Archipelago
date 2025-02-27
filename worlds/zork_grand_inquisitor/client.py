import asyncio

import CommonClient
import NetUtils
import Utils

from typing import Any, Dict, List, Optional, Set, Tuple

from .data_funcs import (
    item_names_to_id,
    item_names_to_item,
    location_names_to_id,
    id_to_client_seed_information,
    id_to_craftable_spell_behaviors,
    id_to_deathsanity,
    id_to_entrance_randomizer,
    id_to_hotspots,
    id_to_items,
    id_to_landmarksanity,
    id_to_locations,
    id_to_goals,
    id_to_starting_locations,
)

from .enums import ZorkGrandInquisitorItems, ZorkGrandInquisitorLocations
from .game_controller import GameController


class ZorkGrandInquisitorCommandProcessor(CommonClient.ClientCommandProcessor):
    def _cmd_zork(self) -> None:
        """Attach to an open Zork Grand Inquisitor process."""
        if not self.ctx.server or not self.ctx.slot:
            self.output("You must be connected to an Archipelago server before using /zork.")
            return

        result: bool = self.ctx.game_controller.open_process_handle()

        if result:
            self.ctx.process_attached_at_least_once = True
            self.output("Successfully attached to Zork Grand Inquisitor process.")

            self.ctx.game_controller.output_seed_information()
            self.ctx.game_controller.output_starter_kit()
        else:
            self.output("Failed to attach to Zork Grand Inquisitor process.")

    def _cmd_brog(self) -> None:
        """List received Brog items."""
        self.ctx.game_controller.list_received_brog_items()

    def _cmd_griff(self) -> None:
        """List received Griff items."""
        self.ctx.game_controller.list_received_griff_items()

    def _cmd_lucy(self) -> None:
        """List received Lucy items."""
        self.ctx.game_controller.list_received_lucy_items()

    def _cmd_hotspots(self) -> None:
        """List received Hotspots."""
        self.ctx.game_controller.list_received_hotspots()

    def _cmd_deathlink(self) -> None:
        """Toggle deathlink status."""
        if not self.ctx.game_controller.option_death_link:
            return

        self.ctx.death_link_status = not self.ctx.death_link_status


class ZorkGrandInquisitorContext(CommonClient.CommonContext):
    tags: Set[str] = {"AP"}
    game: str = "Zork Grand Inquisitor"
    command_processor: CommonClient.ClientCommandProcessor = ZorkGrandInquisitorCommandProcessor
    items_handling: int = 0b111
    want_slot_data: bool = True

    item_name_to_id: Dict[str, int] = item_names_to_id()
    location_name_to_id: Dict[str, int] = location_names_to_id()

    id_to_items: Dict[int, ZorkGrandInquisitorItems] = id_to_items()
    id_to_locations: Dict[int, ZorkGrandInquisitorLocations] = id_to_locations()

    game_controller: GameController
    death_link_status: bool = False

    controller_task: Optional[asyncio.Task]

    process_attached_at_least_once: bool
    can_display_process_message: bool

    def __init__(self, server_address: Optional[str], password: Optional[str]) -> None:
        super().__init__(server_address, password)

        self.game_controller = GameController(logger=CommonClient.logger)

        self.controller_task = None

        self.process_attached_at_least_once = False
        self.can_display_process_message = True

    def run_gui(self) -> None:
        from kvui import GameManager

        class TextManager(GameManager):
            logging_pairs: List[Tuple[str, str]] = [("Client", "Archipelago")]
            base_title: str = "Archipelago Zork Grand Inquisitor Client"

        self.ui = TextManager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")

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

        self.items_received = []
        self.locations_info = {}

        await super().disconnect(allow_autoreconnect)

    def on_package(self, cmd: str, _args: Any) -> None:
        if cmd == "Connected":
            self.game = self.slot_info[self.slot].game

            # Options
            self.game_controller.option_goal = id_to_goals()[_args["slot_data"]["goal"]]

            self.game_controller.option_artifacts_of_magic_required = (
                _args["slot_data"]["artifacts_of_magic_required"]
            )

            self.game_controller.option_artifacts_of_magic_total = (
                _args["slot_data"]["artifacts_of_magic_total"]
            )

            self.game_controller.option_landmarks_required = (
                _args["slot_data"]["landmarks_required"]
            )

            self.game_controller.option_deaths_required = (
                _args["slot_data"]["deaths_required"]
            )

            self.game_controller.option_starting_location = (
                id_to_starting_locations()[_args["slot_data"]["starting_location"]]
            )

            self.game_controller.option_hotspots = (
                id_to_hotspots()[_args["slot_data"]["hotspots"]]
            )

            self.game_controller.option_craftable_spells = (
                id_to_craftable_spell_behaviors()[_args["slot_data"]["craftable_spells"]]
            )

            self.game_controller.option_wild_voxam = _args["slot_data"]["wild_voxam"] == 1
            self.game_controller.option_wild_voxam_chance = _args["slot_data"]["wild_voxam_chance"]

            self.game_controller.option_deathsanity = (
                id_to_deathsanity()[_args["slot_data"]["deathsanity"]]
            )

            self.game_controller.option_landmarksanity = (
                id_to_landmarksanity()[_args["slot_data"]["landmarksanity"]]
            )

            self.game_controller.option_entrance_randomizer = (
                id_to_entrance_randomizer()[_args["slot_data"]["entrance_randomizer"]]
            )

            self.game_controller.option_entrance_randomizer_include_subway_destinations = (
                _args["slot_data"]["entrance_randomizer_include_subway_destinations"] == 1
            )

            self.game_controller.option_trap_percentage = _args["slot_data"]["trap_percentage"]

            self.game_controller.option_grant_missable_location_checks = (
                _args["slot_data"]["grant_missable_location_checks"] == 1
            )

            self.game_controller.option_client_seed_information = (
                id_to_client_seed_information()[_args["slot_data"]["client_seed_information"]]
            )

            is_death_link = _args["slot_data"]["death_link"] == 1

            self.game_controller.option_death_link = is_death_link  # Represents the option; will never change
            self.death_link_status = is_death_link  # Represents the toggleable status

            # Starter Kit
            self.game_controller.starter_kit = _args["slot_data"]["starter_kit"]

            # Initial Totemizer Destination
            self.game_controller.initial_totemizer_destination = item_names_to_item()[
                _args["slot_data"]["initial_totemizer_destination"]
            ]

            # Entrance Randomizer Data
            self.game_controller.entrance_randomizer_data = _args["slot_data"]["entrance_randomizer_data"]

            # Save IDs
            self.game_controller.save_ids = tuple(_args["slot_data"]["save_ids"])

    def on_deathlink(self, data: Dict[str, Any]) -> None:
        self.last_death_link = max(data["time"], self.last_death_link)
        self.game_controller.pending_death_link = (True, data.get("source"), data.get("cause"))

    async def controller(self):
        while not self.exit_event.is_set():
            await asyncio.sleep(0.1)

            # Enqueue Received Item Delta
            goal_item_count: int = 0

            received_traps: List[ZorkGrandInquisitorItems] = list()

            network_item: NetUtils.NetworkItem
            for network_item in self.items_received:
                item: ZorkGrandInquisitorItems = self.id_to_items[network_item.item]

                if item in self.game_controller.all_goal_items:
                    goal_item_count += 1
                    continue
                elif item in self.game_controller.all_trap_items:
                    received_traps.append(item)
                    continue
                elif item not in self.game_controller.received_items:
                    if item not in self.game_controller.received_items_queue:
                        self.game_controller.received_items_queue.append(item)

            if goal_item_count > self.game_controller.goal_item_count:
                self.game_controller.goal_item_count = goal_item_count
                self.game_controller.output_goal_item_update()

            self.game_controller.received_traps = received_traps

            # Game Controller Update
            if self.game_controller.is_process_running():
                self.game_controller.update()
                self.can_display_process_message = True
            else:
                process_message: str

                if self.process_attached_at_least_once:
                    process_message = (
                        "Connection to the Zork Grand Inquisitor process was lost. Ensure you are connected "
                        "to an Archipelago server and the game is running, then use the /zork command to reconnect."
                    )
                else:
                    process_message = (
                        "To start playing, connect to an Archipelago server and use the /zork command to "
                        "link to an active Zork Grand Inquisitor process."
                    )

                if self.can_display_process_message:
                    CommonClient.logger.info(process_message)
                    self.can_display_process_message = False

            # Network Operations
            if self.server and self.slot:
                # Send Checked Locations
                checked_location_ids: List[int] = list()

                while len(self.game_controller.completed_locations_queue) > 0:
                    location: ZorkGrandInquisitorLocations = self.game_controller.completed_locations_queue.popleft()
                    location_id: int = self.location_name_to_id[location.value]

                    checked_location_ids.append(location_id)

                await self.send_msgs([
                    {
                        "cmd": "LocationChecks",
                        "locations": checked_location_ids
                    }
                ])

                # Check for Goal Completion
                if self.game_controller.goal_completed:
                    await self.send_msgs([
                        {
                            "cmd": "StatusUpdate",
                            "status": CommonClient.ClientStatus.CLIENT_GOAL
                        }
                    ])

                # Handle Energy Link
                while len(self.game_controller.energy_link_queue) > 0:
                    energy_to_add: int = self.game_controller.energy_link_queue.popleft()

                    await self.send_msgs([
                        {
                            "cmd": "Set",
                            "key": f"EnergyLink{self.team}",
                            "slot": self.slot,
                            "operations":
                                [
                                    {"operation": "add", "value": energy_to_add},
                                ],
                        },
                    ])

                    CommonClient.logger.info(f"Added {energy_to_add} J to the Energy Link pool")

                # Handle Death Link
                await self.update_death_link(self.death_link_status)

                if self.game_controller.outgoing_death_link[0]:
                    if self.death_link_status:
                        death_cause: Optional[str] = self.game_controller.outgoing_death_link[1]

                        if death_cause:
                            death_cause = death_cause.replace(
                                "PLAYER",
                                self.player_names[self.slot]
                            )
                        else:
                            death_cause = ""

                        await self.send_death(death_cause)

                    self.game_controller.outgoing_death_link = (False, None)


def main() -> None:
    Utils.init_logging("ZorkGrandInquisitorClient", exception_logger="Client")

    async def _main():
        ctx: ZorkGrandInquisitorContext = ZorkGrandInquisitorContext(None, None)

        ctx.server_task = asyncio.create_task(CommonClient.server_loop(ctx), name="server loop")
        ctx.controller_task = asyncio.create_task(ctx.controller(), name="ZorkGrandInquisitorController")

        if CommonClient.gui_enabled:
            ctx.run_gui()

        ctx.run_cli()

        await ctx.exit_event.wait()
        await ctx.shutdown()

    import colorama

    colorama.init()

    asyncio.run(_main())

    colorama.deinit()


if __name__ == "__main__":
    main()

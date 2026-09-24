from typing import Any, Dict, List, Optional, Tuple

import logging

from rule_builder.rules import And, CanReachLocation, Has, Rule

from BaseClasses import Item, Location, Region, Tutorial

from worlds.AutoWorld import WebWorld, World

from .data.game_data import (
    character_option_to_starting_region,
    locations_removed_under_the_heist_goal,
)

from .data.item_data import DayOfTheTentacleItemData, item_data
from .data.location_data import DayOfTheTentacleLocationData, location_data
from .data.rule_data import entrance_rule_data, location_rule_data

from .data_funcs import (
    id_to_goals,
    id_to_starting_characters,
    item_groups,
    item_names_to_id,
    items_with_tag,
    location_groups,
    location_names_to_id,
    locations_with_tag,
    process_slot_data,
)

from .enums import (
    DayOfTheTentacleCharacterOptions,
    DayOfTheTentacleGoalOptions,
    DayOfTheTentacleItems,
    DayOfTheTentacleLocations,
    DayOfTheTentacleRegions,
    DayOfTheTentacleTags,
)

from .options import DayOfTheTentacleOptions, option_groups


class DayOfTheTentacleItem(Item):
    game = "Day of the Tentacle"


class DayOfTheTentacleLocation(Location):
    game = "Day of the Tentacle"


class DayOfTheTentacleWebWorld(WebWorld):
    theme: str = "partyTime"

    tutorials: List[Tutorial] = [
        Tutorial(
            "Multiworld Setup Guide",
            "A guide to setting up the Day of the Tentacle randomizer connected to an Archipelago Multiworld",
            "English",
            "setup_en.md",
            "setup/en",
            ["Serpent.AI"],
        )
    ]

    option_groups = option_groups


class DayOfTheTentacleWorld(World):
    """
    Day of the Tentacle is a 1993 point-and-click adventure comedy from LucasArts. After Purple Tentacle drinks toxic
    sludge and sets out to conquer the world, three friends, Bernard, Hoagie and Laverne, use time-traveling
    Chron-O-Johns to trade items and solve puzzles across the Past, Present and Future of the Edison family's mansion,
    in a race to stop him.
    """

    options_dataclass = DayOfTheTentacleOptions
    options: DayOfTheTentacleOptions

    game = "Day of the Tentacle"

    item_name_to_id = item_names_to_id()
    location_name_to_id = location_names_to_id()

    item_name_groups = item_groups()
    location_name_groups = location_groups()

    required_client_version: Tuple[int, int, int] = (0, 6, 7)

    web = DayOfTheTentacleWebWorld()

    filler_item_names: List[str] = item_groups()["Filler Item"]

    # Options
    goal: DayOfTheTentacleGoalOptions
    swiss_deposits_total: int
    swiss_deposits_required: int
    starting_character: DayOfTheTentacleCharacterOptions
    include_room_visits: bool
    include_voice_lines: bool

    # Universal Tracker
    location_id_to_alias: Dict[int, str]
    ut_can_gen_without_yaml: bool = True
    explicit_indirect_conditions = False

    @property
    def is_universal_tracker(self) -> bool:
        return hasattr(self.multiworld, "re_gen_passthrough")

    def generate_early(self) -> None:
        self.goal = id_to_goals()[self.options.goal.value]

        self.swiss_deposits_total = self.options.swiss_deposits_total.value
        self.swiss_deposits_required = self.options.swiss_deposits_required.value

        if self.swiss_deposits_required > self.swiss_deposits_total:
            self.swiss_deposits_required = self.swiss_deposits_total

            logging.warning(
                f"Day of the Tentacle: {self.player_name} has more required Swiss Deposits than total Swiss Deposits. "
                "Adjusting required Swiss Deposits to match total Swiss Deposits..."
            )

        self.starting_character = id_to_starting_characters()[self.options.starting_character.value]

        self.include_room_visits = bool(self.options.include_room_visits.value)
        self.include_voice_lines = bool(self.options.include_voice_lines.value)

        # Universal Tracker Support
        if self.is_universal_tracker:
            self.location_id_to_alias = dict()
            self._apply_universal_tracker_passthrough()

    def create_regions(self) -> None:
        region_mapping: Dict[DayOfTheTentacleRegions, Region] = dict()

        region_enum_item: DayOfTheTentacleRegions
        for region_enum_item in entrance_rule_data.keys():
            region: Region = Region(region_enum_item.value, self.player, self.multiworld)

            region_mapping[region_enum_item] = region
            self.multiworld.regions.append(region)

        # Menu
        region_menu: Region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(region_menu)

        region_menu.connect(region_mapping[character_option_to_starting_region[self.starting_character]])

        # Locations
        locations_to_create: List[DayOfTheTentacleLocations] = locations_with_tag(DayOfTheTentacleTags.CORE_LOCATION)

        if self.include_room_visits:
            locations_to_create.extend(locations_with_tag(DayOfTheTentacleTags.VISITED_LOCATION))

        if self.include_voice_lines:
            locations_to_create.extend(locations_with_tag(DayOfTheTentacleTags.VOICE_LINE_LOCATION))

        if self.goal == DayOfTheTentacleGoalOptions.SWISS_BANK_HEIST:
            locations_to_create = [
                location for location in locations_to_create if location not in locations_removed_under_the_heist_goal
            ]

        region_locations_mapping: Dict[DayOfTheTentacleRegions, List[DayOfTheTentacleLocations]] = dict()

        location: DayOfTheTentacleLocations
        data: DayOfTheTentacleLocationData
        for location in locations_to_create:
            data = location_data[location]

            if data.region not in region_locations_mapping:
                region_locations_mapping[data.region] = list()

            region_locations_mapping[data.region].append(location)

        region: Region
        for region_enum_item, region in region_mapping.items():
            regions_locations: List[DayOfTheTentacleLocations] = region_locations_mapping.get(region_enum_item, list())

            location_enum_item: DayOfTheTentacleLocations
            for location_enum_item in regions_locations:
                data = location_data[location_enum_item]

                location_object: DayOfTheTentacleLocation = DayOfTheTentacleLocation(
                    self.player,
                    location_enum_item.value,
                    data.archipelago_id,
                    region_mapping[data.region],
                )

                # Access Rules
                location_rule: Optional[Rule] = location_rule_data[location_enum_item]

                if self.goal == DayOfTheTentacleGoalOptions.STOP_PURPLE_TENTACLE:
                    if location_enum_item == DayOfTheTentacleLocations.PRESENT_DWAYNES_ROOM_USE_PHONE:
                        deposits_rule: Rule = Has(DayOfTheTentacleItems.SWISS_DEPOSIT.value, self.swiss_deposits_required)

                        location_rule = deposits_rule if location_rule is None else And(location_rule, deposits_rule)

                if location_rule is not None:
                    self.set_rule(location_object, location_rule)

                region.locations.append(location_object)

            # Connections
            region_exit: DayOfTheTentacleRegions
            for region_exit in entrance_rule_data[region_enum_item].keys():
                entrance_rule: Optional[Rule] = entrance_rule_data[region_enum_item][region_exit]

                if entrance_rule is None:
                    region.connect(region_mapping[region_exit])
                else:
                    region.connect(region_mapping[region_exit], rule=entrance_rule)

        # Endgame
        endgame_region: Region = Region("Endgame", self.player, self.multiworld)
        self.multiworld.regions.append(endgame_region)

        if self.goal == DayOfTheTentacleGoalOptions.STOP_PURPLE_TENTACLE:
            region_mapping[DayOfTheTentacleRegions.PRESENT_BASEMENT_LAB].connect(
                endgame_region,
                rule=And(
                    CanReachLocation(
                        DayOfTheTentacleLocations.PAST_OUTHOUSES_USE_BATTERY_WITH_PLUG.value,
                        parent_region_name=DayOfTheTentacleRegions.PAST_OUTHOUSES.value,
                    ),
                    CanReachLocation(
                        DayOfTheTentacleLocations.FUTURE_KUMQUAT_TREE_USE_EXTENSION_CORD_WITH_CHRON_O_JOHN.value,
                        parent_region_name=DayOfTheTentacleRegions.FUTURE_KUMQUAT_TREE.value,
                    ),
                    CanReachLocation(
                        DayOfTheTentacleLocations.FUTURE_BASEMENT_LAB_USE_HAMSTER_WITH_GENERATOR.value,
                        parent_region_name=DayOfTheTentacleRegions.FUTURE_BASEMENT_LAB.value,
                    ),
                    CanReachLocation(
                        DayOfTheTentacleLocations.PRESENT_DWAYNES_ROOM_USE_PHONE.value,
                        parent_region_name=DayOfTheTentacleRegions.PRESENT_DWAYNES_ROOM.value,
                    ),
                ),
            )
        elif self.goal == DayOfTheTentacleGoalOptions.SWISS_BANK_HEIST:
            region_mapping[DayOfTheTentacleRegions.PRESENT_FRONT_YARD].connect(
                endgame_region,
                rule=And(
                    Has(DayOfTheTentacleItems.SWISS_DEPOSIT.value, self.swiss_deposits_required),
                    Has(DayOfTheTentacleItems.SWISS_BANKBOOK.value),
                    Has(DayOfTheTentacleItems.CHARACTER_BERNARD.value),
                ),
            )

    def create_items(self) -> None:
        ## Precollect
        items_to_precollect: List[str] = list()

        # Starting Character
        items_to_precollect.append(DayOfTheTentacleItems[f"CHARACTER_{self.starting_character.name}"].value)

        ## Item Pool
        item_pool: List[DayOfTheTentacleItem] = list()

        # Characters
        item: DayOfTheTentacleItems
        for item in items_with_tag(DayOfTheTentacleTags.CHARACTER_ITEM):
            if item.value not in items_to_precollect:
                item_pool.append(self.create_item(item.value))

        # Inventory Items
        for item in items_with_tag(DayOfTheTentacleTags.INVENTORY_ITEM):
            item_pool.append(self.create_item(item.value))

        # Goal Items
        for _ in range(self.swiss_deposits_total):
            item_pool.append(self.create_item(DayOfTheTentacleItems.SWISS_DEPOSIT.value))

        # Filler
        total_location_count: int = len(self.multiworld.get_unfilled_locations(self.player))
        to_fill_location_count: int = total_location_count - len(item_pool)

        for _ in range(to_fill_location_count):
            item_pool.append(self.create_item(self.get_filler_item_name()))

        self.multiworld.itempool += item_pool

        item_name: str
        for item_name in items_to_precollect:
            self.multiworld.push_precollected(self.create_item(item_name))

    def create_item(self, name: str) -> DayOfTheTentacleItem:
        data: DayOfTheTentacleItemData = item_data[DayOfTheTentacleItems(name)]

        return DayOfTheTentacleItem(
            name,
            data.classification,
            data.archipelago_id,
            self.player,
        )

    def generate_basic(self) -> None:
        self.multiworld.completion_condition[self.player] = lambda state: state.can_reach_region("Endgame", self.player)

    def fill_slot_data(self) -> Dict[str, Any]:
        slot_data: Dict[str, Any] = self.options.as_dict(
            "goal",
            "swiss_deposits_total",
            "swiss_deposits_required",
            "starting_character",
            "include_room_visits",
            "include_voice_lines",
        )

        slot_data["swiss_deposits_required"] = self.swiss_deposits_required

        return slot_data

    def get_filler_item_name(self) -> str:
        return self.random.choice(self.filler_item_names)

    @staticmethod
    def interpret_slot_data(slot_data: Dict[str, Any]) -> Dict[str, Any]:
        return process_slot_data(slot_data)

    def _apply_universal_tracker_passthrough(self) -> None:
        if "Day of the Tentacle" in self.multiworld.re_gen_passthrough:
            passthrough: Dict[str, Any] = self.multiworld.re_gen_passthrough["Day of the Tentacle"]

            self.goal = passthrough["goal"]
            self.swiss_deposits_total = passthrough["swiss_deposits_total"]
            self.swiss_deposits_required = passthrough["swiss_deposits_required"]
            self.starting_character = passthrough["starting_character"]
            self.include_room_visits = passthrough["include_room_visits"]
            self.include_voice_lines = passthrough["include_voice_lines"]

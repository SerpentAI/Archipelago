from typing import Any, Dict, List, Optional, TextIO, Tuple

from rule_builder.rules import Rule, And, CanReachLocation

from BaseClasses import Item, Location, Region, Tutorial

from worlds.AutoWorld import WebWorld, World

from .data.item_data import RivenItemData, item_data
from .data.location_data import RivenLocationData, location_data
from .data.rule_data import entrance_rule_data, location_rule_data

from .data_funcs import (
    id_to_goals,
    id_to_starting_movement_speeds,
    item_names_to_id,
    item_groups,
    items_with_tag,
    location_groups,
    location_names_to_id,
    process_slot_data,
)

from .enums import (
    RivenAPGoals,
    RivenAPStartingMovementSpeeds,
    RivenAPStartingRoutes,
    RivenAPTags,
    RivenAPTrapTypes,
    RivenItems,
    RivenLocations,
    RivenRegions,
)

from .options import RivenOptions, option_groups


class RivenItem(Item):
    game = "Riven"


class RivenLocation(Location):
    game = "Riven"


class RivenWebWorld(WebWorld):
    theme: str = "ocean"

    tutorials: List[Tutorial] = [
        Tutorial(
            "Multiworld Setup Guide",
            "A guide to setting up the Riven randomizer connected to an Archipelago Multiworld",
            "English",
            "setup_en.md",
            "setup/en",
            ["Serpent.AI"],
        )
    ]

    option_groups = option_groups


class RivenWorld(World):
    """
    Riven revitalizes the classic point-and-click puzzle adventure experience with modernized real-time visuals and fluid free-roaming navigation, rebuilding the iconic 1997 masterpiece into a fully realized 3D world. Featuring expanded environmental narrative elements and a remastered atmospheric soundtrack, the game delivers redesigned puzzles and intricate island environments that reward meticulous observation and profound logical deduction.
    """

    options_dataclass = RivenOptions
    options: RivenOptions

    game = "Riven"

    item_name_to_id = item_names_to_id()
    location_name_to_id = location_names_to_id()

    item_name_groups = item_groups()
    location_name_groups = location_groups()

    required_client_version: Tuple[int, int, int] = (0, 6, 7)

    web = RivenWebWorld()

    filler_item_names: List[str] = item_groups()["Filler Item"]

    # Options
    goal: RivenAPGoals
    extra_progressive_star_fissure_telescope_solutions: int
    starting_movement_speed: RivenAPStartingMovementSpeeds
    progressive_movement_speed_item_count: int
    trap_percentage: int
    trap_weights: Dict[RivenAPTrapTypes, int]
    trap_duration: int

    # Generation
    selected_starting_route: RivenAPStartingRoutes

    # Universal Tracker
    location_id_to_alias: Dict[int, str]
    ut_can_gen_without_yaml: bool = True
    explicit_indirect_conditions = False

    @property
    def is_universal_tracker(self) -> bool:
        return hasattr(self.multiworld, "re_gen_passthrough")

    def generate_early(self) -> None:
        self.goal = id_to_goals()[self.options.goal.value]
        self.extra_progressive_star_fissure_telescope_solutions = self.options.extra_progressive_star_fissure_telescope_solutions.value

        self.starting_movement_speed = id_to_starting_movement_speeds()[self.options.starting_movement_speed.value]
        self.progressive_movement_speed_item_count = self.options.progressive_movement_speed_item_count.value

        self.trap_percentage = self.options.trap_percentage.value

        self.trap_weights = {
            trap_type: 1 for trap_type in RivenAPTrapTypes
        }

        trap_type_name: str
        weight: Any
        for trap_type_name, weight in self.options.trap_weights.value.items():
            try:
                trap_type: RivenAPTrapTypes = RivenAPTrapTypes(trap_type_name)
            except Exception:
                continue

            if isinstance(weight, int) and weight >= 0:
                self.trap_weights[trap_type] = weight

        self.trap_duration = self.options.trap_duration.value

        starting_route_pool: List[str] = sorted([starting_route.value for starting_route in RivenAPStartingRoutes])
        self.selected_starting_route = RivenAPStartingRoutes(self.random.choice(starting_route_pool))

        # Universal Tracker Support
        if self.is_universal_tracker:
            self.location_id_to_alias = dict()
            self._apply_universal_tracker_passthrough()

    def create_regions(self) -> None:
        regions_to_skip: List[RivenRegions] = list()

        if self.goal == RivenAPGoals.STAR_FISSURE:
            regions_to_skip.extend([RivenRegions.PRISON_JAIL_CELL, RivenRegions.AGE_OF_TAY, RivenRegions.AGE_233])

        region_mapping: Dict[RivenRegions, Region] = dict()

        region_enum_item: RivenRegions
        for region_enum_item in entrance_rule_data.keys():
            if region_enum_item in regions_to_skip:
                continue

            region: Region = Region(region_enum_item.value, self.player, self.multiworld)

            region_mapping[region_enum_item] = region
            self.multiworld.regions.append(region)

        region_locations_mapping: Dict[RivenRegions, List[RivenLocations]] = dict()

        location: RivenLocations
        data: RivenLocationData
        for location, data in location_data.items():
            if data.region in regions_to_skip:
                continue

            if data.region not in region_locations_mapping:
                region_locations_mapping[data.region] = list()

            region_locations_mapping[data.region].append(location)

        region_enum_item: RivenRegions
        region: Region
        for region_enum_item, region in region_mapping.items():
            regions_locations: List[RivenLocations] = region_locations_mapping.get(region_enum_item, list())

            # Locations
            location_enum_item: RivenLocations
            for location_enum_item in regions_locations:
                data: RivenLocationData = location_data[location_enum_item]

                location: RivenLocation = RivenLocation(
                    self.player,
                    location_enum_item.value,
                    data.archipelago_id,
                    region_mapping[data.region],
                )

                # Access Rules
                location_rule: Optional[Rule] = location_rule_data[location_enum_item]

                if location_rule is not None:
                    self.set_rule(location, location_rule)

                region.locations.append(location)

            # Connections
            region_exit: RivenRegions
            for region_exit in entrance_rule_data[region_enum_item].keys():
                if region_exit in regions_to_skip:
                    continue

                entrance_rule: Optional[Rule] = entrance_rule_data[region_enum_item][region_exit]

                if entrance_rule is None:
                    region.connect(region_mapping[region_exit])
                else:
                    region.connect(region_mapping[region_exit], rule=entrance_rule)

        # Endgame
        endgame_region: Region = Region("Endgame", self.player, self.multiworld)
        self.multiworld.regions.append(endgame_region)

        star_fissure_region: Region = region_mapping[RivenRegions.TEMPLE_STAR_FISSURE]

        if self.goal == RivenAPGoals.GOOD_ENDING:
            star_fissure_region.connect(
                endgame_region,
                rule=And(
                    CanReachLocation(
                        RivenLocations.AGE_233_TRAP_GEHN.value,
                        parent_region_name=RivenRegions.AGE_233.value,
                    ),
                    CanReachLocation(
                        RivenLocations.PRISON_JAIL_CELL_FREE_CATHERINE.value,
                        parent_region_name=RivenRegions.PRISON_JAIL_CELL.value,
                    ),
                )
            )
        elif self.goal == RivenAPGoals.STAR_FISSURE:
            star_fissure_region.connect(endgame_region)

    def create_items(self) -> None:
        ## Precollect
        items_to_precollect: List[str] = list()

        # Starting Route Items
        starting_route_to_items: Dict[RivenAPStartingRoutes, Tuple[RivenItems, ...]] = {
            RivenAPStartingRoutes.TEMPLE_GOLDEN_DOME: (RivenItems.TEMPLE_GATE_ROOM_GATE_GOLDEN_DOME,),
            RivenAPStartingRoutes.STARRY_PRISON: (RivenItems.TEMPLE_GATE_ROOM_GATE_SPINNING_DOME,),
        }

        item: RivenItems
        for item in starting_route_to_items[self.selected_starting_route]:
            items_to_precollect.append(item.value)

        ## Item Pool
        item_pool: List[RivenItem] = list()

        # Unlock Items
        item: RivenItems
        for item in items_with_tag(RivenAPTags.UNLOCK_ITEM):
            if item.value not in items_to_precollect:
                item_pool.append(self.create_item(item.value))

        # Solution Items
        item: RivenItems
        for item in items_with_tag(RivenAPTags.SOLUTION_ITEM):
            if self.goal == RivenAPGoals.STAR_FISSURE and item == RivenItems.SOLUTION_PRISON_ELEVATOR:
                continue

            item_count: int = 1

            if item == RivenItems.SOLUTION_STAR_FISSURE_TELESCOPE:
                item_count = 10 + self.extra_progressive_star_fissure_telescope_solutions

            for _ in range(item_count):
                item_pool.append(self.create_item(item.value))

        # Useful Items
        item: RivenItems
        for item in items_with_tag(RivenAPTags.USEFUL_ITEM):
            item_count: int = 1

            if item == RivenItems.MOVEMENT_SPEED:
                item_count = self.progressive_movement_speed_item_count

            for _ in range(item_count):
                item_pool.append(self.create_item(item.value))

        # Filler / Traps
        total_location_count: int = len(self.multiworld.get_unfilled_locations(self.player))
        to_fill_location_count: int = total_location_count - len(item_pool)

        item_name: str
        for item_name in self._generate_filler_trap_item_pool(to_fill_location_count):
            item_pool.append(self.create_item(item_name))

        self.multiworld.itempool += item_pool

        item: str
        for item in items_to_precollect:
            self.multiworld.push_precollected(self.create_item(item))

    def create_item(self, name: str) -> RivenItem:
        data: RivenItemData = item_data[RivenItems(name)]

        return RivenItem(
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
            "extra_progressive_star_fissure_telescope_solutions",
            "starting_movement_speed",
            "progressive_movement_speed_item_count",
            "trap_percentage",
            "trap_weights",
            "trap_duration"
        )

        slot_data["selected_starting_route"] = self.selected_starting_route.value

        return slot_data

    def write_spoiler_header(self, spoiler_handle: TextIO) -> None:
        spoiler_handle.write(f"\nStarting Route: {self.selected_starting_route.value}\n")

    def get_filler_item_name(self) -> str:
        return self.random.choice(self.filler_item_names)

    @staticmethod
    def interpret_slot_data(slot_data: Dict[str, Any]) -> Dict[str, Any]:
        return process_slot_data(slot_data)

    def _apply_universal_tracker_passthrough(self) -> None:
        if "Riven" in self.multiworld.re_gen_passthrough:
            passthrough: Dict[str, Any] = self.multiworld.re_gen_passthrough["Riven"]

            self.goal = passthrough["goal"]
            self.extra_progressive_star_fissure_telescope_solutions = passthrough["extra_progressive_star_fissure_telescope_solutions"]
            self.starting_movement_speed = passthrough["starting_movement_speed"]
            self.progressive_movement_speed_item_count = passthrough["progressive_movement_speed_item_count"]
            self.trap_percentage = passthrough["trap_percentage"]
            self.trap_weights = passthrough["trap_weights"]
            self.trap_duration = passthrough["trap_duration"]

            self.selected_starting_route = passthrough["selected_starting_route"]

    def _generate_filler_trap_item_pool(self, count: int) -> List[str]:
        trap_items_needed: int = round(self.trap_percentage / 100 * count)
        filler_items_needed: int = count - trap_items_needed

        item_pool: List[str] = list()

        if trap_items_needed > 0:
            trap_items: List[RivenAPTrapTypes] = list(self.trap_weights.keys())
            trap_item_weights: List[int] = list(self.trap_weights.values())

            if sum(trap_item_weights) == 0:
                trap_item_weights = [1 for _ in trap_item_weights]

            item_pool.extend([
                trap_type.value for trap_type in self.random.choices(trap_items, trap_item_weights, k=trap_items_needed)
            ])

        for _ in range(filler_items_needed):
            filler_item_name: str = self.random.choice(self.filler_item_names)
            item_pool.append(filler_item_name)

        return item_pool

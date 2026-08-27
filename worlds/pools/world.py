import logging

from typing import Any, Dict, List, Optional, TextIO, Tuple

from rule_builder.rules import Rule, Has

from BaseClasses import Item, Location, Region, Tutorial


from worlds.AutoWorld import WebWorld, World

from .data.game_data import eligible_starting_levels
from .data.item_data import PoolsItemData, item_data
from .data.location_data import PoolsLocationData, location_data
from .data.rule_data import location_rule_data

from .data_funcs import (
    id_to_goals,
    item_names_to_id,
    item_groups,
    location_groups,
    location_names_to_id,
    locations_with_tag,
    process_slot_data,
)

from .enums import (
    PoolsGoals,
    PoolsItems,
    PoolsLevels,
    PoolsLocations,
    PoolsTags,
    PoolsTrapTypes,
)

from .options import PoolsOptions, option_groups


class PoolsItem(Item):
    game = "POOLS"


class PoolsLocation(Location):
    game = "POOLS"


class PoolsWebWorld(WebWorld):
    theme: str = "ocean"

    tutorials: List[Tutorial] = [
        Tutorial(
            "Multiworld Setup Guide",
            "A guide to setting up the POOLS randomizer connected to an Archipelago Multiworld",
            "English",
            "setup_en.md",
            "setup/en",
            ["Serpent.AI"],
        )
    ]

    option_groups = option_groups


class PoolsWorld(World):
    """
    POOLS delivers a deeply unsettling psychological horror experience defined by oppressive silence, disorienting architectural surrealism, and pure environmental dread. Stripping away traditional HUD elements, inventory management, and monster encounters, the game relies entirely on photorealistic tilework, eerie acoustics, and the creeping anxiety of navigating an endless, sunlit subterranean maze.
    """

    options_dataclass = PoolsOptions
    options: PoolsOptions

    game = "POOLS"

    item_name_to_id = item_names_to_id()
    location_name_to_id = location_names_to_id()

    item_name_groups = item_groups()
    location_name_groups = location_groups()

    required_client_version: Tuple[int, int, int] = (0, 6, 7)

    web = PoolsWebWorld()

    filler_item_names: List[str] = item_groups()["Filler Item"]

    # Options
    goal: PoolsGoals
    rubber_ducks_total: int
    rubber_ducks_required: int
    include_level_0: bool
    include_chairs: bool
    trap_percentage: int
    trap_weights: Dict[PoolsTrapTypes, int]
    trap_duration: int

    # Generation
    selected_starting_level: PoolsLevels

    # Universal Tracker
    location_id_to_alias: Dict[int, str]
    ut_can_gen_without_yaml: bool = True
    explicit_indirect_conditions = False

    @property
    def is_universal_tracker(self) -> bool:
        return hasattr(self.multiworld, "re_gen_passthrough")

    def generate_early(self) -> None:
        self.goal = id_to_goals()[self.options.goal.value]

        self.rubber_ducks_required = self.options.rubber_ducks_required.value
        self.rubber_ducks_total = self.options.rubber_ducks_total.value

        if self.rubber_ducks_required > self.rubber_ducks_total:
            self.rubber_ducks_required = self.rubber_ducks_total

            logging.warning(
                f"POOLS: {self.player_name} has more required rubber ducks than total rubber ducks. "
                "Adjusting required rubber ducks to match total rubber ducks..."
            )

        # Location Options
        self.include_level_0 = bool(self.options.include_level_0.value)
        self.include_chairs = bool(self.options.include_chairs.value)

        # Starting Level
        starting_level_pool: List[PoolsLevels] = eligible_starting_levels[:]

        if self.include_level_0:
            starting_level_pool.append(PoolsLevels.LEVEL_0)

        self.selected_starting_level = self.random.choice(starting_level_pool)

        # Traps
        self.trap_percentage = self.options.trap_percentage.value

        self.trap_weights = {
            trap_type: 1 for trap_type in PoolsTrapTypes
        }

        trap_type_name: str
        weight: Any
        for trap_type_name, weight in self.options.trap_weights.value.items():
            try:
                trap_type: PoolsTrapTypes = PoolsTrapTypes(trap_type_name)
            except Exception:
                continue

            if isinstance(weight, int) and weight >= 0:
                self.trap_weights[trap_type] = weight

        self.trap_duration = self.options.trap_duration.value

        # Universal Tracker Support
        if self.is_universal_tracker:
            self.location_id_to_alias = dict()
            self._apply_universal_tracker_passthrough()

    def create_regions(self) -> None:
        # Menu
        region_menu: Region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(region_menu)

        # Endgame
        region_endgame: Region = Region("Endgame", self.player, self.multiworld)

        # Levels
        level: PoolsLevels
        for level in list(PoolsLevels)[:-1]:
            if level == PoolsLevels.LEVEL_0 and not self.include_level_0:
                continue

            region_level: Region = Region(level.value, self.player, self.multiworld)

            level_tag: PoolsTags = getattr(PoolsTags, f"{level.name}_LOCATION")

            level_locations: List[PoolsLocations] = locations_with_tag(level_tag)

            location_enum_item: PoolsLocations
            for location_enum_item in level_locations:
                data: PoolsLocationData = location_data[location_enum_item]

                if not self.include_chairs and PoolsTags.CHAIR_LOCATION in data.tags:
                    continue

                location: PoolsLocation = PoolsLocation(
                    self.player,
                    location_enum_item.value,
                    data.archipelago_id,
                    region_level,
                )

                location_access_rule: Optional[Rule] = location_rule_data.get(location_enum_item)

                if location_access_rule is not None:
                    self.set_rule(location, location_access_rule)

                region_level.locations.append(location)

            if level == PoolsLevels.LEVEL_6:
                region_level.connect(region_endgame, rule=Has(PoolsItems.RUBBER_DUCK.value, self.rubber_ducks_required))
                self.multiworld.regions.append(region_endgame)

            level_unlock_item: PoolsItems = getattr(PoolsItems, f"{level.name}_UNLOCK")

            region_menu.connect(region_level, rule=Has(level_unlock_item.value))

            self.multiworld.regions.append(region_level)

    def create_items(self) -> None:
        ## Precollect
        items_to_precollect: List[str] = list()

        # Starting Level
        starting_level_unlock_item: PoolsItems = getattr(PoolsItems, f"{self.selected_starting_level.name}_UNLOCK")
        items_to_precollect.append(starting_level_unlock_item.value)

        ## Item Pool
        item_pool: List[PoolsItem] = list()

        # Goal Items
        i: int
        for i in range(self.rubber_ducks_total):
            item_pool.append(self.create_item(PoolsItems.RUBBER_DUCK.value))

        # Level Unlock Items
        level: PoolsLevels
        for level in list(PoolsLevels):
            if level == PoolsLevels.ENDING:
                continue
            elif level == PoolsLevels.LEVEL_0 and not self.include_level_0:
                continue
            elif level == self.selected_starting_level:
                continue

            level_unlock_item: PoolsItems = getattr(PoolsItems, f"{level.name}_UNLOCK")

            item_pool.append(self.create_item(level_unlock_item.value))

        # Pool Depths
        i: int
        for i in range(1, 12):
            pool_depth_item: PoolsItems = getattr(PoolsItems, f"POOLS_{i}T")
            item_pool.append(self.create_item(pool_depth_item.value))

        # Diving Boards
        item_pool.append(self.create_item(PoolsItems.DIVING_BOARDS.value))

        # Slides
        item_pool.append(self.create_item(PoolsItems.SLIDES_RED.value))
        item_pool.append(self.create_item(PoolsItems.SLIDES_YELLOW.value))
        item_pool.append(self.create_item(PoolsItems.SLIDES_GREEN.value))
        item_pool.append(self.create_item(PoolsItems.SLIDES_BLUE.value))

        if self.include_level_0:
            item_pool.append(self.create_item(PoolsItems.SLIDES_EXTRA.value))

        # Chairs
        if self.include_chairs:
            item_pool.append(self.create_item(PoolsItems.CHAIRS_PLASTIC.value))
            item_pool.append(self.create_item(PoolsItems.CHAIRS_SAUNA.value))
            item_pool.append(self.create_item(PoolsItems.CHAIRS_ARMCHAIR.value))
            item_pool.append(self.create_item(PoolsItems.CHAIRS_WOODEN.value))
            item_pool.append(self.create_item(PoolsItems.CHAIRS_SUBWAY.value))

            if self.include_level_0:
                item_pool.append(self.create_item(PoolsItems.CHAIRS_PARK.value))
                item_pool.append(self.create_item(PoolsItems.CHAIRS_SOFA.value))

        # Useful Items
        item_pool.append(self.create_item(PoolsItems.RUN.value))

        for _ in range(30):
            item_pool.append(self.create_item(PoolsItems.PROGRESSIVE_MOVEMENT_SPEED.value))
            item_pool.append(self.create_item(PoolsItems.PROGRESSIVE_WATER_SPEED.value))

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

    def create_item(self, name: str) -> PoolsItem:
        data: PoolsItemData = item_data[PoolsItems(name)]

        return PoolsItem(
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
            "rubber_ducks_total",
            "rubber_ducks_required",
            "include_level_0",
            "include_chairs",
            "trap_percentage",
            "trap_weights",
            "trap_duration",
        )

        slot_data["trap_weights"] = {
            trap_type.value: weight for trap_type, weight in self.trap_weights.items()
        }

        slot_data["selected_starting_level"] = self.selected_starting_level.value

        # Relay generate_early Overrides
        if slot_data["rubber_ducks_required"] != self.rubber_ducks_required:
            slot_data["rubber_ducks_required"] = self.rubber_ducks_required

        return slot_data

    def write_spoiler_header(self, spoiler_handle: TextIO) -> None:
        spoiler_handle.write(f"\n\nStarting Level:  {self.selected_starting_level.value}\n")

    def get_filler_item_name(self) -> str:
        return self.random.choice(self.filler_item_names)

    @staticmethod
    def interpret_slot_data(slot_data: Dict[str, Any]) -> Dict[str, Any]:
        return process_slot_data(slot_data)

    def _apply_universal_tracker_passthrough(self) -> None:
        if "POOLS" in self.multiworld.re_gen_passthrough:
            passthrough: Dict[str, Any] = self.multiworld.re_gen_passthrough["POOLS"]

            self.goal = passthrough["goal"]
            self.rubber_ducks_total = passthrough["rubber_ducks_total"]
            self.rubber_ducks_required = passthrough["rubber_ducks_required"]
            self.include_level_0 = passthrough["include_level_0"]
            self.include_chairs = passthrough["include_chairs"]
            self.trap_percentage = passthrough["trap_percentage"]
            self.trap_weights = passthrough["trap_weights"]
            self.trap_duration = passthrough["trap_duration"]

            self.selected_starting_level = passthrough["selected_starting_level"]

    def _generate_filler_trap_item_pool(self, count: int) -> List[str]:
        trap_items_needed: int = round(self.trap_percentage / 100 * count)
        filler_items_needed: int = count - trap_items_needed

        item_pool: List[str] = list()

        if trap_items_needed > 0:
            trap_items: List[PoolsTrapTypes] = list(self.trap_weights.keys())
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

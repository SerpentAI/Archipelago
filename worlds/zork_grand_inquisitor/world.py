from typing import Any, Dict, List, Set, Tuple, Union

from BaseClasses import Item, ItemClassification, Location, Region, Tutorial

from worlds.AutoWorld import WebWorld, World

from .data.item_data import ZorkGrandInquisitorItemData
from .data.location_data import ZorkGrandInquisitorLocationData

from .data.mapping_data import (
    early_items_for_starting_location,
    endgame_connecting_regions_for_goal,
    starter_kits_for_starting_location,
    starting_location_to_region,
)

from .data.region_data import region_data

from .data_funcs import (
    item_names_to_id,
    item_names_to_item,
    location_names_to_id,
    id_to_craftable_spell_behaviors,
    id_to_deathsanity,
    id_to_goals,
    id_to_hotspots,
    id_to_landmarksanity,
    id_to_starting_locations,
    item_groups,
    items_with_tag,
    location_groups,
    locations_by_region_for_world,
    prepare_item_data,
    prepare_location_data,
    location_access_rule_for,
    entrance_access_rule_for,
    goal_access_rule_for,
)

from .enums import (
    ZorkGrandInquisitorCraftableSpellBehaviors,
    ZorkGrandInquisitorDeathsanity,
    ZorkGrandInquisitorEvents,
    ZorkGrandInquisitorGoals,
    ZorkGrandInquisitorHotspots,
    ZorkGrandInquisitorItems,
    ZorkGrandInquisitorLandmarksanity,
    ZorkGrandInquisitorLocations,
    ZorkGrandInquisitorRegions,
    ZorkGrandInquisitorStartingLocations,
    ZorkGrandInquisitorTags,
)

from .options import ZorkGrandInquisitorOptions


class ZorkGrandInquisitorItem(Item):
    game = "Zork Grand Inquisitor"


class ZorkGrandInquisitorLocation(Location):
    game = "Zork Grand Inquisitor"


class ZorkGrandInquisitorWebWorld(WebWorld):
    theme: str = "stone"

    tutorials: List[Tutorial] = [
        Tutorial(
            "Multiworld Setup Guide",
            "A guide to setting up the Zork Grand Inquisitor randomizer connected to an Archipelago Multiworld",
            "English",
            "setup_en.md",
            "setup/en",
            ["Serpent.AI"],
        )
    ]


class ZorkGrandInquisitorWorld(World):
    """
    Zork: Grand Inquisitor is a 1997 point-and-click adventure game for PC.
    Magic has been banned from the great Underground Empire of Zork. By edict of the Grand Inquisitor Mir Yannick, the
    Empire has been sealed off and the practice of mystic arts declared punishable by "Totemization" (a very bad thing).
    The only way to restore magic to the kingdom is to find three hidden artifacts: The Coconut of Quendor, The Cube of
    Foundation, and The Skull of Yoruk.
    """

    options_dataclass = ZorkGrandInquisitorOptions
    options: ZorkGrandInquisitorOptions

    game = "Zork Grand Inquisitor"

    item_name_to_id = item_names_to_id()
    location_name_to_id = location_names_to_id()

    item_name_groups = item_groups()
    location_name_groups = location_groups()

    required_client_version: Tuple[int, int, int] = (0, 5, 0)

    web = ZorkGrandInquisitorWebWorld()

    craftable_spells: ZorkGrandInquisitorCraftableSpellBehaviors
    deathsanity: ZorkGrandInquisitorDeathsanity
    early_items: Tuple[ZorkGrandInquisitorItems, ...]
    filler_item_names: List[str] = item_groups()["Filler"]
    goal: ZorkGrandInquisitorGoals
    grant_missable_location_checks: bool
    hotspots: ZorkGrandInquisitorHotspots
    initial_totemizer_destination: ZorkGrandInquisitorItems
    item_data: Dict[ZorkGrandInquisitorItems, ZorkGrandInquisitorItemData]
    item_name_to_item: Dict[str, ZorkGrandInquisitorItems] = item_names_to_item()
    landmarksanity: ZorkGrandInquisitorLandmarksanity

    location_data: Dict[
        Union[ZorkGrandInquisitorLocations, ZorkGrandInquisitorEvents], ZorkGrandInquisitorLocationData
    ]

    locked_items: Dict[ZorkGrandInquisitorLocations, ZorkGrandInquisitorItems]
    place_early_items_locally: bool
    starter_kit: Tuple[ZorkGrandInquisitorItems, ...]
    starting_location: ZorkGrandInquisitorStartingLocations

    def generate_early(self) -> None:
        self.goal = id_to_goals()[self.options.goal.value]
        self.starting_location = id_to_starting_locations()[self.options.starting_location.value]

        self.starter_kit = tuple()

        if starter_kits_for_starting_location[self.starting_location] is not None:
            self.starter_kit = self.random.choice(
                starter_kits_for_starting_location[self.starting_location]
            )

        self.early_items = tuple()

        if early_items_for_starting_location[self.starting_location] is not None:
            self.early_items = self.random.choice(
                early_items_for_starting_location[self.starting_location]
            )

        self.craftable_spells = id_to_craftable_spell_behaviors()[self.options.craftable_spells.value]
        self.hotspots = id_to_hotspots()[self.options.hotspots]

        self.deathsanity = id_to_deathsanity()[self.options.deathsanity]
        self.landmarksanity = id_to_landmarksanity()[self.options.landmarksanity]

        self.place_early_items_locally = bool(self.options.place_early_items_locally)
        self.grant_missable_location_checks = bool(self.options.grant_missable_location_checks)

        self.item_data = prepare_item_data(
            self.starting_location,
            self.goal,
            self.deathsanity,
            self.landmarksanity,
        )

        self.location_data = prepare_location_data(
            self.starting_location,
            self.goal,
            self.deathsanity,
            self.landmarksanity,
        )

        self.locked_items = self._prepare_locked_items()

        self.initial_totemizer_destination = self._select_initial_totemizer_destination()

    def create_regions(self) -> None:
        region_mapping: Dict[ZorkGrandInquisitorRegions, Region] = dict()

        region_enum_item: ZorkGrandInquisitorRegions
        for region_enum_item in region_data.keys():
            region_mapping[region_enum_item] = Region(region_enum_item.value, self.player, self.multiworld)

        region_locations_mapping: Dict[ZorkGrandInquisitorRegions, List[ZorkGrandInquisitorLocations]]
        region_locations_mapping = locations_by_region_for_world(self.location_data)

        region_connecting_endgame: ZorkGrandInquisitorRegions = endgame_connecting_regions_for_goal[self.goal]

        region_enum_item: ZorkGrandInquisitorRegions
        region: Region
        for region_enum_item, region in region_mapping.items():
            regions_locations: List[ZorkGrandInquisitorLocations] = region_locations_mapping[region_enum_item]

            # Locations
            location_enum_item: ZorkGrandInquisitorLocations
            for location_enum_item in regions_locations:
                data: ZorkGrandInquisitorLocationData = self.location_data[location_enum_item]

                location: ZorkGrandInquisitorLocation = ZorkGrandInquisitorLocation(
                    self.player,
                    location_enum_item.value,
                    data.archipelago_id,
                    region_mapping[data.region],
                )

                # Locked Items
                if location_enum_item in self.locked_items:
                    location.place_locked_item(self.create_item(self.locked_items[location_enum_item].value))
                elif isinstance(location_enum_item, ZorkGrandInquisitorEvents):
                    location.place_locked_item(
                        ZorkGrandInquisitorItem(
                            data.event_item_name,
                            ItemClassification.progression,
                            None,
                            self.player,
                        )
                    )

                # Access Rules
                location_access_rule: str = location_access_rule_for(location_enum_item, self.player)

                if location_access_rule != "lambda state: True":
                    location.access_rule = eval(location_access_rule)

                region.locations.append(location)

            # Connections
            region_exit: ZorkGrandInquisitorRegions
            for region_exit in region_data[region_enum_item].exits or tuple():
                entrance_access_rule: str = entrance_access_rule_for(region_enum_item, region_exit, self.player)

                if entrance_access_rule == "lambda state: True":
                    region.connect(region_mapping[region_exit])
                else:
                    region.connect(region_mapping[region_exit], rule=eval(entrance_access_rule))

            if region_enum_item == region_connecting_endgame:
                goal_access_rule: str = goal_access_rule_for(region_enum_item, self.goal, self.player)
                region.connect(region_mapping[ZorkGrandInquisitorRegions.ENDGAME], rule=eval(goal_access_rule))

            self.multiworld.regions.append(region)

        # Connect "Menu" region to starting location and to endgame when applicable
        region_menu: Region = Region("Menu", self.player, self.multiworld)
        region_starting_location: ZorkGrandInquisitorRegions = starting_location_to_region[self.starting_location]

        region_menu.connect(region_mapping[ZorkGrandInquisitorRegions.ANYWHERE])
        region_menu.connect(region_mapping[region_starting_location])

        if region_connecting_endgame == ZorkGrandInquisitorRegions.MENU:
            goal_access_rule: str = goal_access_rule_for(ZorkGrandInquisitorRegions.MENU, self.goal, self.player)
            region_menu.connect(region_mapping[ZorkGrandInquisitorRegions.ENDGAME], rule=eval(goal_access_rule))

        self.multiworld.regions.append(region_menu)

    def create_items(self) -> None:
        items_to_ignore: Set[ZorkGrandInquisitorItems] = set()
        items_to_precollect: Set[ZorkGrandInquisitorItems] = set()
        items_to_place_early: Set[ZorkGrandInquisitorItems]

        item: ZorkGrandInquisitorItems

        for item in items_with_tag(ZorkGrandInquisitorTags.FILLER):
            items_to_ignore.add(item)

        for item in items_with_tag(ZorkGrandInquisitorTags.GOAL_THREE_ARTIFACTS):
            items_to_ignore.add(item)

        for item in self.locked_items.values():
            items_to_ignore.add(item)

        for item in self.starter_kit:
            items_to_precollect.add(item)

        hotspot_items: Set[ZorkGrandInquisitorItems] = items_with_tag(ZorkGrandInquisitorTags.HOTSPOT)

        hotspot_regional_items: Set[ZorkGrandInquisitorItems] = items_with_tag(
            ZorkGrandInquisitorTags.HOTSPOT_REGIONAL
        )

        if self.hotspots == ZorkGrandInquisitorHotspots.ENABLED:
            for item in hotspot_items:
                items_to_ignore.add(item)

            for item in hotspot_regional_items:
                items_to_precollect.add(item)
        elif self.hotspots == ZorkGrandInquisitorHotspots.REQUIRE_ITEM_PER_REGION:
            for item in hotspot_items:
                items_to_ignore.add(item)
        elif self.hotspots == ZorkGrandInquisitorHotspots.REQUIRE_ITEM_PER_HOTSPOT:
            for item in hotspot_regional_items:
                items_to_ignore.add(item)

        items_to_precollect.add(self.initial_totemizer_destination)

        if self.starting_location != ZorkGrandInquisitorStartingLocations.DM_LAIR_INTERIOR:
            items_to_precollect.add(ZorkGrandInquisitorItems.HOTSPOT_DUNGEON_MASTERS_HOUSE_EXIT)

        if self.starting_location != ZorkGrandInquisitorStartingLocations.SPELL_LAB:
            items_to_precollect.add(ZorkGrandInquisitorItems.HOTSPOT_SPELL_LAB_BRIDGE_EXIT)

        items_to_place_early = set(self.early_items) - items_to_precollect

        # Create Item Pool
        item_pool: List[ZorkGrandInquisitorItem] = list()

        data: ZorkGrandInquisitorItemData
        for item, data in self.item_data.items():
            if item in items_to_ignore or item in items_to_precollect:
                continue

            item_pool.append(self.create_item(item.value))

        total_locations: int = len(self.multiworld.get_unfilled_locations(self.player))
        item_pool += [self.create_filler() for _ in range(total_locations - len(item_pool))]

        self.multiworld.itempool += item_pool

        # Precollect Items
        for item in items_to_precollect:
            self.multiworld.push_precollected(self.create_item(item.value))

        # Set Early Items
        # TODO: Does this even work? Needs testing
        if len(items_to_place_early):
            early: Dict[int, Dict[str, int]]
            early = self.multiworld.local_early_items if self.place_early_items_locally else self.multiworld.early_items

            for item in items_to_place_early:
                early[self.player][item.value] = 1

    def create_item(self, name: str) -> ZorkGrandInquisitorItem:
        data: ZorkGrandInquisitorItemData = self.item_data[self.item_name_to_item[name]]

        return ZorkGrandInquisitorItem(
            name,
            data.classification,
            data.archipelago_id,
            self.player,
        )

    def generate_basic(self) -> None:
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)

    def fill_slot_data(self) -> Dict[str, Any]:
        slot_data: Dict[str, Any] = self.options.as_dict(
            "goal",
            "starting_location",
            "hotspots",
            "craftable_spells",
            "deathsanity",
            "landmarksanity",
            "grant_missable_location_checks",
        )

        slot_data["initial_totemizer_destination"] = self.initial_totemizer_destination.value

        return slot_data

    def get_filler_item_name(self) -> str:
        return self.random.choice(self.filler_item_names)

    def _prepare_locked_items(
        self,
    ) -> Dict[ZorkGrandInquisitorLocations, ZorkGrandInquisitorItems]:
        locked_items: Dict[ZorkGrandInquisitorLocations, ZorkGrandInquisitorItems] = dict()

        # Goal Items
        if self.goal == ZorkGrandInquisitorGoals.THREE_ARTIFACTS:
            locked_items[
                ZorkGrandInquisitorLocations.COME_TO_PAPA_YOU_NUT
            ] = ZorkGrandInquisitorItems.COCONUT_OF_QUENDOR

            locked_items[
                ZorkGrandInquisitorLocations.GOOD_PUZZLE_SMART_BROG
            ] = ZorkGrandInquisitorItems.SKULL_OF_YORUK

            locked_items[
                ZorkGrandInquisitorLocations.YOU_LOSE_MUFFET_ANTE_UP
            ] = ZorkGrandInquisitorItems.CUBE_OF_FOUNDATION

        # Craftable Spells
        if self.craftable_spells == ZorkGrandInquisitorCraftableSpellBehaviors.VANILLA:
            if ZorkGrandInquisitorItems.SPELL_BEBURTT not in self.starter_kit:
                locked_items[
                    ZorkGrandInquisitorLocations.IMBUE_BEBURTT
                ] = ZorkGrandInquisitorItems.SPELL_BEBURTT

            if ZorkGrandInquisitorItems.SPELL_OBIDIL not in self.starter_kit:
                locked_items[
                    ZorkGrandInquisitorLocations.OBIDIL_DRIED_UP
                ] = ZorkGrandInquisitorItems.SPELL_OBIDIL

            if ZorkGrandInquisitorItems.SPELL_SNAVIG not in self.starter_kit:
                locked_items[
                    ZorkGrandInquisitorLocations.SNAVIG_REPAIRED
                ] = ZorkGrandInquisitorItems.SPELL_SNAVIG

            if ZorkGrandInquisitorItems.SPELL_YASTARD not in self.starter_kit:
                locked_items[
                    ZorkGrandInquisitorLocations.OH_WOW_TALK_ABOUT_DEJA_VU
                ] = ZorkGrandInquisitorItems.SPELL_YASTARD
        elif self.craftable_spells == ZorkGrandInquisitorCraftableSpellBehaviors.ANY_SPELL:
            allowable_spells: Set[ZorkGrandInquisitorItems] = {
                ZorkGrandInquisitorItems.SPELL_BEBURTT,
                ZorkGrandInquisitorItems.SPELL_GLORF,
                ZorkGrandInquisitorItems.SPELL_GOLGATEM,
                ZorkGrandInquisitorItems.SPELL_IGRAM,
                ZorkGrandInquisitorItems.SPELL_KENDALL,
                ZorkGrandInquisitorItems.SPELL_OBIDIL,
                ZorkGrandInquisitorItems.SPELL_NARWILE,
                ZorkGrandInquisitorItems.SPELL_REZROV,
                ZorkGrandInquisitorItems.SPELL_SNAVIG,
                ZorkGrandInquisitorItems.SPELL_THROCK,
                ZorkGrandInquisitorItems.SPELL_YASTARD,
            }

            allowable_spells -= set(self.starter_kit)

            allowable_spells_yastard: List[str] = sorted([item.value for item in allowable_spells])

            spell_yastard: ZorkGrandInquisitorItems = self.item_name_to_item[
                self.random.choice(allowable_spells_yastard)
            ]

            locked_items[ZorkGrandInquisitorLocations.OH_WOW_TALK_ABOUT_DEJA_VU] = spell_yastard

            allowable_spells -= {spell_yastard}

            if self.starting_location != ZorkGrandInquisitorStartingLocations.SPELL_LAB:
                allowable_spells -= {
                    ZorkGrandInquisitorItems.SPELL_GOLGATEM,
                    ZorkGrandInquisitorItems.SPELL_REZROV,
                }

            allowable_spells_spell_lab: List[str] = sorted(
                [item.value for item in allowable_spells]
            )

            spells_to_lock: List[ZorkGrandInquisitorItems] = [
                self.item_name_to_item[item]
                for item in self.random.sample(allowable_spells_spell_lab, 3)
            ]

            locked_items[ZorkGrandInquisitorLocations.IMBUE_BEBURTT] = spells_to_lock[0]
            locked_items[ZorkGrandInquisitorLocations.OBIDIL_DRIED_UP] = spells_to_lock[1]
            locked_items[ZorkGrandInquisitorLocations.SNAVIG_REPAIRED] = spells_to_lock[2]

        return locked_items

    def _select_initial_totemizer_destination(self) -> ZorkGrandInquisitorItems:
        return self.random.choice((
            ZorkGrandInquisitorItems.TOTEMIZER_DESTINATION_HALL_OF_INQUISITION,
            ZorkGrandInquisitorItems.TOTEMIZER_DESTINATION_SURFACE_OF_MERZ,
            ZorkGrandInquisitorItems.TOTEMIZER_DESTINATION_NEWARK_NEW_JERSEY,
            ZorkGrandInquisitorItems.TOTEMIZER_DESTINATION_INFINITY,
            ZorkGrandInquisitorItems.TOTEMIZER_DESTINATION_STRAIGHT_TO_HELL,
        ))

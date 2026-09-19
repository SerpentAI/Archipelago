import logging

from typing import Any, Dict, List, Optional, TextIO, Tuple

from rule_builder.rules import And, Has, Or

from BaseClasses import Item, ItemClassification, Location, Region, Tutorial

from Options import OptionError

from worlds.AutoWorld import WebWorld, World

from .data.game_data import TwentyMinutesWeaponData, weapon_to_vanilla_weapon_data
from .data.item_data import TwentyMinutesItemData, item_data
from .data.location_data import TwentyMinutesLocationData, location_data

from .data_funcs import (
    id_to_goals,
    id_to_starting_maps,
    item_names_to_id,
    item_groups,
    location_groups,
    location_names_to_id,
    locations_with_tags,
    process_slot_data,
)

from .enums import (
    TwentyMinutesCharacters,
    TwentyMinutesGoalOptions,
    TwentyMinutesMapOptions,
    TwentyMinutesMaps,
    TwentyMinutesRunes,
    TwentyMinutesTags,
    TwentyMinutesTrapTypes,
    TwentyMinutesWeapons,
)

from .options import TwentyMinutesOptions, option_groups


class TwentyMinutesItem(Item):
    game = "20 Minutes Till Dawn"


class TwentyMinutesLocation(Location):
    game = "20 Minutes Till Dawn"


class TwentyMinutesWebWorld(WebWorld):
    theme: str = "partyTime"

    tutorials: List[Tutorial] = [
        Tutorial(
            "Multiworld Setup Guide",
            "A guide to setting up the 20 Minutes Till Dawn randomizer connected to an Archipelago Multiworld",
            "English",
            "setup_en.md",
            "setup/en",
            ["Serpent.AI"],
        )
    ]

    option_groups = option_groups


class TwentyMinutesWorld(World):
    """
    20 Minutes Till Dawn is a top-down survival roguelike where a lone hero fights off endless waves of Lovecraftian
    horrors under a starless sky. Choosing from a roster of characters, weapons, and runes, players must level up,
    adapt their build, and hold out until dawn breaks.
    """

    options_dataclass = TwentyMinutesOptions
    options: TwentyMinutesOptions

    game = "20 Minutes Till Dawn"

    item_name_to_id = item_names_to_id()
    location_name_to_id = location_names_to_id()

    item_name_groups = item_groups()
    location_name_groups = location_groups()

    required_client_version: Tuple[int, int, int] = (0, 6, 7)

    web = TwentyMinutesWebWorld()

    filler_item_names: List[str] = item_groups()["Filler Item"]

    # Options
    goal: TwentyMinutesGoalOptions
    forbidden_tomes_total: int
    forbidden_tomes_required: int
    character_selection: Dict[TwentyMinutesCharacters, bool]
    character_count: int
    weapon_selection: Dict[TwentyMinutesWeapons, bool]
    weapon_count: int
    starting_map: TwentyMinutesMapOptions
    starting_darkness: int
    maximum_survivable_darkness: int
    randomize_weapon_attributes: bool
    weapon_attribute_randomization_chance: int
    trap_percentage: int
    trap_weights: Dict[TwentyMinutesTrapTypes, int]
    death_link: bool

    # Generation
    selected_characters: List[TwentyMinutesCharacters]
    selected_starting_character: TwentyMinutesCharacters

    selected_weapons: List[TwentyMinutesWeapons]
    selected_starting_weapon: TwentyMinutesWeapons

    selected_starting_map: TwentyMinutesMaps
    selected_full_run_map: TwentyMinutesMaps

    weapon_data: Optional[Dict[TwentyMinutesWeapons, TwentyMinutesWeaponData]] = None

    # Universal Tracker
    location_id_to_alias: Dict[int, str]
    ut_can_gen_without_yaml: bool = True
    explicit_indirect_conditions = False
    glitches_item_name: str = "OOL"

    def generate_early(self) -> None:
        self.goal = id_to_goals()[self.options.goal.value]

        self.forbidden_tomes_total = self.options.forbidden_tomes_total.value
        self.forbidden_tomes_required = self.options.forbidden_tomes_required.value

        if self.forbidden_tomes_required > self.forbidden_tomes_total:
            self.forbidden_tomes_required = self.forbidden_tomes_total

            logging.warning(
                f"20 Minutes Till Dawn: {self.player_name} has more required Forbidden Tomes than total Forbidden Tomes. "
                "Adjusting required Forbidden Tomes to match total Forbidden Tomes..."
            )

        # Characters
        character_pool: List[TwentyMinutesCharacters] = list()

        character_name: str
        is_enabled: bool
        for character_name, is_enabled in self.options.character_selection.value.items():
            if is_enabled:
                character_pool.append(TwentyMinutesCharacters(character_name))

        character_pool = list(sorted(character_pool, key=lambda c: c.value))

        if not len(character_pool):
            raise OptionError(
                f"20 Minutes Till Dawn: {self.player_name} must have at least 1 Character selected to play. "
                "All of their Characters are set to False."
            )

        self.character_count = min(self.options.character_count.value, len(character_pool))

        characters: List[TwentyMinutesCharacters] = self.random.sample(character_pool, self.character_count)

        self.selected_characters = characters
        self.selected_starting_character = characters[0]

        # Weapons
        weapon_pool: List[TwentyMinutesWeapons] = list()

        weapon_name: str
        is_enabled: bool
        for weapon_name, is_enabled in self.options.weapon_selection.value.items():
            if is_enabled:
                weapon_pool.append(TwentyMinutesWeapons(weapon_name))

        weapon_pool = list(sorted(weapon_pool, key=lambda w: w.value))

        if len(weapon_pool) < 2:
            raise OptionError(
                f"20 Minutes Till Dawn: {self.player_name} must have at least 2 Weapons selected to play. "
                "Too few of their Weapons are set to True."
            )

        self.weapon_count = min(self.options.weapon_count.value, len(weapon_pool))

        weapons: List[TwentyMinutesWeapons] = self.random.sample(weapon_pool, self.weapon_count)

        self.selected_weapons = weapons
        self.selected_starting_weapon = weapons[0]

        # Maps
        starting_map_option: TwentyMinutesMapOptions = id_to_starting_maps()[self.options.starting_map.value]

        self.selected_starting_map = TwentyMinutesMaps[starting_map_option.name]
        self.selected_full_run_map = self.random.choice(list(TwentyMinutesMaps))

        # Darkness
        self.starting_darkness = self.options.starting_darkness.value
        self.maximum_survivable_darkness = self.options.maximum_survivable_darkness.value

        # Weapon Randomization
        self.randomize_weapon_attributes = bool(self.options.randomize_weapon_attributes.value)
        self.weapon_attribute_randomization_chance = self.options.weapon_attribute_randomization_chance.value

        self.weapon_data = None

        if self.randomize_weapon_attributes:
            self.weapon_data = dict()

            attribute_ranges: Dict[str, Tuple[float, float]] = self._get_weapon_data_attribute_ranges()

            weapon: TwentyMinutesWeapons
            for weapon in self.selected_weapons:
                baseline: TwentyMinutesWeaponData = weapon_to_vanilla_weapon_data[weapon]
                rolled_values: Dict[str, Any] = dict()

                field_name: str
                for field_name in TwentyMinutesWeaponData._fields:
                    baseline_value: Any = getattr(baseline, field_name)

                    if field_name == "piercing" and baseline_value == 999:
                        rolled_values[field_name] = baseline_value
                        continue

                    if field_name == "spread" and baseline_value < 0:
                        rolled_values[field_name] = baseline_value
                        continue

                    if self.random.randint(1, 100) <= self.weapon_attribute_randomization_chance:
                        low, high = attribute_ranges[field_name]
                        stdev: float = (high - low) / 6.0
                        rolled_value: float = self.random.gauss(baseline_value, stdev)
                        rolled_value = max(low, min(high, rolled_value))

                        if isinstance(baseline_value, int):
                            rolled_values[field_name] = round(rolled_value)
                        else:
                            rolled_values[field_name] = round(rolled_value, 2)
                    else:
                        rolled_values[field_name] = baseline_value

                self.weapon_data[weapon] = TwentyMinutesWeaponData(**rolled_values)

        # Traps
        self.trap_percentage = self.options.trap_percentage.value

        self.trap_weights = {trap_type: 1 for trap_type in TwentyMinutesTrapTypes}

        trap_type_name: str
        weight: Any
        for trap_type_name, weight in self.options.trap_weights.value.items():
            try:
                trap_type: TwentyMinutesTrapTypes = TwentyMinutesTrapTypes(trap_type_name)
            except Exception:
                continue

            if isinstance(weight, int) and weight >= 0:
                self.trap_weights[trap_type] = weight

        # DeathLink
        self.death_link = bool(self.options.death_link.value)

        # Universal Tracker Support
        if self.is_universal_tracker:
            self.location_id_to_alias = dict()
            self._apply_universal_tracker_passthrough()

    @property
    def is_universal_tracker(self) -> bool:
        return hasattr(self.multiworld, "re_gen_passthrough")

    def create_regions(self) -> None:
        # Menu
        region_menu: Region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(region_menu)

        # Endgame
        region_endgame: Region = Region("Endgame", self.player, self.multiworld)
        self.multiworld.regions.append(region_endgame)

        if self.goal == TwentyMinutesGoalOptions.FORBIDDEN_TOME_HUNT:
            region_menu.connect(region_endgame, rule=Has("Forbidden Tome", self.forbidden_tomes_required))

        # Maps
        map_: TwentyMinutesMaps
        for map_ in TwentyMinutesMaps:
            included_segment_count: int = 5 if map_ == self.selected_full_run_map else 3

            region_map: Region = Region(map_.value, self.player, self.multiworld)
            region_menu.connect(region_map, rule=Has(f"Map Unlock: {map_.value}"))

            # Kill Count
            kill_count_location_names: List[str] = locations_with_tags([
                TwentyMinutesTags.KILL_COUNT_LOCATION,
                getattr(TwentyMinutesTags, f"{map_.name}_LOCATION"),
            ])

            location_name: str
            for location_name in kill_count_location_names:
                data: TwentyMinutesLocationData = location_data[location_name]

                segment_index: int = 0

                candidate_segment_index: int
                for candidate_segment_index in range(1, 6):
                    if getattr(TwentyMinutesTags, f"MAP_SEGMENT_{candidate_segment_index}_LOCATION") in data.tags:
                        segment_index = candidate_segment_index
                        break

                if segment_index > included_segment_count:
                    continue

                location: TwentyMinutesLocation = TwentyMinutesLocation(
                    self.player,
                    location_name,
                    data.archipelago_id,
                    region_map,
                )

                if segment_index >= 2:
                    self.set_rule(
                        location,
                        Or(
                            Has(f"Progressive Timer: {map_.value}", segment_index - 1),
                            And(Has("OOL"), Has(f"Progressive Timer: {map_.value}", segment_index - 2)),
                        ),
                    )

                region_map.locations.append(location)

            # Character
            character: TwentyMinutesCharacters
            for character in self.selected_characters:
                region_map_character: Region = Region(f"{map_.value} - {character.value}", self.player, self.multiworld)
                region_map.connect(region_map_character, rule=Has(f"Character Unlock: {character.value}"))

                # Survival Time
                survival_time_location_names: List[str] = locations_with_tags([
                    TwentyMinutesTags.SURVIVAL_TIME_LOCATION,
                    getattr(TwentyMinutesTags, f"{map_.name}_LOCATION"),
                    getattr(TwentyMinutesTags, f"{character.name}_LOCATION"),
                ])

                survival_time_location_name: str
                for survival_time_location_name in survival_time_location_names:
                    survival_time_data: TwentyMinutesLocationData = location_data[survival_time_location_name]

                    survival_time_segment_index: int = 0

                    survival_time_candidate_segment_index: int
                    for survival_time_candidate_segment_index in range(1, 6):
                        if getattr(TwentyMinutesTags, f"MAP_SEGMENT_{survival_time_candidate_segment_index}_LOCATION") in survival_time_data.tags:
                            survival_time_segment_index = survival_time_candidate_segment_index
                            break

                    if survival_time_location_name.endswith("Survive the Run"):
                        if included_segment_count != 3:
                            continue
                    elif survival_time_location_name.endswith("Survive 11 Minutes"):
                        if included_segment_count != 5:
                            continue
                    elif survival_time_segment_index > included_segment_count:
                        continue

                    survival_time_location: TwentyMinutesLocation = TwentyMinutesLocation(
                        self.player,
                        survival_time_location_name,
                        survival_time_data.archipelago_id,
                        region_map_character,
                    )

                    if survival_time_segment_index >= 2:
                        self.set_rule(survival_time_location, Has(f"Progressive Timer: {map_.value}", survival_time_segment_index - 1))

                    region_map_character.locations.append(survival_time_location)

                # Level Up
                level_up_location_names: List[str] = locations_with_tags([
                    TwentyMinutesTags.LEVEL_UP_LOCATION,
                    getattr(TwentyMinutesTags, f"{map_.name}_LOCATION"),
                    getattr(TwentyMinutesTags, f"{character.name}_LOCATION"),
                ])

                level_up_location_name: str
                for level_up_location_name in level_up_location_names:
                    level_up_data: TwentyMinutesLocationData = location_data[level_up_location_name]

                    level_up_segment_index: int = 0

                    level_up_candidate_segment_index: int
                    for level_up_candidate_segment_index in range(1, 6):
                        if getattr(TwentyMinutesTags, f"MAP_SEGMENT_{level_up_candidate_segment_index}_LOCATION") in level_up_data.tags:
                            level_up_segment_index = level_up_candidate_segment_index
                            break

                    if level_up_segment_index > included_segment_count:
                        continue

                    level_up_location: TwentyMinutesLocation = TwentyMinutesLocation(
                        self.player,
                        level_up_location_name,
                        level_up_data.archipelago_id,
                        region_map_character,
                    )

                    if level_up_segment_index >= 2:
                        self.set_rule(
                            level_up_location,
                            Or(
                                Has(f"Progressive Timer: {map_.value}", level_up_segment_index - 1),
                                And(Has("OOL"), Has(f"Progressive Timer: {map_.value}", level_up_segment_index - 2)),
                            ),
                        )

                    region_map_character.locations.append(level_up_location)

                self.multiworld.regions.append(region_map_character)

            # Weapon
            weapon: TwentyMinutesWeapons
            for weapon in self.selected_weapons:
                region_map_weapon: Region = Region(f"{map_.value} - {weapon.value}", self.player, self.multiworld)
                region_map.connect(region_map_weapon, rule=Has(f"Weapon Unlock: {weapon.value}"))

                # Survival Time
                weapon_survival_time_location_names: List[str] = locations_with_tags([
                    TwentyMinutesTags.SURVIVAL_TIME_LOCATION,
                    getattr(TwentyMinutesTags, f"{map_.name}_LOCATION"),
                    getattr(TwentyMinutesTags, f"{weapon.name}_LOCATION"),
                ])

                weapon_survival_time_location_name: str
                for weapon_survival_time_location_name in weapon_survival_time_location_names:
                    weapon_survival_time_data: TwentyMinutesLocationData = location_data[weapon_survival_time_location_name]

                    weapon_survival_time_segment_index: int = 0

                    weapon_survival_time_candidate_segment_index: int
                    for weapon_survival_time_candidate_segment_index in range(1, 6):
                        if getattr(TwentyMinutesTags, f"MAP_SEGMENT_{weapon_survival_time_candidate_segment_index}_LOCATION") in weapon_survival_time_data.tags:
                            weapon_survival_time_segment_index = weapon_survival_time_candidate_segment_index
                            break

                    if weapon_survival_time_location_name.endswith("Survive the Run"):
                        if included_segment_count != 3:
                            continue
                    elif weapon_survival_time_location_name.endswith("Survive 11 Minutes"):
                        if included_segment_count != 5:
                            continue
                    elif weapon_survival_time_segment_index > included_segment_count:
                        continue

                    weapon_survival_time_location: TwentyMinutesLocation = TwentyMinutesLocation(
                        self.player,
                        weapon_survival_time_location_name,
                        weapon_survival_time_data.archipelago_id,
                        region_map_weapon,
                    )

                    if weapon_survival_time_segment_index >= 2:
                        self.set_rule(weapon_survival_time_location, Has(f"Progressive Timer: {map_.value}", weapon_survival_time_segment_index - 1))

                    region_map_weapon.locations.append(weapon_survival_time_location)

                # Level Up
                weapon_level_up_location_names: List[str] = locations_with_tags([
                    TwentyMinutesTags.LEVEL_UP_LOCATION,
                    getattr(TwentyMinutesTags, f"{map_.name}_LOCATION"),
                    getattr(TwentyMinutesTags, f"{weapon.name}_LOCATION"),
                ])

                weapon_level_up_location_name: str
                for weapon_level_up_location_name in weapon_level_up_location_names:
                    weapon_level_up_data: TwentyMinutesLocationData = location_data[weapon_level_up_location_name]

                    weapon_level_up_segment_index: int = 0

                    weapon_level_up_candidate_segment_index: int
                    for weapon_level_up_candidate_segment_index in range(1, 6):
                        if getattr(TwentyMinutesTags, f"MAP_SEGMENT_{weapon_level_up_candidate_segment_index}_LOCATION") in weapon_level_up_data.tags:
                            weapon_level_up_segment_index = weapon_level_up_candidate_segment_index
                            break

                    if weapon_level_up_segment_index > included_segment_count:
                        continue

                    weapon_level_up_location: TwentyMinutesLocation = TwentyMinutesLocation(
                        self.player,
                        weapon_level_up_location_name,
                        weapon_level_up_data.archipelago_id,
                        region_map_weapon,
                    )

                    if weapon_level_up_segment_index >= 2:
                        self.set_rule(
                            weapon_level_up_location,
                            Or(
                                Has(f"Progressive Timer: {map_.value}", weapon_level_up_segment_index - 1),
                                And(Has("OOL"), Has(f"Progressive Timer: {map_.value}", weapon_level_up_segment_index - 2)),
                            ),
                        )

                    region_map_weapon.locations.append(weapon_level_up_location)

                self.multiworld.regions.append(region_map_weapon)

            if map_ == self.selected_full_run_map and self.goal == TwentyMinutesGoalOptions.FORBIDDEN_TOMES_FINAL_MAP:
                required_darkness_reductions: int = max(0, self.starting_darkness - self.maximum_survivable_darkness)

                region_map.connect(
                    region_endgame,
                    rule=And(
                        Has(f"Progressive Timer: {map_.value}", 4),
                        Has("Forbidden Tome", self.forbidden_tomes_required),
                        Or(
                            Has("Progressive Darkness Reduction", required_darkness_reductions),
                            Has("OOL"),
                        ),
                    ),
                )

            self.multiworld.regions.append(region_map)

    def create_items(self) -> None:
        ## Precollect
        items_to_precollect: List[str] = list()

        # Starting Character
        items_to_precollect.append(f"Character Unlock: {self.selected_starting_character.value}")

        # Starting Weapon
        items_to_precollect.append(f"Weapon Unlock: {self.selected_starting_weapon.value}")

        # Starting Map
        items_to_precollect.append(f"Map Unlock: {self.selected_starting_map.value}")

        ## Item Pool
        item_pool: List[TwentyMinutesItem] = list()

        # Forbidden Tomes
        i: int
        for i in range(self.forbidden_tomes_total):
            item_pool.append(self.create_item("Forbidden Tome"))

        # Characters
        character: TwentyMinutesCharacters
        for character in self.selected_characters:
            # Unlock
            character_unlock_name: str = f"Character Unlock: {character.value}"

            if character_unlock_name not in items_to_precollect:
                item_pool.append(self.create_item(character_unlock_name))

            # Heart Container
            i: int
            for i in range(5):
                item_pool.append(self.create_item(f"Heart Container: {character.value}"))

            # Soul Heart Capacity
            i: int
            for i in range(3):
                item_pool.append(self.create_item(f"Soul Heart Capacity: {character.value}"))

            # Progressive Powerup Choices
            i: int
            for i in range(4):
                item_pool.append(self.create_item(f"Progressive Powerup Choices: {character.value}"))

        # Weapons
        weapon: TwentyMinutesWeapons
        for weapon in self.selected_weapons:
            weapon_unlock_name: str = f"Weapon Unlock: {weapon.value}"

            if weapon_unlock_name not in items_to_precollect:
                item_pool.append(self.create_item(weapon_unlock_name))

        # Maps
        map_: TwentyMinutesMaps
        for map_ in TwentyMinutesMaps:
            # Unlock
            map_unlock_name: str = f"Map Unlock: {map_.value}"

            if map_unlock_name not in items_to_precollect:
                item_pool.append(self.create_item(map_unlock_name))

            # Progressive Timer
            progressive_timer_count: int = 4 if map_ == self.selected_full_run_map else 2

            i: int
            for i in range(progressive_timer_count):
                item_pool.append(self.create_item(f"Progressive Timer: {map_.value}"))

        # Progressive Darkness Reduction
        darkness_reduction_classification: ItemClassification = (
            ItemClassification.progression
            if self.goal == TwentyMinutesGoalOptions.FORBIDDEN_TOMES_FINAL_MAP
            else ItemClassification.useful
        )

        i: int
        for i in range(self.starting_darkness):
            darkness_reduction_item: TwentyMinutesItem = self.create_item("Progressive Darkness Reduction")
            darkness_reduction_item.classification = darkness_reduction_classification

            item_pool.append(darkness_reduction_item)

        # Runes
        rune: TwentyMinutesRunes
        for rune in TwentyMinutesRunes:
            item_pool.append(self.create_item(f"3 Rune Points: {rune.value}"))

            i: int
            for i in range(2):
                item_pool.append(self.create_item(f"1 Rune Point: {rune.value}"))

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

    def create_item(self, name: str) -> TwentyMinutesItem:
        data: TwentyMinutesItemData = item_data[name]

        return TwentyMinutesItem(
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
            "forbidden_tomes_total",
            "forbidden_tomes_required",
            "character_selection",
            "character_count",
            "weapon_selection",
            "weapon_count",
            "starting_map",
            "starting_darkness",
            "maximum_survivable_darkness",
            "randomize_weapon_attributes",
            "weapon_attribute_randomization_chance",
            "trap_percentage",
            "trap_weights",
            "death_link",
        )

        slot_data["trap_weights"] = {
            trap_type.value: weight for trap_type, weight in self.trap_weights.items()
        }

        slot_data["selected_characters"] = [character.value for character in self.selected_characters]
        slot_data["selected_starting_character"] = self.selected_starting_character.value

        slot_data["selected_weapons"] = [weapon.value for weapon in self.selected_weapons]
        slot_data["selected_starting_weapon"] = self.selected_starting_weapon.value

        slot_data["selected_starting_map"] = self.selected_starting_map.value
        slot_data["selected_full_run_map"] = self.selected_full_run_map.value

        slot_data["weapon_data"] = None

        if self.weapon_data is not None:
            slot_data["weapon_data"] = {
                weapon.value: dict(data._asdict()) for weapon, data in self.weapon_data.items()
            }

        # Relay generate_early Overrides
        if slot_data["forbidden_tomes_required"] != self.forbidden_tomes_required:
            slot_data["forbidden_tomes_required"] = self.forbidden_tomes_required

        if slot_data["character_count"] != self.character_count:
            slot_data["character_count"] = self.character_count

        if slot_data["weapon_count"] != self.weapon_count:
            slot_data["weapon_count"] = self.weapon_count

        return slot_data

    def write_spoiler_header(self, spoiler_handle: TextIO) -> None:
        join_string: str = "\n  "
        nested_join_string: str = "\n    "

        # Characters
        if len(self.selected_characters) == 1:
            spoiler_handle.write(f"\nSelected Character: {self.selected_starting_character.value}")
        else:
            spoiler_handle.write(f"\nStarting Character: {self.selected_starting_character.value}")

            spoiler_handle.write(
                f"\n\nUnlockable Characters:\n  {join_string.join(sorted([c.value for c in self.selected_characters[1:]]))}"
            )

        # Weapons
        if len(self.selected_weapons) == 1:
            spoiler_handle.write(f"\n\nSelected Weapon: {self.selected_starting_weapon.value}")
        else:
            spoiler_handle.write(f"\n\nStarting Weapon: {self.selected_starting_weapon.value}")

            spoiler_handle.write(
                f"\n\nUnlockable Weapons:\n  {join_string.join(sorted([w.value for w in self.selected_weapons[1:]]))}"
            )

        # Maps
        spoiler_handle.write(f"\n\nStarting Map: {self.selected_starting_map.value}")
        spoiler_handle.write(f"\nFull Run Map: {self.selected_full_run_map.value}")

        # Randomized Weapon Data
        if self.weapon_data is not None:
            spoiler_handle.write("\n\nRandomized Weapon Attributes:")

            weapon: TwentyMinutesWeapons
            data: TwentyMinutesWeaponData
            for weapon, data in self.weapon_data.items():
                spoiler_handle.write(join_string + weapon.value + ":")

                vanilla_data: TwentyMinutesWeaponData = weapon_to_vanilla_weapon_data[weapon]

                field_name: str
                for field_name in TwentyMinutesWeaponData._fields:
                    humanized_field_name: str = field_name.replace("_", " ").title()

                    value: Any = getattr(data, field_name)
                    vanilla_value: Any = getattr(vanilla_data, field_name)

                    delta: float = value - vanilla_value
                    delta_sign: str = "+" if delta >= 0 else ""

                    spoiler_handle.write(nested_join_string + f"{humanized_field_name}: {value} ({delta_sign}{delta:.2f})")

    def get_filler_item_name(self) -> str:
        return self.random.choice(self.filler_item_names)

    @staticmethod
    def interpret_slot_data(slot_data: Dict[str, Any]) -> Dict[str, Any]:
        return process_slot_data(slot_data)

    def _apply_universal_tracker_passthrough(self) -> None:
        if "20 Minutes Till Dawn" in self.multiworld.re_gen_passthrough:
            passthrough: Dict[str, Any] = self.multiworld.re_gen_passthrough["20 Minutes Till Dawn"]

            self.goal = passthrough["goal"]
            self.forbidden_tomes_total = passthrough["forbidden_tomes_total"]
            self.forbidden_tomes_required = passthrough["forbidden_tomes_required"]
            self.character_selection = passthrough["character_selection"]
            self.character_count = passthrough["character_count"]
            self.weapon_selection = passthrough["weapon_selection"]
            self.weapon_count = passthrough["weapon_count"]
            self.starting_map = passthrough["starting_map"]
            self.starting_darkness = passthrough["starting_darkness"]
            self.maximum_survivable_darkness = passthrough["maximum_survivable_darkness"]
            self.randomize_weapon_attributes = passthrough["randomize_weapon_attributes"]
            self.weapon_attribute_randomization_chance = passthrough["weapon_attribute_randomization_chance"]
            self.trap_percentage = passthrough["trap_percentage"]
            self.trap_weights = passthrough["trap_weights"]
            self.death_link = passthrough["death_link"]

            self.selected_characters = passthrough["selected_characters"]
            self.selected_starting_character = passthrough["selected_starting_character"]

            self.selected_weapons = passthrough["selected_weapons"]
            self.selected_starting_weapon = passthrough["selected_starting_weapon"]

            self.selected_starting_map = passthrough["selected_starting_map"]
            self.selected_full_run_map = passthrough["selected_full_run_map"]

            self.weapon_data = passthrough["weapon_data"]

    @staticmethod
    def _get_weapon_data_attribute_ranges() -> Dict[str, Tuple[float, float]]:
        ranges: Dict[str, Tuple[float, float]] = dict()

        field_name: str
        for field_name in TwentyMinutesWeaponData._fields:
            field_values = [getattr(weapon_data, field_name) for weapon_data in weapon_to_vanilla_weapon_data.values()]

            if field_name == "piercing":
                field_values = [value for value in field_values if value != 999]

            if field_name == "spread":
                field_values = [value for value in field_values if value >= 0]

            ranges[field_name] = (min(field_values), max(field_values))

        return ranges

    def _generate_filler_trap_item_pool(self, count: int) -> List[str]:
        trap_items_needed: int = round(self.trap_percentage / 100 * count)
        filler_items_needed: int = count - trap_items_needed

        item_pool: List[str] = list()

        if trap_items_needed > 0:
            trap_items: List[TwentyMinutesTrapTypes] = list(self.trap_weights.keys())
            trap_item_weights: List[int] = list(self.trap_weights.values())

            if sum(trap_item_weights) == 0:
                trap_item_weights = [1 for _ in trap_item_weights]

            item_pool.extend([
                trap_type.value for trap_type in self.random.choices(trap_items, trap_item_weights, k=trap_items_needed)
            ])

        for _ in range(filler_items_needed):
            item_pool.append(self.random.choice(self.filler_item_names))

        return item_pool

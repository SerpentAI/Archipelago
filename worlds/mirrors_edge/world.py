import logging

from typing import Any, Dict, List, Optional, TextIO, Tuple

from rule_builder.rules import And, Has, Or

from BaseClasses import Item, ItemClassification, Location, Region, Tutorial

from worlds.AutoWorld import WebWorld, World

from .data.game_data import (
    level_base_target_times,
    level_to_checkpoints,
    levels_with_multiple_zero_requirements,
    levels_with_one_zero_requirements,
    levels_with_requirements,
)

from .data.item_data import MirrorsEdgeItemData, item_data
from .data.location_data import location_data
from .data.rule_data import level_checkpoint_rules

from .data_funcs import (
    id_to_goals,
    id_to_logic,
    item_names_to_id,
    item_groups,
    location_groups,
    location_names_to_id,
    process_slot_data,
)

from .enums import (
    MirrorsEdgeAPGoals,
    MirrorsEdgeAPLogic,
    MirrorsEdgeAPTrapTypes,
    MirrorsEdgeAbilities,
    MirrorsEdgeLevels,
    MirrorsEdgeLevelCheckpoints,
)

from .options import MirrorsEdgeOptions, option_groups


class MirrorsEdgeItem(Item):
    game = "Mirror's Edge"


class MirrorsEdgeLocation(Location):
    game = "Mirror's Edge"


class MirrorsEdgeWebWorld(WebWorld):
    theme: str = "ocean"

    tutorials: List[Tutorial] = [
        Tutorial(
            "Multiworld Setup Guide",
            "A guide to setting up the Mirror's Edge randomizer connected to an Archipelago Multiworld",
            "English",
            "setup_en.md",
            "setup/en",
            ["Serpent.AI"],
        )
    ]

    option_groups = option_groups


class MirrorsEdgeWorld(World):
    """
    Mirror’s Edge focuses on first-person movement and momentum-based parkour.
    By emphasizing technical maneuvers such as wall-runs, slides, and vaulted jumps,
    the game challenges players to navigate a sterile urban environment with efficiency.
    Players are challenged to optimize their routes and maintain top speed through a series
    of demanding, physics-based obstacle courses.
    """

    options_dataclass = MirrorsEdgeOptions
    options: MirrorsEdgeOptions

    game = "Mirror's Edge"

    item_name_to_id = item_names_to_id()
    location_name_to_id = location_names_to_id()

    item_name_groups = item_groups()
    location_name_groups = location_groups()

    required_client_version: Tuple[int, int, int] = (0, 6, 7)

    web = MirrorsEdgeWebWorld()

    filler_item_names: List[str] = item_groups()["Filler Item"]

    # Options
    goal: MirrorsEdgeAPGoals
    runner_bags_total: int
    runner_bags_required: int
    logic: MirrorsEdgeAPLogic
    open_world: bool
    starting_ability_count: int
    include_2_star_ratings: bool
    include_3_star_ratings: bool
    target_time_adjustment_percentage: int
    useful_item_percentage: int
    trap_percentage: int
    trap_weights: Dict[MirrorsEdgeAPTrapTypes, int]
    fov_adjustment: int

    # Generation
    starting_levels: List[MirrorsEdgeLevels]
    levels: List[MirrorsEdgeLevels]
    goal_level: Optional[MirrorsEdgeLevels] = None

    starting_abilities: List[MirrorsEdgeAbilities]
    abilities: List[MirrorsEdgeAbilities]

    target_times: Dict[MirrorsEdgeLevels, List[int]]

    # Universal Tracker
    location_id_to_alias: Dict[int, str]
    ut_can_gen_without_yaml: bool = True

    @property
    def is_universal_tracker(self) -> bool:
        return hasattr(self.multiworld, "re_gen_passthrough")

    def generate_early(self) -> None:
        self.goal = id_to_goals()[self.options.goal.value]

        self.runner_bags_required = self.options.runner_bags_required.value
        self.runner_bags_total = self.options.runner_bags_total.value

        if self.runner_bags_required > self.runner_bags_total:
            self.runner_bags_required = self.runner_bags_total

            logging.warning(
                f"Mirror's Edge: {self.player_name} has more required runner bags than total runner bags. "
                "Adjusting required runner bags to match total runner bags..."
            )

        self.logic = id_to_logic()[self.options.logic.value]

        # Levels
        self.open_world = bool(self.options.open_world.value)

        level_pool: List[MirrorsEdgeLevels] = list()

        if self.open_world:
            level_pool: List[MirrorsEdgeLevels] = [level for level in MirrorsEdgeLevels]
            self.random.shuffle(level_pool)

            self.starting_levels = level_pool[:]
        else:
            self.starting_levels = list()
            remainder: List[MirrorsEdgeLevels] = list()

            with_multiple_zero_requirements: List[MirrorsEdgeLevels] = list(
                levels_with_multiple_zero_requirements[:]
            )

            self.random.shuffle(with_multiple_zero_requirements)

            level_pool.append(with_multiple_zero_requirements[0])
            self.starting_levels.append(with_multiple_zero_requirements[0])

            remainder.extend(with_multiple_zero_requirements[1:])

            with_one_zero_requirements: List[MirrorsEdgeLevels] = list(
                levels_with_one_zero_requirements[:]
            )

            self.random.shuffle(with_one_zero_requirements)

            level_pool.extend(with_one_zero_requirements[:3])
            self.starting_levels.extend(with_one_zero_requirements[:3])

            remainder.extend(with_one_zero_requirements[3:])

            with_requirements: List[MirrorsEdgeLevels] = list(
                levels_with_requirements[:]
            )

            self.random.shuffle(with_requirements)

            level_pool.append(with_requirements[0])
            self.starting_levels.append(with_requirements[0])

            remainder.extend(with_requirements[1:])

            self.random.shuffle(remainder)

            level_pool.extend(remainder)

        if self.goal == MirrorsEdgeAPGoals.RUNNER_BAGS_FINAL_LEVEL:
            self.goal_level = level_pool[-1]
            self.levels = level_pool[:-1]
        else:
            self.levels = level_pool[:]

        # Abilities
        self.abilities = [ability for ability in MirrorsEdgeAbilities]
        self.random.shuffle(self.abilities)

        self.starting_ability_count = self.options.starting_ability_count.value
        self.starting_abilities = self.abilities[:self.starting_ability_count]

        # Target Times
        self.include_2_star_ratings = bool(self.options.include_2_star_ratings.value)
        self.include_3_star_ratings = bool(self.options.include_3_star_ratings.value)

        self.target_time_adjustment_percentage = self.options.target_time_adjustment_percentage.value

        self.target_times = dict()

        level: MirrorsEdgeLevels
        for level in self.levels:
            if level == self.goal_level:
                continue

            self.target_times[level] = [
                round(int(base_time * (self.target_time_adjustment_percentage / 100.0)))
                for base_time in level_base_target_times[level]
            ]

            if not self.include_2_star_ratings:
                self.target_times[level][1] = 0

            if not self.include_3_star_ratings:
                self.target_times[level][2] = 0

        # Traps
        self.trap_percentage = self.options.trap_percentage.value

        self.trap_weights = {
            trap_type: 1 for trap_type in MirrorsEdgeAPTrapTypes
        }

        trap_type_name: str
        weight: Any
        for trap_type_name, weight in self.options.trap_weights.value.items():
            try:
                trap_type: MirrorsEdgeAPTrapTypes = MirrorsEdgeAPTrapTypes(trap_type_name)
            except Exception:
                continue

            if isinstance(weight, int) and weight >= 0:
                self.trap_weights[trap_type] = weight

        ###

        self.useful_item_percentage = self.options.useful_item_percentage.value
        self.fov_adjustment = self.options.fov_adjustment.value

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

        victory_location: MirrorsEdgeLocation = MirrorsEdgeLocation(
            self.player,
            "Victory",
            None,
            region_endgame,
        )

        victory_location.place_locked_item(
            MirrorsEdgeItem(
                "Victory",
                ItemClassification.progression,
                None,
                self.player,
            )
        )

        region_endgame.locations.append(victory_location)

        if self.goal == MirrorsEdgeAPGoals.RUNNER_BAG_HUNT:
            region_menu.connect(region_endgame, rule=Has("Runner Bag", self.runner_bags_required))

            self.multiworld.regions.append(region_endgame)

        # Levels
        level: MirrorsEdgeLevels
        for level in (self.levels + [self.goal_level]):
            if level is None:
                continue

            region_level: Region = Region(level.value, self.player, self.multiworld)
            previous_region: Region = region_level

            level_checkpoints: Tuple[MirrorsEdgeLevels, ...] = level_to_checkpoints[level]
            last_checkpoint: MirrorsEdgeLevels = level_checkpoints[-1]

            checkpoint: MirrorsEdgeLevelCheckpoints
            for checkpoint in level_to_checkpoints[level]:
                region_checkpoint: Region = Region(checkpoint.value, self.player, self.multiworld)

                # Location
                if level != self.goal_level:
                    checkpoint_location: MirrorsEdgeLocation = MirrorsEdgeLocation(
                        self.player,
                        checkpoint.value,
                        location_data[checkpoint.value].archipelago_id,
                        region_checkpoint,
                    )

                    region_checkpoint.locations.append(checkpoint_location)

                if checkpoint == last_checkpoint:
                    if level != self.goal_level:
                        region_1_star: Region = Region(
                            f"{level.value} - 1 Star Rating",
                            self.player,
                            self.multiworld,
                        )

                        location_1_star: MirrorsEdgeLocation = MirrorsEdgeLocation(
                            self.player,
                            f"{level.value} - 1 Star Rating",
                            location_data[f"{level.value} - 1 Star Rating"].archipelago_id,
                            region_1_star,
                        )

                        region_1_star.locations.append(location_1_star)

                        region_checkpoint.connect(region_1_star, rule=Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINT.value}"))
                        self.multiworld.regions.append(region_1_star)

                        if self.include_2_star_ratings:
                            region_2_star: Region = Region(
                                f"{level.value} - 2 Star Rating",
                                self.player,
                                self.multiworld,
                            )

                            location_2_star: MirrorsEdgeLocation = MirrorsEdgeLocation(
                                self.player,
                                f"{level.value} - 2 Star Rating",
                                location_data[f"{level.value} - 2 Star Rating"].archipelago_id,
                                region_2_star,
                            )

                            region_2_star.locations.append(location_2_star)

                            region_checkpoint.connect(
                                region_2_star,
                                rule=And(
                                    Has(f"Ability Unlock: {MirrorsEdgeAbilities.BALANCE.value}"),
                                    Or(
                                        Has(f"Ability Unlock: {MirrorsEdgeAbilities.BARGE.value}"),
                                        Has(f"Ability Unlock: {MirrorsEdgeAbilities.MELEE_ATTACK.value}"),
                                    ),
                                    Has(f"Ability Unlock: {MirrorsEdgeAbilities.CLIMB.value}"),
                                    Has(f"Ability Unlock: {MirrorsEdgeAbilities.COIL.value}"),
                                    Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
                                    Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.GRAB_JUMP.value}"),
                                    Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINGBOARD.value}"),
                                    Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINT.value}"),
                                    Has(f"Ability Unlock: {MirrorsEdgeAbilities.SWING.value}"),
                                    Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
                                    Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_CLIMB.value}"),
                                    Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_CLIMB_ONE_EIGHTY_TURN_JUMP.value}"),
                                    Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_RUN.value}"),
                                    Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_RUN_JUMP.value}"),
                                    Has(f"Ability Unlock: {MirrorsEdgeAbilities.ZIPLINE.value}"),
                                )
                            )

                            self.multiworld.regions.append(region_2_star)

                        if self.include_3_star_ratings:
                            region_3_star: Region = Region(
                                f"{level.value} - 3 Star Rating",
                                self.player,
                                self.multiworld,
                            )

                            location_3_star: MirrorsEdgeLocation = MirrorsEdgeLocation(
                                self.player,
                                f"{level.value} - 3 Star Rating",
                                location_data[f"{level.value} - 3 Star Rating"].archipelago_id,
                                region_3_star,
                            )

                            region_3_star.locations.append(location_3_star)

                            region_checkpoint.connect(
                                region_3_star,
                                rule=And(
                                    Has(f"Ability Unlock: {MirrorsEdgeAbilities.BALANCE.value}"),
                                    Or(
                                        Has(f"Ability Unlock: {MirrorsEdgeAbilities.BARGE.value}"),
                                        Has(f"Ability Unlock: {MirrorsEdgeAbilities.MELEE_ATTACK.value}"),
                                    ),
                                    Has(f"Ability Unlock: {MirrorsEdgeAbilities.CLIMB.value}"),
                                    Has(f"Ability Unlock: {MirrorsEdgeAbilities.COIL.value}"),
                                    Has(f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"),
                                    Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.GRAB_JUMP.value}"),
                                    Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINGBOARD.value}"),
                                    Has(f"Ability Unlock: {MirrorsEdgeAbilities.SPRINT.value}"),
                                    Has(f"Ability Unlock: {MirrorsEdgeAbilities.SWING.value}"),
                                    Has(f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"),
                                    Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_CLIMB.value}"),
                                    Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_CLIMB_ONE_EIGHTY_TURN_JUMP.value}"),
                                    Has(f"Ability Unlock: {MirrorsEdgeAbilities.WALL_RUN.value}"),
                                    Has(f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_RUN_JUMP.value}"),
                                    Has(f"Ability Unlock: {MirrorsEdgeAbilities.ZIPLINE.value}"),
                                )
                            )

                            self.multiworld.regions.append(region_3_star)

                    if level == self.goal_level and self.goal == MirrorsEdgeAPGoals.RUNNER_BAGS_FINAL_LEVEL:
                        region_checkpoint.connect(region_endgame, rule=Has("Runner Bag", self.runner_bags_required))

                        self.multiworld.regions.append(region_endgame)

                previous_region.connect(region_checkpoint, rule=level_checkpoint_rules[checkpoint])
                self.multiworld.regions.append(region_checkpoint)

                previous_region = region_checkpoint

            region_menu.connect(region_level, rule=Has(f"Level Unlock: {level.value}"))
            self.multiworld.regions.append(region_level)

    def create_items(self) -> None:
        ## Precollect
        items_to_precollect: List[str] = list()

        # Starting Levels
        level: MirrorsEdgeLevels
        for level in self.starting_levels:
            items_to_precollect.append(f"Level Unlock: {level.value}")

        # Starting Abilities
        ability: MirrorsEdgeAbilities
        for ability in self.starting_abilities:
            if ability in [
                MirrorsEdgeAbilities.GRAB_JUMP, MirrorsEdgeAbilities.WALL_RUN_JUMP, MirrorsEdgeAbilities.WALL_CLIMB_ONE_EIGHTY_TURN_JUMP
            ]:
                items_to_precollect.append(f"Ability Extension Unlock: {ability.value}")
            else:
                items_to_precollect.append(f"Ability Unlock: {ability.value}")

        # Logic
        if self.logic == MirrorsEdgeAPLogic.ADVANCED:
            items_to_precollect.append("Advanced Logic")

        ## Item Pool
        item_pool: List[MirrorsEdgeItem] = list()

        # Runner Bags
        i: int
        for i in range(self.runner_bags_total):
            item: MirrorsEdgeItem = self.create_item("Runner Bag")

            # Upgrade from useful instead of the other way around to accommodate UT
            if i < self.runner_bags_required:
                item.classification = ItemClassification.progression_deprioritized_skip_balancing

            item_pool.append(item)

        # Levels
        level: MirrorsEdgeLevels
        for level in (self.levels + [self.goal_level]):
            if level is None:
                continue

            item_name: str = f"Level Unlock: {level.value}"

            if item_name in items_to_precollect:
                continue

            item_pool.append(self.create_item(item_name))

        # Abilities
        ability: MirrorsEdgeAbilities
        for ability in self.abilities:
            if ability in [
                MirrorsEdgeAbilities.GRAB_JUMP, MirrorsEdgeAbilities.WALL_RUN_JUMP, MirrorsEdgeAbilities.WALL_CLIMB_ONE_EIGHTY_TURN_JUMP
            ]:
                item_name: str = f"Ability Extension Unlock: {ability.value}"
            else:
                item_name: str = f"Ability Unlock: {ability.value}"

            if item_name in items_to_precollect:
                continue

            item_pool.append(self.create_item(item_name))

        # Useful / Filler / Traps
        total_location_count: int = len(self.multiworld.get_unfilled_locations(self.player))
        to_fill_location_count: int = total_location_count - len(item_pool)

        item_name: str
        for item_name in self._generate_useful_filler_trap_item_pool(to_fill_location_count):
            item_pool.append(self.create_item(item_name))

        self.multiworld.itempool += item_pool

        item: str
        for item in items_to_precollect:
            self.multiworld.push_precollected(self.create_item(item))

    def create_item(self, name: str) -> MirrorsEdgeItem:
        data: MirrorsEdgeItemData = item_data[name]

        return MirrorsEdgeItem(
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
            "runner_bags_total",
            "runner_bags_required",
            "logic",
            "open_world",
            "starting_ability_count",
            "include_2_star_ratings",
            "include_3_star_ratings",
            "target_time_adjustment_percentage",
            "useful_item_percentage",
            "trap_percentage",
            "trap_weights",
            "fov_adjustment",
        )

        slot_data["trap_weights"] = {
            trap_type.value: weight for trap_type, weight in self.trap_weights.items()
        }

        slot_data["starting_levels"] = [level.value for level in self.starting_levels]
        slot_data["levels"] = [level.value for level in self.levels]
        slot_data["goal_level"] = self.goal_level.value if self.goal_level is not None else None

        slot_data["starting_abilities"] = [ability.value for ability in self.starting_abilities]
        slot_data["abilities"] = [ability.value for ability in self.abilities]

        slot_data["target_times"] = dict()

        level: MirrorsEdgeLevels
        level_target_times: List[int]
        for level, level_target_times in self.target_times.items():
            slot_data["target_times"][level.value] = level_target_times

        # Relay generate_early Overrides
        if slot_data["runner_bags_required"] != self.runner_bags_required:
            slot_data["runner_bags_required"] = self.runner_bags_required

        return slot_data

    def write_spoiler_header(self, spoiler_handle: TextIO) -> None:
        join_string: str = "\n  "

        # Levels
        if not self.open_world:
            spoiler_handle.write(
                f"\n\nStarting Levels:\n  {join_string.join(sorted([l.value for l in self.starting_levels]))}"
            )

            spoiler_handle.write(
                f"\n\nUnlockable Levels:\n  {join_string.join(sorted([l.value for l in self.levels[5:]]))}"
            )

        if self.goal_level is not None:
            spoiler_handle.write(f"\n\nGoal Level: {self.goal_level.value}")

        # Abilities
        if len(self.starting_abilities):
            spoiler_handle.write(
                f"\n\nStarting Abilities:\n  {join_string.join(sorted([a.value for a in self.starting_abilities]))}"
            )

            spoiler_handle.write(
                f"\n\nUnlockable Abilities:\n  {join_string.join(sorted([a.value for a in self.abilities[self.starting_ability_count:]]))}"
            )

        # Target Times
        spoiler_handle.write("\n\nTarget Times:")

        level: MirrorsEdgeLevels
        level_target_times: List[int]
        for level, level_target_times in self.target_times.items():
            spoiler_handle.write(join_string + f"{level.value}: {level_target_times}")

    def get_filler_item_name(self) -> str:
        return self.random.choice(self.filler_item_names)

    @staticmethod
    def interpret_slot_data(slot_data: Dict[str, Any]) -> Dict[str, Any]:
        return process_slot_data(slot_data)

    def _apply_universal_tracker_passthrough(self) -> None:
        if "Mirror's Edge" in self.multiworld.re_gen_passthrough:
            passthrough: Dict[str, Any] = self.multiworld.re_gen_passthrough["Mirror's Edge"]

            self.goal = passthrough["goal"]
            self.runner_bags_total = passthrough["runner_bags_total"]
            self.runner_bags_required = passthrough["runner_bags_required"]
            self.logic = passthrough["logic"]
            self.open_world = passthrough["open_world"]
            self.starting_ability_count = passthrough["starting_ability_count"]
            self.include_2_star_ratings = passthrough["include_2_star_ratings"]
            self.include_3_star_ratings = passthrough["include_3_star_ratings"]
            self.target_time_adjustment_percentage = passthrough["target_time_adjustment_percentage"]
            self.useful_item_percentage = passthrough["useful_item_percentage"]
            self.trap_percentage = passthrough["trap_percentage"]
            self.trap_weights = passthrough["trap_weights"]
            self.fov_adjustment = passthrough["fov_adjustment"]

            self.starting_levels = passthrough["starting_levels"]
            self.levels = passthrough["levels"]
            self.goal_level = passthrough["goal_level"]

            self.starting_abilities = passthrough["starting_abilities"]
            self.abilities = passthrough["abilities"]

            self.target_times = passthrough["target_times"]

            # Location Aliases
            level: MirrorsEdgeLevels
            target_times: List[int]
            for level, target_times in self.target_times.items():
                i: int
                target_time: int
                for i, target_time in enumerate(target_times):
                    if target_time == 0:
                        continue

                    formatted_target_time: str = f"{target_time // 60:1d}:{target_time % 60:02d}"

                    self.location_id_to_alias[self.location_name_to_id[f"{level.value} - {i + 1} Star Rating"]] = formatted_target_time

    def _generate_useful_filler_trap_item_pool(self, count: int) -> List[str]:
        useful_items_needed: int = round(self.useful_item_percentage / 100 * count)

        _remaining_items: int = count - useful_items_needed

        trap_items_needed: int = round(self.trap_percentage / 100 * _remaining_items)
        filler_items_needed: int = _remaining_items - trap_items_needed

        item_pool: List[str] = list()

        if useful_items_needed > 0:
            useful_item_pool: List[str] = list()

            level: MirrorsEdgeLevels
            for level in self.levels:
                useful_item_pool.append(f"{level.value}: 1 Second Time Bonus")
                useful_item_pool.append(f"{level.value}: 3 Seconds Time Bonus")
                useful_item_pool.append(f"{level.value}: 5 Seconds Time Bonus")

            item_pool.extend([
                useful_item for useful_item in self.random.choices(useful_item_pool, k=useful_items_needed)
            ])

        if trap_items_needed > 0:
            trap_items: List[MirrorsEdgeAPTrapTypes] = list(self.trap_weights.keys())
            trap_item_weights: List[int] = list(self.trap_weights.values())

            if sum(trap_item_weights) == 0:
                trap_item_weights = [1 for _ in trap_item_weights]

            item_pool.extend([
                trap_type.value for trap_type in self.random.choices(trap_items, trap_item_weights, k=trap_items_needed)
            ])

        for _ in range(filler_items_needed):
            filler_item_name: str = self.random.choice(self.filler_item_names)

            if self.random.randint(1, 500) == 1:
                filler_item_name = "Classified " + filler_item_name

            item_pool.append(filler_item_name)

        return item_pool

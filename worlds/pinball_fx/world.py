import logging

from typing import Any, Dict, List, Optional, TextIO, Tuple

from BaseClasses import Item, ItemClassification, Location, Region, Tutorial

from Options import OptionError

from rule_builder.rules import And, Has

from worlds.AutoWorld import WebWorld, World

from .data.item_data import PinballFXItemData, item_data
from .data.location_data import PinballFXLocationData, location_data
from .data.game_data import base_target_scores, table_to_table_groups

from .data_funcs import (
    id_to_goals,
    id_to_requirement_modes,
    item_names_to_id,
    item_groups,
    location_groups,
    location_names_to_id,
    locations_with_tags,
    process_slot_data,
)

from .enums import (
    PinballFXAPGoals,
    PinballFXAPRequirementModes,
    PinballFXAPTags,
    PinballFXAPTrapTypes,
    PinballFXGameModes,
    PinballFXTables,
)

from .options import PinballFXOptions, option_groups


class PinballFXItem(Item):
    game = "Pinball FX"


class PinballFXLocation(Location):
    game = "Pinball FX"


class PinballFXWebWorld(WebWorld):
    theme: str = "partyTime"

    tutorials: List[Tutorial] = [
        Tutorial(
            "Multiworld Setup Guide",
            "A guide to setting up the Pinball FX randomizer connected to an Archipelago Multiworld",
            "English",
            "setup_en.md",
            "setup/en",
            ["Serpent.AI"],
        )
    ]

    option_groups = option_groups


class PinballFXWorld(World):
    """
    Pinball FX delivers fast, physics-driven pinball action with meticulously crafted tables inspired by iconic franchises and original designs. With competitive modes, online tournaments, and precise controls, it brings the classic arcade experience into the modern era with a deep, skill-based challenge.
    """

    options_dataclass = PinballFXOptions
    options: PinballFXOptions

    game = "Pinball FX"

    item_name_to_id = item_names_to_id()
    location_name_to_id = location_names_to_id()

    item_name_groups = item_groups()
    location_name_groups = location_groups()

    required_client_version: Tuple[int, int, int] = (0, 6, 7)

    web = PinballFXWebWorld()

    filler_item_names: List[str] = item_groups()["Filler Item"]

    # Options
    goal: PinballFXAPGoals
    shiny_quarters_total: int
    shiny_quarters_required: int
    pinball_table_selection: Dict[PinballFXTables, bool]
    pinball_table_count: int
    include_very_high_tier_scores: bool
    include_one_ball_challenges: bool
    include_flips_challenges: bool
    include_distance_challenges: bool
    target_score_requirement_mode: PinballFXAPRequirementModes
    target_score_requirement_percentage: int
    useful_item_percentage: int
    trap_percentage: int
    trap_weights: Dict[PinballFXAPTrapTypes, int]
    trap_duration: int

    # Generation
    selected_tables: List[PinballFXTables]
    selected_starter_table_modes: Dict[PinballFXTables, List[PinballFXGameModes]]
    selected_goal_table: Optional[PinballFXTables] = None

    target_scores: Dict[PinballFXTables, Dict[PinballFXGameModes, List[int]]]

    # Metadata
    target_score_ratios: Dict[PinballFXTables, float]

    # Universal Tracker
    location_id_to_alias: Dict[int, str]
    ut_can_gen_without_yaml: bool = True
    explicit_indirect_conditions = False

    @property
    def is_universal_tracker(self) -> bool:
        return hasattr(self.multiworld, "re_gen_passthrough")

    def generate_early(self) -> None:
        self.goal = id_to_goals()[self.options.goal.value]

        self.pinball_table_count = self.options.pinball_table_count.value

        self.shiny_quarters_required = self.options.shiny_quarters_required.value
        self.shiny_quarters_total = self.options.shiny_quarters_total.value

        if self.shiny_quarters_total > (self.pinball_table_count * 2):
            self.shiny_quarters_total = self.pinball_table_count * 2

            logging.warning(
                f"Pinball FX: {self.player_name} has more total shiny quarters than allowable with the selected "
                f"number of pinball tables. Adjusting total shiny quarters to {self.shiny_quarters_total}..."
            )

        if self.shiny_quarters_required > self.shiny_quarters_total:
            self.shiny_quarters_required = self.shiny_quarters_total

            logging.warning(
                f"Pinball FX: {self.player_name} has more required shiny quarters than total shiny quarters. "
                "Adjusting required shiny quarters to match total shiny quarters..."
            )

        pinball_table_pool: List[PinballFXTables] = list()

        table_name: str
        is_enabled: bool
        for table_name, is_enabled in self.options.pinball_table_selection.value.items():
            if is_enabled:
                if table_name.startswith("[Free"):
                    table_name = table_name.split("Tables] ")[1]
                else:
                    table_name = table_name.split("DLC] ")[1]

                pinball_table_pool.append(PinballFXTables(table_name))

        pinball_table_pool = list(sorted(pinball_table_pool, key=lambda t: t.value))

        if len(pinball_table_pool) < 6:
            raise OptionError(
                f"Pinball FX: {self.player_name} must have at least 6 pinball tables selected to play. "
                f"They only have {len(pinball_table_pool)} selected."
            )

        if self.pinball_table_count > len(pinball_table_pool):
            self.pinball_table_count = len(pinball_table_pool)

            logging.warning(
                f"Pinball FX: {self.player_name} has a pinball table count higher than their selected pinball "
                "table pool. Adjusting pinball table count to match the size of their pinball table pool..."
            )

        self.random.shuffle(pinball_table_pool)

        pinball_table_pool = pinball_table_pool[:self.pinball_table_count]

        if self.goal == PinballFXAPGoals.SHINY_QUARTERS_FINAL_TABLE:
            self.selected_goal_table = pinball_table_pool[-1]
            self.selected_tables = pinball_table_pool[:-1]
        else:
            self.selected_tables = pinball_table_pool[:]

        selected_starter_tables: List[PinballFXTables] = self.selected_tables[:3]

        self.selected_starter_table_modes = dict()

        game_mode_pool: List[PinballFXGameModes] = [
            PinballFXGameModes.CLASSIC,
            PinballFXGameModes.TIME,
        ]

        self.include_one_ball_challenges = bool(self.options.include_one_ball_challenges.value)
        self.include_flips_challenges = bool(self.options.include_flips_challenges.value)
        self.include_distance_challenges = bool(self.options.include_distance_challenges.value)

        if self.include_one_ball_challenges:
            game_mode_pool.append(PinballFXGameModes.ONE_BALL)

        if self.include_flips_challenges:
            game_mode_pool.append(PinballFXGameModes.FLIPS)

        if self.include_distance_challenges:
            game_mode_pool.append(PinballFXGameModes.DISTANCE)

        table: PinballFXTables
        for table in selected_starter_tables:
            self.selected_starter_table_modes[table] = self.random.sample(game_mode_pool, 2)

        self.include_very_high_tier_scores = bool(self.options.include_very_high_tier_scores.value)

        self.target_score_requirement_mode = id_to_requirement_modes()[
            self.options.target_score_requirement_mode.value
        ]

        self.target_score_requirement_percentage = self.options.target_score_requirement_percentage.value

        self.target_scores = dict()
        self.target_score_ratios = dict()

        table: PinballFXTables
        for table in (self.selected_tables + [self.selected_goal_table]):
            if table is None:
                continue

            base_scores: List[int] = base_target_scores[table]

            if self.target_score_requirement_mode == PinballFXAPRequirementModes.SAME_FOR_ALL_TABLES:
                self.target_score_ratios[table] = round(self.target_score_requirement_percentage / 100.0, 2)
            elif self.target_score_requirement_mode == PinballFXAPRequirementModes.RANDOM_PER_TABLE:
                random_percentage: int = self.random.randint(max(self.target_score_requirement_percentage - 100, 50), self.target_score_requirement_percentage)
                self.target_score_ratios[table] = round(random_percentage / 100.0, 2)

            self.target_scores[table] = dict()

            i: int
            game_mode: PinballFXGameModes
            for i, game_mode in enumerate(PinballFXGameModes):
                self.target_scores[table][game_mode] = None

                if game_mode == PinballFXGameModes.ONE_BALL and not self.include_one_ball_challenges:
                    continue
                elif game_mode == PinballFXGameModes.FLIPS and not self.include_flips_challenges:
                    continue
                elif game_mode == PinballFXGameModes.DISTANCE and not self.include_distance_challenges:
                    continue

                if i == 0:
                    # People tend to grind Classic Mode, so leaderboard scores are statistically anomalous
                    # We use slightly modified Time Challenge scores for balance
                    adjusted_scores: List[int] = [
                        round(int((base_scores[3] / 3.5) * 0.15 * self.target_score_ratios[table]), -3),
                        round(int((base_scores[3] / 3.5) * 0.325 * self.target_score_ratios[table]), -3),
                        round(int((base_scores[3] / 3.5) * 0.7 * self.target_score_ratios[table]), -3),
                        round(int((base_scores[3] / 3.5) * self.target_score_ratios[table]), -3),
                    ]
                else:
                    adjusted_scores: List[int] = [
                        round(int((base_scores[i] / 3) * 0.15 * self.target_score_ratios[table]), -3),
                        round(int((base_scores[i] / 3) * 0.325 * self.target_score_ratios[table]), -3),
                        round(int((base_scores[i] / 3) * 0.7 * self.target_score_ratios[table]), -3),
                        round(int((base_scores[i] / 3) * self.target_score_ratios[table]), -3),
                    ]

                    if 0 in adjusted_scores:
                        adjusted_scores: List[int] = [
                            round(int((base_scores[i] / 3) * 0.15 * self.target_score_ratios[table]), -2),
                            round(int((base_scores[i] / 3) * 0.325 * self.target_score_ratios[table]), -2),
                            round(int((base_scores[i] / 3) * 0.7 * self.target_score_ratios[table]), -2),
                            round(int((base_scores[i] / 3) * self.target_score_ratios[table]), -2),
                        ]

                self.target_scores[table][game_mode] = adjusted_scores

        self.useful_item_percentage = self.options.useful_item_percentage.value

        self.trap_percentage = self.options.trap_percentage.value

        self.trap_weights = {
            trap_type: 1 for trap_type in PinballFXAPTrapTypes
        }

        trap_type_name: str
        weight: Any
        for trap_type_name, weight in self.options.trap_weights.value.items():
            try:
                trap_type: PinballFXAPTrapTypes = PinballFXAPTrapTypes(trap_type_name)
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
        region_menu: Region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(region_menu)

        region_endgame: Region = Region("Endgame", self.player, self.multiworld)

        if self.goal == PinballFXAPGoals.SHINY_QUARTERS_HUNT:
            region_menu.connect(region_endgame, rule=Has("Shiny Quarter", self.shiny_quarters_required))
            self.multiworld.regions.append(region_endgame)

        # Tables
        table: PinballFXTables
        for table in (self.selected_tables + [self.selected_goal_table]):
            if table is None:
                continue

            region_table: Region = Region(f"Table: {table.value}", self.player, self.multiworld)

            if table != self.selected_goal_table:
                table_tag: PinballFXAPTags = getattr(PinballFXAPTags, f"{table.name}_LOCATION")

                classic_mode_location_names: List[str] = locations_with_tags([table_tag, PinballFXAPTags.CLASSIC_MODE_LOCATION])

                location_name: str
                for location_name in classic_mode_location_names:
                    data: PinballFXLocationData = location_data[location_name]

                    if PinballFXAPTags.TARGET_SCORE_VERY_HIGH_LOCATION in data.tags and not self.include_very_high_tier_scores:
                        continue

                    location: PinballFXLocation = PinballFXLocation(
                        self.player,
                        location_name,
                        data.archipelago_id,
                        region_table,
                    )

                    self.set_rule(location, Has(f"Classic Mode Unlock: {table.value}"))

                    region_table.locations.append(location)

                time_challenge_location_names: List[str] = locations_with_tags([table_tag, PinballFXAPTags.TIME_CHALLENGE_LOCATION])

                location_name: str
                for location_name in time_challenge_location_names:
                    data: PinballFXLocationData = location_data[location_name]

                    if PinballFXAPTags.TARGET_SCORE_VERY_HIGH_LOCATION in data.tags and not self.include_very_high_tier_scores:
                        continue

                    location: PinballFXLocation = PinballFXLocation(
                        self.player,
                        location_name,
                        data.archipelago_id,
                        region_table,
                    )

                    self.set_rule(location, Has(f"Time Challenge Unlock: {table.value}"))

                    region_table.locations.append(location)

                if self.include_one_ball_challenges:
                    one_ball_challenge_location_names: List[str] = locations_with_tags([table_tag, PinballFXAPTags.ONE_BALL_CHALLENGE_LOCATION])

                    location_name: str
                    for location_name in one_ball_challenge_location_names:
                        data: PinballFXLocationData = location_data[location_name]

                        if PinballFXAPTags.TARGET_SCORE_VERY_HIGH_LOCATION in data.tags and not self.include_very_high_tier_scores:
                            continue

                        location: PinballFXLocation = PinballFXLocation(
                            self.player,
                            location_name,
                            data.archipelago_id,
                            region_table,
                        )

                        self.set_rule(location, Has(f"1 Ball Challenge Unlock: {table.value}"))

                        region_table.locations.append(location)

                if self.include_flips_challenges:
                    flips_challenge_location_names: List[str] = locations_with_tags([table_tag, PinballFXAPTags.FLIPS_CHALLENGE_LOCATION])

                    location_name: str
                    for location_name in flips_challenge_location_names:
                        data: PinballFXLocationData = location_data[location_name]

                        if PinballFXAPTags.TARGET_SCORE_VERY_HIGH_LOCATION in data.tags and not self.include_very_high_tier_scores:
                            continue

                        location: PinballFXLocation = PinballFXLocation(
                            self.player,
                            location_name,
                            data.archipelago_id,
                            region_table,
                        )

                        self.set_rule(location, Has(f"Flips Challenge Unlock: {table.value}"))

                        region_table.locations.append(location)

                if self.include_distance_challenges:
                    distance_challenge_location_names: List[str] = locations_with_tags([table_tag, PinballFXAPTags.DISTANCE_CHALLENGE_LOCATION])

                    location_name: str
                    for location_name in distance_challenge_location_names:
                        data: PinballFXLocationData = location_data[location_name]

                        if PinballFXAPTags.TARGET_SCORE_VERY_HIGH_LOCATION in data.tags and not self.include_very_high_tier_scores:
                            continue

                        location: PinballFXLocation = PinballFXLocation(
                            self.player,
                            location_name,
                            data.archipelago_id,
                            region_table,
                        )

                        self.set_rule(location, Has(f"Distance Challenge Unlock: {table.value}"))

                        region_table.locations.append(location)

            region_menu.connect(region_table)

            if table == self.selected_goal_table and self.goal == PinballFXAPGoals.SHINY_QUARTERS_FINAL_TABLE:
                region_table.connect(
                    region_endgame,
                    rule=And(Has("Shiny Quarter", self.shiny_quarters_required), Has(f"Classic Mode Unlock: {table.value}"))
                )

                self.multiworld.regions.append(region_endgame)

            self.multiworld.regions.append(region_table)

    def create_items(self) -> None:
        ## Precollect
        items_to_precollect: List[str] = list()

        # Starting Table Game Modes
        table: PinballFXTables
        game_modes: List[PinballFXGameModes]
        for table, game_modes in self.selected_starter_table_modes.items():
            game_mode: PinballFXGameModes
            for game_mode in game_modes:
                items_to_precollect.append(f"{game_mode.value} Unlock: {table.value}")

        ## Item Pool
        item_pool: List[PinballFXItem] = list()

        # Shiny Quarters
        i: int
        for i in range(self.shiny_quarters_total):
            item: PinballFXItem = self.create_item("Shiny Quarter")

            if i >= self.shiny_quarters_required:
                item.classification = ItemClassification.useful

            item_pool.append(item)

        # Table Game Mode Unlocks
        table: PinballFXTables
        for table in self.selected_tables:
            game_mode: PinballFXGameModes
            for game_mode in PinballFXGameModes:
                if game_mode == PinballFXGameModes.ONE_BALL and not self.include_one_ball_challenges:
                    continue
                elif game_mode == PinballFXGameModes.FLIPS and not self.include_flips_challenges:
                    continue
                elif game_mode == PinballFXGameModes.DISTANCE and not self.include_distance_challenges:
                    continue

                item_name: str = f"{game_mode.value} Unlock: {table.value}"

                if item_name in items_to_precollect:
                    continue

                item_pool.append(self.create_item(item_name))

        if self.selected_goal_table is not None:
            item_pool.append(self.create_item(f"{PinballFXGameModes.CLASSIC.value} Unlock: {self.selected_goal_table.value}"))

        # Traps / Useful / Filler
        total_location_count: int = len(self.multiworld.get_unfilled_locations(self.player))
        to_fill_location_count: int = total_location_count - len(item_pool)

        item_name: str
        for item_name in self._generate_useful_filler_trap_item_pool(to_fill_location_count):
            item_pool.append(self.create_item(item_name))

        self.multiworld.itempool += item_pool

        item: str
        for item in items_to_precollect:
            self.multiworld.push_precollected(self.create_item(item))

    def create_item(self, name: str) -> PinballFXItem:
        data: PinballFXItemData = item_data[name]

        return PinballFXItem(
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
            "shiny_quarters_total",
            "shiny_quarters_required",
            "pinball_table_selection",
            "pinball_table_count",
            "include_very_high_tier_scores",
            "include_one_ball_challenges",
            "include_flips_challenges",
            "include_distance_challenges",
            "target_score_requirement_mode",
            "target_score_requirement_percentage",
            "useful_item_percentage",
            "trap_percentage",
            "trap_weights",
            "trap_duration",
        )

        slot_data["trap_weights"] = {
            trap_type.value: weight for trap_type, weight in self.trap_weights.items()
        }

        slot_data["selected_tables"] = [table.value for table in self.selected_tables]

        slot_data["selected_starter_table_modes"] = dict()

        table: PinballFXTables
        game_modes: List[PinballFXGameModes]
        for table, game_modes in self.selected_starter_table_modes.items():
            slot_data["selected_starter_table_modes"][table.value] = [
                game_mode.value for game_mode in game_modes
            ]

        slot_data["selected_goal_table"] = None

        if self.selected_goal_table is not None:
            slot_data["selected_goal_table"] = self.selected_goal_table.value

        slot_data["target_scores"] = dict()

        table: PinballFXTables
        game_mode_scores: Dict[PinballFXGameModes, List[int]]
        for table, game_mode_scores in self.target_scores.items():
            slot_data["target_scores"][table.value] = dict()

            game_mode: PinballFXGameModes
            scores: List[int]
            for game_mode, scores in game_mode_scores.items():
                slot_data["target_scores"][table.value][game_mode.value] = scores

        slot_data["target_score_ratios"] = {
            table.value: self.target_score_ratios[table] for table in self.target_score_ratios.keys()
        }

        # Relay generate_early Overrides
        if slot_data["shiny_quarters_total"] != self.shiny_quarters_total:
            slot_data["shiny_quarters_total"] = self.shiny_quarters_total

        if slot_data["shiny_quarters_required"] != self.shiny_quarters_required:
            slot_data["shiny_quarters_required"] = self.shiny_quarters_required

        pinball_table_count: int = len(self.selected_tables)

        if self.selected_goal_table is not None:
            pinball_table_count += 1

        if slot_data["pinball_table_count"] != pinball_table_count:
            slot_data["pinball_table_count"] = pinball_table_count

        return slot_data

    def write_spoiler_header(self, spoiler_handle: TextIO) -> None:
        join_string: str = "\n  "
        nested_join_string: str = "\n    "

        spoiler_handle.write(f"\n\nSelected Tables:\n  {join_string.join([t.value for t in self.selected_tables])}")

        if self.selected_goal_table is not None:
            spoiler_handle.write(f"\n\nGoal Table: {self.selected_goal_table.value}")

        spoiler_handle.write(f"\n\nStarting Game Modes:")

        table: PinballFXTables
        game_modes: List[PinballFXGameModes]
        for table, game_modes in self.selected_starter_table_modes.items():
            spoiler_handle.write(join_string + f"{table.value}:  {', '.join(sorted([game_mode.value for game_mode in game_modes]))}")

        depth: int = 4

        if not self.include_very_high_tier_scores:
            depth = 3

        spoiler_handle.write(f"\n\nTarget Scores:")

        table: PinballFXTables
        game_mode_scores: Dict[PinballFXGameModes, List[int]]
        for table, game_mode_scores in self.target_scores.items():
            spoiler_handle.write(join_string + f"{table.value} ({self.target_score_ratios[table]}x):")

            game_mode: PinballFXGameModes
            scores: List[int]
            for game_mode, scores in game_mode_scores.items():
                if game_mode == PinballFXGameModes.ONE_BALL and not self.include_one_ball_challenges:
                    continue
                elif game_mode == PinballFXGameModes.FLIPS and not self.include_flips_challenges:
                    continue
                elif game_mode == PinballFXGameModes.DISTANCE and not self.include_distance_challenges:
                    continue

                spoiler_handle.write(nested_join_string + f"{game_mode.value}: {' / '.join(f'{score:,}' for score in scores[:depth])}")

        if self.selected_goal_table is not None:
            spoiler_handle.write(f"\n\nGoal Table Target Score:")
            spoiler_handle.write(join_string + f"{self.selected_goal_table.value}: {self.target_scores[self.selected_goal_table][PinballFXGameModes.CLASSIC][2]:,}")

        spoiler_handle.write("\n")

    def get_filler_item_name(self) -> str:
        return self.random.choice(self.filler_item_names)

    @staticmethod
    def interpret_slot_data(slot_data: Dict[str, Any]) -> Dict[str, Any]:
        return process_slot_data(slot_data)

    def _apply_universal_tracker_passthrough(self) -> None:
        if "Pinball FX" in self.multiworld.re_gen_passthrough:
            passthrough: Dict[str, Any] = self.multiworld.re_gen_passthrough["Pinball FX"]

            self.goal = passthrough["goal"]
            self.shiny_quarters_total = passthrough["shiny_quarters_total"]
            self.shiny_quarters_required = passthrough["shiny_quarters_required"]
            self.pinball_table_selection = passthrough["pinball_table_selection"]
            self.pinball_table_count = passthrough["pinball_table_count"]
            self.include_very_high_tier_scores = passthrough["include_very_high_tier_scores"]
            self.include_one_ball_challenges = passthrough["include_one_ball_challenges"]
            self.include_flips_challenges = passthrough["include_flips_challenges"]
            self.include_distance_challenges = passthrough["include_distance_challenges"]
            self.target_score_requirement_mode = passthrough["target_score_requirement_mode"]
            self.target_score_requirement_percentage = passthrough["target_score_requirement_percentage"]
            self.useful_item_percentage = passthrough["useful_item_percentage"]
            self.trap_percentage = passthrough["trap_percentage"]
            self.trap_weights = passthrough["trap_weights"]
            self.trap_duration = passthrough["trap_duration"]
            self.selected_tables = passthrough["selected_tables"]
            self.selected_starter_table_modes = passthrough["selected_starter_table_modes"]
            self.selected_goal_table = passthrough["selected_goal_table"]
            self.target_scores = passthrough["target_scores"]
            self.target_score_ratios = passthrough["target_score_ratios"]

            # Location Aliases
            index_mapping: Dict[int, str] = {
                0: "(Low)",
                1: "(Mid)",
                2: "(High)",
                3: "(Very High)",
            }

            table: PinballFXTables
            game_mode_scores: Dict[PinballFXGameModes, List[int]]
            for table, game_mode_scores in self.target_scores.items():
                if table == self.selected_goal_table:
                    continue

                game_mode: PinballFXGameModes
                scores: List[int]
                for game_mode, scores in game_mode_scores.items():
                    if game_mode == PinballFXGameModes.ONE_BALL and not self.include_one_ball_challenges:
                        continue
                    elif game_mode == PinballFXGameModes.FLIPS and not self.include_flips_challenges:
                        continue
                    elif game_mode == PinballFXGameModes.DISTANCE and not self.include_distance_challenges:
                        continue

                    i: int
                    score: int
                    for i, score in enumerate(scores):
                        self.location_id_to_alias[
                            self.location_name_to_id[f"{table.value} - {game_mode.value}: Target Score {index_mapping[i]}"]
                        ] = f"{score:,} - {table_to_table_groups[table].value}"

    def _generate_useful_filler_trap_item_pool(self, count: int) -> List[str]:
        useful_items_needed: int = round(self.useful_item_percentage / 100 * count)

        _remaining_items: int = count - useful_items_needed

        trap_items_needed: int = round(self.trap_percentage / 100 * _remaining_items)
        filler_items_needed: int = _remaining_items - trap_items_needed

        item_pool: List[str] = list()

        if useful_items_needed > 0:
            useful_item_pool: List[str] = list()

            table: PinballFXTables
            for table in self.selected_tables:
                useful_item_pool.append(f"{table.value} - Classic Mode: Score Multiplier")
                useful_item_pool.append(f"{table.value} - Classic Mode: Target Score Discount")

                useful_item_pool.append(f"{table.value} - Time Challenge: Score Multiplier")
                useful_item_pool.append(f"{table.value} - Time Challenge: Target Score Discount")

                if self.include_one_ball_challenges:
                    useful_item_pool.append(f"{table.value} - 1 Ball Challenge: Score Multiplier")
                    useful_item_pool.append(f"{table.value} - 1 Ball Challenge: Target Score Discount")

                if self.include_flips_challenges:
                    useful_item_pool.append(f"{table.value} - Flips Challenge: Score Multiplier")
                    useful_item_pool.append(f"{table.value} - Flips Challenge: Target Score Discount")

                if self.include_distance_challenges:
                    useful_item_pool.append(f"{table.value} - Distance Challenge: Score Multiplier")
                    useful_item_pool.append(f"{table.value} - Distance Challenge: Target Score Discount")

            item_pool.extend([
                useful_item for useful_item in self.random.choices(useful_item_pool, k=useful_items_needed)
            ])

        if trap_items_needed > 0:
            trap_items: List[PinballFXAPTrapTypes] = list(self.trap_weights.keys())
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

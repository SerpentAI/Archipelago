import logging

from typing import Any, Dict, List, Optional, TextIO, Tuple

from rule_builder.rules import Rule, And, Has

from BaseClasses import Item, ItemClassification, Location, Region, Tutorial

from Options import OptionError

from worlds.AutoWorld import WebWorld, World

from .data.game_data import (
    level_to_par_score,
    level_to_par_time,
    mutator_option_balanced,
    mutator_option_mostly_buffs,
    mutator_option_mostly_debuffs,
    mutator_option_only_buffs,
    mutator_option_only_debuffs,
    mutator_option_oops_all_the_same,
    mutator_to_score_multiplier,
    rank_to_par_score_multiplier,
    stylish_action_maximums,
    stylish_actions_pool,
)

from .data.item_data import SeveredSteelItemData, item_data
from .data.location_data import SeveredSteelLocationData, location_data

from .data_funcs import (
    id_to_goals,
    id_to_mutator_pool_types,
    id_to_requirement_modes,
    item_names_to_id,
    item_groups,
    location_groups,
    location_names_to_id,
    locations_with_tag,
    process_slot_data,
)

from .enums import (
    SeveredSteelAPGoals,
    SeveredSteelAPMutatorPoolTypes,
    SeveredSteelAPRequirementModes,
    SeveredSteelAPTags,
    SeveredSteelAPTrapTypes,
    SeveredSteelLevels,
    SeveredSteelMutators,
    SeveredSteelRanks,
    SeveredSteelStylishActions,
)

from .options import SeveredSteelOptions, option_groups


class SeveredSteelItem(Item):
    game = "Severed Steel"


class SeveredSteelLocation(Location):
    game = "Severed Steel"


class SeveredSteelWebWorld(WebWorld):
    theme: str = "partyTime"

    tutorials: List[Tutorial] = [
        Tutorial(
            "Multiworld Setup Guide",
            "A guide to setting up the Severed Steel randomizer connected to an Archipelago Multiworld",
            "English",
            "setup_en.md",
            "setup/en",
            ["Serpent.AI"],
        )
    ]

    option_groups = option_groups


class SeveredSteelWorld(World):
    """
    Severed Steel delivers a high-octane single-player first-person shooter experience defined by dynamic acrobatic movement, fully destructible environments, and a unique one-armed protagonist. Featuring a stylish bullet-time mechanic and an intense dark electronic soundtrack, the game rewards momentum, fluid stunt combinations, and relentless combat precision across fast-paced environments.
    """

    options_dataclass = SeveredSteelOptions
    options: SeveredSteelOptions

    game = "Severed Steel"

    item_name_to_id = item_names_to_id()
    location_name_to_id = location_names_to_id()

    item_name_groups = item_groups()
    location_name_groups = location_groups()

    required_client_version: Tuple[int, int, int] = (0, 6, 7)

    web = SeveredSteelWebWorld()

    filler_item_names: List[str] = item_groups()["Filler Item"]

    # Options
    goal: SeveredSteelAPGoals
    edensys_root_keys_total: int
    edensys_root_keys_required: int
    level_selection: Dict[SeveredSteelLevels, bool]
    level_count: int
    mutator_percentage: int
    mutator_pool_type: SeveredSteelAPMutatorPoolTypes
    mirrored_percentage: int
    include_target_times: bool
    include_challenges: bool
    include_stylish_action_challenges: bool
    stylish_action_challenge_count_per_level: int
    rank_score_requirement_mode: SeveredSteelAPRequirementModes
    rank_score_requirement_percentage: int
    target_time_requirement_mode: SeveredSteelAPRequirementModes
    target_time_requirement_percentage: int
    include_overpowered_items: bool
    invincible_mode: bool
    trap_percentage: int
    trap_weights: Dict[SeveredSteelAPTrapTypes, int]
    trap_duration: int

    # Generation
    selected_levels: List[SeveredSteelLevels]
    selected_starting_levels: List[SeveredSteelLevels]
    selected_goal_level: Optional[SeveredSteelLevels] = None

    level_to_mutator: Dict[SeveredSteelLevels, Optional[SeveredSteelMutators]]
    level_to_is_mirrored: Dict[SeveredSteelLevels, bool]

    level_to_stylish_action_challenges: Dict[SeveredSteelLevels, Optional[List[Tuple[SeveredSteelStylishActions, int]]]]

    target_rank_scores: Dict[SeveredSteelLevels, List[int]]
    target_times: Dict[SeveredSteelLevels, Optional[int]]

    # Metadata
    target_rank_score_ratios: Dict[SeveredSteelLevels, float]
    target_time_ratios: Dict[SeveredSteelLevels, Optional[float]]

    # Universal Tracker
    location_id_to_alias: Dict[int, str]
    ut_can_gen_without_yaml: bool = True
    explicit_indirect_conditions = False

    @property
    def is_universal_tracker(self) -> bool:
        return hasattr(self.multiworld, "re_gen_passthrough")

    def generate_early(self) -> None:
        self.goal = id_to_goals()[self.options.goal.value]

        self.edensys_root_keys_required = self.options.edensys_root_keys_required.value
        self.edensys_root_keys_total = self.options.edensys_root_keys_total.value

        if self.edensys_root_keys_required > self.edensys_root_keys_total:
            self.edensys_root_keys_required = self.edensys_root_keys_total

            logging.warning(
                f"Severed Steel: {self.player_name} has more required edensys root keys than total edensys root keys. "
                "Adjusting required edensys root keys to match total edensys root keys..."
            )

        # Levels
        level_pool: List[SeveredSteelLevels] = list()

        level_name: str
        is_enabled: bool
        for level_name, is_enabled in self.options.level_selection.value.items():
            if is_enabled:
                level_pool.append(SeveredSteelLevels(level_name))

        level_pool = list(sorted(level_pool, key=lambda s: s.value))

        if len(level_pool) < 12:
            raise OptionError(f"Severed Steel: {self.player_name} must have at least 12 Levels selected to play.")

        self.level_count = min(self.options.level_count.value, len(level_pool))

        self.random.shuffle(level_pool)
        level_pool = level_pool[:self.level_count]

        if self.goal == SeveredSteelAPGoals.EDENSYS_ROOT_KEYS_FINAL_LEVEL:
            self.selected_goal_level = level_pool[-1]
            self.selected_levels = level_pool[:-1]
        else:
            self.selected_levels = level_pool[:]

        self.selected_starting_levels = self.selected_levels[:3]

        # Level Modifiers
        self.level_to_mutator = dict()
        self.level_to_is_mirrored = dict()

        level: SeveredSteelLevels
        for level in self.selected_levels:  # Exclude goal level, if any, from modifiers
            self.level_to_mutator[level] = None
            self.level_to_is_mirrored[level] = False

        modifiable_level_pool: List[SeveredSteelLevels] = self.selected_levels[:]

        self.mutator_percentage = self.options.mutator_percentage.value
        self.mutator_pool_type = id_to_mutator_pool_types()[self.options.mutator_pool_type.value]

        mutated_level_count: int = int(round(len(self.selected_levels) * (self.mutator_percentage / 100.0)))

        if mutated_level_count > 0:
            mutator_pool: List[SeveredSteelMutators] = list()

            if self.mutator_pool_type == SeveredSteelAPMutatorPoolTypes.ONLY_DEBUFFS:
                mutator_pool = mutator_option_only_debuffs[:]
            elif self.mutator_pool_type == SeveredSteelAPMutatorPoolTypes.MOSTLY_DEBUFFS:
                mutator_pool = mutator_option_mostly_debuffs[:]
            elif self.mutator_pool_type == SeveredSteelAPMutatorPoolTypes.BALANCED:
                mutator_pool = mutator_option_balanced[:]
            elif self.mutator_pool_type == SeveredSteelAPMutatorPoolTypes.MOSTLY_BUFFS:
                mutator_pool = mutator_option_mostly_buffs[:]
            elif self.mutator_pool_type == SeveredSteelAPMutatorPoolTypes.ONLY_BUFFS:
                mutator_pool = mutator_option_only_buffs[:]
            elif self.mutator_pool_type == SeveredSteelAPMutatorPoolTypes.OOPS_ALL_TRIPLE_THREAT:
                mutator_pool = [SeveredSteelMutators.TRIPLE_THREAT]
            elif self.mutator_pool_type == SeveredSteelAPMutatorPoolTypes.OOPS_ALL_THE_SAME:
                mutator_pool = mutator_option_oops_all_the_same[:]

            self.random.shuffle(modifiable_level_pool)

            i: int
            for i in range(mutated_level_count):
                self.level_to_mutator[modifiable_level_pool[i]] = self.random.choice(mutator_pool)

        self.mirrored_percentage = self.options.mirrored_percentage.value

        mirrored_level_count: int = int(round(len(self.selected_levels) * (self.mirrored_percentage / 100.0)))

        if mirrored_level_count > 0:
            self.random.shuffle(modifiable_level_pool)

            i: int
            for i in range(mirrored_level_count):
                self.level_to_is_mirrored[modifiable_level_pool[i]] = True

        # Location Options
        self.include_target_times = self.options.include_target_times.value
        self.include_challenges = self.options.include_challenges.value
        self.include_stylish_action_challenges = self.options.include_stylish_action_challenges.value

        # Stylish Action Challenges
        self.stylish_action_challenge_count_per_level = self.options.stylish_action_challenge_count_per_level.value

        self.level_to_stylish_action_challenges = dict()

        level: SeveredSteelLevels
        for level in self.selected_levels:  # Exclude goal level, if any, from stylish action challenges
            if self.include_stylish_action_challenges:
                self.level_to_stylish_action_challenges[level] = list()

                mutator: Optional[SeveredSteelMutators] = self.level_to_mutator[level]

                stylish_action: SeveredSteelStylishActions
                for stylish_action in self.random.sample(stylish_actions_pool, self.stylish_action_challenge_count_per_level):
                    if stylish_action_maximums[stylish_action] == 1:
                        if mutator == SeveredSteelMutators.TRIPLE_THREAT:
                            self.level_to_stylish_action_challenges[level].append((stylish_action, self.random.randint(1, 3)))
                        else:
                            self.level_to_stylish_action_challenges[level].append((stylish_action, 1))
                    else:
                        if mutator == SeveredSteelMutators.TRIPLE_THREAT:
                            self.level_to_stylish_action_challenges[level].append(
                                (stylish_action, self.random.randint(1, stylish_action_maximums[stylish_action] * 3))
                            )
                        else:
                            self.level_to_stylish_action_challenges[level].append(
                                (stylish_action, self.random.randint(1, stylish_action_maximums[stylish_action]))
                            )
            else:
                self.level_to_stylish_action_challenges[level] = None

        # Target Rank Scores
        self.rank_score_requirement_mode = id_to_requirement_modes()[self.options.rank_score_requirement_mode.value]
        self.rank_score_requirement_percentage = self.options.rank_score_requirement_percentage.value

        self.target_rank_scores = dict()
        self.target_rank_score_ratios = dict()

        level: SeveredSteelLevels
        for level in self.selected_levels:
            self.target_rank_scores[level] = list()
            self.target_rank_score_ratios[level] = list()

            par_score: int = level_to_par_score[level]

            if self.level_to_mutator[level] in mutator_to_score_multiplier:
                par_score = round(int(par_score * mutator_to_score_multiplier[self.level_to_mutator[level]]), -2)

            par_scores: List[int] = list()

            ranks: List[SeveredSteelRanks] = [
                SeveredSteelRanks.B,
                SeveredSteelRanks.A,
                SeveredSteelRanks.S,
                SeveredSteelRanks.S_PLUS,
                SeveredSteelRanks.S_PLUS_PLUS,
            ]

            rank: SeveredSteelRanks
            for rank in ranks:
                par_scores.append(par_score * rank_to_par_score_multiplier[rank])

            if self.rank_score_requirement_mode == SeveredSteelAPRequirementModes.SAME_FOR_ALL:
                percentage: int = self.rank_score_requirement_percentage
                self.target_rank_score_ratios[level] = round(percentage / 100.0, 2)

                adjusted_scores: List[int] = [round(int(score * (percentage / 100)), -2) for score in par_scores]
            elif self.rank_score_requirement_mode == SeveredSteelAPRequirementModes.RANDOM:
                percentage: int = self.random.randint(50, self.rank_score_requirement_percentage)
                self.target_rank_score_ratios[level] = round(percentage / 100.0, 2)

                adjusted_scores: List[int] = [round(int(score * (percentage / 100)), -2) for score in par_scores]
            else:
                adjusted_scores = par_scores[:]

            self.target_rank_scores[level] = adjusted_scores

        # Target Times
        self.target_time_requirement_mode = id_to_requirement_modes()[self.options.target_time_requirement_mode.value]
        self.target_time_requirement_percentage = self.options.target_time_requirement_percentage.value

        self.target_times = dict()
        self.target_time_ratios = dict()

        level: SeveredSteelLevels
        for level in self.selected_levels:
            if self.include_target_times:
                par_time: int = level_to_par_time[level] // 2  # Used to be 5x #10 leaderboard time; now 2.5x

                if self.target_time_requirement_mode == SeveredSteelAPRequirementModes.SAME_FOR_ALL:
                    percentage: int = self.target_time_requirement_percentage
                    self.target_time_ratios[level] = round(percentage / 100.0, 2)

                    adjusted_time: int = int(par_time * (percentage / 100))
                elif self.target_time_requirement_mode == SeveredSteelAPRequirementModes.RANDOM:
                    percentage: int = self.random.randint(self.target_time_requirement_percentage, 250)
                    self.target_time_ratios[level] = round(percentage / 100.0, 2)

                    adjusted_time: int = int(par_time * (percentage / 100))
                else:
                    adjusted_time = par_time

                if self.level_to_mutator[level] == SeveredSteelMutators.TRIPLE_THREAT:
                    adjusted_time *= 3

                self.target_times[level] = adjusted_time
            else:
                self.target_times[level] = None
                self.target_time_ratios[level] = None

        # Item Options
        self.include_overpowered_items = bool(self.options.include_overpowered_items.value)

        if self.level_count < 20:
            self.include_overpowered_items = False

            logging.warning(
                f"Severed Steel: {self.player_name} wants to include overpowered items and had less than 20 levels. "
                "Disabling the inclusion of overpowered items..."
            )

        # Gameplay Options
        self.invincible_mode = bool(self.options.invincible_mode.value)

        # Traps
        self.trap_percentage = self.options.trap_percentage.value

        self.trap_weights = {
            trap_type: 1 for trap_type in SeveredSteelAPTrapTypes
        }

        trap_type_name: str
        weight: Any
        for trap_type_name, weight in self.options.trap_weights.value.items():
            try:
                trap_type: SeveredSteelAPTrapTypes = SeveredSteelAPTrapTypes(trap_type_name)
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

        if self.goal == SeveredSteelAPGoals.EDENSYS_ROOT_KEY_HUNT:
            region_menu.connect(region_endgame, rule=Has("EdenSys Root Key", self.edensys_root_keys_required))

            self.multiworld.regions.append(region_endgame)

        allowable_stylish_action_challenge_numbers: List[str] = [
            str(i) for i in range(1, self.stylish_action_challenge_count_per_level + 1)
        ]

        # Levels
        level: SeveredSteelLevels
        for level in (self.selected_levels + [self.selected_goal_level]):
            if level is None:
                continue

            region_level: Region = Region(level.value, self.player, self.multiworld)

            if level != self.selected_goal_level:
                level_tag: SeveredSteelAPTags = getattr(SeveredSteelAPTags, f"{level.name}_LOCATION")

                level_location_names: List[str] = locations_with_tag(level_tag)

                location_name: str
                for location_name in level_location_names:
                    data: SeveredSteelLocationData = location_data[location_name]

                    if not self.include_target_times and SeveredSteelAPTags.TARGET_TIME_LOCATION in data.tags:
                        continue

                    if not self.include_challenges and SeveredSteelAPTags.CHALLENGE_BASE_LOCATION in data.tags:
                        continue

                    if not self.include_stylish_action_challenges and SeveredSteelAPTags.CHALLENGE_STYLISH_ACTION_LOCATION in data.tags:
                        continue

                    if SeveredSteelAPTags.CHALLENGE_STYLISH_ACTION_LOCATION in data.tags:
                        if location_name.split("#")[-1] not in allowable_stylish_action_challenge_numbers:
                            continue

                    location: SeveredSteelLocation = SeveredSteelLocation(
                        self.player,
                        location_name,
                        data.archipelago_id,
                        region_level,
                    )

                    location_access_rule: Optional[Rule] = None

                    if SeveredSteelAPTags.RANK_A_LOCATION in data.tags:
                        location_access_rule = And(
                            Has("Progressive Multiplier Burn Rate Reduction", 1),
                            Has("Progressive Fresh Cooldown Reduction", 1),
                        )
                    elif SeveredSteelAPTags.RANK_S_LOCATION in data.tags:
                        location_access_rule = And(
                            Has("Progressive Multiplier Burn Rate Reduction", 2),
                            Has("Progressive Fresh Cooldown Reduction", 2),
                        )
                    elif SeveredSteelAPTags.RANK_S_PLUS_LOCATION in data.tags:
                        location_access_rule = And(
                            Has("Progressive Multiplier Burn Rate Reduction", 3),
                            Has("Progressive Fresh Cooldown Reduction", 3),
                        )
                    elif SeveredSteelAPTags.RANK_S_PLUS_PLUS_LOCATION in data.tags:
                        location_access_rule = And(
                            Has("Progressive Multiplier Burn Rate Reduction", 4),
                            Has("Progressive Fresh Cooldown Reduction", 4),
                        )
                    elif SeveredSteelAPTags.CHALLENGE_STYLISH_ACTION_LOCATION in data.tags:
                        index: int = int(location_name.split("#")[-1]) - 1
                        stylish_action: SeveredSteelStylishActions = self.level_to_stylish_action_challenges[level][index][0]

                        location_access_rule = Has(f"Stylish Action License: {stylish_action.value}")

                    if location_access_rule is not None:
                        self.set_rule(location, location_access_rule)

                    region_level.locations.append(location)
            else:
                if self.goal == SeveredSteelAPGoals.EDENSYS_ROOT_KEYS_FINAL_LEVEL:
                    region_level.connect(region_endgame, rule=Has("EdenSys Root Key", self.edensys_root_keys_required))

            region_menu.connect(region_level, rule=Has(f"Level Unlock: {level.value}"))

            if level == self.selected_goal_level and self.goal == SeveredSteelAPGoals.EDENSYS_ROOT_KEYS_FINAL_LEVEL:
                self.multiworld.regions.append(region_endgame)

            self.multiworld.regions.append(region_level)

    def create_items(self) -> None:
        ## Precollect
        items_to_precollect: List[str] = list()

        # Starting Levels
        level: SeveredSteelLevels
        for level in self.selected_starting_levels:
            items_to_precollect.append(f"Level Unlock: {level.value}")

        ## Item Pool
        item_pool: List[SeveredSteelItem] = list()

        # Goal Items
        i: int
        for i in range(self.edensys_root_keys_total):
            item: SeveredSteelItem = self.create_item("EdenSys Root Key")

            if i >= self.edensys_root_keys_required:
                item.classification = ItemClassification.useful

            item_pool.append(item)

        # Rank-Boosting Items
        for _ in range(5):
            item_pool.append(self.create_item("Progressive Multiplier Burn Rate Reduction"))
            item_pool.append(self.create_item("Progressive Fresh Cooldown Reduction"))

        # Level Unlock Items
        level: SeveredSteelLevels
        for level in (self.selected_levels + [self.selected_goal_level]):
            if level is None:
                continue

            location_name: str = f"Level Unlock: {level.value}"

            if location_name in items_to_precollect:
                continue

            item_pool.append(self.create_item(location_name))

        # Stylish Action License Items
        if self.include_stylish_action_challenges:
            stylish_action: SeveredSteelStylishActions
            for stylish_action in stylish_actions_pool:
                item_pool.append(self.create_item(f"Stylish Action License: {stylish_action.value}"))

        # Per-Level Items
        level: SeveredSteelLevels
        for level in (self.selected_levels + [self.selected_goal_level]):
            if level is None:
                continue

            item_pool.append(self.create_item(f"{level.value}: 10% Target Time Discount"))
            item_pool.append(self.create_item(f"{level.value}: Double Score"))

            if self.include_overpowered_items:
                item_pool.append(self.create_item(f"{level.value}: Unlimited Ammo Unlocked"))
                item_pool.append(self.create_item(f"{level.value}: Unlimited Cannon Ammo Unlocked"))

                if not self.invincible_mode:
                    item_pool.append(self.create_item(f"{level.value}: Invincibility Unlocked"))

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

    def create_item(self, name: str) -> SeveredSteelItem:
        data: SeveredSteelItemData = item_data[name]

        return SeveredSteelItem(
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
            "edensys_root_keys_total",
            "edensys_root_keys_required",
            "level_selection",
            "level_count",
            "mutator_percentage",
            "mutator_pool_type",
            "mirrored_percentage",
            "include_target_times",
            "include_challenges",
            "include_stylish_action_challenges",
            "stylish_action_challenge_count_per_level",
            "rank_score_requirement_mode",
            "rank_score_requirement_percentage",
            "target_time_requirement_mode",
            "target_time_requirement_percentage",
            "include_overpowered_items",
            "invincible_mode",
            "trap_percentage",
            "trap_weights",
            "trap_duration",
        )

        slot_data["trap_weights"] = {
            trap_type.value: weight for trap_type, weight in self.trap_weights.items()
        }

        slot_data["selected_levels"] = [level.value for level in self.selected_levels]
        slot_data["selected_starting_levels"] = [level.value for level in self.selected_starting_levels]
        slot_data["selected_goal_level"] = self.selected_goal_level.value if self.selected_goal_level is not None else None

        slot_data["level_to_mutator"] = dict()

        level: SeveredSteelLevels
        mutator: Optional[SeveredSteelMutators]
        for level, mutator in self.level_to_mutator.items():
            slot_data["level_to_mutator"][level.value] = None

            if mutator is not None:
                slot_data["level_to_mutator"][level.value] = mutator.value

        slot_data["level_to_is_mirrored"] = dict()

        level: SeveredSteelLevels
        is_mirrored: bool
        for level, is_mirrored in self.level_to_is_mirrored.items():
            slot_data["level_to_is_mirrored"][level.value] = is_mirrored

        slot_data["level_to_stylish_action_challenges"] = dict()

        level: SeveredSteelLevels
        challenge_data: Optional[List[Tuple[SeveredSteelStylishActions, int]]]
        for level, challenge_data in self.level_to_stylish_action_challenges.items():
            if challenge_data is None:
                slot_data["level_to_stylish_action_challenges"][level.value] = None
                continue

            slot_data["level_to_stylish_action_challenges"][level.value] = list()

            challenge_item: Tuple[SeveredSteelStylishActions, int]
            for challenge_item in challenge_data:
                slot_data["level_to_stylish_action_challenges"][level.value].append((challenge_item[0].value, challenge_item[1]))

        slot_data["target_rank_scores"] = dict()

        level: SeveredSteelLevels
        rank_scores: List[int]
        for level, rank_scores in self.target_rank_scores.items():
            slot_data["target_rank_scores"][level.value] = rank_scores

        slot_data["target_times"] = dict()

        level: SeveredSteelLevels
        times: Optional[List[int]]
        for level, time in self.target_times.items():
            slot_data["target_times"][level.value] = time

        slot_data["target_rank_score_ratios"] = dict()

        level: SeveredSteelLevels
        rank_score_ratio: float
        for level, rank_score_ratio in self.target_rank_score_ratios.items():
            slot_data["target_rank_score_ratios"][level.value] = rank_score_ratio

        slot_data["target_time_ratios"] = dict()

        level: SeveredSteelLevels
        time_ratio: Optional[float]
        for level, time_ratio in self.target_time_ratios.items():
            slot_data["target_time_ratios"][level.value] = time_ratio

        # Relay generate_early Overrides
        if slot_data["edensys_root_keys_required"] != self.edensys_root_keys_required:
            slot_data["edensys_root_keys_required"] = self.edensys_root_keys_required

        if slot_data["level_count"] != self.level_count:
            slot_data["level_count"] = self.level_count

        if slot_data["include_overpowered_items"] != self.include_overpowered_items:
            slot_data["include_overpowered_items"] = self.include_overpowered_items

        return slot_data

    def write_spoiler_header(self, spoiler_handle: TextIO) -> None:
        join_string: str = "\n  "
        nested_join_string: str = "\n    "

        # Levels
        spoiler_handle.write(
            f"\n\nStarting Levels:\n  {join_string.join([l.value for l in self.selected_starting_levels])}"
        )

        spoiler_handle.write(
            f"\n\nUnlockable Levels:\n  {join_string.join([l.value for l in self.selected_levels[3:]])}"
        )

        if self.selected_goal_level is not None:
            spoiler_handle.write(f"\n\nGoal Level: {self.selected_goal_level.value}")

        # Level Mutators
        if self.mutator_percentage > 0:
            spoiler_handle.write(f"\n\nLevel Mutators:")

            level: SeveredSteelLevels
            for level in self.selected_levels:
                mutator: Optional[SeveredSteelMutators] = self.level_to_mutator[level]
                mutator_name: str = ""

                if mutator is not None:
                    mutator_name = mutator.value

                spoiler_handle.write(join_string + f"{level.value}: {mutator_name}")

        # Mirrored Levels
        if self.mirrored_percentage > 0:
            spoiler_handle.write(f"\n\nMirrored Levels:")

            level: SeveredSteelLevels
            for level in self.selected_levels:
                is_mirrored: bool = self.level_to_is_mirrored[level]
                is_mirrored_name: str = ""

                if is_mirrored:
                    is_mirrored_name = "Mirrored"

                spoiler_handle.write(join_string + f"{level.value}: {is_mirrored_name}")

        # Stylish Action Challenges
        if self.include_stylish_action_challenges:
            spoiler_handle.write(f"\n\nStylish Action Challenges:")

            level: SeveredSteelLevels
            for level in self.selected_levels:
                spoiler_handle.write(join_string + f"{level.value}:")

                challenge: Tuple[SeveredSteelStylishActions, int]
                for challenge in self.level_to_stylish_action_challenges[level]:
                    spoiler_handle.write(nested_join_string + f"{challenge[1]}x {challenge[0].value}")

        # Target Rank Scores
        spoiler_handle.write(f"\n\nTarget Rank Scores:")

        level: SeveredSteelLevels
        for level in self.selected_levels:
            rank_scores: List[int] = self.target_rank_scores[level]
            ratio: float = round(self.target_rank_score_ratios[level], 2)

            spoiler_handle.write(join_string + f"{level.value} ({ratio}x): {' / '.join(f'{score:,}' for score in rank_scores)}")

        # Target Times
        if self.include_target_times:
            spoiler_handle.write(f"\n\nTarget Times:")

            level: SeveredSteelLevels
            for level in self.selected_levels:
                time: int = self.target_times[level]
                formatted_time: str = f"{time // 60:1d}:{time % 60:02d}"
                ratio: float = round(self.target_time_ratios[level], 2)

                spoiler_handle.write(join_string + f"{level.value} ({ratio}x): {formatted_time}")

        spoiler_handle.write("\n")

    def get_filler_item_name(self) -> str:
        return self.random.choice(self.filler_item_names)

    @staticmethod
    def interpret_slot_data(slot_data: Dict[str, Any]) -> Dict[str, Any]:
        return process_slot_data(slot_data)

    def _apply_universal_tracker_passthrough(self) -> None:
        if "Severed Steel" in self.multiworld.re_gen_passthrough:
            passthrough: Dict[str, Any] = self.multiworld.re_gen_passthrough["Severed Steel"]

            self.goal = passthrough["goal"]
            self.edensys_root_keys_total = passthrough["edensys_root_keys_total"]
            self.edensys_root_keys_required = passthrough["edensys_root_keys_required"]
            self.level_selection = passthrough["level_selection"]
            self.level_count = passthrough["level_count"]
            self.mutator_percentage = passthrough["mutator_percentage"]
            self.mutator_pool_type = passthrough["mutator_pool_type"]
            self.mirrored_percentage = passthrough["mirrored_percentage"]
            self.include_target_times = passthrough["include_target_times"]
            self.include_challenges = passthrough["include_challenges"]
            self.include_stylish_action_challenges = passthrough["include_stylish_action_challenges"]
            self.stylish_action_challenge_count_per_level = passthrough["stylish_action_challenge_count_per_level"]
            self.rank_score_requirement_mode = passthrough["rank_score_requirement_mode"]
            self.rank_score_requirement_percentage = passthrough["rank_score_requirement_percentage"]
            self.target_time_requirement_mode = passthrough["target_time_requirement_mode"]
            self.target_time_requirement_percentage = passthrough["target_time_requirement_percentage"]
            self.include_overpowered_items = passthrough["include_overpowered_items"]
            self.invincible_mode = passthrough["invincible_mode"]
            self.trap_percentage = passthrough["trap_percentage"]
            self.trap_weights = passthrough["trap_weights"]
            self.trap_duration = passthrough["trap_duration"]

            self.selected_levels = passthrough["selected_levels"]
            self.selected_starting_levels = passthrough["selected_starting_levels"]
            self.selected_goal_level = passthrough["selected_goal_level"]

            self.level_to_mutator = passthrough["level_to_mutator"]
            self.level_to_is_mirrored = passthrough["level_to_is_mirrored"]

            self.level_to_stylish_action_challenges = passthrough["level_to_stylish_action_challenges"]

            self.target_rank_scores = passthrough["target_rank_scores"]
            self.target_times = passthrough["target_times"]

            self.target_rank_score_ratios = passthrough["target_rank_score_ratios"]
            self.target_time_ratios = passthrough["target_time_ratios"]

            # Location Aliases
            level: SeveredSteelLevels
            for level in self.selected_levels:
                self.location_id_to_alias[
                    self.location_name_to_id[f"{level.value} - Obtain a B Rank"]
                ] = f"{self.target_rank_scores[level][0]:,}"

                self.location_id_to_alias[
                    self.location_name_to_id[f"{level.value} - Obtain an A Rank"]
                ] = f"{self.target_rank_scores[level][1]:,}"

                self.location_id_to_alias[
                    self.location_name_to_id[f"{level.value} - Obtain an S Rank"]
                ] = f"{self.target_rank_scores[level][2]:,}"

                self.location_id_to_alias[
                    self.location_name_to_id[f"{level.value} - Obtain an S+ Rank"]
                ] = f"{self.target_rank_scores[level][3]:,}"

                self.location_id_to_alias[
                    self.location_name_to_id[f"{level.value} - Obtain an S++ Rank"]
                ] = f"{self.target_rank_scores[level][4]:,}"

                if self.include_target_times:
                    time: int = self.target_times[level]
                    formatted_time: str = f"{time // 60:1d}:{time % 60:02d}"

                    self.location_id_to_alias[
                        self.location_name_to_id[f"{level.value} - Beat the Target Time"]
                    ] = formatted_time

                if self.include_stylish_action_challenges:
                    i: int
                    for i in range(self.stylish_action_challenge_count_per_level):
                        challenge: Tuple[SeveredSteelStylishActions, int] = self.level_to_stylish_action_challenges[level][i]

                        self.location_id_to_alias[
                            self.location_name_to_id[f"{level.value} - Complete Stylish Action Challenge #{i + 1}"]
                        ] = f"{challenge[1]}x {challenge[0].value}"

    def _generate_filler_trap_item_pool(self, count: int) -> List[str]:
        trap_items_needed: int = round(self.trap_percentage / 100 * count)
        filler_items_needed: int = count - trap_items_needed

        item_pool: List[str] = list()

        if trap_items_needed > 0:
            trap_items: List[SeveredSteelAPTrapTypes] = list(self.trap_weights.keys())
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

import logging

from typing import Any, Dict, List, Optional, TextIO, Tuple

from BaseClasses import Item, ItemClassification, Location, Region, Tutorial

from Options import OptionError

from worlds.AutoWorld import WebWorld, World

from .data.game_data import (
    level_to_base_scores,
    level_to_base_combo_scores,
    level_to_gaps,
    level_to_level_types,
)

from .data.item_data import TonyHawksProSkater12ItemData, item_data
from .data.location_data import TonyHawksProSkater12LocationData, location_data

from .data_funcs import (
    id_to_goals,
    id_to_requirement_modes,
    item_names_to_id,
    item_groups,
    location_groups,
    location_names_to_id,
    locations_with_tag,
    locations_with_tags,
    location_access_rule_for,
    process_slot_data,
)

from .enums import (
    TonyHawksProSkater12APGoals,
    TonyHawksProSkater12APRequirementModes,
    TonyHawksProSkater12APTags,
    TonyHawksProSkater12APTrapTypes,
    TonyHawksProSkater12Gaps,
    TonyHawksProSkater12Levels,
    TonyHawksProSkater12LevelTypes,
    TonyHawksProSkater12Skaters,
)

from .options import TonyHawksProSkater12Options, option_groups


class TonyHawksProSkater12Item(Item):
    game = "Tony Hawk's Pro Skater 1 + 2"


class TonyHawksProSkater12Location(Location):
    game = "Tony Hawk's Pro Skater 1 + 2"


class TonyHawksProSkater12WebWorld(WebWorld):
    theme: str = "partyTime"

    tutorials: List[Tutorial] = [
        Tutorial(
            "Multiworld Setup Guide",
            "A guide to setting up the Tony Hawk's Pro Skater 1 + 2 randomizer connected to an Archipelago Multiworld",
            "English",
            "setup_en.md",
            "setup/en",
            ["Serpent.AI"],
        )
    ]

    option_groups = option_groups


class TonyHawksProSkater12World(World):
    """
    Tony Hawk's Pro Skater 1 + 2 revitalizes the classic arcade skateboarding experience with modernized visuals
    and fluid mechanics, merging the original two titles into a single, seamless collection. Featuring an expanded
    roster of professional skaters and a contemporary soundtrack, the game delivers enhanced environments and objectives
    that reward creative combos and precise trick execution.
    """

    options_dataclass = TonyHawksProSkater12Options
    options: TonyHawksProSkater12Options

    game = "Tony Hawk's Pro Skater 1 + 2"

    item_name_to_id = item_names_to_id()
    location_name_to_id = location_names_to_id()

    item_name_groups = item_groups()
    location_name_groups = location_groups()

    required_client_version: Tuple[int, int, int] = (0, 6, 7)

    web = TonyHawksProSkater12WebWorld()

    filler_item_names: List[str] = item_groups()["Filler Item"]

    # Options
    goal: TonyHawksProSkater12APGoals
    secret_tapes_total: int
    secret_tapes_required: int
    skater_selection: Dict[TonyHawksProSkater12Skaters, bool]
    skater_count: int
    level_selection: Dict[TonyHawksProSkater12Levels, bool]
    level_count: int
    include_platinum_scores: bool
    include_platinum_combo_scores: bool
    include_signature_specials: bool
    include_long_tricks: bool
    include_gaps: bool
    gap_count_per_level: int
    score_requirement_mode: TonyHawksProSkater12APRequirementModes
    score_requirement_percentage: int
    combo_score_requirement_mode: TonyHawksProSkater12APRequirementModes
    combo_score_requirement_percentage: int
    starting_trick_type_weights: Dict[str, int]
    include_overpowered_abilities: bool
    trap_percentage: int
    trap_weights: Dict[TonyHawksProSkater12APTrapTypes, int]

    # Generation
    selected_skaters: List[TonyHawksProSkater12Skaters]
    selected_starting_skater: TonyHawksProSkater12Skaters

    selected_levels: List[TonyHawksProSkater12Levels]
    selected_starting_levels: List[TonyHawksProSkater12Levels]
    selected_goal_level: Optional[TonyHawksProSkater12Levels] = None

    target_scores: Dict[TonyHawksProSkater12Levels, Dict[TonyHawksProSkater12Skaters, List[int]]]
    target_combo_scores: Dict[TonyHawksProSkater12Levels, Dict[TonyHawksProSkater12Skaters, List[int]]]

    target_gaps: Optional[
        Dict[TonyHawksProSkater12Levels, Dict[TonyHawksProSkater12Skaters, List[TonyHawksProSkater12Gaps]]]
    ] = None

    target_long_tricks: Dict[TonyHawksProSkater12Levels, Dict[TonyHawksProSkater12Skaters, List[float]]]

    starting_trick_types: Dict[TonyHawksProSkater12Skaters, str]

    # Metadata
    target_score_ratios: Dict[TonyHawksProSkater12Levels, Dict[TonyHawksProSkater12Skaters, float]]
    target_combo_score_ratios: Dict[TonyHawksProSkater12Levels, Dict[TonyHawksProSkater12Skaters, float]]

    # Universal Tracker
    location_id_to_alias: Dict[int, str]
    ut_can_gen_without_yaml: bool = True

    @property
    def is_universal_tracker(self) -> bool:
        return hasattr(self.multiworld, "re_gen_passthrough")

    def generate_early(self) -> None:
        self.goal = id_to_goals()[self.options.goal.value]

        self.secret_tapes_required = self.options.secret_tapes_required.value
        self.secret_tapes_total = self.options.secret_tapes_total.value

        if self.secret_tapes_required > self.secret_tapes_total:
            self.secret_tapes_required = self.secret_tapes_total

            logging.warning(
                f"Tony Hawk's Pro Skater 1 + 2: {self.player_name} has more required secret tapes than total secret tapes. "
                "Adjusting required secret tapes to match total secret tapes..."
            )

        # Skaters
        skater_pool: List[TonyHawksProSkater12Skaters] = list()

        skater_name: str
        is_enabled: bool
        for skater_name, is_enabled in self.options.skater_selection.value.items():
            if is_enabled:
                skater_pool.append(TonyHawksProSkater12Skaters(skater_name))

        skater_pool = list(sorted(skater_pool, key=lambda s: s.value))

        if not len(skater_pool):
            raise OptionError(
                f"Tony Hawk's Pro Skater 1 + 2: {self.player_name} must have at least 1 Skater selected to play. "
                "All of their Skaters are set to False."
            )

        self.skater_count = min(self.options.skater_count.value, len(skater_pool))

        skaters: List[TonyHawksProSkater12Skaters] = self.random.sample(skater_pool, self.skater_count)

        self.selected_skaters = skaters
        self.selected_starting_skater = skaters[0]

        # Levels
        level_pool: List[TonyHawksProSkater12Levels] = list()

        level_name: str
        is_enabled: bool
        for level_name, is_enabled in self.options.level_selection.value.items():
            if is_enabled:
                level_pool.append(TonyHawksProSkater12Levels(level_name))

        level_pool = list(sorted(level_pool, key=lambda s: s.value))

        if len(level_pool) < 8:
            raise OptionError(f"Tony Hawk's Pro Skater 1 + 2: {self.player_name} must have at least 8 Levels selected to play.")

        self.level_count = min(self.options.level_count.value, len(level_pool))

        while True:
            self.random.shuffle(level_pool)

            if level_to_level_types[level_pool[0]] == TonyHawksProSkater12LevelTypes.OBJECTIVES:
                break

        level_pool = level_pool[:self.level_count]

        if self.goal == TonyHawksProSkater12APGoals.SECRET_TAPES_FINAL_LEVEL:
            self.selected_goal_level = level_pool[-1]
            self.selected_levels = level_pool[:-1]
        else:
            self.selected_levels = level_pool[:]

        self.selected_starting_levels = self.selected_levels[:3]

        # Target Scores
        self.score_requirement_mode = id_to_requirement_modes()[self.options.score_requirement_mode.value]
        self.score_requirement_percentage = self.options.score_requirement_percentage.value

        self.include_platinum_scores = bool(self.options.include_platinum_scores.value)

        self.target_scores = dict()
        self.target_score_ratios = dict()

        level: TonyHawksProSkater12Levels
        for level in (self.selected_levels + [self.selected_goal_level]):
            if level is None or level == self.selected_goal_level:
                continue

            self.target_scores[level] = dict()
            self.target_score_ratios[level] = dict()

            skater: TonyHawksProSkater12Skaters
            for skater in self.selected_skaters:
                base_scores: List[int] = level_to_base_scores[level]

                if self.score_requirement_mode == TonyHawksProSkater12APRequirementModes.SAME_FOR_ALL:
                    percentage: int = self.score_requirement_percentage

                    if level_to_level_types[level] == TonyHawksProSkater12LevelTypes.NO_OBJECTIVES:
                        percentage = min(percentage, 200)

                    self.target_score_ratios[level][skater] = round(percentage / 100.0, 2)

                    adjusted_scores: List[int] = [round(int(score * (percentage / 100)), -3) for score in base_scores]
                elif self.score_requirement_mode == TonyHawksProSkater12APRequirementModes.RANDOM:
                    percentage: int = self.random.randint(50, self.score_requirement_percentage)

                    if level_to_level_types[level] == TonyHawksProSkater12LevelTypes.NO_OBJECTIVES:
                        percentage = min(percentage, 200)

                    self.target_score_ratios[level][skater] = round(percentage / 100.0, 2)

                    adjusted_scores: List[int] = [round(int(score * (percentage / 100)), -3) for score in base_scores]
                else:
                    self.target_score_ratios[level][skater] = 1.0

                    adjusted_scores: List[int] = base_scores[:]

                if not self.include_platinum_scores:
                    adjusted_scores[3] = 0

                self.target_scores[level][skater] = adjusted_scores

        # Target Combo Scores
        self.combo_score_requirement_mode = id_to_requirement_modes()[self.options.combo_score_requirement_mode.value]
        self.combo_score_requirement_percentage = self.options.combo_score_requirement_percentage.value

        self.include_platinum_combo_scores = bool(self.options.include_platinum_combo_scores.value)

        self.target_combo_scores = dict()
        self.target_combo_score_ratios = dict()

        level: TonyHawksProSkater12Levels
        for level in (self.selected_levels + [self.selected_goal_level]):
            if level is None or level == self.selected_goal_level:
                continue

            self.target_combo_scores[level] = dict()
            self.target_combo_score_ratios[level] = dict()

            skater: TonyHawksProSkater12Skaters
            for skater in self.selected_skaters:
                base_combo_scores: List[int] = level_to_base_combo_scores[level]

                if self.combo_score_requirement_mode == TonyHawksProSkater12APRequirementModes.SAME_FOR_ALL:
                    percentage: int = self.combo_score_requirement_percentage

                    if level_to_level_types[level] == TonyHawksProSkater12LevelTypes.NO_OBJECTIVES:
                        percentage = min(percentage, 200)

                    self.target_combo_score_ratios[level][skater] = round(percentage / 100.0, 2)

                    adjusted_combo_scores: List[int] = [
                        round(int(score * (percentage / 100)), -3) for score in base_combo_scores
                    ]
                elif self.combo_score_requirement_mode == TonyHawksProSkater12APRequirementModes.RANDOM:
                    percentage: int = self.random.randint(50, self.combo_score_requirement_percentage)

                    if level_to_level_types[level] == TonyHawksProSkater12LevelTypes.NO_OBJECTIVES:
                        percentage = min(percentage, 200)

                    self.target_combo_score_ratios[level][skater] = round(percentage / 100.0, 2)

                    adjusted_combo_scores: List[int] = [
                        round(int(score * (percentage / 100)), -3) for score in base_combo_scores
                    ]
                else:
                    self.target_combo_score_ratios[level][skater] = 1.0

                    adjusted_combo_scores: List[int] = base_combo_scores[:]

                if not self.include_platinum_combo_scores:
                    adjusted_combo_scores[3] = 0

                self.target_combo_scores[level][skater] = adjusted_combo_scores

        # Gaps
        self.include_gaps = bool(self.options.include_gaps.value)
        self.gap_count_per_level = self.options.gap_count_per_level.value

        self.target_gaps = dict()

        if self.include_gaps:
            level: TonyHawksProSkater12Levels
            for level in (self.selected_levels + [self.selected_goal_level]):
                if level is None or level == self.selected_goal_level:
                    continue

                self.target_gaps[level] = dict()

                skater: TonyHawksProSkater12Skaters
                for skater in self.selected_skaters:
                    self.target_gaps[level][skater] = self.random.sample(level_to_gaps[level], self.gap_count_per_level)

        # Long Tricks
        self.include_long_tricks = bool(self.options.include_long_tricks.value)

        self.target_long_tricks = dict()

        if self.include_long_tricks:
            level: TonyHawksProSkater12Levels
            for level in (self.selected_levels + [self.selected_goal_level]):
                if level is None or level == self.selected_goal_level:
                    continue

                self.target_long_tricks[level] = dict()

                skater: TonyHawksProSkater12Skaters
                for skater in self.selected_skaters:
                    # Order is Grind, Lip, Manual
                    self.target_long_tricks[level][skater] = [
                        round(self.random.uniform(4.0, 8.0), 1),
                        round(self.random.uniform(3.0, 7.0), 1),
                        round(self.random.uniform(8.0, 16.0), 1),
                    ]

                    # Exceptions
                    if level == TonyHawksProSkater12Levels.CHOPPER_DROP:
                        self.target_long_tricks[level][skater][0] = round(self.random.uniform(1.0, 3.0), 1)

        # Signature Specials
        self.include_signature_specials = bool(self.options.include_signature_specials.value)

        # Starting Trick Types
        self.starting_trick_type_weights = {
            "Flip Tricks": 1,
            "Grab Tricks": 3,
            "Grind Tricks": 3,
            "Manual Tricks": 2,
            "Lip Tricks": 1,
        }

        self.starting_trick_types = dict()

        trick_type: str
        weight: Any
        for trick_type, weight in self.options.starting_trick_type_weights.value.items():
            if trick_type not in self.starting_trick_type_weights:
                continue

            if isinstance(weight, int) and weight >= 0:
                self.starting_trick_type_weights[trick_type] = weight

        skater: TonyHawksProSkater12Skaters
        for skater in self.selected_skaters:
            trick_types: List[str] = list(self.starting_trick_type_weights.keys())

            weights: List[int] = list()

            weight: Any
            for weight in self.starting_trick_type_weights.values():
                if isinstance(weight, int) and weight >= 0:
                    weights.append(weight)
                else:
                    weights.append(0)

            if sum(weights) == 0:
                weights = [1 for _ in weights]

            self.starting_trick_types[skater] = self.random.choices(trick_types, weights=weights, k=1)[0]

        # Overpowered Abilities
        self.include_overpowered_abilities = bool(self.options.include_overpowered_abilities.value)

        # Traps
        self.trap_percentage = self.options.trap_percentage.value

        self.trap_weights = {
            trap_type: 1 for trap_type in TonyHawksProSkater12APTrapTypes
        }

        trap_type_name: str
        weight: Any
        for trap_type_name, weight in self.options.trap_weights.value.items():
            try:
                trap_type: TonyHawksProSkater12APTrapTypes = TonyHawksProSkater12APTrapTypes(trap_type_name)
            except Exception:
                continue

            if isinstance(weight, int) and weight >= 0:
                self.trap_weights[trap_type] = weight

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

        victory_location: TonyHawksProSkater12Location = TonyHawksProSkater12Location(
            self.player,
            "Victory",
            None,
            region_endgame,
        )

        victory_location.place_locked_item(
            TonyHawksProSkater12Item(
                "Victory",
                ItemClassification.progression,
                None,
                self.player,
            )
        )

        region_endgame.locations.append(victory_location)

        if self.goal == TonyHawksProSkater12APGoals.SECRET_TAPE_HUNT:
            region_menu.connect(
                region_endgame,
                rule=lambda state: state.has("Secret Tape", self.player, self.secret_tapes_required)
            )

            self.multiworld.regions.append(region_endgame)

        allowable_gap_numbers: List[str] = [str(i) for i in range(1, self.gap_count_per_level + 1)]

        # Levels
        level: TonyHawksProSkater12Levels
        for level in (self.selected_levels + [self.selected_goal_level]):
            if level is None:
                continue

            region_level: Region = Region(level.value, self.player, self.multiworld)

            # Level - Skater
            skater: TonyHawksProSkater12Skaters
            for skater in self.selected_skaters:
                region_level_skater: Region = Region(f"{level.value} - {skater.value}", self.player, self.multiworld)

                if level != self.selected_goal_level:
                    level_skater_tag: TonyHawksProSkater12APTags = getattr(
                        TonyHawksProSkater12APTags, f"{level.name}_{skater.name}_LOCATION"
                    )

                    level_skater_location_names: List[str] = locations_with_tag(level_skater_tag)

                    location_name: str
                    for location_name in level_skater_location_names:
                        data: TonyHawksProSkater12LocationData = location_data[location_name]

                        if not self.include_platinum_scores and TonyHawksProSkater12APTags.PLATINUM_SCORE_LOCATION in data.tags:
                            continue

                        if not self.include_platinum_combo_scores and TonyHawksProSkater12APTags.PLATINUM_COMBO_LOCATION in data.tags:
                            continue

                        if not self.include_long_tricks and TonyHawksProSkater12APTags.LONG_GRIND_TRICK_LOCATION in data.tags:
                            continue

                        if not self.include_long_tricks and TonyHawksProSkater12APTags.LONG_LIP_TRICK_LOCATION in data.tags:
                            continue

                        if not self.include_long_tricks and TonyHawksProSkater12APTags.LONG_MANUAL_TRICK_LOCATION in data.tags:
                            continue

                        if not self.include_gaps and TonyHawksProSkater12APTags.GAP_LOCATION in data.tags:
                            continue

                        if TonyHawksProSkater12APTags.GAP_LOCATION in data.tags and location_name.split("#")[-1] not in allowable_gap_numbers:
                            continue

                        location: TonyHawksProSkater12Location = TonyHawksProSkater12Location(
                            self.player,
                            location_name,
                            data.archipelago_id,
                            region_level_skater,
                        )

                        location_access_rule: str = location_access_rule_for(location_name, self.player)

                        if location_access_rule != "lambda state: True":
                            location.access_rule = eval(location_access_rule)

                        region_level_skater.locations.append(location)
                else:
                    if self.goal == TonyHawksProSkater12APGoals.SECRET_TAPES_FINAL_LEVEL:
                        region_level_skater.connect(
                            region_endgame,
                            rule=lambda state: state.has("Secret Tape", self.player, self.secret_tapes_required)
                        )

                region_level.connect(
                    region_level_skater,
                    rule=lambda state, s=skater: state.has(f"Skater Unlock: {s.value}", self.player)
                )

                self.multiworld.regions.append(region_level_skater)

            region_menu.connect(
                region_level,
                rule=lambda state, l=level: state.has(f"Level Unlock: {l.value}", self.player)
            )

            if level == self.selected_goal_level and self.goal == TonyHawksProSkater12APGoals.SECRET_TAPES_FINAL_LEVEL:
                self.multiworld.regions.append(region_endgame)

            self.multiworld.regions.append(region_level)

        # Skaters
        if self.include_signature_specials:
            skater: TonyHawksProSkater12Skaters
            for skater in self.selected_skaters:
                region_skater: Region = Region(skater.value, self.player, self.multiworld)

                skater_tag: TonyHawksProSkater12APTags = getattr(TonyHawksProSkater12APTags, f"{skater.name}_LOCATION")

                location_name: str
                for location_name in locations_with_tags([skater_tag, TonyHawksProSkater12APTags.SIGNATURE_SPECIAL_LOCATION]):
                    data: TonyHawksProSkater12LocationData = location_data[location_name]

                    location: TonyHawksProSkater12Location = TonyHawksProSkater12Location(
                        self.player,
                        location_name,
                        data.archipelago_id,
                        region_skater,
                    )

                    location_access_rule: str = location_access_rule_for(location_name, self.player)

                    if location_access_rule != "lambda state: True":
                        location.access_rule = eval(location_access_rule)

                    region_skater.locations.append(location)

                region_menu.connect(
                    region_skater,
                    rule=lambda state, s=skater: state.has(f"Skater Unlock: {s.value}", self.player)
                )

                self.multiworld.regions.append(region_skater)

    def create_items(self) -> None:
        ## Precollect
        items_to_precollect: List[str] = list()

        # Starting Skater
        items_to_precollect.append(f"Skater Unlock: {self.selected_starting_skater.value}")

        # Starting Levels
        level: TonyHawksProSkater12Levels
        for level in self.selected_starting_levels:
            items_to_precollect.append(f"Level Unlock: {level.value}")

        # Starting Trick Types
        skater: TonyHawksProSkater12Skaters
        trick_type_name: str
        for skater, trick_type_name in self.starting_trick_types.items():
            if trick_type_name == "Flip Tricks":
                items_to_precollect.append(f"Flip Tricks: {skater.value}")
            elif trick_type_name == "Grab Tricks":
                items_to_precollect.append(f"Grab Tricks: {skater.value}")
            elif trick_type_name == "Grind Tricks":
                items_to_precollect.append(f"Progressive Grind Tricks: {skater.value}")
            elif trick_type_name == "Lip Tricks":
                items_to_precollect.append(f"Progressive Lip Tricks: {skater.value}")
            elif trick_type_name == "Manual Tricks":
                items_to_precollect.append(f"Progressive Manual Tricks: {skater.value}")

        ## Item Pool
        item_pool: List[TonyHawksProSkater12Item] = list()

        # Secret Tapes
        i: int
        for i in range(self.secret_tapes_total):
            item: TonyHawksProSkater12Item = self.create_item("Secret Tape")

            if i >= self.secret_tapes_required:
                item.classification = ItemClassification.useful

            item_pool.append(item)

        # Levels
        level: TonyHawksProSkater12Levels
        for level in (self.selected_levels + [self.selected_goal_level]):
            if level is None:
                continue

            location_name: str = f"Level Unlock: {level.value}"

            if location_name in items_to_precollect:
                continue

            item_pool.append(self.create_item(location_name))

        # Skaters + Items
        skater: TonyHawksProSkater12Skaters
        for skater in self.selected_skaters:
            # Unlock
            unlock_item: str = f"Skater Unlock: {skater.value}"

            if unlock_item not in items_to_precollect:
                item_pool.append(self.create_item(unlock_item))

            # Progressive Stats
            i: int
            for i in range(1, 4):
                progressive_stats_item: TonyHawksProSkater12Item = self.create_item(f"Progressive Stats: {skater.value}")

                if i == 3:
                    if not self.include_overpowered_abilities:
                        break

                    progressive_stats_item.classification = ItemClassification.useful

                item_pool.append(progressive_stats_item)

            # Flip Tricks
            flip_tricks_name: str = f"Flip Tricks: {skater.value}"

            if flip_tricks_name not in items_to_precollect:
                item_pool.append(self.create_item(flip_tricks_name))

            # Grab Tricks
            grab_tricks_name: str = f"Grab Tricks: {skater.value}"

            if grab_tricks_name not in items_to_precollect:
                item_pool.append(self.create_item(grab_tricks_name))

            # Progressive Grind Tricks
            progressive_grind_tricks_name: str = f"Progressive Grind Tricks: {skater.value}"

            count: int = 2

            if progressive_grind_tricks_name in items_to_precollect:
                count -= 1

            i: int
            for i in range(1, count + 1):
                progressive_grind_tricks_item: TonyHawksProSkater12Item = self.create_item(progressive_grind_tricks_name)

                if i == count:
                    if not self.include_overpowered_abilities:
                        break

                    progressive_grind_tricks_item.classification = ItemClassification.useful

                item_pool.append(progressive_grind_tricks_item)

            # Progressive Lip Tricks
            progressive_lip_tricks_name: str = f"Progressive Lip Tricks: {skater.value}"

            count: int = 2

            if progressive_lip_tricks_name in items_to_precollect:
                count -= 1

            i: int
            for i in range(1, count + 1):
                progressive_lip_tricks_item: TonyHawksProSkater12Item = self.create_item(progressive_lip_tricks_name)

                if i == count:
                    if not self.include_overpowered_abilities:
                        break

                    progressive_lip_tricks_item.classification = ItemClassification.useful

                item_pool.append(progressive_lip_tricks_item)

            # Progressive Manual Tricks
            progressive_manual_tricks_name: str = f"Progressive Manual Tricks: {skater.value}"

            count: int = 2

            if progressive_manual_tricks_name in items_to_precollect:
                count -= 1

            i: int
            for i in range(1, count + 1):
                progressive_manual_item: TonyHawksProSkater12Item = self.create_item(progressive_manual_tricks_name)

                if i == count:
                    if not self.include_overpowered_abilities:
                        break

                    progressive_manual_item.classification = ItemClassification.useful

                item_pool.append(progressive_manual_item)

            # Progressive Special Meter
            i: int
            for i in range(1, 3):
                progressive_special_meter_item: TonyHawksProSkater12Item = self.create_item(
                    f"Progressive Special Meter: {skater.value}"
                )

                if i == 2:
                    progressive_special_meter_item.classification = ItemClassification.useful

                item_pool.append(progressive_special_meter_item)

            # Spin Tricks
            item_pool.append(self.create_item(f"Spin Tricks: {skater.value}"))

            # Transfers
            item_pool.append(self.create_item(f"Transfers: {skater.value}"))

            # Wallplants
            item_pool.append(self.create_item(f"Wallplants: {skater.value}"))

            # Extra Tricks
            item_pool.append(self.create_item(f"Extra Tricks: {skater.value}"))

            # Stance Switching
            item_pool.append(self.create_item(f"Stance Switching: {skater.value}"))

            # Double Score
            item_pool.append(self.create_item(f"Double Score: {skater.value}"))

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

    def create_item(self, name: str) -> TonyHawksProSkater12Item:
        data: TonyHawksProSkater12ItemData = item_data[name]

        return TonyHawksProSkater12Item(
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
            "secret_tapes_total",
            "secret_tapes_required",
            "skater_selection",
            "skater_count",
            "level_selection",
            "level_count",
            "include_platinum_scores",
            "include_platinum_combo_scores",
            "include_signature_specials",
            "include_long_tricks",
            "include_gaps",
            "gap_count_per_level",
            "score_requirement_mode",
            "score_requirement_percentage",
            "combo_score_requirement_mode",
            "combo_score_requirement_percentage",
            "starting_trick_type_weights",
            "include_overpowered_abilities",
            "trap_percentage",
            "trap_weights",
        )

        slot_data["trap_weights"] = {
            trap_type.value: weight for trap_type, weight in self.trap_weights.items()
        }

        slot_data["selected_skaters"] = [skater.value for skater in self.selected_skaters]
        slot_data["selected_starting_skater"] = self.selected_starting_skater.value

        slot_data["selected_levels"] = [level.value for level in self.selected_levels]
        slot_data["selected_starting_levels"] = [level.value for level in self.selected_starting_levels]
        slot_data["selected_goal_level"] = self.selected_goal_level.value if self.selected_goal_level is not None else None

        slot_data["target_scores"] = dict()

        level: TonyHawksProSkater12Levels
        skater_data: Dict[TonyHawksProSkater12Skaters, List[int]]
        for level, skater_data in self.target_scores.items():
            slot_data["target_scores"][level.value] = dict()

            skater: TonyHawksProSkater12Skaters
            scores: List[int]
            for skater, scores in skater_data.items():
                slot_data["target_scores"][level.value][skater.value] = scores

        slot_data["target_combo_scores"] = dict()

        level: TonyHawksProSkater12Levels
        skater_data: Dict[TonyHawksProSkater12Skaters, List[int]]
        for level, skater_data in self.target_combo_scores.items():
            slot_data["target_combo_scores"][level.value] = dict()

            skater: TonyHawksProSkater12Skaters
            scores: List[int]
            for skater, scores in skater_data.items():
                slot_data["target_combo_scores"][level.value][skater.value] = scores

        slot_data["target_gaps"] = dict()

        level: TonyHawksProSkater12Levels
        skater_data: Dict[TonyHawksProSkater12Skaters, List[int]]
        for level, skater_data in self.target_gaps.items():
            slot_data["target_gaps"][level.value] = dict()

            skater: TonyHawksProSkater12Skaters
            gaps: List[TonyHawksProSkater12Gaps]
            for skater, gaps in skater_data.items():
                slot_data["target_gaps"][level.value][skater.value] = [gap.value for gap in gaps]

        slot_data["target_long_tricks"] = dict()

        level: TonyHawksProSkater12Levels
        skater_data: Dict[TonyHawksProSkater12Skaters, List[float]]
        for level, skater_data in self.target_long_tricks.items():
            slot_data["target_long_tricks"][level.value] = dict()

            skater: TonyHawksProSkater12Skaters
            durations: List[float]
            for skater, durations in skater_data.items():
                slot_data["target_long_tricks"][level.value][skater.value] = durations

        slot_data["starting_trick_types"] = dict()

        for skater, trick_type_name in self.starting_trick_types.items():
            slot_data["starting_trick_types"][skater.value] = trick_type_name

        starting_trick_types: Dict[TonyHawksProSkater12Skaters, str]

        slot_data["target_score_ratios"] = dict()

        level: TonyHawksProSkater12Levels
        skater_data: Dict[TonyHawksProSkater12Skaters, float]
        for level, skater_data in self.target_score_ratios.items():
            slot_data["target_score_ratios"][level.value] = dict()

            skater: TonyHawksProSkater12Skaters
            ratio: float
            for skater, ratio in skater_data.items():
                slot_data["target_score_ratios"][level.value][skater.value] = ratio

        slot_data["target_combo_score_ratios"] = dict()

        level: TonyHawksProSkater12Levels
        skater_data: Dict[TonyHawksProSkater12Skaters, float]
        for level, skater_data in self.target_combo_score_ratios.items():
            slot_data["target_combo_score_ratios"][level.value] = dict()

            skater: TonyHawksProSkater12Skaters
            ratio: float
            for skater, ratio in skater_data.items():
                slot_data["target_combo_score_ratios"][level.value][skater.value] = ratio

        # Relay generate_early Overrides
        if slot_data["secret_tapes_required"] != self.secret_tapes_required:
            slot_data["secret_tapes_required"] = self.secret_tapes_required

        if slot_data["skater_count"] != self.skater_count:
            slot_data["skater_count"] = self.skater_count

        if slot_data["level_count"] != self.level_count:
            slot_data["level_count"] = self.level_count

        if slot_data["starting_trick_type_weights"] != self.starting_trick_type_weights:
            slot_data["starting_trick_type_weights"] = self.starting_trick_type_weights

        return slot_data

    def write_spoiler_header(self, spoiler_handle: TextIO) -> None:
        join_string: str = "\n  "
        nested_join_string: str = "\n    "

        # Skaters
        if len(self.selected_skaters) == 1:
            spoiler_handle.write(f"\nSelected Skater: {self.selected_starting_skater.value}")
        else:
            spoiler_handle.write(f"\nStarting Skater: {self.selected_starting_skater.value}")

            spoiler_handle.write(
                f"\n\nUnlockable Skaters:\n  {join_string.join(sorted([s.value for s in self.selected_skaters[1:]]))}"
            )

        # Levels
        spoiler_handle.write(
            f"\n\nStarting Levels:\n  {join_string.join(sorted([l.value for l in self.selected_starting_levels]))}"
        )

        spoiler_handle.write(
            f"\n\nUnlockable Levels:\n  {join_string.join(sorted([l.value for l in self.selected_levels[3:]]))}"
        )

        if self.selected_goal_level is not None:
            spoiler_handle.write(f"\n\nGoal Level: {self.selected_goal_level.value}")

        # Target Scores
        spoiler_handle.write("\n\nTarget Scores:")

        level: TonyHawksProSkater12Levels
        score_data: Dict[TonyHawksProSkater12Skaters, List[int]]
        for level, score_data in self.target_scores.items():
            spoiler_handle.write(join_string + level.value + ":")

            depth: int = 4 if self.include_platinum_scores else 3

            skater: TonyHawksProSkater12Skaters
            scores: List[int]
            for skater, scores in score_data.items():
                spoiler_handle.write(nested_join_string + f"{skater.value} ({self.target_score_ratios[level][skater]}x): {scores[:depth]}")

        # Target Combo Scores
        spoiler_handle.write("\n\nTarget Combo Scores:")

        level: TonyHawksProSkater12Levels
        combo_score_data: Dict[TonyHawksProSkater12Skaters, List[int]]
        for level, combo_score_data in self.target_combo_scores.items():
            spoiler_handle.write(join_string + level.value + ":")

            depth: int = 4 if self.include_platinum_combo_scores else 3

            skater: TonyHawksProSkater12Skaters
            combo_scores: List[int]
            for skater, combo_scores in combo_score_data.items():
                spoiler_handle.write(nested_join_string + f"{skater.value} ({self.target_combo_score_ratios[level][skater]}x): {combo_scores[:depth]}")

        # Gaps
        if self.include_gaps:
            spoiler_handle.write("\n\nTarget Gaps:")

            level: TonyHawksProSkater12Levels
            gap_data: Dict[TonyHawksProSkater12Skaters, List[TonyHawksProSkater12Gaps]]
            for level, gap_data in self.target_gaps.items():
                spoiler_handle.write(join_string + level.value + ":")

                skater: TonyHawksProSkater12Skaters
                gaps: List[TonyHawksProSkater12Gaps]
                for skater, gaps in gap_data.items():
                    spoiler_handle.write(nested_join_string + f"{skater.value}: {', '.join([gap.value for gap in gaps])}")

        # Long Tricks
        if self.include_long_tricks:
            spoiler_handle.write("\n\nLong Trick Durations (Grind, Lip, Manual):")

            level: TonyHawksProSkater12Levels
            long_trick_data: Dict[TonyHawksProSkater12Levels, Dict[TonyHawksProSkater12Skaters, List[float]]]
            for level, long_trick_data in self.target_long_tricks.items():
                spoiler_handle.write(join_string + level.value + ":")

                skater: TonyHawksProSkater12Skaters
                durations: List[float]
                for skater, durations in long_trick_data.items():
                    spoiler_handle.write(nested_join_string + f"{skater.value}: {durations}")

        # Starting Trick Types
        spoiler_handle.write("\n\nStarting Trick Types:")

        skater: TonyHawksProSkater12Skaters
        for skater in self.selected_skaters:
            spoiler_handle.write(join_string + f"{skater.value}: {self.starting_trick_types[skater]}")

    def get_filler_item_name(self) -> str:
        return self.random.choice(self.filler_item_names)

    @staticmethod
    def interpret_slot_data(slot_data: Dict[str, Any]) -> Dict[str, Any]:
        return process_slot_data(slot_data)

    def _apply_universal_tracker_passthrough(self) -> None:
        if "Tony Hawk's Pro Skater 1 + 2" in self.multiworld.re_gen_passthrough:
            passthrough: Dict[str, Any] = self.multiworld.re_gen_passthrough["Tony Hawk's Pro Skater 1 + 2"]

            self.goal = passthrough["goal"]
            self.secret_tapes_total = passthrough["secret_tapes_total"]
            self.secret_tapes_required = passthrough["secret_tapes_required"]
            self.skater_selection = passthrough["skater_selection"]
            self.skater_count = passthrough["skater_count"]
            self.level_selection = passthrough["level_selection"]
            self.level_count = passthrough["level_count"]
            self.include_platinum_scores = passthrough["include_platinum_scores"]
            self.include_platinum_combo_scores = passthrough["include_platinum_combo_scores"]
            self.include_signature_specials = passthrough["include_signature_specials"]
            self.include_long_tricks = passthrough["include_long_tricks"]
            self.include_gaps = passthrough["include_gaps"]
            self.gap_count_per_level = passthrough["gap_count_per_level"]
            self.score_requirement_mode = passthrough["score_requirement_mode"]
            self.score_requirement_percentage = passthrough["score_requirement_percentage"]
            self.combo_score_requirement_mode = passthrough["combo_score_requirement_mode"]
            self.combo_score_requirement_percentage = passthrough["combo_score_requirement_percentage"]
            self.starting_trick_type_weights = passthrough["starting_trick_type_weights"]
            self.include_overpowered_abilities= passthrough["include_overpowered_abilities"]
            self.trap_percentage = passthrough["trap_percentage"]
            self.trap_weights = passthrough["trap_weights"]

            self.selected_skaters = passthrough["selected_skaters"]
            self.selected_starting_skater = passthrough["selected_starting_skater"]

            self.selected_levels = passthrough["selected_levels"]
            self.selected_starting_levels = passthrough["selected_starting_levels"]
            self.selected_goal_level = passthrough["selected_goal_level"]

            self.target_scores = passthrough["target_scores"]
            self.target_combo_scores = passthrough["target_combo_scores"]

            self.target_gaps = passthrough["target_gaps"]
            self.target_long_tricks = passthrough["target_long_tricks"]

            self.starting_trick_types = passthrough["starting_trick_types"]

            self.target_score_ratios = passthrough["target_score_ratios"]
            self.target_combo_score_ratios = passthrough["target_combo_score_ratios"]

            # Location Aliases
            level: TonyHawksProSkater12Levels
            skater_data: Dict[TonyHawksProSkater12Skaters, List[int]]
            for level, skater_data in self.target_scores.items():
                skater: TonyHawksProSkater12Skaters
                scores: List[int]
                for skater, scores in skater_data.items():
                    location_names_and_scores: List[Tuple[str, int]] = [
                        (f"{level.value} - {skater.value} - High Score", scores[0]),
                        (f"{level.value} - {skater.value} - Pro Score", scores[1]),
                        (f"{level.value} - {skater.value} - Sick Score", scores[2]),
                    ]

                    if self.include_platinum_scores:
                        location_names_and_scores.append((f"{level.value} - {skater.value} - Platinum Score", scores[3]))

                    location_name: str
                    score: int
                    for location_name, score in location_names_and_scores:
                        self.location_id_to_alias[self.location_name_to_id[location_name]] = f"{score:,}"

            level: TonyHawksProSkater12Levels
            skater_data: Dict[TonyHawksProSkater12Skaters, List[int]]
            for level, skater_data in self.target_combo_scores.items():
                skater: TonyHawksProSkater12Skaters
                scores: List[int]
                for skater, scores in skater_data.items():
                    location_names_and_scores: List[Tuple[str, int]] = [
                        (f"{level.value} - {skater.value} - High Combo", scores[0]),
                        (f"{level.value} - {skater.value} - Pro Combo", scores[1]),
                        (f"{level.value} - {skater.value} - Sick Combo", scores[2]),
                    ]

                    if self.include_platinum_combo_scores:
                        location_names_and_scores.append((f"{level.value} - {skater.value} - Platinum Combo", scores[3]))

                    location_name: str
                    score: int
                    for location_name, score in location_names_and_scores:
                        self.location_id_to_alias[self.location_name_to_id[location_name]] = f"{score:,}"

            level: TonyHawksProSkater12Levels
            skater_data: Dict[TonyHawksProSkater12Skaters, List[TonyHawksProSkater12Gaps]]
            for level, skater_data in self.target_long_tricks.items():
                skater: TonyHawksProSkater12Skaters
                durations: List[float]
                for skater, durations in skater_data.items():
                    location_names_and_durations: List[Tuple[str, List[float]]] = [
                        (f"{level.value} - {skater.value} - Long Grind Trick", round(durations[0], 2)),
                        (f"{level.value} - {skater.value} - Long Lip Trick", round(durations[1], 2)),
                        (f"{level.value} - {skater.value} - Long Manual Trick", round(durations[2], 2)),
                    ]

                    location_name: str
                    duration: float
                    for location_name, duration in location_names_and_durations:
                        self.location_id_to_alias[self.location_name_to_id[location_name]] = f"{duration} seconds"

            level: TonyHawksProSkater12Levels
            skater_data: Dict[TonyHawksProSkater12Skaters, str]
            for level, skater_data in self.target_gaps.items():
                skater: TonyHawksProSkater12Skaters
                gaps: List[TonyHawksProSkater12Gaps]
                for skater, gaps in skater_data.items():
                    gap: TonyHawksProSkater12Gaps
                    for i, gap in enumerate(gaps):
                        self.location_id_to_alias[self.location_name_to_id[f"{level.value} - {skater.value} - Gap #{i + 1}"]] = gap.value.split(" (")[0]

    def _generate_filler_trap_item_pool(self, count: int) -> List[str]:
        trap_items_needed: int = round(self.trap_percentage / 100 * count)
        filler_items_needed: int = count - trap_items_needed

        item_pool: List[str] = list()

        if trap_items_needed > 0:
            trap_items: List[TonyHawksProSkater12APTrapTypes] = list(self.trap_weights.keys())
            trap_item_weights: List[int] = list(self.trap_weights.values())

            if sum(trap_item_weights) == 0:
                trap_item_weights = [1 for _ in trap_item_weights]

            item_pool.extend([
                trap_type.value for trap_type in self.random.choices(trap_items, trap_item_weights, k=trap_items_needed)
            ])

        for _ in range(filler_items_needed):
            filler_item_name: str = self.random.choice(self.filler_item_names)

            if self.random.randint(1, 500) == 1:
                filler_item_name = "Rare " + filler_item_name

            item_pool.append(filler_item_name)

        return item_pool

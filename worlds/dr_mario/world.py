import itertools
import logging
import settings

from typing import Any, ClassVar, Dict, List, TextIO, Tuple

from rule_builder.rules import And, AtLeast, Has, HasAny, Or, Rule

from BaseClasses import Item, ItemClassification, Location, Region, Tutorial

from Options import OptionError

from worlds.AutoWorld import WebWorld, World

from .data.game_data import (
    level_to_maximum_logical_garbage_levels,
    level_to_maximum_match_length,
    level_to_maximum_starting_garbage_levels,
    level_to_maximum_virus_count,
    level_to_vanilla_virus_count,
    virus_color_conflicts,
)

from .data.item_data import DrMarioItemData, item_data
from .data.location_data import DrMarioLocationData, location_data

from .data_funcs import (
    id_to_final_level_speeds,
    id_to_goals,
    id_to_speed_up_behaviors,
    item_names_to_id,
    item_groups,
    items_with_tag,
    location_groups,
    location_names_to_id,
    locations_with_tag,
    process_slot_data,
)

from .enums import (
    DrMarioColors,
    DrMarioFinalLevelSpeedOptions,
    DrMarioGoalOptions,
    DrMarioLevels,
    DrMarioMusicTracks,
    DrMarioNesColors,
    DrMarioSpeeds,
    DrMarioSpeedUpBehaviorOptions,
    DrMarioTags,
    DrMarioTrapTypes,
)

from .options import DrMarioOptions, option_groups


class DrMarioItem(Item):
    game = "Dr. Mario"


class DrMarioLocation(Location):
    game = "Dr. Mario"


class DrMarioWebWorld(WebWorld):
    theme: str = "partyTime"

    tutorials: List[Tutorial] = [
        Tutorial(
            "Multiworld Setup Guide",
            "A guide to setting up the Dr. Mario randomizer connected to an Archipelago Multiworld",
            "English",
            "setup_en.md",
            "setup/en",
            ["Serpent.AI"],
        )
    ]

    option_groups = option_groups


class DrMarioSettings(settings.Group):
    class MesenPath(settings.UserFilePath):
        """
        The location of the Mesen you want to auto launch the Dr. Mario ROM with
        """
        is_exe = True
        description = "Mesen Executable"

    class RomFile(settings.UserFilePath):
        """File name of your Dr. Mario ROM"""
        description = "Dr. Mario ROM File"
        copy_to = "Dr. Mario (Japan, USA) (En) (Rev 1).nes"
        md5s = ["a4e02baf4284348c045655b91cb84bde"]

    class RomStart(settings.Bool):
        """
        Set this to true to autostart the Dr. Mario ROM in Mesen when the client opens and Mesen isn't running,
        or to false to never open it automatically.
        """

    mesen_path: MesenPath = MesenPath(None)
    rom_file: RomFile = RomFile(RomFile.copy_to)
    rom_start: RomStart | bool = True


class DrMarioWorld(World):
    """
    Dr. Mario is a falling block puzzle game where Mario, now a doctor, throws two-colored pills into a medicine bottle
    full of viruses. Lining up four of the same color eliminates them, and wiping out every virus in the bottle clears
    the level.
    """

    options_dataclass = DrMarioOptions
    options: DrMarioOptions

    settings_key = "dr_mario_options"
    settings: ClassVar[DrMarioSettings]

    game = "Dr. Mario"

    item_name_to_id = item_names_to_id()
    location_name_to_id = location_names_to_id()

    item_name_groups = item_groups()
    location_name_groups = location_groups()

    required_client_version: Tuple[int, int, int] = (0, 6, 7)

    web = DrMarioWebWorld()

    filler_item_names: List[str] = item_groups()["Filler Item"]

    # Options
    goal: DrMarioGoalOptions
    antiviral_serum_total: int
    antiviral_serum_required: int
    final_level: int
    final_level_speed: DrMarioFinalLevelSpeedOptions
    progressive_level_unlocks: bool
    starting_match_length: int
    starting_garbage_levels: int
    restrict_rotations: bool
    lock_next_pill_preview: bool
    speed_up_behavior: DrMarioSpeedUpBehaviorOptions
    trap_percentage: int
    trap_weights: Dict[DrMarioTrapTypes, int]
    trap_duration: int
    randomize_music: bool
    lock_music_choices: bool
    randomize_mario_color: bool
    mario_color_weights: Dict[DrMarioNesColors, int]
    randomize_virus_colors: bool
    virus_color_weights: Dict[DrMarioNesColors, int]
    randomize_checkerboard_colors: bool
    checkerboard_color_weights: Dict[DrMarioNesColors, int]
    death_link: bool

    # Generation
    selected_levels: List[DrMarioLevels]
    selected_starting_levels: List[DrMarioLevels]
    selected_final_level: DrMarioLevels

    level_to_starting_pill: Dict[DrMarioLevels, str]
    level_to_starting_rotation: Dict[DrMarioLevels, str]
    level_to_starting_garbage_levels: Dict[DrMarioLevels, int]
    level_to_virus_count_delta: Dict[DrMarioLevels, int]

    selected_music_tracks: Dict[DrMarioMusicTracks, DrMarioMusicTracks]
    selected_mario_color: DrMarioNesColors
    selected_virus_colors: Dict[DrMarioColors, DrMarioNesColors]
    level_to_checkerboard_colors: Dict[DrMarioLevels, Dict[DrMarioSpeeds, DrMarioNesColors]]
    selected_splash_checkerboard_color: DrMarioNesColors

    # Universal Tracker
    location_id_to_alias: Dict[int, str]
    ut_can_gen_without_yaml: bool = True
    explicit_indirect_conditions = False
    glitches_item_name: str = "OOL"

    @property
    def is_universal_tracker(self) -> bool:
        return hasattr(self.multiworld, "re_gen_passthrough")

    def generate_early(self) -> None:
        self.goal = id_to_goals()[self.options.goal.value]

        self.antiviral_serum_total = self.options.antiviral_serum_total.value
        self.antiviral_serum_required = self.options.antiviral_serum_required.value

        if self.antiviral_serum_required > self.antiviral_serum_total:
            self.antiviral_serum_required = self.antiviral_serum_total

            logging.warning(
                f"Dr. Mario: {self.player_name} has more required Antiviral Serum than total Antiviral Serum. "
                "Adjusting required Antiviral Serum to match total Antiviral Serum..."
            )

        # Levels
        self.final_level = self.options.final_level.value
        self.final_level_speed = id_to_final_level_speeds()[self.options.final_level_speed.value]
        self.progressive_level_unlocks = bool(self.options.progressive_level_unlocks.value)

        level_pool: List[DrMarioLevels] = list(DrMarioLevels)[:self.final_level + 1]

        self.selected_final_level = level_pool[-1]

        if self.goal == DrMarioGoalOptions.ANTIVIRAL_SERUM_FINAL_LEVEL:
            self.selected_levels = level_pool[:-1]
        else:
            self.selected_levels = level_pool[:]

        if self.progressive_level_unlocks:
            self.selected_starting_levels = level_pool[:3]
        else:
            low_levels: List[DrMarioLevels] = [
                level for level in level_pool[:-1]
                if level_to_maximum_match_length[level] == 7
            ]

            starting_levels: List[DrMarioLevels] = self.random.sample(low_levels, 2)
            starting_levels.append(self.random.choice([level for level in level_pool[:-1] if level not in starting_levels]))

            self.selected_starting_levels = sorted(starting_levels, key=level_pool.index)

        # Level Modifiers
        self.starting_garbage_levels = self.options.starting_garbage_levels.value

        self.level_to_starting_pill = dict()
        self.level_to_starting_rotation = dict()
        self.level_to_starting_garbage_levels = dict()
        self.level_to_virus_count_delta = dict()

        pill_items: List[str] = items_with_tag(DrMarioTags.PILL_ITEM)
        rotation_items: List[str] = items_with_tag(DrMarioTags.ROTATION_ITEM)

        level: DrMarioLevels
        for level in level_pool:
            if level in self.selected_levels:
                level_items: List[str] = items_with_tag(getattr(DrMarioTags, f"{level.name}_ITEM"))
                level_pill_items: List[str] = [
                    item for item in pill_items if item in level_items and sum(color.value in item for color in DrMarioColors) == 2
                ]

                self.level_to_starting_pill[level] = self.random.choice(level_pill_items)
                self.level_to_starting_rotation[level] = self.random.choice([item for item in rotation_items if item in level_items])

            self.level_to_starting_garbage_levels[level] = min(
                self.starting_garbage_levels,
                level_to_maximum_starting_garbage_levels[level],
            )

            if level in (DrMarioLevels.LEVEL_0, DrMarioLevels.LEVEL_1):
                self.level_to_virus_count_delta[level] = 0
            else:
                self.level_to_virus_count_delta[level] = self.random.randint(
                    -4,
                    min(4, level_to_maximum_virus_count[level] - level_to_vanilla_virus_count[level]),
                )

        # Gameplay Options
        self.starting_match_length = self.options.starting_match_length.value
        self.restrict_rotations = bool(self.options.restrict_rotations.value)
        self.lock_next_pill_preview = bool(self.options.lock_next_pill_preview.value)
        self.speed_up_behavior = id_to_speed_up_behaviors()[self.options.speed_up_behavior.value]

        # Traps
        self.trap_percentage = self.options.trap_percentage.value

        self.trap_weights = {
            trap_type: 1 for trap_type in DrMarioTrapTypes
        }

        trap_type_name: str
        weight: Any
        for trap_type_name, weight in self.options.trap_weights.value.items():
            try:
                trap_type: DrMarioTrapTypes = DrMarioTrapTypes(trap_type_name)
            except Exception:
                continue

            if isinstance(weight, int) and weight >= 0:
                self.trap_weights[trap_type] = weight

        self.trap_duration = self.options.trap_duration.value

        # Cosmetic Options
        self.randomize_music = bool(self.options.randomize_music.value)

        music_tracks: List[DrMarioMusicTracks] = [
            DrMarioMusicTracks.CHILL,
            DrMarioMusicTracks.CUTSCENE,
            DrMarioMusicTracks.FEVER,
            DrMarioMusicTracks.LEVEL_TWENTY_LOW_CLEAR,
            DrMarioMusicTracks.OPTIONS,
            DrMarioMusicTracks.TITLE,
            DrMarioMusicTracks.TWO_PLAYER_VICTORY,
        ]

        self.selected_music_tracks = {music_track: music_track for music_track in music_tracks}

        if self.randomize_music:
            shuffled_music_tracks: List[DrMarioMusicTracks] = list(music_tracks)
            self.random.shuffle(shuffled_music_tracks)

            self.selected_music_tracks = dict(zip(music_tracks, shuffled_music_tracks))

        self.lock_music_choices = bool(self.options.lock_music_choices.value)

        nes_color_names: Dict[str, DrMarioNesColors] = {
            color.name.replace("_", " ").title(): color for color in DrMarioNesColors
        }

        self.randomize_mario_color = bool(self.options.randomize_mario_color.value)

        self.mario_color_weights = {
            nes_color_names[color_name]: weight
            for color_name, weight in self.options.mario_color_weights.value.items()
            if color_name in self.options.mario_color_weights.default and isinstance(weight, int) and weight >= 0
        }

        self.selected_mario_color = DrMarioNesColors.YELLOW

        if self.randomize_mario_color:
            if not any(self.mario_color_weights.values()):
                raise OptionError(
                    f"Dr. Mario: {self.player_name} must have at least 1 Mario Color Weight above 0 to randomize "
                    "Mario's color."
                )

            self.selected_mario_color = self.random.choices(
                list(self.mario_color_weights.keys()),
                list(self.mario_color_weights.values()),
            )[0]

        self.randomize_virus_colors = bool(self.options.randomize_virus_colors.value)

        self.virus_color_weights = {
            nes_color_names[color_name]: weight
            for color_name, weight in self.options.virus_color_weights.value.items()
            if color_name in self.options.virus_color_weights.default and isinstance(weight, int) and weight >= 0
        }

        self.selected_virus_colors = {
            DrMarioColors.BLUE: DrMarioNesColors.LIGHT_BLUE,
            DrMarioColors.RED: DrMarioNesColors.MAGENTA,
            DrMarioColors.YELLOW: DrMarioNesColors.LIGHT_YELLOW,
        }

        if self.randomize_virus_colors:
            virus_color_sets: List[Tuple[DrMarioNesColors, ...]] = [
                color_set for color_set in itertools.combinations([nes_color for nes_color, weight in self.virus_color_weights.items() if weight > 0], 3)
                if not any(other_color in virus_color_conflicts[nes_color] for nes_color, other_color in itertools.combinations(color_set, 2))
            ]

            if not len(virus_color_sets):
                raise OptionError(
                    f"Dr. Mario: {self.player_name} must have Virus Color Weights above 0 for at least 3 colors that "
                    "contrast enough with each other to randomize the virus colors."
                )

            virus_color_set: Tuple[DrMarioNesColors, ...] = self.random.choices(
                virus_color_sets,
                [self.virus_color_weights[first_color] * self.virus_color_weights[second_color] * self.virus_color_weights[third_color] for first_color, second_color, third_color in virus_color_sets],
            )[0]

            self.selected_virus_colors = dict(zip(DrMarioColors, self.random.sample(virus_color_set, 3)))

        self.randomize_checkerboard_colors = bool(self.options.randomize_checkerboard_colors.value)

        self.checkerboard_color_weights = {
            nes_color_names[color_name]: weight
            for color_name, weight in self.options.checkerboard_color_weights.value.items()
            if color_name in self.options.checkerboard_color_weights.default and isinstance(weight, int) and weight >= 0
        }

        self.level_to_checkerboard_colors = {
            level: {
                DrMarioSpeeds.HIGH: DrMarioNesColors.GRAY,
                DrMarioSpeeds.LOW: DrMarioNesColors.DARK_GREEN,
                DrMarioSpeeds.MEDIUM: DrMarioNesColors.DARK_VIOLET,
            }
            for level in DrMarioLevels
        }

        self.selected_splash_checkerboard_color = DrMarioNesColors.DARK_GREEN

        if self.randomize_checkerboard_colors:
            if len([weight for weight in self.checkerboard_color_weights.values() if weight > 0]) < 3:
                raise OptionError(
                    f"Dr. Mario: {self.player_name} must have at least 3 Checkerboard Color Weights above 0 to "
                    "randomize the checkerboard colors."
                )

            level: DrMarioLevels
            for level in DrMarioLevels:
                checkerboard_color_pool: Dict[DrMarioNesColors, int] = dict(self.checkerboard_color_weights)

                speed: DrMarioSpeeds
                for speed in DrMarioSpeeds:
                    nes_color: DrMarioNesColors = self.random.choices(
                        list(checkerboard_color_pool.keys()),
                        list(checkerboard_color_pool.values()),
                    )[0]

                    self.level_to_checkerboard_colors[level][speed] = nes_color

                    del checkerboard_color_pool[nes_color]

            self.selected_splash_checkerboard_color = self.random.choices(
                list(self.checkerboard_color_weights.keys()),
                list(self.checkerboard_color_weights.values()),
            )[0]

        self.death_link = bool(self.options.death_link.value)

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
        self.multiworld.regions.append(region_endgame)

        if self.goal == DrMarioGoalOptions.ANTIVIRAL_SERUM_HUNT:
            region_menu.connect(region_endgame, rule=Has("Antiviral Serum", self.antiviral_serum_required))

        # Levels
        pill_items: List[str] = items_with_tag(DrMarioTags.PILL_ITEM)

        type_to_maximum_match_length: Dict[DrMarioTags, int] = {
            DrMarioTags.CHAIN_2_LOCATION: 5,
            DrMarioTags.COLOR_LINE_LOCATION: 4,
            DrMarioTags.MULTI_LINE_2_LOCATION: 5,
            DrMarioTags.MULTI_LINE_3_LOCATION: 4,
        }

        level: DrMarioLevels
        for level in self.selected_levels:
            level_index: int = list(DrMarioLevels).index(level)

            region_level: Region = Region(level.value, self.player, self.multiworld)

            level_items: List[str] = items_with_tag(getattr(DrMarioTags, f"{level.name}_ITEM"))
            level_pill_items: List[str] = [item for item in pill_items if item in level_items]

            color_to_pill_rule: Dict[DrMarioColors, Rule] = {
                color: HasAny(*[item for item in level_pill_items if color.value in item]) for color in DrMarioColors
            }

            level_location_names: List[str] = locations_with_tag(getattr(DrMarioTags, f"{level.name}_LOCATION"))

            location_name: str
            for location_name in level_location_names:
                data: DrMarioLocationData = location_data[location_name]

                if DrMarioTags.LEVEL_CLEAR_MEDIUM_SPEED_LOCATION in data.tags and self.final_level_speed.value < 1:
                    continue

                if DrMarioTags.LEVEL_CLEAR_HIGH_SPEED_LOCATION in data.tags and self.final_level_speed.value < 2:
                    continue

                if DrMarioTags.MULTI_VIRUS_2_LOCATION in data.tags and level_index < 6:
                    continue

                if DrMarioTags.MULTI_LINE_3_LOCATION in data.tags and level_index < 8:
                    continue

                if DrMarioTags.COLOR_LINE_LOCATION in data.tags and level_index < 6:
                    continue

                if DrMarioTags.CHAIN_2_LOCATION in data.tags and level_index < 4:
                    continue

                if DrMarioTags.COLOR_VIRUS_COUNT_2_LOCATION in data.tags and level_index < 1:
                    continue

                if DrMarioTags.COLOR_VIRUS_COUNT_3_LOCATION in data.tags and level_index < 3:
                    continue

                if DrMarioTags.MULTI_VIRUS_3_LOCATION in data.tags and level_index < 12:
                    continue

                location: DrMarioLocation = DrMarioLocation(
                    self.player,
                    location_name,
                    data.archipelago_id,
                    region_level,
                )

                location_rules: List[Rule] = list()
                location_ool_rules: List[Rule] = [Has("OOL")]

                if DrMarioTags.LEVEL_CLEAR_LOCATION in data.tags:
                    location_rules.extend(color_to_pill_rule.values())

                    if DrMarioTags.LEVEL_CLEAR_MEDIUM_SPEED_LOCATION in data.tags:
                        location_rules.append(Has("Progressive Speed Unlock", 1))
                    elif DrMarioTags.LEVEL_CLEAR_HIGH_SPEED_LOCATION in data.tags:
                        location_rules.append(Has("Progressive Speed Unlock", 2))
                elif DrMarioTags.VIRUS_ELIMINATION_QUARTER_LOCATION in data.tags:
                    location_rules.append(AtLeast(2, *color_to_pill_rule.values()))
                elif DrMarioTags.VIRUS_ELIMINATION_HALF_LOCATION in data.tags or DrMarioTags.COLOR_ELIMINATION_LOCATION in data.tags:
                    location_rules.extend(color_to_pill_rule.values())
                elif DrMarioTags.COLOR_LINE_LOCATION in data.tags or DrMarioTags.COLOR_VIRUS_COUNT_LOCATION in data.tags:
                    color: DrMarioColors
                    for color in DrMarioColors:
                        if color.value in location_name:
                            location_rules.append(color_to_pill_rule[color])

                maximum_match_length: int = min(
                    [level_to_maximum_match_length[level]]
                    + [type_to_maximum_match_length[tag] for tag in data.tags if tag in type_to_maximum_match_length]
                )

                location_ool_rules.extend(location_rules)

                location_rules.append(Has("Progressive Match Length Reduction", 7 - maximum_match_length))
                location_ool_rules.append(Has("Progressive Match Length Reduction", max(0, 6 - maximum_match_length)))

                location_rules.append(
                    Has(
                        f"{level.value}: Progressive Starting Garbage Reduction",
                        3 - level_to_maximum_logical_garbage_levels[level],
                    )
                )

                location_ool_rules.append(
                    Has(
                        f"{level.value}: Progressive Starting Garbage Reduction",
                        max(0, 2 - level_to_maximum_logical_garbage_levels[level]),
                    )
                )

                if level_index >= 17:
                    location_rules.append(Has(f"{level.value}: Clockwise Rotation"))
                    location_rules.append(Has(f"{level.value}: Counterclockwise Rotation"))

                    location_ool_rules.append(HasAny(f"{level.value}: Clockwise Rotation", f"{level.value}: Counterclockwise Rotation"))

                is_ool_relaxed: bool = (
                    maximum_match_length < 7
                    or level_to_maximum_logical_garbage_levels[level] < 3
                    or level_index >= 17
                )

                if is_ool_relaxed:
                    self.set_rule(location, Or(And(*location_rules), And(*location_ool_rules)))
                else:
                    self.set_rule(location, And(*location_rules))

                region_level.locations.append(location)

            level_access_rule: Rule

            if self.progressive_level_unlocks:
                level_access_rule = Has("Progressive Level Unlock", level_index - 2)
            else:
                level_access_rule = Has(f"Level Unlock: {level.value}")

            region_menu.connect(region_level, rule=level_access_rule)

            self.multiworld.regions.append(region_level)

        # Final Level
        if self.goal == DrMarioGoalOptions.ANTIVIRAL_SERUM_FINAL_LEVEL:
            region_final_level: Region = Region(self.selected_final_level.value, self.player, self.multiworld)

            region_menu.connect(region_final_level, rule=Has("Antiviral Serum", self.antiviral_serum_required))
            region_final_level.connect(region_endgame, rule=Has("Progressive Speed Unlock", self.final_level_speed.value))

            self.multiworld.regions.append(region_final_level)

    def create_items(self) -> None:
        ## Precollect
        items_to_precollect: List[str] = list()

        # Starting Levels
        if not self.progressive_level_unlocks:
            level: DrMarioLevels
            for level in self.selected_starting_levels:
                items_to_precollect.append(f"Level Unlock: {level.value}")

        # Match Length Reductions
        for _ in range(7 - self.starting_match_length):
            items_to_precollect.append("Progressive Match Length Reduction")

        # Music Unlocks
        if not self.lock_music_choices:
            items_to_precollect.append("Music Unlock: Fever")
            items_to_precollect.append("Music Unlock: Chill")

        # Per-Level Items
        level: DrMarioLevels
        for level in self.selected_levels:
            items_to_precollect.append(self.level_to_starting_pill[level])

            if self.restrict_rotations:
                items_to_precollect.append(self.level_to_starting_rotation[level])
            else:
                items_to_precollect.append(f"{level.value}: Clockwise Rotation")
                items_to_precollect.append(f"{level.value}: Counterclockwise Rotation")

            if not self.lock_next_pill_preview:
                items_to_precollect.append(f"{level.value}: Next Pill Preview")

            for _ in range(3 - self.level_to_starting_garbage_levels[level]):
                items_to_precollect.append(f"{level.value}: Progressive Starting Garbage Reduction")

        # Final Level Items
        pill_items: List[str] = items_with_tag(DrMarioTags.PILL_ITEM)

        if self.goal == DrMarioGoalOptions.ANTIVIRAL_SERUM_FINAL_LEVEL:
            final_level: DrMarioLevels = self.selected_final_level
            final_level_items: List[str] = items_with_tag(getattr(DrMarioTags, f"{final_level.name}_ITEM"))

            items_to_precollect.extend([item for item in pill_items if item in final_level_items])

            items_to_precollect.append(f"{final_level.value}: Clockwise Rotation")
            items_to_precollect.append(f"{final_level.value}: Counterclockwise Rotation")
            items_to_precollect.append(f"{final_level.value}: Next Pill Preview")

            for _ in range(3):
                items_to_precollect.append(f"{final_level.value}: Progressive Starting Garbage Reduction")

        ## Item Pool
        item_pool: List[DrMarioItem] = list()

        # Goal Items
        i: int
        for i in range(self.antiviral_serum_total):
            item: DrMarioItem = self.create_item("Antiviral Serum")

            if i >= self.antiviral_serum_required:
                item.classification = ItemClassification.useful

            item_pool.append(item)

        # Level Unlock Items
        if self.progressive_level_unlocks:
            for _ in range(len(self.selected_levels) - 3):
                item_pool.append(self.create_item("Progressive Level Unlock"))
        else:
            level: DrMarioLevels
            for level in self.selected_levels:
                item_name: str = f"Level Unlock: {level.value}"

                if item_name in items_to_precollect:
                    continue

                item_pool.append(self.create_item(item_name))

        # Speed Unlock Items
        for _ in range(self.final_level_speed.value):
            item_pool.append(self.create_item("Progressive Speed Unlock"))

        # Match Length Reduction Items
        for _ in range(self.starting_match_length - 3):
            item_pool.append(self.create_item("Progressive Match Length Reduction"))

        # Music Unlock Items
        if self.lock_music_choices:
            item_pool.append(self.create_item("Music Unlock: Fever"))
            item_pool.append(self.create_item("Music Unlock: Chill"))

        # Per-Level Items
        level: DrMarioLevels
        for level in self.selected_levels:
            level_items: List[str] = items_with_tag(getattr(DrMarioTags, f"{level.name}_ITEM"))

            item_name: str
            for item_name in [item for item in pill_items if item in level_items]:
                if item_name != self.level_to_starting_pill[level]:
                    item_pool.append(self.create_item(item_name))

            if self.restrict_rotations:
                for item_name in (f"{level.value}: Clockwise Rotation", f"{level.value}: Counterclockwise Rotation"):
                    if item_name != self.level_to_starting_rotation[level]:
                        item_pool.append(self.create_item(item_name))

            if self.lock_next_pill_preview:
                item_pool.append(self.create_item(f"{level.value}: Next Pill Preview"))

            for _ in range(self.level_to_starting_garbage_levels[level]):
                item_pool.append(self.create_item(f"{level.value}: Progressive Starting Garbage Reduction"))

        # Filler / Traps
        total_location_count: int = len(self.multiworld.get_unfilled_locations(self.player))
        to_fill_location_count: int = total_location_count - len(item_pool)

        item_name: str
        for item_name in self._generate_filler_trap_item_pool(to_fill_location_count):
            item_pool.append(self.create_item(item_name))

        self.multiworld.itempool += item_pool

        item_name: str
        for item_name in items_to_precollect:
            self.multiworld.push_precollected(self.create_item(item_name))

    def create_item(self, name: str) -> DrMarioItem:
        data: DrMarioItemData = item_data[name]

        return DrMarioItem(
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
            "antiviral_serum_total",
            "antiviral_serum_required",
            "final_level",
            "final_level_speed",
            "progressive_level_unlocks",
            "starting_match_length",
            "starting_garbage_levels",
            "restrict_rotations",
            "lock_next_pill_preview",
            "speed_up_behavior",
            "trap_percentage",
            "trap_weights",
            "trap_duration",
            "randomize_music",
            "lock_music_choices",
            "randomize_mario_color",
            "randomize_virus_colors",
            "randomize_checkerboard_colors",
            "death_link",
        )

        slot_data["trap_weights"] = {
            trap_type.value: weight for trap_type, weight in self.trap_weights.items()
        }

        slot_data["selected_levels"] = [level.value for level in self.selected_levels]
        slot_data["selected_starting_levels"] = [level.value for level in self.selected_starting_levels]
        slot_data["selected_final_level"] = self.selected_final_level.value

        slot_data["level_to_starting_pill"] = {
            level.value: pill for level, pill in self.level_to_starting_pill.items()
        }

        slot_data["level_to_starting_rotation"] = {
            level.value: rotation for level, rotation in self.level_to_starting_rotation.items()
        }

        slot_data["level_to_starting_garbage_levels"] = {
            level.value: garbage_levels for level, garbage_levels in self.level_to_starting_garbage_levels.items()
        }

        slot_data["level_to_virus_count_delta"] = {
            level.value: delta for level, delta in self.level_to_virus_count_delta.items()
        }

        slot_data["selected_music_tracks"] = {
            music_track.value: selected_music_track.value for music_track, selected_music_track in self.selected_music_tracks.items()
        }

        slot_data["selected_mario_color"] = self.selected_mario_color.value

        slot_data["selected_virus_colors"] = {
            color.value: nes_color.value for color, nes_color in self.selected_virus_colors.items()
        }

        slot_data["level_to_checkerboard_colors"] = {
            level.value: {speed.value: nes_color.value for speed, nes_color in speed_colors.items()}
            for level, speed_colors in self.level_to_checkerboard_colors.items()
        }

        slot_data["selected_splash_checkerboard_color"] = self.selected_splash_checkerboard_color.value

        # Relay generate_early Overrides
        if slot_data["antiviral_serum_required"] != self.antiviral_serum_required:
            slot_data["antiviral_serum_required"] = self.antiviral_serum_required

        return slot_data

    def write_spoiler_header(self, spoiler_handle: TextIO) -> None:
        join_string: str = "\n  "

        # Levels
        spoiler_handle.write(
            f"\n\nStarting Levels:\n  {join_string.join([l.value for l in self.selected_starting_levels])}"
        )

        spoiler_handle.write(
            f"\n\nUnlockable Levels:\n  "
            f"{join_string.join([l.value for l in self.selected_levels if l not in self.selected_starting_levels])}"
        )

        spoiler_handle.write(
            f"\n\nFinal Level: {self.selected_final_level.value} on {self.final_level_speed.name.title()} Speed"
        )

        # Level Modifiers
        spoiler_handle.write(f"\n\nStarting Pills:")

        level: DrMarioLevels
        for level in self.selected_levels:
            spoiler_handle.write(join_string + self.level_to_starting_pill[level])

        if self.restrict_rotations:
            spoiler_handle.write(f"\n\nStarting Rotations:")

            level: DrMarioLevels
            for level in self.selected_levels:
                spoiler_handle.write(join_string + self.level_to_starting_rotation[level])

        if self.starting_garbage_levels > 0:
            spoiler_handle.write(f"\n\nStarting Garbage Levels:")

            level: DrMarioLevels
            garbage_levels: int
            for level, garbage_levels in self.level_to_starting_garbage_levels.items():
                spoiler_handle.write(join_string + f"{level.value}: {garbage_levels}")

        spoiler_handle.write(f"\n\nVirus Counts:")

        level: DrMarioLevels
        delta: int
        for level, delta in self.level_to_virus_count_delta.items():
            spoiler_handle.write(join_string + f"{level.value}: {level_to_vanilla_virus_count[level] + delta} ({delta:+d})")

        # Cosmetics
        if self.randomize_music:
            spoiler_handle.write(f"\n\nMusic:")

            music_track: DrMarioMusicTracks
            selected_music_track: DrMarioMusicTracks
            for music_track, selected_music_track in self.selected_music_tracks.items():
                spoiler_handle.write(join_string + f"{music_track.value}: {selected_music_track.value}")

        if self.randomize_mario_color:
            spoiler_handle.write(f"\n\nMario Color: {self.selected_mario_color.name.replace('_', ' ').title()}")

        if self.randomize_virus_colors:
            spoiler_handle.write(f"\n\nVirus Colors:")

            color: DrMarioColors
            nes_color: DrMarioNesColors
            for color, nes_color in self.selected_virus_colors.items():
                spoiler_handle.write(join_string + f"{color.value}: {nes_color.name.replace('_', ' ').title()}")

        if self.randomize_checkerboard_colors:
            spoiler_handle.write(f"\n\nCheckerboard Colors:")
            spoiler_handle.write(join_string + f"Splash: {self.selected_splash_checkerboard_color.name.replace('_', ' ').title()}")

            level: DrMarioLevels
            for level in self.selected_levels:
                speed_colors: str = ", ".join(
                    f"{speed.value} {nes_color.name.replace('_', ' ').title()}" for speed, nes_color in self.level_to_checkerboard_colors[level].items()
                )

                spoiler_handle.write(join_string + f"{level.value}: {speed_colors}")

        spoiler_handle.write("\n")

    def get_filler_item_name(self) -> str:
        return self.random.choice(self.filler_item_names)

    @staticmethod
    def interpret_slot_data(slot_data: Dict[str, Any]) -> Dict[str, Any]:
        return process_slot_data(slot_data)

    def _apply_universal_tracker_passthrough(self) -> None:
        if "Dr. Mario" in self.multiworld.re_gen_passthrough:
            passthrough: Dict[str, Any] = self.multiworld.re_gen_passthrough["Dr. Mario"]

            self.goal = passthrough["goal"]
            self.antiviral_serum_total = passthrough["antiviral_serum_total"]
            self.antiviral_serum_required = passthrough["antiviral_serum_required"]
            self.final_level = passthrough["final_level"]
            self.final_level_speed = passthrough["final_level_speed"]
            self.progressive_level_unlocks = passthrough["progressive_level_unlocks"]
            self.starting_match_length = passthrough["starting_match_length"]
            self.starting_garbage_levels = passthrough["starting_garbage_levels"]
            self.restrict_rotations = passthrough["restrict_rotations"]
            self.lock_next_pill_preview = passthrough["lock_next_pill_preview"]
            self.speed_up_behavior = passthrough["speed_up_behavior"]
            self.trap_percentage = passthrough["trap_percentage"]
            self.trap_weights = passthrough["trap_weights"]
            self.trap_duration = passthrough["trap_duration"]
            self.randomize_music = passthrough["randomize_music"]
            self.lock_music_choices = passthrough["lock_music_choices"]
            self.randomize_mario_color = passthrough["randomize_mario_color"]
            self.randomize_virus_colors = passthrough["randomize_virus_colors"]
            self.randomize_checkerboard_colors = passthrough["randomize_checkerboard_colors"]
            self.death_link = passthrough["death_link"]

            self.selected_levels = passthrough["selected_levels"]
            self.selected_starting_levels = passthrough["selected_starting_levels"]
            self.selected_final_level = passthrough["selected_final_level"]

            self.level_to_starting_pill = passthrough["level_to_starting_pill"]
            self.level_to_starting_rotation = passthrough["level_to_starting_rotation"]
            self.level_to_starting_garbage_levels = passthrough["level_to_starting_garbage_levels"]
            self.level_to_virus_count_delta = passthrough["level_to_virus_count_delta"]

            self.selected_music_tracks = passthrough["selected_music_tracks"]
            self.selected_mario_color = passthrough["selected_mario_color"]
            self.selected_virus_colors = passthrough["selected_virus_colors"]
            self.level_to_checkerboard_colors = passthrough["level_to_checkerboard_colors"]
            self.selected_splash_checkerboard_color = passthrough["selected_splash_checkerboard_color"]

            # Location Aliases
            if self.randomize_virus_colors:
                level: DrMarioLevels
                for level in self.selected_levels:
                    color: DrMarioColors
                    nes_color: DrMarioNesColors
                    for color, nes_color in self.selected_virus_colors.items():
                        nes_color_name: str = nes_color.name.replace("_", " ").title()

                        self.location_id_to_alias[
                            self.location_name_to_id[f"{level.value} - Eliminate All {color.value} Viruses"]
                        ] = nes_color_name

                        self.location_id_to_alias[
                            self.location_name_to_id[f"{level.value} - Clear 2 {color.value} Lines with One Pill"]
                        ] = nes_color_name

                        count: int
                        for count in range(1, 4):
                            self.location_id_to_alias[
                                self.location_name_to_id[f"{level.value} - Eliminate {count} {color.value} {'Virus' if count == 1 else 'Viruses'}"]
                            ] = nes_color_name

    def _generate_filler_trap_item_pool(self, count: int) -> List[str]:
        trap_items_needed: int = round(self.trap_percentage / 100 * count)
        filler_items_needed: int = count - trap_items_needed

        item_pool: List[str] = list()

        if trap_items_needed > 0:
            trap_items: List[DrMarioTrapTypes] = list(self.trap_weights.keys())
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

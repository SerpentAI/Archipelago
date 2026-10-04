from typing import List

from dataclasses import dataclass

from Options import (
    Choice,
    DeathLinkMixin,
    DefaultOnToggle,
    OptionDict,
    OptionGroup,
    PerGameCommonOptions,
    Range,
    StartInventoryPool,
    Toggle,
)

from .enums import DrMarioNesColors, DrMarioTrapTypes


class Goal(Choice):
    """
    Determines the victory condition.

    Antiviral Serum + Final Level: Collect enough Antiviral Serum to unlock a Final Level and clear it.
    Antiviral Serum Hunt: Collect a set amount of Antiviral Serum spread across the multiworld.
    """

    display_name = "Goal"

    option_antiviral_serum_final_level = 0
    option_antiviral_serum_hunt = 1

    default = 0


class AntiviralSerumTotal(Range):
    """
    Determines how much Antiviral Serum is in the item pool.
    """

    display_name = "Antiviral Serum Total"

    range_start = 1
    range_end = 20

    default = 20


class AntiviralSerumRequired(Range):
    """
    Determines how much Antiviral Serum is required to either win or unlock the final level.

    If this number is higher than the total amount of Antiviral Serum, it will be set to that number instead.
    """

    display_name = "Antiviral Serum Required"

    range_start = 1
    range_end = 20

    default = 15


class FinalLevel(Range):
    """
    Determines your final level.

    No higher level will be included. With the Antiviral Serum + Final Level goal, clearing it wins the game.
    """

    display_name = "Final Level"

    range_start = 10
    range_end = 20

    default = 12


class FinalLevelSpeed(Choice):
    """
    Determines the speed your final level must be cleared on.

    Level clear locations will be added for every speed up to this one.
    """

    display_name = "Final Level Speed"

    option_low = 0
    option_medium = 1
    option_high = 2

    default = 1


class ProgressiveLevelUnlocks(DefaultOnToggle):
    """
    If enabled, you start with Level 0, Level 1 and Level 2, and the levels up to your final level are unlocked in order with Progressive Level Unlock items.

    If disabled, you start with 3 random levels below your final level, and each other level is unlocked by its own Level Unlock item.
    """

    display_name = "Progressive Level Unlocks"


class StartingMatchLength(Range):
    """
    Determines how many viruses and pill halves of the same color must line up to clear them at the start.

    Progressive Match Length Reduction items will be added to the item pool to bring it down to 3.

    4 is vanilla.
    """

    display_name = "Starting Match Length"

    range_start = 3
    range_end = 7

    default = 4


class StartingGarbageLevels(Range):
    """
    Determines how many levels of garbage a level starts with. Each garbage level drops 4 half pills of 2-player garbage. Higher levels start with progressively fewer garbage levels to keep them possible.

    Progressive Starting Garbage Reduction items for each level will be added to the item pool to bring it down to 0.
    """

    display_name = "Starting Garbage Levels"

    range_start = 0
    range_end = 3

    default = 0


class RestrictRotations(Toggle):
    """
    If enabled, levels start with only one random rotation direction.

    The Clockwise Rotation or Counterclockwise Rotation item for the other direction of each level will be added to the item pool.
    """

    display_name = "Restrict Rotations"


class LockNextPillPreview(Toggle):
    """
    If enabled, levels start with the next pill preview hidden.

    A Next Pill Preview item for each level will be added to the item pool.
    """

    display_name = "Lock Next Pill Preview"


class SpeedUpBehavior(Choice):
    """
    Determines how pills speed up during a level.

    Vanilla: Pills fall faster every 10 pills, up to a maximum speed.
    Disabled: Pills keep the same fall speed for the whole level.
    """

    display_name = "Speed Up Behavior"

    option_vanilla = 0
    option_disabled = 1

    default = 0


class TrapPercentage(Range):
    """
    Determines what percentage of filler items will get converted to trap items.

    Trap Items are made up of the following types:
    - Board Effects (Contagion, Garbage, Mutation, :))
    - Control Effects (Reverse Control)
    - Visual Effects (Grayscale)
    """

    display_name = "Trap Percentage"

    range_start = 0
    range_end = 100

    default = 0


class TrapWeights(OptionDict):
    """
    Determines the relative weights of each Trap Type if Trap Percentage is greater than 0.

    Each weight is required to be zero or more.
    """

    display_name = "Trap Weights"

    default = {trap_type.value: 1 for trap_type in DrMarioTrapTypes}


class TrapDuration(Range):
    """
    Determines how long each trap that isn't instant will last (in seconds).
    """

    display_name = "Trap Duration"

    range_start = 5
    range_end = 30

    default = 10


class RandomizeMusic(Toggle):
    """
    If enabled, the songs of the game are shuffled.
    """

    display_name = "Randomize Music"


class LockMusicChoices(Toggle):
    """
    If enabled, you start with only the Off music choice.

    Music Unlock items for Fever and Chill will be added to the item pool.
    """

    display_name = "Lock Music Choices"


class RandomizeMarioColor(Toggle):
    """
    If enabled, Mario's color will be picked using the Mario Color Weights.
    """

    display_name = "Randomize Mario Color"


class MarioColorWeights(OptionDict):
    """
    Determines the relative weights of each NES color when picking Mario's color.

    Each weight is required to be zero or more, and at least one needs to be more than zero.

    Only applies if Randomize Mario Color is enabled.
    """

    display_name = "Mario Color Weights"

    default = {
        color.name.replace("_", " ").title(): int(color == DrMarioNesColors.YELLOW)
        for color in DrMarioNesColors
        if 0x10 <= color.value <= 0x1C
    }


class RandomizeVirusColors(Toggle):
    """
    If enabled, the 3 virus colors will be picked using the Virus Color Weights.
    """

    display_name = "Randomize Virus Colors"


class VirusColorWeights(OptionDict):
    """
    Determines the relative weights of each NES color when picking the 3 virus colors. Only colors that contrast enough with each other are picked together.

    Each weight is required to be zero or more, and at least three colors that contrast enough with each other need to be more than zero.

    Only applies if Randomize Virus Colors is enabled.
    """

    display_name = "Virus Color Weights"

    default = {
        color.name.replace("_", " ").title(): int(color in (DrMarioNesColors.LIGHT_BLUE, DrMarioNesColors.LIGHT_YELLOW, DrMarioNesColors.MAGENTA))
        for color in DrMarioNesColors
        if 0x11 <= color.value <= 0x2C and 0x1 <= color.value & 0x0F <= 0xC
    }


class RandomizeCheckerboardColors(Toggle):
    """
    If enabled, the checkerboard color of each level and speed will be picked using the Checkerboard Color Weights.
    """

    display_name = "Randomize Checkerboard Colors"


class CheckerboardColorWeights(OptionDict):
    """
    Determines the relative weights of each NES color when picking the checkerboard color of each level and speed.

    Each weight is required to be zero or more, and at least three need to be more than zero.

    Only applies if Randomize Checkerboard Colors is enabled.
    """

    display_name = "Checkerboard Color Weights"

    default = {
        color.name.replace("_", " ").title(): int(color in (DrMarioNesColors.DARK_GREEN, DrMarioNesColors.DARK_VIOLET, DrMarioNesColors.GRAY))
        for color in DrMarioNesColors
        if color.value <= 0x0C
    }


@dataclass
class DrMarioOptions(PerGameCommonOptions, DeathLinkMixin):
    start_inventory_from_pool: StartInventoryPool
    goal: Goal
    antiviral_serum_total: AntiviralSerumTotal
    antiviral_serum_required: AntiviralSerumRequired
    final_level: FinalLevel
    final_level_speed: FinalLevelSpeed
    progressive_level_unlocks: ProgressiveLevelUnlocks
    starting_match_length: StartingMatchLength
    starting_garbage_levels: StartingGarbageLevels
    restrict_rotations: RestrictRotations
    lock_next_pill_preview: LockNextPillPreview
    speed_up_behavior: SpeedUpBehavior
    trap_percentage: TrapPercentage
    trap_weights: TrapWeights
    trap_duration: TrapDuration
    randomize_music: RandomizeMusic
    lock_music_choices: LockMusicChoices
    randomize_mario_color: RandomizeMarioColor
    mario_color_weights: MarioColorWeights
    randomize_virus_colors: RandomizeVirusColors
    virus_color_weights: VirusColorWeights
    randomize_checkerboard_colors: RandomizeCheckerboardColors
    checkerboard_color_weights: CheckerboardColorWeights


option_groups: List[OptionGroup] = [
    OptionGroup(
        "Goal Options",
        [
            Goal,
            AntiviralSerumTotal,
            AntiviralSerumRequired,
        ],
    ),
    OptionGroup(
        "Level Options",
        [
            FinalLevel,
            FinalLevelSpeed,
            ProgressiveLevelUnlocks,
        ],
    ),
    OptionGroup(
        "Gameplay Options",
        [
            StartingMatchLength,
            StartingGarbageLevels,
            RestrictRotations,
            LockNextPillPreview,
            SpeedUpBehavior,
        ],
    ),
    OptionGroup(
        "Trap Options",
        [
            TrapPercentage,
            TrapWeights,
            TrapDuration,
        ],
    ),
    OptionGroup(
        "Cosmetic Options",
        [
            RandomizeMusic,
            LockMusicChoices,
            RandomizeMarioColor,
            MarioColorWeights,
            RandomizeVirusColors,
            VirusColorWeights,
            RandomizeCheckerboardColors,
            CheckerboardColorWeights,
        ],
    ),
]

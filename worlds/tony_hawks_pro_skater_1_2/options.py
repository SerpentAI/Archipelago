from typing import Dict, List

from dataclasses import dataclass

from Options import (
    Choice,
    DefaultOnToggle,
    OptionDict,
    OptionGroup,
    PerGameCommonOptions,
    Range,
    StartInventoryPool,
    Toggle,
)

from .enums import TonyHawksProSkater12Levels, TonyHawksProSkater12Skaters, TonyHawksProSkater12APTrapTypes


class Goal(Choice):
    """
    Determines the victory condition.

    Secret Tapes + Final Level: Collect enough Secret Tapes to unlock a Final Level and score 1 Million Points on it.
    Secret Tape Hunt: Collect a set number of Secret Tapes spread across the multiworld.
    """
    display_name = "Goal"

    option_secret_tapes_final_level = 0
    option_secret_tape_hunt = 1

    default = 0


class SecretTapesTotal(Range):
    """
    Determines how many Secret Tapes are in the item pool.
    """

    display_name = "Secret Tapes Total"

    range_start = 1
    range_end = 50

    default = 20


class SecretTapesRequired(Range):
    """
    Determines how many Secret Tapes are required to either win or unlock the final level.

    If this number is higher than the total number of Secret Tapes, it will be set to that number instead.
    """

    display_name = "Secret Tapes Required"

    range_start = 1
    range_end = 50

    default = 15


class SkaterSelection(OptionDict):
    """
    Determines which Skaters can be considered for inclusion in the multiworld.

    Set any Skater you don't want to possibly play as to false.

    At least one Skater needs to be selected to play this implementation.
    """

    display_name = "Skater Selection"

    skaters: Dict[TonyHawksProSkater12Skaters, bool] = dict()

    skater: TonyHawksProSkater12Skaters
    for skater in TonyHawksProSkater12Skaters:
        if skater in [TonyHawksProSkater12Skaters.OFFICER_DICK, TonyHawksProSkater12Skaters.ROSWELL_ALIEN]:
            skaters[skater] = False
            continue

        skaters[skater] = True

    valid_keys = {skater.value: value for skater, value in skaters.items()}

    default = valid_keys


class SkaterCount(Range):
    """
    Determines how many Skaters will be picked from your selection for inclusion in the multiworld.

    Every Skater will have their own location checks on every level, as well as their own item progression.
    Make sure your selection is adequate for the desired game length.

    If this number is higher than the size of your Skater selection, it will be set to that number instead.
    """

    display_name = "Skater Count"

    range_start = 1
    range_end = 14

    default = 1


class LevelSelection(OptionDict):
    """
    Determines which Levels can be considered for inclusion in the multiworld.

    Set any Level you don't want to possibly play as to false.

    A minimum of 8 Levels needs to be selected to play this implementation.
    """

    display_name = "Level Selection"

    levels: Dict[TonyHawksProSkater12Levels, bool] = dict()

    level: TonyHawksProSkater12Levels
    for level in TonyHawksProSkater12Levels:
        if level in [TonyHawksProSkater12Levels.CHOPPER_DROP, TonyHawksProSkater12Levels.SKATE_HEAVEN]:
            levels[level] = False
            continue

        levels[level] = True

    valid_keys = {level.value: value for level, value in levels.items()}

    default = valid_keys


class LevelCount(Range):
    """
    Determines how many Levels will be picked for inclusion in the multiworld.

    If this number is higher than the size of your Level selection, it will be set to that number instead.
    """

    display_name = "Level Count"

    range_start = 8
    range_end = 19

    default = 8


class IncludePlatinumScores(Toggle):
    """
    If enabled, locations for Platinum Scores on each level will be created when generating the multiworld.
    """

    display_name = "Include Platinum Scores"


class IncludePlatinumComboScores(Toggle):
    """
    If enabled, locations for Platinum Combo Scores on each level will be created when generating the multiworld.
    """

    display_name = "Include Platinum Combo Scores"


class IncludeSignatureSpecials(Toggle):
    """
    If enabled, locations for landing each of the 3 Signature Specials for each included Skater will be created when generating the multiworld.
    """

    display_name = "Include Signature Specials"


class IncludeLongTricks(Toggle):
    """
    If enabled, locations for landing a set of random long grinds, lips and manuals on each level will be created when generating the multiworld.
    """

    display_name = "Include Long Tricks"


class IncludeGaps(Toggle):
    """
    If enabled, locations for landing a set number of random Gaps on each level will be created when generating the multiworld.
    """

    display_name = "Include Gaps"


class GapCountPerLevel(Range):
    """
    Determines how many random Gaps will be selected for each level to have locations for, if Gaps are included.
    """

    display_name = "Gap Count Per Level"

    range_start = 1
    range_end = 5

    default = 3


class ScoreRequirementMode(Choice):
    """
    Determines how Score requirements are set.

    Same for All Levels: A single percentage will be applied to the Score requirements of all levels
    Random per Level: Each level will have a random percentage applied to its Score requirements
    """

    display_name = "Score Requirement Mode"

    option_same_for_all_levels: int = 0
    option_random_per_level: int = 1

    default = 0


class ScoreRequirementPercentage(Range):
    """
    Determines the percentage to apply Score requirements. You will not unlock location checks until
    you reach or exceed the Score requirements on a given level.

    When the requirement mode is set to random per level, the specified percentage will act as the maximum possible.
    """

    display_name = "Score Requirement Percentage"

    range_start = 50
    range_end = 1000

    default = 100


class ComboScoreRequirementMode(Choice):
    """
    Determines how Combo Score requirements are set.

    Same for All Levels: A single percentage will be applied to the Combo Score requirements of all levels
    Random per Level: Each level will have a random percentage applied to its Combo Score requirements
    """

    display_name = "Combo Score Requirement Mode"

    option_same_for_all_levels: int = 0
    option_random_per_level: int = 1

    default = 0


class ComboScoreRequirementPercentage(Range):
    """
    Determines the percentage to apply Combo Score requirements. You will not unlock location checks until
    you reach or exceed the Combo Score requirements on a given level.

    When the requirement mode is set to random per level, the specified percentage will act as the maximum possible.
    """

    display_name = "Combo Score Requirement Percentage"

    range_start = 50
    range_end = 1000

    default = 100


class StartingTrickTypeWeights(OptionDict):
    """
    Determines the relative weights of each starting trick type for a given Skater.

    At least one weight needs to be 1 or more.
    """

    display_name = "Starting Trick Type Weights"

    default = {
        "Flip Tricks": 1,
        "Grab Tricks": 3,
        "Grind Tricks": 3,
        "Manual Tricks": 2,
        "Lip Tricks": 1,
    }


class IncludeOverpoweredAbilities(DefaultOnToggle):
    """
    If enabled, items for abilities that could be considered overpowered will be added to the pool.

    Progressive Grind Tricks gets another tier that grants perfect balance.
    Progressive Lip Tricks gets another tier that grants perfect balance.
    Progressive Manual Tricks gets another tier that grants perfect balance.
    Progressive Stats gets another tier that prevents the skater from ever bailing.
    """

    display_name = "Include Overpowered Abilities"


class TrapPercentage(Range):
    """
      Determines what percentage of filler items will get converted to trap items.

      Trap Items are made up of the following types:
      - Post-Processing Effects (Black and White, Bloom, Chromatic, Color Inversion, Mobile Game, Retro, Tunnel Vision)
      - Skater Model Effects (Giant, Tiny, Wide)
      - Physics Effects (High Gravity, Low Gravity, Super Speed)
      - Control Effects (Reverse Directional Controls)
    """

    display_name = "Trap Percentage"

    range_start = 0
    range_end = 100

    default = 0


class TrapWeights(OptionDict):
    """
    Determines the relative weights of each Trap Type, if Trap Percentage is greater than 0.

    Each weight is required to be zero or more.
    """

    display_name = "Trap Weights"

    default = {trap_type.value: 1 for trap_type in TonyHawksProSkater12APTrapTypes}


@dataclass
class TonyHawksProSkater12Options(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    goal: Goal
    secret_tapes_total: SecretTapesTotal
    secret_tapes_required: SecretTapesRequired
    skater_selection: SkaterSelection
    skater_count: SkaterCount
    level_selection: LevelSelection
    level_count: LevelCount
    include_platinum_scores: IncludePlatinumScores
    include_platinum_combo_scores: IncludePlatinumComboScores
    include_signature_specials: IncludeSignatureSpecials
    include_long_tricks: IncludeLongTricks
    include_gaps: IncludeGaps
    gap_count_per_level: GapCountPerLevel
    score_requirement_mode: ScoreRequirementMode
    score_requirement_percentage: ScoreRequirementPercentage
    combo_score_requirement_mode: ComboScoreRequirementMode
    combo_score_requirement_percentage: ComboScoreRequirementPercentage
    starting_trick_type_weights: StartingTrickTypeWeights
    include_overpowered_abilities: IncludeOverpoweredAbilities
    trap_percentage: TrapPercentage
    trap_weights: TrapWeights


option_groups: List[OptionGroup] = [
    OptionGroup(
        "Goal Options",
        [
            Goal,
            SecretTapesTotal,
            SecretTapesRequired,
        ],
    ),
    OptionGroup(
        "Skater Options",
        [
            SkaterSelection,
            SkaterCount,
        ],
    ),
    OptionGroup(
        "Level Options",
        [
            LevelSelection,
            LevelCount,
        ],
    ),
    OptionGroup(
        "Location Options",
        [
            IncludePlatinumScores,
            IncludePlatinumComboScores,
            IncludeSignatureSpecials,
            IncludeLongTricks,
            IncludeGaps,
            GapCountPerLevel,
        ],
    ),
    OptionGroup(
        "Score Requirement Options",
        [
            ScoreRequirementMode,
            ScoreRequirementPercentage,
            ComboScoreRequirementMode,
            ComboScoreRequirementPercentage,
        ],
    ),
    OptionGroup(
        "Gameplay Options",
        [
            StartingTrickTypeWeights,
            IncludeOverpoweredAbilities,
        ],
    ),
    OptionGroup(
        "Trap Options",
        [
            TrapPercentage,
            TrapWeights,
        ],
    ),
]

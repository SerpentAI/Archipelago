from typing import List

from dataclasses import dataclass

from Options import (
    Choice,
    OptionDict,
    OptionGroup,
    PerGameCommonOptions,
    Range,
    StartInventoryPool,
    Toggle,
)

from .data_funcs import generate_dlc_table_strings
from .enums import PinballFXAPTrapTypes


class Goal(Choice):
    """
    Determines the victory condition.

    Shiny Quarters + Final Table: Collect enough Shiny Quarters to unlock a Final Table and get a classic mode high score on it.
    Shiny Quarter Hunt: Collect a set number of Shiny Quarters spread across the multiworld.
    """
    display_name = "Goal"

    option_shiny_quarters_final_table: int = 0
    option_shiny_quarter_hunt: int = 1

    default = 0


class ShinyQuartersTotal(Range):
    """
    Determines how many Shiny Quarters are in the item pool.

    This number will not be allowed to go over 2 * (number of pinball tables) and will be clamped accordingly if so.
    """

    display_name = "Shiny Quarters Total"

    range_start = 1
    range_end = 100

    default = 20


class ShinyQuartersRequired(Range):
    """
    Determines how many Shiny Quarters are required to either win or unlock the final table.

    If this number is higher than the total number of Shiny Quarters, it will be set to that number instead.
    """

    display_name = "Shiny Quarters Required"

    range_start = 1
    range_end = 100

    default = 15


class PinballTableSelection(OptionDict):
    """
    Determines which Pinball Tables can be considered for inclusion in the multiworld.

    Set any table you don't own (or don't want to play) for Pinball FX to false.

    A minimum of 6 Pinball Tables must be selected to play this implementation.
    """

    display_name = "Pinball Table Selection"

    valid_keys = {string: True for string in generate_dlc_table_strings()}

    default = valid_keys


class PinballTableCount(Range):
    """
    Determines how many Pinball Tables will be picked from your table selection for inclusion in the multiworld.

    If this number is higher than the size of your Pinball Table selection, it will be set to that number instead.

    Note: Setting this value below 10 could extremely rarely lead to generation failures when paired with other
          restrictive options.
    """

    display_name = "Pinball Table Count"

    range_start = 6
    range_end = 140

    default = 10


class IncludeVeryHighTierScores(Toggle):
    """
    If enabled, locations for Very High-Tier Target Scores will be created when generating the multiworld.

    Enabling this option will add more locations, but will also place additional player skill expectations on you.
    """

    display_name = "Include Very High-Tier Scores"


class IncludeOneBallChallenges(Toggle):
    """
    If enabled, locations for 1 Ball Challenges will be created when generating the multiworld.
    By default, only Classic Mode and Time Challenge locations are included when generating.

    Items to unlock the 1 Ball Challenge for each table will be added to the item pool.
    """

    display_name = "Include 1 Ball Challenges"


class IncludeFlipsChallenges(Toggle):
    """
    If enabled, locations for Flips Challenges will be created when generating the multiworld.
    By default, only Classic Mode and Time Challenge locations are included when generating.

    Items to unlock the Flips Challenge for each table will be added to the item pool.
    """

    display_name = "Include Flips Challenges"


class IncludeDistanceChallenges(Toggle):
    """
    If enabled, locations for Distance Challenges will be created when generating the multiworld.
    By default, only Classic Mode and Time Challenge locations are included when generating.

    Items to unlock the Distance Challenge for each table will be added to the item pool.
    """

    display_name = "Include 1 Ball Challenges"


class TargetScoreRequirementMode(Choice):
    """
    Determines how Target Score requirements are set.

    Same for All Tables: A single percentage will be applied to the Target Scores of all tables
    Random per Table: Each table will have a random percentage applied to its Target Scores
    """

    display_name = "Target Score Requirement Mode"

    option_same_for_all_tables: int = 0
    option_random_per_table: int = 1

    default = 0


class TargetScoreRequirementPercentage(Range):
    """
    Determines the percentage to apply Target Scores. You will not unlock location checks until
    you reach or exceed the Target Scores on a given table.

    When the requirement mode is set to random per table, the specified percentage will act as the maximum possible.

    The Pinball FX Archipelago client will display the expected scores for each table under the Pinball FX tab.

    WARNING: Values over 100 are intended for players experienced with scoring high on various pinball tables.
             More casual players may never be able to reach the resulting Target Scores. Be advised.
    """

    display_name = "Target Score Requirement Percentage"

    range_start = 50
    range_end = 400

    default = 100


class UsefulItemPercentage(Range):
    """
    Determines what percentage of filler items will get converted to useful items.

    Useful items are (per mode / challenge type): Target Score Discount, Target Score Multiplier

    These will make the game slightly easier, but are also table-specific for balance purposes.

    The Pinball FX Archipelago client will display the useful items assigned to each table under the Pinball FX tab.
    """

    display_name = "Useful Item Percentage"

    range_start = 0
    range_end = 100

    default = 50


class TrapPercentage(Range):
    """
    Determines what percentage of filler items will get converted to trap items.

    Trap Items are made up of the following types:
    - Post-Processing Effects (Black and White, Bloom, Chromatic, Color Inversion, Grainy, Tunnel Vision)

    This percentage is applied to the remaining filler items AFTER the useful item conversion has taken place.
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

    default = {trap_type.value: 1 for trap_type in PinballFXAPTrapTypes}


class TrapDuration(Range):
    """
    Determines how long each trap will last (in seconds).
    """

    display_name = "Trap Duration"

    range_start = 20
    range_end = 300

    default = 30


@dataclass
class PinballFXOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    goal: Goal
    shiny_quarters_total: ShinyQuartersTotal
    shiny_quarters_required: ShinyQuartersRequired
    pinball_table_selection: PinballTableSelection
    pinball_table_count: PinballTableCount
    include_very_high_tier_scores: IncludeVeryHighTierScores
    include_one_ball_challenges: IncludeOneBallChallenges
    include_flips_challenges: IncludeFlipsChallenges
    include_distance_challenges: IncludeDistanceChallenges
    target_score_requirement_mode: TargetScoreRequirementMode
    target_score_requirement_percentage: TargetScoreRequirementPercentage
    useful_item_percentage: UsefulItemPercentage
    trap_percentage: TrapPercentage
    trap_weights: TrapWeights
    trap_duration: TrapDuration


option_groups: List[OptionGroup] = [
    OptionGroup(
        "Goal Options",
        [
            Goal,
            ShinyQuartersTotal,
            ShinyQuartersRequired,
        ],
    ),
    OptionGroup(
        "Pinball Table Options",
        [
            PinballTableSelection,
            PinballTableCount,
        ],
    ),
    OptionGroup(
        "Location Options",
        [
            IncludeVeryHighTierScores,
            IncludeOneBallChallenges,
            IncludeFlipsChallenges,
            IncludeDistanceChallenges,
        ],
    ),
    OptionGroup(
        "Target Score Options",
        [
            TargetScoreRequirementMode,
            TargetScoreRequirementPercentage,
        ],
    ),
    OptionGroup(
        "Useful Item Options",
        [
            UsefulItemPercentage,
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
]

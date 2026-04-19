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

from .enums import MirrorsEdgeAPTrapTypes


class Goal(Choice):
    """
    Determines the victory condition.

    Runner Bags + Final Level: Collect enough Runner Bags to unlock a Final Level and clear it.
    Runner Bag Hunt: Collect a set number of Runner Bags spread across the multiworld.
    """
    display_name = "Goal"

    option_runner_bags_final_level = 0
    option_runner_bag_hunt = 1

    default = 0


class RunnerBagsTotal(Range):
    """
    Determines how many Runner Bags are in the item pool.
    """

    display_name = "Runner Bags Total"

    range_start = 1
    range_end = 50

    default = 20


class RunnerBagsRequired(Range):
    """
    Determines how many Runner Bags are required to either win or unlock the final level.

    If this number is higher than the total number of Runner Bags, it will be set to that number instead.
    """

    display_name = "Runner Bags Required"

    range_start = 1
    range_end = 50

    default = 15


class Logic(Choice):
    """
    Determines the Logic level.

    Regular: Requirements are aligned with the skills and knowledge of a more casual Mirror's Edge player.

    Advanced: Requirements can require tighter execution, more creative routes, and performing moves off of unintended objects to progress.
              Glitches and professional movement are NOT included in Advanced logic.
    """
    display_name = "Logic"

    option_regular = 0
    option_advanced = 1

    default = 0


class OpenWorld(Toggle):
    """
    If enabled, all levels will be unlocked from the start.
    Otherwise, you will start with 5 random levels unlocked and will need to unlock the rest by finding Level Unlock items in the multiworld.
    """

    display_name = "Open World"


class StartingAbilityCount(Range):
    """
    Determines how many abilities Faith will start with. Abilities are randomly selected.

    The intended experience is to start with 0, but you can add a few if you want to open up your early game.
    There are 19 abilities total.

    If a non-zero quantity is selected and paired with Open World, there will be very few progression items in your seed.
    This effectively means fewer, larger spheres. Be advised.
    """

    display_name = "Starting Ability Count"

    range_start = 0
    range_end = 8

    default = 0


class IncludeTwoStarRatings(Toggle):
    """
    If enabled, locations for 2-Star Ratings on each level will be created when generating the multiworld.

    Notes: These are considered fairly hard in vanilla time trials with access to all moves.

           They will therefore only be considered in logic when you have unlocked all moves.
           You can still send location checks if you manage to obtain the ratings before that.

           Difficulty can be mitigated with the Target Time Adjustment Percentage option below.
           You can also convert some filler items to useful Time Bonus items.
    """

    display_name = "Include 2-Star Ratings"


class IncludeThreeStarRatings(Toggle):
    """
    If enabled, locations for 3-Star Ratings on each level will be created when generating the multiworld.

    Notes: These are considered very hard in vanilla time trials with access to all moves.

           They will therefore only be considered in logic when you have unlocked all moves.
           You can still send location checks if you manage to obtain the ratings before that.

           Difficulty can be mitigated with the Target Time Adjustment Percentage option below.
           You can also convert some filler items to useful Time Bonus items.
    """

    display_name = "Include 3-Star Ratings"


class TargetTimeAdjustmentPercentage(Range):
    """
    Determines by what percentage Star Rating Target Times will be adjusted.

    This can be useful for players who feel the vanilla target times are too challenging to meet.

    Examples:
        - If set to 90, a target time of 1 minute 40 seconds will become 1 minute 30 seconds.
        - If set to 150, a target time of 1 minute 40 seconds will become 2 minutes 30 seconds.

    Note that the adjusted target times won't be reflected in-game. Your location checks will still pivot on the adjusted times.

    The Mirror's Edge Archipelago client will display the adjusted target times for each level under the Mirror's Edge tab.
    """

    display_name = "Target Time Adjustment Percentage"

    range_start = 90
    range_end = 200

    default = 100


class UsefulItemPercentage(Range):
    """
    Determines what percentage of filler items will get converted to useful items.

    Useful items are various Time Bonus denominations: 1 Second, 3 Seconds, 5 Seconds
    These will make meeting the star rating target times easier but are also level-specific for balance purposes.

    The sum of all Time Bonuses for a given level will be subtracted from your final time.

    The Mirror's Edge Archipelago client will display the useful items assigned to each level under the Mirror's Edge tab.
    """

    display_name = "Useful Item Percentage"

    range_start = 0
    range_end = 100

    default = 50


class TrapPercentage(Range):
    """
    Determines what percentage of filler items will get converted to trap items.

    Trap Items are the following:
    - Injury Trap: HP is set to 1 with slower regeneration than usual
    - Slippery Trap: Ground friction is nullified. Any movement in a direction will keep going in that direction until countered
    - Slow Trap: Movement speed is greatly reduced
    - Wide FOV Trap: Camera field-of-value is greatly increased

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

    default = {trap_type.value: 1 for trap_type in MirrorsEdgeAPTrapTypes}


class FOVAdjustment(Range):
    """
    Determines what field-of-view value the camera will be forced to use.

    This is a quality-of-life option since the game doesn't allow you to change FOV natively outside modifying engine INI files.
    """

    display_name = "FOV Adjustment"
    range_start = 80
    range_end = 110

    default = 85


@dataclass
class MirrorsEdgeOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    goal: Goal
    runner_bags_total: RunnerBagsTotal
    runner_bags_required: RunnerBagsRequired
    logic: Logic
    open_world: OpenWorld
    starting_ability_count: StartingAbilityCount
    include_2_star_ratings: IncludeTwoStarRatings
    include_3_star_ratings: IncludeThreeStarRatings
    target_time_adjustment_percentage: TargetTimeAdjustmentPercentage
    useful_item_percentage: UsefulItemPercentage
    trap_percentage: TrapPercentage
    trap_weights: TrapWeights
    fov_adjustment: FOVAdjustment


option_groups: List[OptionGroup] = [
    OptionGroup(
        "Goal Options",
        [
            Goal,
            RunnerBagsTotal,
            RunnerBagsRequired,
        ],
    ),
    OptionGroup(
        "Logic Options",
        [
            Logic,
        ],
    ),
    OptionGroup(
        "Item Options",
        [
            OpenWorld,
            StartingAbilityCount,
        ],
    ),
    OptionGroup(
        "Location Options",
        [
            IncludeTwoStarRatings,
            IncludeThreeStarRatings,
        ],
    ),
    OptionGroup(
        "Difficulty Customization Options",
        [
            TargetTimeAdjustmentPercentage,
            UsefulItemPercentage,
        ],
    ),
    OptionGroup(
        "Trap Options",
        [
            TrapPercentage,
            TrapWeights,
        ],
    ),
    OptionGroup(
        "Quality-of-life Options",
        [
            FOVAdjustment,
        ],
    ),
]

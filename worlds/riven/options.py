from typing import List

from dataclasses import dataclass

from Options import (
    Choice,
    OptionGroup,
    PerGameCommonOptions,
    OptionDict,
    Range,
    StartInventoryPool,
)

from .enums import RivenAPTrapTypes


class Goal(Choice):
    """
    Determines the victory condition.

    Good Ending: Trap Gehn, Free Catherine, and open the Star Fissure. The full Riven experience.
    Star Fissure: Open the Star Fissure. A more streamlined experience with no need to visit Tay or 233.
    """
    display_name: str = "Goal"

    option_good_ending: int = 0
    option_star_fissure: int = 1

    default = 0


class ExtraProgressiveStarFissureTelescopeSolutions(Range):
    """
    Determines how many extra Progressive Puzzle Solution: Star Fissure Telescope items are added to the pool.
    No matter your goal, you will always need 10 to logically be able to reach it.

    0 means you need 10 / 10
    5 means you need 10 / 15
    """

    display_name = "Extra Progressive Star Fissure Telescope Solutions"

    range_start = 0
    range_end = 5

    default = 0


class StartingMovementSpeed(Choice):
    """
    Determines the starting walk / run speed.

    Slower: Slower walk / run speed than vanilla (400 -> 300 units)
    Vanilla: Vanilla walk / run speed (400 units)
    Faster: Faster walk / run speed than vanilla (400 -> 500 units)

    You can optionally add Progressive Movement Speed items to the pool to speed you up.
    """
    display_name: str = "Starting Movement Speed"

    option_slower: int = 0
    option_vanilla: int = 1
    option_faster: int = 2

    default = 1


class ProgressiveMovementSpeedItemCount(Range):
    """
    Determines how many extra Progressive Movement Speed items are added to the pool.
    Each Progressive Movement Speed adds 100 units (Vanilla walk / run speed is 400 units)
    """

    display_name = "Progressive Movement Speed Item Count"

    range_start = 0
    range_end = 5

    default = 3


class TrapPercentage(Range):
    """
    Determines what percentage of filler items will get converted to trap items.

    Trap Items are made up of the following types:
    - Post-Processing Effects (Black and White, Bloom, Chromatic, Color Inversion, Mobile Game, Tunnel Vision)
    - Movement Speed Effects (Slow)
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

    default = {trap_type.value: 1 for trap_type in RivenAPTrapTypes}


class TrapDuration(Range):
    """
    Determines how long each trap will last (in seconds).
    """

    display_name = "Trap Duration"

    range_start = 20
    range_end = 300

    default = 30


@dataclass
class RivenOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    goal: Goal
    extra_progressive_star_fissure_telescope_solutions: ExtraProgressiveStarFissureTelescopeSolutions
    starting_movement_speed: StartingMovementSpeed
    progressive_movement_speed_item_count: ProgressiveMovementSpeedItemCount
    trap_percentage: TrapPercentage
    trap_weights: TrapWeights
    trap_duration: TrapDuration


option_groups: List[OptionGroup] = [
    OptionGroup(
        "Goal Options",
        [
            Goal,
            ExtraProgressiveStarFissureTelescopeSolutions,
        ],
    ),
    OptionGroup(
        "Gameplay Options",
        [
            StartingMovementSpeed,
            ProgressiveMovementSpeedItemCount,
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

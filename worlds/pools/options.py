from typing import List

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

from .enums import PoolsTrapTypes


class Goal(Choice):
    """
    Determines the victory condition.

    Rubber Ducks + Complete Level 6: Collect enough Rubber Ducks and complete Level 6.
    """
    display_name = "Goal"

    option_rubber_ducks_complete_level_6 = 0

    default = 0


class RubberDucksTotal(Range):
    """
    Determines how many Rubber Ducks are in the item pool.
    """

    display_name = "Rubber Ducks Total"

    range_start = 1
    range_end = 50

    default = 50


class RubberDucksRequired(Range):
    """
    Determines how many Rubber Ducks are required to unlock the goal condition.

    If this number is higher than the total number of Rubber Ducks, it will be set to that number instead.
    """

    display_name = "Rubber Ducks Required"

    range_start = 1
    range_end = 50

    default = 40


class IncludeLevel0(Toggle):
    """
    If enabled, locations for Level 0 will be created when generating the multiworld.

    Level 0 is disabled by default as it is a prologue meant to explain how the player got to the poolrooms.
    It is very different from the rest of the game. Location-wise, less of a focus on pools and more on props and chairs.
    """

    display_name = "Include Level 0"


class IncludeChairs(DefaultOnToggle):
    """
    If enabled, locations for sitting on each unique chair will be created when generating the multiworld.

    Introduces new progression items that unlock each chair type in the item pool.

    Chairs are of the following types:
    - Plastic Chairs
    - Sauna Benches
    - Armchairs
    - Wooden Chairs
    - Subway Chairs
    - Park Benches
    - Sofas

    You can disable this option if you want fewer locations or a more straightforward game.
    """

    display_name = "Include Chairs"


class TrapPercentage(Range):
    """
    Determines what percentage of filler items will get converted to trap items.

    Trap Items are the following:
    - No-Look: Disables camera movement
    - Rewind: Force rewinds your actions
    - Slow: Slows you down to a crawl
    - Wet: Keeps the camera lens wet
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

    default = {trap_type.value: 1 for trap_type in PoolsTrapTypes}


class TrapDuration(Range):
    """
    Determines how long each trap will last (in seconds).

    Rewind Traps will last half that duration.
    """

    display_name = "Trap Duration"

    range_start = 10
    range_end = 30

    default = 15


@dataclass
class PoolsOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    goal: Goal
    rubber_ducks_total: RubberDucksTotal
    rubber_ducks_required: RubberDucksRequired
    include_level_0: IncludeLevel0
    include_chairs: IncludeChairs
    trap_percentage: TrapPercentage
    trap_weights: TrapWeights
    trap_duration: TrapDuration


option_groups: List[OptionGroup] = [
    OptionGroup(
        "Goal Options",
        [
            Goal,
            RubberDucksTotal,
            RubberDucksRequired,
        ],
    ),
    OptionGroup(
        "Location Options",
        [
            IncludeLevel0,
            IncludeChairs,
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

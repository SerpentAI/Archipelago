from typing import List

from dataclasses import dataclass

from Options import (
    Choice,
    DefaultOnToggle,
    OptionGroup,
    PerGameCommonOptions,
    Range,
    StartInventoryPool,
    Toggle,
)


class Goal(Choice):
    """
    Determines the victory condition.

    Stop Purple Tentacle: Collect a set number of Swiss Deposits spread across the multiworld so the Swiss account can pay for the diamond, then stop Purple Tentacle's plan for world domination.
    Swiss Bank Heist: Collect a set number of Swiss Deposits and the Swiss Bankbook spread across the multiworld, then leave the motel through the front door as Bernard with the bankbook, abandoning your friends.
    """

    display_name = "Goal"

    option_stop_purple_tentacle = 0
    option_swiss_bank_heist = 1

    default = 0


class SwissDepositsTotal(Range):
    """
    Determines how many Swiss Deposits are in the item pool.
    """

    display_name = "Swiss Deposits Total"

    range_start = 1
    range_end = 30

    default = 20


class SwissDepositsRequired(Range):
    """
    Determines how many Swiss Deposits are required to complete the goal.

    If this number is higher than the total number of Swiss Deposits, it will be set to that number instead.
    """

    display_name = "Swiss Deposits Required"

    range_start = 1
    range_end = 30

    default = 15


class StartingCharacter(Choice):
    """
    Determines the character you start the game controlling.

    The other two characters need to be unlocked with Character items before you can switch or send items to them.
    """

    display_name = "Starting Character"

    option_bernard = 0
    option_hoagie = 1
    option_laverne = 2

    default = "random"


class IncludeRoomVisits(DefaultOnToggle):
    """
    If enabled, locations for entering rooms for the first time will be created when generating the multiworld.
    """

    display_name = "Include Room Visits"


class IncludeVoiceLines(Toggle):
    """
    If enabled, locations for certain interactions that make a character speak a specific line will be created when generating the multiworld.
    """

    display_name = "Include Voice Lines"


@dataclass
class DayOfTheTentacleOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    goal: Goal
    swiss_deposits_total: SwissDepositsTotal
    swiss_deposits_required: SwissDepositsRequired
    starting_character: StartingCharacter
    include_room_visits: IncludeRoomVisits
    include_voice_lines: IncludeVoiceLines


option_groups: List[OptionGroup] = [
    OptionGroup(
        "Goal Options",
        [
            Goal,
            SwissDepositsTotal,
            SwissDepositsRequired,
        ],
    ),
    OptionGroup(
        "Character Options",
        [
            StartingCharacter,
        ],
    ),
    OptionGroup(
        "Location Options",
        [
            IncludeRoomVisits,
            IncludeVoiceLines,
        ],
    ),
]

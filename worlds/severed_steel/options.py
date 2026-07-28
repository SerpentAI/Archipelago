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

from .enums import SeveredSteelAPTrapTypes, SeveredSteelLevels


class Goal(Choice):
    """
    Determines the victory condition.

    EdenSys Root Keys + Final Level: Collect enough EdenSys Root Keys to unlock a Final Level and clear it.
    EdenSys Root Key Hunt: Collect a set number of EdenSys Root Keys spread across the multiworld.
    """
    display_name = "Goal"

    option_edensys_root_keys_final_level = 0
    option_edensys_root_key_hunt = 1

    default = 0


class EdenSysRootKeysTotal(Range):
    """
    Determines how many EdenSys Root Keys are in the item pool.
    """

    display_name = "EdenSys Root Keys Total"

    range_start = 1
    range_end = 25

    default = 20


class EdenSysRootKeysRequired(Range):
    """
    Determines how many EdenSys Root Keys are required to either win or unlock the final level.

    If this number is higher than the total number of EdenSys Root Keys, it will be set to that number instead.
    """

    display_name = "EdenSys Root Keys Required"

    range_start = 1
    range_end = 25

    default = 15


class LevelSelection(OptionDict):
    """
    Determines which Levels can be considered for inclusion in the multiworld.

    Set any Level you don't want to possibly play as to false.

    A minimum of 12 Levels must be selected.
    """

    display_name = "Level Selection"

    levels: Dict[SeveredSteelLevels, bool] = dict()

    level: SeveredSteelLevels
    for level in SeveredSteelLevels:
        levels[level] = True

    valid_keys = {level.value: value for level, value in levels.items()}

    default = valid_keys


class LevelCount(Range):
    """
    Determines how many Levels will be picked for inclusion in the multiworld.

    If this number is higher than the size of your Level selection, it will be set to that number instead.
    """

    display_name = "Level Count"

    range_start = 12
    range_end = 51

    default = 16


class MutatorPercentage(Range):
    """
    Determines what percentage of levels will require being played with a specific Mutator active.

    The Severed Steel Archipelago client will display which Mutator is required for each level under the Severed Steel tab.
    It will also unlock all Mutators if you haven't unlocked them all for Firefight 2.0.
    """

    display_name = "Mutator Percentage"

    range_start = 0
    range_end = 100

    default = 0


class MutatorPoolType(Choice):
    """
    Determines the Mutator Pool Type.

    Only Debuffs: Only pick from Mutators that are detrimental to the player
    Mostly Debuffs: Many debuffs, few neutrals, few buffs
    Balanced: A good mix of everything
    Mostly Buffs: Many buffs, few neutrals, few debuffs
    Only Buffs: Only pick from Mutators that are a boon to the player
    Oops All Triple Threat: Only pick Triple Threat
    Oops All The Same: Only pick one random Mutator that gets applied to all levels

    Keep in mind Buffs will generally apply a 0.X multiplier to your score.
    """
    display_name = "Goal"

    option_only_debuffs = 0
    option_mostly_debuffs = 1
    option_balanced = 2
    option_mostly_buffs = 3
    option_only_buffs = 4
    option_oops_all_triple_threat = 5
    option_oops_all_the_same = 6

    default = 2


class MirroredPercentage(Range):
    """
    Determines what percentage of levels will require being played Mirrored.

    The Severed Steel Archipelago client will display if Mirrored is required for each level under the Severed Steel tab.
    It will also unlock the Mirrored option for each level if you haven't unlocked them all for Firefight 2.0.
    """

    display_name = "Mirrored Percentage"

    range_start = 0
    range_end = 100

    default = 0


class IncludeTargetTimes(Toggle):
    """
    If enabled, locations for meeting a Target Time on each level will be created when generating the multiworld.
    """

    display_name = "Include Target Times"


class IncludeChallenges(Toggle):
    """
    If enabled, locations for completing both Challenges on each level will be created when generating the multiworld.
    """

    display_name = "Include Challenges"


class IncludeStylishActionChallenges(Toggle):
    """
    If enabled, locations for completing a set number of random Stylish Action Challenges on each level will be created when generating the multiworld.

    The following Stylish Actions can be used when generating a Challenge:
    Dive Frag, Wall Run Frag, Flip Frag, Kickslide, Slide Frag, Quick Shot, Multikill, Throw Hit, Cannon Frag, Drop Kick, Wall Bang, Stole Weapon, Air Shot, Kick, Nice Throw

    The Severed Steel Archipelago client will display the appropriate Stylish Action Challenges when a level is loaded under the Severed Steel tab.
    """

    display_name = "Include Stylish Action Challenges"


class StylishActionChallengeCountPerLevel(Range):
    """
    Determines how many random Stylish Action Challenges will be generated for each level to have locations for, if Stylish Action Challenges are included.
    """

    display_name = "Stylish Action Challenge Count Per Level"

    range_start = 1
    range_end = 5

    default = 3


class RankScoreRequirementMode(Choice):
    """
    Determines how Rank Score requirements are set.

    Same for All Levels: A single percentage will be applied to the Rank Score requirements of all levels
    Random per Level: Each level will have a random percentage applied to its Rank Score requirements
    """

    display_name = "Rank Score Requirement Mode"

    option_same_for_all_levels: int = 0
    option_random_per_level: int = 1

    default = 0


class RankScoreRequirementPercentage(Range):
    """
    Determines the percentage to apply Rank Score requirements. You will not unlock Rank-related location checks until
    you reach or exceed the Score requirements for each rank on a given level.

    When the requirement mode is set to random per level, the specified percentage will act as the maximum possible.

    The Severed Steel Archipelago client will display the appropriate Rank Score requirements when a level is loaded under the Severed Steel tab.
    """

    display_name = "Score Requirement Percentage"

    range_start = 50
    range_end = 250

    default = 100


class TargetTimeRequirementMode(Choice):
    """
    Determines how Target Time requirements are set, if they are included.

    Same for All Levels: A single percentage will be applied to the Target Time requirements of all levels
    Random per Level: Each level will have a random percentage applied to its Target Time requirements
    """

    display_name = "Target Time Requirement Mode"

    option_same_for_all_levels: int = 0
    option_random_per_level: int = 1

    default = 0


class TargetTimeRequirementPercentage(Range):
    """
    Determines the percentage to apply Target Time requirements.

    When the requirement mode is set to random per level, the specified percentage will act as the minimum possible.

    The game doesn't provide target times. Base Target Times were determined by taking the 10th time on the leaderboard and multiplying it by 2.5.
    Experiment to find a percentage that suits your skill level.

    The Severed Steel Archipelago client will display the appropriate Target Time when a level is loaded under the Severed Steel tab.
    """

    display_name = "Target Time Percentage"

    range_start = 50
    range_end = 250

    default = 125


class IncludeOverpoweredItems(DefaultOnToggle):
    """
    If enabled, level-specific items granting you abilities that could be considered overpowered will be added to the pool.

    Overpowered Items are the following:
    - Unlimited Ammo
    - Unlimited Cannon Ammo
    - Invincibility
    """

    display_name = "Include Overpowered Abilities"


class InvincibleMode(Toggle):
    """
    If enabled, the player character will be invincible at all times. Sometimes you just want to style on enemies...
    """

    display_name = "Invincible Mode"


class TrapPercentage(Range):
    """
    Determines what percentage of filler items will get converted to trap items.

    Trap Items are made up of the following types:
    - Post-Processing Effects (Black and White, Bloom, Chromatic, Color Inversion, Mobile Game, Tunnel Vision)
    - Time Dilation Effects (Fast-Mo)
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

    default = {trap_type.value: 1 for trap_type in SeveredSteelAPTrapTypes}


class TrapDuration(Range):
    """
    Determines how long each trap will last (in seconds).
    """

    display_name = "Trap Duration"

    range_start = 20
    range_end = 300

    default = 30


@dataclass
class SeveredSteelOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    goal: Goal
    edensys_root_keys_total: EdenSysRootKeysTotal
    edensys_root_keys_required: EdenSysRootKeysRequired
    level_selection: LevelSelection
    level_count: LevelCount
    mutator_percentage: MutatorPercentage
    mutator_pool_type: MutatorPoolType
    mirrored_percentage: MirroredPercentage
    include_target_times: IncludeTargetTimes
    include_challenges: IncludeChallenges
    include_stylish_action_challenges: IncludeStylishActionChallenges
    stylish_action_challenge_count_per_level: StylishActionChallengeCountPerLevel
    rank_score_requirement_mode: RankScoreRequirementMode
    rank_score_requirement_percentage: RankScoreRequirementPercentage
    target_time_requirement_mode: TargetTimeRequirementMode
    target_time_requirement_percentage: TargetTimeRequirementPercentage
    include_overpowered_items: IncludeOverpoweredItems
    invincible_mode: InvincibleMode
    trap_percentage: TrapPercentage
    trap_weights: TrapWeights
    trap_duration: TrapDuration


option_groups: List[OptionGroup] = [
    OptionGroup(
        "Goal Options",
        [
            Goal,
            EdenSysRootKeysTotal,
            EdenSysRootKeysRequired,
        ],
    ),
    OptionGroup(
        "Level Options",
        [
            LevelSelection,
            LevelCount,
            MutatorPercentage,
            MutatorPoolType,
            MirroredPercentage,
        ],
    ),

    OptionGroup(
        "Location Options",
        [
            IncludeTargetTimes,
            IncludeChallenges,
            IncludeStylishActionChallenges,
            StylishActionChallengeCountPerLevel,
        ],
    ),
    OptionGroup(
        "Difficulty Customization Options",
        [
            RankScoreRequirementMode,
            RankScoreRequirementPercentage,
            TargetTimeRequirementMode,
            TargetTimeRequirementPercentage,
        ],
    ),
    OptionGroup(
        "Item Options",
        [
            IncludeOverpoweredItems,
        ],
    ),
    OptionGroup(
        "Gameplay Options",
        [
            InvincibleMode,
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

from typing import List

from dataclasses import dataclass

from Options import (
    Choice,
    DeathLinkMixin,
    OptionDict,
    OptionGroup,
    PerGameCommonOptions,
    Range,
    StartInventoryPool,
    Toggle,
)

from .enums import TwentyMinutesCharacters, TwentyMinutesTrapTypes, TwentyMinutesWeapons


class Goal(Choice):
    """
    Determines the victory condition.

    Forbidden Tomes + Final Map: Collect enough Forbidden Tomes to unlock the goal map's true time limit, then survive 20 minutes on it.
    Forbidden Tome Hunt: Collect a set number of Forbidden Tomes spread across the multiworld.

    Regardless of which Goal is selected, only one Map is ever allowed to reach the full 20 minute run length through
    its Progressive Timer items. The other Maps are capped at 12 minutes.
    """
    display_name = "Goal"

    option_forbidden_tomes_final_map = 0
    option_forbidden_tome_hunt = 1

    default = 0


class ForbiddenTomesTotal(Range):
    """
    Determines how many Forbidden Tomes are in the item pool.
    """

    display_name = "Forbidden Tomes Total"

    range_start = 1
    range_end = 25

    default = 20


class ForbiddenTomesRequired(Range):
    """
    Determines how many Forbidden Tomes are required to unlock the goal map's true time limit.

    If this number is higher than the total number of Forbidden Tomes, it will be set to that number instead.
    """

    display_name = "Forbidden Tomes Required"

    range_start = 1
    range_end = 25

    default = 15


class CharacterSelection(OptionDict):
    """
    Determines which Characters can be considered for inclusion in the multiworld.

    Set any Character you don't want to possibly play as to false.
    """

    display_name = "Character Selection"

    valid_keys = {character.value: True for character in TwentyMinutesCharacters}

    default = valid_keys


class CharacterCount(Range):
    """
    Determines how many Characters will be picked from your selection for inclusion in the multiworld.

    Each included Character gets their own set of location checks. One Character will always be available from the
    start, randomly picked from your selection. The rest will need to be unlocked with Character Unlock items.

    If this number is higher than the size of your Character selection, it will be set to that number instead.
    """

    display_name = "Character Count"

    range_start = 1
    range_end = 13

    default = 3


class WeaponSelection(OptionDict):
    """
    Determines which Weapons can be considered for inclusion in the multiworld.

    Set any Weapon you don't want to possibly play with to false.
    """

    display_name = "Weapon Selection"

    valid_keys = {weapon.value: True for weapon in TwentyMinutesWeapons}

    default = valid_keys


class WeaponCount(Range):
    """
    Determines how many Weapons will be picked from your selection for inclusion in the multiworld.

    Each included Weapon gets their own set of location checks. One Weapon will always be available from the
    start, randomly picked from your selection. The rest will need to be unlocked with Weapon Unlock items.

    If this number is higher than the size of your Weapon selection, it will be set to that number instead.
    """

    display_name = "Weapon Count"

    range_start = 2
    range_end = 11

    default = 3


class StartingMap(Choice):
    """
    Determines the Map you will start with access to. The other Maps will need to be unlocked with Map Unlock items.
    """

    display_name = "Starting Map"

    option_forest = 0
    option_temple = 1
    option_pumpkin_patch = 2

    default = "random"


class StartingDarkness(Range):
    """
    Determines the Darkness level all Maps will start at.

    Progressive Darkness Reduction items will be added to the item pool to allow you to reach Darkness 0.
    """

    display_name = "Starting Darkness"

    range_start = 0
    range_end = 15

    default = 3


class MaximumSurvivableDarkness(Range):
    """
    Determines the Darkness level at which surviving a full 20 minute run is considered achievable in logic.
    """

    display_name = "Maximum Survivable Darkness"

    range_start = 0
    range_end = 15

    default = 0


class RandomizeWeaponAttributes(Toggle):
    """
    If enabled, Weapon attributes (damage, reload time, projectile count, and so on) will be randomized once at
    generation time, independently for each Weapon in the pool.

    Randomized values are drawn from the range observed across all vanilla Weapons for that attribute, so a
    randomized Weapon can end up stronger or weaker than its vanilla self, but never wildly outside what the game
    already considers normal.
    """

    display_name = "Randomize Weapon Attributes"


class WeaponAttributeRandomizationChance(Range):
    """
    Determines the percentage chance, per attribute per Weapon, that an attribute gets randomized rather than kept
    at its vanilla value.

    Only relevant if Randomize Weapon Attributes is enabled.
    """

    display_name = "Weapon Attribute Randomization Chance"

    range_start = 0
    range_end = 100

    default = 50


class TrapPercentage(Range):
    """
    Determines what percentage of filler items will get converted to trap items.
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

    default = {trap_type.value: 1 for trap_type in TwentyMinutesTrapTypes}


@dataclass
class TwentyMinutesOptions(PerGameCommonOptions, DeathLinkMixin):
    start_inventory_from_pool: StartInventoryPool
    goal: Goal
    forbidden_tomes_total: ForbiddenTomesTotal
    forbidden_tomes_required: ForbiddenTomesRequired
    character_selection: CharacterSelection
    character_count: CharacterCount
    weapon_selection: WeaponSelection
    weapon_count: WeaponCount
    starting_map: StartingMap
    starting_darkness: StartingDarkness
    maximum_survivable_darkness: MaximumSurvivableDarkness
    randomize_weapon_attributes: RandomizeWeaponAttributes
    weapon_attribute_randomization_chance: WeaponAttributeRandomizationChance
    trap_percentage: TrapPercentage
    trap_weights: TrapWeights


option_groups: List[OptionGroup] = [
    OptionGroup(
        "Goal Options",
        [
            Goal,
            ForbiddenTomesTotal,
            ForbiddenTomesRequired,
        ],
    ),
    OptionGroup(
        "Character Options",
        [
            CharacterSelection,
            CharacterCount,
        ],
    ),
    OptionGroup(
        "Weapon Options",
        [
            WeaponSelection,
            WeaponCount,
        ],
    ),
    OptionGroup(
        "Map Options",
        [
            StartingMap,
        ],
    ),
    OptionGroup(
        "Difficulty Customization Options",
        [
            StartingDarkness,
            MaximumSurvivableDarkness,
        ],
    ),
    OptionGroup(
        "Gameplay Options",
        [
            RandomizeWeaponAttributes,
            WeaponAttributeRandomizationChance,
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

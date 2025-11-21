from typing import List

from dataclasses import dataclass

from Options import (
    Choice,
    DeathLinkMixin,
    DefaultOnToggle,
    OptionGroup,
    PerGameCommonOptions,
    Range,
    StartInventoryPool,
    Toggle,
)


# Goal Options
# ...

# Character Options
class CharacterRace(Choice):
    """
    Determines the race of the player character.

    During character creation, the race selection will be locked to this choice.
    """

    display_name = "Character Race"

    option_argonian: int = 0
    option_breton: int = 1
    option_dark_elf: int = 2
    option_high_elf: int = 3
    option_imperial: int = 4
    option_khajiit: int = 5
    option_nord: int = 6
    option_orc: int = 7
    option_redguard: int = 8
    option_wood_elf: int = 9

    default = "random"


class CharacterSex(Choice):
    """
    Determines the sex of the player character.

    During character creation, the sex selection will be locked to this choice.
    """

    display_name = "Character Sex"

    option_female: int = 0
    option_male: int = 1

    default = "random"


class CharacterClass(Choice):
    """
    Determines the class of the player character.

    During character creation, the class selection will be locked to this choice.
    """

    display_name = "Character Class"

    option_acrobat: int = 0
    option_agent: int = 1
    option_archer: int = 2
    option_assassin: int = 3
    option_barbarian: int = 4
    option_bard: int = 5
    option_battlemage: int = 6
    option_crusader: int = 7
    option_healer: int = 8
    option_knight: int = 9
    option_mage: int = 10
    option_monk: int = 11
    option_nightblade: int = 12
    option_pilgrim: int = 13
    option_rogue: int = 14
    option_scout: int = 15
    option_sorcerer: int = 16
    option_spellsword: int = 17
    option_thief: int = 18
    option_warrior: int = 19
    option_witchhunter: int = 20

    default = "random"


class CharacterBirthsign(Choice):
    """
    Determines the birthsign of the player character.

    During character creation, the birthsign selection will be locked to this choice.
    """

    display_name = "Character Birthsign"

    option_the_apprentice: int = 0
    option_the_atronach: int = 1
    option_the_lady: int = 2
    option_the_lord: int = 3
    option_the_lover: int = 4
    option_the_mage: int = 5
    option_the_ritual: int = 6
    option_the_serpent: int = 7
    option_the_shadow: int = 8
    option_the_steed: int = 9
    option_the_thief: int = 10
    option_the_tower: int = 11
    option_the_warrior: int = 12

    default = "random"


# Alchemy Options
class AlchemyIngredientEffects(Choice):
    """
    Determines how alchemy ingredient effects are selected and assigned.

    Vanilla: Use vanilla effects for each alchemy ingredient
    Reorder: Reorder each set of vanilla effects randomly for each alchemy ingredient
    Shuffle: Shuffle all sets of vanilla effects between alchemy ingredients
    Shuffle and Reorder: Same as Shuffle, but also reorder each set of effects for each ingredient
    Randomize: 4 random effects are assigned to each alchemy ingredient.

    Note: Selecting something other than 'Vanilla' or 'Reorder' means you will lose the ability to look up alchemy
    ingredient effects (or rely on existing game knowledge). This will make the game take significantly longer, as you
    will have to gather a lot of ingredients and experiment with them to discover their effects.
    """

    display_name = "Alchemy Ingredient Effects"

    option_vanilla: int = 0
    option_reorder: int = 1
    option_shuffle: int = 2
    option_shuffle_and_reorder: int = 3
    option_randomize: int = 4

    default = 0


@dataclass
class TES3Options(PerGameCommonOptions, DeathLinkMixin):
    character_race: CharacterRace
    character_sex: CharacterSex
    character_class: CharacterClass
    character_birthsign: CharacterBirthsign
    alchemy_ingredient_effects: AlchemyIngredientEffects


option_groups: List[OptionGroup] = [
    OptionGroup(
        "Character Options",
        [
            CharacterRace,
            CharacterSex,
            CharacterClass,
            CharacterBirthsign,
        ],
    ),
    OptionGroup(
        "Alchemy Options",
        [
            AlchemyIngredientEffects,
        ],
    ),
]
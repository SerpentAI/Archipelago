from dataclasses import dataclass

from Options import Choice, DefaultOnToggle, NamedRange, PerGameCommonOptions


class DamageTakenDifficulty(Choice):
    """
    Determines the difficulty of damage taken

    Vanilla: Mario loses a powerup tier when taking damage
    One Hit Small Mario: Mario becomes small when taking damage, regardless of powerup tier
    One Hit KO: Mario dies when taking damage, regardless of powerup tier
    """

    display_name: str = "Damage Taken Difficulty"

    default = 0

    option_vanilla: int = 0
    option_one_hit_small_mario: int = 1
    option_one_hit_ko: int = 2


class EasierSpadeGame(DefaultOnToggle):
    """If true, spade game reels will stop instantly instead of having hard to predict delays"""

    display_name: str = "Easier Spade Game"


class EnemyDifficulty(Choice):
    """
    Determines the difficulty of enemy behaviors

    Vanilla: Original enemy behaviors
    Hard: Applies all harder behaviors to enemies
    Randomized: Applies a random set of harder behaviors to enemies

    The behaviors that can be affected are the following:
    -
    """

    display_name: str = "Enemy Difficulty"

    default = 0

    option_vanilla: int = 0
    option_hard: int = 1
    option_randomized: int = 2
    option_custom: int = 3


class GameMechanicDifficulty(Choice):
    """
    Determines the difficulty of some game mechanics

    Vanilla: Original game mechanics
    Hard: Applies all harder modifiers to game mechanics
    Randomized: Applies a random set of harder modifiers to game mechanics

    The game mechanics that can be affected are the following:
    -
    """

    display_name: str = "Game Mechanic Difficulty"

    default = 0

    option_vanilla: int = 0
    option_hard: int = 1
    option_randomized: int = 2
    option_custom: int = 3


class MarioOutfitColor(Choice):
    """
    Determines the color of Mario's outfit
    """

    display_name: str = "Mario Outfit Color"

    default = 9

    option_black: int = 0
    option_blue: int = 1
    option_gray: int = 2
    option_green: int = 3
    option_light_blue: int = 4
    option_light_green: int = 5
    option_orange: int = 6
    option_pink: int = 7
    option_purple: int = 8
    option_red: int = 9
    option_turquoise: int = 10
    option_white: int = 11
    option_yellow: int = 12


# See if it's possible to shuffle castles

class ShuffleFortresses(DefaultOnToggle):
    """
        If true, the fortresses will be shuffled among themselves
    """

    display_name: str = "Shuffle Fortresses"


class ShuffleLevels(DefaultOnToggle):
    """
        If true, the regular levels will be shuffled among themselves
    """

    display_name: str = "Shuffle Levels"


class ShuffleWorld8Ships(DefaultOnToggle):
    """
        If true, the world 8 ships will be shuffled among themselves
    """

    display_name: str = "Shuffle World 8 Ships"


class StartingLives(NamedRange):
    """
    Determines the number of lives the player starts with
    """

    display_name: str = "Starting Lives"

    range_start = 1
    range_end = 99

    default = "vanilla"

    special_range_names = {
        "infinite": -1,
        "infinite_with_death_counter": -2,
        "vanilla": 4,
    }


@dataclass
class SMB3Options(PerGameCommonOptions):
    shuffle_levels: ShuffleLevels
    shuffle_fortresses: ShuffleFortresses
    shuffle_world_8_ships: ShuffleWorld8Ships

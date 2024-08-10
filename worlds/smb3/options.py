from dataclasses import dataclass

from Options import Choice, DefaultOnToggle, NamedRange, PerGameCommonOptions, Toggle


class DamageTakenDifficulty(Choice):
    """
    Determines the difficulty of damage taken

    Vanilla: Mario loses a powerup tier when taking damage
    One Hit Small Mario: Mario becomes small when taking damage, regardless of powerup tier
    One Hit KO: Mario dies when taking damage, regardless of powerup tier
    """

    display_name: str = "Damage Taken Difficulty"

    default: int = 0

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

    default: int = 0

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

    default: int = 0

    option_vanilla: int = 0
    option_hard: int = 1
    option_randomized: int = 2
    option_custom: int = 3


class MarioOutfitColor(Choice):
    """
    Determines the color of Mario's outfit
    """

    display_name: str = "Mario Outfit Color"

    default: int = 9

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


class StartingLives(NamedRange):
    """
    Determines the number of lives the player starts with
    """

    display_name: str = "Starting Lives"

    range_start = 1
    range_end = 99

    default: str = "vanilla"

    special_range_names = {
        "infinite": -1,
        "infinite_with_death_counter": -2,
        "vanilla": 4,
    }











class Goal(Choice):
    """
    Determines the victory condition

    Three Artifacts: Retrieve the three artifacts of magic and place them in the walking castle
    """
    display_name: str = "Goal"

    default: int = 0
    option_three_artifacts: int = 0


class QuickPortFoozle(DefaultOnToggle):
    """If true, the items needed to go down the well will be found in early locations for a smoother early game"""

    display_name: str = "Quick Port Foozle"


class StartWithHotspotItems(DefaultOnToggle):
    """
    If true, the player will be given all the hotspot items at the start of the game, effectively removing the need
    to enable the important hotspots in the game before interacting with them. Recommended for beginners

    Note: The spots these hotspot items would have occupied in the item pool will instead be filled with junk items.
    Expect a higher volume of filler items if you enable this option
    """

    display_name: str = "Start with Hotspot Items"


class Deathsanity(Toggle):
    """If true, adds 16 player death locations to the world"""

    display_name: str = "Deathsanity"


class GrantMissableLocationChecks(Toggle):
    """
    If true, performing an irreversible action will grant the locations checks that would have become unobtainable as a
    result of that action when you meet the item requirements

    Otherwise, the player is expected to potentially have to use the save system to reach those location checks. If you
    don't like the idea of rarely having to reload an earlier save to get a location check, make sure this option is
    enabled
    """

    display_name: str = "Grant Missable Checks"


@dataclass
class SMB3Options(PerGameCommonOptions):
    goal: Goal
    quick_port_foozle: QuickPortFoozle
    start_with_hotspot_items: StartWithHotspotItems
    deathsanity: Deathsanity
    grant_missable_location_checks: GrantMissableLocationChecks

from dataclasses import dataclass

from Options import Choice, DefaultOnToggle, PerGameCommonOptions, Toggle


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


class StartingLocation(Choice):
    """
    Determines the in-game location the player will start at. The player always starts with VOXAM, which can be used to
    teleport back to the starting location at any time
    """

    display_name: str = "Starting Location"

    option_port_foozle: int = 0
    option_crossroads: int = 1
    option_dm_lair: int = 2
    option_dm_lair_house: int = 3
    option_gue_tech: int = 4
    option_spell_lab: int = 5
    option_hades_shore: int = 6
    option_flood_control_dam_3: int = 7
    option_monastery_totemizer: int = 8
    option_monastery_exhibit: int = 9

    default = "random"


@dataclass
class ZorkGrandInquisitorOptions(PerGameCommonOptions):
    goal: Goal
    quick_port_foozle: QuickPortFoozle
    start_with_hotspot_items: StartWithHotspotItems
    deathsanity: Deathsanity
    grant_missable_location_checks: GrantMissableLocationChecks
    starting_location: StartingLocation

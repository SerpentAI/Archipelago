from dataclasses import dataclass

from Options import Choice, DefaultOnToggle, PerGameCommonOptions, Toggle


class Goal(Choice):
    """
    Determines the victory condition

    Three Artifacts: Retrieve the three artifacts of magic and place them in the walking castle
    """
    display_name: str = "Goal"

    option_three_artifacts: int = 0

    default = 0


class StartingLocation(Choice):
    """
    Determines the in-game location the player will start at. The player always starts with VOXAM, which can be used to
    teleport back to the starting location at any time. Depending on the starting location, the player may also be given
    a starter kit of items to help them get going
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

    default = 0


class StartWithHotspotItems(DefaultOnToggle):
    """
    If true, the player will be given all the hotspot items at the start of the game, effectively removing the need
    to enable the important hotspots in the game before interacting with them. Recommended for beginners

    Note: The spots these hotspot items would have occupied in the item pool will instead be filled with junk items.
    Expect a higher volume of filler items if you enable this option
    """

    display_name: str = "Start with Hotspot Items"


class CraftableSpells(Choice):
    """
    Determines the behavior when craftable spells (BEBURTT, OBIDIL, SNAVIG, YASTARD) are obtained.
    Spells in a starting location's starter kit always have precedence over this option

    Vanilla: After crafting a spell, the player will be given that exact spell
    Any Spell: After crafting a spell, the player will be given a random spell
    Anything: After crafting a spell, a random item from the multiworld will be unlocked
    """

    display_name: str = "Craftable Spells"

    option_vanilla: int = 0
    option_any_spell: int = 1
    option_anything: int = 2

    default = 2


class Deathsanity(Toggle):
    """If true, adds 22 unique player death locations to the world"""  # TODO: Add note about it being forced in Necro goal

    display_name: str = "Deathsanity"


class Landmarksanity(DefaultOnToggle):
    """If true, adds 20 landmark locations to the world"""  # TODO: Add note about it being forced in Zork Tour goal

    display_name: str = "Landmarksanity"


class PlaceEarlyItemsLocally(Toggle):
    """If true, items to be placed early in the multiworld (when applicable) will be placed locally"""

    display_name: str = "Place Early Items Locally"


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
class ZorkGrandInquisitorOptions(PerGameCommonOptions):
    goal: Goal
    starting_location: StartingLocation
    start_with_hotspot_items: StartWithHotspotItems
    craftable_spells: CraftableSpells
    deathsanity: Deathsanity
    landmarksanity: Landmarksanity
    place_early_items_locally: PlaceEarlyItemsLocally
    grant_missable_location_checks: GrantMissableLocationChecks

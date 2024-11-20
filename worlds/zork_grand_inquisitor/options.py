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


class Hotspots(Choice):
    """
    Determines the behavior of hotspots (interactable areas of the screen) in the game.

    Enabled: All hotspots will be enabled at the start of the game
    Require Item per Region: An item will enable all hotspots for a given region (e.g. Hotspots: Crossroads)
    Require Item per Hotspot: An item will enable a specific hotspot (e.g. Hotspot: Subway Token Slot)
    """

    display_name: str = "Hotspots"

    option_enabled: int = 0
    option_require_item_per_region: int = 1
    option_require_item_per_hotspot: int = 2

    default = 0


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
    hotspots: Hotspots
    craftable_spells: CraftableSpells
    deathsanity: Deathsanity
    landmarksanity: Landmarksanity
    place_early_items_locally: PlaceEarlyItemsLocally
    grant_missable_location_checks: GrantMissableLocationChecks

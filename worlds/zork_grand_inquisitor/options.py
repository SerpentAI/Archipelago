from dataclasses import dataclass

from Options import (
    Choice,
    DeathLinkMixin,
    DefaultOnToggle,
    PerGameCommonOptions,
    Range,
    StartInventoryPool,
    Toggle,
)


class Goal(Choice):
    """
    Determines the victory condition.

    Three Artifacts: Retrieve the Coconut of Quendor, the Cube of Foundation and the Skull of Yoruk
    Artifact of Magic Hunt: Retrieve X artifacts of magic and bring them to the walking castle
    Spell Heist: Acquire all spells and travel to the Port Foozle signpost
    Zork Tour: Visit all 20 landmarks and travel to the Port Foozle signpost
    Grim Journey: Experience all 22 player deaths and go beyond the gates of Hades
    """
    display_name: str = "Goal"

    option_three_artifacts: int = 0
    option_artifact_of_magic_hunt: int = 1
    option_spell_heist: int = 2
    option_zork_tour: int = 3
    option_grim_journey: int = 4

    default = 0


class ArtifactsOfMagicTotal(Range):
    """
    Determines how many Artifacts of Magic are in the item pool.

    Only relevant if the selected goal is Artifact of Magic Hunt.
    """

    display_name = "Artifacts of Magic Total"

    range_start = 5
    range_end = 25

    default = 15


class ArtifactsOfMagicRequired(Range):
    """
    Determines how many Artifacts of Magic are required to win.

    Only relevant if the selected goal is Artifact of Magic Hunt.
    """

    display_name = "Artifacts of Magic Required"

    range_start = 5
    range_end = 25

    default = 10


class StartingLocation(Choice):
    """
    Determines the in-game location the player will start at.

    The player always starts with VOXAM, which can be used to teleport back to the starting location at any time.
    Depending on the starting location, the player may also be given a starter kit of items to help them get going.

    Note: VOXAM will only work from the spell quickbar. It will have no effect from the spellbook.
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
    Spells in a starting location's starter kit always have precedence over this option.

    Vanilla: After crafting a spell, the player will be given that exact spell
    Any Spell: After crafting a spell, the player will be given a random spell
    Anything: After crafting a spell, a random item from the multiworld will be unlocked
    """

    display_name: str = "Craftable Spells"

    option_vanilla: int = 0
    option_any_spell: int = 1
    option_anything: int = 2

    default = 2


class WildVoxam(Toggle):
    """
    If true, casting VOXAM will have a small chance to teleport the player to a different location.

    This option can enable small stretches of out-of-logic gameplay in the early game, with strong diminishing returns
    as the game progresses.
    """

    display_name: str = "Wild VOXAM"


class WildVoxamChance(Range):
    """
    Determines the percentage chance that a VOXAM cast will be wild.
    """

    display_name = "Wild VOXAM Chance %"

    range_start = 1
    range_end = 10

    default = 5


class Deathsanity(Toggle):
    """
    If true, adds 22 unique player death locations to the world.

    This option will be forced on if your goal is Grim Journey.
    """

    display_name: str = "Deathsanity"


class Landmarksanity(DefaultOnToggle):
    """
    If true, adds 20 landmark locations to the world.

    This option will be forced on if your goal is Zork Tour.
    """

    display_name: str = "Landmarksanity"


class GrantMissableLocationChecks(Toggle):
    """
    If true, performing an irreversible action will grant the locations checks that would have become unobtainable as a
    result of that action when you meet the item requirements.

    Otherwise, the player is expected to potentially have to use the save system to reach those location checks. If you
    don't like the idea of rarely having to reload an earlier save to get a location check, make sure this option is
    enabled.
    """

    display_name: str = "Grant Missable Checks"


class ClientSeedInformation(Choice):
    """
    Determines what information about the seed the client will reveal after using the /zork command.

    Reveal Nothing: No information about the seed is displayed
    Reveal Goal: Only the goal of the seed is displayed
    Reveal Goal and Options: Both the goal and the options of the seed are displayed
    """

    display_name: str = "Client Seed Information"

    option_reveal_nothing: int = 0
    option_reveal_goal: int = 1
    option_reveal_goal_and_options: int = 2

    default = 2


@dataclass
class ZorkGrandInquisitorOptions(PerGameCommonOptions, DeathLinkMixin):
    start_inventory_from_pool: StartInventoryPool
    goal: Goal
    artifacts_of_magic_total: ArtifactsOfMagicTotal
    artifacts_of_magic_required: ArtifactsOfMagicRequired
    starting_location: StartingLocation
    hotspots: Hotspots
    craftable_spells: CraftableSpells
    wild_voxam: WildVoxam
    wild_voxam_chance: WildVoxamChance
    deathsanity: Deathsanity
    landmarksanity: Landmarksanity
    grant_missable_location_checks: GrantMissableLocationChecks
    client_seed_information: ClientSeedInformation

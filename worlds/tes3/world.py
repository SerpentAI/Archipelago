from typing import List, Tuple

from BaseClasses import Entrance, EntranceType, Item, ItemClassification, Location, Region, Tutorial

from worlds.AutoWorld import WebWorld, World

from .options import TES3Options, option_groups


class TES3Item(Item):
    game = "The Elder Scrolls III Morrowind"


class TES3Location(Location):
    game = "The Elder Scrolls III Morrowind"


class TES3WebWorld(WebWorld):
    theme: str = "dirt"

    tutorials: List[Tutorial] = [
        Tutorial(
            "Multiworld Setup Guide",
            "A guide to setting up The Elder Scrolls III Morrowind randomizer connected to an Archipelago Multiworld",
            "English",
            "setup_en.md",
            "setup/en",
            ["Serpent.AI"],
        )
    ]

    option_groups = option_groups


class TES3World(World):
    """
    The Elder Scrolls III: Morrowind is a 2002 action role-playing open world game for PC (and Xbox).
    Morrowind drops you on the alien island of Vvardenfell as a nobody tasked with unraveling a prophecy tied to ancient
    politics, a diseased demigod, and a fractured empire; the game’s open world pushes you to navigate faction
    rivalries, moral ambiguity, and a culture that often treats you with suspicion, all while piecing together who you
    are and whether you’re truly the prophesied figure or just another pawn in a long, ugly power struggle.
    """

    options_dataclass = TES3Options
    options: TES3Options

    game = "The Elder Scrolls III Morrowind"

    item_name_to_id = dict()
    location_name_to_id = dict()

    item_name_groups = dict()
    location_name_groups = dict()

    required_client_version: Tuple[int, int, int] = (0, 6, 2)

    web = TES3WebWorld()

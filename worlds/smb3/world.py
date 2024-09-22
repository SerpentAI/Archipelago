from typing import List, Tuple, Mapping, Any, Dict

from BaseClasses import Item, ItemClassification, Location, Region, Tutorial

from worlds.AutoWorld import WebWorld, World

from .options import SMB3Options


class SMB3Item(Item):
    game = "Super Mario Bros. 3"


class SMB3Location(Location):
    game = "Super Mario Bros. 3"


class SMB3WebWorld(WebWorld):
    theme: str = "grass"

    tutorials: List[Tutorial] = [
        Tutorial(
            "Multiworld Setup Guide",
            "A guide to setting up the Super Mario Bros. 3 randomizer connected to an Archipelago Multiworld",
            "English",
            "setup_en.md",
            "setup/en",
            ["Serpent.AI"],
        )
    ]


class SMB3World(World):
    """
    Super Mario Bros. 3, the third entry in the Super Mario Bros. series and Super Mario
    franchise, sees Mario or Luigi navigate a nonlinear world map containing platforming
    levels and optional minigames and challenges. The game features more diverse movement
    options and new items alongside more complex level designs and boss battles.
    """

    options_dataclass = SMB3Options
    options: SMB3Options

    game = "Super Mario Bros. 3"

    topology_present = True

    # item_name_to_id = item_names_to_id()
    # location_name_to_id = location_names_to_id()
    #
    # item_name_groups = item_groups()
    # location_name_groups = location_groups()

    required_client_version: Tuple[int, int, int] = (0, 5, 0)

    web = SMB3WebWorld()

    def generate_early(self) -> None:
        pass
        # Depending on the level shuffle options, randomize and create a mapping of which location holds which level

    def create_regions(self) -> None:
        pass

    def create_items(self) -> None:
        pass

    def create_item(self, name: str) -> "Item":
        pass

    def set_rules(self) -> None:  # Not sure if we will need this one. If the lambda system is enough, we can remove it
        pass

    def generate_basic(self) -> None:
        pass

    def fill_slot_data(self) -> Mapping[str, Any]:
        pass

    def extend_hint_information(self, hint_data: Dict[int, Dict[int, str]]):
        pass

    def get_filler_item_name(self) -> str:
        pass

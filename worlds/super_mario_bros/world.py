from typing import Any, Dict, List, Tuple

from BaseClasses import Entrance, EntranceType, Item, ItemClassification, Location, Region, Tutorial

from worlds.AutoWorld import WebWorld, World

# from .data_funcs import (
#     id_to_alchemy_ingredient_effects,
#     id_to_birthsigns,
#     id_to_classes,
#     id_to_races,
#     id_to_sexes,
#     process_ingredient_alchemy_effects,
# )
#
# from .enums import (
#     TES3AlchemyEffects,
#     TES3Birthsigns,
#     TES3Classes,
#     TES3Ingredients,
#     TES3OptionAlchemyIngredientEffects,
#     TES3Races,
#     TES3Sexes,
# )

# from .options import TES3Options, option_groups


class SuperMarioBrosItem(Item):
    game = "Super Mario Bros."


class SuperMarioBrosLocation(Location):
    game = "Super Mario Bros."


class SuperMarioBrosWebWorld(WebWorld):
    theme: str = "grass"

    tutorials: List[Tutorial] = [
        Tutorial(
            "Multiworld Setup Guide",
            "A guide to setting up Super Mario Bros. randomizer connected to an Archipelago Multiworld",
            "English",
            "setup_en.md",
            "setup/en",
            ["Serpent.AI"],
        )
    ]

    # option_groups = option_groups


class SuperMarioBrosWorld(World):
    """
    Super Mario Bros. is a landmark 1985 side-scrolling platform game for the Nintendo Entertainment System (NES)
    that tasks players with guiding the plumber Mario through the fantastical Mushroom Kingdom. The objective is to
    rescue Princess Toadstool from the clutches of the evil King Koopa (Bowser), who has used black magic to turn
    the kingdom's inhabitants into inanimate objects like bricks and plants.
    """

    # options_dataclass = TES3Options
    # options: TES3Options

    game = "Super Mario Bros."

    item_name_to_id = dict()
    location_name_to_id = dict()

    item_name_groups = dict()
    location_name_groups = dict()

    required_client_version: Tuple[int, int, int] = (0, 6, 5)

    web = SuperMarioBrosWebWorld()



    ut_can_gen_without_yaml: bool = True

    @property
    def is_universal_tracker(self) -> bool:
        return hasattr(self.multiworld, "re_gen_passthrough")

    def generate_early(self) -> None:
        return None

    def create_regions(self) -> None:
        return None

    def create_items(self) -> None:
        return None

    # def create_item(self, name: str) -> TES3Item:
    #     pass

    # def generate_basic(self) -> None:
        # self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)

    def fill_slot_data(self) -> Dict[str, Any]:
        return dict()

        slot_data: Dict[str, Any] = dict()

        slot_data["alchemy_ingredient_effects"] = self.alchemy_ingredient_effects.value

        slot_data["character_birthsign"] = self.character_birthsign.value
        slot_data["character_class"] = self.character_class.value
        slot_data["character_race"] = self.character_race.value
        slot_data["character_sex"] = self.character_sex.value

        if self.alchemy_ingredient_effects != TES3OptionAlchemyIngredientEffects.VANILLA:
            slot_data["alchemy_effects"] = dict()

            ingredient: TES3Ingredients
            alchemy_effects: Tuple[TES3AlchemyEffects, ...]
            for ingredient, alchemy_effects in self.alchemy_effects.items():
                slot_data["alchemy_effects"][ingredient.value] = [
                    alchemy_effect.value for alchemy_effect in alchemy_effects
                ]

        print(slot_data)

        return slot_data
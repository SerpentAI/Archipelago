from typing import Any, Dict, List, Tuple

from BaseClasses import Entrance, EntranceType, Item, ItemClassification, Location, Region, Tutorial

from worlds.AutoWorld import WebWorld, World

from .data_funcs import (
    id_to_alchemy_ingredient_effects,
    id_to_birthsigns,
    id_to_classes,
    id_to_races,
    id_to_sexes,
    process_ingredient_alchemy_effects,
)

from .enums import (
    TES3AlchemyEffects,
    TES3Birthsigns,
    TES3Classes,
    TES3Ingredients,
    TES3OptionAlchemyIngredientEffects,
    TES3Races,
    TES3Sexes,
)

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

    required_client_version: Tuple[int, int, int] = (0, 6, 4)

    web = TES3WebWorld()

    alchemy_ingredient_effects: TES3OptionAlchemyIngredientEffects
    character_birthsign: TES3Birthsigns
    character_class: TES3Classes
    character_race: TES3Races
    character_sex: TES3Sexes

    alchemy_effects: Dict[TES3Ingredients, Tuple[TES3AlchemyEffects, ...]]

    ut_can_gen_without_yaml: bool = True

    @property
    def is_universal_tracker(self) -> bool:
        return hasattr(self.multiworld, "re_gen_passthrough")

    def generate_early(self) -> None:
        self.alchemy_ingredient_effects = id_to_alchemy_ingredient_effects()[
            self.options.alchemy_ingredient_effects.value
        ]

        self.character_birthsign = id_to_birthsigns()[self.options.character_birthsign.value]
        self.character_class = id_to_classes()[self.options.character_class.value]
        self.character_race = id_to_races()[self.options.character_race.value]
        self.character_sex = id_to_sexes()[self.options.character_sex.value]

        # Alchemy Effects
        self.alchemy_effects = process_ingredient_alchemy_effects(
            alchemy_effect_shuffle_mode=self.alchemy_ingredient_effects,
            random=self.random,
        )

    def create_regions(self) -> None:
        return None

    def create_items(self) -> None:
        return None

    # def create_item(self, name: str) -> TES3Item:
    #     pass

    # def generate_basic(self) -> None:
        # self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)

    def fill_slot_data(self) -> Dict[str, Any]:
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

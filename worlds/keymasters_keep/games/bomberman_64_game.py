from __future__ import annotations

import functools
from typing import List

from dataclasses import dataclass

from Options import Toggle

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class Bomberman64ArchipelagoOptions:
    bomberman_64_allow_rainbow_palace: Bomberman64AllowRainbowPalace


class Bomberman64Game(Game):
    # Initial Proposal by @delcake on Discord

    name = "Bomberman 64"
    platform = KeymastersKeepGamePlatforms.N64

    platforms_other = None

    is_adult_only_or_unrated = False

    options_cls = Bomberman64ArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Complete objectives on DIFF difficulty",
                data={"DIFF": (self.difficulties, 1)},
            ),
        ]

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Complete STAGE",
                data={"STAGE": (self.base_stages, 1)},
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Complete STAGE",
                data={"STAGE": (self.deep_stages, 1)},
                is_time_consuming=True,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Earn CARDS gold card(s) from STAGE",
                data={"CARDS": (self.stage_gold_card_range, 1), "STAGE": (self.base_stages, 1)},
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Earn CARDS gold card(s) from STAGE",
                data={"CARDS": (self.stage_gold_card_range, 1), "STAGE": (self.deep_stages, 1)},
                is_time_consuming=True,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Earn the Target Time gold card from STAGE",
                data={"STAGE": (self.base_stages, 1)},
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Earn the Target Time gold card from STAGE",
                data={"STAGE": (self.deep_stages, 1)},
                is_time_consuming=True,
                is_difficult=False,
                weight=23,
            ),
            GameObjectiveTemplate(
                label="Complete all stages in WORLD",
                data={"WORLD": (self.base_worlds, 1)},
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Complete all stages in WORLD",
                data={"WORLD": (self.deep_worlds, 1)},
                is_time_consuming=True,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Complete all stages in WORLD, earning at least CARDS gold cards from the set",
                data={"WORLD": (self.base_worlds, 1), "CARDS": (self.world_gold_card_range, 1)},
                is_time_consuming=False,
                is_difficult=True,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Complete all stages in WORLD, earning at least CARDS gold cards from the set",
                data={"WORLD": (self.deep_worlds, 1), "CARDS": (self.world_gold_card_range, 1)},
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
        ]

    @staticmethod
    def base_stages() -> List[str]:
        return [
            "Blue Resort Stage 1 - Switches and Bridges",
            "Blue Resort Stage 2 - VS Artemis",
            "Blue Resort Stage 3 - Pump it Up!",
            "Blue Resort Stage 4 - Sewer Savage",
            "Green Garden Stage 1 - Untouchable Treasure",
            "Green Garden Stage 2 - Friend or Foe?",
            "Green Garden Stage 3 - To Have or Have Not",
            "Green Garden Stage 4 - Winged Guardian",
            "Red Mountain Stage 1 - Hot on the Trail",
            "Red Mountain Stage 2 - VS Orion",
            "Red Mountain Stage 3 - On the Right Track",
            "Red Mountain Stage 4 - Hot Avenger",
            "White Glacier Stage 1 - Blizzard Peaks",
            "White Glacier Stage 2 - VS Regulus",
            "White Glacier Stage 3 - Shiny Slippy Icy Floor",
            "White Glacier Stage 4 - Cold Killers",
        ]

    @functools.cached_property
    def late_stages(self) -> List[str]:
        return [
            "Black Fortress Stage 1 - Go for Broke",
            "Black Fortress Stage 2 - High-Tech Harvester",
            "Black Fortress Stage 3 - Trap Tower",
            "Black Fortress Stage 4 - VS Altair",
        ]
    
    @functools.cached_property
    def secret_stages(self) -> List[str]:
        return [
            "Rainbow Palace Stage 1 - Beyond the Clouds",
            "Rainbow Palace Stage 2 - VS Spellmaker",
            "Rainbow Palace Stage 3 - Doom Castle",
            "Rainbow Palace Stage 4 - The Final Battle!",
        ]
    
    def deep_stages(self) -> List[str]:
        deep_stages: List[str] = self.late_stages[:]

        if self.archipelago_options.bomberman_64_allow_rainbow_palace:
            deep_stages.append(self.secret_stages)
        
        return deep_stages
    
    @staticmethod
    def base_worlds() -> List[str]:
        return [
            "Blue Resort",
            "Green Garden",
            "Red Mountain",
            "White Glacier",
        ]
    
    @functools.cached_property
    def late_worlds(self) -> List[str]:
        return [
            "Black Fortress",
        ]
    
    def deep_worlds(self) -> List[str]:
        deep_worlds: List[str] = self.late_worlds[:]

        if self.archipelago_options.bomberman_64_allow_rainbow_palace:
            deep_worlds.append("Rainbow Palace")
        
        return deep_worlds
    
    @staticmethod
    def difficulties() -> List[str]:
        return [
            "Hard",
            "Normal",
        ]
    
    @staticmethod
    def stage_gold_card_range() -> range:
        return range(1, 6)
    
    @staticmethod
    def world_gold_card_range() -> range:
        return range(5,16)


# Archipelago Options
class Bomberman64AllowRainbowPalace(Toggle):
    """
    Whether or not objectives are allowed require accessing the secret Rainbow Palace stages.
    """
    display_name = "Bomberman 64 Allow Rainbow Palace"

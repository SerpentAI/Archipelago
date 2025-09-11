from __future__ import annotations

from typing import List

from dataclasses import dataclass

from Options import DefaultOnToggle, OptionList, OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class ArchipelagoMultiworldRandomizerArchipelagoOptions:
    archipelago_multiworld_randomizer_game_selection: ArchipelagoMultiworldRandomizerGameSelection
    archipelago_multiworld_randomizer_objective_types: ArchipelagoMultiworldRandomizerObjectiveTypes
    archipelago_multiworld_randomizer_bingo_release_always_off: ArchipelagoMultiworldRandomizerBingoReleaseAlwaysOff


class ArchipelagoMultiworldRandomizerGame(Game):
    name = "Archipelago Multiworld Randomizer"
    platform = KeymastersKeepGamePlatforms.META

    platforms_other = None

    is_adult_only_or_unrated = False

    options_cls = ArchipelagoMultiworldRandomizerArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        game_objective_templates: List[GameObjectiveTemplate] = list()

        if self.include_solo_randomizer_objectives:
            game_objective_templates.append(
                GameObjectiveTemplate(
                    label="[Hints: HINT_COST%] Complete a solo randomizer with GAME",
                    data={
                        "HINT_COST": (self.hint_costs, 1),
                        "GAME": (self.games, 1)
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=2,
                ),
            )

        if self.include_small_multiworld_randomizer_objectives:
            game_objective_templates.extend([
                GameObjectiveTemplate(
                    label="[Hints: HINT_COST%  Release: RELEASE] Complete a multiworld randomizer with GAMES",
                    data={
                        "HINT_COST": (self.hint_costs, 1),
                        "RELEASE": (self.release, 1),
                        "GAMES": (self.games, 2)
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=3,
                ),
                GameObjectiveTemplate(
                    label="[Hints: HINT_COST%  Release: RELEASE] Complete a multiworld randomizer with GAMES",
                    data={
                        "HINT_COST": (self.hint_costs, 1),
                        "RELEASE": (self.release, 1),
                        "GAMES": (self.games, 3)
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=4,
                ),
            ])

        if self.include_small_multiworld_randomizer_with_apbingo_objectives:
            objective_label: str = (
                "[Hints: HINT_COST%  Release: RELEASE] Get COUNT bingo(s) on a SIZExSIZE APBingo board in a multiworld "
                "randomizer with GAMES"
            )

            if self.apbingo_release_always_off:
                objective_label = objective_label.replace("Release: RELEASE", "Release: Off")

            game_objective_templates.extend([
                GameObjectiveTemplate(
                    label=objective_label,
                    data={
                        "HINT_COST": (self.hint_costs, 1),
                        "RELEASE": (self.release, 1),
                        "GAMES": (self.games, 2),
                        "COUNT": (self.bingo_counts, 1),
                        "SIZE": (self.bingo_board_sizes, 1)
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label=objective_label,
                    data={
                        "HINT_COST": (self.hint_costs, 1),
                        "RELEASE": (self.release, 1),
                        "GAMES": (self.games, 3),
                        "COUNT": (self.bingo_counts, 1),
                        "SIZE": (self.bingo_board_sizes, 1)
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=3,
                ),
            ])

        if self.include_apbingo_blackout_objectives:
            objective_label: str = (
                "[Hints: HINT_COST%  Release: RELEASE] Blackout a SIZExSIZE APBingo board in a multiworld "
                "randomizer with GAMES"
            )

            if self.apbingo_release_always_off:
                objective_label = objective_label.replace("Release: RELEASE", "Release: Off")

            game_objective_templates.extend([
                GameObjectiveTemplate(
                    label=objective_label,
                    data={
                        "HINT_COST": (self.hint_costs, 1),
                        "RELEASE": (self.release, 1),
                        "GAMES": (self.games, 2),
                        "SIZE": (self.bingo_board_sizes, 1)
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label=objective_label,
                    data={
                        "HINT_COST": (self.hint_costs, 1),
                        "RELEASE": (self.release, 1),
                        "GAMES": (self.games, 3),
                        "SIZE": (self.bingo_board_sizes, 1)
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=1,
                ),
            ])

        return game_objective_templates

    @property
    def objective_types(self) -> List[str]:
        return sorted(self.archipelago_options.archipelago_multiworld_randomizer_objective_types.value)

    @property
    def include_solo_randomizer_objectives(self) -> bool:
        return "Solo Randomizer" in self.objective_types

    @property
    def include_small_multiworld_randomizer_objectives(self) -> bool:
        return "Small Multiworld Randomizer" in self.objective_types

    @property
    def include_small_multiworld_randomizer_with_apbingo_objectives(self) -> bool:
        return "Small Multiworld Randomizer with APBingo" in self.objective_types

    @property
    def include_apbingo_blackout_objectives(self) -> bool:
        return "APBingo Blackout" in self.objective_types

    @property
    def apbingo_release_always_off(self) -> bool:
        return self.archipelago_options.archipelago_multiworld_randomizer_bingo_release_always_off.value

    @staticmethod
    def hint_costs() -> List[int]:
        return list(range(0, 26)) + [100]

    @staticmethod
    def release() -> List[str]:
        return ["Off", "On", "On", "On", "On"]

    def games(self) -> List[str]:
        games: List[str] = list(self.archipelago_options.archipelago_multiworld_randomizer_game_selection.value)
        return sorted(games)

    @staticmethod
    def bingo_board_sizes() -> List[int]:
        return list(range(3, 11))

    @staticmethod
    def bingo_counts() -> List[int]:
        return list(range(1, 7))


# Archipelago Options
class ArchipelagoMultiworldRandomizerGameSelection(OptionList):
    """
    Defines which APWorlds to select from.

    You can customize this list to your liking. Defaults to all supported games in 0.6.1

    You are allowed to add the same game multiple times here. This will act as a weighted pool.
    """

    display_name = "Archipelago Multiworld Randomizer Game Selection"

    default = [
        "A Hat in Time",
        "A Short Hike",
        "Adventure",
        "Aquaria",
        "Blasphemous",
        "Bomb Rush Cyberfunk",
        "Bumper Stickers",
        "Castlevania",
        "Castlevania: Circle of the Moon",
        "Celeste 64",
        "ChecksFinder",
        "Clique",
        "Dark Souls III",
        "DLC Quest",
        "Donkey Kong Country 3: Dixie Kong's Double Trouble!",
        "DOOM 1993",
        "DOOM II",
        "Factorio",
        "Faxanadu",
        "Final Fantasy",
        "Final Fantasy: Mystic Quest",
        "Heretic",
        "Hollow Knight",
        "Hylics 2",
        "Inscryption",
        "KINGDOM HEARTS FINAL MIX",
        "KINGDOM HEARTS II FINAL MIX",
        "Kirby's Dream Land 3",
        "Landstalker - The Treasures of King Nole",
        "Lingo",
        "Lufia II: Rise of the Sinistrals",
        "Mario & Luigi: Superstar Saga",
        "Mega Man 2",
        "Mega Man Battle Network 3 Blue",
        "Meritous",
        "Minecraft",
        "Muse Dash",
        "Noita",
        "Old School Runescape",
        "Overcooked! 2",
        "Pokémon Emerald",
        "Pokémon Red and Blue",
        "Raft",
        "Risk of Rain 2",
        "Rogue Legacy",
        "Saving Princess",
        "Secret of Evermore",
        "Shivers",
        "Sid Meier's Civilization VI",
        "Slay the Spire",
        "SMZ3",
        "Sonic Adventure 2: Battle",
        "StarCraft II",
        "Stardew Valley",
        "Subnautica",
        "Super Mario 64",
        "Super Mario World",
        "Super Mario World 2: Yoshi's Island",
        "Super Metroid",
        "Terraria",
        "The Legend of Zelda",
        "The Legend of Zelda: A Link to the Past",
        "The Legend of Zelda: Link's Awakening DX",
        "The Legend of Zelda: Ocarina of Time",
        "The Legend of Zelda: The Wind Waker",
        "The Messenger",
        "The Witness",
        "Timespinner",
        "TUNIC",
        "Undertale",
        "VVVVVV",
        "Wargroove",
        "Yacht Dice",
        "Yu-Gi-Oh! Ultimate Masters: WCT 2006",
        "Zillion",
        "Zork: Grand Inquisitor",
    ]


class ArchipelagoMultiworldRandomizerObjectiveTypes(OptionSet):
    """
    Defines which types of Archipelago Multiworld Randomizer objectives to use when generating.
    """

    display_name = "Archipelago Multiworld Randomizer Objective Types"

    valid_keys = [
        "Solo Randomizer",
        "Small Multiworld Randomizer",
        "Small Multiworld Randomizer with APBingo",
        "APBingo Blackout",
    ]

    default = valid_keys


class ArchipelagoMultiworldRandomizerBingoReleaseAlwaysOff(DefaultOnToggle):
    """
    Indicates whether to force the release parameter to always be "Off" for APBingo objectives.
    """

    display_name = "Archipelago Multiworld Randomizer Bingo Release Always Off"

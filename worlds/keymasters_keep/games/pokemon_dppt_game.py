from __future__ import annotations

from typing import List, Set

from dataclasses import dataclass

from Options import OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class PokemonDPPtKeymastersKeepOptions:
    pokemon_dppt_owned_games: PokemonDPPtOwnedGames
    pokemon_dppt_objectives: PokemonDPPtObjectives


class PokemonDPPtGame(Game):
    # Initial implementation by Seafo
    # Based on soopercool101's Pokémon RSE implementation

    name = "Pokémon Diamond, Pearl, and Platinum Versions"
    platform = KeymastersKeepGamePlatforms.NDS

    is_adult_only_or_unrated = False

    options_cls = PokemonDPPtKeymastersKeepOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Use POKEMON as your lead whenever possible",
                data={"POKEMON": (self.wild_pokemon, 1)},
            ),
            GameObjectiveTemplate(
                label="Use POKEMON as your lead whenever possible",
                data={"POKEMON": (self.wild_pokemon, 1)},
            ),
            GameObjectiveTemplate(
                label="Use POKEMON as your lead whenever possible",
                data={"POKEMON": (self.wild_pokemon, 1)},
            ),
            GameObjectiveTemplate(
                label="Use RAREPOKEMON as your lead whenever possible",
                data={"RAREPOKEMON": (self.difficult_pokemon, 1)},
            ),
        ]

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        objectives: List[GameObjectiveTemplate] = list()
        if self.objective_catching:
            objectives += self.catching_objectives()
        if self.objective_contests:
            objectives += self.contest_objectives()
        if self.objective_battles:
            objectives += self.battle_objectives()
        if self.objective_battle_frontier:
            objectives += self.battle_frontier_objectives()
        if len(objectives) == 0:  # Fallback default objectives. Better versions of these exist in other categories
            objectives += [
                GameObjectiveTemplate(
                    label="Without using Fly, travel between the following cities: CITY",
                    data={"CITY": (self.cities, 2)},
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=20
                ),
                GameObjectiveTemplate(
                    label="Encounter a wild POKEMON",
                    data={"POKEMON": (self.wild_pokemon, 1)},
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=70
                ),
                GameObjectiveTemplate(
                    label="Encounter a wild Feebas",
                    data=dict(),
                    is_time_consuming=True,
                    is_difficult=True,
                    weight=1
                ),
            ]

        return objectives

    def catching_objectives(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Catch a wild POKEMON",
                data={"POKEMON": (self.wild_pokemon, 1)},
                is_time_consuming=False,
                is_difficult=False,
                weight=100,
            ),
            GameObjectiveTemplate(
                label="Catch a wild POKEMON in a BALL",
                data={"POKEMON": (self.wild_pokemon, 1), "BALL": (self.poke_ball_types, 1)},
                is_time_consuming=False,
                is_difficult=False,
                weight=70,
            ),
            GameObjectiveTemplate(
                label="Catch a wild Feebas",
                data=dict(),
                is_time_consuming=True,
                is_difficult=True,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Catch a wild Feebas in a BALL",
                data={"BALL": (self.poke_ball_types, 1)},
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Catch a swarming wild Pokémon",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=20,
            ),
            GameObjectiveTemplate(
                label="Catch a swarming wild Pokémon in a BALL",
                data={"BALL": (self.poke_ball_types, 1)},
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Catch a wild POKEMON in the Great Marsh",
                data={"POKEMON": (self.marsh_pokemon, 1)},
                is_time_consuming=True,
                is_difficult=False,
                weight=25,
            ),
            GameObjectiveTemplate(
                label="Catch a wild Pokémon on a Honey Tree",
                data=dict(),
                is_time_consuming=True,
                is_difficult=False,
                weight=15,
            ),
            GameObjectiveTemplate(
                label="Catch a wild Pokémon on a Honey Tree in a BALL",
                data={"BALL": (self.poke_ball_types, 1)},
                is_time_consuming=True,
                is_difficult=False,
                weight=3,
            ),
        ]

    def contest_objectives(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Make a TYPE Poffin",
                data={"TYPE": (self.common_poffin_types, 1)},
                is_time_consuming=False,
                is_difficult=False,
                weight=50,
            ),
            GameObjectiveTemplate(
                label="Make a TYPE Poffin",
                data={"TYPE": (self.rare_poffin_types, 1)},
                is_time_consuming=True,
                is_difficult=True,
                weight=10,
            ),
            GameObjectiveTemplate(
                label="Win a Normal Rank Super Contest",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=30,
            ),
            GameObjectiveTemplate(
                label="Win a Great Rank Super Contest",
                data=dict(),
                is_time_consuming=True,
                is_difficult=False,
                weight=20,
            ),
            GameObjectiveTemplate(
                label="Win an Ultra Rank Super Contest",
                data=dict(),
                is_time_consuming=True,
                is_difficult=False,
                weight=15,
            ),
            GameObjectiveTemplate(
                label="Win a Master Rank Super Contest",
                data=dict(),
                is_time_consuming=True,
                is_difficult=True,
                weight=10,
            ),
            GameObjectiveTemplate(
                label="Win a Normal Rank TYPE Super Contest",
                data={"TYPE": (self.contest_types, 1)},
                is_time_consuming=False,
                is_difficult=False,
                weight=20,
            ),
            GameObjectiveTemplate(
                label="Win a Great Rank TYPE Super Contest",
                data={"TYPE": (self.contest_types, 1)},
                is_time_consuming=True,
                is_difficult=False,
                weight=15,
            ),
            GameObjectiveTemplate(
                label="Win an Ultra Rank TYPE Super Contest",
                data={"TYPE": (self.contest_types, 1)},
                is_time_consuming=True,
                is_difficult=False,
                weight=10,
            ),
            GameObjectiveTemplate(
                label="Win a Master Rank TYPE Super Contest",
                data={"TYPE": (self.contest_types, 1)},
                is_time_consuming=True,
                is_difficult=True,
                weight=8,
            ),
        ]

    def battle_objectives(self) -> List[GameObjectiveTemplate]:
        objectives: List[GameObjectiveTemplate] = [
            GameObjectiveTemplate(
                label="Defeat the Pokémon League and enter the Hall of Fame",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=25,
            ),
            GameObjectiveTemplate(
                label="Defeat a wild POKEMON",
                data={"POKEMON": (self.wild_pokemon, 1)},
                is_time_consuming=False,
                is_difficult=False,
                weight=100,
            ),
            GameObjectiveTemplate(
                label="Defeat the Pokémon League and enter the Hall of Fame with only one Pokémon",
                data=dict(),
                is_time_consuming=False,
                is_difficult=True,
                weight=10,
            ),
            GameObjectiveTemplate(
                label="Without using Fly, items, or a Pokémon Center, travel between the following cities "
                      "and defeat every wild encounter you see: CITY",
                data={"CITY": (self.cities, 2)},
                is_time_consuming=True,
                is_difficult=False,
                weight=35,
            ),
            GameObjectiveTemplate(
                label="Win any Vs. Seeker rematch",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=35,
            ),
        ]

        if self.has_platinum:
            objectives.extend([
                GameObjectiveTemplate(
                    label="Win any battle in the Battleground",
                    data=dict(),
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=5,
                ),
            ])

        return objectives

    def battle_frontier_objectives(self) -> List[GameObjectiveTemplate]:
        if self.has_platinum:
            return [
                GameObjectiveTemplate(
                    label="Win 7 battles in a row in the FACILITY",
                    data={"FACILITY": (self.battle_frontier_facilities, 1)},
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=60,
                ),
                GameObjectiveTemplate(
                    label="Win 10 battles in a row in the Battle Hall",
                    data=dict(),
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=15,
                ),
                GameObjectiveTemplate(
                    label="Win a battle against BRAIN",
                    data={"BRAIN": (self.battle_frontier_brains, 1)},
                    is_time_consuming=True,
                    is_difficult=True,
                    weight=5,
                ),
            ]
        else:
            return [
                GameObjectiveTemplate(
                    label="Win 7 battles in a row in the Battle Tower",
                    data=dict(),
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=20,
                ),
            ]

    @property
    def games_owned(self) -> Set[str]:
        return self.archipelago_options.pokemon_dppt_owned_games.value

    @property
    def has_diamond(self) -> bool:
        return "Diamond" in self.games_owned

    @property
    def has_pearl(self) -> bool:
        return "Pearl" in self.games_owned

    @property
    def has_platinum(self) -> bool:
        return "Platinum" in self.games_owned

    @property
    def objectives(self) -> Set[str]:
        return self.archipelago_options.pokemon_dppt_objectives.value

    @property
    def objective_catching(self) -> bool:
        return "Catching" in self.objectives

    @property
    def objective_contests(self) -> bool:
        return "Contests" in self.objectives

    @property
    def objective_battles(self) -> bool:
        return "Battles" in self.objectives

    @property
    def objective_battle_frontier(self) -> bool:
        return "Battle Frontier" in self.objectives

    def wild_pokemon(self) -> List[str]:
        # List fully in common with all three games
        pokemon: List[str] = self.wild_dppt()[:]

        # Full version exclusives
        if self.has_diamond:
            pokemon.extend(self.wild_d()[:])
        if self.has_pearl:
            pokemon.extend(self.wild_p()[:])
        if self.has_platinum:
            pokemon.extend(self.wild_pt()[:])

        # Exclusive to two games
        if self.has_diamond or self.has_pearl:
            pokemon.extend(self.wild_dp()[:])
        if self.has_diamond or self.has_platinum:
            pokemon.extend(self.wild_dpt()[:])
        if self.has_pearl or self.has_platinum:
            pokemon.extend(self.wild_ppt()[:])

        return pokemon

    def difficult_pokemon(self) -> List[str]:
        # Evolutions, Breeding, and other rare repeatable Pokémon
        pokemon: List[str] = [
            # Evolution exclusive
            "Pidgeotto",
            "Pidgeot",
            "Raichu",
            "Nidoqueen",
            "Nidoking",
            "Clefable",
            "Wigglytuff",
            "Crobat",
            "Vileplume",
            "Bellossom",
            "Parasect",
            "Persian",
            "Poliwrath",
            "Victreebel",
            "Rapidash",
            "Magnezone",
            "Dodrio",
            "Muk",
            "Cloyster",
            "Hypno",
            "Kingler",
            "Electrode",
            "Exeggutor",
            "Marowak",
            "Hitmonlee",
            "Hitmonchan",
            "Hitmontop",
            "Lickilicky",
            "Blissey",
            "Starmie",
            "Vaporeon",
            "Jolteon",
            "Flareon",
            "Espeon",
            "Umbreon",
            "Leafeon",
            "Glaceon",
            "Omastar",
            "Kabutops",
            "Snorlax",
            "Dragonite",
            "Furret",
            "Togetic",
            "Togekiss",
            "Xatu",
            "Ampharos",
            "Jumpluff",
            "Ambipom",
            "Sunflora",
            "Yanmega",
            "Granbull",
            "Weavile",
            "Mamoswine",
            "Mantine",
            "Donphan",
            "Linoone",
            "Gardevoir",
            "Gallade",
            "Breloom",
            "Vigoroth",
            "Slaking",
            "Ninjask",
            "Shedinja",
            "Exploud",
            "Hariyama",
            "Probopass",
            "Delcatty",
            "Manectric",
            "Roserade",
            "Swalot",
            "Grumpig",
            "Altaria",
            "Claydol",
            "Cradily",
            "Armaldo",
            "Milotic",
            "Glalie",
            "Froslass",
            "Metang",
            "Metagross",
            "Staraptor",
            "Luxray",
            "Wormadam",
            "Mothim",
            "Vespiquen",
            "Cherrim",
            "Drifblim",
            "Lopunny",
            "Garchomp",

            # Daily Trophy Garden encounters
            "Igglybuff",
            "Jigglypuff",
            "Meowth",
            "Happiny",
            "Eevee",
            "Azurill",
            "Plusle",
            "Minun",
            "Castform",

            # Daily Great Marsh encounters
            "Paras",
            "Exeggcute",
            "Kangaskhan",
            "Shroomish",
            "Gulpin",
            "Skorupi",
            "Drapion",
            "Toxicroak",
            "Carnivine",

            # Swarm encounters
            "Farfetch'd",
            "Doduo",
            "Drowzee",
            "Krabby",
            "Voltorb",
            "Cubone",
            "Natu",
            "Dunsparce",
            "Snubbull",
            "Corsola",
            "Delibird",
            "Phanpy",
            "Zigzagoon",
            "Slakoth",
            "Makuhita",
            "Skitty",
            "Electrike",
            "Spoink",
            "Spinda",
            "Beldum",

            # Revived from a fossil
            "Omanyte",
            "Kabuto",
            "Aerodactyl",
            "Lileep",
            "Anorith",

            # Honey Tree-only
            "Munchlax",
            "Aipom",
            "Heracross",
            "Burmy",
            "Combee",
            "Cherubi",

            # Time-based
            "Hoothoot",
            "Noctowl",
            "Ledian",
            "Ariados",
            "Banette",
            "Kricketot",
            "Drifloon",  # Specifically date-based
            "Chatot",

            # Breeding exclusive
            "Ledyba",
            "Spinarak",
            "Wynaut",
            "Taillow",
            "Whismur",
            "Shuppet",

            # Great Marsh exclusives
            "Yanma",
            "Carvanha",

            # Absurdly rare
            "Feebas",
        ]

        if self.has_diamond:
            pokemon.append("Murkrow")  # Time-based
            pokemon.append("Honchkrow")  # Evolution-only
            pokemon.append("Cranidos")  # Fossil-only; unreliable availability in Platinum
            pokemon.append("Rampardos")  # Evolution-only

        if self.has_pearl:
            pokemon.append("Misdreavus")  # Time-based
            pokemon.append("Mismagius")  # Evolution-only
            pokemon.append("Shieldon")  # Fossil-only; unreliable availability in Platinum
            pokemon.append("Bastiodon")  # Evolution-only

        if self.has_diamond or self.has_pearl:
            pokemon.append("Porygon")  # Trophy Garden-only
            pokemon.append("Flygon")  # Evolution-only

        if self.has_diamond or self.has_platinum:
            # Evolution-only
            pokemon.append("Pupitar")
            pokemon.append("Tyranitar")
            pokemon.append("Lairon")
            pokemon.append("Aggron")

        if self.has_pearl or self.has_platinum:
            # Evolution-only
            pokemon.append("Slowbro")
            pokemon.append("Walrein")
            pokemon.append("Shelgon")
            pokemon.append("Salamence")

        if self.has_platinum:
            pokemon.extend([
                # Great Marsh-only
                "Tangela",
                "Tropius",
                # Evolution-only
                "Tangrowth",
                # Breeding exclusive
                "Elekid",
                "Magby",
            ][:])

        if not self.has_diamond:
            pokemon.append("Mime Jr.")  # Trophy Garden-only in all other games

        if not self.has_pearl:
            pokemon.append("Bonsly")  # Trophy Garden-only in all other games

        if not self.has_diamond and not self.has_pearl:
            pokemon.extend([
                # Time-based in Platinum
                "Cleffa",
                "Clefairy",
                "Oddish",
                "Bellsprout",
                "Wurmple",
                "Kricketune",
                # Trophy Garden-only in Platinum
                "Ditto",  # PokéRadar in Diamond and Pearl
                # Evolution-only in Platinum
                "Lanturn",
                "Skiploom",  # PokéRadar in Diamond and Pearl
                "Sharpedo",
                # Great Marsh-only in Platinum
                "Wooper",
            ])

        if not self.has_diamond and not self.has_platinum:
            # Evolution-only in Pearl
            pokemon.append("Mr. Mime")
            pokemon.append("Silcoon")

        if not self.has_pearl and not self.has_platinum:
            # Evolution-only in Diamond
            pokemon.append("Sudowoodo")
            pokemon.append("Cascoon")
            pokemon.append("Dustox")

        if not self.has_platinum:
            pokemon.extend([
                # Swarm-only outside of Platinum
                "Pidgey",
                "Magnemite",
                "Lickitung",
                "Smoochum",
                "Swinub",
                "Surskit",
                "Nosepass",
                "Absol",
                # Evolution-only outside of Platinum
                "Magneton",
                "Jynx",
                "Azumarill",
                "Piloswine",  # PokéRadar in Platinum
                "Masquerain",
                "Gabite",
                # Breeding exclusive outside of Platinum
                "Koffing",
                # Great Marsh-only outside of Platinum
                "Marill",
                "Croagunk",
            ][:])

        if self.has_diamond and not self.has_platinum:
            pokemon.append("Poochyena")  # Breeding exclusive in Diamond; PokéRadar in Platinum

        if self.has_pearl and not self.has_platinum:
            pokemon.append("Houndour")  # Breeding exclusive in Pearl

        if not self.has_diamond and self.has_platinum:
            pokemon.append("Seel")  # Breeding exclusive in Platinum
            pokemon.append("Larvitar")  # PokéRader exclusive in Diamond; Swarm-only in Platinum
            pokemon.append("Mightyena")  # PokéRader exclusive in Diamond; Evolution-only in Platinum
            pokemon.append("Kecleon")  # PokéRader exclusive in Diamond; Great Marsh-only in Platinum

        if not self.has_pearl and self.has_platinum:
            pokemon.append("Pinsir")  # Swarm-only in Platinum
            pokemon.append("Houndoom")  # PokéRader exclusive in Pearl; Evolution-only in Platinum
            pokemon.append("Spheal")  # Breeding exclusive in Platinum

        return pokemon

    def marsh_pokemon(self) -> List[str]:
        pokemon: List[str] = self.marsh_dppt()[:]

        if self.has_diamond or self.has_pearl:
            pokemon.extend(self.marsh_dp()[:])

        if self.has_platinum:
            pokemon.extend(self.marsh_pt()[:])

        return pokemon

    @staticmethod
    def poke_ball_types() -> List[str]:
        return [
            "Poké Ball",
            "Great Ball",
            "Ultra Ball",
            "Net Ball",
            "Nest Ball",
            "Repeat Ball",
            "Timer Ball",
            "Luxury Ball",
            "Premier Ball",
            "Dusk Ball",
            "Heal Ball",
            "Quick Ball",
            # Dive and Master Balls *can* be found infinitely, but are too annoying
        ]

    @staticmethod
    def wild_dppt() -> List[str]:
        return [
            "Rattata",
            "Raticate",
            "Spearow",
            "Fearow",
            "Pichu",
            "Pikachu",
            "Female Nidoran",  # PokéRader
            "Nidorina",  # PokéRader
            "Male Nidoran",  # PokéRader
            "Nidorino",  # PokéRader
            "Zubat",
            "Golbat",
            "Gloom",
            "Venonat",  # PokéRader
            "Venomoth",  # PokéRader
            "Diglett",
            "Dugtrio",
            "Psyduck",
            "Golduck",
            "Mankey",  # PokéRader
            "Primeape",  # PokéRader
            "Poliwag",
            "Poliwhirl",
            "Abra",
            "Kadabra",
            "Machop",
            "Machoke",
            "Weepinbell",
            "Tentacool",
            "Tentacruel",
            "Geodude",
            "Graveler",
            "Ponyta",
            "Grimer",  # PokéRader
            "Shellder",
            "Gastly",
            "Haunter",
            "Onix",
            "Steelix",
            "Tyrogue",  # PokéRader
            "Weezing",
            "Rhyhorn",
            "Rhydon",
            "Chansey",
            "Horsea",
            "Seadra",
            "Goldeen",
            "Seaking",
            "Staryu",
            "Tauros",  # PokéRader
            "Magikarp",
            "Gyarados",
            "Lapras",
            "Dratini",
            "Dragonair",
            "Sentret",  # PokéRader
            "Chinchou",
            "Togepi",  # PokéRader
            "Mareep",  # PokéRader
            "Flaaffy",  # PokéRader
            "Hoppip",  # PokéRader
            "Sunkern",  # PokéRader
            "Quagsire",
            "Unown",
            "Wobbuffet",  # PokéRader
            "Girafarig",
            "Qwilfish",
            "Sneasel",
            "Slugma",
            "Magcargo",
            "Remoraid",
            "Octillery",
            "Mantyke",
            "Skarmory",
            "Smeargle",  # PokéRader
            "Miltank",  # PokéRader
            "Beautifly",
            "Swellow",  # PokéRader
            "Wingull",
            "Pelipper",
            "Ralts",  # PokéRader in Diamond and Pearl
            "Kirlia",  # PokéRader in Diamond and Pearl
            "Nincada",  # PokéRader
            "Loudred",  # PokéRader
            "Meditite",
            "Medicham",
            "Volbeat",
            "Illumise",
            "Budew",
            "Roselia",
            "Wailmer",
            "Wailord",
            "Numel",
            "Camerupt",
            "Torkoal",  # PokéRader
            "Cacnea",
            "Cacturne",
            "Swablu",  # PokéRader in Diamond and Pearl
            "Barboach",
            "Whiscash",
            "Corphish",
            "Crawdaunt",
            "Baltoy",  # PokéRader
            "Duskull",  # PokéRader in Diamond and Pearl
            "Dusclops",  # PokéRader in Diamond and Pearl
            "Chingling",
            "Chimecho",
            "Snorunt",  # PokéRader in Diamond and Pearl
            "Relicanth",
            "Luvdisc",
            "Starly",
            "Staravia",
            "Bidoof",
            "Bibarel",
            "Shinx",
            "Luxio",
            "Pachirisu",
            "Buizel",
            "Floatzel",
            "West Sea Shellos",
            "East Sea Shellos",
            "West Sea Gastrodon",
            "East Sea Gastrodon",
            "Buneary",
            "Bronzor",
            "Bronzong",
            "Gible",
            "Hippopotas",
            "Hippowdon",
            "Finneon",
            "Lumineon",
            "Snover",
            "Abomasnow",
        ]

    @staticmethod
    def wild_dp() -> List[str]:
        return [
            "Cleffa",
            "Clefairy",
            "Oddish",
            "Bellsprout",
            "Ditto",  # PokéRader
            "Lanturn",
            "Skiploom",  # PokéRader
            "Wurmple",
            "Sharpedo",
            "Trapinch",  # PokéRader
            "Vibrava",  # PokéRader
            "Clamperl",
            "Kricketune",
        ]

    @staticmethod
    def wild_d() -> List[str]:
        return [
            "Seel",
            "Mime Jr.",
            "Larvitar",  # PokéRader
            "Mightyena",  # PokéRader
            "Kecleon",  # PokéRader
            "Stunky",
            "Skuntank",
        ]

    @staticmethod
    def wild_dpt() -> List[str]:
        return [
            "Dewgong",
            "Mr. Mime",
            "Scyther",
            "Silcoon",
        ]

    @staticmethod
    def wild_p() -> List[str]:
        return [
            "Pinsir",
            "Bonsly",
            "Houndoom",  # PokéRader
            "Spheal",
            "Glameow",
            "Purugly",
        ]

    @staticmethod
    def wild_ppt() -> List[str]:
        return [
            "Slowpoke",  # PokéRader
            "Sudowoodo",
            "Stantler",  # PokéRader
            "Cascoon",
            "Dustox",
            "Sealeo",
            "Bagon",  # PokéRader
        ]

    @staticmethod
    def wild_pt() -> List[str]:
        return [
            "Pidgey",
            "Magnemite",
            "Magneton",
            "Lickitung",
            "Koffing",
            "Smoochum",
            "Jynx",
            "Electabuzz",
            "Magmar",
            "Marill",
            "Azumarill",
            "Gligar",
            "Swinub",
            "Piloswine",  # PokéRader
            "Houndour",
            "Poochyena",  # PokéRader
            "Surskit",
            "Masquerain",
            "Nosepass",
            "Absol",
            "Gabite",
            "Croagunk",
        ]

    @staticmethod
    def marsh_dppt() -> List[str]:
        return [
            "Magikarp",
            "Gyarados",
            "Hoothoot",  # Time-based
            "Noctowl",  # Time-based
            "Wooper",
            "Quagsire",
            "Carvanha",
            "Barboach",
            "Whiscash",
            "Bibarel",
        ]

    @staticmethod
    def marsh_dp() -> List[str]:
        return [
            "Psyduck",
            "Azurill",
            "Marill",
            "Budew",  # Time-based
            "Starly",  # Time-based
            "Bidoof",
        ]

    @staticmethod
    def marsh_pt() -> List[str]:
        return [
            "Tangela",
            "Yanma",
            "Tropius",  # Time-based
        ]

    @staticmethod
    def common_poffin_types() -> List[str]:
        return [
            "Spicy",
            "Dry",
            "Sweet",
            "Bitter",
            "Sour",
        ]

    @staticmethod
    def rare_poffin_types() -> List[str]:
        return [
            "Spicy-Dry",
            "Spicy-Sweet",
            "Spicy-Bitter",
            "Spicy-Sour",
            "Dry-Sweet",
            "Dry-Bitter",
            "Dry-Sour",
            "Sweet-Spicy",
            "Sweet-Bitter",
            "Sweet-Sour",
            "Bitter-Spicy",
            "Bitter-Dry",
            "Bitter-Sour",
            "Sour-Spicy",
            "Sour-Dry",
            "Sour-Sweet",
        ]

    # Contest ranks are currently all handled individually, so they don't really need to be defined here.
    # @staticmethod
    # def base_contest_ranks() -> List[str]:
    #     return [
    #         "Normal",
    #         "Great",
    #         "Hyper",
    #         "Master",
    #     ]

    @staticmethod
    def contest_types() -> List[str]:
        return [
            "Cool",
            "Beauty",
            "Cute",
            "Smart",
            "Tough"
        ]

    @staticmethod
    def cities() -> List[str]:
        return [
            "Twinleaf Town",
            "Sandgem Town",
            "Jubilife City",
            "Oreburgh City",
            "Floaroma Town",
            "Eterna City",
            "Hearthome City",
            "Solaceon Town",
            "Veilstone City",
            "Pastoria City",
            "Celestic Town",
            "Canalave City",
            "Snowpoint City",
            "Sunyshore City",
            "Pokémon League (South)",
            "Pokémon League (North)",
            "Battle Area",
            "Survival Area",
            "Resort Area",
        ]

    @staticmethod
    def battle_frontier_facilities() -> List[str]:
        return [
            "Battle Tower",
            "Battle Factory",
            "Battle Arcade",
            "Battle Castle",
            # "Battle Hall", # Slightly different objective than the others
        ]

    @staticmethod
    def battle_frontier_brains() -> List[str]:
        return [
            "Tower Tycoon Palmer",
            "Factory Head Thorton",
            "Arcade Star Dahlia",
            "Castle Valet Darach",
            "Hall Matron Argenta",
        ]


# Archipelago Options
class PokemonDPPtOwnedGames(OptionSet):
    """
    Indicates which versions of the games the player owns between Pokémon Diamond/Pearl/Platinum.
    """

    display_name = "Pokémon Diamond/Pearl/Platinum Owned Games"
    valid_keys = [
        "Diamond",
        "Pearl",
        "Platinum"
    ]

    default = valid_keys


class PokemonDPPtObjectives(OptionSet):
    """
    Indicates which objective types the player would like to engage in for Pokémon Diamond/Pearl/Platinum.
    """
    display_name = "Pokémon Diamond/Pearl/Platinum Objective Types"
    valid_keys = [
        "Catching",
        "Contests",
        "Battles",
        "Battle Frontier",
    ]

    default = valid_keys

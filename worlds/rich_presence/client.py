import asyncio
import sys
import time
import urllib.parse

import CommonClient
import Utils

from typing import Any, Dict, List, Optional, Set, Tuple

from .discord_rich_presence import Presence


class DiscordRichPresenceCommandProcessor(CommonClient.ClientCommandProcessor):
    pass


class DiscordRichPresenceContext(CommonClient.CommonContext):
    tags: Set[str] = {"AP", "TextOnly"}
    command_processor: CommonClient.ClientCommandProcessor = DiscordRichPresenceCommandProcessor
    items_handling: int = 0b111
    want_slot_data: bool = False

    timestamp: Optional[int] = None

    rich_presence: Optional[Presence] = None

    state_game: Optional[str] = None
    state_player_count: int = 0
    state_last_location_checked: str = "Nothing Yet"

    def __init__(self, server_address: Optional[str], password: Optional[str]) -> None:
        super().__init__(server_address, password)

        self.timestamp = int(time.time())

        self.rich_presence = Presence("1339447230909644851")
        self.set_rich_presence()

    @property
    def game_to_title(self) -> str:
        if not self.state_game:
            return "Not Connected"

        mapping: Dict[str, str] = {
            "A Difficult Game About Climbing": "A Difficult Game About Climbing",
            "A Hat in Time": "A Hat in Time",
            "A Link Between Worlds": "The Legend of Zelda: A Link Between Worlds",
            "A Link to the Past": "The Legend of Zelda: A Link to the Past",
            "A Short Hike": "A Short Hike",
            "ANIMAL WELL": "ANIMAL WELL",
            "Actraiser": "ActRaiser",
            "Adventure": "Adventure",
            "Against the Storm": "Against the Storm",
            "Air Delivery": "Air Delivery",
            "An Untitled Story": "An Untitled Story",
            "Anodyne": "Anodyne",
            "Another Crabs Treasure": "Another Crab's Treasure",
            "Ape Escape": "Ape Escape",
            "Aquaria": "Aquaria",
            "Astalon": "Astalon: Tears of the Earth",
            "Balatro": "Balatro",
            "Banjo-Tooie": "Banjo-Tooie",
            "Battle for Bikini Bottom": "SpongeBob SquarePants: Battle for Bikini Bottom",
            "Blasphemous": "Blasphemous",
            "Bloons TD6": "Bloons TD 6",
            "Bomb Rush Cyberfunk": "Bomb Rush Cyberfunk",
            "Bomberman 64": "Bomberman 64",
            "Bomberman The Second Attack": "Bomberman 64: The Second Attack!",
            "Bomberman Hero": "Bomberman Hero",
            "Brotato": "Brotato",
            "Castlevania - Circle of the Moon": "Castlevania: Circle of the Moon",
            "Castlevania - Harmony of Dissonance": "Castlevania: Harmony of Dissonance",
            "Castlevania 64": "Castlevania 64",
            "Cat Quest": "Cat Quest",
            "Cave Story": "Cave Story",
            "Cavern of Dreams": "Cavern of Dreams",
            "Celeste 64": "Celeste 64",
            "Celeste": "Celeste",
            "Chrono Trigger Jets of Time": "Chrono Trigger",
            "Civilization V": "Sid Meier's Civilization V",
            "Civilization VI": "Sid Meier's Civilization VI",
            "ClusterTruck": "Clustertruck",
            "Corn Kidz 64": "Corn Kidz 64",
            "CrossCode": "CrossCode",
            "Crystalis": "Crystalis",
            "Cuphead": "Cuphead",
            "DLCQuest": "DLC Quest",
            "DOOM 1993": "DOOM (1993)",
            "DOOM II": "DOOM II",
            "DORONKO WANKO": "DORONKO WANKO",
            "Dark Souls II": "Dark Souls II",
            "Dark Souls III": "Dark Souls III",
            "Dark Souls Remastered": "Dark Souls: Remastered",
            "Deep Rock Galactic": "Deep Rock Galactic",
            "Diddy Kong Racing": "Diddy Kong Racing",
            "Digimon World": "Digimon World",
            "Dome Keeper": "Dome Keeper",
            "Don't Starve Together": "Don't Starve Together",
            "Donkey Kong 64": "Donkey Kong 64",
            "Donkey Kong Country 2": "Donkey Kong Country 2",
            "Donkey Kong Country 3": "Donkey Kong Country 3",
            "Duke Nukem 3D": "Duke Nukem 3D",
            "Dungeon Clawler": "Dungeon Clawler",
            "EarthBound": "EarthBound",
            "Ender Lilies": "Ender Lilies: Quietus of the Knights",
            "Enter The Gungeon": "Enter the Gungeon",
            "FFPS": "Freddy Fazbear's Pizzeria Simulator",
            "FNaFW": "FNaF World",
            "Factorio": "Factorio",
            "Faxanadu": "Faxanadu",
            "Final Fantasy 12 Open World": "Final Fantasy XII",
            "Final Fantasy 6 Worlds Collide": "Final Fantasy VI",
            "Final Fantasy IV Free Enterprise": "Final Fantasy IV",
            "Final Fantasy Mystic Quest": "Final Fantasy: Mystic Quest",
            "Final Fantasy Tactics A2": "Final Fantasy Tactics A2",
            "Final Fantasy Tactics Advance": "Final Fantasy Tactics Advance",
            "Final Fantasy XII Trial Mode": "Final Fantasy XII",
            "Final Fantasy XIV": "Final Fantasy XIV",
            "Final Fantasy": "Final Fantasy",
            "Fire Emblem Sacred Stones": "Fire Emblem: The Sacred Stones",
            "Frogmonster": "Frogmonster",
            "Gauntlet Legends": "Gauntlet Legends",
            "Getting Over It": "Getting Over It with Bennett Foddy",
            "Golden Sun The Lost Age": "Golden Sun: The Lost Age",
            "Grim Dawn": "Grim Dawn",
            "Guild Wars 2": "Guild Wars 2",
            "Hades": "Hades",
            "Hammerwatch": "Hammerwatch",
            "Hatsune Miku Project Diva Mega Mix+": "Hatsune Miku: Project Diva Mega Mix+",
            "Here Comes Niko!": "Here Comes Niko!",
            "Heretic": "Heretic",
            "Hollow Knight": "Hollow Knight",
            "Hylics 2": "Hylics 2",
            "Inscryption": "Inscryption",
            "Into the Breach": "Into the Breach",
            "Ittle Dew 2": "Ittle Dew 2+",
            "Jak and Daxter The Precursor Legacy": "Jak and Daxter: The Precursor Legacy",
            "Keep Talking and Nobody Explodes": "Keep Talking and Nobody Explodes",
            "Kindergarten 2": "Kindergarten 2",
            "Kingdom Hearts 2": "KINGDOM HEARTS II FINAL MIX",
            "Kingdom Hearts Birth by Sleep": "KINGDOM HEARTS Birth by Sleep",
            "Kingdom Hearts RE Chain of Memories": "KINGDOM HEARTS Re:Chain of Memories",
            "Kingdom Hearts": "KINGDOM HEARTS FINAL MIX",
            "Kirby 64 - The Crystal Shards": "Kirby 64: The Crystal Shards",
            "Kirby Super Star": "Kirby Super Star",
            "Kirby's Dream Land 3": "Kirby's Dream Land 3",
            "Landstalker - The Treasures of King Nole": "Landstalker - The Treasures of King Nole",
            "League of Legends": "League of Legends",
            "Lethal Company": "Lethal Company",
            "Lil Gator Game": "Lil Gator Game",
            "Lingo": "Lingo",
            "Links Awakening DX Beta": "The Legend of Zelda: Link's Awakening DX",
            "Links Awakening DX": "The Legend of Zelda: Link's Awakening DX",
            "Lufia II Ancient Cave": "Lufia II: Rise of the Sinistrals",
            "Luigi's Mansion": "Luigi's Mansion",
            "Lunacid": "Lunacid",
            "Majora's Mask Recompiled": "The Legend of Zelda: Majora's Mask",
            "Mario & Luigi Superstar Saga": "Mario & Luigi: Superstar Saga",
            "Mario Kart 64": "Mario Kart 64",
            "Mega Man 2": "Mega Man 2",
            "Mega Man 3": "Mega Man 3",
            "Mega Man X": "Mega Man X",
            "Mega Man X2": "Mega Man X2",
            "Mega Man X3": "Mega Man X3",
            "MegaMan Battle Network 3": "Mega Man Battle Network 3",
            "MetroCUBEvania": "MetroCUBEvania",
            "Metroid Prime": "Metroid Prime",
            "Metroid Zero Mission": "Metroid: Zero Mission",
            "Mindustry": "Mindustry",
            "Minecraft Dig": "Minecraft",
            "Minecraft": "Minecraft",
            "Minishoot Adventures": "Minishoot' Adventures",
            "Minit": "Minit",
            "Momodora Moonlit Farewell": "Momodora: Moonlit Farewell",
            "Monster Sanctuary": "Monster Sanctuary",
            "Muse Dash": "Muse Dash",
            "Nine Sols": "Nine Sols",
            "Nodebuster": "Nodebuster",
            "Noita": "Noita",
            "Ocarina of Time": "The Legend of Zelda: Ocarina of Time",
            "Old School Runescape": "Old School RuneScape",
            "OpenRCT2": "OpenRCT2",
            "Ori and the Blind Forest": "Ori and the Blind Forest",
            "Ori and the Will of the Wisps": "Ori and the Will of the Wisps",
            "Outer Wilds": "Outer Wilds",
            "Overcooked! 2": "Overcooked! 2",
            "Oxygen Not Included": "Oxygen Not Included",
            "Paper Mario": "Paper Mario",
            "Peaks of Yore": "Peaks of Yore",
            "plateup": "PlateUp!",
            "Pokemon Crystal": "Pokémon Crystal",
            "Pokemon Emerald": "Pokémon Emerald",
            "Pokemon FireRed and LeafGreen": "Pokémon FireRed and LeafGreen",
            "Pokemon Mystery Dungeon Explorers of Sky": "Pokémon Mystery Dungeon: Explorers of Sky",
            "Pokemon Red and Blue": "Pokémon Red and Blue",
            "Prodigal": "Prodigal",
            "Pseudoregalia": "Pseudoregalia",
            "Psychonauts": "Psychonauts",
            "Quake 1": "Quake",
            "Rabi-Ribi": "Rabi-Ribi",
            "Raft": "Raft",
            "Rain World": "Rain World",
            "Ratchet & Clank 2": "Ratchet & Clank: Going Commando",
            "Resident Evil 2 Remake": "Resident Evil 2 (Remake)",
            "Resident Evil 3 Remake": "Resident Evil 3 (Remake)",
            "Reventure": "Reventure",
            "Rift of the Necrodancer": "Rift of the NecroDancer",
            "Rift Wizard": "Rift Wizard",
            "Risk of Rain 2": "Risk of Rain 2",
            "Risk of Rain": "Risk of Rain",
            "Rogue Legacy": "Rogue Legacy",
            "Rusted Moss": "Rusted Moss",
            "Satisfactory": "Satisfactory",
            "Scooby-Doo! Night of 100 Frights": "Scooby-Doo! Night of 100 Frights",
            "Sea of Thieves": "Sea of Thieves",
            "Secret of Evermore": "Secret of Evermore",
            "Sentinels of the Multiverse": "Sentinels of the Multiverse",
            "Shadow The Hedgehog": "Shadow the Hedgehog",
            "Shivers": "Shivers",
            "Skyward Sword": "The Legend of Zelda: Skyward Sword",
            "Slay the Spire": "Slay the Spire",
            "Sly Cooper and the Thievius Raccoonus": "Sly Cooper and the Thievius Raccoonus",
            "Sonic Adventure 2 Battle": "Sonic Adventure 2: Battle",
            "Sonic Adventure DX": "Sonic Adventure DX",
            "Sonic Heroes": "Sonic Heroes",
            "Sonic Riders": "Sonic Riders",
            "Sonic the Hedgehog 1": "Sonic the Hedgehog",
            "Soul Blazer": "Soul Blazer",
            "Spelunker": "Spelunker",
            "Spelunky 2": "Spelunky 2",
            "Stacklands": "Stacklands",
            "Star Fox 64": "Star Fox 64",
            "Star Wars Episode I Racer": "Star Wars: Episode I - Racer",
            "Starcraft 2": "StarCraft II",
            "Stardew Valley": "Stardew Valley",
            "Subnautica": "Subnautica",
            "Subversion": "Super Metroid: Subversion",
            "Super Cat Planet": "Super Cat Planet",
            "Super Junkoid": "Super Junkoid",
            "Super Mario 64": "Super Mario 64",
            "Super Mario Land 2": "Super Mario Land 2: 6 Golden Coins",
            "Super Mario RPG Legend of the Seven Stars": "Super Mario RPG: Legend of the Seven Stars",
            "Super Mario Sunshine": "Super Mario Sunshine",
            "Super Mario World": "Super Mario World",
            "Super Metroid Map Rando": "Super Metroid",
            "Super Metroid": "Super Metroid",
            "Symphony of the Night": "Castlevania: Symphony of the Night",
            "System Shock 2": "System Shock 2",
            "TUNIC": "TUNIC",
            "Tetris Attack": "Tetris Attack",
            "Terraria": "Terraria",
            "Tevi": "TEVI",
            "The Binding of Isaac Repentance": "The Binding of Isaac: Repentance",
            "The Guardian Legend": "The Guardian Legend",
            "The Legend of Zelda - Oracle of Ages": "The Legend of Zelda: Oracle of Ages",
            "The Legend of Zelda - Oracle of Seasons": "The Legend of Zelda: Oracle of Seasons",
            "The Legend of Zelda": "The Legend of Zelda",
            "The Messenger": "The Messenger",
            "The Minish Cap": "The Legend of Zelda: The Minish Cap",
            "The Simpsons Hit And Run": "The Simpsons: Hit & Run",
            "The Sims 4": "The Sims 4",
            "The Wind Waker": "The Legend of Zelda: The Wind Waker",
            "The Witness": "The Witness",
            "Timespinner": "Timespinner",
            "ToeJam and Earl": "ToeJam & Earl",
            "Touhou 6": "Touhou 6: Embodiment of Scarlet Devil",
            "Trails in the Sky the 3rd": "The Legend of Heroes: Trails in the Sky the 3rd",
            "TurnipBoy": "Turnip Boy Commits Tax Evasion",
            "Twilight Princess": "The Legend of Zelda: Twilight Princess",
            "Ty the Tasmanian Tiger": "Ty the Tasmanian Tiger",
            "Tyrian": "Tyrian",
            "UFO 50": "UFO 50",
            "ULTRAKILL": "ULTRAKILL",
            "Undertale": "Undertale",
            "VVVVVV": "VVVVVV",
            "Void Stranger": "Void Stranger",
            "WEBFISHING": "WEBFISHING",
            "Wargroove 2": "Wargroove 2",
            "Wargroove": "Wargroove",
            "Wario Land 4": "Wario Land 4",
            "Wario Land": "Wario Land: Super Mario Land 3",
            "XCOM 2 War of the Chosen": "XCOM 2: War of the Chosen",
            "Xenoblade X": "Xenoblade Chronicles X",
            "Yoku's Island Express": "Yoku's Island Express",
            "Yooka-Laylee": "Yooka-Laylee",
            "Yoshi's Island": "Super Mario World 2: Yoshi's Island",
            "Yu-Gi-Oh! 2006": "Yu-Gi-Oh! Ultimate Masters: WCT 2006",
            "Yu-Gi-Oh! Dungeon Dice Monsters": "Yu-Gi-Oh! Dungeon Dice Monsters",
            "Yu-Gi-Oh! Forbidden Memories": "Yu-Gi-Oh! Forbidden Memories",
            "Yu-Gi-Oh! GX: Duel Academy": "Yu-Gi-Oh! GX: Duel Academy",
            "Zelda II: The Adventure of Link": "Zelda II: The Adventure of Link",
            "Zillion": "Zillion",
            "Zork Grand Inquisitor": "Zork: Grand Inquisitor",
            "osu!": "Osu!",
            "shapez": "Shapez",
            "shapez 2": "Shapez 2",
        }

        return mapping.get(self.state_game, self.state_game)

    @property
    def game_to_image_key(self) -> Optional[str]:
        if not self.state_game:
            return None

        mapping: Dict[str, str] = {
            "A Difficult Game About Climbing": "adifficultgameaboutclimbing",
            "A Hat in Time": "ahatintime",
            "A Link Between Worlds": "thelegendofzeldaalinkbetweenworlds",
            "A Link to the Past": "thelegendofzeldaalinktothepast",
            "A Short Hike": "ashorthike",
            "ANIMAL WELL": "animalwell",
            "Actraiser": "actraiser",
            "Adventure": "adventure",
            "Against the Storm": "againstthestorm",
            "Air Delivery": "airdelivery",
            "An Untitled Story": "anuntitledstory",
            "Anodyne": "anodyne",
            "Another Crabs Treasure": "anothercrabstreasure",
            "Ape Escape": "apeescape",
            "Aquaria": "aquaria",
            "Astalon": "astalon",
            "Balatro": "balatro",
            "Banjo-Tooie": "banjotooie",
            "Battle for Bikini Bottom": "spongebobsquarepantsbattleforbikinibottom",
            "Blasphemous": "blasphemous",
            "Bloons TD6": "bloonstd6",
            "Bomb Rush Cyberfunk": "bombrushcyberfunk",
            "Bomberman 64": "bomberman64",
            "Bomberman The Second Attack": "bomberman64thesecondattack",
            "Bomberman Hero": "bombermanhero",
            "Brotato": "brotato",
            "Castlevania - Circle of the Moon": "castlevaniacircleofthemoon",
            "Castlevania - Harmony of Dissonance": "castlevaniaharmonyofdissonance",
            "Castlevania 64": "castlevania64",
            "Cat Quest": "catquest",
            "Cave Story": "cavestory",
            "Cavern of Dreams": "cavernofdreams",
            "Celeste 64": "celeste64",
            "Celeste": "celeste",
            "Chrono Trigger Jets of Time": "chronotrigger",
            "Civilization V": "sidmeierscivilizationv",
            "Civilization VI": "sidmeierscivilizationvi",
            "ClusterTruck": "clustertruck",
            "Corn Kidz 64": "cornkidz64",
            "CrossCode": "crosscode",
            "Crystalis": "crystalis",
            "Cuphead": "cuphead",
            "DLCQuest": "dlcquest",
            "DOOM 1993": "doom1993",
            "DOOM II": "doom2",
            "DORONKO WANKO": "doronkowanko",
            "Dark Souls II": "darksouls2",
            "Dark Souls III": "darksouls3",
            "Dark Souls Remastered": "darksoulsremastered",
            "Deep Rock Galactic": "deeprockgalactic",
            "Diddy Kong Racing": "diddykongracing",
            "Digimon World": "digimonworld",
            "Dome Keeper": "domekeeper",
            "Don't Starve Together": "dontstarvetogether",
            "Donkey Kong 64": "donkeykong64",
            "Donkey Kong Country 2": "donkeykongcountry2",
            "Donkey Kong Country 3": "donkeykongcountry3",
            "Duke Nukem 3D": "dukenukem3d",
            "Dungeon Clawler": "dungeonclawler",
            "EarthBound": "earthbound",
            "Ender Lilies": "enderlilies",
            "Enter The Gungeon": "enterthegungeon",
            "FFPS": "freddyfazbearspizzeriasimulator",
            "FNaFW": "fnafworld",
            "Factorio": "factorio",
            "Faxanadu": "faxanadu",
            "Final Fantasy 12 Open World": "finalfantasy12",
            "Final Fantasy 6 Worlds Collide": "finalfantasy6",
            "Final Fantasy IV Free Enterprise": "finalfantasy4",
            "Final Fantasy Mystic Quest": "finalfantasymysticquest",
            "Final Fantasy Tactics A2": "finalfantasytacticsa2",
            "Final Fantasy Tactics Advance": "finalfantasytacticsadvance",
            "Final Fantasy XII Trial Mode": "finalfantasy12",
            "Final Fantasy XIV": "finalfantasy14",
            "Final Fantasy": "finalfantasy",
            "Fire Emblem Sacred Stones": "fireemblemthesacredstones",
            "Frogmonster": "frogmonster",
            "Gauntlet Legends": "gauntletlegends",
            "Getting Over It": "gettingoverit",
            "Golden Sun The Lost Age": "goldensunthelostage",
            "Grim Dawn": "grimdawn",
            "Guild Wars 2": "guildwars2",
            "Hades": "hades",
            "Hammerwatch": "hammerwatch",
            "Hatsune Miku Project Diva Mega Mix+": "hatsunemikuprojectdivamegamix",
            "Here Comes Niko!": "herecomesniko",
            "Heretic": "heretic",
            "Hollow Knight": "hollowknight",
            "Hylics 2": "hylics2",
            "Inscryption": "inscryption",
            "Into the Breach": "intothebreach",
            "Ittle Dew 2": "ittledew2",
            "Jak and Daxter The Precursor Legacy": "jakanddaxtertheprecursorlegacy",
            "Keep Talking and Nobody Explodes": "keeptalkingandnobodyexplodes",
            "Kindergarten 2": "kindergarten2",
            "Kingdom Hearts 2": "kingdomhearts2finalmix",
            "Kingdom Hearts Birth by Sleep": "kingdomheartsbirthbysleep",
            "Kingdom Hearts RE Chain of Memories": "kingdomheartsrechainofmemories",
            "Kingdom Hearts": "kingdomheartsfinalmix",
            "Kirby 64 - The Crystal Shards": "kirby64thecrystalshards",
            "Kirby Super Star": "kirbysuperstar",
            "Kirby's Dream Land 3": "kirbysdreamland3",
            "Landstalker - The Treasures of King Nole": "landstalkerthetreasuresofkingnole",
            "League of Legends": "leagueoflegends",
            "Lethal Company": "lethalcompany",
            "Lil Gator Game": "lilgatorgame",
            "Lingo": "lingo",
            "Links Awakening DX Beta": "thelegendofzeldalinksawakeningdx",
            "Links Awakening DX": "thelegendofzeldalinksawakeningdx",
            "Lufia II Ancient Cave": "lufiaiiriseofthesinistrals",
            "Luigi's Mansion": "luigismansion",
            "Lunacid": "lunacid",
            "Majora's Mask Recompiled": "thelegendofzeldamajorasmask",
            "Mario & Luigi Superstar Saga": "marioluigisuperstarsaga",
            "Mario Kart 64": "mariokart64",
            "Mega Man 2": "megaman2",
            "Mega Man 3": "megaman3",
            "Mega Man X": "megamanx",
            "Mega Man X2": "megamanx2",
            "Mega Man X3": "megamanx3",
            "MegaMan Battle Network 3": "megamanbattlenetwork3",
            "MetroCUBEvania": "metrocubevania",
            "Metroid Prime": "metroidprime",
            "Metroid Zero Mission": "metroidzeromission",
            "Mindustry": "mindustry",
            "Minecraft Dig": "minecraft",
            "Minecraft": "minecraft",
            "Minishoot Adventures": "minishootadventures",
            "Minit": "minit",
            "Momodora Moonlit Farewell": "momodoramoonlitfarewell",
            "Monster Sanctuary": "monstersanctuary",
            "Muse Dash": "musedash",
            "Nine Sols": "ninesols",
            "Nodebuster": "nodebuster",
            "Noita": "noita",
            "Ocarina of Time": "thelegendofzeldaocarinaoftime",
            "Old School Runescape": "oldschoolrunescape",
            "OpenRCT2": "openrct2",
            "Ori and the Blind Forest": "oriandtheblindforest",
            "Ori and the Will of the Wisps": "oriandthewillofthewisps",
            "Outer Wilds": "outerwilds",
            "Overcooked! 2": "overcooked2",
            "Oxygen Not Included": "oxygennotincluded",
            "Paper Mario": "papermario",
            "Peaks of Yore": "peaksofyore",
            "Pokemon Crystal": "pokemoncrystal",
            "Pokemon Emerald": "pokemonemerald",
            "Pokemon FireRed and LeafGreen": "pokemonfireredandleafgreen",
            "Pokemon Mystery Dungeon Explorers of Sky": "pokemonmysterydungeonexplorersofsky",
            "Pokemon Red and Blue": "pokemonredandblue",
            "Prodigal": "prodigal",
            "Pseudoregalia": "pseudoregalia",
            "Psychonauts": "psychonauts",
            "Quake 1": "quake",
            "Rabi-Ribi": "rabiribi",
            "Raft": "raft",
            "Rain World": "rainworld",
            "Ratchet & Clank 2": "ratchetandclankgoingcommando",
            "Resident Evil 2 Remake": "residentevil2remake",
            "Resident Evil 3 Remake": "residentevil3remake",
            "Reventure": "reventure",
            "Rift of the Necrodancer": "riftofthenecrodancer",
            "Rift Wizard": "riftwizard",
            "Risk of Rain 2": "riskofrain2",
            "Risk of Rain": "riskofrain",
            "Rogue Legacy": "roguelegacy",
            "Rusted Moss": "rustedmoss",
            "Satisfactory": "satisfactory",
            "Scooby-Doo! Night of 100 Frights": "scoobydoonightof100frights",
            "Sea of Thieves": "seaofthieves",
            "Secret of Evermore": "secretofevermore",
            "Sentinels of the Multiverse": "sentinelsofthemultiverse",
            "Shadow The Hedgehog": "shadowthehedgehog",
            "Shivers": "shivers",
            "Skyward Sword": "thelegendofzeldaskywardsword",
            "Slay the Spire": "slaythespire",
            "Sly Cooper and the Thievius Raccoonus": "slycooperandthethieviusraccoonus",
            "Sonic Adventure 2 Battle": "sonicadventure2battle",
            "Sonic Adventure DX": "sonicadventuredx",
            "Sonic Heroes": "sonicheroes",
            "Sonic Riders": "sonicriders",
            "Sonic the Hedgehog 1": "sonicthehedgehog",
            "Soul Blazer": "soulblazer",
            "Spelunker": "spelunker",
            "Spelunky 2": "spelunky2",
            "Stacklands": "stacklands",
            "Star Fox 64": "starfox64",
            "Star Wars Episode I Racer": "starwarsepisodeiracer",
            "Starcraft 2": "starcraft2",
            "Stardew Valley": "stardewvalley",
            "Subnautica": "subnautica",
            "Subversion": "supermetroidsubversion",
            "Super Cat Planet": "supercatplanet",
            "Super Junkoid": "superjunkoid",
            "Super Mario 64": "supermario64",
            "Super Mario Land 2": "supermarioland26goldencoins",
            "Super Mario RPG Legend of the Seven Stars": "supermariorpglegendofthesevenstars",
            "Super Mario Sunshine": "supermariosunshine",
            "Super Mario World": "supermarioworld",
            "Super Metroid Map Rando": "supermetroid",
            "Super Metroid": "supermetroid",
            "Symphony of the Night": "symphonyofthenight",
            "System Shock 2": "systemshock2",
            "TUNIC": "tunic",
            "Tetris Attack": "tetrisattack",
            "Terraria": "terraria",
            "Tevi": "tevi",
            "The Binding of Isaac Repentance": "thebindingofisaacrepentance",
            "The Guardian Legend": "theguardianlegend",
            "The Legend of Zelda - Oracle of Ages": "thelegendofzeldaoracleofages",
            "The Legend of Zelda - Oracle of Seasons": "thelegendofzeldaoracleofseasons",
            "The Legend of Zelda": "thelegendofzelda",
            "The Messenger": "themessenger",
            "The Minish Cap": "thelegendofzeldatheminishcap",
            "The Simpsons Hit And Run": "thesimpsonshitandrun",
            "The Sims 4": "thesims4",
            "The Wind Waker": "thelegendofzeldathewindwaker",
            "The Witness": "thewitness",
            "Timespinner": "timespinner",
            "ToeJam and Earl": "toejamandearl",
            "Touhou 6": "touhou6embodimentofscarletdevil",
            "Trails in the Sky the 3rd": "thelegendofheroestrailsintheskythe3rd",
            "TurnipBoy": "turnipboycommitstaxevasion",
            "Twilight Princess": "thelegendofzeldatwilightprincess",
            "Ty the Tasmanian Tiger": "tythetasmaniantiger",
            "Tyrian": "tyrian",
            "UFO 50": "ufo50",
            "ULTRAKILL": "ultrakill",
            "Undertale": "undertale",
            "VVVVVV": "vvvvvv",
            "Void Stranger": "voidstranger",
            "WEBFISHING": "webfishing",
            "Wargroove 2": "wargroove2",
            "Wargroove": "wargroove",
            "Wario Land 4": "warioland4",
            "Wario Land": "wariolandsupermarioland3",
            "XCOM 2 War of the Chosen": "xcom2warofthechosen",
            "Xenoblade X": "xenobladechroniclesx",
            "Yoku's Island Express": "yokusislandexpress",
            "Yooka-Laylee": "yookalaylee",
            "Yoshi's Island": "supermarioworld2yoshisisland",
            "Yu-Gi-Oh! 2006": "yugiohultimatemasterswct2006",
            "Yu-Gi-Oh! Dungeon Dice Monsters": "yugiohdungeondicemonsters",
            "Yu-Gi-Oh! Forbidden Memories": "yugiohforbiddenmemories",
            "Yu-Gi-Oh! GX: Duel Academy": "yugiohgxduelacademy",
            "Zelda II: The Adventure of Link": "zelda2theadventureoflink",
            "Zillion": "zillion",
            "Zork Grand Inquisitor": "zorkgrandinquisitor",
            "osu!": "osu",
            "plateup": "plateup",
            "shapez": "shapez",
            "shapez 2": "shapez2",
        }

        return mapping.get(self.state_game)

    def set_rich_presence(self) -> None:
        game_title: str = self.game_to_title

        if not self.state_game:
            self.rich_presence.clear()
        else:
            self.rich_presence.set({
                "details": game_title,
                "state": f"In the Multiworld ({len(self.checked_locations)} / {len(self.server_locations)})",
                "assets": {
                    "large_image": self.game_to_image_key or "archipelago",
                    "large_text": f"Last Location Checked: {self.state_last_location_checked}",
                    "small_image": "archipelago",
                    "small_text": f"{self.state_player_count} Player Multiworld",
                },
                "timestamps": {
                    "start": self.timestamp,
                },
            })

    def run_gui(self) -> None:
        from kvui import GameManager

        class TextManager(GameManager):
            logging_pairs: List[Tuple[str, str]] = [("Client", "Archipelago")]
            base_title: str = "Archipelago Discord Rich Presence Client"

        self.ui = TextManager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super().server_auth(password_requested)

        await self.get_username()
        await self.send_connect()

    async def disconnect(self, allow_autoreconnect: bool = False):
        self.state_game = None
        self.state_player_count = 0
        self.state_last_location_checked = "Nothing Yet"

        self.set_rich_presence()

        self.items_received = []
        self.locations_info = {}

        await super().disconnect(allow_autoreconnect)

    def on_package(self, cmd: str, _args: Any) -> None:
        if cmd == "Connected":
            self.timestamp = int(time.time())

            self.state_game = self.slot_info[self.slot].game
            self.state_player_count = len(_args["players"])

            self.set_rich_presence()
        elif cmd == "RoomUpdate":
            self.set_rich_presence()
        elif cmd == "PrintJSON":
            is_valid: bool = False

            for part in _args["data"]:
                if part["text"] in [" sent ", " found their "]:
                    is_valid = True
                    break

            if is_valid:
                for part in _args["data"]:
                    if "type" not in part:
                        continue

                    if part["type"] == "location_id" and part["player"] == self.slot:
                        self.state_last_location_checked = self.location_names.lookup_in_slot(
                            int(part["text"]),
                            self.slot
                        )

                        self.set_rich_presence()


def main(*args) -> None:
    Utils.init_logging("DiscordRichPresenceClient", exception_logger="Client")

    parser = CommonClient.get_base_parser(description="Discord Rich Presence Client")

    parser.add_argument("url", nargs="?", help="Archipelago Connection URL")
    parser.add_argument('--name', default=None, help="Archipelago Slot Name")

    args = parser.parse_args(args)

    if args.url:
        url = urllib.parse.urlparse(args.url)
        args.connect = url.netloc
        if url.username:
            args.name = urllib.parse.unquote(url.username)
        if url.password:
            args.password = urllib.parse.unquote(url.password)

    async def _main(_args):
        ctx: DiscordRichPresenceContext = DiscordRichPresenceContext(args.connect, args.password)

        ctx.server_task = asyncio.create_task(CommonClient.server_loop(ctx), name="ServerLoop")

        if CommonClient.gui_enabled:
            ctx.run_gui()

        ctx.run_cli()

        await ctx.exit_event.wait()
        await ctx.shutdown()

    import colorama

    colorama.init()

    asyncio.run(_main(args))

    colorama.deinit()


if __name__ == "__main__":
    main(*sys.argv[1:])

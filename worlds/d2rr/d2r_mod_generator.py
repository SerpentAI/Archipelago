from .data.mod_generator import d2r_tables

from .enums import (
    D2RClasses,
)


class D2RModGenerator:
    actinfo_table: d2r_tables.ActInfoD2RTable
    armor_table: d2r_tables.ArmorD2RTable
    belts_table: d2r_tables.BeltsD2RTable
    charstats_table: d2r_tables.CharStatsD2RTable
    cubemain_table: d2r_tables.CubeMainD2RTable
    experience_table: d2r_tables.ExperienceD2RTable
    levels_table: d2r_tables.LevelsD2RTable
    lvlmaze_table: d2r_tables.LvlMazeD2RTable
    misc_table: d2r_tables.MiscD2RTable
    monstats_table: d2r_tables.MonStatsD2RTable
    npc_table: d2r_tables.NPCD2RTable
    runes_table: d2r_tables.RunesD2RTable
    setitems_table: d2r_tables.SetItemsD2RTable
    shrines_table: d2r_tables.ShrinesD2RTable
    skills_table: d2r_tables.SkillsD2RTable
    sounds_table: d2r_tables.SoundsD2RTable
    superuniques_table: d2r_tables.SuperUniquesD2RTable
    treasureclassex_table: d2r_tables.TresureClassExD2RTable
    uniqueitems_table: d2r_tables.UniqueItemsD2RTable
    weapons_table: d2r_tables.WeaponsD2RTable

    def __init__(self):
        self.actinfo_table = d2r_tables.ActInfoD2RTable()
        self.armor_table = d2r_tables.ArmorD2RTable()
        self.belts_table = d2r_tables.BeltsD2RTable()
        self.charstats_table = d2r_tables.CharStatsD2RTable()
        self.cubemain_table = d2r_tables.CubeMainD2RTable()
        self.experience_table = d2r_tables.ExperienceD2RTable()
        self.levels_table = d2r_tables.LevelsD2RTable()
        self.lvlmaze_table = d2r_tables.LvlMazeD2RTable()
        self.misc_table = d2r_tables.MiscD2RTable()
        self.monstats_table = d2r_tables.MonStatsD2RTable()
        self.npc_table = d2r_tables.NPCD2RTable()
        self.runes_table = d2r_tables.RunesD2RTable()
        self.setitems_table = d2r_tables.SetItemsD2RTable()
        self.shrines_table = d2r_tables.ShrinesD2RTable()
        self.skills_table = d2r_tables.SkillsD2RTable()
        self.sounds_table = d2r_tables.SoundsD2RTable()
        self.superuniques_table = d2r_tables.SuperUniquesD2RTable()
        self.treasureclassex_table = d2r_tables.TresureClassExD2RTable()
        self.uniqueitems_table = d2r_tables.UniqueItemsD2RTable()
        self.weapons_table = d2r_tables.WeaponsD2RTable()

    def generate(
        self,
        mod_name: str,
        character_name: str,  # Needs to be an AP option, because D2R character names have restrictions
        character_class: D2RClasses,
    ):
        self.apply_base_mod()

    def apply_base_mod(self):
        self._lock_level_transitions()

    def _lock_level_transitions(self):
        # Blood Moor -> Den of Evil
        self.levels_table.set_value_by_row_index("Act 1 - Wilderness 1", "Vis3", "2")
        self.levels_table.set_value_by_row_index("Act 1 - Wilderness 1", "Vis4", "2")
        self.levels_table.set_value_by_row_index("Act 1 - Wilderness 1", "Vis5", "2")
        self.levels_table.set_value_by_row_index("Act 1 - Wilderness 1", "Vis6", "2")

        # Den of Evil -> Blood Moor
        self.levels_table.set_value_by_row_index("Act 1 - Cave 1", "Vis0", "8")

        # Cold Plains -> Cave
        self.levels_table.set_value_by_row_index("Act 1 - Wilderness 2", "Vis3", "3")
        self.levels_table.set_value_by_row_index("Act 1 - Wilderness 2", "Vis4", "3")
        self.levels_table.set_value_by_row_index("Act 1 - Wilderness 2", "Vis5", "3")
        self.levels_table.set_value_by_row_index("Act 1 - Wilderness 2", "Vis6", "3")

        # Cave -> Cold Plains
        self.levels_table.set_value_by_row_index("Act 1 - Cave 2", "Vis0", "9")

        # Burial Grounds -> Crypt
        self.levels_table.set_value_by_row_index("Act 1 - Graveyard", "Vis0", "17")

        # Crypt -> Burial Grounds
        self.levels_table.set_value_by_row_index("Act 1 - Crypt 1 A", "Vis0", "18")

        # Burial Grounds -> Mausoleum
        self.levels_table.set_value_by_row_index("Act 1 - Graveyard", "Vis1", "17")

        # Mausoleum -> Burial Grounds
        self.levels_table.set_value_by_row_index("Act 1 - Crypt 2 A", "Vis0", "19")

        # Stony Field -> Underground Passage
        self.levels_table.set_value_by_row_index("Act 1 - Wilderness 3", "Vis3", "4")
        self.levels_table.set_value_by_row_index("Act 1 - Wilderness 3", "Vis4", "4")
        self.levels_table.set_value_by_row_index("Act 1 - Wilderness 3", "Vis5", "4")
        self.levels_table.set_value_by_row_index("Act 1 - Wilderness 3", "Vis6", "4")

        # Underground Passage -> Stony Field
        self.levels_table.set_value_by_row_index("Act 1 - Cave 3", "Vis0", "10")

        # Underground Passage -> Dark Wood
        self.levels_table.set_value_by_row_index("Act 1 - Cave 3", "Vis1", "10")

        # Dark Wood -> Underground Passage
        self.levels_table.set_value_by_row_index("Act 1 - Wilderness 4", "Vis3", "5")
        self.levels_table.set_value_by_row_index("Act 1 - Wilderness 4", "Vis4", "5")
        self.levels_table.set_value_by_row_index("Act 1 - Wilderness 4", "Vis5", "5")
        self.levels_table.set_value_by_row_index("Act 1 - Wilderness 4", "Vis6", "5")

        # Black Marsh -> Hole
        self.levels_table.set_value_by_row_index("Act 1 - Wilderness 5", "Vis3", "6")
        self.levels_table.set_value_by_row_index("Act 1 - Wilderness 5", "Vis4", "6")
        self.levels_table.set_value_by_row_index("Act 1 - Wilderness 5", "Vis5", "6")
        self.levels_table.set_value_by_row_index("Act 1 - Wilderness 5", "Vis6", "6")

        # Hole -> Black Marsh
        self.levels_table.set_value_by_row_index("Act 1 - Cave 4", "Vis0", "11")

        # Black Marsh -> Forgotten Tower
        self.levels_table.set_value_by_row_index("Act 1 - Wilderness 5", "Vis2", "6")

        # Forgotten Tower -> Black Marsh
        self.levels_table.set_value_by_row_index("Act 1 - Tower 2", "Vis0", "20")

        # Tamoe Highlands -> Pit
        self.levels_table.set_value_by_row_index("Act 1 - Wilderness 6", "Vis3", "7")
        self.levels_table.set_value_by_row_index("Act 1 - Wilderness 6", "Vis4", "7")
        self.levels_table.set_value_by_row_index("Act 1 - Wilderness 6", "Vis5", "7")
        self.levels_table.set_value_by_row_index("Act 1 - Wilderness 6", "Vis6", "7")

        # Pit -> Tamoe Highlands
        self.levels_table.set_value_by_row_index("Act 1 - Cave 5", "Vis0", "12")

        # Barracks -> Jail
        self.levels_table.set_value_by_row_index("Act 1 - Barracks", "Vis1", "28")

        # Jail -> Barracks
        self.levels_table.set_value_by_row_index("Act 1 - Jail 1", "Vis0", "29")

        # Jail -> Inner Cloister
        self.levels_table.set_value_by_row_index("Act 1 - Jail 3", "Vis1", "31")

        # Inner Cloister -> Jail
        self.levels_table.set_value_by_row_index("Act 1 - Courtyard 2", "Vis0", "32")

        # Cathedral -> Catacombs
        self.levels_table.set_value_by_row_index("Act 1 - Cathedral", "Vis1", "33")

        # Catacombs -> Cathedral
        self.levels_table.set_value_by_row_index("Act 1 - Catacombs 1", "Vis0", "34")

        # Lut Gholein -> Sewers
        self.levels_table.set_value_by_row_index("Act 2 - Town", "Vis2", "40")
        self.levels_table.set_value_by_row_index("Act 2 - Town", "Vis3", "40")

        # Sewers -> Lut Gholein
        self.levels_table.set_value_by_row_index("Act 2 - Sewer 1 A", "Vis0", "47")
        self.levels_table.set_value_by_row_index("Act 2 - Sewer 1 A", "Vis1", "47")

        # Rocky Waste -> Stony Tomb
        self.levels_table.set_value_by_row_index("Act 2 - Desert 1", "Vis0", "41")
        self.levels_table.set_value_by_row_index("Act 2 - Desert 1", "Vis1", "41")
        self.levels_table.set_value_by_row_index("Act 2 - Desert 1", "Vis2", "41")
        self.levels_table.set_value_by_row_index("Act 2 - Desert 1", "Vis3", "41")

        # Stony Tomb -> Rocky Waste
        self.levels_table.set_value_by_row_index("Act 2 - Tomb 1 A", "Vis0", "55")

        # Dry Hills -> Halls of the Dead
        self.levels_table.set_value_by_row_index("Act 2 - Desert 2", "Vis0", "42")
        self.levels_table.set_value_by_row_index("Act 2 - Desert 2", "Vis1", "42")
        self.levels_table.set_value_by_row_index("Act 2 - Desert 2", "Vis2", "42")
        self.levels_table.set_value_by_row_index("Act 2 - Desert 2", "Vis3", "42")

        # Halls of the Dead -> Dry Hills
        self.levels_table.set_value_by_row_index("Act 2 - Tomb 2 A", "Vis0", "56")

        # Far Oasis -> Maggot Lair
        self.levels_table.set_value_by_row_index("Act 2 - Desert 3", "Vis4", "43")

        # Maggot Lair -> Far Oasis
        self.levels_table.set_value_by_row_index("Act 2 - Lair 1 A", "Vis0", "62")

        # Lost City -> Ancient Tunnels
        self.levels_table.set_value_by_row_index("Act 2 - Desert 4", "Vis2", "44")

        # Ancient Tunnels -> Lost City
        self.levels_table.set_value_by_row_index("Act 2 - Sewer 2 A", "Vis0", "65")

        # Valley of Snakes -> Claw Viper Temple
        self.levels_table.set_value_by_row_index("Act 2 - Desert 5", "Vis1", "45")

        # Claw Viper Temple -> Valley of Snakes
        self.levels_table.set_value_by_row_index("Act 2 - Tomb 3 A", "Vis0", "58")

        # Lut Gholein -> Harem
        self.levels_table.set_value_by_row_index("Act 2 - Town", "Vis4", "40")

        # Harem -> Lut Gholein
        self.levels_table.set_value_by_row_index("Act 2 - Harem", "Vis0", "50")

        # Harem -> Palace Cellar
        self.levels_table.set_value_by_row_index("Act 2 - Corrupt Harem 1", "Vis2", "51")
        self.levels_table.set_value_by_row_index("Act 2 - Corrupt Harem 1", "Vis3", "51")

        # Palace Cellar -> Harem
        self.levels_table.set_value_by_row_index("Act 2 - Basement 1", "Vis0", "52")
        self.levels_table.set_value_by_row_index("Act 2 - Basement 1", "Vis1", "52")

        # Canyon of the Magi -> All 7 Tal Rasha's Tombs
        self.levels_table.set_value_by_row_index("Act 2 - Valley of the Kings", "Vis1", "46")
        self.levels_table.set_value_by_row_index("Act 2 - Valley of the Kings", "Vis2", "46")
        self.levels_table.set_value_by_row_index("Act 2 - Valley of the Kings", "Vis3", "46")
        self.levels_table.set_value_by_row_index("Act 2 - Valley of the Kings", "Vis4", "46")
        self.levels_table.set_value_by_row_index("Act 2 - Valley of the Kings", "Vis5", "46")
        self.levels_table.set_value_by_row_index("Act 2 - Valley of the Kings", "Vis6", "46")
        self.levels_table.set_value_by_row_index("Act 2 - Valley of the Kings", "Vis7", "46")

        ### Tal Rasha's Tombs Vis Mapping (Verified with WinDS1Edit)
        # Circle -> 4
        # Crescent -> 3
        # Square -> 2
        # Star -> 1
        # Double V -> 5
        # Triangle -> 6
        # Circle Crescent -> 7

        # Tal Rasha's Tomb - Star -> Canyon of the Magi
        self.levels_table.set_value_by_row_index("Act 2 - Tomb Tal 1", "Vis0", "66")

        # Tal Rasha's Tomb - Square -> Canyon of the Magi
        self.levels_table.set_value_by_row_index("Act 2 - Tomb Tal 2", "Vis0", "67")

        # Tal Rasha's Tomb - Crescent -> Canyon of the Magi
        self.levels_table.set_value_by_row_index("Act 2 - Tomb Tal 3", "Vis0", "68")

        # Tal Rasha's Tomb - Circle -> Canyon of the Magi
        self.levels_table.set_value_by_row_index("Act 2 - Tomb Tal 4", "Vis0", "69")

        # Tal Rasha's Tomb - Double V -> Canyon of the Magi
        self.levels_table.set_value_by_row_index("Act 2 - Tomb Tal 5", "Vis0", "70")

        # Tal Rasha's Tomb - Triangle -> Canyon of the Magi
        self.levels_table.set_value_by_row_index("Act 2 - Tomb Tal 6", "Vis0", "71")

        # Tal Rasha's Tomb - Circle Crescent -> Canyon of the Magi
        self.levels_table.set_value_by_row_index("Act 2 - Tomb Tal 7", "Vis0", "72")

        # Spider Forest -> Arachnid Lair
        self.levels_table.set_value_by_row_index("Act 3 - Jungle 1", "Vis0", "76")

        # Arachnid Lair -> Spider Forest
        self.levels_table.set_value_by_row_index("Act 3 - Spider 1", "Vis1", "84")

        # Spider Forest -> Spider Cavern
        self.levels_table.set_value_by_row_index("Act 3 - Jungle 1", "Vis1", "76")

        # Spider Cavern -> Spider Forest
        self.levels_table.set_value_by_row_index("Act 3 - Spider 2", "Vis1", "85")

        # Flayer Jungle -> Swampy Pit
        self.levels_table.set_value_by_row_index("Act 3 - Jungle 3", "Vis0", "78")

        # Swampy Pit -> Flayer Jungle
        self.levels_table.set_value_by_row_index("Act 3 - Dungeon 1 A", "Vis1", "86")

        # Flayer Jungle -> Flayer Dungeon
        self.levels_table.set_value_by_row_index("Act 3 - Jungle 3", "Vis1", "78")

        # Flayer Dungeon -> Flayer Jungle
        self.levels_table.set_value_by_row_index("Act 3 - Dungeon 2 A", "Vis1", "88")

        # Kurast Bazaar -> Kurast Sewers
        self.levels_table.set_value_by_row_index("Act 3 - Kurast 2", "Vis0", "80")
        self.levels_table.set_value_by_row_index("Act 3 - Kurast 2", "Vis1", "80")

        # Kurast Sewers -> Kurast Bazaar
        self.levels_table.set_value_by_row_index("Act 3 - Sewer 1", "Vis0", "92")
        self.levels_table.set_value_by_row_index("Act 3 - Sewer 1", "Vis1", "92")

        # Kurast Bazaar -> Ruined Temple
        self.levels_table.set_value_by_row_index("Act 3 - Kurast 2", "Vis2", "80")

        # Ruined Temple -> Kurast Bazaar
        self.levels_table.set_value_by_row_index("Act 3 - Temple 1", "Vis0", "94")
        self.levels_table.set_value_by_row_index("Act 3 - Temple 1", "Vis1", "94")

        # Kurast Bazaar -> Disused Fane
        self.levels_table.set_value_by_row_index("Act 3 - Kurast 2", "Vis3", "80")

        # Disused Fane -> Kurast Bazaar
        self.levels_table.set_value_by_row_index("Act 3 - Temple 2", "Vis0", "95")
        self.levels_table.set_value_by_row_index("Act 3 - Temple 2", "Vis1", "95")

        # Upper Kurast -> Kurast Sewers
        self.levels_table.set_value_by_row_index("Act 3 - Kurast 3", "Vis0", "81")
        self.levels_table.set_value_by_row_index("Act 3 - Kurast 3", "Vis1", "81")

        # Kurast Sewers -> Upper Kurast
        self.levels_table.set_value_by_row_index("Act 3 - Sewer 1", "Vis2", "92")
        self.levels_table.set_value_by_row_index("Act 3 - Sewer 1", "Vis3", "92")

        # Upper Kurast -> Forgotten Reliquary
        self.levels_table.set_value_by_row_index("Act 3 - Kurast 3", "Vis2", "81")

        # Forgotten Reliquary -> Upper Kurast
        self.levels_table.set_value_by_row_index("Act 3 - Temple 3", "Vis0", "96")
        self.levels_table.set_value_by_row_index("Act 3 - Temple 3", "Vis1", "96")

        # Upper Kurast -> Forgotten Temple
        self.levels_table.set_value_by_row_index("Act 3 - Kurast 3", "Vis3", "81")

        # Forgotten Temple -> Upper Kurast
        self.levels_table.set_value_by_row_index("Act 3 - Temple 4", "Vis0", "97")
        self.levels_table.set_value_by_row_index("Act 3 - Temple 4", "Vis1", "97")

        # Kurast Causeway -> Ruined Fane
        self.levels_table.set_value_by_row_index("Act 3 - Kurast 4", "Vis2", "82")

        # Ruined Fane -> Kurast Causeway
        self.levels_table.set_value_by_row_index("Act 3 - Temple 5", "Vis0", "98")
        self.levels_table.set_value_by_row_index("Act 3 - Temple 5", "Vis1", "98")

        # Kurast Causeway -> Disused Reliquary
        self.levels_table.set_value_by_row_index("Act 3 - Kurast 4", "Vis3", "82")

        # Disused Reliquary -> Kurast Causeway
        self.levels_table.set_value_by_row_index("Act 3 - Temple 6", "Vis0", "99")
        self.levels_table.set_value_by_row_index("Act 3 - Temple 6", "Vis1", "99")

        # Travincal -> Durance of Hate

        # Durance of Hate -> Travincal

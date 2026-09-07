from typing import Dict, Optional, Set, Tuple

import dataclasses

from ..enums import DuskBosses, DuskDifficulties, DuskEndlessLevels, DuskLevels, DuskWeapons


@dataclasses.dataclass
class DuskWeaponLoadout:
    weapons: Set[DuskWeapons]
    max_ammo: Dict[DuskWeapons, float]
    has_sword_upgrade: bool = False
    has_dual_pistols_upgrade: bool = False
    has_dual_shotgun_upgrade: bool = False


# boss_index_to_boss: Dict[int, DuskBosses] = {
#     1: DuskBosses.INTOXIGATOR,
#     2: DuskBosses.THE_DUKE_BROTHERS,
# }

difficulty_value_to_difficulty: Dict[int, DuskDifficulties] = {
    0: DuskDifficulties.ACCESSIBLE,
    1: DuskDifficulties.GO_EASY,
    2: DuskDifficulties.I_CAN_TAKE_IT,
    3: DuskDifficulties.ACCESSIBLE,
    4: DuskDifficulties.ACCESSIBLE,
}

episode_to_levels: Dict[int, Tuple[DuskLevels, ...]] = {
    1: (
        DuskLevels.E1M1,
        DuskLevels.E1M2,
        DuskLevels.E1M3,
        DuskLevels.E1M4,
        DuskLevels.E1M5,
        DuskLevels.E1M6,
        DuskLevels.E1M7,
        DuskLevels.E1M8,
        DuskLevels.E1M9,
        DuskLevels.E1M10,
        DuskLevels.E1MS,
    ),
    2: (
        DuskLevels.E2M1,
        DuskLevels.E2M2,
        DuskLevels.E2M3,
        DuskLevels.E2M4,
        DuskLevels.E2M5,
        DuskLevels.E2M6,
        DuskLevels.E2M7,
        DuskLevels.E2M8,
        DuskLevels.E2M9,
        DuskLevels.E2M10,
        DuskLevels.E2MS,
    ),
    3: (
        DuskLevels.E3M1,
        DuskLevels.E3M2,
        DuskLevels.E3M3,
        DuskLevels.E3M4,
        DuskLevels.E3M5,
        DuskLevels.E3M6,
        DuskLevels.E3M7,
        DuskLevels.E3M8,
        DuskLevels.E3M9,
        DuskLevels.E3M10,
        DuskLevels.E3MS,
    ),
}

level_to_all_kill_count: Dict[DuskLevels, int] = {
    DuskLevels.E1M1: 26,
    DuskLevels.E1M2: 66,
    DuskLevels.E1M3: 59,
    DuskLevels.E1M4: 55,
    DuskLevels.E1M5: 57,
    DuskLevels.E1M6: 37,
    DuskLevels.E1M7: 83,
    DuskLevels.E1M8: 102,
    DuskLevels.E1M9: 85,
    DuskLevels.E1M10: 8,
    DuskLevels.E1MS: 43,
    DuskLevels.E2M1: 94,
    DuskLevels.E2M2: 48,
    DuskLevels.E2M3: 71,
    DuskLevels.E2M4: 85,
    DuskLevels.E2M5: 88,
    DuskLevels.E2M6: 80,
    DuskLevels.E2M7: 101,
    DuskLevels.E2M8: 83,
    DuskLevels.E2M9: 71,
    DuskLevels.E2M10: 1,
    DuskLevels.E2MS: 53,
    DuskLevels.E3M1: 94,
    DuskLevels.E3M2: 94,
    DuskLevels.E3M3: 57,
    DuskLevels.E3M4: 43,
    DuskLevels.E3M5: 116,
    DuskLevels.E3M6: 72,
    DuskLevels.E3M7: 22,
    DuskLevels.E3M8: 104,
    DuskLevels.E3M9: 270,
    DuskLevels.E3M10: 7,
    DuskLevels.E3MS: 138,
}

level_to_bosses: Dict[DuskLevels, Optional[Tuple[DuskBosses, ...]]] = {
    DuskLevels.E1M1: None,
    DuskLevels.E1M2: None,
    DuskLevels.E1M3: (DuskBosses.INTOXIGATOR,),
    DuskLevels.E1M4: None,
    DuskLevels.E1M5: None,
    DuskLevels.E1M6: None,
    DuskLevels.E1M7: (DuskBosses.THE_DUKE_BROTHERS,),
    DuskLevels.E1M8: None,
    DuskLevels.E1M9: None,
    DuskLevels.E1M10: (DuskBosses.EXPERIMENTS,),
    DuskLevels.E1MS: None,
    DuskLevels.E2M1: None,
    DuskLevels.E2M2: None,
    DuskLevels.E2M3: None,
    DuskLevels.E2M4: None,
    DuskLevels.E2M5: (DuskBosses.MAMA,),
    DuskLevels.E2M6: (DuskBosses.BIG_JOHN,),
    DuskLevels.E2M7: None,
    DuskLevels.E2M8: None,
    DuskLevels.E2M9: (DuskBosses.SON_OF_INTOXIGATOR, DuskBosses.THE_TWINS,),
    DuskLevels.E2M10: (DuskBosses.GUARDIAN,),
    DuskLevels.E2MS: None,
    DuskLevels.E3M1: None,
    DuskLevels.E3M2: None,
    DuskLevels.E3M3: (DuskBosses.CHOMPER,),
    DuskLevels.E3M4: None,
    DuskLevels.E3M5: None,
    DuskLevels.E3M6: None,
    DuskLevels.E3M7: None,
    DuskLevels.E3M8: (DuskBosses.LITTLENECK,),
    DuskLevels.E3M9: (DuskBosses.WATCHERS_OF_THE_GATE,),
    DuskLevels.E3M10: (DuskBosses.JAKOB, DuskBosses.NYARLATHOTEP,),
    DuskLevels.E3MS: (DuskBosses.ONE_AS_MANY,),
}

scene_name_to_endless_level: Dict[str, DuskEndlessLevels] = {
    "EndlessArena1": DuskEndlessLevels.EL1,
    "EndlessArena2": DuskEndlessLevels.EL2,
    "EndlessArena3": DuskEndlessLevels.EL3,
}

scene_name_to_level: Dict[str, DuskLevels] = {
    "E1M1": DuskLevels.E1M1,
    "E1M2": DuskLevels.E1M2,
    "E1M3": DuskLevels.E1M3,
    "E1M4": DuskLevels.E1M4,
    "E1M5": DuskLevels.E1M5,
    "E1M5AndAHalf": DuskLevels.E1M6,
    "E1M6-2": DuskLevels.E1M7,
    "E1M7": DuskLevels.E1M8,
    "E1M8": DuskLevels.E1M9,
    "E1M9": DuskLevels.E1M10,
    "E1MS": DuskLevels.E1MS,
    "E2M1": DuskLevels.E2M1,
    "E2M2": DuskLevels.E2M2,
    "E2M3": DuskLevels.E2M3,
    "E2M4": DuskLevels.E2M4,
    "E2M5": DuskLevels.E2M5,
    "E2M6": DuskLevels.E2M6,
    "E2M7": DuskLevels.E2M7,
    "E2M8": DuskLevels.E2M8,
    "E2M9": DuskLevels.E2M9,
    "E2M10": DuskLevels.E2M10,
    "E2MS": DuskLevels.E2MS,
    "E3M1": DuskLevels.E3M1,
    "e3m2": DuskLevels.E3M2,
    "E3M3": DuskLevels.E3M3,
    "E3M4": DuskLevels.E3M4,
    "E3M5": DuskLevels.E3M5,
    "E3M6": DuskLevels.E3M6,
    "E3M7": DuskLevels.E3M7,
    "E3M8": DuskLevels.E3M8,
    "E3M9": DuskLevels.E3M9,
    "E3M10": DuskLevels.E3M10,
    "E3MS": DuskLevels.E3MS,
}

selected_weapon_index_to_weapon: Dict[int, DuskWeapons] = {
    1: DuskWeapons.SICKLES,
    2: DuskWeapons.PISTOL,
    3: DuskWeapons.SHOTGUN,
    4: DuskWeapons.SUPER_SHOTGUN,
    5: DuskWeapons.ASSAULT_RIFLE,
    6: DuskWeapons.HUNTING_RIFLE,
    7: DuskWeapons.CROSSBOW,
    8: DuskWeapons.MORTAR,
    9: DuskWeapons.RIVETER,
    10: DuskWeapons.CIGAR,
}

weapon_to_weapon_internal_index: Dict[DuskWeapons, int] = {
    DuskWeapons.SICKLES: 0,
    DuskWeapons.PISTOL: 1,
    DuskWeapons.SHOTGUN: 2,
    DuskWeapons.SUPER_SHOTGUN: 3,
    DuskWeapons.ASSAULT_RIFLE: 4,
    DuskWeapons.HUNTING_RIFLE: 5,
    DuskWeapons.CROSSBOW: 6,
    DuskWeapons.MORTAR: 7,
    DuskWeapons.RIVETER: 8,
    DuskWeapons.CIGAR: 9,
}

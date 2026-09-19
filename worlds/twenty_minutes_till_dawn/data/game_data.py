from typing import Dict, NamedTuple

from ..enums import TwentyMinutesCharacters, TwentyMinutesMaps, TwentyMinutesWeapons


class TwentyMinutesWeaponData(NamedTuple):
    damage: float
    shot_cooldown: float
    maximum_ammunition: int
    reload_time: float
    number_of_projectiles: int
    spread: float
    knockback: float
    projectile_speed: float
    bounce: int
    piercing: int
    inaccuracy: float


character_button_index_to_character: Dict[int, TwentyMinutesCharacters] = {
    0: TwentyMinutesCharacters.SHANA,
    1: TwentyMinutesCharacters.DIAMOND,
    2: TwentyMinutesCharacters.SCARLETT,
    3: TwentyMinutesCharacters.HINA,
    4: TwentyMinutesCharacters.SPARK,
    5: TwentyMinutesCharacters.LILITH,
    6: TwentyMinutesCharacters.ABBY,
    7: TwentyMinutesCharacters.YUKI,
    8: TwentyMinutesCharacters.LUNA,
    9: TwentyMinutesCharacters.DASHER,
    10: TwentyMinutesCharacters.KATANA,
    11: TwentyMinutesCharacters.HASTUR,
    12: TwentyMinutesCharacters.RAVEN,
}

map_root_object_name_to_map: Dict[str, TwentyMinutesMaps] = {
    "PF_ForestMap(Clone)": TwentyMinutesMaps.FOREST,
    "PF_TempleMap(Clone)": TwentyMinutesMaps.TEMPLE,
    "PF_PumpkinMap(Clone)": TwentyMinutesMaps.PUMPKIN_PATCH,
}

weapon_button_index_to_weapon: Dict[int, TwentyMinutesWeapons] = {
    0: TwentyMinutesWeapons.REVOLVER,
    1: TwentyMinutesWeapons.SHOTGUN,
    2: TwentyMinutesWeapons.CROSSBOW,
    3: TwentyMinutesWeapons.FLAME_CANNON,
    4: TwentyMinutesWeapons.DUAL_SMGS,
    5: TwentyMinutesWeapons.BAT_GUN,
    6: TwentyMinutesWeapons.GRENADE_LAUNCHER,
    7: TwentyMinutesWeapons.MAGIC_BOW,
    8: TwentyMinutesWeapons.CYCLONE_SWORD,
    9: TwentyMinutesWeapons.SALVO_KNIFE,
    10: TwentyMinutesWeapons.SPORE_GUN,
}

weapon_to_vanilla_weapon_data: Dict[TwentyMinutesWeapons, TwentyMinutesWeaponData] = {
    TwentyMinutesWeapons.REVOLVER: TwentyMinutesWeaponData(
        damage=20.0,
        shot_cooldown=0.25,
        maximum_ammunition=6,
        reload_time=1.0,
        number_of_projectiles=1,
        spread=0.0,
        knockback=2.0,
        projectile_speed=15.0,
        bounce=0,
        piercing=0,
        inaccuracy=10.0
    ),
    TwentyMinutesWeapons.SHOTGUN: TwentyMinutesWeaponData(
        damage=10.0,
        shot_cooldown=0.20,
        maximum_ammunition=2,
        reload_time=1.0,
        number_of_projectiles=4,
        spread=45.0,
        knockback=1.0,
        projectile_speed=20.0,
        bounce=0,
        piercing=1,
        inaccuracy=10.0
    ),
    TwentyMinutesWeapons.CROSSBOW: TwentyMinutesWeaponData(
        damage=20.0,
        shot_cooldown=0.15,
        maximum_ammunition=1,
        reload_time=1.0,
        number_of_projectiles=1,
        spread=0.0,
        knockback=5.0,
        projectile_speed=40.0,
        bounce=0,
        piercing=1,
        inaccuracy=0.0
    ),
    TwentyMinutesWeapons.FLAME_CANNON: TwentyMinutesWeaponData(
        damage=3.0,
        shot_cooldown=0.15,
        maximum_ammunition=12,
        reload_time=1.6,
        number_of_projectiles=1,
        spread=15.0,
        knockback=2.0,
        projectile_speed=15.0,
        bounce=0,
        piercing=999,
        inaccuracy=30.0
    ),
    TwentyMinutesWeapons.DUAL_SMGS: TwentyMinutesWeaponData(
        damage=8.0,
        shot_cooldown=0.25,
        maximum_ammunition=24,
        reload_time=2.0,
        number_of_projectiles=1,
        spread=10.0,
        knockback=1.0,
        projectile_speed=10.0,
        bounce=0,
        piercing=0,
        inaccuracy=10.0
    ),
    TwentyMinutesWeapons.BAT_GUN: TwentyMinutesWeaponData(
        damage=18.0,
        shot_cooldown=0.5,
        maximum_ammunition=12,
        reload_time=1.5,
        number_of_projectiles=1,
        spread=60.0,
        knockback=2.0,
        projectile_speed=15.0,
        bounce=1,
        piercing=0,
        inaccuracy=10.0
    ),
    TwentyMinutesWeapons.GRENADE_LAUNCHER: TwentyMinutesWeaponData(
        damage=60.0,
        shot_cooldown=0.35,
        maximum_ammunition=6,
        reload_time=1.5,
        number_of_projectiles=1,
        spread=0.0,
        knockback=2.0,
        projectile_speed=25.0,
        bounce=0,
        piercing=0,
        inaccuracy=10.0
    ),
    TwentyMinutesWeapons.MAGIC_BOW: TwentyMinutesWeaponData(
        damage=16.0,
        shot_cooldown=0.30,
        maximum_ammunition=4,
        reload_time=1.2,
        number_of_projectiles=1,
        spread=0.0,
        knockback=0.5,
        projectile_speed=15.0,
        bounce=0,
        piercing=1,
        inaccuracy=5.0
    ),
    TwentyMinutesWeapons.CYCLONE_SWORD: TwentyMinutesWeaponData(
        damage=20.0,
        shot_cooldown=0.25,
        maximum_ammunition=8,
        reload_time=1.0,
        number_of_projectiles=1,
        spread=0.0,
        knockback=2.0,
        projectile_speed=20.0,
        bounce=0,
        piercing=999,
        inaccuracy=10.0
    ),
    TwentyMinutesWeapons.SALVO_KNIFE: TwentyMinutesWeaponData(
        damage=20.0,
        shot_cooldown=0.60,
        maximum_ammunition=12,
        reload_time=0.6,
        number_of_projectiles=1,
        spread=-10.0,
        knockback=2.0,
        projectile_speed=25.0,
        bounce=0,
        piercing=0,
        inaccuracy=0.0
    ),
    TwentyMinutesWeapons.SPORE_GUN: TwentyMinutesWeaponData(
        damage=18.0,
        shot_cooldown=0.20,
        maximum_ammunition=10,
        reload_time=0.8,
        number_of_projectiles=1,
        spread=0.0,
        knockback=1.0,
        projectile_speed=15.0,
        bounce=0,
        piercing=0,
        inaccuracy=10.0
    ),
}

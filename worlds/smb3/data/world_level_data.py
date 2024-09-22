from typing import Dict, List, NamedTuple, Set, Tuple

from ..enums import (
    SMB3Levels,
    SMB3LevelEnemyItemOffsetValues,
    SMB3LevelObjectSetValues,
    SMB3LevelOffsetValues,
    SMB3Worlds,
)

from .offset_data import offsets


class SMB3LevelData(NamedTuple):
    world: SMB3Worlds
    enemy_item_offsets: List[int, ...]
    enemy_item_offset_values: SMB3LevelEnemyItemOffsetValues
    object_set_offsets: List[int, ...]
    object_set_values: SMB3LevelObjectSetValues
    level_offsets: List[int, ...]
    level_offset_values: SMB3LevelOffsetValues


level_data: Dict[SMB3Levels, SMB3LevelData] = {
    SMB3Levels.GRASS_LAND_1: SMB3LevelData(
        world=SMB3Worlds.GRASS_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.GRASS_LAND_1,
        object_set_values=SMB3LevelObjectSetValues.GRASS_LAND_1,
        level_offset_values=SMB3LevelOffsetValues.GRASS_LAND_1,
    ),
    SMB3Levels.GRASS_LAND_2: SMB3LevelData(
        world=SMB3Worlds.GRASS_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.GRASS_LAND_2,
        object_set_values=SMB3LevelObjectSetValues.GRASS_LAND_2,
        level_offset_values=SMB3LevelOffsetValues.GRASS_LAND_2,
    ),
    SMB3Levels.GRASS_LAND_3: SMB3LevelData(
        world=SMB3Worlds.GRASS_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.GRASS_LAND_3,
        object_set_values=SMB3LevelObjectSetValues.GRASS_LAND_3,
        level_offset_values=SMB3LevelOffsetValues.GRASS_LAND_3,
    ),
    SMB3Levels.GRASS_LAND_4: SMB3LevelData(
        world=SMB3Worlds.GRASS_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.GRASS_LAND_4,
        object_set_values=SMB3LevelObjectSetValues.GRASS_LAND_4,
        level_offset_values=SMB3LevelOffsetValues.GRASS_LAND_4,
    ),
    SMB3Levels.GRASS_LAND_5: SMB3LevelData(
        world=SMB3Worlds.GRASS_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.GRASS_LAND_5,
        object_set_values=SMB3LevelObjectSetValues.GRASS_LAND_5,
        level_offset_values=SMB3LevelOffsetValues.GRASS_LAND_5,
    ),
    SMB3Levels.GRASS_LAND_6: SMB3LevelData(
        world=SMB3Worlds.GRASS_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.GRASS_LAND_6,
        object_set_values=SMB3LevelObjectSetValues.GRASS_LAND_6,
        level_offset_values=SMB3LevelOffsetValues.GRASS_LAND_6,
    ),
    SMB3Levels.GRASS_LAND_FORTRESS: SMB3LevelData(
        world=SMB3Worlds.GRASS_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.GRASS_LAND_FORTRESS,
        object_set_values=SMB3LevelObjectSetValues.GRASS_LAND_FORTRESS,
        level_offset_values=SMB3LevelOffsetValues.GRASS_LAND_FORTRESS,
    ),
    SMB3Levels.GRASS_LAND_CASTLE: SMB3LevelData(
        world=SMB3Worlds.GRASS_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.GRASS_LAND_CASTLE,
        object_set_values=SMB3LevelObjectSetValues.GRASS_LAND_CASTLE,
        level_offset_values=SMB3LevelOffsetValues.GRASS_LAND_CASTLE,
    ),
    SMB3Levels.GRASS_LAND_MUSHROOM_HOUSE_1: SMB3LevelData(
        world=SMB3Worlds.GRASS_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.GRASS_LAND_MUSHROOM_HOUSE_1,
        object_set_values=SMB3LevelObjectSetValues.GRASS_LAND_MUSHROOM_HOUSE_1,
        level_offset_values=SMB3LevelOffsetValues.GRASS_LAND_MUSHROOM_HOUSE_1,
    ),
    SMB3Levels.GRASS_LAND_MUSHROOM_HOUSE_2: SMB3LevelData(
        world=SMB3Worlds.GRASS_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.GRASS_LAND_MUSHROOM_HOUSE_2,
        object_set_values=SMB3LevelObjectSetValues.GRASS_LAND_MUSHROOM_HOUSE_2,
        level_offset_values=SMB3LevelOffsetValues.GRASS_LAND_MUSHROOM_HOUSE_2,
    ),
    SMB3Levels.GRASS_LAND_SPADE_BONUS: SMB3LevelData(
        world=SMB3Worlds.GRASS_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.GRASS_LAND_SPADE_BONUS,
        object_set_values=SMB3LevelObjectSetValues.GRASS_LAND_SPADE_BONUS,
        level_offset_values=SMB3LevelOffsetValues.GRASS_LAND_SPADE_BONUS,
    ),
    SMB3Levels.DESERT_LAND_1: SMB3LevelData(
        world=SMB3Worlds.DESERT_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.DESERT_LAND_1,
        object_set_values=SMB3LevelObjectSetValues.DESERT_LAND_1,
        level_offset_values=SMB3LevelOffsetValues.DESERT_LAND_1,
    ),
    SMB3Levels.DESERT_LAND_2: SMB3LevelData(
        world=SMB3Worlds.DESERT_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.DESERT_LAND_2,
        object_set_values=SMB3LevelObjectSetValues.DESERT_LAND_2,
        level_offset_values=SMB3LevelOffsetValues.DESERT_LAND_2,
    ),
    SMB3Levels.DESERT_LAND_3: SMB3LevelData(
        world=SMB3Worlds.DESERT_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.DESERT_LAND_3,
        object_set_values=SMB3LevelObjectSetValues.DESERT_LAND_3,
        level_offset_values=SMB3LevelOffsetValues.DESERT_LAND_3,
    ),
    SMB3Levels.DESERT_LAND_4: SMB3LevelData(
        world=SMB3Worlds.DESERT_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.DESERT_LAND_4,
        object_set_values=SMB3LevelObjectSetValues.DESERT_LAND_4,
        level_offset_values=SMB3LevelOffsetValues.DESERT_LAND_4,
    ),
    SMB3Levels.DESERT_LAND_5: SMB3LevelData(
        world=SMB3Worlds.DESERT_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.DESERT_LAND_5,
        object_set_values=SMB3LevelObjectSetValues.DESERT_LAND_5,
        level_offset_values=SMB3LevelOffsetValues.DESERT_LAND_5,
    ),
    SMB3Levels.DESERT_LAND_QUICKSAND: SMB3LevelData(
        world=SMB3Worlds.DESERT_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.DESERT_LAND_QUICKSAND,
        object_set_values=SMB3LevelObjectSetValues.DESERT_LAND_QUICKSAND,
        level_offset_values=SMB3LevelOffsetValues.DESERT_LAND_QUICKSAND,
    ),
    SMB3Levels.DESERT_LAND_PYRAMID: SMB3LevelData(
        world=SMB3Worlds.DESERT_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.DESERT_LAND_PYRAMID,
        object_set_values=SMB3LevelObjectSetValues.DESERT_LAND_PYRAMID,
        level_offset_values=SMB3LevelOffsetValues.DESERT_LAND_PYRAMID,
    ),
    SMB3Levels.DESERT_LAND_FORTRESS: SMB3LevelData(
        world=SMB3Worlds.DESERT_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.DESERT_LAND_FORTRESS,
        object_set_values=SMB3LevelObjectSetValues.DESERT_LAND_FORTRESS,
        level_offset_values=SMB3LevelOffsetValues.DESERT_LAND_FORTRESS,
    ),
    SMB3Levels.DESERT_LAND_CASTLE: SMB3LevelData(
        world=SMB3Worlds.DESERT_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.DESERT_LAND_CASTLE,
        object_set_values=SMB3LevelObjectSetValues.DESERT_LAND_CASTLE,
        level_offset_values=SMB3LevelOffsetValues.DESERT_LAND_CASTLE,
    ),
    SMB3Levels.DESERT_LAND_MUSHROOM_HOUSE_1: SMB3LevelData(
        world=SMB3Worlds.DESERT_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.DESERT_LAND_MUSHROOM_HOUSE_1,
        object_set_values=SMB3LevelObjectSetValues.DESERT_LAND_MUSHROOM_HOUSE_1,
        level_offset_values=SMB3LevelOffsetValues.DESERT_LAND_MUSHROOM_HOUSE_1,
    ),
    SMB3Levels.DESERT_LAND_MUSHROOM_HOUSE_2: SMB3LevelData(
        world=SMB3Worlds.DESERT_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.DESERT_LAND_MUSHROOM_HOUSE_2,
        object_set_values=SMB3LevelObjectSetValues.DESERT_LAND_MUSHROOM_HOUSE_2,
        level_offset_values=SMB3LevelOffsetValues.DESERT_LAND_MUSHROOM_HOUSE_2,
    ),
    SMB3Levels.DESERT_LAND_MUSHROOM_HOUSE_3: SMB3LevelData(
        world=SMB3Worlds.DESERT_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.DESERT_LAND_MUSHROOM_HOUSE_3,
        object_set_values=SMB3LevelObjectSetValues.DESERT_LAND_MUSHROOM_HOUSE_3,
        level_offset_values=SMB3LevelOffsetValues.DESERT_LAND_MUSHROOM_HOUSE_3,
    ),
    SMB3Levels.DESERT_LAND_SPADE_BONUS_1: SMB3LevelData(
        world=SMB3Worlds.DESERT_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.DESERT_LAND_SPADE_BONUS_1,
        object_set_values=SMB3LevelObjectSetValues.DESERT_LAND_SPADE_BONUS_1,
        level_offset_values=SMB3LevelOffsetValues.DESERT_LAND_SPADE_BONUS_1,
    ),
    SMB3Levels.DESERT_LAND_SPADE_BONUS_2: SMB3LevelData(
        world=SMB3Worlds.DESERT_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.DESERT_LAND_SPADE_BONUS_2,
        object_set_values=SMB3LevelObjectSetValues.DESERT_LAND_SPADE_BONUS_2,
        level_offset_values=SMB3LevelOffsetValues.DESERT_LAND_SPADE_BONUS_2,
    ),
    SMB3Levels.WATER_LAND_1: SMB3LevelData(
        world=SMB3Worlds.WATER_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.WATER_LAND_1,
        object_set_values=SMB3LevelObjectSetValues.WATER_LAND_1,
        level_offset_values=SMB3LevelOffsetValues.WATER_LAND_1,
    ),
    SMB3Levels.WATER_LAND_2: SMB3LevelData(
        world=SMB3Worlds.WATER_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.WATER_LAND_2,
        object_set_values=SMB3LevelObjectSetValues.WATER_LAND_2,
        level_offset_values=SMB3LevelOffsetValues.WATER_LAND_2,
    ),
    SMB3Levels.WATER_LAND_3: SMB3LevelData(
        world=SMB3Worlds.WATER_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.WATER_LAND_3,
        object_set_values=SMB3LevelObjectSetValues.WATER_LAND_3,
        level_offset_values=SMB3LevelOffsetValues.WATER_LAND_3,
    ),
    SMB3Levels.WATER_LAND_4: SMB3LevelData(
        world=SMB3Worlds.WATER_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.WATER_LAND_4,
        object_set_values=SMB3LevelObjectSetValues.WATER_LAND_4,
        level_offset_values=SMB3LevelOffsetValues.WATER_LAND_4,
    ),
    SMB3Levels.WATER_LAND_5: SMB3LevelData(
        world=SMB3Worlds.WATER_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.WATER_LAND_5,
        object_set_values=SMB3LevelObjectSetValues.WATER_LAND_5,
        level_offset_values=SMB3LevelOffsetValues.WATER_LAND_5,
    ),
    SMB3Levels.WATER_LAND_6: SMB3LevelData(
        world=SMB3Worlds.WATER_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.WATER_LAND_6,
        object_set_values=SMB3LevelObjectSetValues.WATER_LAND_6,
        level_offset_values=SMB3LevelOffsetValues.WATER_LAND_6,
    ),
    SMB3Levels.WATER_LAND_7: SMB3LevelData(
        world=SMB3Worlds.WATER_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.WATER_LAND_7,
        object_set_values=SMB3LevelObjectSetValues.WATER_LAND_7,
        level_offset_values=SMB3LevelOffsetValues.WATER_LAND_7,
    ),
    SMB3Levels.WATER_LAND_8: SMB3LevelData(
        world=SMB3Worlds.WATER_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.WATER_LAND_8,
        object_set_values=SMB3LevelObjectSetValues.WATER_LAND_8,
        level_offset_values=SMB3LevelOffsetValues.WATER_LAND_8,
    ),
    SMB3Levels.WATER_LAND_9: SMB3LevelData(
        world=SMB3Worlds.WATER_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.WATER_LAND_9,
        object_set_values=SMB3LevelObjectSetValues.WATER_LAND_9,
        level_offset_values=SMB3LevelOffsetValues.WATER_LAND_9,
    ),
    SMB3Levels.WATER_LAND_FORTRESS_1: SMB3LevelData(
        world=SMB3Worlds.WATER_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.WATER_LAND_FORTRESS_1,
        object_set_values=SMB3LevelObjectSetValues.WATER_LAND_FORTRESS_1,
        level_offset_values=SMB3LevelOffsetValues.WATER_LAND_FORTRESS_1,
    ),
    SMB3Levels.WATER_LAND_FORTRESS_2: SMB3LevelData(
        world=SMB3Worlds.WATER_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.WATER_LAND_FORTRESS_2,
        object_set_values=SMB3LevelObjectSetValues.WATER_LAND_FORTRESS_2,
        level_offset_values=SMB3LevelOffsetValues.WATER_LAND_FORTRESS_2,
    ),
    SMB3Levels.WATER_LAND_CASTLE: SMB3LevelData(
        world=SMB3Worlds.WATER_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.WATER_LAND_CASTLE,
        object_set_values=SMB3LevelObjectSetValues.WATER_LAND_CASTLE,
        level_offset_values=SMB3LevelOffsetValues.WATER_LAND_CASTLE,
    ),
    SMB3Levels.WATER_LAND_MUSHROOM_HOUSE_1: SMB3LevelData(
        world=SMB3Worlds.WATER_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.WATER_LAND_MUSHROOM_HOUSE_1,
        object_set_values=SMB3LevelObjectSetValues.WATER_LAND_MUSHROOM_HOUSE_1,
        level_offset_values=SMB3LevelOffsetValues.WATER_LAND_MUSHROOM_HOUSE_1,
    ),
    SMB3Levels.WATER_LAND_MUSHROOM_HOUSE_2: SMB3LevelData(
        world=SMB3Worlds.WATER_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.WATER_LAND_MUSHROOM_HOUSE_2,
        object_set_values=SMB3LevelObjectSetValues.WATER_LAND_MUSHROOM_HOUSE_2,
        level_offset_values=SMB3LevelOffsetValues.WATER_LAND_MUSHROOM_HOUSE_2,
    ),
    SMB3Levels.WATER_LAND_MUSHROOM_HOUSE_3: SMB3LevelData(
        world=SMB3Worlds.WATER_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.WATER_LAND_MUSHROOM_HOUSE_3,
        object_set_values=SMB3LevelObjectSetValues.WATER_LAND_MUSHROOM_HOUSE_3,
        level_offset_values=SMB3LevelOffsetValues.WATER_LAND_MUSHROOM_HOUSE_3,
    ),
    SMB3Levels.WATER_LAND_MUSHROOM_HOUSE_4: SMB3LevelData(
        world=SMB3Worlds.WATER_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.WATER_LAND_MUSHROOM_HOUSE_4,
        object_set_values=SMB3LevelObjectSetValues.WATER_LAND_MUSHROOM_HOUSE_4,
        level_offset_values=SMB3LevelOffsetValues.WATER_LAND_MUSHROOM_HOUSE_4,
    ),
    SMB3Levels.WATER_LAND_MUSHROOM_HOUSE_5: SMB3LevelData(
        world=SMB3Worlds.WATER_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.WATER_LAND_MUSHROOM_HOUSE_5,
        object_set_values=SMB3LevelObjectSetValues.WATER_LAND_MUSHROOM_HOUSE_5,
        level_offset_values=SMB3LevelOffsetValues.WATER_LAND_MUSHROOM_HOUSE_5,
    ),
    SMB3Levels.WATER_LAND_SPADE_BONUS_1: SMB3LevelData(
        world=SMB3Worlds.WATER_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.WATER_LAND_SPADE_BONUS_1,
        object_set_values=SMB3LevelObjectSetValues.WATER_LAND_SPADE_BONUS_1,
        level_offset_values=SMB3LevelOffsetValues.WATER_LAND_SPADE_BONUS_1,
    ),
    SMB3Levels.WATER_LAND_SPADE_BONUS_2: SMB3LevelData(
        world=SMB3Worlds.WATER_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.WATER_LAND_SPADE_BONUS_2,
        object_set_values=SMB3LevelObjectSetValues.WATER_LAND_SPADE_BONUS_2,
        level_offset_values=SMB3LevelOffsetValues.WATER_LAND_SPADE_BONUS_2,
    ),
    SMB3Levels.WATER_LAND_SPADE_BONUS_3: SMB3LevelData(
        world=SMB3Worlds.WATER_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.WATER_LAND_SPADE_BONUS_3,
        object_set_values=SMB3LevelObjectSetValues.WATER_LAND_SPADE_BONUS_3,
        level_offset_values=SMB3LevelOffsetValues.WATER_LAND_SPADE_BONUS_3,
    ),
    SMB3Levels.WATER_LAND_SPADE_BONUS_4: SMB3LevelData(
        world=SMB3Worlds.WATER_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.WATER_LAND_SPADE_BONUS_4,
        object_set_values=SMB3LevelObjectSetValues.WATER_LAND_SPADE_BONUS_4,
        level_offset_values=SMB3LevelOffsetValues.WATER_LAND_SPADE_BONUS_4,
    ),
    SMB3Levels.WATER_LAND_SPADE_BONUS_5: SMB3LevelData(
        world=SMB3Worlds.WATER_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.WATER_LAND_SPADE_BONUS_5,
        object_set_values=SMB3LevelObjectSetValues.WATER_LAND_SPADE_BONUS_5,
        level_offset_values=SMB3LevelOffsetValues.WATER_LAND_SPADE_BONUS_5,
    ),
    # Giant land
    SMB3Levels.GIANT_LAND_1: SMB3LevelData(
        world=SMB3Worlds.GIANT_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.GIANT_LAND_1,
        object_set_values=SMB3LevelObjectSetValues.GIANT_LAND_1,
        level_offset_values=SMB3LevelOffsetValues.GIANT_LAND_1,
    ),
    SMB3Levels.GIANT_LAND_2: SMB3LevelData(
        world=SMB3Worlds.GIANT_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.GIANT_LAND_2,
        object_set_values=SMB3LevelObjectSetValues.GIANT_LAND_2,
        level_offset_values=SMB3LevelOffsetValues.GIANT_LAND_2,
    ),
    SMB3Levels.GIANT_LAND_3: SMB3LevelData(
        world=SMB3Worlds.GIANT_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.GIANT_LAND_3,
        object_set_values=SMB3LevelObjectSetValues.GIANT_LAND_3,
        level_offset_values=SMB3LevelOffsetValues.GIANT_LAND_3,
    ),
    SMB3Levels.GIANT_LAND_4: SMB3LevelData(
        world=SMB3Worlds.GIANT_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.GIANT_LAND_4,
        object_set_values=SMB3LevelObjectSetValues.GIANT_LAND_4,
        level_offset_values=SMB3LevelOffsetValues.GIANT_LAND_4,
    ),
    SMB3Levels.GIANT_LAND_5: SMB3LevelData(
        world=SMB3Worlds.GIANT_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.GIANT_LAND_5,
        object_set_values=SMB3LevelObjectSetValues.GIANT_LAND_5,
        level_offset_values=SMB3LevelOffsetValues.GIANT_LAND_5,
    ),
    SMB3Levels.GIANT_LAND_6: SMB3LevelData(
        world=SMB3Worlds.GIANT_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.GIANT_LAND_6,
        object_set_values=SMB3LevelObjectSetValues.GIANT_LAND_6,
        level_offset_values=SMB3LevelOffsetValues.GIANT_LAND_6,
    ),
    SMB3Levels.GIANT_LAND_FORTRESS_1: SMB3LevelData(
        world=SMB3Worlds.GIANT_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.GIANT_LAND_FORTRESS_1,
        object_set_values=SMB3LevelObjectSetValues.GIANT_LAND_FORTRESS_1,
        level_offset_values=SMB3LevelOffsetValues.GIANT_LAND_FORTRESS_1,
    ),
    SMB3Levels.GIANT_LAND_FORTRESS_2: SMB3LevelData(
        world=SMB3Worlds.GIANT_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.GIANT_LAND_FORTRESS_2,
        object_set_values=SMB3LevelObjectSetValues.GIANT_LAND_FORTRESS_2,
        level_offset_values=SMB3LevelOffsetValues.GIANT_LAND_FORTRESS_2,
    ),
    SMB3Levels.GIANT_LAND_CASTLE: SMB3LevelData(
        world=SMB3Worlds.GIANT_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.GIANT_LAND_CASTLE,
        object_set_values=SMB3LevelObjectSetValues.GIANT_LAND_CASTLE,
        level_offset_values=SMB3LevelOffsetValues.GIANT_LAND_CASTLE,
    ),
    SMB3Levels.GIANT_LAND_MUSHROOM_HOUSE_1: SMB3LevelData(
        world=SMB3Worlds.GIANT_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.GIANT_LAND_MUSHROOM_HOUSE_1,
        object_set_values=SMB3LevelObjectSetValues.GIANT_LAND_MUSHROOM_HOUSE_1,
        level_offset_values=SMB3LevelOffsetValues.GIANT_LAND_MUSHROOM_HOUSE_1,
    ),
    SMB3Levels.GIANT_LAND_MUSHROOM_HOUSE_2: SMB3LevelData(
        world=SMB3Worlds.GIANT_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.GIANT_LAND_MUSHROOM_HOUSE_2,
        object_set_values=SMB3LevelObjectSetValues.GIANT_LAND_MUSHROOM_HOUSE_2,
        level_offset_values=SMB3LevelOffsetValues.GIANT_LAND_MUSHROOM_HOUSE_2,
    ),
    SMB3Levels.GIANT_LAND_MUSHROOM_HOUSE_3: SMB3LevelData(
        world=SMB3Worlds.GIANT_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.GIANT_LAND_MUSHROOM_HOUSE_3,
        object_set_values=SMB3LevelObjectSetValues.GIANT_LAND_MUSHROOM_HOUSE_3,
        level_offset_values=SMB3LevelOffsetValues.GIANT_LAND_MUSHROOM_HOUSE_3,
    ),
    SMB3Levels.GIANT_LAND_MUSHROOM_HOUSE_4: SMB3LevelData(
        world=SMB3Worlds.GIANT_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.GIANT_LAND_MUSHROOM_HOUSE_4,
        object_set_values=SMB3LevelObjectSetValues.GIANT_LAND_MUSHROOM_HOUSE_4,
        level_offset_values=SMB3LevelOffsetValues.GIANT_LAND_MUSHROOM_HOUSE_4,
    ),
    SMB3Levels.GIANT_LAND_SPADE_BONUS_1: SMB3LevelData(
        world=SMB3Worlds.GIANT_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.GIANT_LAND_SPADE_BONUS_1,
        object_set_values=SMB3LevelObjectSetValues.GIANT_LAND_SPADE_BONUS_1,
        level_offset_values=SMB3LevelOffsetValues.GIANT_LAND_SPADE_BONUS_1,
    ),
    SMB3Levels.GIANT_LAND_SPADE_BONUS_2: SMB3LevelData(
        world=SMB3Worlds.GIANT_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.GIANT_LAND_SPADE_BONUS_2,
        object_set_values=SMB3LevelObjectSetValues.GIANT_LAND_SPADE_BONUS_2,
        level_offset_values=SMB3LevelOffsetValues.GIANT_LAND_SPADE_BONUS_2,
    ),
    SMB3Levels.SKY_LAND_1: SMB3LevelData(
        world=SMB3Worlds.SKY_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.SKY_LAND_1,
        object_set_values=SMB3LevelObjectSetValues.SKY_LAND_1,
        level_offset_values=SMB3LevelOffsetValues.SKY_LAND_1,
    ),
    SMB3Levels.SKY_LAND_2: SMB3LevelData(
        world=SMB3Worlds.SKY_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.SKY_LAND_2,
        object_set_values=SMB3LevelObjectSetValues.SKY_LAND_2,
        level_offset_values=SMB3LevelOffsetValues.SKY_LAND_2,
    ),
    SMB3Levels.SKY_LAND_3: SMB3LevelData(
        world=SMB3Worlds.SKY_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.SKY_LAND_3,
        object_set_values=SMB3LevelObjectSetValues.SKY_LAND_3,
        level_offset_values=SMB3LevelOffsetValues.SKY_LAND_3,
    ),
    SMB3Levels.SKY_LAND_4: SMB3LevelData(
        world=SMB3Worlds.SKY_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.SKY_LAND_4,
        object_set_values=SMB3LevelObjectSetValues.SKY_LAND_4,
        level_offset_values=SMB3LevelOffsetValues.SKY_LAND_4,
    ),
    SMB3Levels.SKY_LAND_5: SMB3LevelData(
        world=SMB3Worlds.SKY_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.SKY_LAND_5,
        object_set_values=SMB3LevelObjectSetValues.SKY_LAND_5,
        level_offset_values=SMB3LevelOffsetValues.SKY_LAND_5,
    ),
    SMB3Levels.SKY_LAND_6: SMB3LevelData(
        world=SMB3Worlds.SKY_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.SKY_LAND_6,
        object_set_values=SMB3LevelObjectSetValues.SKY_LAND_6,
        level_offset_values=SMB3LevelOffsetValues.SKY_LAND_6,
    ),
    SMB3Levels.SKY_LAND_7: SMB3LevelData(
        world=SMB3Worlds.SKY_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.SKY_LAND_7,
        object_set_values=SMB3LevelObjectSetValues.SKY_LAND_7,
        level_offset_values=SMB3LevelOffsetValues.SKY_LAND_7,
    ),
    SMB3Levels.SKY_LAND_8: SMB3LevelData(
        world=SMB3Worlds.SKY_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.SKY_LAND_8,
        object_set_values=SMB3LevelObjectSetValues.SKY_LAND_8,
        level_offset_values=SMB3LevelOffsetValues.SKY_LAND_8,
    ),
    SMB3Levels.SKY_LAND_9: SMB3LevelData(
        world=SMB3Worlds.SKY_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.SKY_LAND_9,
        object_set_values=SMB3LevelObjectSetValues.SKY_LAND_9,
        level_offset_values=SMB3LevelOffsetValues.SKY_LAND_9,
    ),
    SMB3Levels.SKY_LAND_TOWER: SMB3LevelData(
        world=SMB3Worlds.SKY_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.SKY_LAND_TOWER,
        object_set_values=SMB3LevelObjectSetValues.SKY_LAND_TOWER,
        level_offset_values=SMB3LevelOffsetValues.SKY_LAND_TOWER,
    ),
    SMB3Levels.SKY_LAND_FORTRESS_1: SMB3LevelData(
        world=SMB3Worlds.SKY_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.SKY_LAND_FORTRESS_1,
        object_set_values=SMB3LevelObjectSetValues.SKY_LAND_FORTRESS_1,
        level_offset_values=SMB3LevelOffsetValues.SKY_LAND_FORTRESS_1,
    ),
    SMB3Levels.SKY_LAND_FORTRESS_2: SMB3LevelData(
        world=SMB3Worlds.SKY_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.SKY_LAND_FORTRESS_2,
        object_set_values=SMB3LevelObjectSetValues.SKY_LAND_FORTRESS_2,
        level_offset_values=SMB3LevelOffsetValues.SKY_LAND_FORTRESS_2,
    ),
    SMB3Levels.SKY_LAND_CASTLE: SMB3LevelData(
        world=SMB3Worlds.SKY_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.SKY_LAND_CASTLE,
        object_set_values=SMB3LevelObjectSetValues.SKY_LAND_CASTLE,
        level_offset_values=SMB3LevelOffsetValues.SKY_LAND_CASTLE,
    ),
    SMB3Levels.SKY_LAND_MUSHROOM_HOUSE_1: SMB3LevelData(
        world=SMB3Worlds.SKY_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.SKY_LAND_MUSHROOM_HOUSE_1,
        object_set_values=SMB3LevelObjectSetValues.SKY_LAND_MUSHROOM_HOUSE_1,
        level_offset_values=SMB3LevelOffsetValues.SKY_LAND_MUSHROOM_HOUSE_1,
    ),
    SMB3Levels.SKY_LAND_MUSHROOM_HOUSE_2: SMB3LevelData(
        world=SMB3Worlds.SKY_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.SKY_LAND_MUSHROOM_HOUSE_2,
        object_set_values=SMB3LevelObjectSetValues.SKY_LAND_MUSHROOM_HOUSE_2,
        level_offset_values=SMB3LevelOffsetValues.SKY_LAND_MUSHROOM_HOUSE_2,
    ),
    SMB3Levels.SKY_LAND_MUSHROOM_HOUSE_3: SMB3LevelData(
        world=SMB3Worlds.SKY_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.SKY_LAND_MUSHROOM_HOUSE_3,
        object_set_values=SMB3LevelObjectSetValues.SKY_LAND_MUSHROOM_HOUSE_3,
        level_offset_values=SMB3LevelOffsetValues.SKY_LAND_MUSHROOM_HOUSE_3,
    ),
    SMB3Levels.SKY_LAND_SPADE_BONUS_1: SMB3LevelData(
        world=SMB3Worlds.SKY_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.SKY_LAND_SPADE_BONUS_1,
        object_set_values=SMB3LevelObjectSetValues.SKY_LAND_SPADE_BONUS_1,
        level_offset_values=SMB3LevelOffsetValues.SKY_LAND_SPADE_BONUS_1,
    ),
    SMB3Levels.SKY_LAND_SPADE_BONUS_2: SMB3LevelData(
        world=SMB3Worlds.SKY_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.SKY_LAND_SPADE_BONUS_2,
        object_set_values=SMB3LevelObjectSetValues.SKY_LAND_SPADE_BONUS_2,
        level_offset_values=SMB3LevelOffsetValues.SKY_LAND_SPADE_BONUS_2,
    ),
    SMB3Levels.SKY_LAND_SPADE_BONUS_3: SMB3LevelData(
        world=SMB3Worlds.SKY_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.SKY_LAND_SPADE_BONUS_3,
        object_set_values=SMB3LevelObjectSetValues.SKY_LAND_SPADE_BONUS_3,
        level_offset_values=SMB3LevelOffsetValues.SKY_LAND_SPADE_BONUS_3,
    ),
    SMB3Levels.ICE_LAND_1: SMB3LevelData(
        world=SMB3Worlds.ICE_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.ICE_LAND_1,
        object_set_values=SMB3LevelObjectSetValues.ICE_LAND_1,
        level_offset_values=SMB3LevelOffsetValues.ICE_LAND_1,
    ),
    SMB3Levels.ICE_LAND_2: SMB3LevelData(
        world=SMB3Worlds.ICE_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.ICE_LAND_2,
        object_set_values=SMB3LevelObjectSetValues.ICE_LAND_2,
        level_offset_values=SMB3LevelOffsetValues.ICE_LAND_2,
    ),
    SMB3Levels.ICE_LAND_3: SMB3LevelData(
        world=SMB3Worlds.ICE_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.ICE_LAND_3,
        object_set_values=SMB3LevelObjectSetValues.ICE_LAND_3,
        level_offset_values=SMB3LevelOffsetValues.ICE_LAND_3,
    ),
    SMB3Levels.ICE_LAND_4: SMB3LevelData(
        world=SMB3Worlds.ICE_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.ICE_LAND_4,
        object_set_values=SMB3LevelObjectSetValues.ICE_LAND_4,
        level_offset_values=SMB3LevelOffsetValues.ICE_LAND_4,
    ),
    SMB3Levels.ICE_LAND_5: SMB3LevelData(
        world=SMB3Worlds.ICE_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.ICE_LAND_5,
        object_set_values=SMB3LevelObjectSetValues.ICE_LAND_5,
        level_offset_values=SMB3LevelOffsetValues.ICE_LAND_5,
    ),
    SMB3Levels.ICE_LAND_6: SMB3LevelData(
        world=SMB3Worlds.ICE_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.ICE_LAND_6,
        object_set_values=SMB3LevelObjectSetValues.ICE_LAND_6,
        level_offset_values=SMB3LevelOffsetValues.ICE_LAND_6,
    ),
    SMB3Levels.ICE_LAND_7: SMB3LevelData(
        world=SMB3Worlds.ICE_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.ICE_LAND_7,
        object_set_values=SMB3LevelObjectSetValues.ICE_LAND_7,
        level_offset_values=SMB3LevelOffsetValues.ICE_LAND_7,
    ),
    SMB3Levels.ICE_LAND_8: SMB3LevelData(
        world=SMB3Worlds.ICE_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.ICE_LAND_8,
        object_set_values=SMB3LevelObjectSetValues.ICE_LAND_8,
        level_offset_values=SMB3LevelOffsetValues.ICE_LAND_8,
    ),
    SMB3Levels.ICE_LAND_9: SMB3LevelData(
        world=SMB3Worlds.ICE_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.ICE_LAND_9,
        object_set_values=SMB3LevelObjectSetValues.ICE_LAND_9,
        level_offset_values=SMB3LevelOffsetValues.ICE_LAND_9,
    ),
    SMB3Levels.ICE_LAND_10: SMB3LevelData(
        world=SMB3Worlds.ICE_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.ICE_LAND_10,
        object_set_values=SMB3LevelObjectSetValues.ICE_LAND_10,
        level_offset_values=SMB3LevelOffsetValues.ICE_LAND_10,
    ),
    SMB3Levels.ICE_LAND_FORTRESS_1: SMB3LevelData(
        world=SMB3Worlds.ICE_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.ICE_LAND_FORTRESS_1,
        object_set_values=SMB3LevelObjectSetValues.ICE_LAND_FORTRESS_1,
        level_offset_values=SMB3LevelOffsetValues.ICE_LAND_FORTRESS_1,
    ),
    SMB3Levels.ICE_LAND_FORTRESS_2: SMB3LevelData(
        world=SMB3Worlds.ICE_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.ICE_LAND_FORTRESS_2,
        object_set_values=SMB3LevelObjectSetValues.ICE_LAND_FORTRESS_2,
        level_offset_values=SMB3LevelOffsetValues.ICE_LAND_FORTRESS_2,
    ),
    SMB3Levels.ICE_LAND_FORTRESS_3: SMB3LevelData(
        world=SMB3Worlds.ICE_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.ICE_LAND_FORTRESS_3,
        object_set_values=SMB3LevelObjectSetValues.ICE_LAND_FORTRESS_3,
        level_offset_values=SMB3LevelOffsetValues.ICE_LAND_FORTRESS_3,
    ),
    SMB3Levels.ICE_LAND_CASTLE: SMB3LevelData(
        world=SMB3Worlds.ICE_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.ICE_LAND_CASTLE,
        object_set_values=SMB3LevelObjectSetValues.ICE_LAND_CASTLE,
        level_offset_values=SMB3LevelOffsetValues.ICE_LAND_CASTLE,
    ),
    SMB3Levels.ICE_LAND_MUSHROOM_HOUSE_1: SMB3LevelData(
        world=SMB3Worlds.ICE_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.ICE_LAND_MUSHROOM_HOUSE_1,
        object_set_values=SMB3LevelObjectSetValues.ICE_LAND_MUSHROOM_HOUSE_1,
        level_offset_values=SMB3LevelOffsetValues.ICE_LAND_MUSHROOM_HOUSE_1,
    ),
    SMB3Levels.ICE_LAND_MUSHROOM_HOUSE_2: SMB3LevelData(
        world=SMB3Worlds.ICE_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.ICE_LAND_MUSHROOM_HOUSE_2,
        object_set_values=SMB3LevelObjectSetValues.ICE_LAND_MUSHROOM_HOUSE_2,
        level_offset_values=SMB3LevelOffsetValues.ICE_LAND_MUSHROOM_HOUSE_2,
    ),
    SMB3Levels.ICE_LAND_SPADE_BONUS_1: SMB3LevelData(
        world=SMB3Worlds.ICE_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.ICE_LAND_SPADE_BONUS_1,
        object_set_values=SMB3LevelObjectSetValues.ICE_LAND_SPADE_BONUS_1,
        level_offset_values=SMB3LevelOffsetValues.ICE_LAND_SPADE_BONUS_1,
    ),
    SMB3Levels.ICE_LAND_SPADE_BONUS_2: SMB3LevelData(
        world=SMB3Worlds.ICE_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.ICE_LAND_SPADE_BONUS_2,
        object_set_values=SMB3LevelObjectSetValues.ICE_LAND_SPADE_BONUS_2,
        level_offset_values=SMB3LevelOffsetValues.ICE_LAND_SPADE_BONUS_2,
    ),
    SMB3Levels.ICE_LAND_SPADE_BONUS_3: SMB3LevelData(
        world=SMB3Worlds.ICE_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.ICE_LAND_SPADE_BONUS_3,
        object_set_values=SMB3LevelObjectSetValues.ICE_LAND_SPADE_BONUS_3,
        level_offset_values=SMB3LevelOffsetValues.ICE_LAND_SPADE_BONUS_3,
    ),
    # Pipe land
    SMB3Levels.PIPE_LAND_1: SMB3LevelData(
        world=SMB3Worlds.PIPE_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.PIPE_LAND_1,
        object_set_values=SMB3LevelObjectSetValues.PIPE_LAND_1,
        level_offset_values=SMB3LevelOffsetValues.PIPE_LAND_1,
    ),
    SMB3Levels.PIPE_LAND_2: SMB3LevelData(
        world=SMB3Worlds.PIPE_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.PIPE_LAND_2,
        object_set_values=SMB3LevelObjectSetValues.PIPE_LAND_2,
        level_offset_values=SMB3LevelOffsetValues.PIPE_LAND_2,
    ),
    SMB3Levels.PIPE_LAND_3: SMB3LevelData(
        world=SMB3Worlds.PIPE_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.PIPE_LAND_3,
        object_set_values=SMB3LevelObjectSetValues.PIPE_LAND_3,
        level_offset_values=SMB3LevelOffsetValues.PIPE_LAND_3,
    ),
    SMB3Levels.PIPE_LAND_4: SMB3LevelData(
        world=SMB3Worlds.PIPE_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.PIPE_LAND_4,
        object_set_values=SMB3LevelObjectSetValues.PIPE_LAND_4,
        level_offset_values=SMB3LevelOffsetValues.PIPE_LAND_4,
    ),
    SMB3Levels.PIPE_LAND_5: SMB3LevelData(
        world=SMB3Worlds.PIPE_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.PIPE_LAND_5,
        object_set_values=SMB3LevelObjectSetValues.PIPE_LAND_5,
        level_offset_values=SMB3LevelOffsetValues.PIPE_LAND_5,
    ),
    SMB3Levels.PIPE_LAND_6: SMB3LevelData(
        world=SMB3Worlds.PIPE_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.PIPE_LAND_6,
        object_set_values=SMB3LevelObjectSetValues.PIPE_LAND_6,
        level_offset_values=SMB3LevelOffsetValues.PIPE_LAND_6,
    ),
    SMB3Levels.PIPE_LAND_7: SMB3LevelData(
        world=SMB3Worlds.PIPE_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.PIPE_LAND_7,
        object_set_values=SMB3LevelObjectSetValues.PIPE_LAND_7,
        level_offset_values=SMB3LevelOffsetValues.PIPE_LAND_7,
    ),
    SMB3Levels.PIPE_LAND_8: SMB3LevelData(
        world=SMB3Worlds.PIPE_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.PIPE_LAND_8,
        object_set_values=SMB3LevelObjectSetValues.PIPE_LAND_8,
        level_offset_values=SMB3LevelOffsetValues.PIPE_LAND_8,
    ),
    SMB3Levels.PIPE_LAND_9: SMB3LevelData(
        world=SMB3Worlds.PIPE_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.PIPE_LAND_9,
        object_set_values=SMB3LevelObjectSetValues.PIPE_LAND_9,
        level_offset_values=SMB3LevelOffsetValues.PIPE_LAND_9,
    ),
    SMB3Levels.PIPE_LAND_PIRANHA_1: SMB3LevelData(
        world=SMB3Worlds.PIPE_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.PIPE_LAND_PIRANHA_1,
        object_set_values=SMB3LevelObjectSetValues.PIPE_LAND_PIRANHA_1,
        level_offset_values=SMB3LevelOffsetValues.PIPE_LAND_PIRANHA_1,
    ),
    SMB3Levels.PIPE_LAND_PIRANHA_2: SMB3LevelData(
        world=SMB3Worlds.PIPE_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.PIPE_LAND_PIRANHA_2,
        object_set_values=SMB3LevelObjectSetValues.PIPE_LAND_PIRANHA_2,
        level_offset_values=SMB3LevelOffsetValues.PIPE_LAND_PIRANHA_2,
    ),
    SMB3Levels.PIPE_LAND_FORTRESS_1: SMB3LevelData(
        world=SMB3Worlds.PIPE_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.PIPE_LAND_FORTRESS_1,
        object_set_values=SMB3LevelObjectSetValues.PIPE_LAND_FORTRESS_1,
        level_offset_values=SMB3LevelOffsetValues.PIPE_LAND_FORTRESS_1,
    ),
    SMB3Levels.PIPE_LAND_FORTRESS_2: SMB3LevelData(
        world=SMB3Worlds.PIPE_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.PIPE_LAND_FORTRESS_2,
        object_set_values=SMB3LevelObjectSetValues.PIPE_LAND_FORTRESS_2,
        level_offset_values=SMB3LevelOffsetValues.PIPE_LAND_FORTRESS_2,
    ),
    SMB3Levels.PIPE_LAND_CASTLE: SMB3LevelData(
        world=SMB3Worlds.PIPE_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.PIPE_LAND_CASTLE,
        object_set_values=SMB3LevelObjectSetValues.PIPE_LAND_CASTLE,
        level_offset_values=SMB3LevelOffsetValues.PIPE_LAND_CASTLE,
    ),
    SMB3Levels.PIPE_LAND_MUSHROOM_HOUSE_1: SMB3LevelData(
        world=SMB3Worlds.PIPE_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.PIPE_LAND_MUSHROOM_HOUSE_1,
        object_set_values=SMB3LevelObjectSetValues.PIPE_LAND_MUSHROOM_HOUSE_1,
        level_offset_values=SMB3LevelOffsetValues.PIPE_LAND_MUSHROOM_HOUSE_1,
    ),
    SMB3Levels.PIPE_LAND_MUSHROOM_HOUSE_2: SMB3LevelData(
        world=SMB3Worlds.PIPE_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.PIPE_LAND_MUSHROOM_HOUSE_2,
        object_set_values=SMB3LevelObjectSetValues.PIPE_LAND_MUSHROOM_HOUSE_2,
        level_offset_values=SMB3LevelOffsetValues.PIPE_LAND_MUSHROOM_HOUSE_2,
    ),
    SMB3Levels.PIPE_LAND_MUSHROOM_HOUSE_3: SMB3LevelData(
        world=SMB3Worlds.PIPE_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.PIPE_LAND_MUSHROOM_HOUSE_3,
        object_set_values=SMB3LevelObjectSetValues.PIPE_LAND_MUSHROOM_HOUSE_3,
        level_offset_values=SMB3LevelOffsetValues.PIPE_LAND_MUSHROOM_HOUSE_3,
    ),
    SMB3Levels.PIPE_LAND_SPADE_BONUS_1: SMB3LevelData(
        world=SMB3Worlds.PIPE_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.PIPE_LAND_SPADE_BONUS_1,
        object_set_values=SMB3LevelObjectSetValues.PIPE_LAND_SPADE_BONUS_1,
        level_offset_values=SMB3LevelOffsetValues.PIPE_LAND_SPADE_BONUS_1,
    ),
    SMB3Levels.PIPE_LAND_SPADE_BONUS_2: SMB3LevelData(
        world=SMB3Worlds.PIPE_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.PIPE_LAND_SPADE_BONUS_2,
        object_set_values=SMB3LevelObjectSetValues.PIPE_LAND_SPADE_BONUS_2,
        level_offset_values=SMB3LevelOffsetValues.PIPE_LAND_SPADE_BONUS_2,
    ),
    SMB3Levels.PIPE_LAND_SPADE_BONUS_3: SMB3LevelData(
        world=SMB3Worlds.PIPE_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.PIPE_LAND_SPADE_BONUS_3,
        object_set_values=SMB3LevelObjectSetValues.PIPE_LAND_SPADE_BONUS_3,
        level_offset_values=SMB3LevelOffsetValues.PIPE_LAND_SPADE_BONUS_3,
    ),
    SMB3Levels.DARK_LAND_SHIP_1: SMB3LevelData(
        world=SMB3Worlds.DARK_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.DARK_LAND_SHIP_1,
        object_set_values=SMB3LevelObjectSetValues.DARK_LAND_SHIP_1,
        level_offset_values=SMB3LevelOffsetValues.DARK_LAND_SHIP_1,
    ),
    SMB3Levels.DARK_LAND_SHIP_2: SMB3LevelData(
        world=SMB3Worlds.DARK_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.DARK_LAND_SHIP_2,
        object_set_values=SMB3LevelObjectSetValues.DARK_LAND_SHIP_2,
        level_offset_values=SMB3LevelOffsetValues.DARK_LAND_SHIP_2,
    ),
    SMB3Levels.DARK_LAND_SHIP_3: SMB3LevelData(
        world=SMB3Worlds.DARK_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.DARK_LAND_SHIP_3,
        object_set_values=SMB3LevelObjectSetValues.DARK_LAND_SHIP_3,
        level_offset_values=SMB3LevelOffsetValues.DARK_LAND_SHIP_3,
    ),
    SMB3Levels.DARK_LAND_SHIP_4: SMB3LevelData(
        world=SMB3Worlds.DARK_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.DARK_LAND_SHIP_4,
        object_set_values=SMB3LevelObjectSetValues.DARK_LAND_SHIP_4,
        level_offset_values=SMB3LevelOffsetValues.DARK_LAND_SHIP_4,
    ),
    SMB3Levels.DARK_LAND_HAND_1: SMB3LevelData(
        world=SMB3Worlds.DARK_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.DARK_LAND_HAND_1,
        object_set_values=SMB3LevelObjectSetValues.DARK_LAND_HAND_1,
        level_offset_values=SMB3LevelOffsetValues.DARK_LAND_HAND_1,
    ),
    SMB3Levels.DARK_LAND_HAND_2: SMB3LevelData(
        world=SMB3Worlds.DARK_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.DARK_LAND_HAND_2,
        object_set_values=SMB3LevelObjectSetValues.DARK_LAND_HAND_2,
        level_offset_values=SMB3LevelOffsetValues.DARK_LAND_HAND_2,
    ),
    SMB3Levels.DARK_LAND_HAND_3: SMB3LevelData(
        world=SMB3Worlds.DARK_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.DARK_LAND_HAND_3,
        object_set_values=SMB3LevelObjectSetValues.DARK_LAND_HAND_3,
        level_offset_values=SMB3LevelOffsetValues.DARK_LAND_HAND_3,
    ),
    SMB3Levels.DARK_LAND_1: SMB3LevelData(
        world=SMB3Worlds.DARK_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.DARK_LAND_1,
        object_set_values=SMB3LevelObjectSetValues.DARK_LAND_1,
        level_offset_values=SMB3LevelOffsetValues.DARK_LAND_1,
    ),
    SMB3Levels.DARK_LAND_2: SMB3LevelData(
        world=SMB3Worlds.DARK_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.DARK_LAND_2,
        object_set_values=SMB3LevelObjectSetValues.DARK_LAND_2,
        level_offset_values=SMB3LevelOffsetValues.DARK_LAND_2,
    ),
    SMB3Levels.DARK_LAND_FORTRESS: SMB3LevelData(
        world=SMB3Worlds.DARK_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.DARK_LAND_FORTRESS,
        object_set_values=SMB3LevelObjectSetValues.DARK_LAND_FORTRESS,
        level_offset_values=SMB3LevelOffsetValues.DARK_LAND_FORTRESS,
    ),
    SMB3Levels.DARK_LAND_CASTLE: SMB3LevelData(
        world=SMB3Worlds.DARK_LAND,
        enemy_item_offset_values=SMB3LevelEnemyItemOffsetValues.DARK_LAND_CASTLE,
        object_set_values=SMB3LevelObjectSetValues.DARK_LAND_CASTLE,
        level_offset_values=SMB3LevelOffsetValues.DARK_LAND_CASTLE,
    ),
}

non_randomizable_levels: Set[SMB3Levels] = {
    SMB3Levels.SKY_LAND_TOWER,
    SMB3Levels.DARK_LAND_CASTLE,
}

world_castle_data: Dict[SMB3Worlds, Tuple[SMB3Levels, ...]] = {
    SMB3Worlds.GRASS_LAND: (
        SMB3Levels.GRASS_LAND_CASTLE,
    ),
    SMB3Worlds.DESERT_LAND: (
        SMB3Levels.DESERT_LAND_CASTLE,
    ),
    SMB3Worlds.WATER_LAND: (
        SMB3Levels.WATER_LAND_CASTLE,
    ),
    SMB3Worlds.GIANT_LAND: (
        SMB3Levels.GIANT_LAND_CASTLE,
    ),
    SMB3Worlds.SKY_LAND: (
        SMB3Levels.SKY_LAND_CASTLE,
    ),
    SMB3Worlds.ICE_LAND: (
        SMB3Levels.ICE_LAND_CASTLE,
    ),
    SMB3Worlds.PIPE_LAND: (
        SMB3Levels.PIPE_LAND_CASTLE,
    ),
    SMB3Worlds.DARK_LAND: (
        SMB3Levels.DARK_LAND_CASTLE,
    ),
}

world_fortress_data: Dict[SMB3Worlds, Tuple[SMB3Levels, ...]] = {
    SMB3Worlds.GRASS_LAND: (
        SMB3Levels.GRASS_LAND_FORTRESS,
    ),
    SMB3Worlds.DESERT_LAND: (
        SMB3Levels.DESERT_LAND_FORTRESS,
    ),
    SMB3Worlds.WATER_LAND: (
        SMB3Levels.WATER_LAND_FORTRESS_1,
        SMB3Levels.WATER_LAND_FORTRESS_2,
    ),
    SMB3Worlds.GIANT_LAND: (
        SMB3Levels.GIANT_LAND_FORTRESS_1,
        SMB3Levels.GIANT_LAND_FORTRESS_2,
    ),
    SMB3Worlds.SKY_LAND: (
        SMB3Levels.SKY_LAND_FORTRESS_1,
        SMB3Levels.SKY_LAND_FORTRESS_2,
    ),
    SMB3Worlds.ICE_LAND: (
        SMB3Levels.ICE_LAND_FORTRESS_1,
        SMB3Levels.ICE_LAND_FORTRESS_2,
        SMB3Levels.ICE_LAND_FORTRESS_3,
    ),
    SMB3Worlds.PIPE_LAND: (
        SMB3Levels.PIPE_LAND_FORTRESS_1,
        SMB3Levels.PIPE_LAND_FORTRESS_2,
    ),
    SMB3Worlds.DARK_LAND: (
        SMB3Levels.DARK_LAND_FORTRESS,
    ),
}

world_level_data: Dict[SMB3Worlds, Tuple[SMB3Levels, ...]] = {
    SMB3Worlds.GRASS_LAND: (
        SMB3Levels.GRASS_LAND_1,
        SMB3Levels.GRASS_LAND_2,
        SMB3Levels.GRASS_LAND_3,
        SMB3Levels.GRASS_LAND_4,
        SMB3Levels.GRASS_LAND_5,
        SMB3Levels.GRASS_LAND_6,
    ),
    SMB3Worlds.DESERT_LAND: (
        SMB3Levels.DESERT_LAND_1,
        SMB3Levels.DESERT_LAND_2,
        SMB3Levels.DESERT_LAND_3,
        SMB3Levels.DESERT_LAND_4,
        SMB3Levels.DESERT_LAND_5,
        SMB3Levels.DESERT_LAND_QUICKSAND,
        SMB3Levels.DESERT_LAND_PYRAMID,
    ),
    SMB3Worlds.WATER_LAND: (
        SMB3Levels.WATER_LAND_1,
        SMB3Levels.WATER_LAND_2,
        SMB3Levels.WATER_LAND_3,
        SMB3Levels.WATER_LAND_4,
        SMB3Levels.WATER_LAND_5,
        SMB3Levels.WATER_LAND_6,
        SMB3Levels.WATER_LAND_7,
        SMB3Levels.WATER_LAND_8,
        SMB3Levels.WATER_LAND_9,
    ),
    SMB3Worlds.GIANT_LAND: (
        SMB3Levels.GIANT_LAND_1,
        SMB3Levels.GIANT_LAND_2,
        SMB3Levels.GIANT_LAND_3,
        SMB3Levels.GIANT_LAND_4,
        SMB3Levels.GIANT_LAND_5,
        SMB3Levels.GIANT_LAND_6,
    ),
    SMB3Worlds.SKY_LAND: (
        SMB3Levels.SKY_LAND_1,
        SMB3Levels.SKY_LAND_2,
        SMB3Levels.SKY_LAND_3,
        SMB3Levels.SKY_LAND_4,
        SMB3Levels.SKY_LAND_5,
        SMB3Levels.SKY_LAND_6,
        SMB3Levels.SKY_LAND_7,
        SMB3Levels.SKY_LAND_8,
        SMB3Levels.SKY_LAND_9,
        SMB3Levels.SKY_LAND_TOWER,
    ),
    SMB3Worlds.ICE_LAND: (
        SMB3Levels.ICE_LAND_1,
        SMB3Levels.ICE_LAND_2,
        SMB3Levels.ICE_LAND_3,
        SMB3Levels.ICE_LAND_4,
        SMB3Levels.ICE_LAND_5,
        SMB3Levels.ICE_LAND_6,
        SMB3Levels.ICE_LAND_7,
        SMB3Levels.ICE_LAND_8,
        SMB3Levels.ICE_LAND_9,
        SMB3Levels.ICE_LAND_10,
    ),
    SMB3Worlds.PIPE_LAND: (
        SMB3Levels.PIPE_LAND_1,
        SMB3Levels.PIPE_LAND_2,
        SMB3Levels.PIPE_LAND_3,
        SMB3Levels.PIPE_LAND_4,
        SMB3Levels.PIPE_LAND_5,
        SMB3Levels.PIPE_LAND_6,
        SMB3Levels.PIPE_LAND_7,
        SMB3Levels.PIPE_LAND_8,
        SMB3Levels.PIPE_LAND_9,
        SMB3Levels.PIPE_LAND_PIRANHA_1,
        SMB3Levels.PIPE_LAND_PIRANHA_2,
    ),
    SMB3Worlds.DARK_LAND: (
        SMB3Levels.DARK_LAND_1,
        SMB3Levels.DARK_LAND_2,
        SMB3Levels.DARK_LAND_HAND_1,
        SMB3Levels.DARK_LAND_HAND_2,
        SMB3Levels.DARK_LAND_HAND_3,
    ),
}

world_mushroom_house_data: Dict[SMB3Worlds, Tuple[SMB3Levels, ...]] = {
    SMB3Worlds.GRASS_LAND: (
        SMB3Levels.GRASS_LAND_MUSHROOM_HOUSE_1,
        SMB3Levels.GRASS_LAND_MUSHROOM_HOUSE_2,
    ),
    SMB3Worlds.DESERT_LAND: (
        SMB3Levels.DESERT_LAND_MUSHROOM_HOUSE_1,
        SMB3Levels.DESERT_LAND_MUSHROOM_HOUSE_2,
        SMB3Levels.DESERT_LAND_MUSHROOM_HOUSE_3,
    ),
    SMB3Worlds.WATER_LAND: (
        SMB3Levels.WATER_LAND_MUSHROOM_HOUSE_1,
        SMB3Levels.WATER_LAND_MUSHROOM_HOUSE_2,
        SMB3Levels.WATER_LAND_MUSHROOM_HOUSE_3,
        SMB3Levels.WATER_LAND_MUSHROOM_HOUSE_4,
        SMB3Levels.WATER_LAND_MUSHROOM_HOUSE_5,
    ),
    SMB3Worlds.GIANT_LAND: (
        SMB3Levels.GIANT_LAND_MUSHROOM_HOUSE_1,
        SMB3Levels.GIANT_LAND_MUSHROOM_HOUSE_2,
        SMB3Levels.GIANT_LAND_MUSHROOM_HOUSE_3,
        SMB3Levels.GIANT_LAND_MUSHROOM_HOUSE_4,
    ),
    SMB3Worlds.SKY_LAND: (
        SMB3Levels.SKY_LAND_MUSHROOM_HOUSE_1,
        SMB3Levels.SKY_LAND_MUSHROOM_HOUSE_2,
        SMB3Levels.SKY_LAND_MUSHROOM_HOUSE_3,
    ),
    SMB3Worlds.ICE_LAND: (
        SMB3Levels.ICE_LAND_MUSHROOM_HOUSE_1,
        SMB3Levels.ICE_LAND_MUSHROOM_HOUSE_2,
    ),
    SMB3Worlds.PIPE_LAND: (
        SMB3Levels.PIPE_LAND_MUSHROOM_HOUSE_1,
        SMB3Levels.PIPE_LAND_MUSHROOM_HOUSE_2,
        SMB3Levels.PIPE_LAND_MUSHROOM_HOUSE_3,
    ),
    SMB3Worlds.DARK_LAND: tuple(),
}

world_spade_bonus_data: Dict[SMB3Worlds, Tuple[SMB3Levels, ...]] = {
    SMB3Worlds.GRASS_LAND: (
        SMB3Levels.GRASS_LAND_SPADE_BONUS,
    ),
    SMB3Worlds.DESERT_LAND: (
        SMB3Levels.DESERT_LAND_SPADE_BONUS_1,
        SMB3Levels.DESERT_LAND_SPADE_BONUS_2,
    ),
    SMB3Worlds.WATER_LAND: (
        SMB3Levels.WATER_LAND_SPADE_BONUS_1,
        SMB3Levels.WATER_LAND_SPADE_BONUS_2,
        SMB3Levels.WATER_LAND_SPADE_BONUS_3,
        SMB3Levels.WATER_LAND_SPADE_BONUS_4,
        SMB3Levels.WATER_LAND_SPADE_BONUS_5,
    ),
    SMB3Worlds.GIANT_LAND: (
        SMB3Levels.GIANT_LAND_SPADE_BONUS_1,
        SMB3Levels.GIANT_LAND_SPADE_BONUS_2,
    ),
    SMB3Worlds.SKY_LAND: (
        SMB3Levels.SKY_LAND_SPADE_BONUS_1,
        SMB3Levels.SKY_LAND_SPADE_BONUS_2,
        SMB3Levels.SKY_LAND_SPADE_BONUS_3,
    ),
    SMB3Worlds.ICE_LAND: (
        SMB3Levels.ICE_LAND_SPADE_BONUS_1,
        SMB3Levels.ICE_LAND_SPADE_BONUS_2,
        SMB3Levels.ICE_LAND_SPADE_BONUS_3,
    ),
    SMB3Worlds.PIPE_LAND: (
        SMB3Levels.PIPE_LAND_SPADE_BONUS_1,
        SMB3Levels.PIPE_LAND_SPADE_BONUS_2,
        SMB3Levels.PIPE_LAND_SPADE_BONUS_3,
    ),
    SMB3Worlds.DARK_LAND: tuple(),
}

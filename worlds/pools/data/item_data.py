from typing import Dict, NamedTuple, Tuple

from BaseClasses import ItemClassification

from ..enums import PoolsItems, PoolsTags


class PoolsItemData(NamedTuple):
    archipelago_id: int
    classification: ItemClassification
    tags: Tuple[PoolsTags, ...]


item_base_offset: int = 10000

item_data: Dict[PoolsItems, PoolsItemData] = {
    PoolsItems.RUBBER_DUCK: PoolsItemData(
        archipelago_id=item_base_offset + 1,
        classification=ItemClassification.progression_deprioritized_skip_balancing,
        tags=(
            PoolsTags.GOAL_ITEM,
        )
    ),
    PoolsItems.LEVEL_1_UNLOCK: PoolsItemData(
        archipelago_id=item_base_offset + 2,
        classification=ItemClassification.progression,
        tags=(
            PoolsTags.LEVEL_UNLOCK_ITEM,
        )
    ),
    PoolsItems.LEVEL_2_UNLOCK: PoolsItemData(
        archipelago_id=item_base_offset + 3,
        classification=ItemClassification.progression,
        tags=(
            PoolsTags.LEVEL_UNLOCK_ITEM,
        )
    ),
    PoolsItems.LEVEL_3_UNLOCK: PoolsItemData(
        archipelago_id=item_base_offset + 4,
        classification=ItemClassification.progression,
        tags=(
            PoolsTags.LEVEL_UNLOCK_ITEM,
        )
    ),
    PoolsItems.LEVEL_4_UNLOCK: PoolsItemData(
        archipelago_id=item_base_offset + 5,
        classification=ItemClassification.progression,
        tags=(
            PoolsTags.LEVEL_UNLOCK_ITEM,
        )
    ),
    PoolsItems.LEVEL_5_UNLOCK: PoolsItemData(
        archipelago_id=item_base_offset + 6,
        classification=ItemClassification.progression,
        tags=(
            PoolsTags.LEVEL_UNLOCK_ITEM,
        )
    ),
    PoolsItems.LEVEL_6_UNLOCK: PoolsItemData(
        archipelago_id=item_base_offset + 7,
        classification=ItemClassification.progression,
        tags=(
            PoolsTags.LEVEL_UNLOCK_ITEM,
        )
    ),
    PoolsItems.LEVEL_0_UNLOCK: PoolsItemData(
        archipelago_id=item_base_offset + 8,
        classification=ItemClassification.progression,
        tags=(
            PoolsTags.LEVEL_UNLOCK_ITEM,
            PoolsTags.LEVEL_0_ITEM,
        )
    ),
    PoolsItems.POOLS_1T: PoolsItemData(
        archipelago_id=item_base_offset + 9,
        classification=ItemClassification.progression,
        tags=(
            PoolsTags.POOL_ITEM,
        )
    ),
    PoolsItems.POOLS_2T: PoolsItemData(
        archipelago_id=item_base_offset + 10,
        classification=ItemClassification.progression,
        tags=(
            PoolsTags.POOL_ITEM,
        )
    ),
    PoolsItems.POOLS_3T: PoolsItemData(
        archipelago_id=item_base_offset + 11,
        classification=ItemClassification.progression,
        tags=(
            PoolsTags.POOL_ITEM,
        )
    ),
    PoolsItems.POOLS_4T: PoolsItemData(
        archipelago_id=item_base_offset + 12,
        classification=ItemClassification.progression,
        tags=(
            PoolsTags.POOL_ITEM,
        )
    ),
    PoolsItems.POOLS_5T: PoolsItemData(
        archipelago_id=item_base_offset + 13,
        classification=ItemClassification.progression,
        tags=(
            PoolsTags.POOL_ITEM,
        )
    ),
    PoolsItems.POOLS_6T: PoolsItemData(
        archipelago_id=item_base_offset + 14,
        classification=ItemClassification.progression,
        tags=(
            PoolsTags.POOL_ITEM,
        )
    ),
    PoolsItems.POOLS_7T: PoolsItemData(
        archipelago_id=item_base_offset + 15,
        classification=ItemClassification.progression,
        tags=(
            PoolsTags.POOL_ITEM,
        )
    ),
    PoolsItems.POOLS_8T: PoolsItemData(
        archipelago_id=item_base_offset + 16,
        classification=ItemClassification.progression,
        tags=(
            PoolsTags.POOL_ITEM,
        )
    ),
    PoolsItems.POOLS_9T: PoolsItemData(
        archipelago_id=item_base_offset + 17,
        classification=ItemClassification.progression,
        tags=(
            PoolsTags.POOL_ITEM,
        )
    ),
    PoolsItems.POOLS_10T: PoolsItemData(
        archipelago_id=item_base_offset + 18,
        classification=ItemClassification.progression,
        tags=(
            PoolsTags.POOL_ITEM,
        )
    ),
    PoolsItems.POOLS_11T: PoolsItemData(
        archipelago_id=item_base_offset + 19,
        classification=ItemClassification.progression,
        tags=(
            PoolsTags.POOL_ITEM,
        )
    ),
    PoolsItems.CHAIRS_PLASTIC: PoolsItemData(
        archipelago_id=item_base_offset + 20,
        classification=ItemClassification.progression,
        tags=(
            PoolsTags.CHAIR_ITEM,
        )
    ),
    PoolsItems.DIVING_BOARDS: PoolsItemData(
        archipelago_id=item_base_offset + 21,
        classification=ItemClassification.progression,
        tags=(
            PoolsTags.BOARD_ITEM,
        )
    ),
    PoolsItems.SLIDES_RED: PoolsItemData(
        archipelago_id=item_base_offset + 22,
        classification=ItemClassification.progression,
        tags=(
            PoolsTags.SLIDE_ITEM,
        )
    ),
    PoolsItems.SLIDES_YELLOW: PoolsItemData(
        archipelago_id=item_base_offset + 23,
        classification=ItemClassification.progression,
        tags=(
            PoolsTags.SLIDE_ITEM,
        )
    ),
    PoolsItems.SLIDES_GREEN: PoolsItemData(
        archipelago_id=item_base_offset + 24,
        classification=ItemClassification.progression,
        tags=(
            PoolsTags.SLIDE_ITEM,
        )
    ),
    PoolsItems.SLIDES_BLUE: PoolsItemData(
        archipelago_id=item_base_offset + 25,
        classification=ItemClassification.progression,
        tags=(
            PoolsTags.SLIDE_ITEM,
        )
    ),
    PoolsItems.SLIDES_EXTRA: PoolsItemData(
        archipelago_id=item_base_offset + 26,
        classification=ItemClassification.progression,
        tags=(
            PoolsTags.SLIDE_ITEM,
            PoolsTags.LEVEL_0_ITEM,
        )
    ),
    PoolsItems.CHAIRS_SAUNA: PoolsItemData(
        archipelago_id=item_base_offset + 27,
        classification=ItemClassification.progression,
        tags=(
            PoolsTags.CHAIR_ITEM,
        )
    ),
    PoolsItems.CHAIRS_ARMCHAIR: PoolsItemData(
        archipelago_id=item_base_offset + 28,
        classification=ItemClassification.progression,
        tags=(
            PoolsTags.CHAIR_ITEM,
        )
    ),
    PoolsItems.CHAIRS_WOODEN: PoolsItemData(
        archipelago_id=item_base_offset + 29,
        classification=ItemClassification.progression,
        tags=(
            PoolsTags.CHAIR_ITEM,
        )
    ),
    PoolsItems.CHAIRS_SUBWAY: PoolsItemData(
        archipelago_id=item_base_offset + 30,
        classification=ItemClassification.progression,
        tags=(
            PoolsTags.CHAIR_ITEM,
        )
    ),
    PoolsItems.CHAIRS_PARK: PoolsItemData(
        archipelago_id=item_base_offset + 31,
        classification=ItemClassification.progression,
        tags=(
            PoolsTags.CHAIR_ITEM,
            PoolsTags.LEVEL_0_ITEM,
        )
    ),
    PoolsItems.CHAIRS_SOFA: PoolsItemData(
        archipelago_id=item_base_offset + 32,
        classification=ItemClassification.progression,
        tags=(
            PoolsTags.CHAIR_ITEM,
            PoolsTags.LEVEL_0_ITEM,
        )
    ),
    PoolsItems.PROGRESSIVE_MOVEMENT_SPEED: PoolsItemData(
        archipelago_id=item_base_offset + 33,
        classification=ItemClassification.useful,
        tags=(
            PoolsTags.USEFUL_ITEM,
        )
    ),
    PoolsItems.PROGRESSIVE_WATER_SPEED: PoolsItemData(
        archipelago_id=item_base_offset + 34,
        classification=ItemClassification.useful,
        tags=(
            PoolsTags.USEFUL_ITEM,
        )
    ),
    PoolsItems.RUN: PoolsItemData(
        archipelago_id=item_base_offset + 35,
        classification=ItemClassification.useful,
        tags=(
            PoolsTags.USEFUL_ITEM,
        )
    ),
    # PoolsItems.PROGRESSIVE_ON_DEMAND_REWIND: PoolsItemData(
    #     archipelago_id=item_base_offset + 36,
    #     classification=ItemClassification.useful,
    #     tags=(
    #         PoolsTags.USEFUL_ITEM,
    #     )
    # ),
    PoolsItems.TRAP_NO_LOOK: PoolsItemData(
        archipelago_id=item_base_offset + 37,
        classification=ItemClassification.trap,
        tags=(
            PoolsTags.TRAP_ITEM,
        )
    ),
    PoolsItems.TRAP_REWIND: PoolsItemData(
        archipelago_id=item_base_offset + 38,
        classification=ItemClassification.trap,
        tags=(
            PoolsTags.TRAP_ITEM,
        )
    ),
    PoolsItems.TRAP_SLOW: PoolsItemData(
        archipelago_id=item_base_offset + 39,
        classification=ItemClassification.trap,
        tags=(
            PoolsTags.TRAP_ITEM,
        )
    ),
    PoolsItems.TRAP_WET: PoolsItemData(
        archipelago_id=item_base_offset + 40,
        classification=ItemClassification.trap,
        tags=(
            PoolsTags.TRAP_ITEM,
        )
    ),
    PoolsItems.FILLER_SIGN_NO_LIFEGUARD: PoolsItemData(
        archipelago_id=item_base_offset + 41,
        classification=ItemClassification.filler,
        tags=(
            PoolsTags.FILLER_ITEM,
        )
    ),
    PoolsItems.FILLER_SIGN_NO_DIVING: PoolsItemData(
        archipelago_id=item_base_offset + 42,
        classification=ItemClassification.filler,
        tags=(
            PoolsTags.FILLER_ITEM,
        )
    ),
    PoolsItems.FILLER_SIGN_NO_RUNNING: PoolsItemData(
        archipelago_id=item_base_offset + 43,
        classification=ItemClassification.filler,
        tags=(
            PoolsTags.FILLER_ITEM,
        )
    ),
    PoolsItems.FILLER_SIGN_PLEASE_SHOWER: PoolsItemData(
        archipelago_id=item_base_offset + 44,
        classification=ItemClassification.filler,
        tags=(
            PoolsTags.FILLER_ITEM,
        )
    ),
    PoolsItems.FILLER_SIGN_WET_FLOOR: PoolsItemData(
        archipelago_id=item_base_offset + 45,
        classification=ItemClassification.filler,
        tags=(
            PoolsTags.FILLER_ITEM,
        )
    ),
    PoolsItems.FILLER_NOODLE: PoolsItemData(
        archipelago_id=item_base_offset + 46,
        classification=ItemClassification.filler,
        tags=(
            PoolsTags.FILLER_ITEM,
        )
    ),
    PoolsItems.FILLER_INFLATABLE: PoolsItemData(
        archipelago_id=item_base_offset + 47,
        classification=ItemClassification.filler,
        tags=(
            PoolsTags.FILLER_ITEM,
        )
    ),
    PoolsItems.FILLER_RING: PoolsItemData(
        archipelago_id=item_base_offset + 48,
        classification=ItemClassification.filler,
        tags=(
            PoolsTags.FILLER_ITEM,
        )
    ),
}

from typing import Dict, Tuple, Union

from ..enums import SuperMarioBrosAPItems, SuperMarioBrosAPRegions


Entrance = Tuple[SuperMarioBrosAPRegions, SuperMarioBrosAPRegions]

EntranceRule = Union[
    Tuple[
        Union[
            SuperMarioBrosAPItems,
            Tuple[SuperMarioBrosAPItems, int],
            Tuple[
                Tuple[SuperMarioBrosAPItems, int],
                ...,
            ],
        ],
        ...,
    ],
    None,
]

EntranceRuleData = Dict[
    Tuple[
        SuperMarioBrosAPRegions,
        SuperMarioBrosAPRegions,
    ],
    EntranceRule,
]

entrance_rule_data: EntranceRuleData = {
    (SuperMarioBrosAPRegions.MENU, SuperMarioBrosAPRegions.W_1_1): None,
    (SuperMarioBrosAPRegions.W_1_1, SuperMarioBrosAPRegions.W_1_2): None,
    (SuperMarioBrosAPRegions.W_1_2, SuperMarioBrosAPRegions.W_1_3): None,
    (SuperMarioBrosAPRegions.W_1_3, SuperMarioBrosAPRegions.W_1_4): (
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_CASTLE, 1),
            (SuperMarioBrosAPItems.WORLD_1_4, 1),
        ),
    ),
    (SuperMarioBrosAPRegions.W_1_4, SuperMarioBrosAPRegions.W_2_1): (
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL, 1),
            (SuperMarioBrosAPItems.WORLD_2_1, 1),
        ),
    ),
    (SuperMarioBrosAPRegions.W_2_1, SuperMarioBrosAPRegions.W_2_2): (
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL, 2),
            (SuperMarioBrosAPItems.WORLD_2_2, 1),
        ),
    ),
    (SuperMarioBrosAPRegions.W_2_2, SuperMarioBrosAPRegions.W_2_3): (
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL, 3),
            (SuperMarioBrosAPItems.WORLD_2_3, 1),
        ),
    ),
    (SuperMarioBrosAPRegions.W_2_3, SuperMarioBrosAPRegions.W_2_4): (
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_CASTLE, 2),
            (SuperMarioBrosAPItems.WORLD_2_4, 1),
        ),
    ),
    (SuperMarioBrosAPRegions.W_2_4, SuperMarioBrosAPRegions.W_3_1): (
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL, 4),
            (SuperMarioBrosAPItems.WORLD_3_1, 1),
        ),
    ),
    (SuperMarioBrosAPRegions.W_3_1, SuperMarioBrosAPRegions.W_3_2): (
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL, 5),
            (SuperMarioBrosAPItems.WORLD_3_2, 1),
        ),
    ),
    (SuperMarioBrosAPRegions.W_3_2, SuperMarioBrosAPRegions.W_3_3): (
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL, 6),
            (SuperMarioBrosAPItems.WORLD_3_3, 1),
        ),
    ),
    (SuperMarioBrosAPRegions.W_3_3, SuperMarioBrosAPRegions.W_3_4): (
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_CASTLE, 3),
            (SuperMarioBrosAPItems.WORLD_3_4, 1),
        ),
    ),
    (SuperMarioBrosAPRegions.W_3_4, SuperMarioBrosAPRegions.W_4_1): (
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL, 7),
            (SuperMarioBrosAPItems.WORLD_4_1, 1),
        ),
    ),
    (SuperMarioBrosAPRegions.W_4_1, SuperMarioBrosAPRegions.W_4_2): (
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL, 8),
            (SuperMarioBrosAPItems.WORLD_4_2, 1),
        ),
    ),
    (SuperMarioBrosAPRegions.W_4_2, SuperMarioBrosAPRegions.W_4_3): (
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL, 9),
            (SuperMarioBrosAPItems.WORLD_4_3, 1),
        ),
    ),
    (SuperMarioBrosAPRegions.W_4_3, SuperMarioBrosAPRegions.W_4_4): (
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_CASTLE, 4),
            (SuperMarioBrosAPItems.WORLD_4_4, 1),
        ),
    ),
    (SuperMarioBrosAPRegions.W_4_4, SuperMarioBrosAPRegions.W_5_1): (
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL, 10),
            (SuperMarioBrosAPItems.WORLD_5_1, 1),
        ),
    ),
    (SuperMarioBrosAPRegions.W_5_1, SuperMarioBrosAPRegions.W_5_2): (
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL, 11),
            (SuperMarioBrosAPItems.WORLD_5_2, 1),
        ),
    ),
    (SuperMarioBrosAPRegions.W_5_2, SuperMarioBrosAPRegions.W_5_3): (
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL, 12),
            (SuperMarioBrosAPItems.WORLD_5_3, 1),
        ),
    ),
    (SuperMarioBrosAPRegions.W_5_3, SuperMarioBrosAPRegions.W_5_4): (
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_CASTLE, 5),
            (SuperMarioBrosAPItems.WORLD_5_4, 1),
        ),
    ),
    (SuperMarioBrosAPRegions.W_5_4, SuperMarioBrosAPRegions.W_6_1): (
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL, 13),
            (SuperMarioBrosAPItems.WORLD_6_1, 1),
        ),
    ),
    (SuperMarioBrosAPRegions.W_6_1, SuperMarioBrosAPRegions.W_6_2): (
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL, 14),
            (SuperMarioBrosAPItems.WORLD_6_2, 1),
        ),
    ),
    (SuperMarioBrosAPRegions.W_6_2, SuperMarioBrosAPRegions.W_6_3): (
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL, 15),
            (SuperMarioBrosAPItems.WORLD_6_3, 1),
        ),
    ),
    (SuperMarioBrosAPRegions.W_6_3, SuperMarioBrosAPRegions.W_6_4): (
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_CASTLE, 6),
            (SuperMarioBrosAPItems.WORLD_6_4, 1),
        ),
    ),
    (SuperMarioBrosAPRegions.W_6_4, SuperMarioBrosAPRegions.W_7_1): (
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL, 16),
            (SuperMarioBrosAPItems.WORLD_7_1, 1),
        ),
    ),
    (SuperMarioBrosAPRegions.W_7_1, SuperMarioBrosAPRegions.W_7_2): (
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL, 17),
            (SuperMarioBrosAPItems.WORLD_7_2, 1),
        ),
    ),
    (SuperMarioBrosAPRegions.W_7_2, SuperMarioBrosAPRegions.W_7_3): (
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL, 18),
            (SuperMarioBrosAPItems.WORLD_7_3, 1),
        ),
    ),
    (SuperMarioBrosAPRegions.W_7_3, SuperMarioBrosAPRegions.W_7_4): (
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_CASTLE, 7),
            (SuperMarioBrosAPItems.WORLD_7_4, 1),
        ),
    ),
    (SuperMarioBrosAPRegions.W_7_4, SuperMarioBrosAPRegions.W_8_1): (
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL, 19),
            (SuperMarioBrosAPItems.WORLD_8_1, 1),
        ),
    ),
    (SuperMarioBrosAPRegions.W_8_1, SuperMarioBrosAPRegions.W_8_2): (
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL, 20),
            (SuperMarioBrosAPItems.WORLD_8_2, 1),
        ),
    ),
    (SuperMarioBrosAPRegions.W_8_2, SuperMarioBrosAPRegions.W_8_3): (
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL, 21),
            (SuperMarioBrosAPItems.WORLD_8_3, 1),
        ),
    ),
    (SuperMarioBrosAPRegions.W_8_3, SuperMarioBrosAPRegions.W_8_4): (
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_CASTLE, 8),
            (SuperMarioBrosAPItems.WORLD_8_4, 1),
        ),
    ),
}

entrance_rule_data_second_quest: EntranceRuleData = {
    (SuperMarioBrosAPRegions.MENU, SuperMarioBrosAPRegions.WSQ_1_1): (
        SuperMarioBrosAPItems.SECOND_QUEST_ACCESS,
    ),
    (SuperMarioBrosAPRegions.MENU, SuperMarioBrosAPRegions.WSQ_2_1): (
        SuperMarioBrosAPItems.SECOND_QUEST_ACCESS,
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL_SECOND_QUEST, 3),
            (SuperMarioBrosAPItems.WORLD_2_1_SECOND_QUEST, 1),
        ),
    ),
    (SuperMarioBrosAPRegions.MENU, SuperMarioBrosAPRegions.WSQ_3_1): (
        SuperMarioBrosAPItems.SECOND_QUEST_ACCESS,
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL_SECOND_QUEST, 6),
            (SuperMarioBrosAPItems.WORLD_3_1_SECOND_QUEST, 1),
        ),
    ),
    (SuperMarioBrosAPRegions.MENU, SuperMarioBrosAPRegions.WSQ_4_1): (
        SuperMarioBrosAPItems.SECOND_QUEST_ACCESS,
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL_SECOND_QUEST, 9),
            (SuperMarioBrosAPItems.WORLD_4_1_SECOND_QUEST, 1),
        ),
    ),
    (SuperMarioBrosAPRegions.MENU, SuperMarioBrosAPRegions.WSQ_5_1): (
        SuperMarioBrosAPItems.SECOND_QUEST_ACCESS,
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL_SECOND_QUEST, 12),
            (SuperMarioBrosAPItems.WORLD_5_1_SECOND_QUEST, 1),
        ),
    ),
    (SuperMarioBrosAPRegions.MENU, SuperMarioBrosAPRegions.WSQ_6_1): (
        SuperMarioBrosAPItems.SECOND_QUEST_ACCESS,
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL_SECOND_QUEST, 15),
            (SuperMarioBrosAPItems.WORLD_6_1_SECOND_QUEST, 1),
        ),
    ),
    (SuperMarioBrosAPRegions.MENU, SuperMarioBrosAPRegions.WSQ_7_1): (
        SuperMarioBrosAPItems.SECOND_QUEST_ACCESS,
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL_SECOND_QUEST, 18),
            (SuperMarioBrosAPItems.WORLD_7_1_SECOND_QUEST, 1),
        ),
    ),
    (SuperMarioBrosAPRegions.MENU, SuperMarioBrosAPRegions.WSQ_8_1): (
        SuperMarioBrosAPItems.SECOND_QUEST_ACCESS,
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL_SECOND_QUEST, 21),
            (SuperMarioBrosAPItems.WORLD_8_1_SECOND_QUEST, 1),
        ),
    ),
    (SuperMarioBrosAPRegions.WSQ_1_1, SuperMarioBrosAPRegions.WSQ_1_2): (
        SuperMarioBrosAPItems.SECOND_QUEST_ACCESS,
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL_SECOND_QUEST, 1),
            (SuperMarioBrosAPItems.WORLD_1_2_SECOND_QUEST, 1),
        )
    ),
    (SuperMarioBrosAPRegions.WSQ_1_2, SuperMarioBrosAPRegions.WSQ_1_3): (
        SuperMarioBrosAPItems.SECOND_QUEST_ACCESS,
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL_SECOND_QUEST, 2),
            (SuperMarioBrosAPItems.WORLD_1_3_SECOND_QUEST, 1),
        )
    ),
    (SuperMarioBrosAPRegions.WSQ_1_3, SuperMarioBrosAPRegions.WSQ_1_4): (
        SuperMarioBrosAPItems.SECOND_QUEST_ACCESS,
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_CASTLE_SECOND_QUEST, 1),
            (SuperMarioBrosAPItems.WORLD_1_4_SECOND_QUEST, 1),
        )
    ),
    (SuperMarioBrosAPRegions.WSQ_1_4, SuperMarioBrosAPRegions.WSQ_2_1): (
        SuperMarioBrosAPItems.SECOND_QUEST_ACCESS,
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL_SECOND_QUEST, 3),
            (SuperMarioBrosAPItems.WORLD_2_1_SECOND_QUEST, 1),
        )
    ),
    (SuperMarioBrosAPRegions.WSQ_2_1, SuperMarioBrosAPRegions.WSQ_2_2): (
        SuperMarioBrosAPItems.SECOND_QUEST_ACCESS,
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL_SECOND_QUEST, 4),
            (SuperMarioBrosAPItems.WORLD_2_2_SECOND_QUEST, 1),
        )
    ),
    (SuperMarioBrosAPRegions.WSQ_2_2, SuperMarioBrosAPRegions.WSQ_2_3): (
        SuperMarioBrosAPItems.SECOND_QUEST_ACCESS,
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL_SECOND_QUEST, 5),
            (SuperMarioBrosAPItems.WORLD_2_3_SECOND_QUEST, 1),
        )
    ),
    (SuperMarioBrosAPRegions.WSQ_2_3, SuperMarioBrosAPRegions.WSQ_2_4): (
        SuperMarioBrosAPItems.SECOND_QUEST_ACCESS,
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_CASTLE_SECOND_QUEST, 2),
            (SuperMarioBrosAPItems.WORLD_2_4_SECOND_QUEST, 1),
        )
    ),
    (SuperMarioBrosAPRegions.WSQ_2_4, SuperMarioBrosAPRegions.WSQ_3_1): (
        SuperMarioBrosAPItems.SECOND_QUEST_ACCESS,
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL_SECOND_QUEST, 6),
            (SuperMarioBrosAPItems.WORLD_3_1_SECOND_QUEST, 1),
        )
    ),
    (SuperMarioBrosAPRegions.WSQ_3_1, SuperMarioBrosAPRegions.WSQ_3_2): (
        SuperMarioBrosAPItems.SECOND_QUEST_ACCESS,
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL_SECOND_QUEST, 7),
            (SuperMarioBrosAPItems.WORLD_3_2_SECOND_QUEST, 1),
        )
    ),
    (SuperMarioBrosAPRegions.WSQ_3_2, SuperMarioBrosAPRegions.WSQ_3_3): (
        SuperMarioBrosAPItems.SECOND_QUEST_ACCESS,
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL_SECOND_QUEST, 8),
            (SuperMarioBrosAPItems.WORLD_3_3_SECOND_QUEST, 1),
        )
    ),
    (SuperMarioBrosAPRegions.WSQ_3_3, SuperMarioBrosAPRegions.WSQ_3_4): (
        SuperMarioBrosAPItems.SECOND_QUEST_ACCESS,
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_CASTLE_SECOND_QUEST, 3),
            (SuperMarioBrosAPItems.WORLD_3_4_SECOND_QUEST, 1),
        )
    ),
    (SuperMarioBrosAPRegions.WSQ_3_4, SuperMarioBrosAPRegions.WSQ_4_1): (
        SuperMarioBrosAPItems.SECOND_QUEST_ACCESS,
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL_SECOND_QUEST, 9),
            (SuperMarioBrosAPItems.WORLD_4_1_SECOND_QUEST, 1),
        )
    ),
    (SuperMarioBrosAPRegions.WSQ_4_1, SuperMarioBrosAPRegions.WSQ_4_2): (
        SuperMarioBrosAPItems.SECOND_QUEST_ACCESS,
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL_SECOND_QUEST, 10),
            (SuperMarioBrosAPItems.WORLD_4_2_SECOND_QUEST, 1),
        )
    ),
    (SuperMarioBrosAPRegions.WSQ_4_2, SuperMarioBrosAPRegions.WSQ_4_3): (
        SuperMarioBrosAPItems.SECOND_QUEST_ACCESS,
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL_SECOND_QUEST, 11),
            (SuperMarioBrosAPItems.WORLD_4_3_SECOND_QUEST, 1),
        )
    ),
    (SuperMarioBrosAPRegions.WSQ_4_3, SuperMarioBrosAPRegions.WSQ_4_4): (
        SuperMarioBrosAPItems.SECOND_QUEST_ACCESS,
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_CASTLE_SECOND_QUEST, 4),
            (SuperMarioBrosAPItems.WORLD_4_4_SECOND_QUEST, 1),
        )
    ),
    (SuperMarioBrosAPRegions.WSQ_4_4, SuperMarioBrosAPRegions.WSQ_5_1): (
        SuperMarioBrosAPItems.SECOND_QUEST_ACCESS,
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL_SECOND_QUEST, 12),
            (SuperMarioBrosAPItems.WORLD_5_1_SECOND_QUEST, 1),
        )
    ),
    (SuperMarioBrosAPRegions.WSQ_5_1, SuperMarioBrosAPRegions.WSQ_5_2): (
        SuperMarioBrosAPItems.SECOND_QUEST_ACCESS,
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL_SECOND_QUEST, 13),
            (SuperMarioBrosAPItems.WORLD_5_2_SECOND_QUEST, 1),
        )
    ),
    (SuperMarioBrosAPRegions.WSQ_5_2, SuperMarioBrosAPRegions.WSQ_5_3): (
        SuperMarioBrosAPItems.SECOND_QUEST_ACCESS,
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL_SECOND_QUEST, 14),
            (SuperMarioBrosAPItems.WORLD_5_3_SECOND_QUEST, 1),
        )
    ),
    (SuperMarioBrosAPRegions.WSQ_5_3, SuperMarioBrosAPRegions.WSQ_5_4): (
        SuperMarioBrosAPItems.SECOND_QUEST_ACCESS,
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_CASTLE_SECOND_QUEST, 5),
            (SuperMarioBrosAPItems.WORLD_5_4_SECOND_QUEST, 1),
        )
    ),
    (SuperMarioBrosAPRegions.WSQ_5_4, SuperMarioBrosAPRegions.WSQ_6_1): (
        SuperMarioBrosAPItems.SECOND_QUEST_ACCESS,
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL_SECOND_QUEST, 15),
            (SuperMarioBrosAPItems.WORLD_6_1_SECOND_QUEST, 1),
        )
    ),
    (SuperMarioBrosAPRegions.WSQ_6_1, SuperMarioBrosAPRegions.WSQ_6_2): (
        SuperMarioBrosAPItems.SECOND_QUEST_ACCESS,
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL_SECOND_QUEST, 16),
            (SuperMarioBrosAPItems.WORLD_6_2_SECOND_QUEST, 1),
        )
    ),
    (SuperMarioBrosAPRegions.WSQ_6_2, SuperMarioBrosAPRegions.WSQ_6_3): (
        SuperMarioBrosAPItems.SECOND_QUEST_ACCESS,
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL_SECOND_QUEST, 17),
            (SuperMarioBrosAPItems.WORLD_6_3_SECOND_QUEST, 1),
        )
    ),
    (SuperMarioBrosAPRegions.WSQ_6_3, SuperMarioBrosAPRegions.WSQ_6_4): (
        SuperMarioBrosAPItems.SECOND_QUEST_ACCESS,
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_CASTLE_SECOND_QUEST, 6),
            (SuperMarioBrosAPItems.WORLD_6_4_SECOND_QUEST, 1),
        )
    ),
    (SuperMarioBrosAPRegions.WSQ_6_4, SuperMarioBrosAPRegions.WSQ_7_1): (
        SuperMarioBrosAPItems.SECOND_QUEST_ACCESS,
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL_SECOND_QUEST, 18),
            (SuperMarioBrosAPItems.WORLD_7_1_SECOND_QUEST, 1),
        )
    ),
    (SuperMarioBrosAPRegions.WSQ_7_1, SuperMarioBrosAPRegions.WSQ_7_2): (
        SuperMarioBrosAPItems.SECOND_QUEST_ACCESS,
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL_SECOND_QUEST, 19),
            (SuperMarioBrosAPItems.WORLD_7_2_SECOND_QUEST, 1),
        )
    ),
    (SuperMarioBrosAPRegions.WSQ_7_2, SuperMarioBrosAPRegions.WSQ_7_3): (
        SuperMarioBrosAPItems.SECOND_QUEST_ACCESS,
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL_SECOND_QUEST, 20),
            (SuperMarioBrosAPItems.WORLD_7_3_SECOND_QUEST, 1),
        )
    ),
    (SuperMarioBrosAPRegions.WSQ_7_3, SuperMarioBrosAPRegions.WSQ_7_4): (
        SuperMarioBrosAPItems.SECOND_QUEST_ACCESS,
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_CASTLE_SECOND_QUEST, 7),
            (SuperMarioBrosAPItems.WORLD_7_4_SECOND_QUEST, 1),
        )
    ),
    (SuperMarioBrosAPRegions.WSQ_7_4, SuperMarioBrosAPRegions.WSQ_8_1): (
        SuperMarioBrosAPItems.SECOND_QUEST_ACCESS,
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL_SECOND_QUEST, 21),
            (SuperMarioBrosAPItems.WORLD_8_1_SECOND_QUEST, 1),
        )
    ),
    (SuperMarioBrosAPRegions.WSQ_8_1, SuperMarioBrosAPRegions.WSQ_8_2): (
        SuperMarioBrosAPItems.SECOND_QUEST_ACCESS,
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL_SECOND_QUEST, 22),
            (SuperMarioBrosAPItems.WORLD_8_2_SECOND_QUEST, 1),
        )
    ),
    (SuperMarioBrosAPRegions.WSQ_8_2, SuperMarioBrosAPRegions.WSQ_8_3): (
        SuperMarioBrosAPItems.SECOND_QUEST_ACCESS,
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_LEVEL_SECOND_QUEST, 23),
            (SuperMarioBrosAPItems.WORLD_8_3_SECOND_QUEST, 1),
        )
    ),
    (SuperMarioBrosAPRegions.WSQ_8_3, SuperMarioBrosAPRegions.WSQ_8_4): (
        SuperMarioBrosAPItems.SECOND_QUEST_ACCESS,
        (
            (SuperMarioBrosAPItems.PROGRESSIVE_CASTLE_SECOND_QUEST, 8),
            (SuperMarioBrosAPItems.WORLD_8_4_SECOND_QUEST, 1),
        )
    ),
}

entrance_rule_data_goal: EntranceRuleData = {
    (SuperMarioBrosAPRegions.W_8_4, SuperMarioBrosAPRegions.VICTORY): None,
}

entrance_rule_data_goal_second_quest: EntranceRuleData = {
    (SuperMarioBrosAPRegions.WSQ_8_4, SuperMarioBrosAPRegions.VICTORY): None,
}

# Entrances for Warp Zones will have to be created dynamically based on the outcome of level randomization
# They might also logically not matter at all since if you warp to a level you don't have access to, you will die
# That said, it could be possible to make non-progressive level unlocks, allowing warp zone routing!

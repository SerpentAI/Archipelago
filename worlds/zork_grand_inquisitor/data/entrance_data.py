from typing import Dict, List, Tuple, Union

from ..enums import (
    ZorkGrandInquisitorEvents,
    ZorkGrandInquisitorGoals,
    ZorkGrandInquisitorItems,
    ZorkGrandInquisitorRegions,
)


Entrance = Tuple[ZorkGrandInquisitorRegions, ZorkGrandInquisitorRegions]

EntranceRule = Union[
    Tuple[
        Tuple[
            Union[
                ZorkGrandInquisitorEvents,
                ZorkGrandInquisitorItems,
                ZorkGrandInquisitorRegions,
                List[Union[ZorkGrandInquisitorItems, int]],
            ],
            ...,
        ],
        ...,
    ],
    None,
]

EntranceRuleData = Dict[
    Tuple[
        ZorkGrandInquisitorRegions,
        ZorkGrandInquisitorRegions,
    ],
    EntranceRule,
]

entrance_rule_data: EntranceRuleData = {
    (ZorkGrandInquisitorRegions.BOTTOM_OF_THE_WELL, ZorkGrandInquisitorRegions.CROSSROADS): None,
    (ZorkGrandInquisitorRegions.BOTTOM_OF_THE_WELL, ZorkGrandInquisitorRegions.OUTSIDE_PORT_FOOZLE_WELL): (
        (
            ZorkGrandInquisitorItems.WELL_ROPE,
            (
                ZorkGrandInquisitorItems.HOTSPOT_BUCKET,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_CROSSROADS,
            ),
        ),
    ),
    (ZorkGrandInquisitorRegions.CROSSROADS, ZorkGrandInquisitorRegions.BOTTOM_OF_THE_WELL): None,
    (ZorkGrandInquisitorRegions.CROSSROADS, ZorkGrandInquisitorRegions.DM_LAIR): (
        (
            ZorkGrandInquisitorItems.SWORD,
            (
                ZorkGrandInquisitorItems.HOTSPOT_DUNGEON_MASTERS_LAIR_ENTRANCE,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_CROSSROADS,
            ),
        ),
    ),
    (ZorkGrandInquisitorRegions.CROSSROADS, ZorkGrandInquisitorRegions.GUE_TECH_ENTRANCE): (
        (
            ZorkGrandInquisitorItems.SPELL_REZROV,
            (
                ZorkGrandInquisitorItems.HOTSPOT_IN_MAGIC_WE_TRUST_DOOR,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_CROSSROADS,
            ),
        ),
    ),
    (ZorkGrandInquisitorRegions.CROSSROADS, ZorkGrandInquisitorRegions.SUBWAY_CROSSROADS): (
        (
            ZorkGrandInquisitorItems.SUBWAY_TOKEN,
            (
                ZorkGrandInquisitorItems.HOTSPOT_SUBWAY_TOKEN_SLOT,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_CROSSROADS,
            ),
        ),
    ),
    (ZorkGrandInquisitorRegions.CROSSROADS, ZorkGrandInquisitorRegions.TELEPORTER): None,
    (ZorkGrandInquisitorRegions.DM_LAIR, ZorkGrandInquisitorRegions.CROSSROADS): None,
    (ZorkGrandInquisitorRegions.DM_LAIR, ZorkGrandInquisitorRegions.DM_LAIR_INTERIOR): (
        (
            ZorkGrandInquisitorEvents.DOOR_SMOKED_CIGAR,
            ZorkGrandInquisitorEvents.DOOR_DRANK_MEAD,
        ),
    ),
    (ZorkGrandInquisitorRegions.DM_LAIR, ZorkGrandInquisitorRegions.TELEPORTER): None,
    (ZorkGrandInquisitorRegions.DM_LAIR_INTERIOR, ZorkGrandInquisitorRegions.DM_LAIR): (
        (
            (
                ZorkGrandInquisitorItems.HOTSPOT_DUNGEON_MASTERS_HOUSE_EXIT,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_DM_LAIR,
            ),
        ),
    ),
    (ZorkGrandInquisitorRegions.DM_LAIR_INTERIOR, ZorkGrandInquisitorRegions.WALKING_CASTLE): (
        (
            (
                ZorkGrandInquisitorItems.HOTSPOT_BLINDS,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_DM_LAIR,
            ),
            ZorkGrandInquisitorItems.SPELL_OBIDIL,
        ),
    ),
    (ZorkGrandInquisitorRegions.DM_LAIR_INTERIOR, ZorkGrandInquisitorRegions.WHITE_HOUSE): (
        (
            (
                ZorkGrandInquisitorItems.HOTSPOT_CLOSET_DOOR,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_DM_LAIR,
            ),
            ZorkGrandInquisitorItems.SPELL_NARWILE,
            ZorkGrandInquisitorItems.SPELL_YASTARD,
        ),
    ),
    (ZorkGrandInquisitorRegions.DRAGON_ARCHIPELAGO, ZorkGrandInquisitorRegions.DRAGON_ARCHIPELAGO_DRAGON): (
        (
            ZorkGrandInquisitorItems.TOTEM_GRIFF,
            (
                ZorkGrandInquisitorItems.HOTSPOT_DRAGON_CLAW,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_DRAGON_ARCHIPELAGO,
            ),
        ),
    ),
    (ZorkGrandInquisitorRegions.DRAGON_ARCHIPELAGO, ZorkGrandInquisitorRegions.HADES_BEYOND_GATES): None,
    (ZorkGrandInquisitorRegions.DRAGON_ARCHIPELAGO_DRAGON, ZorkGrandInquisitorRegions.DRAGON_ARCHIPELAGO): None,
    (ZorkGrandInquisitorRegions.GUE_TECH, ZorkGrandInquisitorRegions.GUE_TECH_ENTRANCE): (
        (
            (
                ZorkGrandInquisitorItems.HOTSPOT_GUE_TECH_WINDOWS,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_GUE_TECH,
            ),
        ),
    ),
    (ZorkGrandInquisitorRegions.GUE_TECH, ZorkGrandInquisitorRegions.GUE_TECH_HALLWAY): (
        (
            ZorkGrandInquisitorItems.SPELL_IGRAM,
            (
                ZorkGrandInquisitorItems.HOTSPOT_PURPLE_WORDS,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_GUE_TECH,
            ),
        ),
    ),
    (ZorkGrandInquisitorRegions.GUE_TECH, ZorkGrandInquisitorRegions.GUE_TECH_OUTSIDE): (
        (
            (
                ZorkGrandInquisitorItems.HOTSPOT_GUE_TECH_DOOR,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_GUE_TECH,
            ),
        ),
    ),
    (ZorkGrandInquisitorRegions.GUE_TECH_ENTRANCE, ZorkGrandInquisitorRegions.CROSSROADS): None,
    (ZorkGrandInquisitorRegions.GUE_TECH_ENTRANCE, ZorkGrandInquisitorRegions.GUE_TECH): (
        (
            (
                ZorkGrandInquisitorItems.HOTSPOT_GUE_TECH_WINDOWS,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_GUE_TECH,
            ),
        ),
    ),
    (ZorkGrandInquisitorRegions.GUE_TECH_HALLWAY, ZorkGrandInquisitorRegions.GUE_TECH): None,
    (ZorkGrandInquisitorRegions.GUE_TECH_HALLWAY, ZorkGrandInquisitorRegions.SPELL_LAB_BRIDGE): (
        (
            ZorkGrandInquisitorItems.STUDENT_ID,
            (
                ZorkGrandInquisitorItems.HOTSPOT_STUDENT_ID_MACHINE,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_GUE_TECH,
            ),
        ),
    ),
    (ZorkGrandInquisitorRegions.GUE_TECH_OUTSIDE, ZorkGrandInquisitorRegions.GUE_TECH): (
        (
            (
                ZorkGrandInquisitorItems.HOTSPOT_GUE_TECH_WINDOWS,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_GUE_TECH,
            ),
        ),
    ),
    (ZorkGrandInquisitorRegions.GUE_TECH_OUTSIDE, ZorkGrandInquisitorRegions.TELEPORTER): None,
    (ZorkGrandInquisitorRegions.HADES, ZorkGrandInquisitorRegions.HADES_BEYOND_GATES): (
        (
            ZorkGrandInquisitorItems.SPELL_SNAVIG,
            ZorkGrandInquisitorItems.TOTEM_BROG,  # Visually hiding this totem is tied to owning it; no choice
        ),
    ),
    (ZorkGrandInquisitorRegions.HADES, ZorkGrandInquisitorRegions.HADES_SHORE): (
        (
            ZorkGrandInquisitorItems.POUCH_OF_ZORKMIDS,
            ZorkGrandInquisitorItems.SPELL_SNAVIG,
        ),
    ),
    (ZorkGrandInquisitorRegions.HADES_BEYOND_GATES, ZorkGrandInquisitorRegions.DRAGON_ARCHIPELAGO): (
        (
            ZorkGrandInquisitorItems.SPELL_NARWILE,
            ZorkGrandInquisitorItems.SPELL_YASTARD,
        ),
    ),
    (ZorkGrandInquisitorRegions.HADES_BEYOND_GATES, ZorkGrandInquisitorRegions.HADES): None,
    (ZorkGrandInquisitorRegions.HADES_SHORE, ZorkGrandInquisitorRegions.HADES): (
        (
            (
                ZorkGrandInquisitorItems.HOTSPOT_HADES_PHONE_RECEIVER,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_HADES,
            ),
            (
                ZorkGrandInquisitorItems.HOTSPOT_HADES_PHONE_BUTTONS,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_HADES,
            ),
            ZorkGrandInquisitorItems.POUCH_OF_ZORKMIDS,
        ),
    ),
    (ZorkGrandInquisitorRegions.HADES_SHORE, ZorkGrandInquisitorRegions.SUBWAY_HADES): None,
    (ZorkGrandInquisitorRegions.HADES_SHORE, ZorkGrandInquisitorRegions.TELEPORTER): None,
    (ZorkGrandInquisitorRegions.MONASTERY, ZorkGrandInquisitorRegions.HADES_SHORE): (
        (
            ZorkGrandInquisitorItems.TOTEMIZER_DESTINATION_STRAIGHT_TO_HELL,
            (
                ZorkGrandInquisitorItems.HOTSPOT_TOTEMIZER_WHEELS,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_MONASTERY,
            ),
            (
                ZorkGrandInquisitorItems.HOTSPOT_TOTEMIZER_SWITCH,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_MONASTERY,
            ),
        ),
    ),
    (ZorkGrandInquisitorRegions.MONASTERY, ZorkGrandInquisitorRegions.MONASTERY_EXHIBIT): (
        (
            ZorkGrandInquisitorItems.TOTEMIZER_DESTINATION_HALL_OF_INQUISITION,
            (
                ZorkGrandInquisitorItems.HOTSPOT_TOTEMIZER_WHEELS,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_MONASTERY,
            ),
            (
                ZorkGrandInquisitorItems.HOTSPOT_TOTEMIZER_SWITCH,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_MONASTERY,
            ),
        ),
    ),
    (ZorkGrandInquisitorRegions.MONASTERY, ZorkGrandInquisitorRegions.SUBWAY_MONASTERY): None,
    (ZorkGrandInquisitorRegions.MONASTERY_EXHIBIT, ZorkGrandInquisitorRegions.MONASTERY): None,
    (ZorkGrandInquisitorRegions.MONASTERY_EXHIBIT, ZorkGrandInquisitorRegions.PORT_FOOZLE_PAST): (
        (
            (
                ZorkGrandInquisitorItems.HOTSPOT_CLOSING_THE_TIME_TUNNELS_LEVER,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_MONASTERY,
            ),
            (
                ZorkGrandInquisitorItems.HOTSPOT_CLOSING_THE_TIME_TUNNELS_HAMMER_SLOT,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_MONASTERY,
            ),
            ZorkGrandInquisitorItems.LARGE_TELEGRAPH_HAMMER,
            ZorkGrandInquisitorItems.SPELL_NARWILE,
            ZorkGrandInquisitorItems.SPELL_YASTARD,
        ),
    ),
    (
        ZorkGrandInquisitorRegions.OUTSIDE_PORT_FOOZLE_INQUISITION_HQ,
        ZorkGrandInquisitorRegions.OUTSIDE_PORT_FOOZLE_SIGNPOST
    ): None,
    (
        ZorkGrandInquisitorRegions.OUTSIDE_PORT_FOOZLE_SIGNPOST,
        ZorkGrandInquisitorRegions.OUTSIDE_PORT_FOOZLE_INQUISITION_HQ
    ): None,
    (
        ZorkGrandInquisitorRegions.OUTSIDE_PORT_FOOZLE_SIGNPOST,
        ZorkGrandInquisitorRegions.OUTSIDE_PORT_FOOZLE_WELL
    ): None,
    (ZorkGrandInquisitorRegions.OUTSIDE_PORT_FOOZLE_SIGNPOST, ZorkGrandInquisitorRegions.PORT_FOOZLE): None,
    (ZorkGrandInquisitorRegions.OUTSIDE_PORT_FOOZLE_WELL, ZorkGrandInquisitorRegions.BOTTOM_OF_THE_WELL): (
        (ZorkGrandInquisitorItems.WELL_ROPE,),
    ),
    (
        ZorkGrandInquisitorRegions.OUTSIDE_PORT_FOOZLE_WELL,
        ZorkGrandInquisitorRegions.OUTSIDE_PORT_FOOZLE_SIGNPOST
    ): None,
    (ZorkGrandInquisitorRegions.PORT_FOOZLE, ZorkGrandInquisitorRegions.OUTSIDE_PORT_FOOZLE_SIGNPOST): None,
    (ZorkGrandInquisitorRegions.PORT_FOOZLE, ZorkGrandInquisitorRegions.PORT_FOOZLE_JACKS_SHOP): (
        (
            ZorkGrandInquisitorItems.CIGAR,
            (
                ZorkGrandInquisitorItems.HOTSPOT_JACKS_DOOR,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_PORT_FOOZLE,
            ),
            (
                ZorkGrandInquisitorItems.HOTSPOT_GRAND_INQUISITOR_DOLL,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_PORT_FOOZLE,
            ),
        ),
    ),
    (ZorkGrandInquisitorRegions.PORT_FOOZLE_JACKS_SHOP, ZorkGrandInquisitorRegions.PORT_FOOZLE): None,
    (ZorkGrandInquisitorRegions.PORT_FOOZLE_PAST, ZorkGrandInquisitorRegions.MONASTERY_EXHIBIT): None,
    (ZorkGrandInquisitorRegions.PORT_FOOZLE_PAST, ZorkGrandInquisitorRegions.PORT_FOOZLE_PAST_TAVERN): (
        (
            ZorkGrandInquisitorItems.TOTEM_LUCY,
            (
                ZorkGrandInquisitorItems.HOTSPOT_PORT_FOOZLE_PAST_TAVERN_DOOR,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_PORT_FOOZLE_PAST,
            ),
        ),
    ),
    (ZorkGrandInquisitorRegions.PORT_FOOZLE_PAST_TAVERN, ZorkGrandInquisitorRegions.PORT_FOOZLE_PAST): None,
    (ZorkGrandInquisitorRegions.SPELL_LAB, ZorkGrandInquisitorRegions.SPELL_LAB_BRIDGE): None,
    (ZorkGrandInquisitorRegions.SPELL_LAB_BRIDGE, ZorkGrandInquisitorRegions.GUE_TECH_HALLWAY): (
        (
            (
                ZorkGrandInquisitorItems.HOTSPOT_SPELL_LAB_BRIDGE_EXIT,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_SPELL_LAB,
            ),
        ),
    ),
    (ZorkGrandInquisitorRegions.SPELL_LAB_BRIDGE, ZorkGrandInquisitorRegions.SPELL_LAB): (
        (
            ZorkGrandInquisitorItems.SWORD,
            (
                ZorkGrandInquisitorItems.HOTSPOT_ROPE_BRIDGE,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_SPELL_LAB,
            ),
            ZorkGrandInquisitorEvents.DAM_DESTROYED,
            ZorkGrandInquisitorItems.SPELL_GOLGATEM,
            (
                ZorkGrandInquisitorItems.HOTSPOT_SPELL_LAB_CHASM,
                ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_SPELL_LAB,
            ),
        ),
    ),
    (ZorkGrandInquisitorRegions.SPELL_LAB_BRIDGE, ZorkGrandInquisitorRegions.TELEPORTER): None,
    (ZorkGrandInquisitorRegions.SUBWAY_CROSSROADS, ZorkGrandInquisitorRegions.CROSSROADS): None,
    (ZorkGrandInquisitorRegions.SUBWAY_CROSSROADS, ZorkGrandInquisitorRegions.SUBWAY_FLOOD_CONTROL_DAM): (
        (
            ZorkGrandInquisitorItems.SPELL_KENDALL,
            ZorkGrandInquisitorItems.SUBWAY_DESTINATION_FLOOD_CONTROL_DAM,
        ),
    ),
    (ZorkGrandInquisitorRegions.SUBWAY_CROSSROADS, ZorkGrandInquisitorRegions.SUBWAY_HADES): (
        (
            ZorkGrandInquisitorItems.SPELL_KENDALL,
            ZorkGrandInquisitorItems.SUBWAY_DESTINATION_HADES,
        ),
    ),
    (ZorkGrandInquisitorRegions.SUBWAY_CROSSROADS, ZorkGrandInquisitorRegions.SUBWAY_MONASTERY): (
        (
            ZorkGrandInquisitorItems.SPELL_KENDALL,
            ZorkGrandInquisitorItems.SUBWAY_DESTINATION_MONASTERY,
        ),
    ),
    (ZorkGrandInquisitorRegions.SUBWAY_FLOOD_CONTROL_DAM, ZorkGrandInquisitorRegions.SUBWAY_CROSSROADS): (
        (ZorkGrandInquisitorItems.SUBWAY_DESTINATION_CROSSROADS,),
    ),
    (ZorkGrandInquisitorRegions.SUBWAY_FLOOD_CONTROL_DAM, ZorkGrandInquisitorRegions.SUBWAY_HADES): (
        (ZorkGrandInquisitorItems.SUBWAY_DESTINATION_HADES,),
    ),
    (ZorkGrandInquisitorRegions.SUBWAY_FLOOD_CONTROL_DAM, ZorkGrandInquisitorRegions.SUBWAY_MONASTERY): (
        (ZorkGrandInquisitorItems.SUBWAY_DESTINATION_MONASTERY,),
    ),
    (ZorkGrandInquisitorRegions.SUBWAY_HADES, ZorkGrandInquisitorRegions.HADES_SHORE): None,
    (ZorkGrandInquisitorRegions.SUBWAY_HADES, ZorkGrandInquisitorRegions.SUBWAY_CROSSROADS): (
        (ZorkGrandInquisitorItems.SUBWAY_DESTINATION_CROSSROADS,),
    ),
    (ZorkGrandInquisitorRegions.SUBWAY_HADES, ZorkGrandInquisitorRegions.SUBWAY_FLOOD_CONTROL_DAM): (
        (ZorkGrandInquisitorItems.SUBWAY_DESTINATION_FLOOD_CONTROL_DAM,),
    ),
    (ZorkGrandInquisitorRegions.SUBWAY_HADES, ZorkGrandInquisitorRegions.SUBWAY_MONASTERY): (
        (ZorkGrandInquisitorItems.SUBWAY_DESTINATION_MONASTERY,),
    ),
    (ZorkGrandInquisitorRegions.SUBWAY_MONASTERY, ZorkGrandInquisitorRegions.MONASTERY): (
        (ZorkGrandInquisitorItems.MONASTERY_ROPE,),
    ),
    (ZorkGrandInquisitorRegions.SUBWAY_MONASTERY, ZorkGrandInquisitorRegions.SUBWAY_CROSSROADS): (
        (ZorkGrandInquisitorItems.SUBWAY_DESTINATION_CROSSROADS,),
    ),
    (ZorkGrandInquisitorRegions.SUBWAY_MONASTERY, ZorkGrandInquisitorRegions.SUBWAY_FLOOD_CONTROL_DAM): (
        (ZorkGrandInquisitorItems.SUBWAY_DESTINATION_FLOOD_CONTROL_DAM,),
    ),
    (ZorkGrandInquisitorRegions.SUBWAY_MONASTERY, ZorkGrandInquisitorRegions.SUBWAY_HADES): (
        (ZorkGrandInquisitorItems.SUBWAY_DESTINATION_HADES,),
    ),
    (ZorkGrandInquisitorRegions.SUBWAY_MONASTERY, ZorkGrandInquisitorRegions.TELEPORTER): None,
    (ZorkGrandInquisitorRegions.TELEPORTER, ZorkGrandInquisitorRegions.CROSSROADS): (
        (
            ZorkGrandInquisitorItems.MAP,
            ZorkGrandInquisitorItems.TELEPORTER_DESTINATION_CROSSROADS,
        ),
    ),
    (ZorkGrandInquisitorRegions.TELEPORTER, ZorkGrandInquisitorRegions.DM_LAIR): (
        (
            ZorkGrandInquisitorItems.MAP,
            ZorkGrandInquisitorItems.TELEPORTER_DESTINATION_DM_LAIR,
        ),
    ),
    (ZorkGrandInquisitorRegions.TELEPORTER, ZorkGrandInquisitorRegions.GUE_TECH_OUTSIDE): (
        (
            ZorkGrandInquisitorItems.MAP,
            ZorkGrandInquisitorItems.TELEPORTER_DESTINATION_GUE_TECH,
        ),
    ),
    (ZorkGrandInquisitorRegions.TELEPORTER, ZorkGrandInquisitorRegions.HADES_SHORE): (
        (
            ZorkGrandInquisitorItems.MAP,
            ZorkGrandInquisitorItems.TELEPORTER_DESTINATION_HADES,
        ),
    ),
    (ZorkGrandInquisitorRegions.TELEPORTER, ZorkGrandInquisitorRegions.SPELL_LAB_BRIDGE): (
        (
            ZorkGrandInquisitorItems.MAP,
            ZorkGrandInquisitorItems.TELEPORTER_DESTINATION_SPELL_LAB,
        ),
    ),
    (ZorkGrandInquisitorRegions.TELEPORTER, ZorkGrandInquisitorRegions.SUBWAY_MONASTERY): (
        (
            ZorkGrandInquisitorItems.MAP,
            ZorkGrandInquisitorItems.TELEPORTER_DESTINATION_MONASTERY,
        ),
    ),
    (ZorkGrandInquisitorRegions.WALKING_CASTLE, ZorkGrandInquisitorRegions.DM_LAIR_INTERIOR): None,
    (ZorkGrandInquisitorRegions.WHITE_HOUSE, ZorkGrandInquisitorRegions.DM_LAIR_INTERIOR): None,
    (ZorkGrandInquisitorRegions.WHITE_HOUSE, ZorkGrandInquisitorRegions.WHITE_HOUSE_INTERIOR): (
        (
            ZorkGrandInquisitorItems.TOTEM_BROG,
            ZorkGrandInquisitorItems.BROGS_FLICKERING_TORCH,
        ),
    ),
    (ZorkGrandInquisitorRegions.WHITE_HOUSE_INTERIOR, ZorkGrandInquisitorRegions.WHITE_HOUSE): None,
}

endgame_entrance_data_by_goal: Dict[
    ZorkGrandInquisitorGoals,
    EntranceRuleData,
] = {
    ZorkGrandInquisitorGoals.THREE_ARTIFACTS: {
        (ZorkGrandInquisitorRegions.MENU, ZorkGrandInquisitorRegions.ENDGAME): (
            (
                ZorkGrandInquisitorItems.COCONUT_OF_QUENDOR,
                ZorkGrandInquisitorItems.CUBE_OF_FOUNDATION,
                ZorkGrandInquisitorItems.SKULL_OF_YORUK,
            ),
        )
    },
    ZorkGrandInquisitorGoals.ARTIFACT_OF_MAGIC_HUNT: {
        (ZorkGrandInquisitorRegions.WALKING_CASTLE, ZorkGrandInquisitorRegions.ENDGAME): (
            (
                [ZorkGrandInquisitorItems.ARTIFACT_OF_MAGIC, 999],  # Will get replaced with the actual number
            ),
        )
    },
    ZorkGrandInquisitorGoals.SPELL_HEIST: {
        (ZorkGrandInquisitorRegions.OUTSIDE_PORT_FOOZLE_SIGNPOST, ZorkGrandInquisitorRegions.ENDGAME): (
            (
                ZorkGrandInquisitorItems.SPELL_BEBURTT,
                ZorkGrandInquisitorItems.SPELL_GLORF,
                ZorkGrandInquisitorItems.SPELL_GOLGATEM,
                ZorkGrandInquisitorItems.SPELL_IGRAM,
                ZorkGrandInquisitorItems.SPELL_KENDALL,
                ZorkGrandInquisitorItems.SPELL_OBIDIL,
                ZorkGrandInquisitorItems.SPELL_NARWILE,
                ZorkGrandInquisitorItems.SPELL_REZROV,
                ZorkGrandInquisitorItems.SPELL_SNAVIG,
                ZorkGrandInquisitorItems.SPELL_THROCK,
                ZorkGrandInquisitorItems.SPELL_YASTARD,
            ),
        )
    },
    ZorkGrandInquisitorGoals.ZORK_TOUR: {
        (ZorkGrandInquisitorRegions.OUTSIDE_PORT_FOOZLE_SIGNPOST, ZorkGrandInquisitorRegions.ENDGAME): (
            (
                [ZorkGrandInquisitorItems.LANDMARK, 999],  # Will get replaced with the actual number
            ),
        ),
    },
    ZorkGrandInquisitorGoals.GRIM_JOURNEY: {
        (ZorkGrandInquisitorRegions.HADES_BEYOND_GATES, ZorkGrandInquisitorRegions.ENDGAME): (
            (
                [ZorkGrandInquisitorItems.DEATH, 999],  # Will get replaced with the actual number
            ),
        ),
    },
}

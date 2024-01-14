from typing import Dict, Tuple, Union

from ..enums import ZorkGrandInquisitorEvents, ZorkGrandInquisitorItems, ZorkGrandInquisitorRegions


entrance_rule_data: Dict[
    Tuple[
        ZorkGrandInquisitorRegions,
        ZorkGrandInquisitorRegions,
    ],
    Union[
        Tuple[
            Tuple[
                Union[
                    ZorkGrandInquisitorEvents,
                    ZorkGrandInquisitorItems,
                    ZorkGrandInquisitorRegions,
                ],
                ...,
            ],
            ...,
        ],
        None,
    ],
] = {
    (ZorkGrandInquisitorRegions.CROSSROADS, ZorkGrandInquisitorRegions.DM_LAIR): (
        (ZorkGrandInquisitorItems.SWORD,),
        (
            ZorkGrandInquisitorItems.MAP,
            ZorkGrandInquisitorItems.TELEPORTER_DESTINATION_DM_LAIR,
        ),
    ),
    (ZorkGrandInquisitorRegions.CROSSROADS, ZorkGrandInquisitorRegions.GUE_TECH): (
        (ZorkGrandInquisitorItems.SPELL_REZROV,),
        (
            ZorkGrandInquisitorItems.MAP,
            ZorkGrandInquisitorItems.TELEPORTER_DESTINATION_GUE_TECH,
        ),
    ),
    (ZorkGrandInquisitorRegions.CROSSROADS, ZorkGrandInquisitorRegions.HADES_SHORE): (
        (
            ZorkGrandInquisitorItems.MAP,
            ZorkGrandInquisitorItems.TELEPORTER_DESTINATION_HADES,
        ),
    ),
    (ZorkGrandInquisitorRegions.CROSSROADS, ZorkGrandInquisitorRegions.PORT_FOOZLE): None,
    (ZorkGrandInquisitorRegions.CROSSROADS, ZorkGrandInquisitorRegions.SPELL_LAB_BRIDGE): (
        (
            ZorkGrandInquisitorItems.MAP,
            ZorkGrandInquisitorItems.TELEPORTER_DESTINATION_SPELL_LAB,
        ),
    ),
    (ZorkGrandInquisitorRegions.CROSSROADS, ZorkGrandInquisitorRegions.SUBWAY_CROSSROADS): (
        (ZorkGrandInquisitorItems.SUBWAY_TOKEN,),
    ),
    (ZorkGrandInquisitorRegions.CROSSROADS, ZorkGrandInquisitorRegions.SUBWAY_MONASTERY): (
        (
            ZorkGrandInquisitorItems.MAP,
            ZorkGrandInquisitorItems.TELEPORTER_DESTINATION_MONASTERY,
        ),
    ),
    (ZorkGrandInquisitorRegions.DM_LAIR, ZorkGrandInquisitorRegions.CROSSROADS): None,
    (ZorkGrandInquisitorRegions.DM_LAIR, ZorkGrandInquisitorRegions.DM_LAIR_INTERIOR): (
        (
            ZorkGrandInquisitorEvents.DOOR_SMOKED_CIGAR,
            ZorkGrandInquisitorEvents.DOOR_DRANK_MEAD,
        ),
    ),
    (ZorkGrandInquisitorRegions.DM_LAIR, ZorkGrandInquisitorRegions.GUE_TECH): (
        (
            ZorkGrandInquisitorItems.MAP,
            ZorkGrandInquisitorItems.TELEPORTER_DESTINATION_GUE_TECH,
        ),
    ),
    (ZorkGrandInquisitorRegions.DM_LAIR, ZorkGrandInquisitorRegions.HADES_SHORE): (
        (
            ZorkGrandInquisitorItems.MAP,
            ZorkGrandInquisitorItems.TELEPORTER_DESTINATION_HADES,
        ),
    ),
    (ZorkGrandInquisitorRegions.DM_LAIR, ZorkGrandInquisitorRegions.SPELL_LAB_BRIDGE): (
        (
            ZorkGrandInquisitorItems.MAP,
            ZorkGrandInquisitorItems.TELEPORTER_DESTINATION_SPELL_LAB,
        ),
    ),
    (ZorkGrandInquisitorRegions.DM_LAIR, ZorkGrandInquisitorRegions.SUBWAY_MONASTERY): (
        (
            ZorkGrandInquisitorItems.MAP,
            ZorkGrandInquisitorItems.TELEPORTER_DESTINATION_MONASTERY,
        ),
    ),
    (ZorkGrandInquisitorRegions.DM_LAIR_INTERIOR, ZorkGrandInquisitorRegions.DM_LAIR): None,
    (ZorkGrandInquisitorRegions.DM_LAIR_INTERIOR, ZorkGrandInquisitorRegions.WALKING_CASTLE): (
        # (ZorkGrandInquisitorItems.SPELL_OBIDIL,),
    ),
    (ZorkGrandInquisitorRegions.DM_LAIR_INTERIOR, ZorkGrandInquisitorRegions.WHITE_HOUSE): (
        (
            ZorkGrandInquisitorItems.SPELL_NARWILE,
            ZorkGrandInquisitorItems.TOTEM_BROG,
            # ZorkGrandInquisitorItems.SPELL_YASTARD,
            # ZorkGrandInquisitorItems.REVEALED_BROGS_TIME_TUNNEL_ITEMS,
        ),
    ),
    (ZorkGrandInquisitorRegions.DRAGON_ARCHIPELAGO, ZorkGrandInquisitorRegions.ENDGAME): (
        (
            ZorkGrandInquisitorRegions.PORT_FOOZLE_PAST,
            ZorkGrandInquisitorRegions.WHITE_HOUSE,
        ),
    ),
    (ZorkGrandInquisitorRegions.DRAGON_ARCHIPELAGO, ZorkGrandInquisitorRegions.HADES_BEYOND_GATES): None,
    (ZorkGrandInquisitorRegions.GUE_TECH, ZorkGrandInquisitorRegions.CROSSROADS): None,
    (ZorkGrandInquisitorRegions.GUE_TECH, ZorkGrandInquisitorRegions.DM_LAIR): (
        (
            ZorkGrandInquisitorItems.MAP,
            ZorkGrandInquisitorItems.TELEPORTER_DESTINATION_DM_LAIR,
        ),
    ),
    (ZorkGrandInquisitorRegions.GUE_TECH, ZorkGrandInquisitorRegions.GUE_TECH_HALLWAY): (
        (ZorkGrandInquisitorItems.SPELL_IGRAM,),
    ),
    (ZorkGrandInquisitorRegions.GUE_TECH, ZorkGrandInquisitorRegions.HADES_SHORE): (
        (
            ZorkGrandInquisitorItems.MAP,
            ZorkGrandInquisitorItems.TELEPORTER_DESTINATION_HADES,
        ),
    ),
    (ZorkGrandInquisitorRegions.GUE_TECH, ZorkGrandInquisitorRegions.SPELL_LAB_BRIDGE): (
        (
            ZorkGrandInquisitorItems.MAP,
            ZorkGrandInquisitorItems.TELEPORTER_DESTINATION_SPELL_LAB,
        ),
    ),
    (ZorkGrandInquisitorRegions.GUE_TECH, ZorkGrandInquisitorRegions.SUBWAY_MONASTERY): (
        (
            ZorkGrandInquisitorItems.MAP,
            ZorkGrandInquisitorItems.TELEPORTER_DESTINATION_MONASTERY,
        ),
    ),
    (ZorkGrandInquisitorRegions.GUE_TECH_HALLWAY, ZorkGrandInquisitorRegions.GUE_TECH): None,
    (ZorkGrandInquisitorRegions.GUE_TECH_HALLWAY, ZorkGrandInquisitorRegions.SPELL_LAB_BRIDGE): (
        (ZorkGrandInquisitorItems.STUDENT_ID,),
    ),
    (ZorkGrandInquisitorRegions.HADES, ZorkGrandInquisitorRegions.HADES_BEYOND_GATES): (
        (
            ZorkGrandInquisitorEvents.KNOWS_SNAVIG,
            ZorkGrandInquisitorItems.TOTEM_BROG,
        ),
    ),
    (ZorkGrandInquisitorRegions.HADES, ZorkGrandInquisitorRegions.HADES_SHORE): (
        (ZorkGrandInquisitorItems.POUCH_OF_ZORKMIDS,),
    ),
    (ZorkGrandInquisitorRegions.HADES_BEYOND_GATES, ZorkGrandInquisitorRegions.DRAGON_ARCHIPELAGO): (
        (
            ZorkGrandInquisitorItems.SPELL_NARWILE,
            ZorkGrandInquisitorItems.TOTEM_GRIFF,
            # ZorkGrandInquisitorItems.SPELL_YASTARD,
            # ZorkGrandInquisitorItems.REVEALED_GRIFFS_TIME_TUNNEL_ITEMS,
        ),
    ),
    (ZorkGrandInquisitorRegions.HADES_BEYOND_GATES, ZorkGrandInquisitorRegions.HADES): None,
    (ZorkGrandInquisitorRegions.HADES_SHORE, ZorkGrandInquisitorRegions.CROSSROADS): (
        (ZorkGrandInquisitorItems.MAP,),
    ),
    (ZorkGrandInquisitorRegions.HADES_SHORE, ZorkGrandInquisitorRegions.DM_LAIR): (
        (
            ZorkGrandInquisitorItems.MAP,
            ZorkGrandInquisitorItems.TELEPORTER_DESTINATION_DM_LAIR,
        ),
    ),
    (ZorkGrandInquisitorRegions.HADES_SHORE, ZorkGrandInquisitorRegions.GUE_TECH): (
        (
            ZorkGrandInquisitorItems.MAP,
            ZorkGrandInquisitorItems.TELEPORTER_DESTINATION_GUE_TECH,
        ),
    ),
    (ZorkGrandInquisitorRegions.HADES_SHORE, ZorkGrandInquisitorRegions.HADES): (
        (ZorkGrandInquisitorItems.POUCH_OF_ZORKMIDS,),
    ),
    (ZorkGrandInquisitorRegions.HADES_SHORE, ZorkGrandInquisitorRegions.SPELL_LAB_BRIDGE): (
        (
            ZorkGrandInquisitorItems.MAP,
            ZorkGrandInquisitorItems.TELEPORTER_DESTINATION_SPELL_LAB,
        ),
    ),
    (ZorkGrandInquisitorRegions.HADES_SHORE, ZorkGrandInquisitorRegions.SUBWAY_CROSSROADS): None,
    (ZorkGrandInquisitorRegions.HADES_SHORE, ZorkGrandInquisitorRegions.SUBWAY_FLOOD_CONTROL_DAM): (
        (ZorkGrandInquisitorItems.SUBWAY_DESTINATION_FLOOD_CONTROL_DAM,),
    ),
    (ZorkGrandInquisitorRegions.HADES_SHORE, ZorkGrandInquisitorRegions.SUBWAY_MONASTERY): (
        (ZorkGrandInquisitorItems.SUBWAY_DESTINATION_MONASTERY,),
    ),
    (ZorkGrandInquisitorRegions.MENU, ZorkGrandInquisitorRegions.PORT_FOOZLE): None,
    (ZorkGrandInquisitorRegions.MONASTERY, ZorkGrandInquisitorRegions.HADES_SHORE): None,
    (ZorkGrandInquisitorRegions.MONASTERY, ZorkGrandInquisitorRegions.PORT_FOOZLE_PAST): (
        (
            ZorkGrandInquisitorItems.LARGE_TELEGRAPH_HAMMER,
            ZorkGrandInquisitorItems.SPELL_NARWILE,
            ZorkGrandInquisitorItems.TOTEM_LUCY,
            # ZorkGrandInquisitorItems.SPELL_YASTARD,
            # ZorkGrandInquisitorItems.REVEALED_LUCYS_TIME_TUNNEL_ITEMS,
        ),
    ),
    (ZorkGrandInquisitorRegions.MONASTERY, ZorkGrandInquisitorRegions.SUBWAY_MONASTERY): None,
    (ZorkGrandInquisitorRegions.PORT_FOOZLE, ZorkGrandInquisitorRegions.CROSSROADS): (
        (
            ZorkGrandInquisitorEvents.LANTERN_DALBOZ_ACCESSIBLE,
            ZorkGrandInquisitorItems.ROPE,
        ),
    ),
    (ZorkGrandInquisitorRegions.PORT_FOOZLE, ZorkGrandInquisitorRegions.PORT_FOOZLE_JACKS_SHOP): (
        (ZorkGrandInquisitorEvents.CIGAR_ACCESSIBLE,),
    ),
    (ZorkGrandInquisitorRegions.PORT_FOOZLE_JACKS_SHOP, ZorkGrandInquisitorRegions.PORT_FOOZLE): None,
    (ZorkGrandInquisitorRegions.PORT_FOOZLE_PAST, ZorkGrandInquisitorRegions.ENDGAME): (
        (
            ZorkGrandInquisitorRegions.DRAGON_ARCHIPELAGO,
            ZorkGrandInquisitorRegions.WHITE_HOUSE,
        ),
    ),
    (ZorkGrandInquisitorRegions.PORT_FOOZLE_PAST, ZorkGrandInquisitorRegions.MONASTERY): None,
    (ZorkGrandInquisitorRegions.SPELL_LAB, ZorkGrandInquisitorRegions.SPELL_LAB_BRIDGE): None,
    (ZorkGrandInquisitorRegions.SPELL_LAB_BRIDGE, ZorkGrandInquisitorRegions.CROSSROADS): (
        (ZorkGrandInquisitorItems.MAP,),
    ),
    (ZorkGrandInquisitorRegions.SPELL_LAB_BRIDGE, ZorkGrandInquisitorRegions.DM_LAIR): (
        (
            ZorkGrandInquisitorItems.MAP,
            ZorkGrandInquisitorItems.TELEPORTER_DESTINATION_DM_LAIR,
        ),
    ),
    (ZorkGrandInquisitorRegions.SPELL_LAB_BRIDGE, ZorkGrandInquisitorRegions.GUE_TECH): (
        (
            ZorkGrandInquisitorItems.MAP,
            ZorkGrandInquisitorItems.TELEPORTER_DESTINATION_GUE_TECH,
        ),
    ),
    (ZorkGrandInquisitorRegions.SPELL_LAB_BRIDGE, ZorkGrandInquisitorRegions.GUE_TECH_HALLWAY): None,
    (ZorkGrandInquisitorRegions.SPELL_LAB_BRIDGE, ZorkGrandInquisitorRegions.HADES_SHORE): (
        (
            ZorkGrandInquisitorItems.MAP,
            ZorkGrandInquisitorItems.TELEPORTER_DESTINATION_HADES,
        ),
    ),
    (ZorkGrandInquisitorRegions.SPELL_LAB_BRIDGE, ZorkGrandInquisitorRegions.SPELL_LAB): (
        (
            ZorkGrandInquisitorItems.SWORD,
            ZorkGrandInquisitorEvents.DAM_DESTROYED,
            ZorkGrandInquisitorItems.SPELL_GOLGATEM,
        ),
    ),
    (ZorkGrandInquisitorRegions.SPELL_LAB_BRIDGE, ZorkGrandInquisitorRegions.SUBWAY_MONASTERY): (
        (
            ZorkGrandInquisitorItems.MAP,
            ZorkGrandInquisitorItems.TELEPORTER_DESTINATION_MONASTERY,
        ),
    ),
    (ZorkGrandInquisitorRegions.SUBWAY_CROSSROADS, ZorkGrandInquisitorRegions.CROSSROADS): None,
    (ZorkGrandInquisitorRegions.SUBWAY_CROSSROADS, ZorkGrandInquisitorRegions.HADES_SHORE): (
        (
            ZorkGrandInquisitorItems.SPELL_KENDALL,
            ZorkGrandInquisitorItems.SUBWAY_DESTINATION_HADES,
        ),
    ),
    (ZorkGrandInquisitorRegions.SUBWAY_CROSSROADS, ZorkGrandInquisitorRegions.SUBWAY_FLOOD_CONTROL_DAM): (
        (
            ZorkGrandInquisitorItems.SPELL_KENDALL,
            ZorkGrandInquisitorItems.SUBWAY_DESTINATION_FLOOD_CONTROL_DAM,
        ),
    ),
    (ZorkGrandInquisitorRegions.SUBWAY_CROSSROADS, ZorkGrandInquisitorRegions.SUBWAY_MONASTERY): (
        (
            ZorkGrandInquisitorItems.SPELL_KENDALL,
            ZorkGrandInquisitorItems.SUBWAY_DESTINATION_MONASTERY,
        ),
    ),
    (ZorkGrandInquisitorRegions.SUBWAY_FLOOD_CONTROL_DAM, ZorkGrandInquisitorRegions.HADES_SHORE): (
        (ZorkGrandInquisitorItems.SUBWAY_DESTINATION_HADES,),
    ),
    (ZorkGrandInquisitorRegions.SUBWAY_FLOOD_CONTROL_DAM, ZorkGrandInquisitorRegions.SUBWAY_CROSSROADS): None,
    (ZorkGrandInquisitorRegions.SUBWAY_FLOOD_CONTROL_DAM, ZorkGrandInquisitorRegions.SUBWAY_MONASTERY): (
        (ZorkGrandInquisitorItems.SUBWAY_DESTINATION_MONASTERY,),
    ),
    (ZorkGrandInquisitorRegions.SUBWAY_MONASTERY, ZorkGrandInquisitorRegions.HADES_SHORE): (
        (ZorkGrandInquisitorItems.SUBWAY_DESTINATION_HADES,),
    ),
    (ZorkGrandInquisitorRegions.SUBWAY_MONASTERY, ZorkGrandInquisitorRegions.MONASTERY): (
        (
            ZorkGrandInquisitorItems.SWORD,
            ZorkGrandInquisitorEvents.ROPE_GLORFABLE,
        ),
    ),
    (ZorkGrandInquisitorRegions.SUBWAY_MONASTERY, ZorkGrandInquisitorRegions.SUBWAY_CROSSROADS): None,
    (ZorkGrandInquisitorRegions.SUBWAY_MONASTERY, ZorkGrandInquisitorRegions.SUBWAY_FLOOD_CONTROL_DAM): (
        (ZorkGrandInquisitorItems.SUBWAY_DESTINATION_FLOOD_CONTROL_DAM,),
    ),
    (ZorkGrandInquisitorRegions.WALKING_CASTLE, ZorkGrandInquisitorRegions.DM_LAIR_INTERIOR): None,
    (ZorkGrandInquisitorRegions.WHITE_HOUSE, ZorkGrandInquisitorRegions.DM_LAIR_INTERIOR): None,
    (ZorkGrandInquisitorRegions.WHITE_HOUSE, ZorkGrandInquisitorRegions.ENDGAME): (
        (
            ZorkGrandInquisitorRegions.DRAGON_ARCHIPELAGO,
            ZorkGrandInquisitorRegions.PORT_FOOZLE_PAST,
        ),
    ),
}

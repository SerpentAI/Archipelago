from typing import Tuple

from ..enums import ZorkGrandInquisitorRegions


dead_end_entrances: Tuple[
    Tuple[
        ZorkGrandInquisitorRegions,
        ZorkGrandInquisitorRegions,
    ]
] = (
    (
        ZorkGrandInquisitorRegions.HADES,
        ZorkGrandInquisitorRegions.HADES_BEYOND_GATES
    ),
    (
        ZorkGrandInquisitorRegions.MONASTERY,
        ZorkGrandInquisitorRegions.MONASTERY_EXHIBIT
    ),
    (
        ZorkGrandInquisitorRegions.OUTSIDE_PORT_FOOZLE_SIGNPOST,
        ZorkGrandInquisitorRegions.OUTSIDE_PORT_FOOZLE_INQUISITION_HQ
    ),
    (
        ZorkGrandInquisitorRegions.PORT_FOOZLE,
        ZorkGrandInquisitorRegions.PORT_FOOZLE_JACKS_SHOP
    ),
    (
        ZorkGrandInquisitorRegions.SPELL_LAB_BRIDGE,
        ZorkGrandInquisitorRegions.SPELL_LAB
    ),
    (
        ZorkGrandInquisitorRegions.DM_LAIR_INTERIOR,
        ZorkGrandInquisitorRegions.WALKING_CASTLE
    ),
)

dead_end_entrances_reverse: Tuple[
    Tuple[
        ZorkGrandInquisitorRegions,
        ZorkGrandInquisitorRegions,
    ]
] = (
    (
        ZorkGrandInquisitorRegions.HADES_BEYOND_GATES,
        ZorkGrandInquisitorRegions.HADES
    ),
    (
        ZorkGrandInquisitorRegions.MONASTERY_EXHIBIT,
        ZorkGrandInquisitorRegions.MONASTERY
    ),
    (
        ZorkGrandInquisitorRegions.OUTSIDE_PORT_FOOZLE_INQUISITION_HQ,
        ZorkGrandInquisitorRegions.OUTSIDE_PORT_FOOZLE_SIGNPOST
    ),
    (
        ZorkGrandInquisitorRegions.PORT_FOOZLE_JACKS_SHOP,
        ZorkGrandInquisitorRegions.PORT_FOOZLE
    ),
    (
        ZorkGrandInquisitorRegions.SPELL_LAB,
        ZorkGrandInquisitorRegions.SPELL_LAB_BRIDGE
    ),
    (
        ZorkGrandInquisitorRegions.WALKING_CASTLE,
        ZorkGrandInquisitorRegions.DM_LAIR_INTERIOR
    ),
)

one_way_entrances: Tuple[
    Tuple[
        ZorkGrandInquisitorRegions,
        ZorkGrandInquisitorRegions,
    ]
] = (
    (ZorkGrandInquisitorRegions.TELEPORTER, ZorkGrandInquisitorRegions.CROSSROADS),
    (ZorkGrandInquisitorRegions.TELEPORTER, ZorkGrandInquisitorRegions.DM_LAIR),
    (ZorkGrandInquisitorRegions.TELEPORTER, ZorkGrandInquisitorRegions.GUE_TECH_OUTSIDE),
    (ZorkGrandInquisitorRegions.TELEPORTER, ZorkGrandInquisitorRegions.HADES_SHORE),
    (ZorkGrandInquisitorRegions.TELEPORTER, ZorkGrandInquisitorRegions.SPELL_LAB_BRIDGE),
    (ZorkGrandInquisitorRegions.TELEPORTER, ZorkGrandInquisitorRegions.SUBWAY_MONASTERY),
)

randomizable_entrances: Tuple[
    Tuple[
        ZorkGrandInquisitorRegions,
        ZorkGrandInquisitorRegions,
    ]
] = (
    (ZorkGrandInquisitorRegions.BOTTOM_OF_THE_WELL, ZorkGrandInquisitorRegions.CROSSROADS),
    (ZorkGrandInquisitorRegions.BOTTOM_OF_THE_WELL, ZorkGrandInquisitorRegions.OUTSIDE_PORT_FOOZLE_WELL),
    (ZorkGrandInquisitorRegions.CROSSROADS, ZorkGrandInquisitorRegions.BOTTOM_OF_THE_WELL),
    (ZorkGrandInquisitorRegions.CROSSROADS, ZorkGrandInquisitorRegions.DM_LAIR),
    (ZorkGrandInquisitorRegions.CROSSROADS, ZorkGrandInquisitorRegions.GUE_TECH_ENTRANCE),
    (ZorkGrandInquisitorRegions.CROSSROADS, ZorkGrandInquisitorRegions.SUBWAY_CROSSROADS),
    (ZorkGrandInquisitorRegions.DM_LAIR, ZorkGrandInquisitorRegions.CROSSROADS),
    (ZorkGrandInquisitorRegions.DM_LAIR, ZorkGrandInquisitorRegions.DM_LAIR_INTERIOR),
    (ZorkGrandInquisitorRegions.DM_LAIR_INTERIOR, ZorkGrandInquisitorRegions.DM_LAIR),
    (ZorkGrandInquisitorRegions.GUE_TECH, ZorkGrandInquisitorRegions.GUE_TECH_ENTRANCE),
    (ZorkGrandInquisitorRegions.GUE_TECH, ZorkGrandInquisitorRegions.GUE_TECH_OUTSIDE),
    (ZorkGrandInquisitorRegions.GUE_TECH_ENTRANCE, ZorkGrandInquisitorRegions.CROSSROADS),
    (ZorkGrandInquisitorRegions.GUE_TECH_ENTRANCE, ZorkGrandInquisitorRegions.GUE_TECH),
    (ZorkGrandInquisitorRegions.GUE_TECH_HALLWAY, ZorkGrandInquisitorRegions.SPELL_LAB_BRIDGE),
    (ZorkGrandInquisitorRegions.GUE_TECH_OUTSIDE, ZorkGrandInquisitorRegions.GUE_TECH),
    (ZorkGrandInquisitorRegions.HADES, ZorkGrandInquisitorRegions.HADES_SHORE),
    (ZorkGrandInquisitorRegions.HADES_SHORE, ZorkGrandInquisitorRegions.HADES),
    (ZorkGrandInquisitorRegions.HADES_SHORE, ZorkGrandInquisitorRegions.SUBWAY_HADES),
    (ZorkGrandInquisitorRegions.MONASTERY, ZorkGrandInquisitorRegions.SUBWAY_MONASTERY),
    (ZorkGrandInquisitorRegions.OUTSIDE_PORT_FOOZLE_SIGNPOST, ZorkGrandInquisitorRegions.OUTSIDE_PORT_FOOZLE_WELL),
    (ZorkGrandInquisitorRegions.OUTSIDE_PORT_FOOZLE_SIGNPOST, ZorkGrandInquisitorRegions.PORT_FOOZLE),
    (ZorkGrandInquisitorRegions.OUTSIDE_PORT_FOOZLE_WELL, ZorkGrandInquisitorRegions.BOTTOM_OF_THE_WELL),
    (ZorkGrandInquisitorRegions.OUTSIDE_PORT_FOOZLE_WELL, ZorkGrandInquisitorRegions.OUTSIDE_PORT_FOOZLE_SIGNPOST),
    (ZorkGrandInquisitorRegions.PORT_FOOZLE, ZorkGrandInquisitorRegions.OUTSIDE_PORT_FOOZLE_SIGNPOST),
    (ZorkGrandInquisitorRegions.SPELL_LAB_BRIDGE, ZorkGrandInquisitorRegions.GUE_TECH_HALLWAY),
    (ZorkGrandInquisitorRegions.SUBWAY_CROSSROADS, ZorkGrandInquisitorRegions.CROSSROADS),
    (ZorkGrandInquisitorRegions.SUBWAY_CROSSROADS, ZorkGrandInquisitorRegions.SUBWAY_FLOOD_CONTROL_DAM),
    (ZorkGrandInquisitorRegions.SUBWAY_CROSSROADS, ZorkGrandInquisitorRegions.SUBWAY_HADES),
    (ZorkGrandInquisitorRegions.SUBWAY_CROSSROADS, ZorkGrandInquisitorRegions.SUBWAY_MONASTERY),
    (ZorkGrandInquisitorRegions.SUBWAY_FLOOD_CONTROL_DAM, ZorkGrandInquisitorRegions.SUBWAY_CROSSROADS),
    (ZorkGrandInquisitorRegions.SUBWAY_FLOOD_CONTROL_DAM, ZorkGrandInquisitorRegions.SUBWAY_HADES),
    (ZorkGrandInquisitorRegions.SUBWAY_FLOOD_CONTROL_DAM, ZorkGrandInquisitorRegions.SUBWAY_MONASTERY),
    (ZorkGrandInquisitorRegions.SUBWAY_HADES, ZorkGrandInquisitorRegions.HADES_SHORE),
    (ZorkGrandInquisitorRegions.SUBWAY_HADES, ZorkGrandInquisitorRegions.SUBWAY_CROSSROADS),
    (ZorkGrandInquisitorRegions.SUBWAY_HADES, ZorkGrandInquisitorRegions.SUBWAY_FLOOD_CONTROL_DAM),
    (ZorkGrandInquisitorRegions.SUBWAY_HADES, ZorkGrandInquisitorRegions.SUBWAY_MONASTERY),
    (ZorkGrandInquisitorRegions.SUBWAY_MONASTERY, ZorkGrandInquisitorRegions.MONASTERY),
    (ZorkGrandInquisitorRegions.SUBWAY_MONASTERY, ZorkGrandInquisitorRegions.SUBWAY_CROSSROADS),
    (ZorkGrandInquisitorRegions.SUBWAY_MONASTERY, ZorkGrandInquisitorRegions.SUBWAY_FLOOD_CONTROL_DAM),
    (ZorkGrandInquisitorRegions.SUBWAY_MONASTERY, ZorkGrandInquisitorRegions.SUBWAY_HADES),
)

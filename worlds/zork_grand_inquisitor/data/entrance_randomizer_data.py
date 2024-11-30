from typing import Dict, Tuple

from ..enums import ZorkGrandInquisitorRegions


dead_end_regions: Tuple[ZorkGrandInquisitorRegions, ...] = (
    ZorkGrandInquisitorRegions.HADES_BEYOND_GATES,
    ZorkGrandInquisitorRegions.MONASTERY_EXHIBIT,
    ZorkGrandInquisitorRegions.OUTSIDE_PORT_FOOZLE_INQUISITION_HQ,
    ZorkGrandInquisitorRegions.PORT_FOOZLE_JACKS_SHOP,
    ZorkGrandInquisitorRegions.SPELL_LAB,
    ZorkGrandInquisitorRegions.WALKING_CASTLE,
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

randomizable_entrances: Dict[
    Tuple[
        ZorkGrandInquisitorRegions,
        ZorkGrandInquisitorRegions,
    ],
    ZorkGrandInquisitorRegions,
] = {
    (
        ZorkGrandInquisitorRegions.BOTTOM_OF_THE_WELL,
        ZorkGrandInquisitorRegions.CROSSROADS,
    ): ZorkGrandInquisitorRegions.CROSSROADS,
    (
        ZorkGrandInquisitorRegions.BOTTOM_OF_THE_WELL,
        ZorkGrandInquisitorRegions.OUTSIDE_PORT_FOOZLE_WELL,
    ): ZorkGrandInquisitorRegions.OUTSIDE_PORT_FOOZLE_WELL,
    (
        ZorkGrandInquisitorRegions.CROSSROADS,
        ZorkGrandInquisitorRegions.BOTTOM_OF_THE_WELL,
    ): ZorkGrandInquisitorRegions.BOTTOM_OF_THE_WELL,
    (
        ZorkGrandInquisitorRegions.CROSSROADS,
        ZorkGrandInquisitorRegions.DM_LAIR,
    ): ZorkGrandInquisitorRegions.DM_LAIR,
    (
        ZorkGrandInquisitorRegions.CROSSROADS,
        ZorkGrandInquisitorRegions.GUE_TECH_ENTRANCE,
    ): ZorkGrandInquisitorRegions.GUE_TECH_ENTRANCE,
    (
        ZorkGrandInquisitorRegions.CROSSROADS,
        ZorkGrandInquisitorRegions.SUBWAY_CROSSROADS,
    ): ZorkGrandInquisitorRegions.SUBWAY_CROSSROADS,
    (
        ZorkGrandInquisitorRegions.DM_LAIR,
        ZorkGrandInquisitorRegions.CROSSROADS,
    ): ZorkGrandInquisitorRegions.CROSSROADS,
    (
        ZorkGrandInquisitorRegions.DM_LAIR,
        ZorkGrandInquisitorRegions.DM_LAIR_INTERIOR,
    ): ZorkGrandInquisitorRegions.DM_LAIR_INTERIOR,
    (
        ZorkGrandInquisitorRegions.DM_LAIR_INTERIOR,
        ZorkGrandInquisitorRegions.DM_LAIR,
    ): ZorkGrandInquisitorRegions.DM_LAIR,
    (
        ZorkGrandInquisitorRegions.DM_LAIR_INTERIOR,
        ZorkGrandInquisitorRegions.WALKING_CASTLE,
    ): ZorkGrandInquisitorRegions.WALKING_CASTLE,
    (
        ZorkGrandInquisitorRegions.GUE_TECH,
        ZorkGrandInquisitorRegions.GUE_TECH_ENTRANCE,
    ): ZorkGrandInquisitorRegions.GUE_TECH_ENTRANCE,
    (
        ZorkGrandInquisitorRegions.GUE_TECH,
        ZorkGrandInquisitorRegions.GUE_TECH_OUTSIDE,
    ): ZorkGrandInquisitorRegions.GUE_TECH_OUTSIDE,
    (
        ZorkGrandInquisitorRegions.GUE_TECH_ENTRANCE,
        ZorkGrandInquisitorRegions.CROSSROADS,
    ): ZorkGrandInquisitorRegions.CROSSROADS,
    (
        ZorkGrandInquisitorRegions.GUE_TECH_ENTRANCE,
        ZorkGrandInquisitorRegions.GUE_TECH,
    ): ZorkGrandInquisitorRegions.GUE_TECH,
    (
        ZorkGrandInquisitorRegions.GUE_TECH_HALLWAY,
        ZorkGrandInquisitorRegions.SPELL_LAB_BRIDGE,
    ): ZorkGrandInquisitorRegions.SPELL_LAB_BRIDGE,
    (
        ZorkGrandInquisitorRegions.GUE_TECH_OUTSIDE,
        ZorkGrandInquisitorRegions.GUE_TECH,
    ): ZorkGrandInquisitorRegions.GUE_TECH,
    (
        ZorkGrandInquisitorRegions.HADES,
        ZorkGrandInquisitorRegions.HADES_BEYOND_GATES,
    ): ZorkGrandInquisitorRegions.HADES_BEYOND_GATES,
    (
        ZorkGrandInquisitorRegions.HADES,
        ZorkGrandInquisitorRegions.HADES_SHORE,
    ): ZorkGrandInquisitorRegions.HADES_SHORE,
    (
        ZorkGrandInquisitorRegions.HADES_BEYOND_GATES,
        ZorkGrandInquisitorRegions.HADES,
    ): ZorkGrandInquisitorRegions.HADES,
    (
        ZorkGrandInquisitorRegions.HADES_SHORE,
        ZorkGrandInquisitorRegions.HADES,
    ): ZorkGrandInquisitorRegions.HADES,
    (
        ZorkGrandInquisitorRegions.HADES_SHORE,
        ZorkGrandInquisitorRegions.SUBWAY_HADES,
    ): ZorkGrandInquisitorRegions.SUBWAY_HADES,
    (
        ZorkGrandInquisitorRegions.MONASTERY,
        ZorkGrandInquisitorRegions.MONASTERY_EXHIBIT,
    ): ZorkGrandInquisitorRegions.MONASTERY_EXHIBIT,
    (
        ZorkGrandInquisitorRegions.MONASTERY,
        ZorkGrandInquisitorRegions.SUBWAY_MONASTERY,
    ): ZorkGrandInquisitorRegions.SUBWAY_MONASTERY,
    (
        ZorkGrandInquisitorRegions.MONASTERY_EXHIBIT,
        ZorkGrandInquisitorRegions.MONASTERY,
    ): ZorkGrandInquisitorRegions.MONASTERY,
    (
        ZorkGrandInquisitorRegions.OUTSIDE_PORT_FOOZLE_INQUISITION_HQ,
        ZorkGrandInquisitorRegions.OUTSIDE_PORT_FOOZLE_SIGNPOST,
    ): ZorkGrandInquisitorRegions.OUTSIDE_PORT_FOOZLE_SIGNPOST,
    (
        ZorkGrandInquisitorRegions.OUTSIDE_PORT_FOOZLE_SIGNPOST,
        ZorkGrandInquisitorRegions.OUTSIDE_PORT_FOOZLE_INQUISITION_HQ,
    ): ZorkGrandInquisitorRegions.OUTSIDE_PORT_FOOZLE_INQUISITION_HQ,
    (
        ZorkGrandInquisitorRegions.OUTSIDE_PORT_FOOZLE_SIGNPOST,
        ZorkGrandInquisitorRegions.OUTSIDE_PORT_FOOZLE_WELL,
    ): ZorkGrandInquisitorRegions.OUTSIDE_PORT_FOOZLE_WELL,
    (
        ZorkGrandInquisitorRegions.OUTSIDE_PORT_FOOZLE_SIGNPOST,
        ZorkGrandInquisitorRegions.PORT_FOOZLE,
    ): ZorkGrandInquisitorRegions.PORT_FOOZLE,
    (
        ZorkGrandInquisitorRegions.OUTSIDE_PORT_FOOZLE_WELL,
        ZorkGrandInquisitorRegions.BOTTOM_OF_THE_WELL,
    ): ZorkGrandInquisitorRegions.BOTTOM_OF_THE_WELL,
    (
        ZorkGrandInquisitorRegions.OUTSIDE_PORT_FOOZLE_WELL,
        ZorkGrandInquisitorRegions.OUTSIDE_PORT_FOOZLE_SIGNPOST,
    ): ZorkGrandInquisitorRegions.OUTSIDE_PORT_FOOZLE_SIGNPOST,
    (
        ZorkGrandInquisitorRegions.PORT_FOOZLE,
        ZorkGrandInquisitorRegions.OUTSIDE_PORT_FOOZLE_SIGNPOST,
    ): ZorkGrandInquisitorRegions.OUTSIDE_PORT_FOOZLE_SIGNPOST,
    (
        ZorkGrandInquisitorRegions.PORT_FOOZLE,
        ZorkGrandInquisitorRegions.PORT_FOOZLE_JACKS_SHOP,
    ): ZorkGrandInquisitorRegions.PORT_FOOZLE_JACKS_SHOP,
    (
        ZorkGrandInquisitorRegions.PORT_FOOZLE_JACKS_SHOP,
        ZorkGrandInquisitorRegions.PORT_FOOZLE,
    ): ZorkGrandInquisitorRegions.PORT_FOOZLE,
    (
        ZorkGrandInquisitorRegions.SPELL_LAB,
        ZorkGrandInquisitorRegions.SPELL_LAB_BRIDGE,
    ): ZorkGrandInquisitorRegions.SPELL_LAB_BRIDGE,
    (
        ZorkGrandInquisitorRegions.SPELL_LAB_BRIDGE,
        ZorkGrandInquisitorRegions.GUE_TECH_HALLWAY,
    ): ZorkGrandInquisitorRegions.GUE_TECH_HALLWAY,
    (
        ZorkGrandInquisitorRegions.SPELL_LAB_BRIDGE,
        ZorkGrandInquisitorRegions.SPELL_LAB,
    ): ZorkGrandInquisitorRegions.SPELL_LAB,
    (
        ZorkGrandInquisitorRegions.SUBWAY_CROSSROADS,
        ZorkGrandInquisitorRegions.CROSSROADS,
    ): ZorkGrandInquisitorRegions.CROSSROADS,
    (
        ZorkGrandInquisitorRegions.SUBWAY_CROSSROADS,
        ZorkGrandInquisitorRegions.SUBWAY_FLOOD_CONTROL_DAM,
    ): ZorkGrandInquisitorRegions.SUBWAY_FLOOD_CONTROL_DAM,
    (
        ZorkGrandInquisitorRegions.SUBWAY_CROSSROADS,
        ZorkGrandInquisitorRegions.SUBWAY_HADES,
    ): ZorkGrandInquisitorRegions.SUBWAY_HADES,
    (
        ZorkGrandInquisitorRegions.SUBWAY_CROSSROADS,
        ZorkGrandInquisitorRegions.SUBWAY_MONASTERY,
    ): ZorkGrandInquisitorRegions.SUBWAY_MONASTERY,
    (
        ZorkGrandInquisitorRegions.SUBWAY_FLOOD_CONTROL_DAM,
        ZorkGrandInquisitorRegions.SUBWAY_CROSSROADS,
    ): ZorkGrandInquisitorRegions.SUBWAY_CROSSROADS,
    (
        ZorkGrandInquisitorRegions.SUBWAY_FLOOD_CONTROL_DAM,
        ZorkGrandInquisitorRegions.SUBWAY_HADES,
    ): ZorkGrandInquisitorRegions.SUBWAY_HADES,
    (
        ZorkGrandInquisitorRegions.SUBWAY_FLOOD_CONTROL_DAM,
        ZorkGrandInquisitorRegions.SUBWAY_MONASTERY,
    ): ZorkGrandInquisitorRegions.SUBWAY_MONASTERY,
    (
        ZorkGrandInquisitorRegions.SUBWAY_HADES,
        ZorkGrandInquisitorRegions.HADES_SHORE,
    ): ZorkGrandInquisitorRegions.HADES_SHORE,
    (
        ZorkGrandInquisitorRegions.SUBWAY_HADES,
        ZorkGrandInquisitorRegions.SUBWAY_CROSSROADS,
    ): ZorkGrandInquisitorRegions.SUBWAY_CROSSROADS,
    (
        ZorkGrandInquisitorRegions.SUBWAY_HADES,
        ZorkGrandInquisitorRegions.SUBWAY_FLOOD_CONTROL_DAM,
    ): ZorkGrandInquisitorRegions.SUBWAY_FLOOD_CONTROL_DAM,
    (
        ZorkGrandInquisitorRegions.SUBWAY_HADES,
        ZorkGrandInquisitorRegions.SUBWAY_MONASTERY,
    ): ZorkGrandInquisitorRegions.SUBWAY_MONASTERY,
    (
        ZorkGrandInquisitorRegions.SUBWAY_MONASTERY,
        ZorkGrandInquisitorRegions.MONASTERY,
    ): ZorkGrandInquisitorRegions.MONASTERY,
    (
        ZorkGrandInquisitorRegions.SUBWAY_MONASTERY,
        ZorkGrandInquisitorRegions.SUBWAY_CROSSROADS,
    ): ZorkGrandInquisitorRegions.SUBWAY_CROSSROADS,
    (
        ZorkGrandInquisitorRegions.SUBWAY_MONASTERY,
        ZorkGrandInquisitorRegions.SUBWAY_FLOOD_CONTROL_DAM,
    ): ZorkGrandInquisitorRegions.SUBWAY_FLOOD_CONTROL_DAM,
    (
        ZorkGrandInquisitorRegions.SUBWAY_MONASTERY,
        ZorkGrandInquisitorRegions.SUBWAY_HADES,
    ): ZorkGrandInquisitorRegions.SUBWAY_HADES,
    (
        ZorkGrandInquisitorRegions.TELEPORTER,
        ZorkGrandInquisitorRegions.CROSSROADS,
    ): ZorkGrandInquisitorRegions.CROSSROADS,
    (
        ZorkGrandInquisitorRegions.TELEPORTER,
        ZorkGrandInquisitorRegions.DM_LAIR,
    ): ZorkGrandInquisitorRegions.DM_LAIR,
    (
        ZorkGrandInquisitorRegions.TELEPORTER,
        ZorkGrandInquisitorRegions.GUE_TECH_OUTSIDE,
    ): ZorkGrandInquisitorRegions.GUE_TECH_OUTSIDE,
    (
        ZorkGrandInquisitorRegions.TELEPORTER,
        ZorkGrandInquisitorRegions.HADES_SHORE,
    ): ZorkGrandInquisitorRegions.HADES_SHORE,
    (
        ZorkGrandInquisitorRegions.TELEPORTER,
        ZorkGrandInquisitorRegions.SPELL_LAB_BRIDGE,
    ): ZorkGrandInquisitorRegions.SPELL_LAB_BRIDGE,
    (
        ZorkGrandInquisitorRegions.TELEPORTER,
        ZorkGrandInquisitorRegions.SUBWAY_MONASTERY,
    ): ZorkGrandInquisitorRegions.SUBWAY_MONASTERY,
    (
        ZorkGrandInquisitorRegions.WALKING_CASTLE,
        ZorkGrandInquisitorRegions.DM_LAIR_INTERIOR,
    ): ZorkGrandInquisitorRegions.DM_LAIR_INTERIOR,
}

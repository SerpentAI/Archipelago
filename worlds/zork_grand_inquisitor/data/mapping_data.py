from typing import Dict

from ..enums import (
    ZorkGrandInquisitorItems,
    ZorkGrandInquisitorRegions,
    ZorkGrandInquisitorStartingLocations,
)


starting_location_to_logic_helper_item: Dict[
    ZorkGrandInquisitorStartingLocations, ZorkGrandInquisitorItems
] = {
    ZorkGrandInquisitorStartingLocations.PORT_FOOZLE: (
        ZorkGrandInquisitorItems.LOGIC_HELPER_STARTING_LOCATION_PORT_FOOZLE
    ),
    ZorkGrandInquisitorStartingLocations.CROSSROADS: (
        ZorkGrandInquisitorItems.LOGIC_HELPER_STARTING_LOCATION_CROSSROADS
    ),
    ZorkGrandInquisitorStartingLocations.DM_LAIR: (
        ZorkGrandInquisitorItems.LOGIC_HELPER_STARTING_LOCATION_DM_LAIR
    ),
    ZorkGrandInquisitorStartingLocations.DM_LAIR_HOUSE: (
        ZorkGrandInquisitorItems.LOGIC_HELPER_STARTING_LOCATION_DM_LAIR_HOUSE
    ),
    ZorkGrandInquisitorStartingLocations.GUE_TECH: (
        ZorkGrandInquisitorItems.LOGIC_HELPER_STARTING_LOCATION_GUE_TECH
    ),
    ZorkGrandInquisitorStartingLocations.SPELL_LAB: (
        ZorkGrandInquisitorItems.LOGIC_HELPER_STARTING_LOCATION_SPELL_LAB
    ),
    ZorkGrandInquisitorStartingLocations.HADES_SHORE: (
        ZorkGrandInquisitorItems.LOGIC_HELPER_STARTING_LOCATION_HADES_SHORE
    ),
    ZorkGrandInquisitorStartingLocations.FLOOD_CONTROL_DAM_3: (
        ZorkGrandInquisitorItems.LOGIC_HELPER_STARTING_LOCATION_FLOOD_CONTROL_DAM_3
    ),
    ZorkGrandInquisitorStartingLocations.MONASTERY_TOTEMIZER: (
        ZorkGrandInquisitorItems.LOGIC_HELPER_STARTING_LOCATION_MONASTERY_TOTEMIZER
    ),
    ZorkGrandInquisitorStartingLocations.MONASTERY_EXHIBIT: (
        ZorkGrandInquisitorItems.LOGIC_HELPER_STARTING_LOCATION_MONASTERY_EXHIBIT
    ),
}

# TODO: Align Starting Locations with Regions
starting_location_to_region: Dict[
    ZorkGrandInquisitorStartingLocations, ZorkGrandInquisitorRegions
] = {
    ZorkGrandInquisitorStartingLocations.PORT_FOOZLE: ZorkGrandInquisitorRegions.PORT_FOOZLE,
    ZorkGrandInquisitorStartingLocations.CROSSROADS: ZorkGrandInquisitorRegions.CROSSROADS,
    ZorkGrandInquisitorStartingLocations.DM_LAIR: ZorkGrandInquisitorRegions.DM_LAIR,
    ZorkGrandInquisitorStartingLocations.DM_LAIR_HOUSE: ZorkGrandInquisitorRegions.DM_LAIR_INTERIOR,
    ZorkGrandInquisitorStartingLocations.GUE_TECH: ZorkGrandInquisitorRegions.GUE_TECH,
    ZorkGrandInquisitorStartingLocations.SPELL_LAB: ZorkGrandInquisitorRegions.SPELL_LAB,
    ZorkGrandInquisitorStartingLocations.HADES_SHORE: ZorkGrandInquisitorRegions.HADES_SHORE,
    ZorkGrandInquisitorStartingLocations.FLOOD_CONTROL_DAM_3: ZorkGrandInquisitorRegions.SUBWAY_FLOOD_CONTROL_DAM,
    ZorkGrandInquisitorStartingLocations.MONASTERY_TOTEMIZER: ZorkGrandInquisitorRegions.MONASTERY,
    ZorkGrandInquisitorStartingLocations.MONASTERY_EXHIBIT: ZorkGrandInquisitorRegions.MONASTERY_EXHIBIT,
}

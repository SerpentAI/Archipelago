from typing import Dict

from ..enums import ZorkGrandInquisitorItems, ZorkGrandInquisitorStartingLocations


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

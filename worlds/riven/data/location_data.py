from typing import Dict, NamedTuple, Optional, Tuple

from ..enums import (
    RivenAPTags,
    RivenLocations,
    RivenRegions,
)


class RivenLocationData(NamedTuple):
    archipelago_id: Optional[int]
    region: str
    tags: Optional[Tuple[RivenAPTags, ...]] = None


location_offset: int = 10000

location_data: Dict[RivenLocations, RivenLocationData] = {
    RivenLocations.TEMPLE_PLATEAU_READ_ATRUS_JOURNAL: RivenLocationData(
        archipelago_id=location_offset + 1,
        region=RivenRegions.TEMPLE_PLATEAU,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.TEMPLE_LOCATION,
        ),
    ),
    RivenLocations.TEMPLE_PLATEAU_GAZE_STAR_FISSURE: RivenLocationData(
        archipelago_id=location_offset + 2,
        region=RivenRegions.TEMPLE_PLATEAU,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.TEMPLE_LOCATION,
        ),
    ),
    RivenLocations.TEMPLE_PLATEAU_BREAK_TELESCOPE_LEVER: RivenLocationData(
        archipelago_id=location_offset + 3,
        region=RivenRegions.TEMPLE_PLATEAU,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.TEMPLE_LOCATION,
        ),
    ),
    RivenLocations.TEMPLE_PLATEAU_FIND_CHO: RivenLocationData(
        archipelago_id=location_offset + 4,
        region=RivenRegions.TEMPLE_PLATEAU,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.TEMPLE_LOCATION,
        ),
    ),
    RivenLocations.TEMPLE_PLATEAU_REMOVE_HINGE: RivenLocationData(
        archipelago_id=location_offset + 5,
        region=RivenRegions.TEMPLE_PLATEAU,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.TEMPLE_LOCATION,
        ),
    ),
    RivenLocations.TEMPLE_GATE_ROOM_BEETLE_1: RivenLocationData(
        archipelago_id=location_offset + 6,
        region=RivenRegions.TEMPLE_GATE_ROOM,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.TEMPLE_LOCATION,
        ),
    ),
    RivenLocations.TEMPLE_GATE_ROOM_BEETLE_2: RivenLocationData(
        archipelago_id=location_offset + 7,
        region=RivenRegions.TEMPLE_GATE_ROOM,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.TEMPLE_LOCATION,
        ),
    ),
    RivenLocations.TEMPLE_GATE_ROOM_BEETLE_3: RivenLocationData(
        archipelago_id=location_offset + 8,
        region=RivenRegions.TEMPLE_GATE_ROOM,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.TEMPLE_LOCATION,
        ),
    ),
    RivenLocations.TEMPLE_GATE_ROOM_BEETLE_4: RivenLocationData(
        archipelago_id=location_offset + 9,
        region=RivenRegions.TEMPLE_GATE_ROOM,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.TEMPLE_LOCATION,
        ),
    ),
    RivenLocations.TEMPLE_GATE_ROOM_BEETLE_5: RivenLocationData(
        archipelago_id=location_offset + 10,
        region=RivenRegions.TEMPLE_GATE_ROOM,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.TEMPLE_LOCATION,
        ),
    ),
    RivenLocations.TEMPLE_STEAM_CONTROL_ROOM_POWER_TELESCOPE: RivenLocationData(
        archipelago_id=location_offset + 11,
        region=RivenRegions.TEMPLE_STEAM_CONTROL_ROOM,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.TEMPLE_LOCATION,
        ),
    ),
    RivenLocations.TEMPLE_SPINNING_DOME_OPEN_DOME: RivenLocationData(
        archipelago_id=location_offset + 12,
        region=RivenRegions.TEMPLE_SPINNING_DOME,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.TEMPLE_LOCATION,
        ),
    ),
    RivenLocations.TEMPLE_GOLDEN_DOME_ENTER_DOME: RivenLocationData(
        archipelago_id=location_offset + 13,
        region=RivenRegions.TEMPLE_GOLDEN_DOME,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.TEMPLE_LOCATION,
        ),
    ),
    RivenLocations.TEMPLE_GOLDEN_DOME_TEMPLE_SYMBOL: RivenLocationData(
        archipelago_id=location_offset + 14,
        region=RivenRegions.TEMPLE_GOLDEN_DOME,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.TEMPLE_LOCATION,
        ),
    ),
    RivenLocations.TEMPLE_GOLDEN_DOME_JUNGLE_SYMBOL: RivenLocationData(
        archipelago_id=location_offset + 15,
        region=RivenRegions.TEMPLE_GOLDEN_DOME,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.TEMPLE_LOCATION,
        ),
    ),
    RivenLocations.TEMPLE_GOLDEN_DOME_BOILER_SYMBOL: RivenLocationData(
        archipelago_id=location_offset + 16,
        region=RivenRegions.TEMPLE_GOLDEN_DOME,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.TEMPLE_LOCATION,
        ),
    ),
    RivenLocations.TEMPLE_GOLDEN_DOME_SURVEY_SYMBOL: RivenLocationData(
        archipelago_id=location_offset + 17,
        region=RivenRegions.TEMPLE_GOLDEN_DOME,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.TEMPLE_LOCATION,
        ),
    ),
    RivenLocations.TEMPLE_GOLDEN_DOME_PRISON_SYMBOL: RivenLocationData(
        archipelago_id=location_offset + 18,
        region=RivenRegions.TEMPLE_GOLDEN_DOME,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.TEMPLE_LOCATION,
        ),
    ),
    RivenLocations.TEMPLE_PROJECTION_ROOM_ENTER_PROJECTION_ROOM: RivenLocationData(
        archipelago_id=location_offset + 19,
        region=RivenRegions.TEMPLE_PROJECTION_ROOM,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.TEMPLE_LOCATION,
        ),
    ),
    RivenLocations.TEMPLE_PROJECTION_ROOM_SPIDER_CHAIR: RivenLocationData(
        archipelago_id=location_offset + 20,
        region=RivenRegions.TEMPLE_PROJECTION_ROOM,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.TEMPLE_LOCATION,
        ),
    ),
    RivenLocations.TEMPLE_GOLDEN_DOME_COLLAPSE_BRIDGE: RivenLocationData(
        archipelago_id=location_offset + 21,
        region=RivenRegions.TEMPLE_GOLDEN_DOME,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.TEMPLE_LOCATION,
        ),
    ),
    RivenLocations.TEMPLE_GOLDEN_DOME_UPPER_ACCESS_UPPER: RivenLocationData(
        archipelago_id=location_offset + 22,
        region=RivenRegions.TEMPLE_GOLDEN_DOME_UPPER,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.TEMPLE_LOCATION,
        ),
    ),
    RivenLocations.TEMPLE_GOLDEN_DOME_UPPER_PLACE_PURPLE_MARBLE: RivenLocationData(
        archipelago_id=location_offset + 23,
        region=RivenRegions.TEMPLE_GOLDEN_DOME_UPPER,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.TEMPLE_LOCATION,
        ),
    ),
    RivenLocations.TEMPLE_GOLDEN_DOME_UPPER_PLACE_GREEN_MARBLE: RivenLocationData(
        archipelago_id=location_offset + 24,
        region=RivenRegions.TEMPLE_GOLDEN_DOME_UPPER,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.TEMPLE_LOCATION,
        ),
    ),
    RivenLocations.TEMPLE_GOLDEN_DOME_UPPER_PLACE_BLUE_MARBLE: RivenLocationData(
        archipelago_id=location_offset + 25,
        region=RivenRegions.TEMPLE_GOLDEN_DOME_UPPER,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.TEMPLE_LOCATION,
        ),
    ),
    RivenLocations.TEMPLE_GOLDEN_DOME_UPPER_PLACE_RED_MARBLE: RivenLocationData(
        archipelago_id=location_offset + 26,
        region=RivenRegions.TEMPLE_GOLDEN_DOME_UPPER,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.TEMPLE_LOCATION,
        ),
    ),
    RivenLocations.TEMPLE_GOLDEN_DOME_UPPER_PLACE_ORANGE_MARBLE: RivenLocationData(
        archipelago_id=location_offset + 27,
        region=RivenRegions.TEMPLE_GOLDEN_DOME_UPPER,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.TEMPLE_LOCATION,
        ),
    ),
    RivenLocations.TEMPLE_GOLDEN_DOME_UPPER_ACCESS_AGE_233_BOOK: RivenLocationData(
        archipelago_id=location_offset + 28,
        region=RivenRegions.TEMPLE_GOLDEN_DOME_UPPER,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.TEMPLE_LOCATION,
        ),
    ),
    RivenLocations.TEMPLE_MAGLEV_PLATFORM_TO_JUNGLE_PRESS_BUTTON: RivenLocationData(
        archipelago_id=location_offset + 29,
        region=RivenRegions.TEMPLE_MAGLEV_PLATFORM_TO_JUNGLE,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.TEMPLE_LOCATION,
        ),
    ),
    RivenLocations.JUNGLE_VISIT_VISIT_JUNGLE: RivenLocationData(
        archipelago_id=location_offset + 30,
        region=RivenRegions.JUNGLE_VISIT,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.JUNGLE_LOCATION,
        ),
    ),
    RivenLocations.JUNGLE_MAGLEV_PLATFORM_TO_TEMPLE_PRESS_BUTTON: RivenLocationData(
        archipelago_id=location_offset + 31,
        region=RivenRegions.JUNGLE_MAGLEV_PLATFORM_TO_TEMPLE,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.JUNGLE_LOCATION,
        ),
    ),
    RivenLocations.JUNGLE_WAHRK_TOTEM_INTERACT: RivenLocationData(
        archipelago_id=location_offset + 32,
        region=RivenRegions.JUNGLE_WAHRK_TOTEM,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.JUNGLE_LOCATION,
        ),
    ),
    RivenLocations.JUNGLE_WAHRK_TOTEM_DIVERT_WATER: RivenLocationData(
        archipelago_id=location_offset + 33,
        region=RivenRegions.JUNGLE_WAHRK_TOTEM,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.JUNGLE_LOCATION,
        ),
    ),
    RivenLocations.JUNGLE_BEACH_COLLECT_MOIETY_LENS: RivenLocationData(
        archipelago_id=location_offset + 34,
        region=RivenRegions.JUNGLE_BEACH,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.JUNGLE_LOCATION,
        ),
    ),
    RivenLocations.JUNGLE_BEETLE_TOTEM_INTERACT: RivenLocationData(
        archipelago_id=location_offset + 35,
        region=RivenRegions.JUNGLE_BEETLE_TOTEM,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.JUNGLE_LOCATION,
        ),
    ),
    RivenLocations.JUNGLE_OUTSIDE_VILLAGE_SCHOOL_SIDE_GRAB_BBQ: RivenLocationData(
        archipelago_id=location_offset + 36,
        region=RivenRegions.JUNGLE_OUTSIDE_VILLAGE_SCHOOL_SIDE,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.JUNGLE_LOCATION,
        ),
    ),
    RivenLocations.JUNGLE_SCHOOLHOUSE_ENTER_SCHOOLHOUSE: RivenLocationData(
        archipelago_id=location_offset + 37,
        region=RivenRegions.JUNGLE_SCHOOLHOUSE,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.JUNGLE_LOCATION,
        ),
    ),
    RivenLocations.JUNGLE_SCHOOLHOUSE_INSPECT_WAHRK_GAME: RivenLocationData(
        archipelago_id=location_offset + 38,
        region=RivenRegions.JUNGLE_SCHOOLHOUSE,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.JUNGLE_LOCATION,
        ),
    ),
    RivenLocations.JUNGLE_VILLAGE_KNOCK_ON_DOOR: RivenLocationData(
        archipelago_id=location_offset + 39,
        region=RivenRegions.JUNGLE_VILLAGE,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.JUNGLE_LOCATION,
        ),
    ),
    RivenLocations.JUNGLE_VILLAGE_INHALE_STEAM: RivenLocationData(
        archipelago_id=location_offset + 40,
        region=RivenRegions.JUNGLE_VILLAGE,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.JUNGLE_LOCATION,
        ),
    ),
    RivenLocations.JUNGLE_VILLAGE_SHUT_STEAM_VENT: RivenLocationData(
        archipelago_id=location_offset + 41,
        region=RivenRegions.JUNGLE_VILLAGE,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.JUNGLE_LOCATION,
        ),
    ),
    RivenLocations.JUNGLE_VILLAGE_PROVIDE_WATER_TO_TREE: RivenLocationData(
        archipelago_id=location_offset + 42,
        region=RivenRegions.JUNGLE_VILLAGE,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.JUNGLE_LOCATION,
        ),
    ),
    RivenLocations.JUNGLE_BLUE_CAVE_OPEN_SECRET_DOOR: RivenLocationData(
        archipelago_id=location_offset + 43,
        region=RivenRegions.JUNGLE_BLUE_CAVE,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.JUNGLE_LOCATION,
        ),
    ),
    RivenLocations.JUNGLE_LOGGING_AREA_GET_SPOTTED_BY_GUARD: RivenLocationData(
        archipelago_id=location_offset + 44,
        region=RivenRegions.JUNGLE_LOGGING_AREA,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.JUNGLE_LOCATION,
        ),
    ),
    RivenLocations.JUNGLE_YTRAM_TOTEM_INTERACT: RivenLocationData(
        archipelago_id=location_offset + 45,
        region=RivenRegions.JUNGLE_YTRAM_TOTEM,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.JUNGLE_LOCATION,
        ),
    ),
    RivenLocations.JUNGLE_WOODCART_PLATFORM_PRESS_BUTTON: RivenLocationData(
        archipelago_id=location_offset + 46,
        region=RivenRegions.JUNGLE_WOODCART_PLATFORM,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.JUNGLE_LOCATION,
        ),
    ),
    RivenLocations.JUNGLE_WAHRK_ELEVATOR_OPEN_WAHRKS_MOUTH: RivenLocationData(
        archipelago_id=location_offset + 47,
        region=RivenRegions.JUNGLE_WAHRK_ELEVATOR,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.JUNGLE_LOCATION,
        ),
    ),
    RivenLocations.JUNGLE_JUNGLE_CATWALKS_OPEN_DOME: RivenLocationData(
        archipelago_id=location_offset + 48,
        region=RivenRegions.JUNGLE_JUNGLE_CATWALKS,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.JUNGLE_LOCATION,
        ),
    ),
    RivenLocations.JUNGLE_BONE_THRONE_LOOK_DOWN_UPON_VILLAGE: RivenLocationData(
        archipelago_id=location_offset + 49,
        region=RivenRegions.JUNGLE_BONE_THRONE,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.JUNGLE_LOCATION,
        ),
    ),
    RivenLocations.JUNGLE_BONE_THRONE_SEAL_WAHRK_GALLOWS: RivenLocationData(
        archipelago_id=location_offset + 50,
        region=RivenRegions.JUNGLE_BONE_THRONE,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.JUNGLE_LOCATION,
        ),
    ),
    RivenLocations.JUNGLE_MAGLEV_PLATFORM_TO_SURVEY_PRESS_BUTTON: RivenLocationData(
        archipelago_id=location_offset + 51,
        region=RivenRegions.JUNGLE_MAGLEV_PLATFORM_TO_SURVEY,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.JUNGLE_LOCATION,
        ),
    ),
    RivenLocations.JUNGLE_MAGLEV_PLATFORM_TO_SURVEY_PRESS_OTHER_BUTTON: RivenLocationData(
        archipelago_id=location_offset + 52,
        region=RivenRegions.JUNGLE_MAGLEV_PLATFORM_TO_SURVEY,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.JUNGLE_LOCATION,
        ),
    ),
    RivenLocations.JUNGLE_SUBMARINE_CAVE_PRESS_BUTTON: RivenLocationData(
        archipelago_id=location_offset + 53,
        region=RivenRegions.JUNGLE_SUBMARINE_CAVE,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.JUNGLE_LOCATION,
        ),
    ),
    RivenLocations.JUNGLE_SUBMARINE_DESTINATION_SUBMARINE_CAVE_BOARD_SUBMARINE: RivenLocationData(
        archipelago_id=location_offset + 54,
        region=RivenRegions.JUNGLE_SUBMARINE_DESTINATION_SUBMARINE_CAVE,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.JUNGLE_LOCATION,
        ),
    ),
    RivenLocations.JUNGLE_SUBMARINE_DESTINATION_VILLAGE_PILOT: RivenLocationData(
        archipelago_id=location_offset + 55,
        region=RivenRegions.JUNGLE_SUBMARINE_DESTINATION_VILLAGE,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.JUNGLE_LOCATION,
        ),
    ),
    RivenLocations.JUNGLE_VILLAGE_WATER_HOLE_FLICK_SWITCH: RivenLocationData(
        archipelago_id=location_offset + 56,
        region=RivenRegions.JUNGLE_VILLAGE_WATER_HOLE,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.JUNGLE_LOCATION,
        ),
    ),
    RivenLocations.JUNGLE_INSECT_TOTEM_INTERACT: RivenLocationData(
        archipelago_id=location_offset + 57,
        region=RivenRegions.JUNGLE_INSECT_TOTEM,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.JUNGLE_LOCATION,
        ),
    ),
    RivenLocations.JUNGLE_SUBMARINE_DESTINATION_PODIUM_PILOT: RivenLocationData(
        archipelago_id=location_offset + 58,
        region=RivenRegions.JUNGLE_SUBMARINE_DESTINATION_PODIUM,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.JUNGLE_LOCATION,
        ),
    ),
    RivenLocations.JUNGLE_SUBMARINE_DESTINATION_SCHOOLHOUSE_PILOT: RivenLocationData(
        archipelago_id=location_offset + 59,
        region=RivenRegions.JUNGLE_SUBMARINE_DESTINATION_SCHOOLHOUSE,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.JUNGLE_LOCATION,
        ),
    ),
    RivenLocations.JUNGLE_SUBMARINE_DESTINATION_WAHRK_GALLOWS_PILOT: RivenLocationData(
        archipelago_id=location_offset + 60,
        region=RivenRegions.JUNGLE_SUBMARINE_DESTINATION_WAHRK_GALLOWS,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.JUNGLE_LOCATION,
        ),
    ),
    RivenLocations.JUNGLE_WAHRK_GALLOWS_JAIL_CELL_OPEN_SECRET_DOOR: RivenLocationData(
        archipelago_id=location_offset + 61,
        region=RivenRegions.JUNGLE_WAHRK_GALLOWS_JAIL_CELL,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.JUNGLE_LOCATION,
        ),
    ),
    RivenLocations.JUNGLE_SECRET_MOIETY_TUNNEL_TURN_ON_LIGHT_1: RivenLocationData(
        archipelago_id=location_offset + 62,
        region=RivenRegions.JUNGLE_SECRET_MOIETY_TUNNEL,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.JUNGLE_LOCATION,
        ),
    ),
    RivenLocations.JUNGLE_SECRET_MOIETY_TUNNEL_TURN_ON_LIGHT_2: RivenLocationData(
        archipelago_id=location_offset + 63,
        region=RivenRegions.JUNGLE_SECRET_MOIETY_TUNNEL,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.JUNGLE_LOCATION,
        ),
    ),
    RivenLocations.JUNGLE_SECRET_MOIETY_TUNNEL_TURN_ON_LIGHT_3: RivenLocationData(
        archipelago_id=location_offset + 64,
        region=RivenRegions.JUNGLE_SECRET_MOIETY_TUNNEL,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.JUNGLE_LOCATION,
        ),
    ),
    RivenLocations.JUNGLE_SECRET_MOIETY_TUNNEL_TURN_ON_LIGHT_4: RivenLocationData(
        archipelago_id=location_offset + 65,
        region=RivenRegions.JUNGLE_SECRET_MOIETY_TUNNEL,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.JUNGLE_LOCATION,
        ),
    ),
    RivenLocations.JUNGLE_SECRET_MOIETY_TUNNEL_TURN_ON_LIGHT_5: RivenLocationData(
        archipelago_id=location_offset + 66,
        region=RivenRegions.JUNGLE_SECRET_MOIETY_TUNNEL,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.JUNGLE_LOCATION,
        ),
    ),
    RivenLocations.JUNGLE_SECRET_MOIETY_TUNNEL_TURN_ON_LIGHT_6: RivenLocationData(
        archipelago_id=location_offset + 67,
        region=RivenRegions.JUNGLE_SECRET_MOIETY_TUNNEL,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.JUNGLE_LOCATION,
        ),
    ),
    RivenLocations.JUNGLE_SECRET_MOIETY_TUNNEL_TURN_ON_LIGHT_7: RivenLocationData(
        archipelago_id=location_offset + 68,
        region=RivenRegions.JUNGLE_SECRET_MOIETY_TUNNEL,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.JUNGLE_LOCATION,
        ),
    ),
    RivenLocations.JUNGLE_SECRET_MOIETY_TUNNEL_TURN_ON_LIGHT_8: RivenLocationData(
        archipelago_id=location_offset + 69,
        region=RivenRegions.JUNGLE_SECRET_MOIETY_TUNNEL,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.JUNGLE_LOCATION,
        ),
    ),
    RivenLocations.JUNGLE_SECRET_MOIETY_TUNNEL_OPEN_SECRET_DOOR: RivenLocationData(
        archipelago_id=location_offset + 70,
        region=RivenRegions.JUNGLE_SECRET_MOIETY_TUNNEL,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.JUNGLE_LOCATION,
        ),
    ),
    RivenLocations.JUNGLE_ANIMAL_CIRCLE_ROOM_ACCESS_TAY_BOOK: RivenLocationData(
        archipelago_id=location_offset + 71,
        region=RivenRegions.JUNGLE_ANIMAL_CIRCLE_ROOM,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.JUNGLE_LOCATION,
        ),
    ),
    RivenLocations.JUNGLE_ANIMAL_CIRCLE_ROOM_INPUT_CLASSIC_SOLUTION: RivenLocationData(
        archipelago_id=location_offset + 72,
        region=RivenRegions.JUNGLE_ANIMAL_CIRCLE_ROOM,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.JUNGLE_LOCATION,
        ),
    ),
    RivenLocations.BOILER_VISIT_VISIT_BOILER: RivenLocationData(
        archipelago_id=location_offset + 73,
        region=RivenRegions.BOILER_VISIT,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.BOILER_LOCATION,
        ),
    ),
    RivenLocations.BOILER_WOODCART_PLATFORM_PRESS_BUTTON: RivenLocationData(
        archipelago_id=location_offset + 74,
        region=RivenRegions.BOILER_WOODCART_PLATFORM,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.BOILER_LOCATION,
        ),
    ),
    RivenLocations.BOILER_WOODCART_PLATFORM_TURN_ON_WOOD_CHIPPER: RivenLocationData(
        archipelago_id=location_offset + 75,
        region=RivenRegions.BOILER_WOODCART_PLATFORM,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.BOILER_LOCATION,
        ),
    ),
    RivenLocations.BOILER_LAKE_DIRECT_STEAM_WOOD_CHIPPER: RivenLocationData(
        archipelago_id=location_offset + 76,
        region=RivenRegions.BOILER_LAKE,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.BOILER_LOCATION,
        ),
    ),
    RivenLocations.BOILER_LAKE_DIRECT_STEAM_BOILER: RivenLocationData(
        archipelago_id=location_offset + 77,
        region=RivenRegions.BOILER_LAKE,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.BOILER_LOCATION,
        ),
    ),
    RivenLocations.BOILER_LAKE_DISCOVER_BURNT_BOOK: RivenLocationData(
        archipelago_id=location_offset + 78,
        region=RivenRegions.BOILER_LAKE,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.BOILER_LOCATION,
        ),
    ),
    RivenLocations.BOILER_BOILER_CONTROLS_RAISE_FLOOR: RivenLocationData(
        archipelago_id=location_offset + 79,
        region=RivenRegions.BOILER_BOILER_CONTROLS,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.BOILER_LOCATION,
        ),
    ),
    RivenLocations.BOILER_BOILER_CONTROLS_DRAIN_WATER: RivenLocationData(
        archipelago_id=location_offset + 80,
        region=RivenRegions.BOILER_BOILER_CONTROLS,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.BOILER_LOCATION,
        ),
    ),
    RivenLocations.BOILER_BOILER_CONTROLS_TURN_OFF_HEAT: RivenLocationData(
        archipelago_id=location_offset + 81,
        region=RivenRegions.BOILER_BOILER_CONTROLS,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.BOILER_LOCATION,
        ),
    ),
    RivenLocations.BOILER_INSIDE_BOILER_ENTER_BOILER: RivenLocationData(
        archipelago_id=location_offset + 82,
        region=RivenRegions.BOILER_INSIDE_BOILER,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.BOILER_LOCATION,
        ),
    ),
    RivenLocations.BOILER_BALCONY_OPEN_HATCH: RivenLocationData(
        archipelago_id=location_offset + 83,
        region=RivenRegions.BOILER_BALCONY,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.BOILER_LOCATION,
        ),
    ),
    RivenLocations.BOILER_SPINNING_DOME_OPEN_DOME: RivenLocationData(
        archipelago_id=location_offset + 84,
        region=RivenRegions.BOILER_SPINNING_DOME,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.BOILER_LOCATION,
        ),
    ),
    RivenLocations.BOILER_MINING_CAVE_PUMP_SIDE_DRAIN_WATER: RivenLocationData(
        archipelago_id=location_offset + 85,
        region=RivenRegions.BOILER_MINING_CAVE_PUMP_SIDE,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.BOILER_LOCATION,
        ),
    ),
    RivenLocations.BOILER_MINING_CAVE_PUMP_SIDE_MINE_FIRE_MARBLE_GEODE: RivenLocationData(
        archipelago_id=location_offset + 86,
        region=RivenRegions.BOILER_MINING_CAVE_PUMP_SIDE,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.BOILER_LOCATION,
        ),
    ),
    RivenLocations.BOILER_MINING_CAVE_ELEVATOR_SIDE_SLOT_CART_IN_ELEVATOR: RivenLocationData(
        archipelago_id=location_offset + 87,
        region=RivenRegions.BOILER_MINING_CAVE_ELEVATOR_SIDE,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.BOILER_LOCATION,
        ),
    ),
    RivenLocations.BOILER_LAB_VISIT_GEHNS_LAB: RivenLocationData(
        archipelago_id=location_offset + 88,
        region=RivenRegions.BOILER_LAB,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.BOILER_LOCATION,
        ),
    ),
    RivenLocations.BOILER_LAB_READ_GEHNS_JOURNAL: RivenLocationData(
        archipelago_id=location_offset + 89,
        region=RivenRegions.BOILER_LAB,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.BOILER_LOCATION,
        ),
    ),
    RivenLocations.BOILER_LAB_TRY_OUT_MAGNIFYING_GLASS: RivenLocationData(
        archipelago_id=location_offset + 90,
        region=RivenRegions.BOILER_LAB,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.BOILER_LOCATION,
        ),
    ),
    RivenLocations.BOILER_LAB_CLOSE_PRESS: RivenLocationData(
        archipelago_id=location_offset + 91,
        region=RivenRegions.BOILER_LAB,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.BOILER_LOCATION,
        ),
    ),
    RivenLocations.BOILER_LAB_CRACK_OPEN_FIRE_MARBLE_GEODE: RivenLocationData(
        archipelago_id=location_offset + 92,
        region=RivenRegions.BOILER_LAB,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.BOILER_LOCATION,
        ),
    ),
    RivenLocations.BOILER_LAB_MEASURE_OPTIMAL_MARBLE_STRIKE_FORCE: RivenLocationData(
        archipelago_id=location_offset + 93,
        region=RivenRegions.BOILER_LAB,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.BOILER_LOCATION,
        ),
    ),
    RivenLocations.BOILER_LAB_FREE_YTRAM: RivenLocationData(
        archipelago_id=location_offset + 94,
        region=RivenRegions.BOILER_LAB,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.BOILER_LOCATION,
        ),
    ),
    RivenLocations.BOILER_LAB_SPEED_UP_FLYWHEEL: RivenLocationData(
        archipelago_id=location_offset + 95,
        region=RivenRegions.BOILER_LAB,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.BOILER_LOCATION,
        ),
    ),
    RivenLocations.BOILER_LAB_STOP_POLISHER: RivenLocationData(
        archipelago_id=location_offset + 96,
        region=RivenRegions.BOILER_LAB,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.BOILER_LOCATION,
        ),
    ),
    RivenLocations.BOILER_MAGLEV_PLATFORM_TO_SURVEY_PRESS_BUTTON: RivenLocationData(
        archipelago_id=location_offset + 97,
        region=RivenRegions.BOILER_MAGLEV_PLATFORM_TO_SURVEY,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.BOILER_LOCATION,
        ),
    ),
    RivenLocations.SURVEY_VISIT_VISIT_SURVEY: RivenLocationData(
        archipelago_id=location_offset + 98,
        region=RivenRegions.SURVEY_VISIT,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.SURVEY_LOCATION,
        ),
    ),
    RivenLocations.SURVEY_MAGLEV_PLATFORM_TO_BOILER_PRESS_BUTTON: RivenLocationData(
        archipelago_id=location_offset + 99,
        region=RivenRegions.SURVEY_MAGLEV_PLATFORM_TO_BOILER,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.SURVEY_LOCATION,
        ),
    ),
    RivenLocations.SURVEY_MAGLEV_PLATFORM_TO_BOILER_PRESS_OTHER_BUTTON: RivenLocationData(
        archipelago_id=location_offset + 100,
        region=RivenRegions.SURVEY_MAGLEV_PLATFORM_TO_BOILER,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.BOILER_LOCATION,
        ),
    ),
    RivenLocations.SURVEY_GEHNS_SPY_ROOM_DISCOVER_GEHNS_SPY_ROOM: RivenLocationData(
        archipelago_id=location_offset + 101,
        region=RivenRegions.SURVEY_GEHNS_SPY_ROOM,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.SURVEY_LOCATION,
        ),
    ),
    RivenLocations.SURVEY_GEHNS_SPY_ROOM_VIEW_PRISON_CAMERA: RivenLocationData(
        archipelago_id=location_offset + 102,
        region=RivenRegions.SURVEY_GEHNS_SPY_ROOM,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.SURVEY_LOCATION,
        ),
    ),
    RivenLocations.SURVEY_GEHNS_SPY_ROOM_VIEW_JUNGLE_CAMERA: RivenLocationData(
        archipelago_id=location_offset + 103,
        region=RivenRegions.SURVEY_GEHNS_SPY_ROOM,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.SURVEY_LOCATION,
        ),
    ),
    RivenLocations.SURVEY_GEHNS_SPY_ROOM_VIEW_SURVEY_CAMERA: RivenLocationData(
        archipelago_id=location_offset + 104,
        region=RivenRegions.SURVEY_GEHNS_SPY_ROOM,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.SURVEY_LOCATION,
        ),
    ),
    RivenLocations.SURVEY_GEHNS_SPY_ROOM_VIEW_BOILER_CAMERA: RivenLocationData(
        archipelago_id=location_offset + 105,
        region=RivenRegions.SURVEY_GEHNS_SPY_ROOM,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.SURVEY_LOCATION,
        ),
    ),
    RivenLocations.SURVEY_GEHNS_SPY_ROOM_VIEW_TEMPLE_CAMERA: RivenLocationData(
        archipelago_id=location_offset + 106,
        region=RivenRegions.SURVEY_GEHNS_SPY_ROOM,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.SURVEY_LOCATION,
        ),
    ),
    RivenLocations.SURVEY_GEHNS_SPY_ROOM_TURN_ON_BLUE_LIGHT: RivenLocationData(
        archipelago_id=location_offset + 107,
        region=RivenRegions.SURVEY_GEHNS_SPY_ROOM,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.SURVEY_LOCATION,
        ),
    ),
    RivenLocations.SURVEY_GEHNS_SPY_ROOM_TURN_ON_GREEN_LIGHT: RivenLocationData(
        archipelago_id=location_offset + 108,
        region=RivenRegions.SURVEY_GEHNS_SPY_ROOM,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.SURVEY_LOCATION,
        ),
    ),
    RivenLocations.SURVEY_GEHNS_SPY_ROOM_TURN_ON_YELLOW_LIGHT: RivenLocationData(
        archipelago_id=location_offset + 109,
        region=RivenRegions.SURVEY_GEHNS_SPY_ROOM,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.SURVEY_LOCATION,
        ),
    ),
    RivenLocations.SURVEY_GEHNS_SPY_ROOM_TURN_ON_ORANGE_LIGHT: RivenLocationData(
        archipelago_id=location_offset + 110,
        region=RivenRegions.SURVEY_GEHNS_SPY_ROOM,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.SURVEY_LOCATION,
        ),
    ),
    RivenLocations.SURVEY_GEHNS_SPY_ROOM_TURN_ON_RED_LIGHT: RivenLocationData(
        archipelago_id=location_offset + 111,
        region=RivenRegions.SURVEY_GEHNS_SPY_ROOM,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.SURVEY_LOCATION,
        ),
    ),
    RivenLocations.SURVEY_GEHNS_SPY_ROOM_ANNOY_WAHRK: RivenLocationData(
        archipelago_id=location_offset + 112,
        region=RivenRegions.SURVEY_GEHNS_SPY_ROOM,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.SURVEY_LOCATION,
        ),
    ),
    RivenLocations.SURVEY_UPPER_PLATEAU_OPEN_DOME: RivenLocationData(
        archipelago_id=location_offset + 113,
        region=RivenRegions.SURVEY_UPPER_PLATEAU,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.SURVEY_LOCATION,
        ),
    ),
    RivenLocations.SURVEY_UPPER_PLATEAU_PRESS_GEHNTRIS_TEMPLE_BUTTON: RivenLocationData(
        archipelago_id=location_offset + 114,
        region=RivenRegions.SURVEY_UPPER_PLATEAU,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.SURVEY_LOCATION,
        ),
    ),
    RivenLocations.SURVEY_UPPER_PLATEAU_PRESS_GEHNTRIS_JUNGLE_BUTTON: RivenLocationData(
        archipelago_id=location_offset + 115,
        region=RivenRegions.SURVEY_UPPER_PLATEAU,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.SURVEY_LOCATION,
        ),
    ),
    RivenLocations.SURVEY_UPPER_PLATEAU_PRESS_GEHNTRIS_BOILER_BUTTON: RivenLocationData(
        archipelago_id=location_offset + 116,
        region=RivenRegions.SURVEY_UPPER_PLATEAU,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.SURVEY_LOCATION,
        ),
    ),
    RivenLocations.SURVEY_UPPER_PLATEAU_PRESS_GEHNTRIS_SURVEY_BUTTON: RivenLocationData(
        archipelago_id=location_offset + 117,
        region=RivenRegions.SURVEY_UPPER_PLATEAU,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.SURVEY_LOCATION,
        ),
    ),
    RivenLocations.SURVEY_UPPER_PLATEAU_PRESS_GEHNTRIS_PRISON_BUTTON: RivenLocationData(
        archipelago_id=location_offset + 118,
        region=RivenRegions.SURVEY_UPPER_PLATEAU,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.SURVEY_LOCATION,
        ),
    ),
    RivenLocations.SURVEY_UNDERGROUND_TUNNEL_ENCOUNTER_GEHNS_SCRIBE: RivenLocationData(
        archipelago_id=location_offset + 119,
        region=RivenRegions.SURVEY_UNDERGROUND_TUNNEL,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.SURVEY_LOCATION,
        ),
    ),
    RivenLocations.SURVEY_MAGLEV_PLATFORM_TO_JUNGLE_PRESS_BUTTON: RivenLocationData(
        archipelago_id=location_offset + 120,
        region=RivenRegions.SURVEY_MAGLEV_PLATFORM_TO_JUNGLE,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.SURVEY_LOCATION,
        ),
    ),
    RivenLocations.PRISON_VISIT_VISIT_PRISON: RivenLocationData(
        archipelago_id=location_offset + 121,
        region=RivenRegions.PRISON_VISIT,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.PRISON_LOCATION,
        ),
    ),
    RivenLocations.PRISON_SPINNING_DOME_OPEN_DOME: RivenLocationData(
        archipelago_id=location_offset + 122,
        region=RivenRegions.PRISON_SPINNING_DOME,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.PRISON_LOCATION,
        ),
    ),
    RivenLocations.PRISON_BEACH_INTERACT_TOTEM: RivenLocationData(
        archipelago_id=location_offset + 123,
        region=RivenRegions.PRISON_BEACH,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.PRISON_LOCATION,
        ),
    ),
    RivenLocations.PRISON_BEACH_ROTATE_LOG_TELESCOPE: RivenLocationData(
        archipelago_id=location_offset + 124,
        region=RivenRegions.PRISON_BEACH,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.PRISON_LOCATION,
        ),
    ),
    RivenLocations.PRISON_BEACH_LOOK_THROUGH_LOG_TELESCOPE: RivenLocationData(
        archipelago_id=location_offset + 125,
        region=RivenRegions.PRISON_BEACH,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.PRISON_LOCATION,
        ),
    ),
    RivenLocations.PRISON_OUTSIDE_JAIL_CELL_MEET_CATHERINE: RivenLocationData(
        archipelago_id=location_offset + 126,
        region=RivenRegions.PRISON_OUTSIDE_JAIL_CELL,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.PRISON_LOCATION,
        ),
    ),
    RivenLocations.PRISON_JAIL_CELL_FREE_CATHERINE: RivenLocationData(
        archipelago_id=location_offset + 127,
        region=RivenRegions.PRISON_JAIL_CELL,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.PRISON_LOCATION,
        ),
    ),
    RivenLocations.AGE_OF_TAY_GET_IMPRISONED: RivenLocationData(
        archipelago_id=location_offset + 128,
        region=RivenRegions.AGE_OF_TAY,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.AGE_OF_TAY_LOCATION,
        ),
    ),
    RivenLocations.AGE_OF_TAY_GET_PRISON_BOOK_BACK: RivenLocationData(
        archipelago_id=location_offset + 129,
        region=RivenRegions.AGE_OF_TAY,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.AGE_OF_TAY_LOCATION,
        ),
    ),
    RivenLocations.AGE_OF_TAY_READ_CATHERINES_JOURNAL: RivenLocationData(
        archipelago_id=location_offset + 130,
        region=RivenRegions.AGE_OF_TAY,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.AGE_OF_TAY_LOCATION,
        ),
    ),
    RivenLocations.AGE_OF_TAY_EXPLORE_HIVE: RivenLocationData(
        archipelago_id=location_offset + 131,
        region=RivenRegions.AGE_OF_TAY,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.AGE_OF_TAY_LOCATION,
        ),
    ),
    RivenLocations.AGE_233_MEET_GEHN: RivenLocationData(
        archipelago_id=location_offset + 132,
        region=RivenRegions.AGE_233,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.AGE_233_LOCATION,
        ),
    ),
    RivenLocations.AGE_233_TRAP_GEHN: RivenLocationData(
        archipelago_id=location_offset + 133,
        region=RivenRegions.AGE_233,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.AGE_233_LOCATION,
        ),
    ),
    RivenLocations.AGE_233_TURN_ON_STOVE: RivenLocationData(
        archipelago_id=location_offset + 134,
        region=RivenRegions.AGE_233,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.AGE_233_LOCATION,
        ),
    ),
    RivenLocations.AGE_233_LOWER_CAGE: RivenLocationData(
        archipelago_id=location_offset + 135,
        region=RivenRegions.AGE_233,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.AGE_233_LOCATION,
        ),
    ),
    RivenLocations.AGE_233_GRAB_BBQ: RivenLocationData(
        archipelago_id=location_offset + 136,
        region=RivenRegions.AGE_233,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.AGE_233_LOCATION,
        ),
    ),
    # Disabled - Shares "BP_EngageWindow_C_1" instance name with JUNGLE_OUTSIDE_VILLAGE_SCHOOL_SIDE_GRAB_BBQ
    # RivenLocations.AGE_233_SIT_ON_THRONE: RivenLocationData(
    #     archipelago_id=location_offset + 137,
    #     region=RivenRegions.AGE_233,
    #     tags=(
    #         RivenAPTags.CORE_LOCATION,
    #         RivenAPTags.AGE_233_LOCATION,
    #     ),
    # ),
    RivenLocations.AGE_233_TURN_ON_FAUCET: RivenLocationData(
        archipelago_id=location_offset + 138,
        region=RivenRegions.AGE_233,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.AGE_233_LOCATION,
        ),
    ),
    RivenLocations.AGE_233_WATCH_KETAS_PROJECTION: RivenLocationData(
        archipelago_id=location_offset + 139,
        region=RivenRegions.AGE_233,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.AGE_233_LOCATION,
        ),
    ),
    RivenLocations.AGE_233_READ_GEHNS_JOURNAL: RivenLocationData(
        archipelago_id=location_offset + 140,
        region=RivenRegions.AGE_233,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.AGE_233_LOCATION,
        ),
    ),
    RivenLocations.AGE_233_LEARN_PRISON_ELEVATOR_CODE: RivenLocationData(
        archipelago_id=location_offset + 141,
        region=RivenRegions.AGE_233,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.AGE_233_LOCATION,
        ),
    ),
    RivenLocations.STARRY_VISIT_VISIT_STARRY: RivenLocationData(
        archipelago_id=location_offset + 142,
        region=RivenRegions.STARRY_VISIT,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.STARRY_LOCATION,
        ),
    ),
    RivenLocations.STARRY_CONTROLS_NAVIGATE_EXPANSE: RivenLocationData(
        archipelago_id=location_offset + 143,
        region=RivenRegions.STARRY_CONTROLS,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.STARRY_LOCATION,
        ),
    ),
    RivenLocations.STARRY_TEMPLE_DOME_DELIVER_GREEN_POWER_MARBLE: RivenLocationData(
        archipelago_id=location_offset + 144,
        region=RivenRegions.STARRY_TEMPLE_DOME,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.STARRY_LOCATION,
        ),
    ),
    RivenLocations.STARRY_JUNGLE_DOME_DELIVER_RED_POWER_MARBLE: RivenLocationData(
        archipelago_id=location_offset + 145,
        region=RivenRegions.STARRY_JUNGLE_DOME,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.STARRY_LOCATION,
        ),
    ),
    RivenLocations.STARRY_BOILER_DOME_DELIVER_PURPLE_POWER_MARBLE: RivenLocationData(
        archipelago_id=location_offset + 146,
        region=RivenRegions.STARRY_BOILER_DOME,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.STARRY_LOCATION,
        ),
    ),
    RivenLocations.STARRY_SURVEY_DOME_DELIVER_ORANGE_POWER_MARBLE: RivenLocationData(
        archipelago_id=location_offset + 147,
        region=RivenRegions.STARRY_SURVEY_DOME,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.STARRY_LOCATION,
        ),
    ),
    RivenLocations.STARRY_PRISON_DOME_DELIVER_BLUE_POWER_MARBLE: RivenLocationData(
        archipelago_id=location_offset + 148,
        region=RivenRegions.STARRY_PRISON_DOME,
        tags=(
            RivenAPTags.CORE_LOCATION,
            RivenAPTags.STARRY_LOCATION,
        ),
    ),
}

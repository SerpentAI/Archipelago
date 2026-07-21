from typing import Dict, Optional

from rule_builder.rules import Rule, And, CanReachLocation, CanReachRegion, Has, Or

from ..enums import (
    RivenItems,
    RivenLocations,
    RivenRegions,
)


EntranceRuleData = Dict[RivenRegions, Dict[RivenRegions, Optional[Rule]]]

entrance_rule_data: EntranceRuleData = {
    RivenRegions.MENU: {
        RivenRegions.TEMPLE_PLATEAU: None,
    },
    RivenRegions.TEMPLE_PLATEAU: {
        RivenRegions.TEMPLE_STAR_FISSURE: And(
            CanReachLocation(
                RivenLocations.TEMPLE_STEAM_CONTROL_ROOM_POWER_TELESCOPE.value,
                parent_region_name=RivenRegions.TEMPLE_STEAM_CONTROL_ROOM.value,
            ),
            Has(RivenItems.SOLUTION_STAR_FISSURE_TELESCOPE.value, 10)
        ),
        RivenRegions.TEMPLE_GATE_ROOM: None,
        RivenRegions.TEMPLE_TEMPLE: None,
    },
    RivenRegions.TEMPLE_STAR_FISSURE: {
        RivenRegions.TEMPLE_PLATEAU: None,
    },
    RivenRegions.TEMPLE_GATE_ROOM: {
        RivenRegions.TEMPLE_PLATEAU: None,
        RivenRegions.TEMPLE_STEAM_CONTROL_ROOM: None,
        RivenRegions.TEMPLE_GOLDEN_DOME: Has(
            RivenItems.TEMPLE_GATE_ROOM_GATE_GOLDEN_DOME.value
        ),
        RivenRegions.TEMPLE_SPINNING_DOME: Has(
            RivenItems.TEMPLE_GATE_ROOM_GATE_SPINNING_DOME.value
        ),
    },
    RivenRegions.TEMPLE_STEAM_CONTROL_ROOM: {
        RivenRegions.TEMPLE_GATE_ROOM: None,
    },
    RivenRegions.TEMPLE_SPINNING_DOME: {
        RivenRegions.TEMPLE_GATE_ROOM: Has(
            RivenItems.TEMPLE_GATE_ROOM_GATE_SPINNING_DOME.value
        ),
        RivenRegions.STARRY_TEMPLE_DOME: None,
    },
    RivenRegions.TEMPLE_GOLDEN_DOME: {
        RivenRegions.TEMPLE_GATE_ROOM: Has(
            RivenItems.TEMPLE_GATE_ROOM_GATE_GOLDEN_DOME.value
        ),
        RivenRegions.TEMPLE_PROJECTION_ROOM: Has(
            RivenItems.TEMPLE_PROJECTION_ROOM_DOOR.value
        ),
        RivenRegions.TEMPLE_GOLDEN_DOME_UPPER: And(
            CanReachLocation(
                RivenLocations.STARRY_TEMPLE_DOME_DELIVER_GREEN_POWER_MARBLE.value,
                parent_region_name=RivenRegions.STARRY_TEMPLE_DOME.value,
            ),
            CanReachLocation(
                RivenLocations.STARRY_JUNGLE_DOME_DELIVER_RED_POWER_MARBLE.value,
                parent_region_name=RivenRegions.STARRY_JUNGLE_DOME.value,
            ),
            CanReachLocation(
                RivenLocations.STARRY_BOILER_DOME_DELIVER_PURPLE_POWER_MARBLE.value,
                parent_region_name=RivenRegions.STARRY_BOILER_DOME.value,
            ),
            CanReachLocation(
                RivenLocations.STARRY_SURVEY_DOME_DELIVER_ORANGE_POWER_MARBLE.value,
                parent_region_name=RivenRegions.STARRY_SURVEY_DOME.value,
            ),
            CanReachLocation(
                RivenLocations.STARRY_PRISON_DOME_DELIVER_BLUE_POWER_MARBLE.value,
                parent_region_name=RivenRegions.STARRY_PRISON_DOME.value,
            ),
        )
    },
    RivenRegions.TEMPLE_PROJECTION_ROOM: {
        RivenRegions.TEMPLE_GOLDEN_DOME: None,
    },
    RivenRegions.TEMPLE_GOLDEN_DOME_UPPER: {
        RivenRegions.TEMPLE_GOLDEN_DOME: None,
        RivenRegions.AGE_233: Has(
            RivenItems.SOLUTION_GOLDEN_DOME_SLIDERS.value
        ),
    },
    RivenRegions.TEMPLE_TEMPLE: {
        RivenRegions.TEMPLE_PLATEAU: None,
        RivenRegions.TEMPLE_MAGLEV_PLATFORM_TO_JUNGLE: CanReachLocation(
            RivenLocations.TEMPLE_PROJECTION_ROOM_SPIDER_CHAIR.value,
            parent_region_name=RivenRegions.TEMPLE_PROJECTION_ROOM.value,
        ),
    },
    RivenRegions.TEMPLE_MAGLEV_PLATFORM_TO_JUNGLE: {
        RivenRegions.TEMPLE_TEMPLE: CanReachLocation(
            RivenLocations.TEMPLE_PROJECTION_ROOM_SPIDER_CHAIR.value,
            parent_region_name=RivenRegions.TEMPLE_PROJECTION_ROOM.value,
        ),
        RivenRegions.JUNGLE_MAGLEV_PLATFORM_TO_TEMPLE: Has(
            RivenItems.MAGLEV_TEMPLE_JUNGLE_THROTTLE_LEVER.value
        ),
    },
    RivenRegions.JUNGLE_VISIT: {
        RivenRegions.JUNGLE_MAGLEV_PLATFORM_TO_TEMPLE: None,
        # There could be more places that trigger visit detection. Adjust as needed!
    },
    RivenRegions.JUNGLE_MAGLEV_PLATFORM_TO_TEMPLE: {
        RivenRegions.JUNGLE_VISIT: None,
        RivenRegions.TEMPLE_MAGLEV_PLATFORM_TO_JUNGLE: Has(
            RivenItems.MAGLEV_TEMPLE_JUNGLE_THROTTLE_LEVER.value
        ),
        RivenRegions.JUNGLE_WAHRK_TOTEM: None,
    },
    RivenRegions.JUNGLE_WAHRK_TOTEM: {
        RivenRegions.JUNGLE_MAGLEV_PLATFORM_TO_TEMPLE: None,
        RivenRegions.JUNGLE_BEACH: None,
        RivenRegions.JUNGLE_LOGGING_AREA: None,
    },
    RivenRegions.JUNGLE_BEACH: {
        RivenRegions.JUNGLE_WAHRK_TOTEM: None,
        RivenRegions.JUNGLE_BEETLE_TOTEM: None,
    },
    RivenRegions.JUNGLE_BEETLE_TOTEM: {
        RivenRegions.JUNGLE_BEACH: None,
        RivenRegions.JUNGLE_OUTSIDE_VILLAGE_SCHOOL_SIDE: None,
    },
    RivenRegions.JUNGLE_OUTSIDE_VILLAGE_SCHOOL_SIDE: {
        RivenRegions.JUNGLE_BEETLE_TOTEM: None,
        RivenRegions.JUNGLE_SCHOOLHOUSE: Has(
            RivenItems.JUNGLE_VILLAGE_SCHOOLHOUSE_DOOR.value
        ),
        RivenRegions.JUNGLE_VILLAGE: Has(
            RivenItems.JUNGLE_VILLAGE_UPPER_DRAWBRIDGE.value
        ),
    },
    RivenRegions.JUNGLE_SCHOOLHOUSE: {
        RivenRegions.JUNGLE_OUTSIDE_VILLAGE_SCHOOL_SIDE: None,
    },
    RivenRegions.JUNGLE_VILLAGE: {
        RivenRegions.JUNGLE_OUTSIDE_VILLAGE_SCHOOL_SIDE: Has(
            RivenItems.JUNGLE_VILLAGE_UPPER_DRAWBRIDGE.value
        ),
        RivenRegions.JUNGLE_VILLAGE_PODIUM: Has(
            RivenItems.JUNGLE_VILLAGE_PODIUM_PLATFORM.value
        ),
        RivenRegions.JUNGLE_OUTSIDE_VILLAGE_CHIMNEY_SIDE: Has(
            RivenItems.JUNGLE_VILLAGE_LOWER_DRAWBRIDGE.value
        )
    },
    RivenRegions.JUNGLE_VILLAGE_PODIUM: {
        RivenRegions.JUNGLE_VILLAGE: Has(
            RivenItems.JUNGLE_VILLAGE_PODIUM_PLATFORM.value
        ),
    },
    RivenRegions.JUNGLE_OUTSIDE_VILLAGE_CHIMNEY_SIDE: {
        RivenRegions.JUNGLE_VILLAGE: Has(
            RivenItems.JUNGLE_VILLAGE_LOWER_DRAWBRIDGE.value
        ),
        RivenRegions.JUNGLE_VILLAGE_WATER_HOLE: And(
            CanReachRegion(RivenRegions.JUNGLE_SUBMARINE_DESTINATION_PODIUM.value),
            Has(RivenItems.JUNGLE_VILLAGE_PODIUM_PLATFORM.value),
            Has(RivenItems.JUNGLE_VILLAGE_LOWER_DRAWBRIDGE.value),
        ),
        RivenRegions.JUNGLE_BLUE_CAVE: None,
    },
    RivenRegions.JUNGLE_BLUE_CAVE: {
        RivenRegions.JUNGLE_OUTSIDE_VILLAGE_CHIMNEY_SIDE: None,
        RivenRegions.JUNGLE_LOGGING_AREA: None,
        RivenRegions.JUNGLE_ANIMAL_CIRCLE_ROOM: And(
            Has(RivenItems.JUNGLE_BLUE_CAVE_BOLU_STICKS.value),
            Has(RivenItems.SOLUTION_BOLU_STICKS.value),
        )
    },
    RivenRegions.JUNGLE_LOGGING_AREA: {
        RivenRegions.JUNGLE_BLUE_CAVE: None,
        RivenRegions.JUNGLE_JUNGLE: Or(
            Has(RivenItems.JUNGLE_JUNGLE_MAIN_DOOR.value),
            Has(RivenItems.JUNGLE_JUNGLE_SIDE_DOOR.value),
        ),
        RivenRegions.JUNGLE_YTRAM_TOTEM: None,
        RivenRegions.JUNGLE_WOODCART_PLATFORM: None,
        RivenRegions.JUNGLE_WAHRK_TOTEM: None,
    },
    RivenRegions.JUNGLE_YTRAM_TOTEM: {
        RivenRegions.JUNGLE_LOGGING_AREA: None,
    },
    RivenRegions.JUNGLE_WOODCART_PLATFORM: {
        RivenRegions.JUNGLE_LOGGING_AREA: None,
        RivenRegions.BOILER_WOODCART_PLATFORM: Has(
            RivenItems.JUNGLE_WOODCART_PLATFORM_WOODCART_LEVERS.value
        ),
    },
    RivenRegions.JUNGLE_JUNGLE: {
        RivenRegions.JUNGLE_LOGGING_AREA: Or(
            Has(RivenItems.JUNGLE_JUNGLE_MAIN_DOOR.value),
            Has(RivenItems.JUNGLE_JUNGLE_SIDE_DOOR.value),
        ),
        RivenRegions.JUNGLE_WAHRK_ELEVATOR: CanReachLocation(
            RivenLocations.JUNGLE_WAHRK_ELEVATOR_OPEN_WAHRKS_MOUTH.value,
            parent_region_name=RivenRegions.JUNGLE_WAHRK_ELEVATOR.value,
        ),
    },
    RivenRegions.JUNGLE_WAHRK_ELEVATOR: {
        RivenRegions.JUNGLE_JUNGLE: None,
        RivenRegions.JUNGLE_JUNGLE_CATWALKS: Has(
            RivenItems.JUNGLE_JUNGLE_WAHRK_ELEVATOR_LEVER.value
        ),
        RivenRegions.JUNGLE_MAGLEV_PLATFORM_TO_SURVEY: Has(
            RivenItems.JUNGLE_JUNGLE_WAHRK_ELEVATOR_LEVER.value
        ),
    },
    RivenRegions.JUNGLE_JUNGLE_CATWALKS: {
        RivenRegions.JUNGLE_WAHRK_ELEVATOR: Has(
            RivenItems.JUNGLE_JUNGLE_WAHRK_ELEVATOR_LEVER.value
        ),
        RivenRegions.JUNGLE_BONE_THRONE: Has(
            RivenItems.JUNGLE_JUNGLE_BONE_THRONE_DOOR.value
        ),
        RivenRegions.STARRY_JUNGLE_DOME: None,
    },
    RivenRegions.JUNGLE_BONE_THRONE: {
        RivenRegions.JUNGLE_JUNGLE_CATWALKS: None,
    },
    RivenRegions.JUNGLE_MAGLEV_PLATFORM_TO_SURVEY: {
        RivenRegions.JUNGLE_WAHRK_ELEVATOR: Has(
            RivenItems.JUNGLE_JUNGLE_WAHRK_ELEVATOR_LEVER.value
        ),
        RivenRegions.JUNGLE_SUBMARINE_CAVE: None,
        RivenRegions.SURVEY_MAGLEV_PLATFORM_TO_JUNGLE: Has(
            RivenItems.MAGLEV_SURVEY_JUNGLE_THROTTLE_LEVER.value
        ),
    },
    RivenRegions.JUNGLE_SUBMARINE_CAVE: {
        RivenRegions.JUNGLE_MAGLEV_PLATFORM_TO_SURVEY: None,
        RivenRegions.JUNGLE_SUBMARINE_DESTINATION_SUBMARINE_CAVE: Has(
            RivenItems.JUNGLE_SUBMARINE_CAVE_BOARDING_PLATFORM_LEVER.value
        ),
    },
    RivenRegions.JUNGLE_SUBMARINE_DESTINATION_SUBMARINE_CAVE: {
        RivenRegions.JUNGLE_SUBMARINE_CAVE: None,
        RivenRegions.JUNGLE_SUBMARINE_DESTINATION_VILLAGE: None,
        RivenRegions.JUNGLE_SUBMARINE_DESTINATION_WAHRK_GALLOWS: None,
    },
    RivenRegions.JUNGLE_SUBMARINE_DESTINATION_VILLAGE: {
        RivenRegions.JUNGLE_OUTSIDE_VILLAGE_CHIMNEY_SIDE: None,
        RivenRegions.JUNGLE_SUBMARINE_DESTINATION_PODIUM: None,
        RivenRegions.JUNGLE_SUBMARINE_DESTINATION_SUBMARINE_CAVE: None,
    },
    RivenRegions.JUNGLE_VILLAGE_WATER_HOLE: {
        RivenRegions.JUNGLE_OUTSIDE_VILLAGE_CHIMNEY_SIDE: None,
        RivenRegions.JUNGLE_INSECT_TOTEM: CanReachLocation(
            RivenLocations.JUNGLE_VILLAGE_SHUT_STEAM_VENT.value,
            parent_region_name=RivenRegions.JUNGLE_VILLAGE.value,
        )
    },
    RivenRegions.JUNGLE_INSECT_TOTEM: {
        RivenRegions.JUNGLE_VILLAGE_WATER_HOLE: None,
    },
    RivenRegions.JUNGLE_SUBMARINE_DESTINATION_PODIUM: {
        RivenRegions.JUNGLE_VILLAGE_PODIUM: None,
        RivenRegions.JUNGLE_SUBMARINE_DESTINATION_SCHOOLHOUSE: None,
        RivenRegions.JUNGLE_SUBMARINE_DESTINATION_VILLAGE: None,
    },
    RivenRegions.JUNGLE_SUBMARINE_DESTINATION_SCHOOLHOUSE: {
        RivenRegions.JUNGLE_OUTSIDE_VILLAGE_SCHOOL_SIDE: None,
        RivenRegions.JUNGLE_SUBMARINE_DESTINATION_WAHRK_GALLOWS: None,
        RivenRegions.JUNGLE_SUBMARINE_DESTINATION_PODIUM: None,
    },
    RivenRegions.JUNGLE_SUBMARINE_DESTINATION_WAHRK_GALLOWS: {
        RivenRegions.JUNGLE_WAHRK_GALLOWS: None,
        RivenRegions.JUNGLE_SUBMARINE_DESTINATION_SUBMARINE_CAVE: None,
        RivenRegions.JUNGLE_SUBMARINE_DESTINATION_SCHOOLHOUSE: None,
    },
    RivenRegions.JUNGLE_WAHRK_GALLOWS: {
        RivenRegions.JUNGLE_WAHRK_GALLOWS_UPPER: CanReachLocation(
            RivenLocations.JUNGLE_BONE_THRONE_SEAL_WAHRK_GALLOWS.value,
            parent_region_name=RivenRegions.JUNGLE_BONE_THRONE.value,
        ),
    },
    RivenRegions.JUNGLE_WAHRK_GALLOWS_UPPER: {
        RivenRegions.JUNGLE_WAHRK_GALLOWS: CanReachLocation(
            RivenLocations.JUNGLE_BONE_THRONE_SEAL_WAHRK_GALLOWS.value,
            parent_region_name=RivenRegions.JUNGLE_BONE_THRONE.value,
        ),
        RivenRegions.JUNGLE_WAHRK_GALLOWS_JAIL_CELL: Has(
            RivenItems.JUNGLE_WAHRK_GALLOWS_JAIL_CELL_DOOR_CRANK.value
        ),
    },
    RivenRegions.JUNGLE_WAHRK_GALLOWS_JAIL_CELL: {
        RivenRegions.JUNGLE_SECRET_MOIETY_TUNNEL: CanReachLocation(
            RivenLocations.JUNGLE_BEACH_COLLECT_MOIETY_LENS.value,
            parent_region_name=RivenRegions.JUNGLE_BEACH.value
        ),
    },
    RivenRegions.JUNGLE_SECRET_MOIETY_TUNNEL: {
        RivenRegions.JUNGLE_WAHRK_GALLOWS_JAIL_CELL: None,
        RivenRegions.JUNGLE_ANIMAL_CIRCLE_ROOM: Has(
            RivenItems.JUNGLE_SECRET_MOIETY_TUNNEL_SECRET_DOOR.value
        )
    },
    RivenRegions.JUNGLE_ANIMAL_CIRCLE_ROOM: {
        RivenRegions.JUNGLE_SECRET_MOIETY_TUNNEL: And(
            CanReachLocation(
                RivenLocations.JUNGLE_BEACH_COLLECT_MOIETY_LENS.value,
                parent_region_name=RivenRegions.JUNGLE_BEACH.value
            ),
            Has(RivenItems.JUNGLE_SECRET_MOIETY_TUNNEL_SECRET_DOOR.value),
        ),
        RivenRegions.AGE_OF_TAY: Has(
            RivenItems.SOLUTION_ANIMAL_CIRCLE.value
        ),
    },
    RivenRegions.BOILER_VISIT: {
        RivenRegions.BOILER_WOODCART_PLATFORM: None,
        # There could be more places that trigger visit detection. Adjust as needed!
    },
    RivenRegions.BOILER_WOODCART_PLATFORM: {
        RivenRegions.BOILER_VISIT: None,
        RivenRegions.JUNGLE_WOODCART_PLATFORM: Has(
            RivenItems.JUNGLE_WOODCART_PLATFORM_WOODCART_LEVERS.value
        ),
        RivenRegions.BOILER_LAKE: None,
    },
    RivenRegions.BOILER_LAKE: {
        RivenRegions.BOILER_WOODCART_PLATFORM: None,
        RivenRegions.BOILER_BOILER_CONTROLS: None,
    },
    RivenRegions.BOILER_BOILER_CONTROLS: {
        RivenRegions.BOILER_LAKE: None,
        RivenRegions.BOILER_INSIDE_BOILER: And(
            Has(RivenItems.BOILER_BOILER_WATER_VALVE_LEVER.value),
            Has(RivenItems.BOILER_LAKE_STEAM_VALVE_LEVER.value),
        ),
    },
    RivenRegions.BOILER_INSIDE_BOILER: {
        RivenRegions.BOILER_BOILER_CONTROLS: None,
        RivenRegions.BOILER_BALCONY: None,
    },
    RivenRegions.BOILER_BALCONY: {
        RivenRegions.BOILER_LAKE: None,
        RivenRegions.BOILER_SPINNING_DOME: None,
        RivenRegions.BOILER_MINING_CAVE_PUMP_SIDE: None,
        RivenRegions.BOILER_CATWALK: None,
    },
    RivenRegions.BOILER_SPINNING_DOME: {
        RivenRegions.BOILER_BALCONY: None,
        RivenRegions.STARRY_BOILER_DOME: None,
    },
    RivenRegions.BOILER_MINING_CAVE_PUMP_SIDE: {
        RivenRegions.BOILER_BALCONY: None,
        RivenRegions.BOILER_MINING_CAVE_ELEVATOR_SIDE: Has(
            RivenItems.BOILER_MINING_CAVE_WATER_PUMP_BUTTON.value
        ),
    },
    RivenRegions.BOILER_MINING_CAVE_ELEVATOR_SIDE: {
        RivenRegions.BOILER_MINING_CAVE_PUMP_SIDE: None,
        RivenRegions.BOILER_LAB: Has(
            RivenItems.BOILER_LAB_ELEVATOR_CRANKS.value
        )
    },
    RivenRegions.BOILER_LAB: {
        RivenRegions.BOILER_CATWALK: Has(
            RivenItems.BOILER_LAB_CATWALK_DOOR.value
        ),
        RivenRegions.BOILER_MAGLEV_PLATFORM_TO_SURVEY: Has(
            RivenItems.BOILER_LAB_MAGLEV_DOOR.value
        ),
    },
    RivenRegions.BOILER_CATWALK: {
        RivenRegions.BOILER_LAB: Has(
            RivenItems.BOILER_LAB_CATWALK_DOOR.value
        ),
        RivenRegions.BOILER_BALCONY: None,
    },
    RivenRegions.BOILER_MAGLEV_PLATFORM_TO_SURVEY: {
        RivenRegions.BOILER_LAB: Has(
            RivenItems.BOILER_LAB_MAGLEV_DOOR.value
        ),
        RivenRegions.SURVEY_MAGLEV_PLATFORM_TO_BOILER: Has(
            RivenItems.MAGLEV_BOILER_SURVEY_THROTTLE_LEVER.value
        ),
    },
    RivenRegions.SURVEY_VISIT: {
        RivenRegions.SURVEY_MAGLEV_PLATFORM_TO_BOILER: None,
        # There could be more places that trigger visit detection. Adjust as needed!
    },
    RivenRegions.SURVEY_MAGLEV_PLATFORM_TO_BOILER: {
        RivenRegions.SURVEY_VISIT: None,
        RivenRegions.SURVEY_LOWER_PLATEAU: None,
        RivenRegions.SURVEY_GOLDEN_ELEVATOR_ROOM: Has(
            RivenItems.SURVEY_MAGLEV_PLATFORM_TO_BOILER_DOOR_LEVER.value
        ),
        RivenRegions.BOILER_MAGLEV_PLATFORM_TO_SURVEY: Has(
            RivenItems.MAGLEV_BOILER_SURVEY_THROTTLE_LEVER.value
        ),
    },
    RivenRegions.SURVEY_LOWER_PLATEAU: {
        RivenRegions.SURVEY_MAGLEV_PLATFORM_TO_BOILER: None,
        RivenRegions.SURVEY_PLATEAU_ELEVATOR: None,
    },
    RivenRegions.SURVEY_PLATEAU_ELEVATOR: {
        RivenRegions.SURVEY_LOWER_PLATEAU: None,
        RivenRegions.SURVEY_GEHNS_SPY_ROOM: Has(
            RivenItems.SURVEY_PLATEAU_ELEVATOR_BUTTONS.value
        ),
        RivenRegions.SURVEY_UPPER_PLATEAU: Has(
            RivenItems.SURVEY_PLATEAU_ELEVATOR_BUTTONS.value
        ),
    },
    RivenRegions.SURVEY_GEHNS_SPY_ROOM: {
        RivenRegions.SURVEY_PLATEAU_ELEVATOR: None,
    },
    RivenRegions.SURVEY_UPPER_PLATEAU: {
        RivenRegions.SURVEY_PLATEAU_ELEVATOR: Has(
            RivenItems.SURVEY_PLATEAU_ELEVATOR_BUTTONS.value
        ),
        RivenRegions.STARRY_SURVEY_DOME: None,
    },
    RivenRegions.SURVEY_GOLDEN_ELEVATOR_ROOM: {
        RivenRegions.SURVEY_MAGLEV_PLATFORM_TO_BOILER: Has(
            RivenItems.SURVEY_MAGLEV_PLATFORM_TO_BOILER_DOOR_LEVER.value
        ),
        RivenRegions.SURVEY_UNDERGROUND_TUNNEL: None,
    },
    RivenRegions.SURVEY_UNDERGROUND_TUNNEL: {
        RivenRegions.SURVEY_GOLDEN_ELEVATOR_ROOM: None,
        RivenRegions.SURVEY_MAGLEV_PLATFORM_TO_JUNGLE: None,
    },
    RivenRegions.SURVEY_MAGLEV_PLATFORM_TO_JUNGLE: {
        RivenRegions.JUNGLE_MAGLEV_PLATFORM_TO_SURVEY: Has(
            RivenItems.MAGLEV_SURVEY_JUNGLE_THROTTLE_LEVER.value
        ),
    },
    RivenRegions.PRISON_VISIT: {
        RivenRegions.PRISON_SPINNING_DOME: None,
    },
    RivenRegions.PRISON_SPINNING_DOME: {
        RivenRegions.PRISON_VISIT: None,
        RivenRegions.PRISON_BEACH: None,
        RivenRegions.PRISON_ELEVATOR: None,
        RivenRegions.STARRY_PRISON_DOME: None,
    },
    RivenRegions.PRISON_BEACH: {
        RivenRegions.PRISON_SPINNING_DOME: None,
        RivenRegions.PRISON_OUTSIDE_JAIL_CELL: None,
    },
    RivenRegions.PRISON_OUTSIDE_JAIL_CELL: {
        RivenRegions.PRISON_BEACH: None,
    },
    RivenRegions.PRISON_ELEVATOR: {
        RivenRegions.PRISON_SPINNING_DOME: None,
        RivenRegions.PRISON_JAIL_CELL: And(
            CanReachLocation(
                RivenLocations.AGE_233_TRAP_GEHN.value,
                parent_region_name=RivenRegions.AGE_233.value
            ),
            Has(
                RivenItems.SOLUTION_PRISON_ELEVATOR.value
            ),
        ),
    },
    RivenRegions.PRISON_JAIL_CELL: {
        RivenRegions.PRISON_ELEVATOR: None,
    },
    RivenRegions.AGE_OF_TAY: {
        RivenRegions.JUNGLE_ANIMAL_CIRCLE_ROOM: None,
    },
    RivenRegions.AGE_233: {
        RivenRegions.BOILER_LAB: None,
    },
    RivenRegions.STARRY_VISIT: {
        RivenRegions.STARRY_TEMPLE_DOME: None,
    },
    RivenRegions.STARRY_CONTROLS: {
        RivenRegions.STARRY_TEMPLE_DOME: None,
        RivenRegions.STARRY_JUNGLE_DOME: Has(
            RivenItems.STARRY_JUNGLE_BRIDGE.value
        ),
        RivenRegions.STARRY_BOILER_DOME: Has(
            RivenItems.STARRY_BOILER_BRIDGE.value
        ),
        RivenRegions.STARRY_SURVEY_DOME: Has(
            RivenItems.STARRY_SURVEY_BRIDGE.value
        ),
        RivenRegions.STARRY_PRISON_DOME: None,
    },
    RivenRegions.STARRY_TEMPLE_DOME: {
        RivenRegions.STARRY_VISIT: None,
        RivenRegions.STARRY_CONTROLS: None,
        RivenRegions.TEMPLE_SPINNING_DOME: None,
    },
    RivenRegions.STARRY_JUNGLE_DOME: {
        RivenRegions.STARRY_CONTROLS: Has(
            RivenItems.STARRY_JUNGLE_BRIDGE.value
        ),
        RivenRegions.JUNGLE_JUNGLE_CATWALKS: None,
    },
    RivenRegions.STARRY_BOILER_DOME: {
        RivenRegions.STARRY_CONTROLS: Has(
            RivenItems.STARRY_BOILER_BRIDGE.value
        ),
        RivenRegions.BOILER_SPINNING_DOME: None,
    },
    RivenRegions.STARRY_SURVEY_DOME: {
        RivenRegions.STARRY_CONTROLS: Has(
            RivenItems.STARRY_SURVEY_BRIDGE.value
        ),
        RivenRegions.SURVEY_UPPER_PLATEAU: None,
    },
    RivenRegions.STARRY_PRISON_DOME: {
        RivenRegions.STARRY_CONTROLS: None,
        RivenRegions.PRISON_SPINNING_DOME: None,
    },
}

LocationRuleData = Dict[RivenLocations, Optional[Rule]]

location_rule_data: LocationRuleData = {
    RivenLocations.TEMPLE_PLATEAU_READ_ATRUS_JOURNAL: None,
    RivenLocations.TEMPLE_PLATEAU_GAZE_STAR_FISSURE: None,
    RivenLocations.TEMPLE_PLATEAU_BREAK_TELESCOPE_LEVER: None,
    RivenLocations.TEMPLE_PLATEAU_FIND_CHO: None,
    RivenLocations.TEMPLE_PLATEAU_REMOVE_HINGE: None,
    RivenLocations.TEMPLE_GATE_ROOM_BEETLE_1: Has(RivenItems.TEMPLE_GATE_ROOM_BEETLE_VIEWERS.value),
    RivenLocations.TEMPLE_GATE_ROOM_BEETLE_2: Has(RivenItems.TEMPLE_GATE_ROOM_BEETLE_VIEWERS.value),
    RivenLocations.TEMPLE_GATE_ROOM_BEETLE_3: Has(RivenItems.TEMPLE_GATE_ROOM_BEETLE_VIEWERS.value),
    RivenLocations.TEMPLE_GATE_ROOM_BEETLE_4: Has(RivenItems.TEMPLE_GATE_ROOM_BEETLE_VIEWERS.value),
    RivenLocations.TEMPLE_GATE_ROOM_BEETLE_5: Has(RivenItems.TEMPLE_GATE_ROOM_BEETLE_VIEWERS.value),
    RivenLocations.TEMPLE_STEAM_CONTROL_ROOM_POWER_TELESCOPE: Has(RivenItems.TEMPLE_STEAM_CONTROL_STEAM_VALVE_LEVER.value),
    RivenLocations.TEMPLE_SPINNING_DOME_OPEN_DOME: None,
    RivenLocations.TEMPLE_GOLDEN_DOME_ENTER_DOME: None,
    RivenLocations.TEMPLE_GOLDEN_DOME_TEMPLE_SYMBOL: None,
    RivenLocations.TEMPLE_GOLDEN_DOME_JUNGLE_SYMBOL: None,
    RivenLocations.TEMPLE_GOLDEN_DOME_BOILER_SYMBOL: None,
    RivenLocations.TEMPLE_GOLDEN_DOME_SURVEY_SYMBOL: None,
    RivenLocations.TEMPLE_GOLDEN_DOME_PRISON_SYMBOL: None,
    RivenLocations.TEMPLE_PROJECTION_ROOM_ENTER_PROJECTION_ROOM: None,
    RivenLocations.TEMPLE_PROJECTION_ROOM_SPIDER_CHAIR: None,
    RivenLocations.TEMPLE_GOLDEN_DOME_COLLAPSE_BRIDGE: None,
    RivenLocations.TEMPLE_GOLDEN_DOME_UPPER_ACCESS_UPPER: None,
    RivenLocations.TEMPLE_GOLDEN_DOME_UPPER_PLACE_PURPLE_MARBLE: None,
    RivenLocations.TEMPLE_GOLDEN_DOME_UPPER_PLACE_GREEN_MARBLE: None,
    RivenLocations.TEMPLE_GOLDEN_DOME_UPPER_PLACE_BLUE_MARBLE: None,
    RivenLocations.TEMPLE_GOLDEN_DOME_UPPER_PLACE_RED_MARBLE: None,
    RivenLocations.TEMPLE_GOLDEN_DOME_UPPER_PLACE_ORANGE_MARBLE: None,
    RivenLocations.TEMPLE_GOLDEN_DOME_UPPER_ACCESS_AGE_233_BOOK: Has(RivenItems.SOLUTION_GOLDEN_DOME_SLIDERS.value),
    RivenLocations.TEMPLE_MAGLEV_PLATFORM_TO_JUNGLE_PRESS_BUTTON: None,
    RivenLocations.JUNGLE_VISIT_VISIT_JUNGLE: None,
    RivenLocations.JUNGLE_MAGLEV_PLATFORM_TO_TEMPLE_PRESS_BUTTON: None,
    RivenLocations.JUNGLE_WAHRK_TOTEM_INTERACT: None,
    RivenLocations.JUNGLE_WAHRK_TOTEM_DIVERT_WATER: None,
    RivenLocations.JUNGLE_BEACH_COLLECT_MOIETY_LENS: None,
    RivenLocations.JUNGLE_BEETLE_TOTEM_INTERACT: None,
    RivenLocations.JUNGLE_OUTSIDE_VILLAGE_SCHOOL_SIDE_GRAB_BBQ: None,
    RivenLocations.JUNGLE_SCHOOLHOUSE_ENTER_SCHOOLHOUSE: None,
    RivenLocations.JUNGLE_SCHOOLHOUSE_INSPECT_WAHRK_GAME: None,
    RivenLocations.JUNGLE_VILLAGE_KNOCK_ON_DOOR: None,
    RivenLocations.JUNGLE_VILLAGE_INHALE_STEAM: None,
    RivenLocations.JUNGLE_VILLAGE_SHUT_STEAM_VENT: None,
    RivenLocations.JUNGLE_VILLAGE_PROVIDE_WATER_TO_TREE: None,
    RivenLocations.JUNGLE_BLUE_CAVE_OPEN_SECRET_DOOR: And(Has(RivenItems.JUNGLE_BLUE_CAVE_BOLU_STICKS.value), Has(RivenItems.SOLUTION_BOLU_STICKS.value)),
    RivenLocations.JUNGLE_LOGGING_AREA_GET_SPOTTED_BY_GUARD: None,
    RivenLocations.JUNGLE_YTRAM_TOTEM_INTERACT: None,
    RivenLocations.JUNGLE_WOODCART_PLATFORM_PRESS_BUTTON: None,
    RivenLocations.JUNGLE_WAHRK_ELEVATOR_OPEN_WAHRKS_MOUTH: None,
    RivenLocations.JUNGLE_JUNGLE_CATWALKS_OPEN_DOME: None,
    RivenLocations.JUNGLE_BONE_THRONE_LOOK_DOWN_UPON_VILLAGE: None,
    RivenLocations.JUNGLE_BONE_THRONE_SEAL_WAHRK_GALLOWS: None,
    RivenLocations.JUNGLE_MAGLEV_PLATFORM_TO_SURVEY_PRESS_BUTTON: None,
    RivenLocations.JUNGLE_MAGLEV_PLATFORM_TO_SURVEY_PRESS_OTHER_BUTTON: None,
    RivenLocations.JUNGLE_SUBMARINE_CAVE_PRESS_BUTTON: None,
    RivenLocations.JUNGLE_SUBMARINE_DESTINATION_SUBMARINE_CAVE_BOARD_SUBMARINE: None,
    RivenLocations.JUNGLE_SUBMARINE_DESTINATION_VILLAGE_PILOT: None,
    RivenLocations.JUNGLE_VILLAGE_WATER_HOLE_FLICK_SWITCH: None,
    RivenLocations.JUNGLE_INSECT_TOTEM_INTERACT: None,
    RivenLocations.JUNGLE_SUBMARINE_DESTINATION_PODIUM_PILOT: None,
    RivenLocations.JUNGLE_SUBMARINE_DESTINATION_SCHOOLHOUSE_PILOT: None,
    RivenLocations.JUNGLE_SUBMARINE_DESTINATION_WAHRK_GALLOWS_PILOT: None,
    RivenLocations.JUNGLE_WAHRK_GALLOWS_JAIL_CELL_OPEN_SECRET_DOOR: None,
    RivenLocations.JUNGLE_SECRET_MOIETY_TUNNEL_TURN_ON_LIGHT_1: None,
    RivenLocations.JUNGLE_SECRET_MOIETY_TUNNEL_TURN_ON_LIGHT_2: None,
    RivenLocations.JUNGLE_SECRET_MOIETY_TUNNEL_TURN_ON_LIGHT_3: None,
    RivenLocations.JUNGLE_SECRET_MOIETY_TUNNEL_TURN_ON_LIGHT_4: None,
    RivenLocations.JUNGLE_SECRET_MOIETY_TUNNEL_TURN_ON_LIGHT_5: None,
    RivenLocations.JUNGLE_SECRET_MOIETY_TUNNEL_TURN_ON_LIGHT_6: None,
    RivenLocations.JUNGLE_SECRET_MOIETY_TUNNEL_TURN_ON_LIGHT_7: None,
    RivenLocations.JUNGLE_SECRET_MOIETY_TUNNEL_TURN_ON_LIGHT_8: None,
    RivenLocations.JUNGLE_SECRET_MOIETY_TUNNEL_OPEN_SECRET_DOOR: Has(RivenItems.JUNGLE_SECRET_MOIETY_TUNNEL_SECRET_DOOR.value),
    RivenLocations.JUNGLE_ANIMAL_CIRCLE_ROOM_ACCESS_TAY_BOOK: Has(RivenItems.SOLUTION_ANIMAL_CIRCLE.value),
    RivenLocations.JUNGLE_ANIMAL_CIRCLE_ROOM_INPUT_CLASSIC_SOLUTION: None,
    RivenLocations.BOILER_VISIT_VISIT_BOILER: None,
    RivenLocations.BOILER_WOODCART_PLATFORM_PRESS_BUTTON: None,
    RivenLocations.BOILER_WOODCART_PLATFORM_TURN_ON_WOOD_CHIPPER: Has(RivenItems.BOILER_LAKE_STEAM_VALVE_LEVER.value),
    RivenLocations.BOILER_LAKE_DIRECT_STEAM_WOOD_CHIPPER: Has(RivenItems.BOILER_LAKE_STEAM_VALVE_LEVER.value),
    RivenLocations.BOILER_LAKE_DIRECT_STEAM_BOILER: Has(RivenItems.BOILER_LAKE_STEAM_VALVE_LEVER.value),
    RivenLocations.BOILER_LAKE_DISCOVER_BURNT_BOOK: None,
    RivenLocations.BOILER_BOILER_CONTROLS_RAISE_FLOOR: Has(RivenItems.BOILER_LAKE_STEAM_VALVE_LEVER.value),
    RivenLocations.BOILER_BOILER_CONTROLS_DRAIN_WATER: And(Has(RivenItems.BOILER_BOILER_WATER_VALVE_LEVER.value), Has(RivenItems.BOILER_LAKE_STEAM_VALVE_LEVER.value)),
    RivenLocations.BOILER_BOILER_CONTROLS_TURN_OFF_HEAT: None,
    RivenLocations.BOILER_INSIDE_BOILER_ENTER_BOILER: None,
    RivenLocations.BOILER_BALCONY_OPEN_HATCH: None,
    RivenLocations.BOILER_SPINNING_DOME_OPEN_DOME: None,
    RivenLocations.BOILER_MINING_CAVE_PUMP_SIDE_DRAIN_WATER: Has(RivenItems.BOILER_MINING_CAVE_WATER_PUMP_BUTTON.value),
    RivenLocations.BOILER_MINING_CAVE_PUMP_SIDE_MINE_FIRE_MARBLE_GEODE: Has(RivenItems.BOILER_MINING_CAVE_WATER_PUMP_BUTTON.value),
    RivenLocations.BOILER_MINING_CAVE_ELEVATOR_SIDE_SLOT_CART_IN_ELEVATOR: Has(RivenItems.BOILER_LAB_ELEVATOR_CRANKS.value),
    RivenLocations.BOILER_LAB_VISIT_GEHNS_LAB: None,
    RivenLocations.BOILER_LAB_READ_GEHNS_JOURNAL: None,
    RivenLocations.BOILER_LAB_TRY_OUT_MAGNIFYING_GLASS: None,
    RivenLocations.BOILER_LAB_CLOSE_PRESS: None,
    RivenLocations.BOILER_LAB_CRACK_OPEN_FIRE_MARBLE_GEODE: And(Has(RivenItems.BOILER_LAB_GEODE_CUTTER_CRANK.value), CanReachLocation(RivenLocations.BOILER_MINING_CAVE_ELEVATOR_SIDE_SLOT_CART_IN_ELEVATOR.value, parent_region_name=RivenRegions.BOILER_MINING_CAVE_ELEVATOR_SIDE.value)),
    RivenLocations.BOILER_LAB_MEASURE_OPTIMAL_MARBLE_STRIKE_FORCE: And(Has(RivenItems.BOILER_LAB_GEODE_CUTTER_CRANK.value), CanReachLocation(RivenLocations.BOILER_MINING_CAVE_ELEVATOR_SIDE_SLOT_CART_IN_ELEVATOR.value, parent_region_name=RivenRegions.BOILER_MINING_CAVE_ELEVATOR_SIDE.value)),
    RivenLocations.BOILER_LAB_FREE_YTRAM: None,
    RivenLocations.BOILER_LAB_SPEED_UP_FLYWHEEL: None,
    RivenLocations.BOILER_LAB_STOP_POLISHER: None,
    RivenLocations.BOILER_MAGLEV_PLATFORM_TO_SURVEY_PRESS_BUTTON: None,
    RivenLocations.SURVEY_VISIT_VISIT_SURVEY: None,
    RivenLocations.SURVEY_MAGLEV_PLATFORM_TO_BOILER_PRESS_BUTTON: None,
    RivenLocations.SURVEY_MAGLEV_PLATFORM_TO_BOILER_PRESS_OTHER_BUTTON: None,
    RivenLocations.SURVEY_GEHNS_SPY_ROOM_DISCOVER_GEHNS_SPY_ROOM: None,
    RivenLocations.SURVEY_GEHNS_SPY_ROOM_VIEW_PRISON_CAMERA: Has(RivenItems.SURVEY_GEHNS_SPY_ROOM_LEFT_AQUARIUM_CHAIR_LEVER.value),
    RivenLocations.SURVEY_GEHNS_SPY_ROOM_VIEW_JUNGLE_CAMERA: Has(RivenItems.SURVEY_GEHNS_SPY_ROOM_LEFT_AQUARIUM_CHAIR_LEVER.value),
    RivenLocations.SURVEY_GEHNS_SPY_ROOM_VIEW_SURVEY_CAMERA: Has(RivenItems.SURVEY_GEHNS_SPY_ROOM_LEFT_AQUARIUM_CHAIR_LEVER.value),
    RivenLocations.SURVEY_GEHNS_SPY_ROOM_VIEW_BOILER_CAMERA: Has(RivenItems.SURVEY_GEHNS_SPY_ROOM_LEFT_AQUARIUM_CHAIR_LEVER.value),
    RivenLocations.SURVEY_GEHNS_SPY_ROOM_VIEW_TEMPLE_CAMERA: Has(RivenItems.SURVEY_GEHNS_SPY_ROOM_LEFT_AQUARIUM_CHAIR_LEVER.value),
    RivenLocations.SURVEY_GEHNS_SPY_ROOM_TURN_ON_BLUE_LIGHT: Has(RivenItems.SURVEY_GEHNS_SPY_ROOM_RIGHT_AQUARIUM_CHAIR_LEVER.value),
    RivenLocations.SURVEY_GEHNS_SPY_ROOM_TURN_ON_GREEN_LIGHT: Has(RivenItems.SURVEY_GEHNS_SPY_ROOM_RIGHT_AQUARIUM_CHAIR_LEVER.value),
    RivenLocations.SURVEY_GEHNS_SPY_ROOM_TURN_ON_YELLOW_LIGHT: Has(RivenItems.SURVEY_GEHNS_SPY_ROOM_RIGHT_AQUARIUM_CHAIR_LEVER.value),
    RivenLocations.SURVEY_GEHNS_SPY_ROOM_TURN_ON_ORANGE_LIGHT: Has(RivenItems.SURVEY_GEHNS_SPY_ROOM_RIGHT_AQUARIUM_CHAIR_LEVER.value),
    RivenLocations.SURVEY_GEHNS_SPY_ROOM_TURN_ON_RED_LIGHT: Has(RivenItems.SURVEY_GEHNS_SPY_ROOM_RIGHT_AQUARIUM_CHAIR_LEVER.value),
    RivenLocations.SURVEY_GEHNS_SPY_ROOM_ANNOY_WAHRK: Has(RivenItems.SURVEY_GEHNS_SPY_ROOM_RIGHT_AQUARIUM_CHAIR_LEVER.value),
    RivenLocations.SURVEY_UPPER_PLATEAU_OPEN_DOME: None,
    RivenLocations.SURVEY_UPPER_PLATEAU_PRESS_GEHNTRIS_TEMPLE_BUTTON: Has(RivenItems.SURVEY_UPPER_PLATEAU_GEHNTRIS_BOARD.value),
    RivenLocations.SURVEY_UPPER_PLATEAU_PRESS_GEHNTRIS_JUNGLE_BUTTON: Has(RivenItems.SURVEY_UPPER_PLATEAU_GEHNTRIS_BOARD.value),
    RivenLocations.SURVEY_UPPER_PLATEAU_PRESS_GEHNTRIS_BOILER_BUTTON: Has(RivenItems.SURVEY_UPPER_PLATEAU_GEHNTRIS_BOARD.value),
    RivenLocations.SURVEY_UPPER_PLATEAU_PRESS_GEHNTRIS_SURVEY_BUTTON: Has(RivenItems.SURVEY_UPPER_PLATEAU_GEHNTRIS_BOARD.value),
    RivenLocations.SURVEY_UPPER_PLATEAU_PRESS_GEHNTRIS_PRISON_BUTTON: Has(RivenItems.SURVEY_UPPER_PLATEAU_GEHNTRIS_BOARD.value),
    RivenLocations.SURVEY_UNDERGROUND_TUNNEL_ENCOUNTER_GEHNS_SCRIBE: None,
    RivenLocations.SURVEY_MAGLEV_PLATFORM_TO_JUNGLE_PRESS_BUTTON: None,
    RivenLocations.PRISON_VISIT_VISIT_PRISON: None,
    RivenLocations.PRISON_SPINNING_DOME_OPEN_DOME: None,
    RivenLocations.PRISON_BEACH_INTERACT_TOTEM: None,
    RivenLocations.PRISON_BEACH_ROTATE_LOG_TELESCOPE: Has(RivenItems.PRISON_BEACH_LOG_TELESCOPE.value),
    RivenLocations.PRISON_BEACH_LOOK_THROUGH_LOG_TELESCOPE: Has(RivenItems.PRISON_BEACH_LOG_TELESCOPE.value),
    RivenLocations.PRISON_OUTSIDE_JAIL_CELL_MEET_CATHERINE: None,
    RivenLocations.PRISON_JAIL_CELL_FREE_CATHERINE: None,
    RivenLocations.AGE_OF_TAY_GET_IMPRISONED: None,
    RivenLocations.AGE_OF_TAY_GET_PRISON_BOOK_BACK: None,
    RivenLocations.AGE_OF_TAY_READ_CATHERINES_JOURNAL: None,
    RivenLocations.AGE_OF_TAY_EXPLORE_HIVE: None,
    RivenLocations.AGE_233_MEET_GEHN: None,
    RivenLocations.AGE_233_TRAP_GEHN: CanReachLocation(RivenLocations.AGE_OF_TAY_GET_PRISON_BOOK_BACK.value, parent_region_name=RivenRegions.AGE_OF_TAY.value),
    RivenLocations.AGE_233_TURN_ON_STOVE: CanReachLocation(RivenLocations.AGE_OF_TAY_GET_PRISON_BOOK_BACK.value, parent_region_name=RivenRegions.AGE_OF_TAY.value),
    RivenLocations.AGE_233_LOWER_CAGE: CanReachLocation(RivenLocations.AGE_OF_TAY_GET_PRISON_BOOK_BACK.value, parent_region_name=RivenRegions.AGE_OF_TAY.value),
    RivenLocations.AGE_233_GRAB_BBQ: CanReachLocation(RivenLocations.AGE_OF_TAY_GET_PRISON_BOOK_BACK.value, parent_region_name=RivenRegions.AGE_OF_TAY.value),
    RivenLocations.AGE_233_SIT_ON_THRONE: CanReachLocation(RivenLocations.AGE_OF_TAY_GET_PRISON_BOOK_BACK.value, parent_region_name=RivenRegions.AGE_OF_TAY.value),
    RivenLocations.AGE_233_TURN_ON_FAUCET: CanReachLocation(RivenLocations.AGE_OF_TAY_GET_PRISON_BOOK_BACK.value, parent_region_name=RivenRegions.AGE_OF_TAY.value),
    RivenLocations.AGE_233_WATCH_KETAS_PROJECTION: CanReachLocation(RivenLocations.AGE_OF_TAY_GET_PRISON_BOOK_BACK.value, parent_region_name=RivenRegions.AGE_OF_TAY.value),
    RivenLocations.AGE_233_READ_GEHNS_JOURNAL: CanReachLocation(RivenLocations.AGE_OF_TAY_GET_PRISON_BOOK_BACK.value, parent_region_name=RivenRegions.AGE_OF_TAY.value),
    RivenLocations.AGE_233_LEARN_PRISON_ELEVATOR_CODE: CanReachLocation(RivenLocations.AGE_OF_TAY_GET_PRISON_BOOK_BACK.value, parent_region_name=RivenRegions.AGE_OF_TAY.value),
    RivenLocations.STARRY_VISIT_VISIT_STARRY: None,
    RivenLocations.STARRY_CONTROLS_NAVIGATE_EXPANSE: None,
    RivenLocations.STARRY_TEMPLE_DOME_DELIVER_GREEN_POWER_MARBLE: Has(RivenItems.STARRY_MARBLE_DEVICES.value),  # These might need to be done in a certain order for game state to update. TBD
    RivenLocations.STARRY_JUNGLE_DOME_DELIVER_RED_POWER_MARBLE: Has(RivenItems.STARRY_MARBLE_DEVICES.value),
    RivenLocations.STARRY_BOILER_DOME_DELIVER_PURPLE_POWER_MARBLE: Has(RivenItems.STARRY_MARBLE_DEVICES.value),
    RivenLocations.STARRY_SURVEY_DOME_DELIVER_ORANGE_POWER_MARBLE: Has(RivenItems.STARRY_MARBLE_DEVICES.value),
    RivenLocations.STARRY_PRISON_DOME_DELIVER_BLUE_POWER_MARBLE: Has(RivenItems.STARRY_MARBLE_DEVICES.value),
}

from typing import Dict, NamedTuple, Tuple

from BaseClasses import ItemClassification

from ..enums import RivenAPTags, RivenItems


class RivenItemData(NamedTuple):
    archipelago_id: int
    classification: ItemClassification
    tags: Tuple[RivenAPTags, ...]


item_base_offset: int = 10000

item_data: Dict[RivenItems, RivenItemData] = {
    # Progression
    # RivenItems.TEMPLE_GATE_ROOM_BUTTONS: RivenItemData(
    #     archipelago_id=item_base_offset + 1,
    #     classification=ItemClassification.progression,
    #     tags=(
    #         RivenAPTags.UNLOCK_ITEM,
    #         RivenAPTags.TEMPLE_ITEM,
    #     ),
    # ),
    RivenItems.TEMPLE_GATE_ROOM_BEETLE_VIEWERS: RivenItemData(
        archipelago_id=item_base_offset + 2,
        classification=ItemClassification.progression,
        tags=(
            RivenAPTags.UNLOCK_ITEM,
            RivenAPTags.TEMPLE_ITEM,
        ),
    ),
    RivenItems.TEMPLE_GATE_ROOM_GATE_GOLDEN_DOME: RivenItemData(
        archipelago_id=item_base_offset + 3,
        classification=ItemClassification.progression,
        tags=(
            RivenAPTags.UNLOCK_ITEM,
            RivenAPTags.TEMPLE_ITEM,
        ),
    ),
    RivenItems.TEMPLE_GATE_ROOM_GATE_SPINNING_DOME: RivenItemData(
        archipelago_id=item_base_offset + 4,
        classification=ItemClassification.progression,
        tags=(
            RivenAPTags.UNLOCK_ITEM,
            RivenAPTags.TEMPLE_ITEM,
        ),
    ),
    RivenItems.TEMPLE_STEAM_CONTROL_STEAM_VALVE_LEVER: RivenItemData(
        archipelago_id=item_base_offset + 5,
        classification=ItemClassification.progression,
        tags=(
            RivenAPTags.UNLOCK_ITEM,
            RivenAPTags.TEMPLE_ITEM,
        ),
    ),
    RivenItems.TEMPLE_PROJECTION_ROOM_DOOR: RivenItemData(
        archipelago_id=item_base_offset + 6,
        classification=ItemClassification.progression,
        tags=(
            RivenAPTags.UNLOCK_ITEM,
            RivenAPTags.TEMPLE_ITEM,
        ),
    ),
    # RivenItems.TEMPLE_TEMPLE_MAIN_DOOR: RivenItemData(
    #     archipelago_id=item_base_offset + 7,
    #     classification=ItemClassification.progression,
    #     tags=(
    #         RivenAPTags.UNLOCK_ITEM,
    #         RivenAPTags.TEMPLE_ITEM,
    #     ),
    # ),
    RivenItems.JUNGLE_VILLAGE_UPPER_DRAWBRIDGE: RivenItemData(
        archipelago_id=item_base_offset + 8,
        classification=ItemClassification.progression,
        tags=(
            RivenAPTags.UNLOCK_ITEM,
            RivenAPTags.JUNGLE_ITEM,
        ),
    ),
    RivenItems.JUNGLE_VILLAGE_PODIUM_PLATFORM: RivenItemData(
        archipelago_id=item_base_offset + 9,
        classification=ItemClassification.progression,
        tags=(
            RivenAPTags.UNLOCK_ITEM,
            RivenAPTags.JUNGLE_ITEM,
        ),
    ),
    RivenItems.JUNGLE_VILLAGE_LOWER_DRAWBRIDGE: RivenItemData(
        archipelago_id=item_base_offset + 10,
        classification=ItemClassification.progression,
        tags=(
            RivenAPTags.UNLOCK_ITEM,
            RivenAPTags.JUNGLE_ITEM,
        ),
    ),
    RivenItems.JUNGLE_VILLAGE_SCHOOLHOUSE_DOOR: RivenItemData(
        archipelago_id=item_base_offset + 11,
        classification=ItemClassification.progression,
        tags=(
            RivenAPTags.UNLOCK_ITEM,
            RivenAPTags.JUNGLE_ITEM,
        ),
    ),
    RivenItems.JUNGLE_WOODCART_PLATFORM_WOODCART_LEVERS: RivenItemData(
        archipelago_id=item_base_offset + 12,
        classification=ItemClassification.progression,
        tags=(
            RivenAPTags.UNLOCK_ITEM,
            RivenAPTags.JUNGLE_ITEM,
        ),
    ),
    RivenItems.JUNGLE_BLUE_CAVE_BOLU_STICKS: RivenItemData(
        archipelago_id=item_base_offset + 13,
        classification=ItemClassification.progression,
        tags=(
            RivenAPTags.UNLOCK_ITEM,
            RivenAPTags.JUNGLE_ITEM,
        ),
    ),
    RivenItems.JUNGLE_JUNGLE_MAIN_DOOR: RivenItemData(
        archipelago_id=item_base_offset + 14,
        classification=ItemClassification.progression,
        tags=(
            RivenAPTags.UNLOCK_ITEM,
            RivenAPTags.JUNGLE_ITEM,
        ),
    ),
    RivenItems.JUNGLE_JUNGLE_SIDE_DOOR: RivenItemData(
        archipelago_id=item_base_offset + 15,
        classification=ItemClassification.progression,
        tags=(
            RivenAPTags.UNLOCK_ITEM,
            RivenAPTags.JUNGLE_ITEM,
        ),
    ),
    RivenItems.JUNGLE_JUNGLE_WAHRK_ELEVATOR_LEVER: RivenItemData(
        archipelago_id=item_base_offset + 16,
        classification=ItemClassification.progression,
        tags=(
            RivenAPTags.UNLOCK_ITEM,
            RivenAPTags.JUNGLE_ITEM,
        ),
    ),
    RivenItems.JUNGLE_JUNGLE_BONE_THRONE_DOOR: RivenItemData(
        archipelago_id=item_base_offset + 17,
        classification=ItemClassification.progression,
        tags=(
            RivenAPTags.UNLOCK_ITEM,
            RivenAPTags.JUNGLE_ITEM,
        ),
    ),
    RivenItems.JUNGLE_SUBMARINE_CAVE_BOARDING_PLATFORM_LEVER: RivenItemData(
        archipelago_id=item_base_offset + 18,
        classification=ItemClassification.progression,
        tags=(
            RivenAPTags.UNLOCK_ITEM,
            RivenAPTags.JUNGLE_ITEM,
        ),
    ),
    RivenItems.JUNGLE_WAHRK_GALLOWS_JAIL_CELL_DOOR_CRANK: RivenItemData(
        archipelago_id=item_base_offset + 19,
        classification=ItemClassification.progression,
        tags=(
            RivenAPTags.UNLOCK_ITEM,
            RivenAPTags.JUNGLE_ITEM,
        ),
    ),
    RivenItems.JUNGLE_SECRET_MOIETY_TUNNEL_SECRET_DOOR: RivenItemData(
        archipelago_id=item_base_offset + 20,
        classification=ItemClassification.progression,
        tags=(
            RivenAPTags.UNLOCK_ITEM,
            RivenAPTags.JUNGLE_ITEM,
        ),
    ),
    RivenItems.BOILER_LAKE_STEAM_VALVE_LEVER: RivenItemData(
        archipelago_id=item_base_offset + 21,
        classification=ItemClassification.progression,
        tags=(
            RivenAPTags.UNLOCK_ITEM,
            RivenAPTags.BOILER_ITEM,
        ),
    ),
    RivenItems.BOILER_BOILER_WATER_VALVE_LEVER: RivenItemData(
        archipelago_id=item_base_offset + 22,
        classification=ItemClassification.progression,
        tags=(
            RivenAPTags.UNLOCK_ITEM,
            RivenAPTags.BOILER_ITEM,
        ),
    ),
    RivenItems.BOILER_MINING_CAVE_WATER_PUMP_BUTTON: RivenItemData(
        archipelago_id=item_base_offset + 23,
        classification=ItemClassification.progression,
        tags=(
            RivenAPTags.UNLOCK_ITEM,
            RivenAPTags.BOILER_ITEM,
        ),
    ),
    RivenItems.BOILER_LAB_ELEVATOR_CRANKS: RivenItemData(
        archipelago_id=item_base_offset + 24,
        classification=ItemClassification.progression,
        tags=(
            RivenAPTags.UNLOCK_ITEM,
            RivenAPTags.BOILER_ITEM,
        ),
    ),
    RivenItems.BOILER_LAB_CATWALK_DOOR: RivenItemData(
        archipelago_id=item_base_offset + 25,
        classification=ItemClassification.progression,
        tags=(
            RivenAPTags.UNLOCK_ITEM,
            RivenAPTags.BOILER_ITEM,
        ),
    ),
    RivenItems.BOILER_LAB_MAGLEV_DOOR: RivenItemData(
        archipelago_id=item_base_offset + 26,
        classification=ItemClassification.progression,
        tags=(
            RivenAPTags.UNLOCK_ITEM,
            RivenAPTags.BOILER_ITEM,
        ),
    ),
    RivenItems.BOILER_LAB_GEODE_CUTTER_CRANK: RivenItemData(
        archipelago_id=item_base_offset + 27,
        classification=ItemClassification.progression,
        tags=(
            RivenAPTags.UNLOCK_ITEM,
            RivenAPTags.BOILER_ITEM,
        ),
    ),
    RivenItems.SURVEY_PLATEAU_ELEVATOR_BUTTONS: RivenItemData(
        archipelago_id=item_base_offset + 28,
        classification=ItemClassification.progression,
        tags=(
            RivenAPTags.UNLOCK_ITEM,
            RivenAPTags.SURVEY_ITEM,
        ),
    ),
    RivenItems.SURVEY_GEHNS_SPY_ROOM_LEFT_AQUARIUM_CHAIR_LEVER: RivenItemData(
        archipelago_id=item_base_offset + 29,
        classification=ItemClassification.progression,
        tags=(
            RivenAPTags.UNLOCK_ITEM,
            RivenAPTags.SURVEY_ITEM,
        ),
    ),
    RivenItems.SURVEY_GEHNS_SPY_ROOM_RIGHT_AQUARIUM_CHAIR_LEVER: RivenItemData(
        archipelago_id=item_base_offset + 30,
        classification=ItemClassification.progression,
        tags=(
            RivenAPTags.UNLOCK_ITEM,
            RivenAPTags.SURVEY_ITEM,
        ),
    ),
    RivenItems.SURVEY_UPPER_PLATEAU_GEHNTRIS_BOARD: RivenItemData(
        archipelago_id=item_base_offset + 31,
        classification=ItemClassification.progression,
        tags=(
            RivenAPTags.UNLOCK_ITEM,
            RivenAPTags.SURVEY_ITEM,
        ),
    ),
    RivenItems.SURVEY_MAGLEV_PLATFORM_TO_BOILER_DOOR_LEVER: RivenItemData(
        archipelago_id=item_base_offset + 32,
        classification=ItemClassification.progression,
        tags=(
            RivenAPTags.UNLOCK_ITEM,
            RivenAPTags.SURVEY_ITEM,
        ),
    ),
    RivenItems.PRISON_BEACH_LOG_TELESCOPE: RivenItemData(
        archipelago_id=item_base_offset + 33,
        classification=ItemClassification.progression,
        tags=(
            RivenAPTags.UNLOCK_ITEM,
            RivenAPTags.PRISON_ITEM,
        ),
    ),
    RivenItems.STARRY_MARBLE_DEVICES: RivenItemData(
        archipelago_id=item_base_offset + 34,
        classification=ItemClassification.progression,
        tags=(
            RivenAPTags.UNLOCK_ITEM,
            RivenAPTags.STARRY_ITEM,
        ),
    ),
    RivenItems.STARRY_JUNGLE_BRIDGE: RivenItemData(
        archipelago_id=item_base_offset + 35,
        classification=ItemClassification.progression,
        tags=(
            RivenAPTags.UNLOCK_ITEM,
            RivenAPTags.STARRY_ITEM,
        ),
    ),
    RivenItems.STARRY_BOILER_BRIDGE: RivenItemData(
        archipelago_id=item_base_offset + 36,
        classification=ItemClassification.progression,
        tags=(
            RivenAPTags.UNLOCK_ITEM,
            RivenAPTags.STARRY_ITEM,
        ),
    ),
    RivenItems.STARRY_SURVEY_BRIDGE: RivenItemData(
        archipelago_id=item_base_offset + 37,
        classification=ItemClassification.progression,
        tags=(
            RivenAPTags.UNLOCK_ITEM,
            RivenAPTags.STARRY_ITEM,
        ),
    ),
    # RivenItems.STARRY_PRISON_BRIDGE: RivenItemData(
    #     archipelago_id=item_base_offset + 38,
    #     classification=ItemClassification.progression,
    #     tags=(
    #         RivenAPTags.UNLOCK_ITEM,
    #         RivenAPTags.STARRY_ITEM,
    #     ),
    # ),
    RivenItems.MAGLEV_TEMPLE_JUNGLE_THROTTLE_LEVER: RivenItemData(
        archipelago_id=item_base_offset + 39,
        classification=ItemClassification.progression,
        tags=(
            RivenAPTags.UNLOCK_ITEM,
            RivenAPTags.MAGLEV_ITEM,
        ),
    ),
    RivenItems.MAGLEV_BOILER_SURVEY_THROTTLE_LEVER: RivenItemData(
        archipelago_id=item_base_offset + 40,
        classification=ItemClassification.progression,
        tags=(
            RivenAPTags.UNLOCK_ITEM,
            RivenAPTags.MAGLEV_ITEM,
        ),
    ),
    RivenItems.MAGLEV_SURVEY_JUNGLE_THROTTLE_LEVER: RivenItemData(
        archipelago_id=item_base_offset + 41,
        classification=ItemClassification.progression,
        tags=(
            RivenAPTags.UNLOCK_ITEM,
            RivenAPTags.MAGLEV_ITEM,
        ),
    ),
    RivenItems.SOLUTION_ANIMAL_CIRCLE: RivenItemData(
        archipelago_id=item_base_offset + 42,
        classification=ItemClassification.progression,
        tags=(
            RivenAPTags.SOLUTION_ITEM,
        ),
    ),
    RivenItems.SOLUTION_PRISON_ELEVATOR: RivenItemData(
        archipelago_id=item_base_offset + 43,
        classification=ItemClassification.progression,
        tags=(
            RivenAPTags.SOLUTION_ITEM,
        ),
    ),
    RivenItems.SOLUTION_BOLU_STICKS: RivenItemData(
        archipelago_id=item_base_offset + 44,
        classification=ItemClassification.progression,
        tags=(
            RivenAPTags.SOLUTION_ITEM,
        ),
    ),
    RivenItems.SOLUTION_GOLDEN_DOME_SLIDERS: RivenItemData(
        archipelago_id=item_base_offset + 45,
        classification=ItemClassification.progression,
        tags=(
            RivenAPTags.SOLUTION_ITEM,
        ),
    ),
    RivenItems.SOLUTION_STAR_FISSURE_TELESCOPE: RivenItemData(
        archipelago_id=item_base_offset + 46,
        classification=ItemClassification.progression,
        tags=(
            RivenAPTags.SOLUTION_ITEM,
        ),
    ),
    # Useful
    RivenItems.MOVEMENT_SPEED: RivenItemData(
        archipelago_id=item_base_offset + 100 + 1,
        classification=ItemClassification.useful,
        tags=(
            RivenAPTags.USEFUL_ITEM,
        ),
    ),
    # Traps
    RivenItems.TRAP_BLACK_AND_WHITE: RivenItemData(
        archipelago_id=item_base_offset + 200 + 1,
        classification=ItemClassification.trap,
        tags=(
            RivenAPTags.TRAP_ITEM,
        ),
    ),
    RivenItems.TRAP_BLOOM: RivenItemData(
        archipelago_id=item_base_offset + 200 + 2,
        classification=ItemClassification.trap,
        tags=(
            RivenAPTags.TRAP_ITEM,
        ),
    ),
    RivenItems.TRAP_CHROMATIC: RivenItemData(
        archipelago_id=item_base_offset + 200 + 3,
        classification=ItemClassification.trap,
        tags=(
            RivenAPTags.TRAP_ITEM,
        ),
    ),
    RivenItems.TRAP_COLOR_INVERSION: RivenItemData(
        archipelago_id=item_base_offset + 200 + 4,
        classification=ItemClassification.trap,
        tags=(
            RivenAPTags.TRAP_ITEM,
        ),
    ),
    RivenItems.TRAP_MOBILE_GAME: RivenItemData(
        archipelago_id=item_base_offset + 200 + 5,
        classification=ItemClassification.trap,
        tags=(
            RivenAPTags.TRAP_ITEM,
        ),
    ),
    RivenItems.TRAP_SLOW: RivenItemData(
        archipelago_id=item_base_offset + 200 + 6,
        classification=ItemClassification.trap,
        tags=(
            RivenAPTags.TRAP_ITEM,
        ),
    ),
    RivenItems.TRAP_TUNNEL_VISION: RivenItemData(
        archipelago_id=item_base_offset + 200 + 7,
        classification=ItemClassification.trap,
        tags=(
            RivenAPTags.TRAP_ITEM,
        ),
    ),
    # Filler
    RivenItems.VIAL_OF_WAHRK_GALL_INK: RivenItemData(
        archipelago_id=item_base_offset + 300 + 1,
        classification=ItemClassification.filler,
        tags=(
            RivenAPTags.FILLER_ITEM,
        ),
    ),
    RivenItems.SLIVER_OF_FIRE_MARBLE_GLASS: RivenItemData(
        archipelago_id=item_base_offset + 300 + 2,
        classification=ItemClassification.filler,
        tags=(
            RivenAPTags.FILLER_ITEM,
        ),
    ),
    RivenItems.FRACTURED_MAGLEV_FUSE: RivenItemData(
        archipelago_id=item_base_offset + 300 + 3,
        classification=ItemClassification.filler,
        tags=(
            RivenAPTags.FILLER_ITEM,
        ),
    ),
    RivenItems.MOIETY_DART_TIP_RESIN: RivenItemData(
        archipelago_id=item_base_offset + 300 + 4,
        classification=ItemClassification.filler,
        tags=(
            RivenAPTags.FILLER_ITEM,
        ),
    ),
    RivenItems.SCRAP_BOOK_BINDING_LEATHER: RivenItemData(
        archipelago_id=item_base_offset + 300 + 5,
        classification=ItemClassification.filler,
        tags=(
            RivenAPTags.FILLER_ITEM,
        ),
    ),
    RivenItems.CORRODED_BOILER_PRESSURE_GAUGE: RivenItemData(
        archipelago_id=item_base_offset + 300 + 6,
        classification=ItemClassification.filler,
        tags=(
            RivenAPTags.FILLER_ITEM,
        ),
    ),
    RivenItems.CARVED_REBEL_DAGGER: RivenItemData(
        archipelago_id=item_base_offset + 300 + 7,
        classification=ItemClassification.filler,
        tags=(
            RivenAPTags.FILLER_ITEM,
        ),
    ),
    RivenItems.GEHNS_FAILED_AGE_SURVEY_NOTES: RivenItemData(
        archipelago_id=item_base_offset + 300 + 8,
        classification=ItemClassification.filler,
        tags=(
            RivenAPTags.FILLER_ITEM,
        ),
    ),
    RivenItems.POLISHED_SUNNER_BONE_NEEDLE: RivenItemData(
        archipelago_id=item_base_offset + 300 + 9,
        classification=ItemClassification.filler,
        tags=(
            RivenAPTags.FILLER_ITEM,
        ),
    ),
    RivenItems.TARNISHED_SURVEY_SCOPE_LENS: RivenItemData(
        archipelago_id=item_base_offset + 300 + 10,
        classification=ItemClassification.filler,
        tags=(
            RivenAPTags.FILLER_ITEM,
        ),
    ),
}

from typing import Dict, List, Optional, Set

import collections
import logging
import time

from .enums import (
    RivenAPGoals,
    RivenAPStartingMovementSpeeds,
    RivenAPStartingRoutes,
    RivenAPTrapTypes,
    RivenItems,
    RivenLocations,
)

from .game_state_manager import GameStateManager, GameState


class GameController:
    logger: Optional[logging.Logger]

    game_state_manager: GameStateManager

    received_items: Dict[RivenItems, int]
    completed_locations: Set[RivenLocations]

    completed_locations_queue: collections.deque
    received_items_queue: collections.deque

    goal_completed: bool

    # Game State
    game_state: Optional[GameState]

    # Generation Options
    option_goal: Optional[RivenAPGoals]
    option_extra_progressive_star_fissure_telescope_solutions: Optional[int]
    option_starting_movement_speed: Optional[RivenAPStartingMovementSpeeds]
    option_progressive_movement_speed_item_count: Optional[int]
    option_trap_percentage: Optional[int]
    option_trap_weights: Optional[Dict[RivenAPTrapTypes, int]]
    option_trap_duration: Optional[int]

    # Generation Data
    selected_starting_route: Optional[RivenAPStartingRoutes]

    # State
    has_validated_jungle_village_water_hole: bool
    has_validated_boiler_turn_off_heat: bool

    should_prepare_processed_trap_counters: bool
    processed_trap_counters: Dict[RivenAPTrapTypes, int]
    active_trap_timestamps: Dict[RivenAPTrapTypes, Optional[int]]

    def __init__(self, logger: logging.Logger = None) -> None:
        self.logger = logger

        self.game_state_manager = GameStateManager()

        self.received_items = dict()
        self.completed_locations = set()

        self.completed_locations_queue = collections.deque()
        self.received_items_queue = collections.deque()

        self.goal_completed = False

        self.game_state = None

        self.option_goal = None
        self.option_extra_progressive_star_fissure_telescope_solutions = None
        self.option_starting_movement_speed = None
        self.option_progressive_movement_speed_item_count = None
        self.option_trap_percentage = None
        self.option_trap_weights = None
        self.option_trap_duration = None

        self.selected_starting_route = None

        self.has_validated_jungle_village_water_hole = False
        self.has_validated_boiler_turn_off_heat = False

        self.should_prepare_processed_trap_counters = True

        self.processed_trap_counters = {
            RivenAPTrapTypes.BLACK_AND_WHITE: 0,
            RivenAPTrapTypes.BLOOM: 0,
            RivenAPTrapTypes.CHROMATIC: 0,
            RivenAPTrapTypes.COLOR_INVERSION: 0,
            RivenAPTrapTypes.MOBILE_GAME: 0,
            RivenAPTrapTypes.SLOW: 0,
            RivenAPTrapTypes.TUNNEL_VISION: 0,
        }

        self.active_trap_timestamps = {
            RivenAPTrapTypes.BLACK_AND_WHITE: None,
            RivenAPTrapTypes.BLOOM: None,
            RivenAPTrapTypes.CHROMATIC: None,
            RivenAPTrapTypes.COLOR_INVERSION: None,
            RivenAPTrapTypes.MOBILE_GAME: None,
            RivenAPTrapTypes.SLOW: None,
            RivenAPTrapTypes.TUNNEL_VISION: None,
        }

    @property
    def engaged_instance_name_to_locations(self) -> Dict[str, RivenLocations]:
        return {
            "BP_RivenPuzzleLogic_C_3": RivenLocations.TEMPLE_PLATEAU_GAZE_STAR_FISSURE,
            "BeetleViewer_Engage_1": RivenLocations.TEMPLE_GATE_ROOM_BEETLE_1,
            "BeetleViewer_2_Engage": RivenLocations.TEMPLE_GATE_ROOM_BEETLE_2,
            "BeetleViewer_3_Engage": RivenLocations.TEMPLE_GATE_ROOM_BEETLE_3,
            "BeetleViewer_4_Engage": RivenLocations.TEMPLE_GATE_ROOM_BEETLE_4,
            "BeetleViewer_5_Engage": RivenLocations.TEMPLE_GATE_ROOM_BEETLE_5,
            "Engage_EyeWindow_Temple_2": RivenLocations.TEMPLE_GOLDEN_DOME_TEMPLE_SYMBOL,
            "Engage_EyeWindow_Jungle_1": RivenLocations.TEMPLE_GOLDEN_DOME_JUNGLE_SYMBOL,
            "Engage_EyeWindow_Boiler_4": RivenLocations.TEMPLE_GOLDEN_DOME_BOILER_SYMBOL,
            "Engage_EyeWindow_Survey_0": RivenLocations.TEMPLE_GOLDEN_DOME_SURVEY_SYMBOL,
            "Engage_EyeWindow_Prison_3": RivenLocations.TEMPLE_GOLDEN_DOME_PRISON_SYMBOL,
            "SpiderChairEngageRegion": RivenLocations.TEMPLE_PROJECTION_ROOM_SPIDER_CHAIR,
            "BP_EngageWindow_C_1": RivenLocations.JUNGLE_OUTSIDE_VILLAGE_SCHOOL_SIDE_GRAB_BBQ,
            "WahrkEffigyEngageRegion_0": RivenLocations.JUNGLE_VILLAGE_INHALE_STEAM,
            "BP_RivenPuzzleLogic_C_1": RivenLocations.JUNGLE_SCHOOLHOUSE_INSPECT_WAHRK_GAME,
            "TelescopePuzzleLogic": RivenLocations.PRISON_BEACH_LOOK_THROUGH_LOG_TELESCOPE,
            "BP_RivenPuzzleLogic6_2": RivenLocations.STARRY_CONTROLS_NAVIGATE_EXPANSE,
        }

    def log(self, message) -> None:
        if self.logger:
            self.logger.info(message)

    def log_debug(self, message) -> None:
        if self.logger:
            self.logger.debug(message)

    def open_process_handle(self) -> bool:
        return self.game_state_manager.open_process_handle()

    def close_process_handle(self) -> bool:
        return self.game_state_manager.close_process_handle()

    def is_process_running(self) -> bool:
        return self.game_state_manager.is_process_still_running()

    def update(self) -> None:
        if self.game_state_manager.is_process_still_running():
            try:
                self._refresh_game_state()

                if not self.game_state.is_valid:
                    return

                self._apply_permanent_game_state()
                self._apply_conditional_game_state()

                self._check_for_completed_locations()
                self._process_received_items()

                if (self.option_trap_percentage or 0) > 0:
                    self._manage_traps()

                self._check_for_victory()
            except Exception:
                import traceback

                with open("riven_errors.log", "a") as f:
                    f.write(traceback.format_exc() + "\n\n")

    def reset(self) -> None:
        self.received_items = dict()
        self.completed_locations = set()

        self.completed_locations_queue = collections.deque()
        self.received_items_queue = collections.deque()

        self.goal_completed = False

        self.game_state = None

        self.option_goal = None
        self.option_extra_progressive_star_fissure_telescope_solutions = None
        self.option_starting_movement_speed = None
        self.option_progressive_movement_speed_item_count = None
        self.option_trap_percentage = None
        self.option_trap_weights = None
        self.option_trap_duration = None

        self.selected_starting_route = None

        self.has_validated_jungle_village_water_hole = False
        self.has_validated_boiler_turn_off_heat = False

        self.should_prepare_processed_trap_counters = True

        self.processed_trap_counters = {
            RivenAPTrapTypes.BLACK_AND_WHITE: 0,
            RivenAPTrapTypes.BLOOM: 0,
            RivenAPTrapTypes.CHROMATIC: 0,
            RivenAPTrapTypes.COLOR_INVERSION: 0,
            RivenAPTrapTypes.MOBILE_GAME: 0,
            RivenAPTrapTypes.SLOW: 0,
            RivenAPTrapTypes.TUNNEL_VISION: 0,
        }

        self.active_trap_timestamps = {
            RivenAPTrapTypes.BLACK_AND_WHITE: None,
            RivenAPTrapTypes.BLOOM: None,
            RivenAPTrapTypes.CHROMATIC: None,
            RivenAPTrapTypes.COLOR_INVERSION: None,
            RivenAPTrapTypes.MOBILE_GAME: None,
            RivenAPTrapTypes.SLOW: None,
            RivenAPTrapTypes.TUNNEL_VISION: None,
        }

    def _refresh_game_state(self) -> None:
        self.game_state = self.game_state_manager.determine_game_state()

    def _apply_permanent_game_state(self) -> None:
        self.game_state_manager.lock_all_gate_room_levers()
        self.game_state_manager.lock_spider_chair_lever()
        self.game_state_manager.lock_upper_village_drawbridge_controls()
        self.game_state_manager.lock_lower_village_drawbridge_controls()
        self.game_state_manager.lock_village_podium_platform_crank()
        self.game_state_manager.lock_lab_catwalk_lock_lever()
        self.game_state_manager.lock_lab_maglev_lock_lever()
        self.game_state_manager.lock_jungle_bridge_crank()
        self.game_state_manager.lock_boiler_bridge_crank()
        self.game_state_manager.lock_survey_bridge_crank()
        self.game_state_manager.lock_prison_bridge_crank()

    def _apply_conditional_game_state(self) -> None:
        # Temple Gate Room Beetle Viewers
        item_count: int = self.received_items.get(RivenItems.TEMPLE_GATE_ROOM_BEETLE_VIEWERS, 0)

        if item_count > 0:
            self.game_state_manager.unlock_all_beetle_viewers()
        else:
            self.game_state_manager.lock_all_beetle_viewers()

        # Temple Gate Room Gate to Golden Dome
        item_count: int = self.received_items.get(RivenItems.TEMPLE_GATE_ROOM_GATE_GOLDEN_DOME, 0)

        if item_count > 0:
            self.game_state_manager.open_gate_to_golden_dome()

        # Temple Gate Room Gate to Spinning Dome
        item_count: int = self.received_items.get(RivenItems.TEMPLE_GATE_ROOM_GATE_SPINNING_DOME, 0)

        if item_count > 0:
            self.game_state_manager.open_gate_to_spinning_dome()

        # Temple Steam Control Room Steam Valve Lever
        item_count: int = self.received_items.get(RivenItems.TEMPLE_STEAM_CONTROL_STEAM_VALVE_LEVER, 0)

        if item_count > 0:
            self.game_state_manager.unlock_steam_control_room_lever()
        else:
            self.game_state_manager.lock_steam_control_room_lever()

        # Temple Projection Room Door
        item_count: int = self.received_items.get(RivenItems.TEMPLE_PROJECTION_ROOM_DOOR, 0)

        if item_count > 0:
            self.game_state_manager.unlock_projection_room_door()
        else:
            self.game_state_manager.lock_projection_room_door()

        # Jungle Village Upper Drawbridge
        item_count: int = self.received_items.get(RivenItems.JUNGLE_VILLAGE_UPPER_DRAWBRIDGE, 0)

        if item_count > 0:
            self.game_state_manager.lower_upper_village_drawbridge()
        else:
            self.game_state_manager.raise_upper_village_drawbridge()

        # Jungle Village Podium Platform
        item_count: int = self.received_items.get(RivenItems.JUNGLE_VILLAGE_PODIUM_PLATFORM, 0)

        if item_count > 0:
            self.game_state_manager.extend_podium_platform()
        else:
            self.game_state_manager.retract_podium_platform()

        # Jungle Village Lower Drawbridge
        item_count: int = self.received_items.get(RivenItems.JUNGLE_VILLAGE_LOWER_DRAWBRIDGE, 0)

        if item_count > 0:
            self.game_state_manager.lower_lower_village_drawbridge()
        else:
            self.game_state_manager.raise_lower_village_drawbridge()

        # Jungle Village Schoolhouse Door
        item_count: int = self.received_items.get(RivenItems.JUNGLE_VILLAGE_SCHOOLHOUSE_DOOR, 0)

        if item_count > 0:
            self.game_state_manager.unlock_village_school_door()
        else:
            self.game_state_manager.lock_village_school_door()

        # Jungle Woodcart Platform Levers
        item_count: int = self.received_items.get(RivenItems.JUNGLE_WOODCART_PLATFORM_WOODCART_LEVERS, 0)

        if item_count > 0:
            self.game_state_manager.unlock_woodcart_platform_levers()
        else:
            self.game_state_manager.lock_woodcart_platform_levers()

        # Jungle Blue Cave Bolu Sticks
        item_count: int = self.received_items.get(RivenItems.JUNGLE_BLUE_CAVE_BOLU_STICKS, 0)

        if item_count > 0:
            self.game_state_manager.enable_light_posts()
        else:
            self.game_state_manager.disable_light_posts()

        # Jungle Jungle Main Door
        item_count: int = self.received_items.get(RivenItems.JUNGLE_JUNGLE_MAIN_DOOR, 0)

        if item_count > 0:
            self.game_state_manager.unlock_jungle_main_door()
        else:
            self.game_state_manager.lock_jungle_main_door()

        # Jungle Jungle Side Door
        item_count: int = self.received_items.get(RivenItems.JUNGLE_JUNGLE_SIDE_DOOR, 0)

        if item_count > 0:
            self.game_state_manager.unlock_jungle_side_door()
        else:
            self.game_state_manager.lock_jungle_side_door()

        # Jungle Jungle Wahrk Elevator Lever
        item_count: int = self.received_items.get(RivenItems.JUNGLE_JUNGLE_WAHRK_ELEVATOR_LEVER, 0)

        if item_count > 0:
            self.game_state_manager.unlock_wahrk_elevator_lever()
        else:
            self.game_state_manager.lock_wahrk_elevator_lever()

        # Jungle Jungle Bone Throne Door
        item_count: int = self.received_items.get(RivenItems.JUNGLE_JUNGLE_BONE_THRONE_DOOR, 0)

        if item_count > 0:
            self.game_state_manager.unlock_bone_throne_door()
        else:
            self.game_state_manager.lock_bone_throne_door()

        # Jungle Submarine Cave Boarding Platform Lever
        item_count: int = self.received_items.get(RivenItems.JUNGLE_SUBMARINE_CAVE_BOARDING_PLATFORM_LEVER, 0)

        if item_count > 0:
            self.game_state_manager.unlock_submarine_cave_boarding_platform_lever()
        else:
            self.game_state_manager.lock_submarine_cave_boarding_platform_lever()

        # Jungle Wahrk Gallows Jail Cell Door Crank
        item_count: int = self.received_items.get(RivenItems.JUNGLE_WAHRK_GALLOWS_JAIL_CELL_DOOR_CRANK, 0)

        if item_count > 0:
            self.game_state_manager.unlock_wahrk_gallows_jail_cell_door_crank()
        else:
            self.game_state_manager.lock_wahrk_gallows_jail_cell_door_crank()

        # Jungle Secret Moiety Tunnel Secret Door
        item_count: int = self.received_items.get(RivenItems.JUNGLE_SECRET_MOIETY_TUNNEL_SECRET_DOOR, 0)

        if item_count > 0:
            self.game_state_manager.unlock_animal_circle_room_secret_door()
        else:
            self.game_state_manager.lock_animal_circle_room_secret_door()

        # Boiler Lake Steam Valve Lever
        item_count: int = self.received_items.get(RivenItems.BOILER_LAKE_STEAM_VALVE_LEVER, 0)

        if item_count > 0:
            self.game_state_manager.unlock_lake_steam_valve_lever()
        else:
            self.game_state_manager.lock_lake_steam_valve_lever()

        # Boiler Boiler Water Valve Lever
        item_count: int = self.received_items.get(RivenItems.BOILER_BOILER_WATER_VALVE_LEVER, 0)

        if item_count > 0:
            self.game_state_manager.unlock_boiler_water_valve_lever()
        else:
            self.game_state_manager.lock_boiler_water_valve_lever()

        # Boiler Mining Cave Water Pump Button
        item_count: int = self.received_items.get(RivenItems.BOILER_MINING_CAVE_WATER_PUMP_BUTTON, 0)

        if item_count > 0:
            self.game_state_manager.unlock_cave_pump_button()
        else:
            self.game_state_manager.lock_cave_pump_button()

        # Boiler Lab Elevator Cranks
        item_count: int = self.received_items.get(RivenItems.BOILER_LAB_ELEVATOR_CRANKS, 0)

        if item_count > 0:
            self.game_state_manager.unlock_lab_elevator_cranks()
        else:
            self.game_state_manager.lock_lab_elevator_cranks()

        # Boiler Lab Catwalk Door
        item_count: int = self.received_items.get(RivenItems.BOILER_LAB_CATWALK_DOOR, 0)

        if item_count > 0:
            self.game_state_manager.unlock_lab_catwalk_door()
        else:
            self.game_state_manager.lock_lab_catwalk_door()

        # Boiler Lab Maglev Door
        item_count: int = self.received_items.get(RivenItems.BOILER_LAB_MAGLEV_DOOR, 0)

        if item_count > 0:
            self.game_state_manager.unlock_lab_maglev_door()
        else:
            self.game_state_manager.lock_lab_maglev_door()

        # Boiler Lab Geode Cutter Crank
        item_count: int = self.received_items.get(RivenItems.BOILER_LAB_GEODE_CUTTER_CRANK, 0)

        if item_count > 0:
            self.game_state_manager.unlock_lab_press_crank()
        else:
            self.game_state_manager.lock_lab_press_crank()

        # Survey Plateau Elevator Buttons
        item_count: int = self.received_items.get(RivenItems.SURVEY_PLATEAU_ELEVATOR_BUTTONS, 0)

        if item_count > 0:
            self.game_state_manager.unlock_plateau_elevator_buttons()
        else:
            self.game_state_manager.lock_plateau_elevator_buttons()

        # Survey Gehn's Spy Room Left Aquarium Chair Lever
        item_count: int = self.received_items.get(RivenItems.SURVEY_GEHNS_SPY_ROOM_LEFT_AQUARIUM_CHAIR_LEVER, 0)

        if item_count > 0:
            self.game_state_manager.unlock_aquarium_chair_left_lever()
        else:
            self.game_state_manager.lock_aquarium_chair_left_lever()

        # Survey Gehn's Spy Room Right Aquarium Chair Lever
        item_count: int = self.received_items.get(RivenItems.SURVEY_GEHNS_SPY_ROOM_RIGHT_AQUARIUM_CHAIR_LEVER, 0)

        if item_count > 0:
            self.game_state_manager.unlock_aquarium_chair_right_lever()
        else:
            self.game_state_manager.lock_aquarium_chair_right_lever()

        # Survey Upper Plateau Gehntris Board
        item_count: int = self.received_items.get(RivenItems.SURVEY_UPPER_PLATEAU_GEHNTRIS_BOARD, 0)

        if item_count > 0:
            self.game_state_manager.unlock_gehntris_board()
        else:
            self.game_state_manager.lock_gehntris_board()

        # Survey Maglev Platform to Boiler Door Lever
        item_count: int = self.received_items.get(RivenItems.SURVEY_MAGLEV_PLATFORM_TO_BOILER_DOOR_LEVER, 0)

        if item_count > 0:
            self.game_state_manager.unlock_maglev_platform_to_boiler_door_lever()
        else:
            self.game_state_manager.lock_maglev_platform_to_boiler_door_lever()

        # Prison Beach Log Telescope
        item_count: int = self.received_items.get(RivenItems.PRISON_BEACH_LOG_TELESCOPE, 0)

        if item_count > 0:
            self.game_state_manager.unlock_log_telescope_lever()
        else:
            self.game_state_manager.lock_log_telescope_lever()

        # Starry Marble Devices
        item_count: int = self.received_items.get(RivenItems.STARRY_MARBLE_DEVICES, 0)

        if item_count > 0:
            self.game_state_manager.unlock_marble_devices()
        else:
            self.game_state_manager.lock_marble_devices()

        # Starry Jungle Bridge
        item_count: int = self.received_items.get(RivenItems.STARRY_JUNGLE_BRIDGE, 0)

        if item_count > 0:
            self.game_state_manager.extend_starry_expanse_jungle_bridge()
        else:
            self.game_state_manager.retract_starry_expanse_jungle_bridge()

        # Starry Boiler Bridge
        item_count: int = self.received_items.get(RivenItems.STARRY_BOILER_BRIDGE, 0)

        if item_count > 0:
            self.game_state_manager.extend_starry_expanse_boiler_bridge()
        else:
            self.game_state_manager.retract_starry_expanse_boiler_bridge()

        # Starry Survey Bridge
        item_count: int = self.received_items.get(RivenItems.STARRY_SURVEY_BRIDGE, 0)

        if item_count > 0:
            self.game_state_manager.extend_starry_expanse_survey_bridge()
        else:
            self.game_state_manager.retract_starry_expanse_survey_bridge()

        # Maglev Temple Jungle Throttle Lever
        item_count: int = self.received_items.get(RivenItems.MAGLEV_TEMPLE_JUNGLE_THROTTLE_LEVER, 0)

        if item_count > 0:
            self.game_state_manager.unlock_maglev_jungle_temple_throttle_lever()
        else:
            self.game_state_manager.lock_maglev_jungle_temple_throttle_lever()

        # Maglev Boiler Survey Throttle Lever
        item_count: int = self.received_items.get(RivenItems.MAGLEV_BOILER_SURVEY_THROTTLE_LEVER, 0)

        if item_count > 0:
            self.game_state_manager.unlock_maglev_boiler_survey_throttle_lever()
        else:
            self.game_state_manager.lock_maglev_boiler_survey_throttle_lever()

        # Maglev Survey Jungle Throttle Lever
        item_count: int = self.received_items.get(RivenItems.MAGLEV_SURVEY_JUNGLE_THROTTLE_LEVER, 0)

        if item_count > 0:
            self.game_state_manager.unlock_maglev_jungle_survey_throttle_lever()
        else:
            self.game_state_manager.lock_maglev_jungle_survey_throttle_lever()

        # Movement Speed
        if self.active_trap_timestamps[RivenAPTrapTypes.SLOW] is None:
            item_count: int = self.received_items.get(RivenItems.MOVEMENT_SPEED, 0)

            base_max_walk_speed: float = 400.0

            if self.option_starting_movement_speed == RivenAPStartingMovementSpeeds.SLOWER:
                base_max_walk_speed = 300.0
            elif self.option_starting_movement_speed == RivenAPStartingMovementSpeeds.FASTER:
                base_max_walk_speed = 500.0

            max_walk_speed: float = base_max_walk_speed + (item_count * 100.0)

            self.game_state_manager.set_max_walk_speed(max_walk_speed)

    def _check_for_completed_locations(self) -> None:
        checked_locations: List[RivenLocations] = list()

        if self.game_state.engaged_instance_name in self.engaged_instance_name_to_locations:
            location: RivenLocations = self.engaged_instance_name_to_locations[self.game_state.engaged_instance_name]

            if location == RivenLocations.STARRY_CONTROLS_NAVIGATE_EXPANSE:
                if self.game_state.returning_from_starry_expanse:
                    checked_locations.append(location)
            else:
                checked_locations.append(location)

        if self.game_state.reached_last_page_atrus_journal:
            checked_locations.append(RivenLocations.TEMPLE_PLATEAU_READ_ATRUS_JOURNAL)

        if self.game_state.telescope_lever_broken:
            checked_locations.append(RivenLocations.TEMPLE_PLATEAU_BREAK_TELESCOPE_LEVER)

        if self.game_state.looked_down_at_cho:
            checked_locations.append(RivenLocations.TEMPLE_PLATEAU_FIND_CHO)

        if not self.game_state.temple_old_gate_locked:
            checked_locations.append(RivenLocations.TEMPLE_PLATEAU_REMOVE_HINGE)

        if self.game_state.telescope_powered:
            checked_locations.append(RivenLocations.TEMPLE_STEAM_CONTROL_ROOM_POWER_TELESCOPE)

        if self.game_state.temple_fire_marble_dome_open:
            checked_locations.append(RivenLocations.TEMPLE_SPINNING_DOME_OPEN_DOME)

        if self.game_state.first_time_in_sub_dome:
            checked_locations.append(RivenLocations.TEMPLE_GOLDEN_DOME_ENTER_DOME)

        if self.game_state.spider_chair_door_location:
            checked_locations.append(RivenLocations.TEMPLE_PROJECTION_ROOM_ENTER_PROJECTION_ROOM)

        if self.game_state.bridge_collapsed:
            checked_locations.append(RivenLocations.TEMPLE_GOLDEN_DOME_COLLAPSE_BRIDGE)

        if self.game_state.maglev_temple_button_temple:
            checked_locations.append(RivenLocations.TEMPLE_MAGLEV_PLATFORM_TO_JUNGLE_PRESS_BUTTON)

        if self.game_state.sub_dome_elevator_location == 1:
            checked_locations.append(RivenLocations.TEMPLE_GOLDEN_DOME_UPPER_ACCESS_UPPER)

        if self.game_state.violet_marble_location == 0:
            checked_locations.append(RivenLocations.TEMPLE_GOLDEN_DOME_UPPER_PLACE_PURPLE_MARBLE)

        if self.game_state.green_marble_location == 3:
            checked_locations.append(RivenLocations.TEMPLE_GOLDEN_DOME_UPPER_PLACE_GREEN_MARBLE)

        if self.game_state.blue_marble_location == 4:
            checked_locations.append(RivenLocations.TEMPLE_GOLDEN_DOME_UPPER_PLACE_BLUE_MARBLE)

        if self.game_state.red_marble_location == 16:
            checked_locations.append(RivenLocations.TEMPLE_GOLDEN_DOME_UPPER_PLACE_RED_MARBLE)

        if self.game_state.orange_marble_location == 21:
            checked_locations.append(RivenLocations.TEMPLE_GOLDEN_DOME_UPPER_PLACE_ORANGE_MARBLE)

        if self.game_state.sub_dome_powered:
            checked_locations.append(RivenLocations.TEMPLE_GOLDEN_DOME_UPPER_ACCESS_AGE_233_BOOK)

        if self.game_state.first_time_on_jng:
            checked_locations.append(RivenLocations.JUNGLE_VISIT_VISIT_JUNGLE)

        if self.game_state.maglev_temple_button_jungle:
            checked_locations.append(RivenLocations.JUNGLE_MAGLEV_PLATFORM_TO_TEMPLE_PRESS_BUTTON)

        if self.game_state.rebel_viewer_collected:
            checked_locations.append(RivenLocations.JUNGLE_BEACH_COLLECT_MOIETY_LENS)

        if self.game_state.animal_totem_crank_rotation_wahrk != 30.0:
            checked_locations.append(RivenLocations.JUNGLE_WAHRK_TOTEM_INTERACT)

        if self.game_state.ytram_cave_water_diverter_location:
            checked_locations.append(RivenLocations.JUNGLE_WAHRK_TOTEM_DIVERT_WATER)

        if self.game_state.animal_totem_crank_rotation_scarab != 109.0:
            checked_locations.append(RivenLocations.JUNGLE_BEETLE_TOTEM_INTERACT)

        if self.game_state.animal_totem_crank_rotation_ytram != 240.0:
            checked_locations.append(RivenLocations.JUNGLE_YTRAM_TOTEM_INTERACT)

        if self.game_state.animal_totem_crank_rotation_butterfly != 160.0:
            checked_locations.append(RivenLocations.JUNGLE_INSECT_TOTEM_INTERACT)

        if self.game_state.hut_door_knocker_count > 0:
            checked_locations.append(RivenLocations.JUNGLE_VILLAGE_KNOCK_ON_DOOR)

        if self.game_state.cave_water_hole_active:
            checked_locations.append(RivenLocations.JUNGLE_VILLAGE_SHUT_STEAM_VENT)

        if self.game_state.beetle_tree_timer_count < 300:
            checked_locations.append(RivenLocations.JUNGLE_VILLAGE_PROVIDE_WATER_TO_TREE)

        if self.game_state.school_door_open:
            checked_locations.append(RivenLocations.JUNGLE_SCHOOLHOUSE_ENTER_SCHOOLHOUSE)

        if self.game_state.jungle_woodcart_call_button_pressed:
            checked_locations.append(RivenLocations.JUNGLE_WOODCART_PLATFORM_PRESS_BUTTON)

        if self.game_state.has_seen_guard_tower_a_siren_played:
            checked_locations.append(RivenLocations.JUNGLE_LOGGING_AREA_GET_SPOTTED_BY_GUARD)

        if self.game_state.blue_cave_puzzle_solved:
            checked_locations.append(RivenLocations.JUNGLE_BLUE_CAVE_OPEN_SECRET_DOOR)

        if self.game_state.wahrk_totem_mouth_open:
            checked_locations.append(RivenLocations.JUNGLE_WAHRK_ELEVATOR_OPEN_WAHRKS_MOUTH)

        if self.game_state.jungle_fire_marble_dome_open:
            checked_locations.append(RivenLocations.JUNGLE_JUNGLE_CATWALKS_OPEN_DOME)

        if self.game_state.gods_eye_view:
            checked_locations.append(RivenLocations.JUNGLE_BONE_THRONE_LOOK_DOWN_UPON_VILLAGE)

        if self.game_state.gallows_iris_open:
            checked_locations.append(RivenLocations.JUNGLE_BONE_THRONE_SEAL_WAHRK_GALLOWS)

        if self.game_state.maglev_jungle_button_jungle:
            checked_locations.append(RivenLocations.JUNGLE_MAGLEV_PLATFORM_TO_SURVEY_PRESS_BUTTON)

        if self.game_state.maglev_jungle_button_jungle_alt:
            checked_locations.append(RivenLocations.JUNGLE_MAGLEV_PLATFORM_TO_SURVEY_PRESS_OTHER_BUTTON)

        if self.game_state.sub_call_button_pressed:
            checked_locations.append(RivenLocations.JUNGLE_SUBMARINE_CAVE_PRESS_BUTTON)

        if self.game_state.player_engaging_sub:
            checked_locations.append(RivenLocations.JUNGLE_SUBMARINE_DESTINATION_SUBMARINE_CAVE_BOARD_SUBMARINE)

        if self.game_state.sub_location == 1:
            checked_locations.append(RivenLocations.JUNGLE_SUBMARINE_DESTINATION_WAHRK_GALLOWS_PILOT)
        elif self.game_state.sub_location == 2:
            checked_locations.append(RivenLocations.JUNGLE_SUBMARINE_DESTINATION_SCHOOLHOUSE_PILOT)
        elif self.game_state.sub_location == 3:
            checked_locations.append(RivenLocations.JUNGLE_SUBMARINE_DESTINATION_PODIUM_PILOT)
        elif self.game_state.sub_location == 4:
            checked_locations.append(RivenLocations.JUNGLE_SUBMARINE_DESTINATION_VILLAGE_PILOT)

        if self.game_state.should_hold_open_village_water_cavity:
            if self.has_validated_jungle_village_water_hole:
                checked_locations.append(RivenLocations.JUNGLE_VILLAGE_WATER_HOLE_FLICK_SWITCH)
        else:
            self.has_validated_jungle_village_water_hole = True

        if self.game_state.gallows_cell_secret_door_location:
            checked_locations.append(RivenLocations.JUNGLE_WAHRK_GALLOWS_JAIL_CELL_OPEN_SECRET_DOOR)

        if self.game_state.paddle_light_one_on:
            checked_locations.append(RivenLocations.JUNGLE_SECRET_MOIETY_TUNNEL_TURN_ON_LIGHT_1)

        if self.game_state.paddle_light_two_on:
            checked_locations.append(RivenLocations.JUNGLE_SECRET_MOIETY_TUNNEL_TURN_ON_LIGHT_2)

        if self.game_state.paddle_light_three_on:
            checked_locations.append(RivenLocations.JUNGLE_SECRET_MOIETY_TUNNEL_TURN_ON_LIGHT_3)

        if self.game_state.paddle_light_three_b_on:
            checked_locations.append(RivenLocations.JUNGLE_SECRET_MOIETY_TUNNEL_TURN_ON_LIGHT_4)

        if self.game_state.paddle_light_four_on:
            checked_locations.append(RivenLocations.JUNGLE_SECRET_MOIETY_TUNNEL_TURN_ON_LIGHT_5)

        if self.game_state.paddle_light_five_on:
            checked_locations.append(RivenLocations.JUNGLE_SECRET_MOIETY_TUNNEL_TURN_ON_LIGHT_6)

        if self.game_state.paddle_light_six_on:
            checked_locations.append(RivenLocations.JUNGLE_SECRET_MOIETY_TUNNEL_TURN_ON_LIGHT_7)

        if self.game_state.paddle_light_seven_on:
            checked_locations.append(RivenLocations.JUNGLE_SECRET_MOIETY_TUNNEL_TURN_ON_LIGHT_8)

        if self.game_state.secret_block_location < 0:
            checked_locations.append(RivenLocations.JUNGLE_SECRET_MOIETY_TUNNEL_OPEN_SECRET_DOOR)

        if self.game_state.animal_totem_successful:
            checked_locations.append(RivenLocations.JUNGLE_ANIMAL_CIRCLE_ROOM_ACCESS_TAY_BOOK)

        classic_animal_totem_1: bool = self.game_state.animal_totem_guess_one == 15
        classic_animal_totem_2: bool = self.game_state.animal_totem_guess_two == 10
        classic_animal_totem_3: bool = self.game_state.animal_totem_guess_three == 17
        classic_animal_totem_4: bool = self.game_state.animal_totem_guess_four == 3
        classic_animal_totem_5: bool = self.game_state.animal_totem_guess_five == 0

        if all([
            classic_animal_totem_1,
            classic_animal_totem_2,
            classic_animal_totem_3,
            classic_animal_totem_4,
            classic_animal_totem_5
        ]):
            checked_locations.append(RivenLocations.JUNGLE_ANIMAL_CIRCLE_ROOM_INPUT_CLASSIC_SOLUTION)

        if self.game_state.enter_boiler:
            checked_locations.append(RivenLocations.BOILER_VISIT_VISIT_BOILER)

        if self.game_state.boiler_woodcart_call_button_pressed:
            checked_locations.append(RivenLocations.BOILER_WOODCART_PLATFORM_PRESS_BUTTON)

        if self.game_state.woodcart_floor_open:
            checked_locations.append(RivenLocations.BOILER_WOODCART_PLATFORM_TURN_ON_WOOD_CHIPPER)

        if self.game_state.lake_steam_valve_location == 1:
            checked_locations.append(RivenLocations.BOILER_LAKE_DIRECT_STEAM_BOILER)
        elif self.game_state.lake_steam_valve_location == 2:
            checked_locations.append(RivenLocations.BOILER_LAKE_DIRECT_STEAM_WOOD_CHIPPER)

        if self.game_state.boiler_floor_actual_location == 1:
            checked_locations.append(RivenLocations.BOILER_BOILER_CONTROLS_RAISE_FLOOR)

        if self.game_state.boiler_water_lever_float == 0.0:
            checked_locations.append(RivenLocations.BOILER_BOILER_CONTROLS_DRAIN_WATER)

        if not self.game_state.prev_flame_lever_location:
            if self.has_validated_boiler_turn_off_heat:
                checked_locations.append(RivenLocations.BOILER_BOILER_CONTROLS_TURN_OFF_HEAT)
        else:
            self.has_validated_boiler_turn_off_heat = True

        if self.game_state.boiler_door_open:
            checked_locations.append(RivenLocations.BOILER_INSIDE_BOILER_ENTER_BOILER)

        if self.game_state.balcony_hatch_open:
            checked_locations.append(RivenLocations.BOILER_BALCONY_OPEN_HATCH)

        if self.game_state.furnace_door_location == 1:
            checked_locations.append(RivenLocations.BOILER_LAKE_DISCOVER_BURNT_BOOK)

        if self.game_state.boiler_fire_marble_dome_open:
            checked_locations.append(RivenLocations.BOILER_SPINNING_DOME_OPEN_DOME)

        if self.game_state.mining_cave_water_drained:
            checked_locations.append(RivenLocations.BOILER_MINING_CAVE_PUMP_SIDE_DRAIN_WATER)

        if self.game_state.fire_marble_location == 1:
            checked_locations.append(RivenLocations.BOILER_MINING_CAVE_PUMP_SIDE_MINE_FIRE_MARBLE_GEODE)

        if self.game_state.cart_slotted_into_elevator:
            checked_locations.append(RivenLocations.BOILER_MINING_CAVE_ELEVATOR_SIDE_SLOT_CART_IN_ELEVATOR)

        if self.game_state.player_visited_gehns_lab:
            checked_locations.append(RivenLocations.BOILER_LAB_VISIT_GEHNS_LAB)

        if self.game_state.reached_last_page_lab_journal:
            checked_locations.append(RivenLocations.BOILER_LAB_READ_GEHNS_JOURNAL)

        if not self.game_state.mag_glass_location:
            checked_locations.append(RivenLocations.BOILER_LAB_TRY_OUT_MAGNIFYING_GLASS)

        if self.game_state.book_press_crank_rotation == 1800.0:
            checked_locations.append(RivenLocations.BOILER_LAB_CLOSE_PRESS)

        if self.game_state.fire_marble_geode_cracked_open:
            checked_locations.append(RivenLocations.BOILER_LAB_CRACK_OPEN_FIRE_MARBLE_GEODE)

        if self.game_state.has_power_marble_setting:
            checked_locations.append(RivenLocations.BOILER_LAB_MEASURE_OPTIMAL_MARBLE_STRIKE_FORCE)

        if self.game_state.ytram_cinematic_played:
            checked_locations.append(RivenLocations.BOILER_LAB_FREE_YTRAM)

        if self.game_state.flywheel_speed >= 48.0:
            checked_locations.append(RivenLocations.BOILER_LAB_SPEED_UP_FLYWHEEL)

        if not self.game_state.fmf_left_lever:
            checked_locations.append(RivenLocations.BOILER_LAB_STOP_POLISHER)

        if self.game_state.maglev_boiler_button_boiler:
            checked_locations.append(RivenLocations.BOILER_MAGLEV_PLATFORM_TO_SURVEY_PRESS_BUTTON)

        if self.game_state.enter_survey:
            checked_locations.append(RivenLocations.SURVEY_VISIT_VISIT_SURVEY)

        if self.game_state.maglev_boiler_button_survey:
            checked_locations.append(RivenLocations.SURVEY_MAGLEV_PLATFORM_TO_BOILER_PRESS_BUTTON)

        if self.game_state.maglev_boiler_button_survey_alt:
            checked_locations.append(RivenLocations.SURVEY_MAGLEV_PLATFORM_TO_BOILER_PRESS_OTHER_BUTTON)

        if self.game_state.plateau_elevator_location == 0:
            checked_locations.append(RivenLocations.SURVEY_GEHNS_SPY_ROOM_DISCOVER_GEHNS_SPY_ROOM)

        if self.game_state.aquarium_chair_left_lever:
            if self.game_state.left_aquarium_chair_arm_active_view == 0:
                checked_locations.append(RivenLocations.SURVEY_GEHNS_SPY_ROOM_VIEW_PRISON_CAMERA)
            elif self.game_state.left_aquarium_chair_arm_active_view == 1:
                checked_locations.append(RivenLocations.SURVEY_GEHNS_SPY_ROOM_VIEW_JUNGLE_CAMERA)
            elif self.game_state.left_aquarium_chair_arm_active_view == 2:
                checked_locations.append(RivenLocations.SURVEY_GEHNS_SPY_ROOM_VIEW_SURVEY_CAMERA)
            elif self.game_state.left_aquarium_chair_arm_active_view == 3:
                checked_locations.append(RivenLocations.SURVEY_GEHNS_SPY_ROOM_VIEW_BOILER_CAMERA)
            elif self.game_state.left_aquarium_chair_arm_active_view == 4:
                checked_locations.append(RivenLocations.SURVEY_GEHNS_SPY_ROOM_VIEW_TEMPLE_CAMERA)

        if self.game_state.aquarium_chair_right_lever:
            if self.game_state.right_aquarium_chair_arm_active_light == 0:
                checked_locations.append(RivenLocations.SURVEY_GEHNS_SPY_ROOM_TURN_ON_BLUE_LIGHT)
            elif self.game_state.right_aquarium_chair_arm_active_light == 1:
                checked_locations.append(RivenLocations.SURVEY_GEHNS_SPY_ROOM_TURN_ON_GREEN_LIGHT)
            elif self.game_state.right_aquarium_chair_arm_active_light == 2:
                checked_locations.append(RivenLocations.SURVEY_GEHNS_SPY_ROOM_TURN_ON_YELLOW_LIGHT)
            elif self.game_state.right_aquarium_chair_arm_active_light == 3:
                checked_locations.append(RivenLocations.SURVEY_GEHNS_SPY_ROOM_TURN_ON_ORANGE_LIGHT)
            elif self.game_state.right_aquarium_chair_arm_active_light == 4:
                checked_locations.append(RivenLocations.SURVEY_GEHNS_SPY_ROOM_TURN_ON_RED_LIGHT)

        if self.game_state.wahrk_rammed_glass:
            checked_locations.append(RivenLocations.SURVEY_GEHNS_SPY_ROOM_ANNOY_WAHRK)

        if self.game_state.survey_fire_marble_dome_open:
            checked_locations.append(RivenLocations.SURVEY_UPPER_PLATEAU_OPEN_DOME)

        if self.game_state.temple_button_on:
            checked_locations.append(RivenLocations.SURVEY_UPPER_PLATEAU_PRESS_GEHNTRIS_TEMPLE_BUTTON)

        if self.game_state.jungle_button_on:
            checked_locations.append(RivenLocations.SURVEY_UPPER_PLATEAU_PRESS_GEHNTRIS_JUNGLE_BUTTON)

        if self.game_state.boiler_button_on:
            checked_locations.append(RivenLocations.SURVEY_UPPER_PLATEAU_PRESS_GEHNTRIS_BOILER_BUTTON)

        if self.game_state.survey_button_on:
            checked_locations.append(RivenLocations.SURVEY_UPPER_PLATEAU_PRESS_GEHNTRIS_SURVEY_BUTTON)

        if self.game_state.prison_button_on:
            checked_locations.append(RivenLocations.SURVEY_UPPER_PLATEAU_PRESS_GEHNTRIS_PRISON_BUTTON)

        if self.game_state.scribe_run_cinematic_played:
            checked_locations.append(RivenLocations.SURVEY_UNDERGROUND_TUNNEL_ENCOUNTER_GEHNS_SCRIBE)

        if self.game_state.maglev_jungle_button_survey:
            checked_locations.append(RivenLocations.SURVEY_MAGLEV_PLATFORM_TO_JUNGLE_PRESS_BUTTON)

        if self.game_state.enter_prison:
            checked_locations.append(RivenLocations.PRISON_VISIT_VISIT_PRISON)

        if self.game_state.prison_fire_marble_dome_open:
            checked_locations.append(RivenLocations.PRISON_SPINNING_DOME_OPEN_DOME)

        if self.game_state.animal_totem_crank_rotation_fish != 37.0:
            checked_locations.append(RivenLocations.PRISON_BEACH_INTERACT_TOTEM)

        if self.game_state.prison_telescope_rotated:
            checked_locations.append(RivenLocations.PRISON_BEACH_ROTATE_LOG_TELESCOPE)

        if self.game_state.player_visited_catherine_count > 0:
            checked_locations.append(RivenLocations.PRISON_OUTSIDE_JAIL_CELL_MEET_CATHERINE)

        if self.game_state.catherine_free_achievement:
            checked_locations.append(RivenLocations.PRISON_JAIL_CELL_FREE_CATHERINE)

        if self.game_state.player_moved_to_prison_cell:
            checked_locations.append(RivenLocations.AGE_OF_TAY_GET_IMPRISONED)

        if self.game_state.player_has_trap_book:
            checked_locations.append(RivenLocations.AGE_OF_TAY_GET_PRISON_BOOK_BACK)

        if self.game_state.reached_last_page_catherine_journal:
            checked_locations.append(RivenLocations.AGE_OF_TAY_READ_CATHERINES_JOURNAL)

        if self.game_state.has_player_left_tay_prison_cell:
            checked_locations.append(RivenLocations.AGE_OF_TAY_EXPLORE_HIVE)

        if self.game_state.has_met_gehn:
            checked_locations.append(RivenLocations.AGE_233_MEET_GEHN)

        if self.game_state.gehn_trapped:
            checked_locations.append(RivenLocations.AGE_233_TRAP_GEHN)

        if self.game_state.gehn_stove_on:
            checked_locations.append(RivenLocations.AGE_233_TURN_ON_STOVE)

        if self.game_state.gehn_cage_location == 1:
            checked_locations.append(RivenLocations.AGE_233_LOWER_CAGE)

        if self.game_state.spear_crank_rotation == 360.0:
            checked_locations.append(RivenLocations.AGE_233_GRAB_BBQ)

        if self.game_state.gehn_faucet_on:
            checked_locations.append(RivenLocations.AGE_233_TURN_ON_FAUCET)

        if self.game_state.has_seen_keta_vid:
            checked_locations.append(RivenLocations.AGE_233_WATCH_KETAS_PROJECTION)

        if self.game_state.reached_last_page_gehn_journal:
            checked_locations.append(RivenLocations.AGE_233_READ_GEHNS_JOURNAL)

        if self.game_state.player_has_prison_elevator_code:
            checked_locations.append(RivenLocations.AGE_233_LEARN_PRISON_ELEVATOR_CODE)

        if self.game_state.first_time_in_ste:
            checked_locations.append(RivenLocations.STARRY_VISIT_VISIT_STARRY)

        if self.game_state.green_power_marble_delivered:
            checked_locations.append(RivenLocations.STARRY_TEMPLE_DOME_DELIVER_GREEN_POWER_MARBLE)

        if self.game_state.red_power_marble_delivered:
            checked_locations.append(RivenLocations.STARRY_JUNGLE_DOME_DELIVER_RED_POWER_MARBLE)

        if self.game_state.violet_power_marble_delivered:
            checked_locations.append(RivenLocations.STARRY_BOILER_DOME_DELIVER_PURPLE_POWER_MARBLE)

        if self.game_state.orange_power_marble_delivered:
            checked_locations.append(RivenLocations.STARRY_SURVEY_DOME_DELIVER_ORANGE_POWER_MARBLE)

        if self.game_state.blue_power_marble_delivered:
            checked_locations.append(RivenLocations.STARRY_PRISON_DOME_DELIVER_BLUE_POWER_MARBLE)

        location: RivenLocations
        for location in checked_locations:
            if location not in self.completed_locations and location not in self.completed_locations_queue:
                self.completed_locations.add(location)
                self.completed_locations_queue.append(location)

    def _process_received_items(self) -> None:
        while len(self.received_items_queue) > 0:
            item: RivenItems = self.received_items_queue.popleft()

            if item not in self.received_items:
                self.received_items[item] = 0

            self.received_items[item] += 1

        if self.should_prepare_processed_trap_counters:
            self.should_prepare_processed_trap_counters = False

            item: RivenItems
            item_count: int
            for item, item_count in self.received_items.items():
                if item.value.endswith(" Trap"):
                    self.processed_trap_counters[RivenAPTrapTypes(item.value)] = item_count

    def _manage_traps(self) -> None:
        if not self.game_state.is_valid:
            return

        if self.game_state.player_is_engaged:
            return

        now_timestamp: int = int(time.time())

        trap_type: RivenAPTrapTypes
        expiry_timestamp: int
        for trap_type, expiry_timestamp in self.active_trap_timestamps.items():
            if expiry_timestamp is not None:
                if now_timestamp >= expiry_timestamp:
                    if trap_type == RivenAPTrapTypes.BLACK_AND_WHITE:
                        self.game_state_manager.disable_black_and_white_trap()
                    elif trap_type == RivenAPTrapTypes.BLOOM:
                        self.game_state_manager.disable_bloom_trap()
                    elif trap_type == RivenAPTrapTypes.CHROMATIC:
                        self.game_state_manager.disable_chromatic_trap()
                    elif trap_type == RivenAPTrapTypes.COLOR_INVERSION:
                        self.game_state_manager.disable_color_inversion_trap()
                    elif trap_type == RivenAPTrapTypes.MOBILE_GAME:
                        self.game_state_manager.disable_mobile_game_trap()
                    elif trap_type == RivenAPTrapTypes.SLOW:
                        self.game_state_manager.disable_slow_trap()
                    elif trap_type == RivenAPTrapTypes.TUNNEL_VISION:
                        self.game_state_manager.disable_tunnel_vision_trap()

                    self.active_trap_timestamps[trap_type] = None

        item: RivenItems
        item_count: int
        for item, item_count in self.received_items.items():
            if item.value.endswith(" Trap"):
                trap_type: RivenAPTrapTypes = RivenAPTrapTypes(item.value)

                if item_count > self.processed_trap_counters[trap_type]:
                    expiry_timestamp: int = int(time.time()) + self.option_trap_duration

                    if trap_type == RivenAPTrapTypes.BLACK_AND_WHITE:
                        if self.active_trap_timestamps[trap_type] is None:
                            if self.game_state_manager.enable_black_and_white_trap():
                                self.active_trap_timestamps[trap_type] = expiry_timestamp
                                self.processed_trap_counters[trap_type] += 1
                    elif trap_type == RivenAPTrapTypes.BLOOM:
                        if self.active_trap_timestamps[trap_type] is None:
                            if self.game_state_manager.enable_bloom_trap():
                                self.active_trap_timestamps[trap_type] = expiry_timestamp
                                self.processed_trap_counters[trap_type] += 1
                    elif trap_type == RivenAPTrapTypes.CHROMATIC:
                        if self.active_trap_timestamps[trap_type] is None:
                            if self.game_state_manager.enable_chromatic_trap():
                                self.active_trap_timestamps[trap_type] = expiry_timestamp
                                self.processed_trap_counters[trap_type] += 1
                    elif trap_type == RivenAPTrapTypes.COLOR_INVERSION:
                        if self.active_trap_timestamps[trap_type] is None:
                            if self.game_state_manager.enable_color_inversion_trap():
                                self.active_trap_timestamps[trap_type] = expiry_timestamp
                                self.processed_trap_counters[trap_type] += 1
                    elif trap_type == RivenAPTrapTypes.MOBILE_GAME:
                        if self.active_trap_timestamps[trap_type] is None:
                            if self.game_state_manager.enable_mobile_game_trap():
                                self.active_trap_timestamps[trap_type] = expiry_timestamp
                                self.processed_trap_counters[trap_type] += 1
                    elif trap_type == RivenAPTrapTypes.SLOW:
                        if self.active_trap_timestamps[trap_type] is None:
                            if self.game_state_manager.enable_slow_trap():
                                self.active_trap_timestamps[trap_type] = expiry_timestamp
                                self.processed_trap_counters[trap_type] += 1
                    elif trap_type == RivenAPTrapTypes.TUNNEL_VISION:
                        if self.active_trap_timestamps[trap_type] is None:
                            if self.game_state_manager.enable_tunnel_vision_trap():
                                self.active_trap_timestamps[trap_type] = expiry_timestamp
                                self.processed_trap_counters[trap_type] += 1

    def _check_for_victory(self) -> None:
        if self.option_goal == RivenAPGoals.GOOD_ENDING:
            if self.game_state.good_ending_achievement:
                self.goal_completed = True
        elif self.option_goal == RivenAPGoals.STAR_FISSURE:
            if self.game_state.bad_fissure_ending:
                self.goal_completed = True

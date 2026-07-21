from typing import Any, Dict, List, NamedTuple, Optional, Tuple

import ctypes
import struct
import time

import pymem.process
import pymem.ressources.structure

from pymem import Pymem


class GameState(NamedTuple):
    is_valid: bool

    animal_totem_crank_rotation_butterfly: Optional[float] = None
    animal_totem_crank_rotation_fish: Optional[float] = None
    animal_totem_crank_rotation_scarab: Optional[float] = None
    animal_totem_crank_rotation_wahrk: Optional[float] = None
    animal_totem_crank_rotation_ytram: Optional[float] = None
    animal_totem_guess_five: Optional[int] = None
    animal_totem_guess_four: Optional[int] = None
    animal_totem_guess_one: Optional[int] = None
    animal_totem_guess_three: Optional[int] = None
    animal_totem_guess_two: Optional[int] = None
    animal_totem_solution_index: Optional[int] = None
    animal_totem_solution_five: Optional[int] = None
    animal_totem_solution_four: Optional[int] = None
    animal_totem_solution_one: Optional[int] = None
    animal_totem_solution_six: Optional[int] = None
    animal_totem_solution_three: Optional[int] = None
    animal_totem_solution_two: Optional[int] = None
    animal_totem_successful: Optional[bool] = None
    aquarium_chair_left_lever: Optional[bool] = None
    aquarium_chair_right_lever: Optional[bool] = None
    bad_fissure_ending: Optional[bool] = None
    balcony_hatch_open: Optional[bool] = None
    beetle_tree_timer_count: Optional[int] = None
    blue_cave_puzzle_solved: Optional[bool] = None
    blue_cave_solution_index: Optional[int] = None
    blue_marble_location: Optional[int] = None
    blue_power_marble_delivered: Optional[bool] = None
    boiler_button_on: Optional[bool] = None
    boiler_door_open: Optional[bool] = None
    boiler_fire_marble_dome_open: Optional[bool] = None
    boiler_floor_actual_location: Optional[int] = None
    boiler_water_lever_float: Optional[float] = None
    boiler_woodcart_call_button_pressed: Optional[bool] = None
    book_press_crank_rotation: Optional[float] = None
    bridge_collapsed: Optional[bool] = None
    cart_slotted_into_elevator: Optional[bool] = None
    catherine_free_achievement: Optional[bool] = None
    cave_water_hole_active: Optional[bool] = None
    elevator_solution_five: Optional[int] = None
    elevator_solution_four: Optional[int] = None
    elevator_solution_one: Optional[int] = None
    elevator_solution_three: Optional[int] = None
    elevator_solution_two: Optional[int] = None
    engaged_instance_name: Optional[str] = None
    enter_boiler: Optional[bool] = None
    enter_prison: Optional[bool] = None
    enter_survey: Optional[bool] = None
    fire_marble_geode_cracked_open: Optional[bool] = None
    fire_marble_location: Optional[int] = None
    first_time_in_ste: Optional[bool] = None
    first_time_in_sub_dome: Optional[bool] = None
    first_time_on_jng: Optional[bool] = None
    flywheel_speed: Optional[float] = None
    fmf_left_lever: Optional[bool] = None
    furnace_door_location: Optional[int] = None
    gallows_cell_secret_door_location: Optional[bool] = None
    gallows_iris_open: Optional[bool] = None
    gate_room_rotation: Optional[float] = None
    gehn_cage_location: Optional[int] = None
    gehn_faucet_on: Optional[bool] = None
    gehn_stove_on: Optional[bool] = None
    gehn_trapped: Optional[bool] = None
    gods_eye_view: Optional[bool] = None
    good_ending_achievement: Optional[bool] = None
    green_marble_location: Optional[int] = None
    green_power_marble_delivered: Optional[bool] = None
    has_met_gehn: Optional[bool] = None
    has_player_left_tay_prison_cell: Optional[bool] = None
    has_power_marble_setting: Optional[bool] = None
    has_seen_guard_tower_a_siren_played: Optional[bool] = None
    has_seen_keta_vid: Optional[bool] = None
    hut_door_knocker_count: Optional[int] = None
    jungle_button_on: Optional[bool] = None
    jungle_fire_marble_dome_open: Optional[bool] = None
    jungle_woodcart_call_button_pressed: Optional[bool] = None
    lake_steam_valve_location: Optional[int] = None
    left_aquarium_chair_arm_active_view: Optional[int] = None
    light_post_solution_1: Optional[int] = None
    light_post_solution_2: Optional[int] = None
    light_post_solution_3: Optional[int] = None
    looked_down_at_cho: Optional[bool] = None
    mag_glass_location: Optional[bool] = None
    maglev_boiler_button_boiler: Optional[bool] = None
    maglev_boiler_button_survey: Optional[bool] = None
    maglev_boiler_button_survey_alt: Optional[bool] = None
    maglev_jungle_button_jungle: Optional[bool] = None
    maglev_jungle_button_jungle_alt: Optional[bool] = None
    maglev_jungle_button_survey: Optional[bool] = None
    maglev_temple_button_temple: Optional[bool] = None
    maglev_temple_button_jungle: Optional[bool] = None
    mining_cave_water_drained: Optional[bool] = None
    orange_marble_location: Optional[int] = None
    orange_power_marble_delivered: Optional[bool] = None
    paddle_light_five_on: Optional[bool] = None
    paddle_light_four_on: Optional[bool] = None
    paddle_light_one_on: Optional[bool] = None
    paddle_light_seven_on: Optional[bool] = None
    paddle_light_six_on: Optional[bool] = None
    paddle_light_three_b_on: Optional[bool] = None
    paddle_light_three_on: Optional[bool] = None
    paddle_light_two_on: Optional[bool] = None
    plateau_elevator_location: Optional[int] = None
    player_engaging_sub: Optional[bool] = None
    player_has_prison_elevator_code: Optional[bool] = None
    player_has_trap_book: Optional[bool] = None
    player_is_engaged: Optional[bool] = None
    player_moved_to_prison_cell: Optional[bool] = None
    player_visited_catherine_count: Optional[int] = None
    player_visited_gehns_lab: Optional[bool] = None
    prev_flame_lever_location: Optional[bool] = None
    prison_button_on: Optional[bool] = None
    prison_fire_marble_dome_open: Optional[bool] = None
    prison_telescope_rotated: Optional[bool] = None
    reached_last_page_atrus_journal: Optional[bool] = None
    reached_last_page_catherine_journal: Optional[bool] = None
    reached_last_page_gehn_journal: Optional[bool] = None
    reached_last_page_lab_journal: Optional[bool] = None
    rebel_viewer_collected: Optional[bool] = None
    red_marble_location: Optional[int] = None
    red_power_marble_delivered: Optional[bool] = None
    returning_from_starry_expanse: Optional[bool] = None
    right_aquarium_chair_arm_active_light: Optional[int] = None
    school_door_open: Optional[bool] = None
    scribe_run_cinematic_played: Optional[bool] = None
    secret_block_location: Optional[int] = None
    should_hold_open_village_water_cavity: Optional[bool] = None
    slider_offset_solution_index: Optional[int] = None
    slider_solution_blue: Optional[int] = None
    slider_solution_green: Optional[int] = None
    slider_solution_orange: Optional[int] = None
    slider_solution_red: Optional[int] = None
    slider_solution_violet: Optional[int] = None
    spear_crank_rotation: Optional[float] = None
    spider_chair_door_location: Optional[bool] = None
    sub_call_button_pressed: Optional[bool] = None
    sub_dome_elevator_location: Optional[int] = None
    sub_dome_powered: Optional[bool] = None
    sub_location: Optional[int] = None
    survey_button_on: Optional[bool] = None
    survey_fire_marble_dome_open: Optional[bool] = None
    telescope_lever_broken: Optional[bool] = None
    telescope_powered: Optional[bool] = None
    telescope_solution_eight: Optional[int] = None
    telescope_solution_five: Optional[int] = None
    telescope_solution_four: Optional[int] = None
    telescope_solution_nine: Optional[int] = None
    telescope_solution_one: Optional[int] = None
    telescope_solution_seven: Optional[int] = None
    telescope_solution_six: Optional[int] = None
    telescope_solution_ten: Optional[int] = None
    telescope_solution_three: Optional[int] = None
    telescope_solution_two: Optional[int] = None
    temple_button_on: Optional[bool] = None
    temple_fire_marble_dome_open: Optional[bool] = None
    temple_maglev_intro_was_fired: Optional[bool] = None
    temple_old_gate_locked: Optional[bool] = None
    violet_marble_location: Optional[int] = None
    violet_power_marble_delivered: Optional[bool] = None
    wahrk_rammed_glass: Optional[bool] = None
    wahrk_totem_mouth_open: Optional[bool] = None
    woodcart_floor_open: Optional[bool] = None
    ytram_cave_water_diverter_location: Optional[bool] = None
    ytram_cinematic_played: Optional[bool] = None


class GameStateManager:
    process_name: str = "Riven-Win64-Shipping.exe"

    gnames_offset: int = 0x7D96E40
    gobjects_offset: int = 0x7E3D770
    gworld_offset: int = 0x7FAFC08

    process_event_offset: int = 0xF3DAD0
    process_event_vtable_index: int = 0x4D

    process: Optional[Pymem]
    is_process_running: bool

    gnames_mapping: Dict[int, str]
    gnames_mapping_reverse: Dict[str, int]

    gobjects_name_to_object: Dict[str, List[Dict[str, Any]]]
    gobjects_address_to_object: Dict[int, Dict[str, Any]]

    next_allowed_unknown_object_restart: Optional[int]

    last_seen_levels_array_pointer_bytes: bytes
    next_forced_gobjects_refresh: int

    has_wiggled_upper_village_drawbridge: bool
    has_wiggled_lower_village_drawbridge: bool

    game_state: Optional[GameState]

    def __init__(self) -> None:
        self.process = None
        self.is_process_running = False

        self.gnames_mapping = dict()
        self.gnames_mapping_reverse = dict()

        self.gobjects_name_to_object = dict()
        self.gobjects_address_to_object = dict()

        self.next_allowed_unknown_object_restart = None

        self.last_seen_levels_array_pointer_bytes = b""
        self.next_forced_gobjects_refresh = 0

        self.has_wiggled_upper_village_drawbridge = False
        self.has_wiggled_lower_village_drawbridge = False

        self.game_state = GameState(is_valid=False)

    def open_process_handle(self) -> bool:
        try:
            self.process = Pymem(self.process_name)
            self.is_process_running = True

            self._generate_gnames_mapping()

            self.gnames_mapping_reverse = {v: k for k, v in self.gnames_mapping.items()}

            self._refresh_gobjects_mapping()
        except Exception:
            return False

        return True

    def close_process_handle(self) -> bool:
        if pymem.process.close_handle(self.process.process_handle):
            self.is_process_running = False
            self.process = None

            self.gnames_mapping = dict()
            self.gnames_mapping_reverse = dict()

            self.gobjects_name_to_object = dict()
            self.gobjects_address_to_object = dict()

            self.next_allowed_unknown_object_restart = None

            self.last_seen_levels_array_pointer_bytes = b""
            self.next_forced_gobjects_refresh = 0

            self.has_wiggled_upper_village_drawbridge = False
            self.has_wiggled_lower_village_drawbridge = False

            self.game_state = GameState(is_valid=False)

            return True

        return False

    def is_process_still_running(self) -> bool:
        try:
            self.process.read_int(self.process.base_address)
        except Exception:
            self.is_process_running = False
            self.process = None

            self.gnames_mapping = dict()
            self.gnames_mapping_reverse = dict()

            self.gobjects_name_to_object = dict()
            self.gobjects_address_to_object = dict()

            self.next_allowed_unknown_object_restart = None

            self.last_seen_levels_array_pointer_bytes = b""
            self.next_forced_gobjects_refresh = 0

            self.has_wiggled_upper_village_drawbridge = False
            self.has_wiggled_lower_village_drawbridge = False

            self.game_state = GameState(is_valid=False)

            return False

        return True

    def determine_game_state(self) -> GameState:
        if not self.is_process_running:
            return GameState(is_valid=False)

        self._refresh_gobjects_mapping()

        riven_game_state_address: int = self._resolve_address(self.gworld_offset, (0x170, 0x0))

        if riven_game_state_address in (0, None):
            return GameState(is_valid=False)

        internal_game_state: Dict[str, Any] = dict()

        internal_game_state.update(self._determine_game_state_bools(riven_game_state_address + 0x4F8))
        internal_game_state.update(self._determine_game_state_ints(riven_game_state_address + 0x548))
        internal_game_state.update(self._determine_game_state_floats(riven_game_state_address + 0x5E8))

        plateau_elevator_location: int = internal_game_state.get("PlateauElevatorLocation", 1)

        if internal_game_state.get("FirstStepInRiven", False) is False:
            return GameState(is_valid=False)
        # Transitions to Starry Expanse
        elif internal_game_state.get("ReturningFromStarryExpanse", True) is True and self.game_state.returning_from_starry_expanse is False:
            time.sleep(2)

            self.close_process_handle()
            self.open_process_handle()

            return GameState(is_valid=False)
        elif internal_game_state.get("ReturningFromStarryExpanse", False) is False and self.game_state.returning_from_starry_expanse is True:
            time.sleep(2)

            self.close_process_handle()
            self.open_process_handle()

            return GameState(is_valid=False)
        # Transitions to Gehn's Spy Room
        elif plateau_elevator_location == 1 and self.game_state.plateau_elevator_location == 0:
            time.sleep(2)

            self.close_process_handle()
            self.open_process_handle()

            return GameState(is_valid=False)
        elif plateau_elevator_location == 0 and self.game_state.plateau_elevator_location == 1:
            time.sleep(2)

            self.close_process_handle()
            self.open_process_handle()

            return GameState(is_valid=False)
        # Monitor for Unknown Object presence. Restart and apply cooldown if found
        elif "Unknown Object" in self.gobjects_name_to_object:
            now_timestamp: int = int(time.time())

            if self.next_allowed_unknown_object_restart is None or now_timestamp > self.next_allowed_unknown_object_restart:
                time.sleep(2)

                self.close_process_handle()
                self.open_process_handle()

                self.next_allowed_unknown_object_restart = now_timestamp + 60

                return GameState(is_valid=False)

        player_is_engaged: Optional[bool] = self._get_player_is_engaged()
        engaged_instance_name: Optional[str] = self._get_engaged_instance_name()

        left_aquarium_chair_arm_active_view: Optional[int] = self._get_left_aquarium_chair_arm_active_view()
        right_aquarium_chair_arm_active_light: Optional[int] = self._get_right_aquarium_chair_arm_active_light()

        self.game_state = GameState(
            is_valid=True,
            animal_totem_crank_rotation_butterfly=internal_game_state.get("AnimalTotemCrankRotation_Butterfly", 160.0),
            animal_totem_crank_rotation_fish=internal_game_state.get("AnimalTotemCrankRotation_Fish", 37.0),
            animal_totem_crank_rotation_scarab=internal_game_state.get("AnimalTotemCrankRotation_Scarab", 109.0),
            animal_totem_crank_rotation_wahrk=internal_game_state.get("AnimalTotemCrankRotation_Wahrk", 30.0),
            animal_totem_crank_rotation_ytram=internal_game_state.get("AnimalTotemCrankRotation_Ytram", 240.0),
            animal_totem_guess_five=internal_game_state.get("AnimalTotemGuessFive", 0),
            animal_totem_guess_four=internal_game_state.get("AnimalTotemGuessFour", 0),
            animal_totem_guess_one=internal_game_state.get("AnimalTotemGuessOne", 0),
            animal_totem_guess_three=internal_game_state.get("AnimalTotemGuessThree", 0),
            animal_totem_guess_two=internal_game_state.get("AnimalTotemGuessTwo", 0),
            animal_totem_solution_index=internal_game_state.get("AnimalTotemSolutionIndex", 0),
            animal_totem_solution_five=internal_game_state.get("AnimalTotemSolutionFive", 0),
            animal_totem_solution_four=internal_game_state.get("AnimalTotemSolutionFour", 0),
            animal_totem_solution_one=internal_game_state.get("AnimalTotemSolutionOne", 0),
            animal_totem_solution_six=internal_game_state.get("AnimalTotemSolutionSix", 0),
            animal_totem_solution_three=internal_game_state.get("AnimalTotemSolutionThree", 0),
            animal_totem_solution_two=internal_game_state.get("AnimalTotemSolutionTwo", 0),
            animal_totem_successful=internal_game_state.get("AnimalTotemSuccessful", False),
            aquarium_chair_left_lever=internal_game_state.get("AquariumChairLeftLever", False),
            aquarium_chair_right_lever=internal_game_state.get("AquariumChairRightLever", False),
            bad_fissure_ending=internal_game_state.get("BadFissureEnding", False),
            balcony_hatch_open=internal_game_state.get("BalconyHatchOpen", False),
            beetle_tree_timer_count=internal_game_state.get("BeetleTreeTimerCount", 300),
            blue_cave_puzzle_solved=internal_game_state.get("BlueCavePuzzleSolved", False),
            blue_cave_solution_index=internal_game_state.get("BlueCaveSolutionIndex", 0),
            blue_marble_location=internal_game_state.get("BlueMarbleLocation", -1),
            blue_power_marble_delivered=internal_game_state.get("BluePowermarbleDelivered", False),
            boiler_button_on=internal_game_state.get("BoilerButtonOn", False),
            boiler_door_open=internal_game_state.get("BoilerDoorOpen", False),
            boiler_fire_marble_dome_open=internal_game_state.get("BoilerFiremarbleDomeOpen", False),
            boiler_floor_actual_location=internal_game_state.get("BoilerFloorActualLocation", 0),
            boiler_water_lever_float=internal_game_state.get("BoilerWaterLeverFloat", 1.0),
            boiler_woodcart_call_button_pressed=internal_game_state.get("BoilerWoodcartCallButtonPressed", False),
            book_press_crank_rotation=internal_game_state.get("BookPressCrankRotation", 0.0),
            bridge_collapsed=internal_game_state.get("BridgeCollapsed", False),
            cart_slotted_into_elevator=internal_game_state.get("CartSlottedIntoElevator", False),
            catherine_free_achievement=internal_game_state.get("CatherineFreeAchievement", False),
            cave_water_hole_active=internal_game_state.get("CaveWaterHoleActive", False),
            elevator_solution_five=internal_game_state.get("ElevatorSolutionFive", 1),
            elevator_solution_four=internal_game_state.get("ElevatorSolutionFour", 1),
            elevator_solution_one=internal_game_state.get("ElevatorSolutionOne", 1),
            elevator_solution_three=internal_game_state.get("ElevatorSolutionThree", 1),
            elevator_solution_two=internal_game_state.get("ElevatorSolutionTwo", 1),
            engaged_instance_name=engaged_instance_name,
            enter_boiler=internal_game_state.get("EnterBoiler", False),
            enter_prison=internal_game_state.get("EnterPrison", False),
            enter_survey=internal_game_state.get("EnterSurvey", False),
            fire_marble_geode_cracked_open=internal_game_state.get("FiremarbleGeodeCrackedOpen", False),
            fire_marble_location=internal_game_state.get("FiremarbleLocation", 0),
            first_time_in_ste=internal_game_state.get("FirstTimeInSTE", False),
            first_time_in_sub_dome=internal_game_state.get("FirstTimeInSubDome", False),
            first_time_on_jng=internal_game_state.get("FirstTimeOnJNG", False),
            flywheel_speed=internal_game_state.get("FlyWheelSpeed", 0.0),
            fmf_left_lever=internal_game_state.get("FMFLeftLever", True),
            furnace_door_location=internal_game_state.get("FurnaceDoorLocation", 0),
            gallows_cell_secret_door_location=internal_game_state.get("GallowsCellSecretDoorLocation", False),
            gallows_iris_open=internal_game_state.get("GallowsIrisOpen", False),
            gate_room_rotation=internal_game_state.get("GateroomRotation", 144.0),
            gehn_cage_location=internal_game_state.get("GehnCageLocation", 0),
            gehn_faucet_on=internal_game_state.get("GehnFaucetOn", False),
            gehn_stove_on=internal_game_state.get("GehnStoveOn", False),
            gehn_trapped=internal_game_state.get("GehnTrapped", False),
            gods_eye_view=internal_game_state.get("GodsEyeView", False),
            good_ending_achievement=internal_game_state.get("GoodEndingAchievement", False),
            green_marble_location=internal_game_state.get("GreenMarbleLocation", -1),
            green_power_marble_delivered=internal_game_state.get("GreenPowermarbleDelivered", False),
            has_met_gehn=internal_game_state.get("HasMetGehn", False),
            has_player_left_tay_prison_cell=internal_game_state.get("HasPlayerLeftTayPrisonCell", False),
            has_power_marble_setting=internal_game_state.get("HasPowermarbleSetting", False),
            has_seen_guard_tower_a_siren_played=internal_game_state.get("HasSeenGuardTowerASirenPlayed", False),
            has_seen_keta_vid=internal_game_state.get("HasSeenKetaVid", False),
            hut_door_knocker_count=internal_game_state.get("HutDoorKnockerCount", 0),
            jungle_button_on=internal_game_state.get("JungleButtonOn", False),
            jungle_fire_marble_dome_open=internal_game_state.get("JungleFiremarbleDomeOpen", False),
            jungle_woodcart_call_button_pressed=internal_game_state.get("JungleWoodcartCallButtonPressed", False),
            lake_steam_valve_location=internal_game_state.get("LakeSteamValveLocation", 0),
            left_aquarium_chair_arm_active_view=left_aquarium_chair_arm_active_view,
            light_post_solution_1=internal_game_state.get("LightPostSolution1", 0),
            light_post_solution_2=internal_game_state.get("LightPostSolution2", 0),
            light_post_solution_3=internal_game_state.get("LightPostSolution3", 0),
            looked_down_at_cho=internal_game_state.get("LookedDownAtCho", False),
            mag_glass_location=internal_game_state.get("MagGlassLocation", True),
            maglev_boiler_button_boiler=internal_game_state.get("MaglevBoilerButtonBoiler", False),
            maglev_boiler_button_survey=internal_game_state.get("MaglevBoilerButtonSurvey", False),
            maglev_boiler_button_survey_alt=internal_game_state.get("MaglevBoilerButtonSurveyAlt", False),
            maglev_jungle_button_jungle=internal_game_state.get("MaglevJungleButtonJungle", False),
            maglev_jungle_button_jungle_alt=internal_game_state.get("MaglevJungleButtonJungleAlt", False),
            maglev_jungle_button_survey=internal_game_state.get("MaglevJungleButtonSurvey", False),
            maglev_temple_button_temple=internal_game_state.get("MaglevTempleButtonTemple", False),
            maglev_temple_button_jungle=internal_game_state.get("MaglevTempleButtonJungle", False),
            mining_cave_water_drained=internal_game_state.get("MiningCaveWaterDrained", False),
            orange_marble_location=internal_game_state.get("OrangeMarbleLocation", -1),
            orange_power_marble_delivered=internal_game_state.get("OrangePowermarbleDelivered", False),
            paddle_light_five_on=internal_game_state.get("PaddleLightFiveOn", False),
            paddle_light_four_on=internal_game_state.get("PaddleLightFourOn", False),
            paddle_light_one_on=internal_game_state.get("PaddleLightOneOn", False),
            paddle_light_seven_on=internal_game_state.get("PaddleLightSevenOn", False),
            paddle_light_six_on=internal_game_state.get("PaddleLightSixOn", False),
            paddle_light_three_b_on=internal_game_state.get("PaddleLightThreeBOn", False),
            paddle_light_three_on=internal_game_state.get("PaddleLightThreeOn", False),
            paddle_light_two_on=internal_game_state.get("PaddleLightTwoOn", False),
            plateau_elevator_location=internal_game_state.get("PlateauElevatorLocation", 1),
            player_engaging_sub=internal_game_state.get("PlayerEngagingSub", False),
            player_has_prison_elevator_code=internal_game_state.get("PlayerHasPrisonElevatorCode", False),
            player_has_trap_book=internal_game_state.get("PlayerHasTrapBook", False),
            player_is_engaged=player_is_engaged,
            player_moved_to_prison_cell=internal_game_state.get("PlayerMovedToPrisonCell", False),
            player_visited_catherine_count=internal_game_state.get("PlayerVisitedCatherineCount", 0),
            player_visited_gehns_lab=internal_game_state.get("PlayerVisitedGehnsLab", False),
            prev_flame_lever_location=internal_game_state.get("PrevFlameLeverLocation", True),
            prison_button_on=internal_game_state.get("PrisonButtonOn", False),
            prison_fire_marble_dome_open=internal_game_state.get("PrisonFiremarbleDomeOpen", False),
            prison_telescope_rotated=internal_game_state.get("PrisonTelescopeRotated", False),
            reached_last_page_atrus_journal=internal_game_state.get("ReachedLastPageAtrusJournal", False),
            reached_last_page_catherine_journal=internal_game_state.get("ReachedLastPageCatherineJournal", False),
            reached_last_page_gehn_journal=internal_game_state.get("ReachedLastPageGehnJournal", False),
            reached_last_page_lab_journal=internal_game_state.get("ReachedLastPageLabJournal", False),
            rebel_viewer_collected=internal_game_state.get("RebelViewerCollected", False),
            red_marble_location=internal_game_state.get("RedMarbleLocation", -1),
            red_power_marble_delivered=internal_game_state.get("RedPowermarbleDelivered", False),
            returning_from_starry_expanse=internal_game_state.get("ReturningFromStarryExpanse", False),
            right_aquarium_chair_arm_active_light=right_aquarium_chair_arm_active_light,
            school_door_open=internal_game_state.get("SchoolDoorOpen", False),
            scribe_run_cinematic_played=internal_game_state.get("ScribeRunCinematicPlayed", False),
            secret_block_location=internal_game_state.get("SecretBlockLocation", 0),
            should_hold_open_village_water_cavity=internal_game_state.get("ShouldHoldOpenVillageWaterCavity", False),
            slider_offset_solution_index=internal_game_state.get("SliderOffsetSolutionIndex", 0),
            slider_solution_blue=internal_game_state.get("SliderSolutionBlue", 0),
            slider_solution_green=internal_game_state.get("SliderSolutionGreen", 0),
            slider_solution_orange=internal_game_state.get("SliderSolutionOrange", 0),
            slider_solution_red=internal_game_state.get("SliderSolutionRed", 0),
            slider_solution_violet=internal_game_state.get("SliderSolutionViolet", 0),
            spear_crank_rotation=internal_game_state.get("SpearCrankRotation", 0.0),
            spider_chair_door_location=internal_game_state.get("SpiderChairDoorLocation", False),
            sub_call_button_pressed=internal_game_state.get("SubCallButtonPressed", False),
            sub_dome_elevator_location=internal_game_state.get("SubDomeElevatorLocation", 0),
            sub_dome_powered=internal_game_state.get("SubdomePowered", False),
            sub_location=internal_game_state.get("SubLocation", 0),
            survey_button_on=internal_game_state.get("SurveyButtonOn", False),
            survey_fire_marble_dome_open=internal_game_state.get("SurveyFiremarbleDomeOpen", False),
            telescope_lever_broken=internal_game_state.get("TelescopeLeverBroken", False),
            telescope_powered=internal_game_state.get("TelescopePowered", False),
            telescope_solution_eight=internal_game_state.get("TelescopeSolutionEight", 0),
            telescope_solution_five=internal_game_state.get("TelescopeSolutionFive", 0),
            telescope_solution_four=internal_game_state.get("TelescopeSolutionFour", 0),
            telescope_solution_nine=internal_game_state.get("TelescopeSolutionNine", 0),
            telescope_solution_one=internal_game_state.get("TelescopeSolutionOne", 0),
            telescope_solution_seven=internal_game_state.get("TelescopeSolutionSeven", 0),
            telescope_solution_six=internal_game_state.get("TelescopeSolutionSix", 0),
            telescope_solution_ten=internal_game_state.get("TelescopeSolutionTen", 0),
            telescope_solution_three=internal_game_state.get("TelescopeSolutionThree", 0),
            telescope_solution_two=internal_game_state.get("TelescopeSolutionTwo", 0),
            temple_button_on=internal_game_state.get("TempleButtonOn", False),
            temple_fire_marble_dome_open=internal_game_state.get("TempleFiremarbleDomeOpen", False),
            temple_maglev_intro_was_fired=internal_game_state.get("TempleMaglevIntroWasFired", False),
            temple_old_gate_locked=internal_game_state.get("TempleOldGateLocked", True),
            violet_marble_location=internal_game_state.get("VioletMarbleLocation", -1),
            violet_power_marble_delivered=internal_game_state.get("VioletPowermarbleDelivered", False),
            wahrk_rammed_glass=internal_game_state.get("WahrkRammedGlass", False),
            wahrk_totem_mouth_open=internal_game_state.get("WahrkTotemMouthOpen", False),
            woodcart_floor_open=internal_game_state.get("WoodcartFloorOpen", False),
            ytram_cave_water_diverter_location=internal_game_state.get("YtramCaveWaterDiverterLocation", False),
            ytram_cinematic_played=internal_game_state.get("YtramCinematicPlayed", False),
        )

        return self.game_state

    def lock_spider_chair_lever(self) -> bool:
        return self.lock_lever_instances(["SpiderChairLeftSlidingLever2"])

    def lock_village_podium_platform_crank(self) -> bool:
        return self.lock_crank_instances(["SM_Bridge_Crank_12"])

    def lock_lab_catwalk_lock_lever(self) -> bool:
        return self.lock_lever_instances(["CatwalkDoorLock"])

    def lock_lab_maglev_lock_lever(self) -> bool:
        return self.lock_lever_instances(["MaglevDoorLock"])

    def lock_jungle_bridge_crank(self) -> bool:
        return self.lock_crank_instances(["BP_RivenCrank5"])

    def lock_boiler_bridge_crank(self) -> bool:
        return self.lock_crank_instances(["BP_RivenCrank4"])

    def lock_survey_bridge_crank(self) -> bool:
        return self.lock_crank_instances(["BP_RivenCrank7"])

    def lock_prison_bridge_crank(self) -> bool:
        return self.lock_crank_instances(["BP_RivenCrank6"])

    def open_gate_to_golden_dome(self) -> bool:
        return self.open_riven_door_instance("Gate_ToGoldenDome")

    def open_gate_to_spinning_dome(self) -> bool:
        return self.open_riven_door_instance("Gate_ToBackStage")

    def lock_steam_control_room_lever(self) -> bool:
        return self.lock_lever_instances(["BP_RivenGameStateLever2_2"])

    def unlock_steam_control_room_lever(self) -> bool:
        return self.unlock_lever_instances(["BP_RivenGameStateLever2_2"])

    def lock_projection_room_door(self) -> bool:
        return self.lock_door_instance("SpiderRoomDoor")

    def unlock_projection_room_door(self) -> bool:
        return self.unlock_door_instance("SpiderRoomDoor")

    def raise_upper_village_drawbridge(self) -> bool:
        if not self.has_wiggled_upper_village_drawbridge:
            wiggle_results: List[bool] = list()

            wiggle_results.append(self.crank_rotation("SM_Handle_A2_2", 1800.0))
            wiggle_results.append(self.crank_rotation("SM_Handle_A2_2", 0.0))

            if all(wiggle_results):
                self.has_wiggled_upper_village_drawbridge = True

        return self.crank_rotation("SM_Handle_A2_2", 1800.0)

    def lower_upper_village_drawbridge(self) -> bool:
        if not self.has_wiggled_upper_village_drawbridge:
            wiggle_results: List[bool] = list()

            wiggle_results.append(self.crank_rotation("SM_Handle_A2_2", 0.0))
            wiggle_results.append(self.crank_rotation("SM_Handle_A2_2", 1800.0))

            if all(wiggle_results):
                self.has_wiggled_upper_village_drawbridge = True

        return self.crank_rotation("SM_Handle_A2_2", 0.0)

    def retract_podium_platform(self) -> bool:
        return self.crank_rotation("SM_Bridge_Crank_12", 0.0)

    def extend_podium_platform(self) -> bool:
        return self.crank_rotation("SM_Bridge_Crank_12", -1080.0)

    def raise_lower_village_drawbridge(self) -> bool:
        if not self.has_wiggled_lower_village_drawbridge:
            wiggle_results: List[bool] = list()

            wiggle_results.append(self.crank_rotation("SM_Handle_A_5", 1800.0))
            wiggle_results.append(self.crank_rotation("SM_Handle_A_5", 0.0))

            if all(wiggle_results):
                self.has_wiggled_lower_village_drawbridge = True

        return self.crank_rotation("SM_Handle_A_5", 1800.0)

    def lower_lower_village_drawbridge(self) -> bool:
        if not self.has_wiggled_lower_village_drawbridge:
            wiggle_results: List[bool] = list()

            wiggle_results.append(self.crank_rotation("SM_Handle_A_5", 0.0))
            wiggle_results.append(self.crank_rotation("SM_Handle_A_5", 1800.0))

            if all(wiggle_results):
                self.has_wiggled_lower_village_drawbridge = True

        return self.crank_rotation("SM_Handle_A_5", 0.0)

    def lock_village_school_door(self) -> bool:
        return self.lock_door_instance("SM_Door_2")

    def unlock_village_school_door(self) -> bool:
        return self.unlock_door_instance("SM_Door_2")

    def lock_woodcart_platform_levers(self) -> bool:
        return self.lock_lever_instances(["BP_RivenLever2_2", "BP_RivenLever3"])

    def unlock_woodcart_platform_levers(self) -> bool:
        return self.unlock_lever_instances(["BP_RivenLever2_2", "BP_RivenLever3"])

    def lock_wahrk_elevator_lever(self) -> bool:
        return self.lock_lever_instances(["SM_Wharkavator_DoubleDirectionLever_2"])

    def unlock_wahrk_elevator_lever(self) -> bool:
        return self.unlock_lever_instances(["SM_Wharkavator_DoubleDirectionLever_2"])

    def lock_bone_throne_door(self) -> bool:
        return self.lock_lever_instances(["SM_BoneThrone_Door_Lever2"])

    def unlock_bone_throne_door(self) -> bool:
        return self.unlock_lever_instances(["SM_BoneThrone_Door_Lever2"])

    def lock_submarine_cave_boarding_platform_lever(self) -> bool:
        return self.lock_lever_instances(["SM_ToungeDepressor_Lever_7"])

    def unlock_submarine_cave_boarding_platform_lever(self) -> bool:
        return self.unlock_lever_instances(["SM_ToungeDepressor_Lever_7"])

    def lock_wahrk_gallows_jail_cell_door_crank(self) -> bool:
        return self.lock_crank_instances(["BP_GallowsCrank_C_0"])

    def unlock_wahrk_gallows_jail_cell_door_crank(self) -> bool:
        return self.unlock_crank_instances(["BP_GallowsCrank_C_0"])

    def lock_lake_steam_valve_lever(self) -> bool:
        return self.lock_lever_instances(["BP_CyanMultiPositionLever_2"])

    def unlock_lake_steam_valve_lever(self) -> bool:
        return self.unlock_lever_instances(["BP_CyanMultiPositionLever_2"])

    def lock_boiler_water_valve_lever(self) -> bool:
        return self.lock_lever_instances(["BoilerDrainCranklever_0"])

    def unlock_boiler_water_valve_lever(self) -> bool:
        return self.unlock_lever_instances(["BoilerDrainCranklever_0"])

    def lock_cave_pump_button(self) -> bool:
        return self.lock_button_instances(["MiningCavePumpButton"])

    def unlock_cave_pump_button(self) -> bool:
        return self.unlock_button_instances(["MiningCavePumpButton"])

    def lock_lab_elevator_cranks(self) -> bool:
        return self.lock_crank_instances(["DumbwaiterCrank_MiningCave", "DumbwaiterCrank_LabCrank"])

    def unlock_lab_elevator_cranks(self) -> bool:
        return self.unlock_crank_instances(["DumbwaiterCrank_MiningCave", "DumbwaiterCrank_LabCrank"])

    def unlock_lab_catwalk_door(self) -> bool:
        return self.lever_rotation("CatwalkDoorLock", False)

    def lock_lab_catwalk_door(self) -> bool:
        return self.lever_rotation("CatwalkDoorLock", True)

    def unlock_lab_maglev_door(self) -> bool:
        return self.lever_rotation("MaglevDoorLock", False)

    def lock_lab_maglev_door(self) -> bool:
        return self.lever_rotation("MaglevDoorLock", True)

    def lock_lab_press_crank(self) -> bool:
        return self.lock_crank_instances(["LabBookPressCrank2_Blueprint_C_0"])

    def unlock_lab_press_crank(self) -> bool:
        return self.unlock_crank_instances(["LabBookPressCrank2_Blueprint_C_0"])

    def lock_plateau_elevator_buttons(self) -> bool:
        return self.lock_button_instances(["PlateauElevatorButton_Upper", "PlateauElevatorButton_Lower", "GridButton_1"])

    def unlock_plateau_elevator_buttons(self) -> bool:
        return self.unlock_button_instances(["PlateauElevatorButton_Upper", "PlateauElevatorButton_Lower", "GridButton_1"])

    def lock_aquarium_chair_left_lever(self) -> bool:
        return self.lock_lever_instances(["SM_ViewerArm_Lever_Left"])

    def unlock_aquarium_chair_left_lever(self) -> bool:
        return self.unlock_lever_instances(["SM_ViewerArm_Lever_Left"])

    def lock_aquarium_chair_right_lever(self) -> bool:
        return self.lock_lever_instances(["SM_ViewerArm_Lever_Right"])

    def unlock_aquarium_chair_right_lever(self) -> bool:
        return self.unlock_lever_instances(["SM_ViewerArm_Lever_Right"])

    def lock_gehntris_board(self) -> bool:
        return self.lock_button_instances(["BP_RivenButton2_2"])

    def unlock_gehntris_board(self) -> bool:
        return self.unlock_button_instances(["BP_RivenButton2_2"])

    def lock_maglev_platform_to_boiler_door_lever(self) -> bool:
        return self.lock_lever_instances(["SM_DoorHandle_MaglevToElevator_28"])

    def unlock_maglev_platform_to_boiler_door_lever(self) -> bool:
        return self.unlock_lever_instances(["SM_DoorHandle_MaglevToElevator_28"])

    def lock_log_telescope_lever(self) -> bool:
        return self.lock_lever_instances(["SM_Telescope3"])

    def unlock_log_telescope_lever(self) -> bool:
        return self.unlock_lever_instances(["SM_Telescope3"])

    def lock_marble_devices(self) -> bool:
        return self.lock_lever_instances([
            "BP_CapsuleStationLever_Temple",
            "BP_CapsuleStationLever_2",
            "BP_CapsuleStationLever_Boiler",
            "BP_CapsuleStationLever_Survey",
            "BP_CapsuleStationLever_Prison",
        ])

    def unlock_marble_devices(self) -> bool:
        return self.unlock_lever_instances([
            "BP_CapsuleStationLever_Temple",
            "BP_CapsuleStationLever_2",
            "BP_CapsuleStationLever_Boiler",
            "BP_CapsuleStationLever_Survey",
            "BP_CapsuleStationLever_Prison",
        ])

    def retract_starry_expanse_jungle_bridge(self) -> bool:
        return self.crank_rotation("BP_RivenCrank5", 0.0)

    def extend_starry_expanse_jungle_bridge(self) -> bool:
        return self.crank_rotation("BP_RivenCrank5", 1024.0)

    def retract_starry_expanse_boiler_bridge(self) -> bool:
        return self.crank_rotation("BP_RivenCrank4", 0.0)

    def extend_starry_expanse_boiler_bridge(self) -> bool:
        return self.crank_rotation("BP_RivenCrank4", 1024.0)

    def retract_starry_expanse_survey_bridge(self) -> bool:
        return self.crank_rotation("BP_RivenCrank7", 0.0)

    def extend_starry_expanse_survey_bridge(self) -> bool:
        return self.crank_rotation("BP_RivenCrank7", 1024.0)

    def lock_all_gate_room_levers(self) -> bool:
        if not self.is_process_running:
            return False

        lever_instances: List[str] = [
            "BP_RivenSlidingLever_2",
            "BP_RivenSlidingLever2",
        ]

        lever_instance: str
        for lever_instance in lever_instances:
            if lever_instance not in self.gobjects_name_to_object:
                continue

            lever_use_clickable_distance_address: int = self.gobjects_name_to_object[lever_instance][0]["address"] + 0x54A
            lever_max_clickable_distance_address: int = self.gobjects_name_to_object[lever_instance][0]["address"] + 0x550

            try:
                self.process.write_bool(lever_use_clickable_distance_address, True)
                self.process.write_double(lever_max_clickable_distance_address, 0.0)
            except Exception:
                return False

        return True

    def lock_upper_village_drawbridge_controls(self) -> bool:
        if not self.is_process_running:
            return False

        crank_instance: str = "SM_Handle_A2_2"
        lever_instance: str = "SM_Handle_B2"

        if crank_instance not in self.gobjects_name_to_object or lever_instance not in self.gobjects_name_to_object:
            return False

        crank_use_clickable_distance_address: int = self.gobjects_name_to_object[crank_instance][0]["address"] + 0x5E1
        crank_max_clickable_distance_address: int = self.gobjects_name_to_object[crank_instance][0]["address"] + 0x5E8

        lever_use_clickable_distance_address: int = self.gobjects_name_to_object[lever_instance][0]["address"] + 0x690
        lever_max_clickable_distance_address: int = self.gobjects_name_to_object[lever_instance][0]["address"] + 0x688

        try:
            self.process.write_bool(crank_use_clickable_distance_address, True)
            self.process.write_double(crank_max_clickable_distance_address, 0.0)

            self.process.write_bool(lever_use_clickable_distance_address, True)
            self.process.write_double(lever_max_clickable_distance_address, 0.0)
        except Exception:
            return False

        return True

    def lock_lower_village_drawbridge_controls(self) -> bool:
        if not self.is_process_running:
            return False

        crank_instance: str = "SM_Handle_A_5"
        lever_instance: str = "SM_Handle_B_11"

        if crank_instance not in self.gobjects_name_to_object or lever_instance not in self.gobjects_name_to_object:
            return False

        crank_use_clickable_distance_address: int = self.gobjects_name_to_object[crank_instance][0]["address"] + 0x5E1
        crank_max_clickable_distance_address: int = self.gobjects_name_to_object[crank_instance][0]["address"] + 0x5E8

        lever_use_clickable_distance_address: int = self.gobjects_name_to_object[lever_instance][0]["address"] + 0x690
        lever_max_clickable_distance_address: int = self.gobjects_name_to_object[lever_instance][0]["address"] + 0x688

        try:
            self.process.write_bool(crank_use_clickable_distance_address, True)
            self.process.write_double(crank_max_clickable_distance_address, 0.0)

            self.process.write_bool(lever_use_clickable_distance_address, True)
            self.process.write_double(lever_max_clickable_distance_address, 0.0)
        except Exception:
            return False

        return True

    def lock_button_instances(self, button_instances: List[str]) -> bool:
        if not self.is_process_running:
            return False

        button_instance: str
        for button_instance in button_instances:
            if button_instance not in self.gobjects_name_to_object:
                continue

            button_enabled_address: int = self.gobjects_name_to_object[button_instance][0]["address"] + 0x4E8

            try:
                self.process.write_bool(button_enabled_address, False)
            except Exception:
                continue

        return True

    def unlock_button_instances(self, button_instances: List[str]) -> bool:
        if not self.is_process_running:
            return False

        button_instance: str
        for button_instance in button_instances:
            if button_instance not in self.gobjects_name_to_object:
                continue

            button_enabled_address: int = self.gobjects_name_to_object[button_instance][0]["address"] + 0x4E8

            try:
                self.process.write_bool(button_enabled_address, True)
            except Exception:
                continue

        return True

    def lock_all_beetle_viewers(self) -> bool:
        if not self.is_process_running:
            return False

        beetle_viewer_instances: List[str] = [
            "BP_BeetleViewer_1",
            "BP_BeetleViewer_2",
            "BP_BeetleViewer_3",
            "BP_BeetleViewer_4",
            "BP_BeetleViewer_5",
        ]

        beetle_viewer_instance: str
        for beetle_viewer_instance in beetle_viewer_instances:
            if beetle_viewer_instance not in self.gobjects_name_to_object:
                continue

            click_enabled_address: int = self.gobjects_name_to_object[beetle_viewer_instance][0]["address"] + 0x428

            try:
                self.process.write_bool(click_enabled_address, False)
            except Exception:
                continue

        return True

    def unlock_all_beetle_viewers(self) -> bool:
        if not self.is_process_running:
            return False

        beetle_viewer_instances: List[str] = [
            "BP_BeetleViewer_1",
            "BP_BeetleViewer_2",
            "BP_BeetleViewer_3",
            "BP_BeetleViewer_4",
            "BP_BeetleViewer_5",
        ]

        beetle_viewer_instance: str
        for beetle_viewer_instance in beetle_viewer_instances:
            if beetle_viewer_instance not in self.gobjects_name_to_object:
                continue

            click_enabled_address: int = self.gobjects_name_to_object[beetle_viewer_instance][0]["address"] + 0x428

            try:
                self.process.write_bool(click_enabled_address, True)
            except Exception:
                continue

        return True

    def is_riven_door_instance_open(self, instance_name: str) -> bool:
        allowable_instances: List[str] = [
            "Gate_ToBackStage",
            "Gate_ToGoldenDome",
        ]

        if instance_name not in allowable_instances:
            return False

        if not self.is_process_running:
            return False

        if instance_name not in self.gobjects_name_to_object:
            return False

        is_opening_address: int = self.gobjects_name_to_object[instance_name][0]["address"] + 0xA51

        try:
            is_open: bool = self.process.read_bool(is_opening_address)
            return is_open
        except Exception:
            return False

    def open_riven_door_instance(self, instance_name: str) -> bool:
        allowable_instances: List[str] = [
            "Gate_ToBackStage",
            "Gate_ToGoldenDome",
        ]

        if instance_name not in allowable_instances:
            return False

        if not self.is_process_running:
            return False

        if instance_name not in self.gobjects_name_to_object:
            return False

        if self.is_riven_door_instance_open(instance_name):
            return True

        return self.toggle_riven_door_instance(instance_name)

    def close_riven_door_instance(self, instance_name: str) -> bool:
        allowable_instances: List[str] = [
            "Gate_ToBackStage",
            "Gate_ToGoldenDome",
        ]

        if instance_name not in allowable_instances:
            return False

        if not self.is_process_running:
            return False

        if instance_name not in self.gobjects_name_to_object:
            return False

        if not self.is_riven_door_instance_open(instance_name):
            return True

        return self.toggle_riven_door_instance(instance_name)

    def toggle_riven_door_instance(self, instance_name: str) -> bool:
        allowable_instances: List[str] = [
            "Gate_ToBackStage",
            "Gate_ToGoldenDome",
        ]

        if instance_name not in allowable_instances:
            return False

        if not self.is_process_running:
            return False

        if "BP_CyanDoor_C" not in self.gobjects_name_to_object:
            return False
        elif "BP_RivenDoor_C" not in self.gobjects_name_to_object:
            return False

        cyan_door_address: int = self.gobjects_name_to_object["BP_CyanDoor_C"][0]["address"]
        riven_door_address: int = self.gobjects_name_to_object["BP_RivenDoor_C"][0]["address"]

        if instance_name not in self.gobjects_name_to_object:
            return False

        instance_address: int = 0

        object_data: Dict[str, Any]
        for object_data in self.gobjects_name_to_object[instance_name]:
            if object_data["class"] == riven_door_address:
                instance_address = object_data["address"]
                break

        if instance_address == 0:
            return False

        if "Open Door" not in self.gobjects_name_to_object:
            return False

        function_address: int = 0

        object_data: Dict[str, Any]
        for object_data in self.gobjects_name_to_object["Open Door"]:
            if object_data["outer"] == cyan_door_address:
                function_address = object_data["address"]
                break

        if function_address == 0:
            return False

        return self._call_process_event(instance_address, function_address, None, None, None)

    def lock_lever_instances(self, lever_instances: List[str]) -> bool:
        if not self.is_process_running:
            return False

        lever_instance: str
        for lever_instance in lever_instances:
            if lever_instance not in self.gobjects_name_to_object:
                continue

            use_clickable_distance_address: int = self.gobjects_name_to_object[lever_instance][0]["address"] + 0x690
            max_clickable_distance_address: int = self.gobjects_name_to_object[lever_instance][0]["address"] + 0x688

            try:
                self.process.write_bool(use_clickable_distance_address, True)
                self.process.write_double(max_clickable_distance_address, 0.0)
            except Exception:
                continue

        return True

    def unlock_lever_instances(self, lever_instances: List[str]) -> bool:
        if not self.is_process_running:
            return False

        lever_instance: str
        for lever_instance in lever_instances:
            if lever_instance not in self.gobjects_name_to_object:
                continue

            use_clickable_distance_address: int = self.gobjects_name_to_object[lever_instance][0]["address"] + 0x690
            max_clickable_distance_address: int = self.gobjects_name_to_object[lever_instance][0]["address"] + 0x688

            try:
                self.process.write_bool(use_clickable_distance_address, False)
                self.process.write_double(max_clickable_distance_address, 100.0)
            except Exception:
                continue

        return True

    def lock_door_instance(self, door_instance: str) -> bool:
        if not self.is_process_running:
            return False

        if door_instance not in self.gobjects_name_to_object:
            return False

        use_clickable_distance_address: int = self.gobjects_name_to_object[door_instance][0]["address"] + 0x64B
        max_click_distance_address: int = self.gobjects_name_to_object[door_instance][0]["address"] + 0x650

        try:
            self.process.write_bool(use_clickable_distance_address, True)
            self.process.write_double(max_click_distance_address, 0.0)
        except Exception:
            return False

        return True

    def unlock_door_instance(self, door_instance: str) -> bool:
        if not self.is_process_running:
            return False

        if door_instance not in self.gobjects_name_to_object:
            return False

        use_clickable_distance_address: int = self.gobjects_name_to_object[door_instance][0]["address"] + 0x64B
        max_click_distance_address: int = self.gobjects_name_to_object[door_instance][0]["address"] + 0x650

        try:
            self.process.write_bool(use_clickable_distance_address, False)
            self.process.write_double(max_click_distance_address, 100.0)
        except Exception:
            return False

        return True

    def crank_rotation(self, instance_name: str, rotation_degrees: float) -> bool:
        if not self.is_process_running:
            return False

        if instance_name not in self.gobjects_name_to_object:
            return False

        if "BP_CyanCrank_C" not in self.gobjects_name_to_object:
            return False

        cyan_crank_address: int = self.gobjects_name_to_object["BP_CyanCrank_C"][0]["address"]

        allowable_instance_classes: List[str] = [
            "BP_RivenCrank_C",
            "BP_PodiumBridgeCrank_C",
            "BP_VillageDrawbridgeCrank_C",
            "BP_GallowsCrank_C",
        ]

        instance_address: int = 0

        object_data: Dict[str, Any]
        for object_data in self.gobjects_name_to_object[instance_name]:
            if self.gobjects_address_to_object[object_data["class"]]["name"] in allowable_instance_classes:
                instance_address = object_data["address"]
                break

        if instance_address == 0:
            return False

        current_rotation_address: int = instance_address + 0x398

        try:
            current_rotation: float = self.process.read_double(current_rotation_address)
        except Exception:
            return False

        if current_rotation == rotation_degrees:
            return True

        function_address: int = 0

        object_data: Dict[str, Any]
        for object_data in self.gobjects_name_to_object["CrankRotation"]:
            if object_data["outer"] == cyan_crank_address:
                function_address = object_data["address"]
                break

        if function_address == 0:
            return False

        args_bytes: bytes = struct.pack("<f", float(rotation_degrees)) + b"\x00\x00\x00\x00"

        self._call_process_event(instance_address, function_address, args_bytes, None, None)

        function_address: int = 0

        object_data: Dict[str, Any]
        for object_data in self.gobjects_name_to_object["UpdateFloatGameState"]:
            if object_data["outer"] == cyan_crank_address:
                function_address = object_data["address"]
                break

        if function_address == 0:
            return False

        return self._call_process_event(instance_address, function_address, None, None, None)

    def disable_light_posts(self) -> bool:
        if not self.is_process_running:
            return False

        light_post_instances: List[str] = [
            "BP_BlueCaveLightPost_2",
            "BP_BlueCaveLightPost2",
            "BP_BlueCaveLightPost3",
            "BP_BlueCaveLightPost4",
            "BP_BlueCaveLightPost5",
            "BP_BlueCaveLightPost6",
            "BP_BlueCaveLightPost7",
            "BP_BlueCaveLightPost8",
            "BP_BlueCaveLightPost9",
        ]

        light_post_instance: str
        for light_post_instance in light_post_instances:
            if light_post_instance not in self.gobjects_name_to_object:
                continue

            light_post_can_grab_address: int = self.gobjects_name_to_object[light_post_instance][0]["address"] + 0x3C0

            try:
                self.process.write_bool(light_post_can_grab_address, False)
            except Exception:
                continue

        return True

    def enable_light_posts(self) -> bool:
        if not self.is_process_running:
            return False

        light_post_instances: List[str] = [
            "BP_BlueCaveLightPost_2",
            "BP_BlueCaveLightPost2",
            "BP_BlueCaveLightPost3",
            "BP_BlueCaveLightPost4",
            "BP_BlueCaveLightPost5",
            "BP_BlueCaveLightPost6",
            "BP_BlueCaveLightPost7",
            "BP_BlueCaveLightPost8",
            "BP_BlueCaveLightPost9",
        ]

        light_post_instance: str
        for light_post_instance in light_post_instances:
            if light_post_instance not in self.gobjects_name_to_object:
                continue

            light_post_can_grab_address: int = self.gobjects_name_to_object[light_post_instance][0]["address"] + 0x3C0

            try:
                self.process.write_bool(light_post_can_grab_address, True)
            except Exception:
                continue

        return True

    def lock_jungle_main_door(self) -> bool:
        if not self.is_process_running:
            return False

        door_instance: str = "JungleUpperFrontGate_Blueprint"

        if door_instance not in self.gobjects_name_to_object:
            return False

        door_opened_rotation_forward_address: int = self.gobjects_name_to_object[door_instance][0]["address"] + 0x440
        door_opened_rotation_backward_address: int = self.gobjects_name_to_object[door_instance][0]["address"] + 0x448

        try:
            self.process.write_double(door_opened_rotation_forward_address, 0.0)
            self.process.write_double(door_opened_rotation_backward_address, 0.0)
        except Exception:
            return False

        return True

    def unlock_jungle_main_door(self) -> bool:
        if not self.is_process_running:
            return False

        door_instance: str = "JungleUpperFrontGate_Blueprint"

        if door_instance not in self.gobjects_name_to_object:
            return False

        door_opened_rotation_forward_address: int = self.gobjects_name_to_object[door_instance][0]["address"] + 0x440
        door_opened_rotation_backward_address: int = self.gobjects_name_to_object[door_instance][0]["address"] + 0x448

        try:
            self.process.write_double(door_opened_rotation_forward_address, 90.0)
            self.process.write_double(door_opened_rotation_backward_address, -90.0)
        except Exception:
            return False

        return True

    def lock_jungle_side_door(self) -> bool:
        if not self.is_process_running:
            return False

        door_instance: str = "BP_JungleGate_2"

        if door_instance not in self.gobjects_name_to_object:
            return False

        door_opened_rotation_forward_address: int = self.gobjects_name_to_object[door_instance][0]["address"] + 0x440
        door_opened_rotation_backward_address: int = self.gobjects_name_to_object[door_instance][0]["address"] + 0x448

        try:
            self.process.write_double(door_opened_rotation_forward_address, 0.0)
            self.process.write_double(door_opened_rotation_backward_address, 0.0)
        except Exception:
            return False

        return True

    def unlock_jungle_side_door(self) -> bool:
        if not self.is_process_running:
            return False

        door_instance: str = "BP_JungleGate_2"

        if door_instance not in self.gobjects_name_to_object:
            return False

        door_opened_rotation_forward_address: int = self.gobjects_name_to_object[door_instance][0]["address"] + 0x440
        door_opened_rotation_backward_address: int = self.gobjects_name_to_object[door_instance][0]["address"] + 0x448

        try:
            self.process.write_double(door_opened_rotation_forward_address, 60.0)
            self.process.write_double(door_opened_rotation_backward_address, -90.0)
        except Exception:
            return False

        return True

    def lock_crank_instances(self, crank_instances: List[str]) -> bool:
        if not self.is_process_running:
            return False

        crank_instance: str
        for crank_instance in crank_instances:
            if crank_instance not in self.gobjects_name_to_object:
                continue

            crank_use_clickable_distance_address: int = self.gobjects_name_to_object[crank_instance][0]["address"] + 0x5E1
            crank_max_clickable_distance_address: int = self.gobjects_name_to_object[crank_instance][0]["address"] + 0x5E8

            try:
                self.process.write_bool(crank_use_clickable_distance_address, True)
                self.process.write_double(crank_max_clickable_distance_address, 0.0)
            except Exception:
                return False

        return True

    def unlock_crank_instances(self, crank_instances: List[str]) -> bool:
        if not self.is_process_running:
            return False

        crank_instance: str
        for crank_instance in crank_instances:
            if crank_instance not in self.gobjects_name_to_object:
                continue

            crank_use_clickable_distance_address: int = self.gobjects_name_to_object[crank_instance][0]["address"] + 0x5E1
            crank_max_clickable_distance_address: int = self.gobjects_name_to_object[crank_instance][0]["address"] + 0x5E8

            try:
                self.process.write_bool(crank_use_clickable_distance_address, False)
                self.process.write_double(crank_max_clickable_distance_address, 100.0)
            except Exception:
                return False

        return True

    def lock_animal_circle_room_secret_door(self) -> bool:
        if not self.is_process_running:
            return False

        secret_instance: str = "SM_SecretBlock_6"

        if secret_instance not in self.gobjects_name_to_object:
            return False

        secret_max_clickable_distance_address: int = self.gobjects_name_to_object[secret_instance][0]["address"] + 0x468

        try:
            self.process.write_double(secret_max_clickable_distance_address, 0.0)
        except Exception:
            return False

        return True

    def unlock_animal_circle_room_secret_door(self) -> bool:
        if not self.is_process_running:
            return False

        secret_instance: str = "SM_SecretBlock_6"

        if secret_instance not in self.gobjects_name_to_object:
            return False

        secret_max_clickable_distance_address: int = self.gobjects_name_to_object[secret_instance][0]["address"] + 0x468

        try:
            self.process.write_double(secret_max_clickable_distance_address, 150.0)
        except Exception:
            return False

        return True

    def lever_rotation(self, instance_name: str, forward: bool) -> bool:
        if not self.is_process_running:
            return False

        if instance_name not in self.gobjects_name_to_object:
            return False

        if "BP_CyanLever_C" not in self.gobjects_name_to_object:
            return False

        cyan_lever_address: int = self.gobjects_name_to_object["BP_CyanLever_C"][0]["address"]

        allowable_instance_classes: List[str] = [
            "BP_LabDoorLock_C",
        ]

        instance_address: int = 0

        object_data: Dict[str, Any]
        for object_data in self.gobjects_name_to_object[instance_name]:
            if self.gobjects_address_to_object[object_data["class"]]["name"] in allowable_instance_classes:
                instance_address = object_data["address"]
                break

        if instance_address == 0:
            return False

        current_angle_address: int = instance_address + 0x478

        try:
            current_angle: float = self.process.read_double(current_angle_address)
        except Exception:
            return False

        if not forward and current_angle != 90.0:
            return False
        elif forward and current_angle != 0.0:
            return False

        function_address: int = 0

        object_data: Dict[str, Any]
        for object_data in self.gobjects_name_to_object["LeverRotation"]:
            if object_data["outer"] == cyan_lever_address:
                function_address = object_data["address"]
                break

        if function_address == 0:
            return False

        args_bytes: bytes = struct.pack("<?", forward)

        return self._call_process_event(instance_address, function_address, args_bytes, None, None)

    def lock_maglev_jungle_temple_throttle_lever(self) -> bool:
        if not self.is_process_running:
            return False

        maglev_instance: str = "MaglevJNGtoTPL"

        if maglev_instance not in self.gobjects_name_to_object:
            return False

        try:
            throttle_lever_pointer: int = self.gobjects_name_to_object[maglev_instance][0]["address"] + 0x520
            throttle_lever_address: int = self.process.read_longlong(throttle_lever_pointer)

            throttle_lever_actor_pointer: int = throttle_lever_address + 0x2C8
            throttle_lever_actor_address: int = self.process.read_longlong(throttle_lever_actor_pointer)

            self.process.write_double(throttle_lever_actor_address + 0x688, 0.0)
        except Exception:
            return False

        return True

    def unlock_maglev_jungle_temple_throttle_lever(self) -> bool:
        if not self.is_process_running:
            return False

        maglev_instance: str = "MaglevJNGtoTPL"

        if maglev_instance not in self.gobjects_name_to_object:
            return False

        try:
            throttle_lever_pointer: int = self.gobjects_name_to_object[maglev_instance][0]["address"] + 0x520
            throttle_lever_address: int = self.process.read_longlong(throttle_lever_pointer)

            throttle_lever_actor_pointer: int = throttle_lever_address + 0x2C8
            throttle_lever_actor_address: int = self.process.read_longlong(throttle_lever_actor_pointer)

            self.process.write_double(throttle_lever_actor_address + 0x688, 500.0)
        except Exception:
            return False

        return True

    def lock_maglev_boiler_survey_throttle_lever(self) -> bool:
        if not self.is_process_running:
            return False

        maglev_instance: str = "MaglevSRVtoBLR"

        if maglev_instance not in self.gobjects_name_to_object:
            return False

        try:
            throttle_lever_pointer: int = self.gobjects_name_to_object[maglev_instance][0]["address"] + 0x520
            throttle_lever_address: int = self.process.read_longlong(throttle_lever_pointer)

            throttle_lever_actor_pointer: int = throttle_lever_address + 0x2C8
            throttle_lever_actor_address: int = self.process.read_longlong(throttle_lever_actor_pointer)

            self.process.write_double(throttle_lever_actor_address + 0x688, 0.0)
        except Exception:
            return False

        return True

    def unlock_maglev_boiler_survey_throttle_lever(self) -> bool:
        if not self.is_process_running:
            return False

        maglev_instance: str = "MaglevSRVtoBLR"

        if maglev_instance not in self.gobjects_name_to_object:
            return False

        try:
            throttle_lever_pointer: int = self.gobjects_name_to_object[maglev_instance][0]["address"] + 0x520
            throttle_lever_address: int = self.process.read_longlong(throttle_lever_pointer)

            throttle_lever_actor_pointer: int = throttle_lever_address + 0x2C8
            throttle_lever_actor_address: int = self.process.read_longlong(throttle_lever_actor_pointer)

            self.process.write_double(throttle_lever_actor_address + 0x688, 500.0)
        except Exception:
            return False

        return True

    def lock_maglev_jungle_survey_throttle_lever(self) -> bool:
        if not self.is_process_running:
            return False

        maglev_instance: str = "Maglev_JNGtoSRV"

        if maglev_instance not in self.gobjects_name_to_object:
            return False

        try:
            throttle_lever_pointer: int = self.gobjects_name_to_object[maglev_instance][0]["address"] + 0x520
            throttle_lever_address: int = self.process.read_longlong(throttle_lever_pointer)

            throttle_lever_actor_pointer: int = throttle_lever_address + 0x2C8
            throttle_lever_actor_address: int = self.process.read_longlong(throttle_lever_actor_pointer)

            self.process.write_double(throttle_lever_actor_address + 0x688, 0.0)
        except Exception:
            return False

        return True

    def unlock_maglev_jungle_survey_throttle_lever(self) -> bool:
        if not self.is_process_running:
            return False

        maglev_instance: str = "Maglev_JNGtoSRV"

        if maglev_instance not in self.gobjects_name_to_object:
            return False

        try:
            throttle_lever_pointer: int = self.gobjects_name_to_object[maglev_instance][0]["address"] + 0x520
            throttle_lever_address: int = self.process.read_longlong(throttle_lever_pointer)

            throttle_lever_actor_pointer: int = throttle_lever_address + 0x2C8
            throttle_lever_actor_address: int = self.process.read_longlong(throttle_lever_actor_pointer)

            self.process.write_double(throttle_lever_actor_address + 0x688, 500.0)
        except Exception:
            return False

        return True

    def set_max_walk_speed(self, max_walk_speed: float) -> bool:
        if not self.is_process_running:
            return False

        character_movement_component_address: int = self._resolve_address(self.gworld_offset, (0x170, 0x340, 0x0, 0x3A0, 0x3C0, 0x0))

        if character_movement_component_address in (0, None):
            return False

        max_walk_speed_address: int = character_movement_component_address + 0x268

        try:
            self.process.write_float(max_walk_speed_address, max_walk_speed)
        except Exception:
            return False

        return True

    def enable_black_and_white_trap(self) -> bool:
        if not self.is_process_running:
            return False

        camera_component_address: int = self._resolve_address(self.gworld_offset, (0x170, 0x340, 0x0, 0x3A0, 0x960, 0x0))

        if camera_component_address in (None, 0):
            return False

        override_color_saturation_address: int = camera_component_address + 0x3E0
        color_saturation_base_address: int = camera_component_address + 0x420
        color_contrast_base_address: int = camera_component_address + 0x440

        bitfield_value: int = self.process.read_int(override_color_saturation_address)

        bitfield_value |= (1 << 3)
        bitfield_value |= (1 << 4)

        self.process.write_int(override_color_saturation_address, bitfield_value)

        self.process.write_double(color_saturation_base_address + 0x18, 0.0)
        self.process.write_double(color_contrast_base_address + 0x18, 20.0)

        return True

    def disable_black_and_white_trap(self) -> bool:
        if not self.is_process_running:
            return False

        camera_component_address: int = self._resolve_address(self.gworld_offset, (0x170, 0x340, 0x0, 0x3A0, 0x960, 0x0))

        if camera_component_address in (None, 0):
            return False

        override_color_saturation_address: int = camera_component_address + 0x3E0
        color_saturation_base_address: int = camera_component_address + 0x420
        color_contrast_base_address: int = camera_component_address + 0x440

        bitfield_value: int = self.process.read_int(override_color_saturation_address)

        bitfield_value &= ~(1 << 3)
        bitfield_value &= ~(1 << 4)

        self.process.write_int(override_color_saturation_address, bitfield_value)

        self.process.write_double(color_saturation_base_address + 0x18, 1.0)
        self.process.write_double(color_contrast_base_address + 0x18, 1.0)

        return True

    def enable_bloom_trap(self) -> bool:
        if not self.is_process_running:
            return False

        camera_component_address: int = self._resolve_address(self.gworld_offset, (0x170, 0x340, 0x0, 0x3A0, 0x960, 0x0))

        if camera_component_address in (None, 0):
            return False

        override_color_gain_address: int = camera_component_address + 0x3E0
        override_bloom_intensity_address: int = camera_component_address + 0x3E5

        color_gain_base_address: int = camera_component_address + 0x480
        bloom_intensity_address: int = camera_component_address + 0x6E4

        bitfield_value: int = self.process.read_int(override_color_gain_address)
        bitfield_value |= (1 << 6)

        self.process.write_int(override_color_gain_address, bitfield_value)

        bitfield_value: int = self.process.read_int(override_bloom_intensity_address)
        bitfield_value |= (1 << 0)

        self.process.write_int(override_bloom_intensity_address, bitfield_value)

        self.process.write_double(color_gain_base_address + 0x18, 10.0)
        self.process.write_float(bloom_intensity_address, 8.0)

        return True

    def disable_bloom_trap(self) -> bool:
        if not self.is_process_running:
            return False

        camera_component_address: int = self._resolve_address(self.gworld_offset, (0x170, 0x340, 0x0, 0x3A0, 0x960, 0x0))

        if camera_component_address in (None, 0):
            return False

        override_color_gain_address: int = camera_component_address + 0x3E0
        override_bloom_intensity_address: int = camera_component_address + 0x3E5

        color_gain_base_address: int = camera_component_address + 0x480
        bloom_intensity_address: int = camera_component_address + 0x6E4

        bitfield_value: int = self.process.read_int(override_color_gain_address)
        bitfield_value &= ~(1 << 6)

        self.process.write_int(override_color_gain_address, bitfield_value)

        bitfield_value: int = self.process.read_int(override_bloom_intensity_address)
        bitfield_value &= ~(1 << 0)

        self.process.write_int(override_bloom_intensity_address, bitfield_value)

        self.process.write_double(color_gain_base_address + 0x18, 1.0)
        self.process.write_float(bloom_intensity_address, 0.675)

        return True

    def enable_chromatic_trap(self) -> bool:
        if not self.is_process_running:
            return False

        camera_component_address: int = self._resolve_address(self.gworld_offset, (0x170, 0x340, 0x0, 0x3A0, 0x960, 0x0))

        if camera_component_address in (None, 0):
            return False

        override_color_saturation_address: int = camera_component_address + 0x3E0
        color_saturation_base_address: int = camera_component_address + 0x420

        bitfield_value: int = self.process.read_int(override_color_saturation_address)
        bitfield_value |= (1 << 3)

        self.process.write_int(override_color_saturation_address, bitfield_value)

        self.process.write_double(color_saturation_base_address + 0x18, 18.0)

        return True

    def disable_chromatic_trap(self) -> bool:
        if not self.is_process_running:
            return False

        camera_component_address: int = self._resolve_address(self.gworld_offset, (0x170, 0x340, 0x0, 0x3A0, 0x960, 0x0))

        if camera_component_address in (None, 0):
            return False

        override_color_saturation_address: int = camera_component_address + 0x3E0
        color_saturation_base_address: int = camera_component_address + 0x420

        bitfield_value: int = self.process.read_int(override_color_saturation_address)
        bitfield_value &= ~(1 << 3)

        self.process.write_int(override_color_saturation_address, bitfield_value)

        self.process.write_double(color_saturation_base_address + 0x18, 1.0)

        return True

    def enable_color_inversion_trap(self) -> bool:
        if not self.is_process_running:
            return False

        camera_component_address: int = self._resolve_address(self.gworld_offset, (0x170, 0x340, 0x0, 0x3A0, 0x960, 0x0))

        if camera_component_address in (None, 0):
            return False

        override_color_saturation_address: int = camera_component_address + 0x3E0
        color_saturation_base_address: int = camera_component_address + 0x420

        bitfield_value: int = self.process.read_int(override_color_saturation_address)
        bitfield_value |= (1 << 3)

        self.process.write_int(override_color_saturation_address, bitfield_value)

        self.process.write_double(color_saturation_base_address, -1.0)
        self.process.write_double(color_saturation_base_address + 0x8, -1.0)
        self.process.write_double(color_saturation_base_address + 0x10, -1.0)

        return True

    def disable_color_inversion_trap(self) -> bool:
        if not self.is_process_running:
            return False

        camera_component_address: int = self._resolve_address(self.gworld_offset, (0x170, 0x340, 0x0, 0x3A0, 0x960, 0x0))

        if camera_component_address in (None, 0):
            return False

        override_color_saturation_address: int = camera_component_address + 0x3E0
        color_saturation_base_address: int = camera_component_address + 0x420

        bitfield_value: int = self.process.read_int(override_color_saturation_address)
        bitfield_value &= ~(1 << 3)

        self.process.write_int(override_color_saturation_address, bitfield_value)

        self.process.write_double(color_saturation_base_address, 1.0)
        self.process.write_double(color_saturation_base_address + 0x8, 1.0)
        self.process.write_double(color_saturation_base_address + 0x10, 1.0)

        return True

    def enable_mobile_game_trap(self) -> bool:
        if not self.is_process_running:
            return False

        camera_component_address: int = self._resolve_address(self.gworld_offset, (0x170, 0x340, 0x0, 0x3A0, 0x960, 0x0))

        if camera_component_address in (None, 0):
            return False

        aspect_ratio_address: int = camera_component_address + 0x2D0
        constraint_aspect_ratio_address: int = camera_component_address + 0x2D5

        self.process.write_float(aspect_ratio_address, 0.5)

        bitfield_value: int = self.process.read_int(constraint_aspect_ratio_address)
        bitfield_value |= (1 << 0)

        self.process.write_int(constraint_aspect_ratio_address, bitfield_value)

        return True

    def disable_mobile_game_trap(self) -> bool:
        if not self.is_process_running:
            return False

        camera_component_address: int = self._resolve_address(self.gworld_offset, (0x170, 0x340, 0x0, 0x3A0, 0x960, 0x0))

        if camera_component_address in (None, 0):
            return False

        aspect_ratio_address: int = camera_component_address + 0x2D0
        constraint_aspect_ratio_address: int = camera_component_address + 0x2D5

        self.process.write_float(aspect_ratio_address, 1.7777778)

        bitfield_value: int = self.process.read_int(constraint_aspect_ratio_address)
        bitfield_value &= ~(1 << 0)

        self.process.write_int(constraint_aspect_ratio_address, bitfield_value)

        return True

    def enable_slow_trap(self) -> bool:
        self.set_max_walk_speed(100.0)
        return True

    def disable_slow_trap(self) -> bool:
        self.set_max_walk_speed(400.0)
        return True

    def enable_tunnel_vision_trap(self) -> bool:
        if not self.is_process_running:
            return False

        camera_component_address: int = self._resolve_address(self.gworld_offset, (0x170, 0x340, 0x0, 0x3A0, 0x960, 0x0))

        if camera_component_address in (None, 0):
            return False

        override_vignette_intensity_address: int = camera_component_address + 0x3EC
        vignette_intensity_address: int = camera_component_address + 0x970

        bitfield_value: int = self.process.read_int(override_vignette_intensity_address)
        bitfield_value |= (1 << 0)

        self.process.write_int(override_vignette_intensity_address, bitfield_value)

        self.process.write_float(vignette_intensity_address, 7.0)

        return True

    def disable_tunnel_vision_trap(self) -> bool:
        if not self.is_process_running:
            return False

        camera_component_address: int = self._resolve_address(self.gworld_offset, (0x170, 0x340, 0x0, 0x3A0, 0x960, 0x0))

        if camera_component_address in (None, 0):
            return False

        override_vignette_intensity_address: int = camera_component_address + 0x3EC
        vignette_intensity_address: int = camera_component_address + 0x970

        bitfield_value: int = self.process.read_int(override_vignette_intensity_address)
        bitfield_value &= ~(1 << 0)

        self.process.write_int(override_vignette_intensity_address, bitfield_value)

        self.process.write_float(vignette_intensity_address, 0.4)

        return True

    def _generate_gnames_mapping(self):
        if not self.is_process_running:
            return

        mapping: Dict[int, str] = dict()

        gnames_pointer: int = self.process.base_address + self.gnames_offset
        blocks_base_address: int = gnames_pointer + 0x10

        try:
            table_data: bytes = self.process.read_bytes(blocks_base_address, 8192 * 8)
            block_pointers: Tuple[int, ...] = struct.unpack("<8192Q", table_data)
        except:
            return

        block_index: int
        block_pointer: int
        for block_index, block_pointer in enumerate(block_pointers):
            if not block_pointer:
                continue

            try:
                chunk_data: bytes = self.process.read_bytes(block_pointer, 0x20000)
            except:
                continue

            offset: int = 0
            while offset < 0x20000 - 2:
                header: int = int.from_bytes(chunk_data[offset: offset + 2], "little")

                if header == 0:
                    break

                is_wide: bool = header & 0x1
                length: int = header >> 6

                if length <= 0:
                    break

                name_index: int = (block_index << 16) | (offset // 2)

                start: int = offset + 2
                entry_size: int
                name: str

                if is_wide:
                    end: int = start + (length * 2)
                    name = chunk_data[start:end].decode("utf-16", errors="ignore")
                    entry_size = 2 + (length * 2)
                else:
                    end: int = start + length
                    name = chunk_data[start:end].decode("utf-8", errors="ignore")
                    entry_size = 2 + length

                mapping[name_index] = name

                offset += (entry_size + 1) & ~1

        self.gnames_mapping = mapping

    def _refresh_gobjects_mapping(self) -> None:
        if not self.is_process_running:
            return

        should_refresh: bool = self._should_refresh_gobjects_mapping()

        if not should_refresh:
            return

        self.gobjects_name_to_object = dict()
        self.gobjects_address_to_object = dict()

        gobjects_address: int = self.process.base_address + self.gobjects_offset

        chunks_pointer_base_address: int = self.process.read_longlong(gobjects_address + 0x0)
        element_count: int = self.process.read_int(gobjects_address + 0x14)

        chunk_index: int
        for chunk_index in range((element_count // 65536) + 1):
            chunk_address: int = self.process.read_longlong(chunks_pointer_base_address + (chunk_index * 8))

            if not chunk_address:
                continue

            bytes_to_read: int = min(65536, element_count - (chunk_index * 65536))

            chunk_bytes: bytes = self.process.read_bytes(chunk_address, bytes_to_read * 24)

            i: int
            for i in range(bytes_to_read):
                object_pointer: int
                internal_flags: int

                object_pointer, internal_flags = struct.unpack("<QI", chunk_bytes[(i * 24):(i * 24 + 12)])

                internal_flags_exclude_mask: int = 0x30200000  # Unreachable | PendingKill | Garbage

                if internal_flags & internal_flags_exclude_mask:
                    continue

                if object_pointer > 0x100000:
                    try:
                        header_bytes: bytes = self.process.read_bytes(object_pointer + 0x8, 32)

                        object_flags: int
                        class_pointer: int
                        name_index: int
                        name_number: int
                        outer_pointer: int

                        object_flags, _, class_pointer, name_index, name_number, outer_pointer = struct.unpack("<IIQIIQ", header_bytes)

                        object_flags_exclude_mask: int = 0x60018000  # RF_Garbage | RF_PendingKill | RF_BeginDestroyed | RF_FinishDestroyed

                        if object_flags & object_flags_exclude_mask:
                            continue

                        display_name: str = self.gnames_mapping.get(name_index, "Unknown Object")

                        if name_number > 0:
                            display_name = f"{display_name}_{name_number - 1}"

                        if display_name not in self.gobjects_name_to_object:
                            self.gobjects_name_to_object[display_name] = list()

                        self.gobjects_name_to_object[display_name].append({
                            "address": object_pointer,
                            "name": display_name,
                            "outer": outer_pointer,
                            "class": class_pointer,
                        })

                        self.gobjects_address_to_object[object_pointer] = {
                            "address": object_pointer,
                            "name": display_name,
                            "outer": outer_pointer,
                            "class": class_pointer,
                        }
                    except:
                        continue

    def _should_refresh_gobjects_mapping(self) -> bool:
        gworld_address: int = self._resolve_address(self.gworld_offset, (0x0,))

        try:
            levels_array_header_bytes: bytes = self.process.read_bytes(gworld_address + 0x188, 12)

            levels_array_address: int
            levels_array_size: int
            levels_array_address, levels_array_size = struct.unpack("<Qi", levels_array_header_bytes)
        except Exception:
            return False

        if levels_array_size == 0:
            return False

        try:
            levels_array_pointer_bytes: bytes = self.process.read_bytes(levels_array_address, levels_array_size * 8)
        except Exception:
            return False

        if levels_array_pointer_bytes != self.last_seen_levels_array_pointer_bytes:
            self.last_seen_levels_array_pointer_bytes = levels_array_pointer_bytes

            return True

        now_timestamp: int = int(time.time())

        if now_timestamp >= self.next_forced_gobjects_refresh:
            self.next_forced_gobjects_refresh = now_timestamp + 5
            return True

        return False

    def _call_process_event(self, instance_address: int, function_object_address: int, args_bytes: bytes, result_offset: int, result_type: str):
        args_address = None

        if args_bytes is not None:
            args_address = self.process.allocate(len(args_bytes))
            self.process.write_bytes(args_address, args_bytes, len(args_bytes))

        process_event_address = self.process.base_address + self.process_event_offset

        shellcode = b"\x48\x83\xEC\x28"  # sub rsp, 28h
        shellcode += b"\x48\xB9" + struct.pack("<Q", instance_address)  # mov rcx, instance_address
        shellcode += b"\x48\xBA" + struct.pack("<Q", function_object_address)  # mov rdx, function_object_address

        # mov r8, args_address (if applicable)
        if args_bytes is not None:
            shellcode += b"\x49\xB8" + struct.pack("<Q", args_address)
        else:
            shellcode += b"\x4D\x31\xC0"

        shellcode += b"\x48\xB8" + struct.pack("<Q", process_event_address)  # mov rax, process_event_address

        shellcode += b"\xFF\xD0"  # call rax
        shellcode += b"\x48\x83\xC4\x28"  # add rsp, 28h
        shellcode += b"\xC3"  # ret

        execution_address = self.process.allocate(len(shellcode))
        self.process.write_bytes(execution_address, shellcode, len(shellcode))

        thread_handle = self.process.start_thread(execution_address)
        ctypes.windll.kernel32.WaitForSingleObject(thread_handle, -1)

        result = True

        if args_bytes is not None and result_offset is not None:
            if result_type == "bool":
                result = self.process.read_bool(args_address + result_offset)
            elif result_type == "byte":
                result = self.process.read_char(args_address + result_offset)
            elif result_type == "int":
                result = self.process.read_int(args_address + result_offset)
            elif result_type == "float":
                result = self.process.read_float(args_address + result_offset)

        self.process.free(execution_address)

        if args_bytes is not None:
            self.process.free(args_address)

        ctypes.windll.kernel32.CloseHandle(thread_handle)

        return result

    def _determine_game_state_bools(self, tmap_address: int) -> Dict[str, bool]:
        if not self.is_process_running:
            return dict()

        try:
            header_bytes: bytes = self.process.read_bytes(tmap_address, 16)

            data_pointer: int
            count: int
            maximum: int

            data_pointer, count, maximum = struct.unpack("<Qii", header_bytes)

            if not data_pointer or count <= 0:
                return dict()

            stride: int = 0x50
            raw_data: bytes = self.process.read_bytes(data_pointer, maximum * stride)

            game_state: Dict[str, bool] = dict()

            i: int
            for i in range(maximum):
                offset: int = i * stride

                key_index = struct.unpack("<I", raw_data[offset: offset + 4])[0]

                if key_index not in self.gnames_mapping:
                    continue

                fname_index: int = struct.unpack("<I", raw_data[offset + 0x18: offset + 0x1C])[0]
                state_key: str = self.gnames_mapping.get(fname_index, f"Unknown")

                if state_key == "Unknown":
                    continue

                state_value: bool = raw_data[offset + 0x41] != 0

                game_state[state_key] = state_value
        except Exception:
            return dict()

        return game_state

    def _determine_game_state_ints(self, tmap_address: int) -> Dict[str, int]:
        if not self.is_process_running:
            return dict()

        try:
            header_bytes: bytes = self.process.read_bytes(tmap_address, 16)

            data_pointer: int
            count: int
            maximum: int

            data_pointer, count, maximum = struct.unpack("<Qii", header_bytes)

            if not data_pointer or count <= 0:
                return dict()

            stride: int = 0x50
            raw_data: bytes = self.process.read_bytes(data_pointer, maximum * stride)

            game_state: Dict[str, int] = dict()

            i: int
            for i in range(maximum):
                offset: int = i * stride

                key_index = struct.unpack("<I", raw_data[offset: offset + 4])[0]

                if key_index not in self.gnames_mapping:
                    continue

                fname_index: int = struct.unpack("<I", raw_data[offset + 0x18: offset + 0x1C])[0]
                state_key: str = self.gnames_mapping.get(fname_index, f"Unknown")

                if state_key == "Unknown":
                    continue

                state_value = struct.unpack("<i", raw_data[offset + 0x44:offset + 0x48])[0]

                game_state[state_key] = state_value
        except Exception:
            return dict()

        return game_state

    def _determine_game_state_floats(self, tmap_address: int) -> Dict[str, float]:
        if not self.is_process_running:
            return dict()

        try:
            header_bytes: bytes = self.process.read_bytes(tmap_address, 16)

            data_pointer: int
            count: int
            maximum: int

            data_pointer, count, maximum = struct.unpack("<Qii", header_bytes)

            if not data_pointer or count <= 0:
                return dict()

            stride: int = 0x50
            raw_data: bytes = self.process.read_bytes(data_pointer, maximum * stride)

            game_state: Dict[str, float] = dict()

            for i in range(maximum):
                offset: int = i * stride

                key_index: int = struct.unpack("<I", raw_data[offset:offset + 4])[0]

                if key_index not in self.gnames_mapping:
                    continue

                fname_index: int = struct.unpack("<I", raw_data[offset + 0x18:offset + 0x1C])[0]
                state_key: str = self.gnames_mapping.get(fname_index, "Unknown")

                if state_key == "Unknown":
                    continue

                state_value = struct.unpack("<f", raw_data[offset + 0x44:offset + 0x48])[0]

                game_state[state_key] = state_value

        except Exception:
            return dict()

        return game_state

    def _get_player_is_engaged(self) -> Optional[bool]:
        if not self.is_process_running:
            return None

        player_address: int = self._resolve_address(self.gworld_offset, (0x170, 0x340, 0x0, 0x3A0, 0x0))

        if player_address in (0, None):
            return None

        is_engaged_address: int = player_address + 0x725

        try:
            return self.process.read_bool(is_engaged_address)
        except Exception:
            pass

        return None

    def _get_engaged_instance_name(self) -> Optional[str]:
        if not self.is_process_running:
            return None

        engaged_object_address: int = self._resolve_address(self.gworld_offset, (0x170, 0x340, 0x0, 0x3A0, 0x738, 0x0))

        if engaged_object_address >0 and engaged_object_address in self.gobjects_address_to_object:
            return self.gobjects_address_to_object[engaged_object_address]["name"]

        return None

    def _get_left_aquarium_chair_arm_active_view(self) -> Optional[int]:
        if not self.is_process_running:
            return None

        if "SM_ViewerArm_Left" not in self.gobjects_name_to_object:
            return None

        left_aquarium_chair_arm_address: int = 0

        object_data: Dict[str, Any]
        for object_data in self.gobjects_name_to_object["SM_ViewerArm_Left"]:
            class_object_data: Dict[str, Any] = self.gobjects_address_to_object[object_data["class"]]

            if class_object_data["name"] == "BP_WahrkRoomChairLeftArm_C":
                left_aquarium_chair_arm_address = object_data["address"]
                break

        if left_aquarium_chair_arm_address == 0:
            return False

        media_player_busy_address: int = left_aquarium_chair_arm_address + 0x5A8

        is_media_player_busy: bool = False

        try:
            is_media_player_busy = self.process.read_bool(media_player_busy_address)
        except Exception:
            pass

        if not is_media_player_busy:
            return None

        current_selected_view_address: int = left_aquarium_chair_arm_address + 0x510

        try:
            current_selected_view: int = self.process.read_int(current_selected_view_address)
        except Exception:
            return None

        return current_selected_view

    def _get_right_aquarium_chair_arm_active_light(self) -> Optional[int]:
        if not self.is_process_running:
            return None

        if "SM_ViewerArm_Right_17" not in self.gobjects_name_to_object:
            return None

        right_aquarium_chair_arm_address: int = 0

        object_data: Dict[str, Any]
        for object_data in self.gobjects_name_to_object["SM_ViewerArm_Right_17"]:
            class_object_data: Dict[str, Any] = self.gobjects_address_to_object[object_data["class"]]

            if class_object_data["name"] == "BP_WahrkRoomChairRightArm_C":
                right_aquarium_chair_arm_address = object_data["address"]
                break

        if right_aquarium_chair_arm_address == 0:
            return False

        light_on_address: int = right_aquarium_chair_arm_address + 0x520

        is_light_on: bool = False

        try:
            is_light_on = self.process.read_bool(light_on_address)
        except Exception:
            pass

        if not is_light_on:
            return None

        scope_rotation_address: int = right_aquarium_chair_arm_address + 0x4C8

        try:
            scope_rotation: int = self.process.read_int(scope_rotation_address)
        except Exception:
            return None

        return scope_rotation

    def _resolve_address(self, base_offset: int, offsets: Tuple[int, ...]) -> Optional[int]:
        address: int = self.process.read_longlong(self.process.base_address + base_offset)

        for offset in offsets[:-1]:
            try:
                address = self.process.read_longlong(address + offset)
            except Exception:
                return None

        return address + offsets[-1]

from typing import Dict, List, NamedTuple, Optional, TypeVar

import struct

from pymem import Pymem
from pymem.process import close_handle

from .data.game_data import (
    TwentyMinutesWeaponData,
    character_button_index_to_character,
    map_root_object_name_to_map,
    weapon_button_index_to_weapon,
)

from .enums import TwentyMinutesCharacters, TwentyMinutesMaps, TwentyMinutesRunes, TwentyMinutesWeapons

from .unity_mono import MainThreadDispatcher, MonoResolver, read_mono_string


T = TypeVar("T")


class GameState(NamedTuple):
    is_valid: bool

    is_in_menu: Optional[bool] = None
    is_in_run: Optional[bool] = None

    current_map: Optional[TwentyMinutesMaps] = None
    character: Optional[TwentyMinutesCharacters] = None
    weapon: Optional[TwentyMinutesWeapons] = None

    time_elapsed: Optional[float] = None
    time_limit: Optional[float] = None

    player_level: Optional[int] = None
    number_of_powerup_choices: Optional[int] = None
    enemy_kill_count: Optional[int] = None

    current_health: Optional[int] = None
    current_temporary_health: Optional[int] = None
    maximum_health: Optional[int] = None
    maximum_health_base: Optional[int] = None
    maximum_temporary_health: Optional[int] = None


class RunAnchor(NamedTuple):
    game_timer_component_address: int
    game_timer_vtable_address: int
    player_health_address: int
    player_health_vtable_address: int
    game_controller_component_address: int
    player_xp_address: int
    score_calculator_component_address: int
    current_map: Optional[TwentyMinutesMaps]
    character: Optional[TwentyMinutesCharacters]
    weapon: Optional[TwentyMinutesWeapons]


class MenuAnchor(NamedTuple):
    difficulty_controller_component_address: int
    difficulty_controller_vtable_address: int


class GameStateManager:
    process_name: str = "MinutesTillDawn.exe"
    mono_dll_name: str = "mono-2.0-bdwgc.dll"

    process: Optional[Pymem]
    is_process_running: bool

    mono_resolver: Optional[MonoResolver]

    game_state: Optional[GameState]

    run_anchor: Optional[RunAnchor]
    menu_anchor: Optional[MenuAnchor]

    def __init__(self) -> None:
        self.process = None
        self.is_process_running = False

        self.mono_resolver = None

        self.game_state = GameState(is_valid=False)

        self.run_anchor = None
        self.menu_anchor = None

    def open_process_handle(self) -> bool:
        try:
            self.process = Pymem(self.process_name)
            self.is_process_running = True

            self.mono_resolver = MonoResolver(self.process, self.mono_dll_name)
        except Exception:
            return False

        return True

    def close_process_handle(self) -> bool:
        if close_handle(self.process.process_handle):
            self.is_process_running = False
            self.process = None

            self.mono_resolver = None

            self.game_state = GameState(is_valid=False)

            self.run_anchor = None
            self.menu_anchor = None

            return True

        return False

    def is_process_still_running(self) -> bool:
        try:
            self.process.read_int(self.process.base_address)
        except Exception:
            self.is_process_running = False
            self.process = None

            self.mono_resolver = None

            self.game_state = GameState(is_valid=False)

            self.run_anchor = None
            self.menu_anchor = None

            return False

        return True

    def install_main_thread_dispatcher(self) -> bool:
        if not self.is_process_running:
            return False

        if self.mono_resolver.main_thread_dispatcher is not None and self.mono_resolver.main_thread_dispatcher.is_installed:
            return True

        self.mono_resolver.main_thread_dispatcher = MainThreadDispatcher(self.mono_resolver)
        self.mono_resolver.main_thread_dispatcher.install()

        return True

    def determine_game_state(self) -> GameState:
        self.game_state = self._determine_game_state()
        return self.game_state

    def create_archipelago_label(self) -> Optional[int]:
        if not self.is_process_running:
            return None

        if not self.game_state.is_in_menu:
            return None

        existing_label_address: int = self.mono_resolver.find_game_object("ArchipelagoLabel")

        if existing_label_address not in (0, None):
            existing_label_transform_address: int = self.mono_resolver.get_transform(existing_label_address)
            existing_text_object_address: int = self.mono_resolver.find_child_by_name(existing_label_transform_address, "Text (TMP)")

            if existing_text_object_address not in (0, None):
                tmp_image_address: int = self.mono_resolver.get_image("Unity.TextMeshPro")
                tmp_text_class_address: int = self.mono_resolver.get_class(tmp_image_address, "TMPro", "TextMeshProUGUI")
                existing_tmp_component_address: int = self.mono_resolver.get_component(existing_text_object_address, tmp_text_class_address)

                self.mono_resolver.set_tmp_text(existing_tmp_component_address, "Archipelago Mod Loaded!")

            return existing_label_address

        label_address: int = self.mono_resolver.find_game_object("Canvas/TitleScreen/LanguageMenu/HungarianButton")

        if label_address in (0, None):
            return None

        canvas_address: int = self.mono_resolver.find_game_object("Canvas")

        if canvas_address in (0, None):
            return None

        canvas_transform_address: int = self.mono_resolver.get_transform(canvas_address)
        label_transform_address: int = self.mono_resolver.get_transform(label_address)

        self.mono_resolver.set_parent(label_transform_address, canvas_transform_address, False)
        self.mono_resolver.set_name(label_address, "ArchipelagoLabel")

        ui_image_address: int = self.mono_resolver.get_image("UnityEngine.UI")

        button_class_address: int = self.mono_resolver.get_class(ui_image_address, "UnityEngine.UI", "Button")
        button_component_address: int = self.mono_resolver.get_component(label_address, button_class_address)

        if button_component_address not in (0, None):
            self.mono_resolver.set_enabled(button_component_address, False)

        image_class_address: int = self.mono_resolver.get_class(ui_image_address, "UnityEngine.UI", "Image")
        image_component_address: int = self.mono_resolver.get_component(label_address, image_class_address)

        if image_component_address not in (0, None):
            self.mono_resolver.set_raycast_target(image_component_address, False)

        core_image_address: int = self.mono_resolver.get_image("UnityEngine")
        rect_transform_class_address: int = self.mono_resolver.get_class(core_image_address, "UnityEngine", "RectTransform")
        rect_transform_address: int = self.mono_resolver.get_component(label_address, rect_transform_class_address)

        self.mono_resolver.set_anchor_min(rect_transform_address, 1.0, 0.0)
        self.mono_resolver.set_anchor_max(rect_transform_address, 1.0, 0.0)
        self.mono_resolver.set_pivot(rect_transform_address, 1.0, 0.0)
        self.mono_resolver.set_anchored_position(rect_transform_address, 24.0, 4.0)

        text_object_address: int = self.mono_resolver.find_child_by_name(label_transform_address, "Text (TMP)")

        if text_object_address in (0, None):
            return label_address

        tmp_image_address: int = self.mono_resolver.get_image("Unity.TextMeshPro")
        tmp_text_class_address: int = self.mono_resolver.get_class(tmp_image_address, "TMPro", "TextMeshProUGUI")
        tmp_component_address: int = self.mono_resolver.get_component(text_object_address, tmp_text_class_address)

        self.mono_resolver.set_tmp_text(tmp_component_address, "Archipelago Mod Loaded!")

        assembly_image_address: int = self.mono_resolver.get_image("Assembly-CSharp")
        set_tmp_at_runtime_class_address: int = self.mono_resolver.get_class(assembly_image_address, "flanne.UI", "SetTMPAtRuntime")
        set_tmp_at_runtime_component_address: int = self.mono_resolver.get_component(label_address, set_tmp_at_runtime_class_address)

        if set_tmp_at_runtime_component_address in (0, None):
            set_tmp_at_runtime_component_address = self.mono_resolver.get_component(text_object_address, set_tmp_at_runtime_class_address)

        if set_tmp_at_runtime_component_address not in (0, None):
            text_field_offset: int = self.mono_resolver.get_instance_field_offset(set_tmp_at_runtime_class_address, "text")
            label_text_address: int = self.mono_resolver.new_string("Archipelago Mod Loaded!")

            self.process.write_longlong(set_tmp_at_runtime_component_address + text_field_offset, label_text_address)

        self.mono_resolver.set_tmp_font_size(tmp_component_address, 8.5)

        return label_address

    def set_unlocked_characters(self, unlocked_characters: List[TwentyMinutesCharacters]) -> bool:
        return self._set_unlocked_buttons(
            "Canvas/CharacterMenu/Buttons", character_button_index_to_character, unlocked_characters
        )

    def set_unlocked_weapons(self, unlocked_weapons: List[TwentyMinutesWeapons]) -> bool:
        return self._set_unlocked_buttons(
            "Canvas/GunMenu/Buttons", weapon_button_index_to_weapon, unlocked_weapons
        )

    def set_rune_levels(self, rune_levels: Dict[TwentyMinutesRunes, int]) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_menu:
            return False

        if not self._clear_rune_row_level_requirements():
            return False

        rune_unlocker_addresses: List[int] = self._get_rune_unlocker_addresses()
        runes: List[TwentyMinutesRunes] = list(TwentyMinutesRunes)

        if len(rune_unlocker_addresses) != len(runes):
            return False

        assembly_image_address: int = self.mono_resolver.get_image("Assembly-CSharp")
        rune_unlocker_class_address: int = self.mono_resolver.get_class(assembly_image_address, "flanne.UI", "RuneUnlocker")

        set_locked_method_address: int = self.mono_resolver.get_method(rune_unlocker_class_address, "set_locked", 1)
        set_level_method_address: int = self.mono_resolver.get_method(rune_unlocker_class_address, "set_level", 1)
        set_toggle_on_method_address: int = self.mono_resolver.get_method(rune_unlocker_class_address, "set_toggleOn", 1)

        processing_order: List[int] = sorted(range(len(runes)), key=lambda i: -((i % 12) // 3))

        rune_index: int
        for rune_index in processing_order:
            rune_unlocker_address: int = rune_unlocker_addresses[rune_index]
            rune: TwentyMinutesRunes = runes[rune_index]

            level: int = rune_levels.get(rune, 0)

            self._set_int32_property(set_locked_method_address, rune_unlocker_address, 0)
            self._set_int32_property(set_level_method_address, rune_unlocker_address, level)

            self.process.write_float(rune_unlocker_address + 0x6C, 999999.0)

            if level == 0:
                self._set_int32_property(set_toggle_on_method_address, rune_unlocker_address, 0)

        return True

    def hide_unsupported_game_modes(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_menu:
            return False

        mode_paths: List[str] = [
            "Canvas/ConfirmModePanel/ToggleGroup/QuickPlayMode",
            "Canvas/ConfirmModePanel/ToggleGroup/EndlessMode",
        ]

        mode_path: str
        for mode_path in mode_paths:
            mode_address: int = self.mono_resolver.find_game_object(mode_path)

            if mode_address in (0, None):
                return False

            self.mono_resolver.set_active(mode_address, False)

        standard_mode_address: int = self.mono_resolver.find_game_object("Canvas/ConfirmModePanel/ToggleGroup/StandardMode")

        if standard_mode_address not in (0, None):
            ui_image_address: int = self.mono_resolver.get_image("UnityEngine.UI")
            toggle_class_address: int = self.mono_resolver.get_class(ui_image_address, "UnityEngine.UI", "Toggle")
            toggle_component_address: int = self.mono_resolver.get_component(standard_mode_address, toggle_class_address)

            if toggle_component_address not in (0, None):
                set_is_on_method_address: int = self.mono_resolver.get_method(toggle_class_address, "set_isOn", 1)

                self._set_int32_property(set_is_on_method_address, toggle_component_address, 1)

        return True

    def set_available_maps(self, available_maps: List[TwentyMinutesMaps]) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_menu:
            return False

        available_map_set = set(available_maps)

        toggle_group_address: int = self.mono_resolver.find_game_object("Canvas/MapSelectPanel/ToggleGroup")

        if toggle_group_address in (0, None):
            return False

        toggle_group_transform_address: int = self.mono_resolver.get_transform(toggle_group_address)

        maps: List[TwentyMinutesMaps] = list(TwentyMinutesMaps)

        if self.mono_resolver.get_child_count(toggle_group_transform_address) != len(maps):
            return False

        assembly_image_address: int = self.mono_resolver.get_image("Assembly-CSharp")
        unlockable_class_address: int = self.mono_resolver.get_class(assembly_image_address, "flanne", "Unlockable")
        unlock_method_address: int = self.mono_resolver.get_method(unlockable_class_address, "Unlock", 0)

        ui_image_address: int = self.mono_resolver.get_image("UnityEngine.UI")
        toggle_class_address: int = self.mono_resolver.get_class(ui_image_address, "UnityEngine.UI", "Toggle")
        set_is_on_method_address: int = self.mono_resolver.get_method(toggle_class_address, "set_isOn", 1)
        is_on_field_offset: int = self.mono_resolver.get_instance_field_offset(toggle_class_address, "m_IsOn")

        selectable_class_address: int = self.mono_resolver.get_class(ui_image_address, "UnityEngine.UI", "Selectable")
        set_interactable_method_address: int = self.mono_resolver.get_method(selectable_class_address, "set_interactable", 1)
        colors_field_offset: int = self.mono_resolver.get_instance_field_offset(selectable_class_address, "m_Colors")
        disabled_color_bytes: bytes = struct.pack("<ffff", 0.1255, 0.102, 0.1412, 1.0)

        toggle_component_addresses: List[int] = list()

        map_index: int
        for map_index in range(len(maps)):
            child_transform_address: int = self.mono_resolver.get_child(toggle_group_transform_address, map_index)
            child_game_object_address: int = self.mono_resolver.get_game_object(child_transform_address)

            unlockable_component_address: int = self.mono_resolver.get_component(child_game_object_address, unlockable_class_address)

            if unlockable_component_address not in (0, None):
                self.mono_resolver.invoke(unlock_method_address, object_address=unlockable_component_address)

            toggle_component_address: int = self.mono_resolver.get_component(child_game_object_address, toggle_class_address)

            if toggle_component_address in (0, None):
                return False

            toggle_component_addresses.append(toggle_component_address)

            self.process.write_bytes(toggle_component_address + colors_field_offset + 64, disabled_color_bytes, 16)

            is_available: bool = maps[map_index] in available_map_set
            self._set_int32_property(set_interactable_method_address, toggle_component_address, 1 if is_available else 0)

        is_any_available_map_on: bool = False

        for map_index in range(len(maps)):
            if maps[map_index] in available_map_set:
                if self.process.read_bool(toggle_component_addresses[map_index] + is_on_field_offset):
                    is_any_available_map_on = True
                    break

        if not is_any_available_map_on:
            for map_index in range(len(maps)):
                if maps[map_index] in available_map_set:
                    self._set_int32_property(set_is_on_method_address, toggle_component_addresses[map_index], 1)
                    break

        return True

    def set_darkness_level(self, level: int) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_menu:
            return False

        ascension_mode_address: int = self.mono_resolver.find_game_object("Canvas/ConfirmModePanel/AscensionMode")

        if ascension_mode_address in (0, None):
            return False

        arrow_paths: List[str] = [
            "Canvas/ConfirmModePanel/AscensionMode/LeftArrow",
            "Canvas/ConfirmModePanel/AscensionMode/RightArrow",
        ]

        arrow_path: str
        for arrow_path in arrow_paths:
            arrow_address: int = self.mono_resolver.find_game_object(arrow_path)

            if arrow_address in (0, None):
                return False

            self.mono_resolver.set_active(arrow_address, False)

        assembly_image_address: int = self.mono_resolver.get_image("Assembly-CSharp")

        difficulty_controller_class_address: int = self.mono_resolver.get_class(assembly_image_address, "flanne.UI", "DifficultyController")
        difficulty_controller_component_address: int = self.mono_resolver.get_component(ascension_mode_address, difficulty_controller_class_address)

        if difficulty_controller_component_address in (0, None):
            return False

        self.process.write_int(difficulty_controller_component_address + 0x54, 15)

        set_difficulty_method_address: int = self.mono_resolver.get_method(difficulty_controller_class_address, "SetDifficulty", 1)

        self._set_int32_property(set_difficulty_method_address, difficulty_controller_component_address, level)

        difficulty_text_address: int = self.process.read_longlong(difficulty_controller_component_address + 0x30)

        if difficulty_text_address not in (0, None):
            tmp_image_address: int = self.mono_resolver.get_image("Unity.TextMeshPro")
            tmp_text_class_address: int = self.mono_resolver.get_class(tmp_image_address, "TMPro", "TMP_Text")
            set_alpha_method_address: int = self.mono_resolver.get_method(tmp_text_class_address, "set_alpha", 1)

            self._set_float_property(set_alpha_method_address, difficulty_text_address, 0.0)

        return True

    def set_time_limit(self, time_limit: float) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_run:
            return False

        game_timer_address: int = self.mono_resolver.find_game_object("GameTimer")

        if game_timer_address in (0, None):
            return False

        assembly_image_address: int = self.mono_resolver.get_image("Assembly-CSharp")
        game_timer_class_address: int = self.mono_resolver.get_class(assembly_image_address, "flanne", "GameTimer")
        game_timer_component_address: int = self.mono_resolver.get_component(game_timer_address, game_timer_class_address)

        if game_timer_component_address in (0, None):
            return False

        self.process.write_float(game_timer_component_address + 0x18, time_limit)

        return True

    def set_number_of_powerup_choices(self, number_of_powerup_choices: int) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_run:
            return False

        game_controller_component_address: Optional[int] = self._get_game_controller_component_address()

        if game_controller_component_address in (0, None):
            return False

        self.process.write_int(game_controller_component_address + 0x1D0, number_of_powerup_choices)

        return True

    def set_maximum_health_base(self, maximum_health_base: int) -> bool:
        if not self.is_process_running:
            return False
        if not self.game_state.is_in_run:
            return False

        player_health_address: Optional[int] = self._get_player_health_address()

        if player_health_address in (0, None):
            return False

        player_health_class_address: int = self._get_player_health_class_address()
        set_maximum_health_base_method_address: int = self.mono_resolver.get_method(player_health_class_address, "set_baseMaxHP", 1)

        self._set_int32_property(set_maximum_health_base_method_address, player_health_address, maximum_health_base)

        return True

    def set_maximum_temporary_health(self, maximum_temporary_health: int) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_run:
            return False

        player_health_address: Optional[int] = self._get_player_health_address()

        if player_health_address in (0, None):
            return False

        self.process.write_int(player_health_address + 0x88, maximum_temporary_health)

        return True

    def set_maximum_health(self, maximum_health: int) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_run:
            return False

        player_health_address: Optional[int] = self._get_player_health_address()

        if player_health_address in (0, None):
            return False

        player_health_class_address: int = self._get_player_health_class_address()
        set_maximum_health_method_address: int = self.mono_resolver.get_method(player_health_class_address, "set_maxHP", 1)

        self._set_int32_property(set_maximum_health_method_address, player_health_address, maximum_health)

        return True

    def set_current_health(self, current_health: int) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_run:
            return False

        player_health_address: Optional[int] = self._get_player_health_address()

        if player_health_address in (0, None):
            return False

        player_health_class_address: int = self._get_player_health_class_address()
        set_current_health_method_address: int = self.mono_resolver.get_method(player_health_class_address, "set_hp", 1)

        self._set_int32_property(set_current_health_method_address, player_health_address, current_health)

        return True

    def set_current_temporary_health(self, current_temporary_health: int) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_run:
            return False

        player_health_address: Optional[int] = self._get_player_health_address()

        if player_health_address in (0, None):
            return False

        player_health_class_address: int = self._get_player_health_class_address()
        set_current_temporary_health_method_address: int = self.mono_resolver.get_method(player_health_class_address, "set_shp", 1)

        self._set_int32_property(set_current_temporary_health_method_address, player_health_address, current_temporary_health)

        return True

    def kill_player(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_run:
            return False

        player_health_address: Optional[int] = self._get_player_health_address()

        if player_health_address in (0, None):
            return False

        current_health: int = self.process.read_int(player_health_address + 0x94)

        if current_health <= 0:
            return False

        player_health_class_address: int = self._get_player_health_class_address()
        auto_kill_method_address: int = self.mono_resolver.get_method(player_health_class_address, "AutoKill", 0)

        self.mono_resolver.invoke(auto_kill_method_address, object_address=player_health_address)

        return True

    def get_spawn_rate_multiplier(self) -> Optional[float]:
        if not self.is_process_running:
            return None

        if not self.game_state.is_in_run:
            return None

        horde_spawner_component_address: Optional[int] = self._get_horde_spawner_component_address()

        if horde_spawner_component_address in (0, None):
            return None

        return self.process.read_float(horde_spawner_component_address + 0x34)

    def set_spawn_rate_multiplier(self, spawn_rate_multiplier: float) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_run:
            return False

        horde_spawner_component_address: Optional[int] = self._get_horde_spawner_component_address()

        if horde_spawner_component_address in (0, None):
            return False

        self.process.write_float(horde_spawner_component_address + 0x34, spawn_rate_multiplier)

        return True

    def set_all_weapon_data(self, weapon_data_by_weapon: Dict[TwentyMinutesWeapons, TwentyMinutesWeaponData]) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_menu:
            return False

        assembly_image_address: int = self.mono_resolver.get_image("Assembly-CSharp")
        gun_data_class_address: int = self.mono_resolver.get_class(assembly_image_address, "flanne", "GunData")
        get_name_string_method_address: int = self.mono_resolver.get_method(gun_data_class_address, "get_nameString", 0)

        gun_data_addresses: List[int] = self.mono_resolver.find_objects_of_type_all(gun_data_class_address)

        if not gun_data_addresses:
            return False

        weapon_name_to_weapon: Dict[str, TwentyMinutesWeapons] = {
            candidate_weapon.value: candidate_weapon for candidate_weapon in TwentyMinutesWeapons
        }

        gun_data_address: int
        for gun_data_address in gun_data_addresses:
            weapon_name_address: int = self.mono_resolver.invoke(get_name_string_method_address, object_address=gun_data_address)
            weapon_name: Optional[str] = read_mono_string(self.process, weapon_name_address)

            weapon: Optional[TwentyMinutesWeapons] = weapon_name_to_weapon.get(weapon_name)

            if weapon is None or weapon not in weapon_data_by_weapon:
                continue

            weapon_data: TwentyMinutesWeaponData = weapon_data_by_weapon[weapon]

            weapon_data_bytes: bytes = struct.pack(
                "<ffififffiif",
                weapon_data.damage,
                weapon_data.shot_cooldown,
                weapon_data.maximum_ammunition,
                weapon_data.reload_time,
                weapon_data.number_of_projectiles,
                weapon_data.spread,
                weapon_data.knockback,
                weapon_data.projectile_speed,
                weapon_data.bounce,
                weapon_data.piercing,
                weapon_data.inaccuracy,
            )

            self.process.write_bytes(gun_data_address + 0x58, weapon_data_bytes, len(weapon_data_bytes))

        return True

    def disable_player_movement(self) -> bool:
        return self._set_bool_toggle_via_event(0xA0, True)

    def enable_player_movement(self) -> bool:
        return self._set_bool_toggle_via_event(0xA0, False)

    def disable_player_actions(self) -> bool:
        return self._set_bool_toggle_via_event(0xA8, True)

    def enable_player_actions(self) -> bool:
        return self._set_bool_toggle_via_event(0xA8, False)

    def enable_horde_trap(self, spawn_rate_multiplier: float) -> bool:
        return self.set_spawn_rate_multiplier(spawn_rate_multiplier)

    def disable_horde_trap(self, spawn_rate_multiplier: float) -> bool:
        return self.set_spawn_rate_multiplier(spawn_rate_multiplier)

    def enable_paralysis_trap(self) -> bool:
        return self.disable_player_movement()

    def disable_paralysis_trap(self) -> bool:
        return self.enable_player_movement()

    def enable_weapon_malfunction_trap(self) -> bool:
        return self.disable_player_actions()

    def disable_weapon_malfunction_trap(self) -> bool:
        return self.enable_player_actions()

    def enable_wound_trap(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_run:
            return False

        if self.game_state.current_health is None or self.game_state.current_health <= 2:
            return False

        return self.set_current_health(2)

    def disable_wound_trap(self) -> bool:
        # Wound damage is instantaneous; there is nothing to revert once applied
        return True

    def _set_int32_property(self, method_address: int, target_address: int, value: int) -> None:
        value_address: int = self.mono_resolver.caller.write_int32_to_buffer(value)
        params_address: int = self.mono_resolver.caller.write_pointer_array_to_buffer([value_address])

        self.mono_resolver.invoke(method_address, object_address=target_address, params_address=params_address)

    def _set_float_property(self, method_address: int, target_address: int, value: float) -> None:
        value_address: int = self.mono_resolver.caller.write_float_to_buffer(value)
        params_address: int = self.mono_resolver.caller.write_pointer_array_to_buffer([value_address])

        self.mono_resolver.invoke(method_address, object_address=target_address, params_address=params_address)

    def _set_unlocked_buttons(self, buttons_path: str, index_to_item: Dict[int, T], unlocked_items: List[T]) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_menu:
            return False

        unlocked_item_set = set(unlocked_items)

        buttons_address: int = self.mono_resolver.find_game_object(buttons_path)

        if buttons_address in (0, None):
            return False

        buttons_transform_address: int = self.mono_resolver.get_transform(buttons_address)

        assembly_image_address: int = self.mono_resolver.get_image("Assembly-CSharp")
        unlockable_class_address: int = self.mono_resolver.get_class(assembly_image_address, "flanne", "Unlockable")

        unlockable_addresses: List[int] = self.mono_resolver.get_components_in_children(
            buttons_transform_address, unlockable_class_address, include_inactive=True
        )

        lock_method_address: int = self.mono_resolver.get_method(unlockable_class_address, "Lock", 0)
        unlock_method_address: int = self.mono_resolver.get_method(unlockable_class_address, "Unlock", 0)

        unlockable_index: int
        unlockable_address: int
        for unlockable_index, unlockable_address in enumerate(unlockable_addresses):
            item: Optional[T] = index_to_item.get(unlockable_index)

            if item is None:
                continue

            method_address: int = unlock_method_address if item in unlocked_item_set else lock_method_address

            self.mono_resolver.invoke(method_address, object_address=unlockable_address)

        return True

    def _get_player_health_class_address(self) -> int:
        assembly_image_address: int = self.mono_resolver.get_image("Assembly-CSharp")
        return self.mono_resolver.get_class(assembly_image_address, "flanne", "PlayerHealth")

    def _get_game_controller_component_address(self) -> Optional[int]:
        game_controller_address: int = self.mono_resolver.find_game_object("GameController")

        if game_controller_address in (0, None):
            return None

        assembly_image_address: int = self.mono_resolver.get_image("Assembly-CSharp")
        game_controller_class_address: int = self.mono_resolver.get_class(assembly_image_address, "flanne.Core", "GameController")
        game_controller_component_address: int = self.mono_resolver.get_component(game_controller_address, game_controller_class_address)

        if game_controller_component_address in (0, None):
            return None

        return game_controller_component_address

    def _get_player_xp_address(self) -> Optional[int]:
        game_controller_component_address: Optional[int] = self._get_game_controller_component_address()

        if game_controller_component_address in (0, None):
            return None

        player_xp_address: int = self.process.read_longlong(game_controller_component_address + 0x48)

        if player_xp_address in (0, None):
            return None

        return player_xp_address

    def _get_horde_spawner_component_address(self) -> Optional[int]:
        horde_spawner_address: int = self.mono_resolver.find_game_object("EnemySpawners/HordeSpawner")

        if horde_spawner_address in (0, None):
            return None

        assembly_image_address: int = self.mono_resolver.get_image("Assembly-CSharp")
        horde_spawner_class_address: int = self.mono_resolver.get_class(assembly_image_address, "flanne", "HordeSpawner")
        horde_spawner_component_address: int = self.mono_resolver.get_component(horde_spawner_address, horde_spawner_class_address)

        if horde_spawner_component_address in (0, None):
            return None

        return horde_spawner_component_address

    def _get_score_calculator_component_address(self) -> Optional[int]:
        score_calculator_address: int = self.mono_resolver.find_game_object("ScoreCalculator")

        if score_calculator_address in (0, None):
            return None

        assembly_image_address: int = self.mono_resolver.get_image("Assembly-CSharp")
        score_calculator_class_address: int = self.mono_resolver.get_class(assembly_image_address, "flanne", "ScoreCalculator")
        score_calculator_component_address: int = self.mono_resolver.get_component(score_calculator_address, score_calculator_class_address)

        if score_calculator_component_address in (0, None):
            return None

        return score_calculator_component_address

    def _get_player_controller_component_address(self) -> Optional[int]:
        game_controller_component_address: Optional[int] = self._get_game_controller_component_address()

        if game_controller_component_address in (0, None):
            return None

        player_game_object_address: int = self.process.read_longlong(game_controller_component_address + 0x38)

        if player_game_object_address in (0, None):
            return None

        assembly_image_address: int = self.mono_resolver.get_image("Assembly-CSharp")
        player_controller_class_address: int = self.mono_resolver.get_class(assembly_image_address, "flanne", "PlayerController")
        player_controller_component_address: int = self.mono_resolver.get_component(player_game_object_address, player_controller_class_address)

        if player_controller_component_address in (0, None):
            return None

        return player_controller_component_address

    def _get_player_health_address(self) -> Optional[int]:
        player_controller_component_address: Optional[int] = self._get_player_controller_component_address()

        if player_controller_component_address in (0, None):
            return None

        player_health_address: int = self.process.read_longlong(player_controller_component_address + 0x40)

        if player_health_address in (0, None):
            return None

        return player_health_address

    def _get_gun_address(self) -> Optional[int]:
        player_controller_component_address: Optional[int] = self._get_player_controller_component_address()

        if player_controller_component_address in (0, None):
            return None

        gun_address: int = self.process.read_longlong(player_controller_component_address + 0x58)

        if gun_address in (0, None):
            return None

        return gun_address

    def _get_gun_data_address(self) -> Optional[int]:
        gun_address: Optional[int] = self._get_gun_address()

        if gun_address in (0, None):
            return None

        gun_data_address: int = self.process.read_longlong(gun_address + 0x38)

        if gun_data_address in (0, None):
            return None

        return gun_data_address

    def _get_character_data_address(self) -> Optional[int]:
        player_controller_component_address: Optional[int] = self._get_player_controller_component_address()

        if player_controller_component_address in (0, None):
            return None

        character_data_address: int = self.process.read_longlong(player_controller_component_address + 0x70)

        if character_data_address in (0, None):
            return None

        return character_data_address

    def _get_rune_unlocker_addresses(self) -> List[int]:
        assembly_image_address: int = self.mono_resolver.get_image("Assembly-CSharp")
        rune_unlocker_class_address: int = self.mono_resolver.get_class(assembly_image_address, "flanne.UI", "RuneUnlocker")

        row_paths: List[str] = [
            "Canvas/RunesPanel/TreeLayout/SwordRuneTree/RuneRow",
            "Canvas/RunesPanel/TreeLayout/SwordRuneTree/RuneRow (1)",
            "Canvas/RunesPanel/TreeLayout/SwordRuneTree/RuneRow (2)",
            "Canvas/RunesPanel/TreeLayout/SwordRuneTree/RuneRow (3)",
            "Canvas/RunesPanel/TreeLayout/ShieldRuneTree/RuneRow",
            "Canvas/RunesPanel/TreeLayout/ShieldRuneTree/RuneRow (1)",
            "Canvas/RunesPanel/TreeLayout/ShieldRuneTree/RuneRow (2)",
            "Canvas/RunesPanel/TreeLayout/ShieldRuneTree/RuneRow (3)",
        ]

        rune_unlocker_addresses: List[int] = list()

        row_path: str
        for row_path in row_paths:
            row_address: int = self.mono_resolver.find_game_object(row_path)

            if row_address in (0, None):
                return list()

            row_transform_address: int = self.mono_resolver.get_transform(row_address)

            rune_unlocker_addresses.extend(
                self.mono_resolver.get_components_in_children(row_transform_address, rune_unlocker_class_address, include_inactive=True)
            )

        return rune_unlocker_addresses

    def _clear_rune_row_level_requirements(self) -> bool:
        assembly_image_address: int = self.mono_resolver.get_image("Assembly-CSharp")
        rune_row_ui_class_address: int = self.mono_resolver.get_class(assembly_image_address, "flanne.UI", "RuneRowUI")
        level_requirement_field_offset: int = self.mono_resolver.get_instance_field_offset(rune_row_ui_class_address, "levelRequirement")

        row_paths: List[str] = [
            "Canvas/RunesPanel/TreeLayout/SwordRuneTree/RuneRow",
            "Canvas/RunesPanel/TreeLayout/SwordRuneTree/RuneRow (1)",
            "Canvas/RunesPanel/TreeLayout/SwordRuneTree/RuneRow (2)",
            "Canvas/RunesPanel/TreeLayout/SwordRuneTree/RuneRow (3)",
            "Canvas/RunesPanel/TreeLayout/ShieldRuneTree/RuneRow",
            "Canvas/RunesPanel/TreeLayout/ShieldRuneTree/RuneRow (1)",
            "Canvas/RunesPanel/TreeLayout/ShieldRuneTree/RuneRow (2)",
            "Canvas/RunesPanel/TreeLayout/ShieldRuneTree/RuneRow (3)",
        ]

        row_path: str
        for row_path in row_paths:
            row_address: int = self.mono_resolver.find_game_object(row_path)

            if row_address in (0, None):
                return False

            rune_row_ui_component_address: int = self.mono_resolver.get_component(row_address, rune_row_ui_class_address)

            if rune_row_ui_component_address in (0, None):
                return False

            self.process.write_int(rune_row_ui_component_address + level_requirement_field_offset, 0)

        return True

    def _set_bool_toggle_via_event(self, field_offset: int, disabled: bool) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_run:
            return False

        player_controller_component_address: Optional[int] = self._get_player_controller_component_address()

        if player_controller_component_address in (0, None):
            return False

        bool_toggle_address: int = self.process.read_longlong(player_controller_component_address + field_offset)

        if bool_toggle_address in (0, None):
            return False

        assembly_image_address: int = self.mono_resolver.get_image("Assembly-CSharp")
        bool_toggle_class_address: int = self.mono_resolver.get_class(assembly_image_address, "flanne", "BoolToggle")

        current_flip: int = self.process.read_int(bool_toggle_address + 0x1C)

        if disabled:
            if current_flip == 0:
                flip_method_address: int = self.mono_resolver.get_method(bool_toggle_class_address, "Flip", 0)

                self.mono_resolver.invoke(flip_method_address, object_address=bool_toggle_address)
        else:
            flip_method_address: int = self.mono_resolver.get_method(bool_toggle_class_address, "Flip", 0)
            unflip_method_address: int = self.mono_resolver.get_method(bool_toggle_class_address, "UnFlip", 0)

            attempt: int
            for attempt in range(40):
                if current_flip == 0:
                    break

                if current_flip > 0:
                    self.mono_resolver.invoke(unflip_method_address, object_address=bool_toggle_address)
                else:
                    self.mono_resolver.invoke(flip_method_address, object_address=bool_toggle_address)

                current_flip = self.process.read_int(bool_toggle_address + 0x1C)

        return True

    def _determine_game_state(self) -> GameState:
        if not self.is_process_running:
            return GameState(is_valid=False)

        if self.run_anchor is not None:
            if self._is_anchor_alive(self.run_anchor.game_timer_component_address, self.run_anchor.game_timer_vtable_address):
                if self._is_anchor_alive(self.run_anchor.player_health_address, self.run_anchor.player_health_vtable_address):
                    run_game_state: Optional[GameState] = self._read_run_game_state(self.run_anchor)

                    if run_game_state is not None:
                        return run_game_state

            self.run_anchor = None

        if self.menu_anchor is not None:
            if self._is_anchor_alive(self.menu_anchor.difficulty_controller_component_address, self.menu_anchor.difficulty_controller_vtable_address):
                return GameState(is_valid=True, is_in_menu=True, is_in_run=False)

            self.menu_anchor = None

        try:
            loaded_scene_names: List[str] = self.mono_resolver.get_loaded_scene_names()
        except Exception:
            return GameState(is_valid=False)

        is_in_menu: bool = "TitleScreen" in loaded_scene_names
        is_in_run: bool = "Battle" in loaded_scene_names

        if is_in_menu == is_in_run:
            return GameState(is_valid=False)

        if is_in_run:
            try:
                self.run_anchor = self._resolve_run_anchor()
            except Exception:
                self.run_anchor = None

            if self.run_anchor is None:
                return GameState(is_valid=False)

            run_game_state = self._read_run_game_state(self.run_anchor)

            if run_game_state is None:
                self.run_anchor = None
                return GameState(is_valid=False)

            return run_game_state

        try:
            self.menu_anchor = self._resolve_menu_anchor()
        except Exception:
            self.menu_anchor = None

        if self.menu_anchor is None:
            return GameState(is_valid=False)

        return GameState(is_valid=True, is_in_menu=True, is_in_run=False)

    def _is_anchor_alive(self, component_address: int, vtable_address: int) -> bool:
        try:
            if self.process.read_longlong(component_address) != vtable_address:
                return False

            return self.process.read_longlong(component_address + 0x10) != 0
        except Exception:
            return False

    def _resolve_run_anchor(self) -> Optional[RunAnchor]:
        game_timer_address: int = self.mono_resolver.find_game_object("GameTimer")

        if game_timer_address in (0, None):
            return None

        assembly_image_address: int = self.mono_resolver.get_image("Assembly-CSharp")
        game_timer_class_address: int = self.mono_resolver.get_class(assembly_image_address, "flanne", "GameTimer")
        game_timer_component_address: int = self.mono_resolver.get_component(game_timer_address, game_timer_class_address)

        if game_timer_component_address in (0, None):
            return None

        time_elapsed: float = self.process.read_float(game_timer_component_address + 0x20)

        if time_elapsed <= 0.0:
            return None

        game_controller_component_address: Optional[int] = self._get_game_controller_component_address()
        player_health_address: Optional[int] = self._get_player_health_address()
        player_xp_address: Optional[int] = self._get_player_xp_address()
        score_calculator_component_address: Optional[int] = self._get_score_calculator_component_address()

        if None in (game_controller_component_address, player_health_address, player_xp_address, score_calculator_component_address):
            return None

        current_map: Optional[TwentyMinutesMaps] = None

        map_root_object_name: str
        candidate_map: TwentyMinutesMaps
        for map_root_object_name, candidate_map in map_root_object_name_to_map.items():
            map_root_address: int = self.mono_resolver.find_game_object(map_root_object_name)

            if map_root_address not in (0, None):
                current_map = candidate_map
                break

        character: Optional[TwentyMinutesCharacters] = None

        character_data_address: Optional[int] = self._get_character_data_address()

        if character_data_address not in (0, None):
            character_data_class_address: int = self.mono_resolver.get_class(assembly_image_address, "flanne", "CharacterData")
            get_character_name_string_method_address: int = self.mono_resolver.get_method(character_data_class_address, "get_nameString", 0)

            character_name_address: int = self.mono_resolver.invoke(get_character_name_string_method_address, object_address=character_data_address)
            character_name: Optional[str] = read_mono_string(self.process, character_name_address)

            if character_name is not None:
                character_name_to_character: Dict[str, TwentyMinutesCharacters] = {
                    candidate_character.value: candidate_character for candidate_character in TwentyMinutesCharacters
                }
                character = character_name_to_character.get(character_name)

        weapon: Optional[TwentyMinutesWeapons] = None

        gun_data_address: Optional[int] = self._get_gun_data_address()

        if gun_data_address not in (0, None):
            gun_data_class_address: int = self.mono_resolver.get_class(assembly_image_address, "flanne", "GunData")
            get_weapon_name_string_method_address: int = self.mono_resolver.get_method(gun_data_class_address, "get_nameString", 0)

            weapon_name_address: int = self.mono_resolver.invoke(get_weapon_name_string_method_address, object_address=gun_data_address)
            weapon_name: Optional[str] = read_mono_string(self.process, weapon_name_address)

            if weapon_name is not None:
                weapon_name_to_weapon: Dict[str, TwentyMinutesWeapons] = {
                    candidate_weapon.value: candidate_weapon for candidate_weapon in TwentyMinutesWeapons
                }
                weapon = weapon_name_to_weapon.get(weapon_name)

        return RunAnchor(
            game_timer_component_address=game_timer_component_address,
            game_timer_vtable_address=self.process.read_longlong(game_timer_component_address),
            player_health_address=player_health_address,
            player_health_vtable_address=self.process.read_longlong(player_health_address),
            game_controller_component_address=game_controller_component_address,
            player_xp_address=player_xp_address,
            score_calculator_component_address=score_calculator_component_address,
            current_map=current_map,
            character=character,
            weapon=weapon,
        )

    def _resolve_menu_anchor(self) -> Optional[MenuAnchor]:
        ascension_mode_address: int = self.mono_resolver.find_game_object("Canvas/ConfirmModePanel/AscensionMode")

        if ascension_mode_address in (0, None):
            return None

        assembly_image_address: int = self.mono_resolver.get_image("Assembly-CSharp")
        difficulty_controller_class_address: int = self.mono_resolver.get_class(assembly_image_address, "flanne.UI", "DifficultyController")
        difficulty_controller_component_address: int = self.mono_resolver.get_component(ascension_mode_address, difficulty_controller_class_address)

        if difficulty_controller_component_address in (0, None):
            return None

        return MenuAnchor(
            difficulty_controller_component_address=difficulty_controller_component_address,
            difficulty_controller_vtable_address=self.process.read_longlong(difficulty_controller_component_address),
        )

    def _read_run_game_state(self, run_anchor: RunAnchor) -> Optional[GameState]:
        try:
            time_limit: float = self.process.read_float(run_anchor.game_timer_component_address + 0x18)
            time_elapsed: float = self.process.read_float(run_anchor.game_timer_component_address + 0x20)

            player_level: int = self.process.read_int(run_anchor.player_xp_address + 0x38)
            number_of_powerup_choices: int = self.process.read_int(run_anchor.game_controller_component_address + 0x1D0)
            enemy_kill_count: int = self.process.read_int(run_anchor.score_calculator_component_address + 0x28)

            current_health: int = self.process.read_int(run_anchor.player_health_address + 0x94)
            current_temporary_health: int = self.process.read_int(run_anchor.player_health_address + 0x98)
            maximum_health: int = self.process.read_int(run_anchor.player_health_address + 0x90)
            maximum_health_base: int = self.process.read_int(run_anchor.player_health_address + 0x8C)
            maximum_temporary_health: int = self.process.read_int(run_anchor.player_health_address + 0x88)
        except Exception:
            return None

        return GameState(
            is_valid=True,
            is_in_menu=False,
            is_in_run=True,
            current_map=run_anchor.current_map,
            character=run_anchor.character,
            weapon=run_anchor.weapon,
            time_elapsed=time_elapsed,
            time_limit=time_limit,
            player_level=player_level,
            number_of_powerup_choices=number_of_powerup_choices,
            enemy_kill_count=enemy_kill_count,
            current_health=current_health,
            current_temporary_health=current_temporary_health,
            maximum_health=maximum_health,
            maximum_health_base=maximum_health_base,
            maximum_temporary_health=maximum_temporary_health,
        )

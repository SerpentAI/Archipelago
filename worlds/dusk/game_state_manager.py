from typing import Dict, List, NamedTuple, Optional, Set, Tuple

import math
import struct

import pymem.process

from pymem import Pymem

from .data.game_data import (
    DuskWeaponLoadout,
    difficulty_value_to_difficulty,
    episode_to_levels,
    level_to_all_kill_count,
    scene_name_to_endless_level,
    scene_name_to_level,
    selected_weapon_index_to_weapon,
    weapon_to_weapon_internal_index,
)

from .enums import DuskDifficulties, DuskKeys, DuskEndlessLevels, DuskLevels, DuskWeapons

from .unity_mono import MonoResolver, write_mono_bool_array_element, write_mono_float_array_element


class GameState(NamedTuple):
    is_valid: bool

    is_in_menu: Optional[bool] = None
    is_on_map_select: Optional[bool] = None
    is_in_endless_level: Optional[bool] = None
    is_in_level: Optional[bool] = None
    is_on_level_complete: Optional[bool] = None

    map_select_episode: Optional[int] = None

    difficulty: Optional[DuskDifficulties] = None
    selected_weapon: Optional[DuskWeapons] = None

    is_in_water: Optional[bool] = None
    is_dead: Optional[bool] = None

    level: Optional[DuskLevels] = None

    remaining_pickups: Optional[Set[str]] = None
    remaining_enemies: Optional[Set[str]] = None

    was_soap_picked_up: Optional[bool] = None

    got_all_kill: Optional[bool] = None
    got_completionist: Optional[bool] = None
    got_low_tech: Optional[bool] = None
    got_pacifist: Optional[bool] = None
    got_untouchable: Optional[bool] = None

    endless_level: Optional[DuskEndlessLevels] = None

    endless_kill_count: Optional[int] = None
    endless_score: Optional[int] = None
    endless_multiplier: Optional[float] = None


class GameStateManager:
    process_name: str = "DUSK.exe"

    process: Optional[Pymem]
    is_process_running: bool

    resolver: Optional[MonoResolver]

    last_seen_level: Optional[DuskLevels]

    game_state: Optional[GameState]

    def __init__(self) -> None:
        self.process = None
        self.is_process_running = False

        self.resolver = None

        self.last_seen_level = None

        self.game_state = GameState(is_valid=False)

    def open_process_handle(self) -> bool:
        try:
            self.process = Pymem(self.process_name)
            self.is_process_running = True

            self.resolver = MonoResolver(self.process)
        except Exception:
            return False

        return True

    def close_process_handle(self) -> bool:
        if pymem.process.close_handle(self.process.process_handle):
            self.is_process_running = False
            self.process = None

            self.resolver = None

            self.last_seen_level = None

            self.game_state = GameState(is_valid=False)

            return True

        return False

    def is_process_still_running(self) -> bool:
        try:
            self.process.read_int(self.process.base_address)
        except Exception:
            self.is_process_running = False
            self.process = None

            self.resolver = None

            self.last_seen_level = None

            self.game_state = GameState(is_valid=False)

            return False

        return True

    def determine_game_state(self) -> GameState:
        self.game_state = self._determine_game_state()
        return self.game_state

    def create_archipelago_label(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_menu:
            return False

        try:
            existing_label_address: int = self.resolver.find_game_object("ArchipelagoLabel")

            if existing_label_address not in (0, None):
                return True

            source_button_address: int = self.resolver.find_game_object("SettingsButton")

            if source_button_address in (0, None):
                return False

            canvas_address: int = self.resolver.find_game_object("Canvas")

            if canvas_address in (0, None):
                return False

            canvas_transform_address: int = self.resolver.get_transform(canvas_address)

            label_address: int = self.resolver.instantiate(source_button_address, canvas_transform_address)

            if label_address in (0, None):
                return False

            self.resolver.set_active(label_address, True)
            self.resolver.set_name(label_address, "ArchipelagoLabel")

            label_transform_address: int = self.resolver.get_transform(label_address)
            text_child_transform_address: int = self.resolver.get_child(label_transform_address, 0)
            text_child_game_object_address: int = self.resolver.get_game_object(text_child_transform_address)

            core_image_address: int = self.resolver.get_image("UnityEngine.CoreModule")
            ui_image_address: int = self.resolver.get_image("UnityEngine.UI")

            ui_text_class_address: int = self.resolver.get_class(ui_image_address, "UnityEngine.UI", "Text")
            text_component_address: int = self.resolver.get_component(text_child_game_object_address, ui_text_class_address)

            if text_component_address in (0, None):
                return False

            self.resolver.set_text(text_component_address, "Archipelago Mod Loaded!")
            self.resolver.set_font_size(text_component_address, 24)

            rect_transform_class_address: int = self.resolver.get_class(core_image_address, "UnityEngine", "RectTransform")
            rect_transform_address: int = self.resolver.get_component(label_address, rect_transform_class_address)

            if rect_transform_address in (0, None):
                return False

            current_x, current_y = self.resolver.get_anchored_position(rect_transform_address)
            self.resolver.set_anchored_position(rect_transform_address, current_x, current_y - 260)

            ui_button_class_address: int = self.resolver.get_class(ui_image_address, "UnityEngine.UI", "Button")
            button_component_address: int = self.resolver.get_component(label_address, ui_button_class_address)

            if button_component_address in (0, None):
                return False

            self.resolver.set_enabled(button_component_address, False)
        except Exception:
            return False

        return True

    def hide_menu_button(self, button_name: str) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_menu and not self.game_state.is_in_level and not self.game_state.is_in_endless_level:
            return False

        try:
            canvas_address: int = self.resolver.find_game_object("Canvas")

            if canvas_address in (0, None):
                return False

            canvas_transform_address: int = self.resolver.get_transform(canvas_address)
            button_address: int = self.resolver.find_child_by_name(canvas_transform_address, button_name)

            if button_address in (0, None):
                return False

            self.resolver.set_active(button_address, False)
        except Exception:
            return False

        return True

    def show_menu_button(self, button_name: str) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_menu and not self.game_state.is_in_level and not self.game_state.is_in_endless_level:
            return False

        try:
            canvas_address: int = self.resolver.find_game_object("Canvas")

            if canvas_address in (0, None):
                return False

            canvas_transform_address: int = self.resolver.get_transform(canvas_address)
            button_address: int = self.resolver.find_child_by_name(canvas_transform_address, button_name)

            if button_address in (0, None):
                return False

            self.resolver.set_active(button_address, True)
        except Exception:
            return False

        return True

    def hide_campaign_menu_button(self) -> bool:
        return self.hide_menu_button("CampaignMenuButton")

    def set_unlocked_endless_level_buttons(self, unlocked_endless_levels: List[DuskEndlessLevels]) -> bool:
        unlocked_endless_levels_set: Set[DuskEndlessLevels] = set(unlocked_endless_levels)

        endless_level_button_names: Dict[DuskEndlessLevels, str] = {
            DuskEndlessLevels.EL1: "EndlessButton",
            DuskEndlessLevels.EL2: "EndlessButton2",
            DuskEndlessLevels.EL3: "EndlessButton3",
        }

        results: List[bool] = list()

        level: DuskEndlessLevels
        button_name: str
        for level, button_name in endless_level_button_names.items():
            if level in unlocked_endless_levels_set:
                results.append(self.show_menu_button(button_name))
            else:
                results.append(self.hide_menu_button(button_name))

        return all(results)

    def set_unlocked_levels(self, unlocked_levels: List[DuskLevels]) -> bool:
        results: List[bool] = list()

        results.append(self.set_unlocked_level_buttons(unlocked_levels))
        results.append(self.set_unlocked_level_icons(unlocked_levels))

        return all(results)

    def set_unlocked_level_buttons(self, unlocked_levels: List[DuskLevels]) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_on_map_select or self.game_state.map_select_episode is None:
            return False

        try:
            levels_in_episode: Tuple[DuskLevels, ...] = episode_to_levels[self.game_state.map_select_episode]
            unlocked_levels_set: Set[DuskLevels] = set(unlocked_levels)

            buttons_root_address: int = self.resolver.find_game_object("Buttons")

            if buttons_root_address in (0, None):
                return False

            buttons_transform_address: int = self.resolver.get_transform(buttons_root_address)
            button_count: int = self.resolver.get_child_count(buttons_transform_address)

            if button_count != len(levels_in_episode):
                return False

            button_index: int
            for button_index in range(button_count):
                level: DuskLevels = levels_in_episode[button_index]
                is_unlocked: bool = level in unlocked_levels_set

                button_transform_address: int = self.resolver.get_child(buttons_transform_address, button_index)
                button_game_object_address: int = self.resolver.get_game_object(button_transform_address)

                self.resolver.set_active(button_game_object_address, is_unlocked)
        except Exception:
            return False

        return True

    def set_unlocked_level_icons(self, unlocked_levels: List[DuskLevels]) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_on_map_select or self.game_state.map_select_episode is None:
            return False

        map_image_root_name: Optional[str] = {
            1: "EP1mapimage", 2: "EP2mapimage", 3: "EP2mapimage"
        }.get(self.game_state.map_select_episode)

        if map_image_root_name is None:
            return False

        try:
            unlocked_levels_set: Set[DuskLevels] = set(unlocked_levels)

            map_image_root_address: int = self.resolver.find_game_object(map_image_root_name)

            if map_image_root_address in (0, None):
                return False

            map_image_transform_address: int = self.resolver.get_transform(map_image_root_address)
            icon_count: int = self.resolver.get_child_count(map_image_transform_address)

            icon_index: int
            for icon_index in range(icon_count):
                icon_transform_address: int = self.resolver.get_child(map_image_transform_address, icon_index)
                icon_game_object_address: int = self.resolver.get_game_object(icon_transform_address)
                icon_name: Optional[str] = self.resolver.get_object_name(icon_game_object_address)

                level: DuskLevels = DuskLevels[icon_name]
                is_unlocked: bool = level in unlocked_levels_set

                self.resolver.set_active(icon_game_object_address, is_unlocked)
        except Exception:
            return False

        return True

    def set_flashlight_message(self, message: str = " YOU DO NOT HAVE A FLASHLIGHT ") -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_level and not self.game_state.is_in_endless_level:
            return False

        try:
            stat_script_address: int = self._get_stat_script_address()

            if stat_script_address in (0, None):
                return False

            flashlight_message_string_address: int = self._resolve_address(stat_script_address, (0x38, 0x0))

            if flashlight_message_string_address in (0, None):
                return False

            if len(message) > 30:
                message = message[:30]

            message_bytes: bytes = message.encode("utf-16-le")

            string_length_address: int = flashlight_message_string_address + 0x10
            first_char_address: int = flashlight_message_string_address + 0x14

            self.process.write_int(string_length_address, len(message))
            self.process.write_bytes(first_char_address, message_bytes, len(message_bytes))
        except Exception:
            return False

        return True

    def disable_flashlight(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_level and not self.game_state.is_in_endless_level:
            return False

        try:
            stat_script_address: int = self._get_stat_script_address()

            if stat_script_address in (0, None):
                return False

            broken_flashlight_address: int = stat_script_address + 0x112

            self.process.write_bool(broken_flashlight_address, True)
        except Exception:
            return False

        return True

    def enable_flashlight(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_level and not self.game_state.is_in_endless_level:
            return False

        try:
            stat_script_address: int = self._get_stat_script_address()

            if stat_script_address in (0, None):
                return False

            broken_flashlight_address: int = stat_script_address + 0x112

            self.process.write_bool(broken_flashlight_address, False)
        except Exception:
            return False

        return True

    def disable_lava_immunity(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_level and not self.game_state.is_in_endless_level:
            return False

        try:
            selection_script_address: int = self._get_selection_script_address()

            if selection_script_address in (0, None):
                return False

            self.process.write_bool(selection_script_address + 0x18E, False)
            self.process.write_float(selection_script_address + 0x190, 0.0)
        except Exception:
            return False

        return True

    def enable_lava_immunity(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_level and not self.game_state.is_in_endless_level:
            return False

        try:
            selection_script_address: int = self._get_selection_script_address()

            if selection_script_address in (0, None):
                return False

            self.process.write_bool(selection_script_address + 0x18E, True)
            self.process.write_float(selection_script_address + 0x190, 99999.0)
        except Exception:
            return False

        return True

    # This cannot be reverted once enabled!
    def enable_mirror_mode(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_level:
            return False

        try:
            stat_script_address: int = self._get_stat_script_address()

            if stat_script_address in (0, None):
                return False

            mirror_mode_address: int = stat_script_address + 0x111

            self.process.write_bool(mirror_mode_address, True)
        except Exception:
            return False

        return True

    def set_endless_multiplier_decay_speed(self, value: float) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_endless_level:
            return False

        try:
            stat_script_address: int = self._get_stat_script_address()

            if stat_script_address in (0, None):
                return False

            multiplier_decay_speed_address: int = stat_script_address + 0x14C

            self.process.write_float(multiplier_decay_speed_address, value)
        except Exception:
            return False

        return True

    def set_endless_multiplier_limit(self, value: int) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_endless_level:
            return False

        try:
            stat_script_address: int = self._get_stat_script_address()

            if stat_script_address in (0, None):
                return False

            multiplier_limit_address: int = stat_script_address + 0x150

            self.process.write_int(multiplier_limit_address, value)
        except Exception:
            return False

        return True

    def disable_ladders(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_level and not self.game_state.is_in_endless_level:
            return False

        try:
            ladder_use_script_address: int = self._get_ladder_use_script_address()

            if ladder_use_script_address in (0, None):
                return False

            ignore_ladder_toggle_address: int = ladder_use_script_address + 0x50

            self.process.write_bool(ignore_ladder_toggle_address, True)
        except Exception:
            return False

        return True

    def enable_permanent_climb_anything(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_level and not self.game_state.is_in_endless_level:
            return False

        try:
            ladder_use_script_address: int = self._get_ladder_use_script_address()

            if ladder_use_script_address in (0, None):
                return False

            climb_anything_timer_address: int = ladder_use_script_address + 0x4C
            climb_anything_address: int = ladder_use_script_address + 0x48

            self.process.write_float(climb_anything_timer_address, 99999.0)
            self.process.write_bool(climb_anything_address, True)
        except Exception:
            return False

        return True

    def grant_weapon_loadout(self, weapon_loadout: DuskWeaponLoadout) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_level and not self.game_state.is_in_endless_level:
            return False

        try:
            selection_script_address: int = self._get_selection_script_address()

            if selection_script_address in (0, None):
                return False

            weapon_inventory_address: int = self._resolve_address(selection_script_address, (0x28, 0x0))
            ammo_inventory_address: int = self._resolve_address(selection_script_address, (0x30, 0x0))
            max_ammo_address: int = self._resolve_address(selection_script_address, (0x38, 0x0))

            if weapon_inventory_address in (0, None) or ammo_inventory_address in (0, None) or max_ammo_address in (0, None):
                return False

            weapon: DuskWeapons
            i: int
            for weapon, i in weapon_to_weapon_internal_index.items():
                is_unlocked: bool = weapon in weapon_loadout.weapons
                max_ammo: float = weapon_loadout.max_ammo.get(weapon, 0.0)

                write_mono_bool_array_element(self.process, weapon_inventory_address, i, is_unlocked)
                write_mono_float_array_element(self.process, max_ammo_address, i, max_ammo)
                write_mono_float_array_element(self.process, ammo_inventory_address, i, max_ammo)

            self.process.write_bool(selection_script_address + 0x19F, weapon_loadout.has_sword_upgrade)
            self.process.write_bool(selection_script_address + 0x19D, weapon_loadout.has_dual_pistols_upgrade)
            self.process.write_bool(selection_script_address + 0x19C, weapon_loadout.has_dual_shotgun_upgrade)
        except Exception:
            return False

        return True

    def enforce_weapon_unlocks(self, unlocked_weapons: Set[DuskWeapons]) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_level and not self.game_state.is_in_endless_level:
            return False

        try:
            selection_script_address: int = self._get_selection_script_address()

            if selection_script_address in (0, None):
                return False

            weapon_inventory_address: int = self._resolve_address(selection_script_address, (0x28, 0x0))

            if weapon_inventory_address in (0, None):
                return False

            weapon: DuskWeapons
            i: int
            for weapon, i in weapon_to_weapon_internal_index.items():
                if weapon not in unlocked_weapons:
                    write_mono_bool_array_element(self.process, weapon_inventory_address, i, False)
        except Exception:
            return False

        return True

    def enforce_key_unlocks(self, unlocked_keys: Set[DuskKeys]) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_level:
            return False

        try:
            selection_script_address: int = self._get_selection_script_address()

            if selection_script_address in (0, None):
                return False

            key_offsets: Dict[DuskKeys, int] = {
                DuskKeys.RED: 0x189,
                DuskKeys.BLUE: 0x18A,
                DuskKeys.YELLOW: 0x18B,
            }

            key: DuskKeys
            offset: int
            for key, offset in key_offsets.items():
                self.process.write_bool(selection_script_address + offset, key in unlocked_keys)
        except Exception:
            return False

        return True

    def disable_infinite_ammo(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_level and not self.game_state.is_in_endless_level:
            return False

        try:
            selection_script_address: int = self._get_selection_script_address()

            if selection_script_address in (0, None):
                return False

            self.process.write_bool(selection_script_address + 0x1AC, False)
        except Exception:
            return False

        return True

    def enable_infinite_ammo(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_level and not self.game_state.is_in_endless_level:
            return False

        try:
            selection_script_address: int = self._get_selection_script_address()

            if selection_script_address in (0, None):
                return False

            self.process.write_bool(selection_script_address + 0x1AC, True)
        except Exception:
            return False

        return True

    def disable_grab(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_level and not self.game_state.is_in_endless_level:
            return False

        try:
            pick_up_script_address: int = self._get_pick_up_script_address()

            if pick_up_script_address in (0, None):
                return False

            self.process.write_float(pick_up_script_address + 0x60, 0.0)
        except Exception:
            return False

        return True

    def enable_grab(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_level and not self.game_state.is_in_endless_level:
            return False

        try:
            pick_up_script_address: int = self._get_pick_up_script_address()

            if pick_up_script_address in (0, None):
                return False

            self.process.write_float(pick_up_script_address + 0x60, 6.0)
        except Exception:
            return False

        return True

    def disable_throw(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_level and not self.game_state.is_in_endless_level:
            return False

        try:
            pick_up_script_address: int = self._get_pick_up_script_address()

            if pick_up_script_address in (0, None):
                return False

            self.process.write_float(pick_up_script_address + 0x5C, 0.0)
        except Exception:
            return False

        return True

    def enable_throw(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_level and not self.game_state.is_in_endless_level:
            return False

        try:
            pick_up_script_address: int = self._get_pick_up_script_address()

            if pick_up_script_address in (0, None):
                return False

            self.process.write_float(pick_up_script_address + 0x5C, 40.0)
        except Exception:
            return False

        return True

    def disable_slow_motion(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_level and not self.game_state.is_in_endless_level:
            return False

        try:
            my_controller_script_address: int = self._get_my_controller_script_address()

            if my_controller_script_address in (0, None):
                return False

            self.process.write_bool(my_controller_script_address + 0xB1, False)
        except Exception:
            return False

        return True

    def enable_slow_motion(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_level and not self.game_state.is_in_endless_level:
            return False

        try:
            my_controller_script_address: int = self._get_my_controller_script_address()

            if my_controller_script_address in (0, None):
                return False

            self.process.write_bool(my_controller_script_address + 0xB1, True)
        except Exception:
            return False

        return True

    def disable_crouch(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_level and not self.game_state.is_in_endless_level:
            return False

        try:
            my_controller_script_address: int = self._get_my_controller_script_address()

            if my_controller_script_address in (0, None):
                return False

            self.process.write_float(my_controller_script_address + 0xEC, 0.0)
        except Exception:
            return False

        return True

    def enable_crouch(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_level and not self.game_state.is_in_endless_level:
            return False

        try:
            my_controller_script_address: int = self._get_my_controller_script_address()

            if my_controller_script_address in (0, None):
                return False

            self.process.write_float(my_controller_script_address + 0xEC, 7.0)
        except Exception:
            return False

        return True

    def disable_low_gravity(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_level and not self.game_state.is_in_endless_level:
            return False

        try:
            my_controller_script_address: int = self._get_my_controller_script_address()

            if my_controller_script_address in (0, None):
                return False

            self.process.write_float(my_controller_script_address + 0x104, 0.013)
        except Exception:
            return False

        return True

    def enable_low_gravity(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_level and not self.game_state.is_in_endless_level:
            return False

        try:
            my_controller_script_address: int = self._get_my_controller_script_address()

            if my_controller_script_address in (0, None):
                return False

            self.process.write_float(my_controller_script_address + 0x104, 0.0026)
        except Exception:
            return False

        return True

    def disable_jump(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_level and not self.game_state.is_in_endless_level:
            return False

        try:
            my_controller_script_address: int = self._get_my_controller_script_address()

            if my_controller_script_address in (0, None):
                return False

            self.process.write_float(my_controller_script_address + 0x108, 0.0)
        except Exception:
            return False

        return True

    def enable_jump(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_level and not self.game_state.is_in_endless_level:
            return False

        try:
            my_controller_script_address: int = self._get_my_controller_script_address()

            if my_controller_script_address in (0, None):
                return False

            self.process.write_float(my_controller_script_address + 0x108, 0.2)
        except Exception:
            return False

        return True

    def enable_high_jump(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_level and not self.game_state.is_in_endless_level:
            return False

        try:
            my_controller_script_address: int = self._get_my_controller_script_address()

            if my_controller_script_address in (0, None):
                return False

            self.process.write_float(my_controller_script_address + 0x108, 0.33)
        except Exception:
            return False

        return True

    def disable_freeze(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_level and not self.game_state.is_in_endless_level:
            return False

        try:
            my_controller_script_address: int = self._get_my_controller_script_address()

            if my_controller_script_address in (0, None):
                return False

            self.process.write_float(my_controller_script_address + 0x1A4, 0.0)
        except Exception:
            return False

        return True

    def enable_freeze(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_level and not self.game_state.is_in_endless_level:
            return False

        try:
            my_controller_script_address: int = self._get_my_controller_script_address()

            if my_controller_script_address in (0, None):
                return False

            self.process.write_float(my_controller_script_address + 0x1A4, 999.0)
        except Exception:
            return False

        return True

    def disable_superhot(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_level and not self.game_state.is_in_endless_level:
            return False

        try:
            my_controller_script_address: int = self._get_my_controller_script_address()

            if my_controller_script_address in (0, None):
                return False

            self.process.write_bool(my_controller_script_address + 0x1C0, False)
            self.process.write_float(my_controller_script_address + 0x1C4, 0.0)
        except Exception:
            return False

        return True

    def enable_superhot(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_level and not self.game_state.is_in_endless_level:
            return False

        try:
            my_controller_script_address: int = self._get_my_controller_script_address()

            if my_controller_script_address in (0, None):
                return False

            self.process.write_bool(my_controller_script_address + 0x1C0, True)
            self.process.write_float(my_controller_script_address + 0x1C4, 99999.0)
        except Exception:
            return False

        return True

    def set_sickles_attack_cooldown(self, cooldown: float) -> bool:
        return self._set_attack_cooldown(0x284, cooldown)

    def set_sword_attack_cooldown(self, cooldown: float) -> bool:
        return self._set_attack_cooldown(0x290, cooldown)

    def set_pistol_attack_cooldown(self, cooldown: float) -> bool:
        return self._set_attack_cooldown(0x2CC, cooldown)

    def set_dual_pistol_attack_cooldown(self, cooldown: float) -> bool:
        return self._set_attack_cooldown(0x2DC, cooldown)

    def set_shotgun_attack_cooldown(self, cooldown: float) -> bool:
        return self._set_attack_cooldown(0x2A0, cooldown)

    def set_super_shotgun_attack_cooldown(self, cooldown: float) -> bool:
        return self._set_attack_cooldown(0x2C0, cooldown)

    def set_assault_rifle_attack_cooldown(self, cooldown: float) -> bool:
        return self._set_attack_cooldown(0x2F4, cooldown)

    def set_hunting_rifle_attack_cooldown(self, cooldown: float) -> bool:
        return self._set_attack_cooldown(0x2E4, cooldown)

    def set_crossbow_attack_cooldown(self, cooldown: float) -> bool:
        return self._set_attack_cooldown(0x278, cooldown)

    def set_mortar_cooldown(self, cooldown: float) -> bool:
        return self._set_attack_cooldown(0x304, cooldown)

    def set_riveter_attack_cooldown(self, cooldown: float) -> bool:
        return self._set_attack_cooldown(0x310, cooldown)

    def set_health(self, health: float) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_level and not self.game_state.is_in_endless_level:
            return False

        try:
            player_health_management_address: int = self._get_player_health_management_address()

            if player_health_management_address in (0, None):
                return False

            self.process.write_float(player_health_management_address + 0x78, health)
        except Exception:
            return False

        return True

    def kill_player(self) -> bool:
        return self.set_health(0.0)

    def set_armor(self, armor: float) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_level and not self.game_state.is_in_endless_level:
            return False

        try:
            player_health_management_address: int = self._get_player_health_management_address()

            if player_health_management_address in (0, None):
                return False

            self.process.write_float(player_health_management_address + 0x7C, armor)
        except Exception:
            return False

        return True

    def disable_godmode(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_level:
            return False

        try:
            player_health_management_address: int = self._get_player_health_management_address()

            if player_health_management_address in (0, None):
                return False

            self.process.write_bool(player_health_management_address + 0x81, False)
        except Exception:
            return False

        return True

    def enable_godmode(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_level:
            return False

        try:
            player_health_management_address: int = self._get_player_health_management_address()

            if player_health_management_address in (0, None):
                return False

            self.process.write_bool(player_health_management_address + 0x81, True)
        except Exception:
            return False

        return True

    def disable_drunkness(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_level and not self.game_state.is_in_endless_level:
            return False

        try:
            player_health_management_address: int = self._get_player_health_management_address()

            if player_health_management_address in (0, None):
                return False

            self.process.write_float(player_health_management_address + 0x84, 0.0)
            self.process.write_float(player_health_management_address + 0x88, 0.0)
        except Exception:
            return False

        return True

    def enable_drunkness(self) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_level and not self.game_state.is_in_endless_level:
            return False

        try:
            player_health_management_address: int = self._get_player_health_management_address()

            if player_health_management_address in (0, None):
                return False

            self.process.write_float(player_health_management_address + 0x84, 100.0)
            self.process.write_float(player_health_management_address + 0x88, 9999.0)
        except Exception:
            return False

        return True

    def was_soap_picked_up(self) -> Optional[bool]:
        if not self.is_process_running:
            return None

        if not self.game_state.is_in_level:
            return None

        try:
            soap_game_object_address: int = self.resolver.find_game_object("Soap")

            if soap_game_object_address in (0, None):
                return None

            assembly_image_address: int = self.resolver.get_image("Assembly-CSharp")
            destructible_class_address: int = self.resolver.get_class(assembly_image_address, "", "DestructibleObjectScript")

            destructible_address: int = self.resolver.get_component(soap_game_object_address, destructible_class_address)

            if destructible_address in (0, None):
                return None

            original_x: float
            original_y: float
            original_z: float

            original_x, original_y, original_z = struct.unpack("<3f", self.process.read_bytes(destructible_address + 0x100, 12))

            soap_transform_address: int = self.resolver.get_transform(soap_game_object_address)
            current_x, current_y, current_z = self.resolver.get_position(soap_transform_address)

            distance: float = math.dist((current_x, current_y, current_z), (original_x, original_y, original_z))

            return distance > 5.0
        except Exception:
            return None

    def _determine_game_state(self) -> GameState:
        if not self.is_process_running:
            return GameState(is_valid=False)

        try:
            scenes_names: List[str] = self._get_loaded_scenes()
        except Exception:
            return GameState(is_valid=False)

        scene_name: Optional[str] = None

        scene_name_candidate: str
        for scene_name_candidate in scenes_names:
            if scene_name_candidate in ("Menu", "mapscene", "mapscene2", "mapscene3", "WinLevelScene"):
                scene_name = scene_name_candidate
            elif scene_name_candidate in scene_name_to_endless_level:
                scene_name = scene_name_candidate
            elif scene_name_candidate in scene_name_to_level:
                scene_name = scene_name_candidate

            if scene_name is not None:
                break

        if scene_name is None:
            return GameState(is_valid=False)

        if scene_name == "Menu":
            self.last_seen_level = None

            return GameState(
                is_valid=True,
                is_in_menu=True,
                is_on_map_select=False,
                is_in_endless_level=False,
                is_in_level=False,
                is_on_level_complete=False,
            )
        elif scene_name in ("mapscene", "mapscene2", "mapscene3",):
            self.last_seen_level = None

            map_select_episode: int = 1

            if scene_name == "mapscene2":
                map_select_episode = 2
            elif scene_name == "mapscene3":
                map_select_episode = 3

            return GameState(
                is_valid=True,
                is_in_menu=False,
                is_on_map_select=True,
                is_in_endless_level=False,
                is_in_level=False,
                is_on_level_complete=False,
                map_select_episode=map_select_episode,
            )
        elif scene_name == "WinLevelScene":
            if self.last_seen_level is None:
                return GameState(is_valid=False)

            try:
                level_win_stuff_script_address: int = self._get_level_win_stuff_script_address()

                got_all_kill: bool = False
                got_completionist: bool = False
                got_low_tech: bool = False
                got_pacifist: bool = False
                got_untouchable: bool = False

                if level_win_stuff_script_address not in (0, None):
                    persist_script_address: int = self._resolve_address(level_win_stuff_script_address, (0x18, 0x0))

                    if persist_script_address not in (0, None):
                        kills_from_last_level_address: int = persist_script_address + 0xB0

                        completionist_award_address: int = persist_script_address + 0x102
                        low_tech_award_address: int = persist_script_address + 0x101
                        pacifist_award_address: int = persist_script_address + 0x100
                        untouchable_award_address: int = persist_script_address + 0x103

                        got_all_kill = self.process.read_int(kills_from_last_level_address) >= level_to_all_kill_count.get(self.last_seen_level, 999)

                        got_completionist = self.process.read_bool(completionist_award_address)
                        got_low_tech = self.process.read_bool(low_tech_award_address)
                        got_pacifist = self.process.read_bool(pacifist_award_address)
                        got_untouchable = self.process.read_bool(untouchable_award_address)
            except Exception:
                return GameState(is_valid=False)

            return GameState(
                is_valid=True,
                is_in_menu=False,
                is_on_map_select=False,
                is_in_endless_level=False,
                is_in_level=False,
                is_on_level_complete=True,
                level=self.last_seen_level,
                got_all_kill=got_all_kill,
                got_completionist=got_completionist,
                got_low_tech=got_low_tech,
                got_pacifist=got_pacifist,
                got_untouchable=got_untouchable,
            )
        elif scene_name in scene_name_to_endless_level:
            self.last_seen_level = None

            endless_level: DuskEndlessLevels = scene_name_to_endless_level[scene_name]

            try:
                is_dead: Optional[bool] = None

                player_health_management_address: int = self._get_player_health_management_address()

                if player_health_management_address not in (0, None):
                    is_dead = self.process.read_bool(player_health_management_address + 0x80)

                is_in_water: Optional[bool] = None

                my_controller_script_address: int = self._get_my_controller_script_address()

                if my_controller_script_address not in (0, None):
                    is_in_water = self.process.read_bool(my_controller_script_address + 0x174)

                selected_weapon: Optional[DuskWeapons] = None

                selection_script_address: int = self._get_selection_script_address()

                if selection_script_address not in (0, None):
                    selected_weapon = selected_weapon_index_to_weapon.get(self.process.read_int(selection_script_address + 0x1A8))

                difficulty: Optional[DuskDifficulties] = None

                endless_kill_count: int = 0
                endless_score: int = 0
                endless_multiplier: int = 0

                stat_script_address: int = self._get_stat_script_address()

                if stat_script_address not in (0, None):
                    difficulty = difficulty_value_to_difficulty.get(self.process.read_int(stat_script_address + 0x12C))

                    endless_kill_count = self.process.read_int(stat_script_address + 0x114)
                    endless_score = self.process.read_int(stat_script_address + 0x120)
                    endless_multiplier = self.process.read_float(stat_script_address + 0x11C)
            except Exception:
                return GameState(is_valid=False)

            return GameState(
                is_valid=True,
                is_in_menu=False,
                is_on_map_select=False,
                is_in_endless_level=True,
                is_in_level=False,
                is_on_level_complete=False,
                is_dead=is_dead,
                is_in_water=is_in_water,
                selected_weapon=selected_weapon,
                difficulty=difficulty,
                endless_level=endless_level,
                endless_kill_count=endless_kill_count,
                endless_score=endless_score,
                endless_multiplier=endless_multiplier,
            )
        elif scene_name in scene_name_to_level:
            level: DuskLevels = scene_name_to_level[scene_name]

            self.last_seen_level = level

            try:
                was_soap_picked_up: bool = self.was_soap_picked_up() or False

                remaining_pickups: Set[str] = set(self._get_level_pickups().keys())
                remaining_enemies: Set[str] = set(self._get_level_enemies().keys())

                is_dead: Optional[bool] = None

                player_health_management_address: int = self._get_player_health_management_address()

                if player_health_management_address not in (0, None):
                    is_dead = self.process.read_bool(player_health_management_address + 0x80)

                is_in_water: Optional[bool] = None

                my_controller_script_address: int = self._get_my_controller_script_address()

                if my_controller_script_address not in (0, None):
                    is_in_water = self.process.read_bool(my_controller_script_address + 0x174)

                selected_weapon: Optional[DuskWeapons] = None

                selection_script_address: int = self._get_selection_script_address()

                if selection_script_address not in (0, None):
                    selected_weapon = selected_weapon_index_to_weapon.get(self.process.read_int(selection_script_address + 0x1A8))

                difficulty: Optional[DuskDifficulties] = None

                stat_script_address: int = self._get_stat_script_address()

                if stat_script_address not in (0, None):
                    difficulty = difficulty_value_to_difficulty.get(self.process.read_int(stat_script_address + 0x12C))
            except Exception:
                return GameState(is_valid=False)

            return GameState(
                is_valid=True,
                is_in_menu=False,
                is_on_map_select=False,
                is_in_endless_level=False,
                is_in_level=True,
                is_on_level_complete=False,
                is_dead=is_dead,
                is_in_water=is_in_water,
                selected_weapon=selected_weapon,
                difficulty=difficulty,
                level=level,
                was_soap_picked_up=was_soap_picked_up,
                remaining_pickups=remaining_pickups,
                remaining_enemies=remaining_enemies,
            )

        return GameState(is_valid=False)

    def _get_stat_script_address(self) -> Optional[int]:
        assembly_image_address: int = self.resolver.get_image("Assembly-CSharp")
        stat_script_class_address: int = self.resolver.get_class(assembly_image_address, "", "StatScript")

        instance_addresses: List[int] = self.resolver.find_objects_of_type(stat_script_class_address)

        if len(instance_addresses) != 1:
            return None

        return instance_addresses[0]

    def _get_attack_script_address(self) -> Optional[int]:
        stat_script_address: int = self._get_stat_script_address()

        if stat_script_address in (0, None):
            return None

        return self._resolve_address(stat_script_address, (0xB0, 0x0))

    def _get_player_health_management_address(self) -> Optional[int]:
        attack_script_address: int = self._get_attack_script_address()

        if attack_script_address in (0, None):
            return None

        return self._resolve_address(attack_script_address, (0x1E0, 0x0))

    def _get_my_controller_script_address(self) -> Optional[int]:
        assembly_image_address: int = self.resolver.get_image("Assembly-CSharp")
        my_controller_script_class_address: int = self.resolver.get_class(assembly_image_address, "", "MyControllerScript")

        instance_addresses: List[int] = self.resolver.find_objects_of_type(my_controller_script_class_address)

        if len(instance_addresses) != 1:
            return None

        return instance_addresses[0]

    def _get_selection_script_address(self) -> Optional[int]:
        my_controller_script_address: int = self._get_my_controller_script_address()

        if my_controller_script_address in (0, None):
            return None

        return self._resolve_address(my_controller_script_address, (0x80, 0x0))

    def _get_pick_up_script_address(self) -> Optional[int]:
        selection_script_address: int = self._get_selection_script_address()

        if selection_script_address in (0, None):
            return None

        return self._resolve_address(selection_script_address, (0x178, 0x0))

    def _get_ladder_use_script_address(self) -> Optional[int]:
        assembly_image_address: int = self.resolver.get_image("Assembly-CSharp")
        ladder_use_script_class_address: int = self.resolver.get_class(assembly_image_address, "", "LadderUseScript")

        instance_addresses: List[int] = self.resolver.find_objects_of_type(ladder_use_script_class_address)

        if len(instance_addresses) != 1:
            return None

        return instance_addresses[0]

    def _get_level_win_stuff_script_address(self) -> Optional[int]:
        assembly_image_address: int = self.resolver.get_image("Assembly-CSharp")
        level_win_stuff_class_address: int = self.resolver.get_class(assembly_image_address, "", "LevelWinStuffScript")

        instance_addresses: List[int] = self.resolver.find_objects_of_type(level_win_stuff_class_address)

        if len(instance_addresses) != 1:
            return None

        return instance_addresses[0]

    def _get_loaded_scenes(self) -> List[str]:
        core_image_address: int = self.resolver.get_image("UnityEngine.CoreModule")

        scene_manager_class_address: int = self.resolver.get_class(core_image_address, "UnityEngine.SceneManagement", "SceneManager")
        scene_class_address: int = self.resolver.get_class(core_image_address, "UnityEngine.SceneManagement", "Scene")

        get_count_method_address: int = self.resolver.get_method(scene_manager_class_address, "get_sceneCount", 0)
        get_scene_at_method_address: int = self.resolver.get_method(scene_manager_class_address, "GetSceneAt", 1)
        get_name_method_address: int = self.resolver.get_method(scene_class_address, "get_name", 0)

        count_boxed_address: int = self.resolver.invoke(get_count_method_address)
        scene_count: int = self.resolver.unbox_int32(count_boxed_address)

        scene_names: List[Optional[str]] = list()

        scene_index: int
        for scene_index in range(scene_count):
            index_address: int = self.resolver.caller.write_int32_to_buffer(scene_index)
            params_address: int = self.resolver.caller.write_pointer_array_to_buffer([index_address])

            scene_boxed_address: int = self.resolver.invoke(get_scene_at_method_address, object_address=0, params_address=params_address)
            scene_data_address: int = self.resolver.unbox_address(scene_boxed_address)

            name_address: int = self.resolver.invoke(get_name_method_address, object_address=scene_data_address)
            scene_name: Optional[str] = self.resolver.read_mono_string(name_address)

            if scene_name is not None:
                scene_names.append(scene_name)

        return scene_names

    def _get_level_pickups(self) -> Dict[str, int]:
        assembly_image_address: int = self.resolver.get_image("Assembly-CSharp")
        save_pickup_class_address: int = self.resolver.get_class(assembly_image_address, "", "SavePickupScript")

        instance_addresses: List[int] = self.resolver.find_objects_of_type(save_pickup_class_address)

        pickups: Dict[str, int] = dict()

        instance_address: int
        for instance_address in instance_addresses:
            coorsid_address: int = self.resolver.caller.process.read_longlong(instance_address + 0x20)
            coorsid: Optional[str] = self.resolver.read_mono_string(coorsid_address)

            if coorsid is not None:
                pickups[coorsid] = instance_address

        return pickups

    def _get_level_enemies(self) -> Dict[str, int]:
        assembly_image_address: int = self.resolver.get_image("Assembly-CSharp")
        basic_ai_class_address: int = self.resolver.get_class(assembly_image_address, "", "BasicAIScript")
        destructible_class_address: int = self.resolver.get_class(assembly_image_address, "", "DestructibleObjectScript")

        instance_addresses: List[int] = self.resolver.find_objects_of_type(basic_ai_class_address)

        enemies: Dict[str, int] = dict()

        instance_address: int
        for instance_address in instance_addresses:
            game_object_address: int = self.resolver.get_game_object(instance_address)
            name: Optional[str] = self.resolver.get_object_name(game_object_address)

            if name is None:
                continue

            while name in enemies:
                name += "+"

            destructible_address: int = self.resolver.get_component(game_object_address, destructible_class_address)

            if destructible_address in (0, None):
                continue

            enemies[name] = destructible_address

        return enemies

    def _set_attack_cooldown(self, offset: int, cooldown: float) -> bool:
        if not self.is_process_running:
            return False

        if not self.game_state.is_in_level and not self.game_state.is_in_endless_level:
            return False

        try:
            attack_script_address: int = self._get_attack_script_address()

            if attack_script_address in (0, None):
                return False

            self.process.write_float(attack_script_address + offset, cooldown)
        except Exception:
            return False

        return True

    def _resolve_address(self, start_address: int, offsets: Tuple[int, ...]) -> Optional[int]:
        address: int = start_address

        offset: int
        for offset in offsets[:-1]:
            try:
                address = self.process.read_longlong(address + offset)
            except Exception:
                return None

        return address + offsets[-1]

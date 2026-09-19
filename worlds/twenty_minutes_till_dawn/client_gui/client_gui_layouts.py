from typing import Any, Dict, List, Optional

import io
import pkgutil

import NetUtils

from kivy.clock import Clock
from kivy.core.image import Image as CoreImage

from kivy.graphics import Color, Line, Rectangle
from kivy.graphics.texture import Texture

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget

from ..client import TwentyMinutesContext

from ..data.game_data import TwentyMinutesWeaponData, weapon_to_vanilla_weapon_data

from ..enums import (
    TwentyMinutesCharacters,
    TwentyMinutesGoalOptions,
    TwentyMinutesMaps,
    TwentyMinutesWeapons,
)

from ..game_state_manager import GameState

from .. import client_gui


def _get_received_items(ctx: TwentyMinutesContext) -> Dict[str, int]:
    received_items: Dict[str, int] = dict()

    network_item: NetUtils.NetworkItem
    for network_item in ctx.items_received:
        if network_item.item in ctx.id_to_items:
            item_name: str = ctx.id_to_items[network_item.item]

            if item_name not in received_items:
                received_items[item_name] = 0

            received_items[item_name] += 1

    return received_items


def _load_texture(image_path: str) -> Optional[Texture]:
    try:
        image_bytes: Optional[bytes] = pkgutil.get_data(client_gui.__name__, image_path)
    except Exception:
        return None

    if image_bytes is None:
        return None

    try:
        image: CoreImage = CoreImage(io.BytesIO(image_bytes), ext="png")
    except Exception:
        return None

    return image.texture


def _format_weapon_attribute(value: Any, vanilla_value: Any, attribute_color: str, unit: str = "") -> str:
    value_text: str = f"{value:g}" if isinstance(value, float) else str(value)

    text: str = f"[color={attribute_color}]{value_text}{unit}[/color]"

    delta: Any = value - vanilla_value

    if delta != 0:
        delta_text: str = f"{delta:+.2f}" if isinstance(delta, float) else f"{delta:+d}"

        text += f"  [color=888888]{delta_text}[/color]"

    return text


def _apply_lock_gray(text: str, is_unlocked: bool) -> str:
    if is_unlocked:
        return text

    return f"[color=888888]{text}[/color]"


def _unlocked_opacity(is_unlocked: bool, has_texture: bool) -> float:
    if not is_unlocked:
        return 0.15

    return 1.0 if has_texture else 0.3


def _is_relevant_to_current_run(
    location_name: str,
    map_name: str,
    character_name: Optional[str],
    weapon_name: Optional[str],
) -> bool:
    if not location_name.startswith(f"{map_name} - "):
        return False

    if location_name.endswith(" Kills"):
        return True

    if character_name is not None and f" - {character_name} - " in location_name:
        return True

    if weapon_name is not None and f" - {weapon_name} - " in location_name:
        return True

    return False


def _display_name_for_location(location_name: str) -> str:
    if location_name.endswith(" Kills"):
        return location_name.rsplit(" - ", 1)[-1]

    return location_name.split(" - ", 1)[-1]


def _bind_text_size(label: Label) -> None:
    label.bind(size=lambda instance, size: setattr(instance, "text_size", size))


class NotConnectedLayout(BoxLayout):
    ctx: TwentyMinutesContext

    def __init__(self, ctx: TwentyMinutesContext) -> None:
        super().__init__(orientation="horizontal", size_hint_y=0.12)

        self.ctx = ctx

        self.add_widget(
            Label(text="Please connect to an Archipelago server first to view this tab.", font_size="24dp")
        )

    def show(self):
        self.opacity = 1.0
        self.size_hint_y = 0.12
        self.disabled = False

    def hide(self):
        self.opacity = 0.0
        self.size_hint_y = None
        self.height = "0dp"
        self.disabled = True


class GameInformationLayout(BoxLayout):
    ctx: TwentyMinutesContext

    information_label: Label

    forbidden_tomes_label: Label
    goal_label: Label

    map_image: Image
    character_image: Image
    weapon_image: Image

    title_label: Label
    subtitle_label: Label
    stats_label: Label

    locations_in_logic_label: Label
    locations_out_of_logic_label: Label

    last_seen_map: Optional[TwentyMinutesMaps]
    last_seen_character: Optional[TwentyMinutesCharacters]
    last_seen_weapon: Optional[TwentyMinutesWeapons]

    def __init__(self, ctx: TwentyMinutesContext) -> None:
        super().__init__(orientation="vertical", size_hint_y=None, height="280dp", spacing="8dp")

        self.bind(minimum_height=self.setter("height"))

        self.ctx = ctx

        # Header
        self.information_label = Label(
            text="[b]Game Information[/b]",
            markup=True,
            font_size="32dp",
            size_hint_y=None,
            height="38dp",
            halign="left",
            valign="middle",
        )

        _bind_text_size(self.information_label)

        self.add_widget(self.information_label)

        # Forbidden Tomes / Goal
        goal_header_layout: BoxLayout = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height="60dp",
            spacing="8dp",
            padding=[0, 0, 0, 10],
        )

        goal_header_layout.bind(minimum_height=goal_header_layout.setter("height"))

        self.forbidden_tomes_label = Label(
            text="[b]Forbidden Tomes[/b]\nRetrieved [color=00FA9A]0[/color] of [color=00FA9A]0[/color] needed",
            markup=True,
            size_hint_x=40,
            size_hint_y=None,
            height="60dp",
            halign="left",
            valign="middle",
        )

        _bind_text_size(self.forbidden_tomes_label)

        goal_header_layout.add_widget(self.forbidden_tomes_label)

        self.goal_label = Label(
            text="[b]Goal[/b]\n?",
            markup=True,
            size_hint_x=60,
            size_hint_y=None,
            height="60dp",
            halign="left",
            valign="middle",
        )

        _bind_text_size(self.goal_label)

        goal_header_layout.add_widget(self.goal_label)

        self.add_widget(goal_header_layout)

        # Live Run Information
        run_information_layout: BoxLayout = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height="162dp",
            spacing="8dp",
            padding=[0, 0, 0, 10],
        )

        run_information_layout.bind(minimum_height=run_information_layout.setter("height"))

        self.map_image = Image(size=(152, 152), size_hint=(None, None), allow_stretch=True, opacity=0.15)
        run_information_layout.add_widget(self.map_image)

        self.character_image = Image(size=(152, 152), size_hint=(None, None), allow_stretch=True, opacity=0.15)
        run_information_layout.add_widget(self.character_image)

        self.weapon_image = Image(size=(152, 152), size_hint=(None, None), allow_stretch=True, opacity=0.15)
        run_information_layout.add_widget(self.weapon_image)

        text_layout: BoxLayout = BoxLayout(orientation="vertical", size_hint_y=None, height="152dp", spacing="4dp")
        text_layout.bind(minimum_height=text_layout.setter("height"))

        self.title_label = Label(
            text="[b]Not currently in a map...[/b]",
            markup=True,
            size_hint_y=None,
            font_size="16dp",
            height="20dp",
            halign="left",
            valign="middle",
        )

        _bind_text_size(self.title_label)

        text_layout.add_widget(self.title_label)

        self.subtitle_label = Label(
            text="",
            markup=True,
            size_hint_y=None,
            font_size="11dp",
            height="14dp",
            halign="left",
            valign="middle",
        )

        _bind_text_size(self.subtitle_label)

        text_layout.add_widget(self.subtitle_label)

        text_layout.add_widget(Widget(size_hint_y=None, height="6dp"))

        self.stats_label = Label(
            text=(
                "[color=888888]Time: --:-- / --:--[/color]\n"
                "[color=888888]Level: -[/color]\n"
                "[color=888888]Kills: -[/color]\n"
                "[color=888888]Hearts: - / -[/color]\n"
                "[color=888888]Soul Hearts: - / -[/color]"
            ),
            markup=True,
            size_hint_y=None,
            font_size="13dp",
            line_height=1.3,
            height="100dp",
            halign="left",
            valign="top",
        )

        _bind_text_size(self.stats_label)

        text_layout.add_widget(self.stats_label)

        run_information_layout.add_widget(text_layout)

        self.add_widget(run_information_layout)

        # Locations In / Out of Logic
        logic_layout: BoxLayout = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height="90dp",
            spacing="8dp",
        )

        logic_layout.bind(minimum_height=logic_layout.setter("height"))

        locations_in_logic_column: BoxLayout = BoxLayout(
            orientation="vertical", size_hint_y=None, spacing="4dp", pos_hint={"top": 1}
        )
        locations_in_logic_column.bind(minimum_height=locations_in_logic_column.setter("height"))

        locations_in_logic_header: Label = Label(
            text="[b]In Logic Locations[/b]",
            markup=True,
            size_hint_y=None,
            font_size="16dp",
            height="20dp",
            halign="left",
            valign="middle",
        )

        _bind_text_size(locations_in_logic_header)

        locations_in_logic_column.add_widget(locations_in_logic_header)

        self.locations_in_logic_label = Label(
            text="[color=888888]No locations accessible in logic[/color]",
            markup=True,
            size_hint_y=None,
            font_size="12dp",
            height="16dp",
            halign="left",
            valign="top",
        )

        self.locations_in_logic_label.bind(
            texture_size=lambda instance, texture_size: setattr(instance, "height", texture_size[1])
        )
        self.locations_in_logic_label.bind(
            width=lambda instance, width: setattr(instance, "text_size", (width, None))
        )

        locations_in_logic_column.add_widget(self.locations_in_logic_label)

        locations_out_of_logic_column: BoxLayout = BoxLayout(
            orientation="vertical", size_hint_y=None, spacing="4dp", pos_hint={"top": 1}
        )
        locations_out_of_logic_column.bind(minimum_height=locations_out_of_logic_column.setter("height"))

        locations_out_of_logic_header: Label = Label(
            text="[b]Out of Logic Locations[/b]",
            markup=True,
            size_hint_y=None,
            font_size="16dp",
            height="20dp",
            halign="left",
            valign="middle",
        )

        _bind_text_size(locations_out_of_logic_header)

        locations_out_of_logic_column.add_widget(locations_out_of_logic_header)

        self.locations_out_of_logic_label = Label(
            text="[color=888888]No locations accessible out of logic[/color]",
            markup=True,
            size_hint_y=None,
            font_size="12dp",
            height="16dp",
            halign="left",
            valign="top",
        )

        self.locations_out_of_logic_label.bind(
            texture_size=lambda instance, texture_size: setattr(instance, "height", texture_size[1])
        )
        self.locations_out_of_logic_label.bind(
            width=lambda instance, width: setattr(instance, "text_size", (width, None))
        )

        locations_out_of_logic_column.add_widget(self.locations_out_of_logic_label)

        logic_layout.add_widget(locations_in_logic_column)
        logic_layout.add_widget(locations_out_of_logic_column)

        if self.ctx.tracker_loaded:
            self.add_widget(logic_layout)

        self.last_seen_map = None
        self.last_seen_character = None
        self.last_seen_weapon = None

    def update(self) -> None:
        received_items: Dict[str, int] = _get_received_items(self.ctx)

        # Forbidden Tomes
        forbidden_tome_count: int = received_items.get("Forbidden Tome", 0)

        self.forbidden_tomes_label.text = (
            "[b]Forbidden Tomes[/b]\n"
            f"Retrieved [color=00FA9A]{forbidden_tome_count}[/color] of "
            f"[color=00FA9A]{self.ctx.game_controller.option_forbidden_tomes_required}[/color] needed "
            f"([color=888888]{self.ctx.game_controller.option_forbidden_tomes_total} total[/color])"
        )

        # Goal
        if self.ctx.game_controller.option_goal == TwentyMinutesGoalOptions.FORBIDDEN_TOME_HUNT:
            self.goal_label.text = "[b]Goal[/b]\nCollect the Tomes!"
        elif self.ctx.game_controller.option_goal == TwentyMinutesGoalOptions.FORBIDDEN_TOMES_FINAL_MAP:
            goal_map_name: str = "?"

            if self.ctx.game_controller.selected_full_run_map is not None:
                goal_map_name = self.ctx.game_controller.selected_full_run_map.value

            self.goal_label.text = f"[b]Goal[/b]\nCollect the Tomes and survive 20 minutes on {goal_map_name}!"
        else:
            self.goal_label.text = "[b]Goal[/b]\n?"

        # Live Run Information
        game_state: Optional[GameState] = self.ctx.game_controller.game_state

        if game_state is None or not game_state.is_valid or not game_state.is_in_run:
            self._clear_live_current_state()
            return

        current_map: Optional[TwentyMinutesMaps] = game_state.current_map
        current_character: Optional[TwentyMinutesCharacters] = game_state.character
        current_weapon: Optional[TwentyMinutesWeapons] = game_state.weapon

        if self.last_seen_map != current_map:
            texture: Optional[Texture] = _load_texture(f"assets/{current_map.value}.png") if current_map else None

            self.map_image.texture = texture
            self.map_image.opacity = 1.0 if texture is not None else 0.3

            self.last_seen_map = current_map

        if self.last_seen_character != current_character:
            texture: Optional[Texture] = (
                _load_texture(f"assets/{current_character.value}.png") if current_character else None
            )

            self.character_image.texture = texture
            self.character_image.opacity = 1.0 if texture is not None else 0.3

            self.last_seen_character = current_character

        if self.last_seen_weapon != current_weapon:
            texture: Optional[Texture] = (
                _load_texture(f"assets/{current_weapon.value}.png") if current_weapon else None
            )

            self.weapon_image.texture = texture
            self.weapon_image.opacity = 1.0 if texture is not None else 0.3

            self.last_seen_weapon = current_weapon

        map_label: str = current_map.value if current_map is not None else "Unknown Map"
        character_label: str = current_character.value if current_character is not None else "Unknown Character"
        weapon_label: str = current_weapon.value if current_weapon is not None else "Unknown Weapon"

        self.title_label.text = f"[b]{map_label}[/b]"
        self.subtitle_label.text = f"{character_label} / {weapon_label}"

        stats_lines: List[str] = list()

        if game_state.time_elapsed is not None and game_state.time_limit is not None:
            elapsed_minutes, elapsed_seconds = divmod(int(game_state.time_elapsed), 60)
            limit_minutes, limit_seconds = divmod(int(game_state.time_limit), 60)

            stats_lines.append(
                f"[b]Time:[/b] {elapsed_minutes:02d}:{elapsed_seconds:02d} / {limit_minutes:02d}:{limit_seconds:02d}"
            )

        if game_state.player_level is not None:
            stats_lines.append(f"[b]Level:[/b] {game_state.player_level}")

        if game_state.enemy_kill_count is not None:
            stats_lines.append(f"[b]Kills:[/b] {game_state.enemy_kill_count}")

        if game_state.current_health is not None and game_state.maximum_health is not None:
            stats_lines.append(f"[b]Hearts:[/b] {game_state.current_health} / {game_state.maximum_health}")

        if game_state.current_temporary_health is not None and game_state.maximum_temporary_health is not None:
            stats_lines.append(
                f"[b]Soul Hearts:[/b] {game_state.current_temporary_health} / {game_state.maximum_temporary_health}"
            )

        self.stats_label.text = "\n".join(stats_lines)

        # Locations In / Out of Logic
        if self.ctx.tracker_loaded and current_map is not None:
            map_name: str = current_map.value
            character_name: Optional[str] = current_character.value if current_character is not None else None
            weapon_name: Optional[str] = current_weapon.value if current_weapon is not None else None

            in_logic_names: List[str] = sorted(
                location_name
                for location_name in self.ctx.locations_in_logic
                if _is_relevant_to_current_run(location_name, map_name, character_name, weapon_name)
            )

            out_of_logic_names: List[str] = sorted(
                location_name
                for location_name in self.ctx.locations_out_of_logic
                if _is_relevant_to_current_run(location_name, map_name, character_name, weapon_name)
            )

            if in_logic_names:
                self.locations_in_logic_label.text = "\n".join(
                    f"[color=00FA9A]{_display_name_for_location(location_name)}[/color]" for location_name in in_logic_names
                )
            else:
                self.locations_in_logic_label.text = "[color=888888]No locations accessible in logic[/color]"

            if out_of_logic_names:
                self.locations_out_of_logic_label.text = "\n".join(
                    f"[color=FFD300]{_display_name_for_location(location_name)}[/color]" for location_name in out_of_logic_names
                )
            else:
                self.locations_out_of_logic_label.text = "[color=888888]No locations accessible out of logic[/color]"

    def _clear_live_current_state(self) -> None:
        self.map_image.texture = None
        self.map_image.opacity = 0.15

        self.character_image.texture = None
        self.character_image.opacity = 0.15

        self.weapon_image.texture = None
        self.weapon_image.opacity = 0.15

        self.title_label.text = "[b]Not currently in a map...[/b]"
        self.subtitle_label.text = ""
        self.stats_label.text = (
            "[color=888888]Time: --:-- / --:--[/color]\n"
            "[color=888888]Level: -[/color]\n"
            "[color=888888]Kills: -[/color]\n"
            "[color=888888]Hearts: - / -[/color]\n"
            "[color=888888]Soul Hearts: - / -[/color]"
        )

        self.locations_in_logic_label.text = "[color=888888]No locations accessible in logic[/color]"
        self.locations_out_of_logic_label.text = "[color=888888]No locations accessible out of logic[/color]"

        self.last_seen_map = None
        self.last_seen_character = None
        self.last_seen_weapon = None


class MapsLayout(BoxLayout):
    ctx: TwentyMinutesContext

    maps_label: Label
    darkness_label: Label

    map_images: List[Image]
    map_timer_labels: List[Label]
    map_logic_labels: List[Label]

    map_data: Dict[TwentyMinutesMaps, Dict[str, Any]]

    def __init__(self, ctx: TwentyMinutesContext) -> None:
        super().__init__(orientation="vertical", size_hint_y=None, height="40dp", spacing="8dp")

        self.bind(minimum_height=self.setter("height"))

        self.ctx = ctx

        self.maps_label = Label(
            text="[b]Maps[/b]",
            markup=True,
            font_size="32dp",
            size_hint_y=None,
            height="70dp",
            halign="left",
            valign="bottom",
        )

        _bind_text_size(self.maps_label)

        self.add_widget(self.maps_label)

        self.darkness_label = Label(
            text=(
                "[color=888888]Starting Darkness:[/color] [b]0[/b]\n"
                "[color=888888]Current Darkness:[/color] [b]0[/b]\n"
                "[color=888888]Expected Darkness to Clear:[/color] [b]0[/b]"
            ),
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            line_height=1.3,
            height="80dp",
            halign="left",
            valign="top",
        )

        _bind_text_size(self.darkness_label)

        self.add_widget(self.darkness_label)

        self.map_images = list()
        self.map_timer_labels = list()
        self.map_logic_labels = list()

        self.map_data = dict()

        map_: TwentyMinutesMaps
        for map_ in TwentyMinutesMaps:
            self.map_data[map_] = {
                "image_path": f"assets/{map_.value}.png",
                "unlock_item": f"Map Unlock: {map_.value}",
                "is_full_run_map": map_ == self.ctx.game_controller.selected_full_run_map,
            }

        grid_layout: GridLayout = GridLayout(
            cols=3,
            spacing=12,
            padding=0,
            size_hint_y=None,
        )

        grid_layout.bind(minimum_height=grid_layout.setter("height"))

        map_: TwentyMinutesMaps
        data: Dict[str, Any]
        for map_, data in self.map_data.items():
            map_layout: BoxLayout = BoxLayout(
                orientation="vertical",
                size_hint_x=None,
                size_hint_y=None,
                width="128dp",
                height="186dp",
                spacing="4dp",
            )

            map_layout.bind(minimum_height=map_layout.setter("height"))

            map_image: Image = Image(
                texture=_load_texture(data["image_path"]),
                size=(128, 128),
                size_hint=(None, None),
                allow_stretch=True,
                opacity=0.15,
            )

            if data["is_full_run_map"]:
                with map_image.canvas.after:
                    Color(1, 0.85, 0.2, 0.15)
                    fill_rect: Rectangle = Rectangle(pos=map_image.pos, size=map_image.size)

                    Color(1, 0.85, 0.2, 1.0)
                    border: Line = Line(rectangle=(*map_image.pos, *map_image.size), width=2)

                def _update_goal_decoration(*_, fill_rect=fill_rect, border=border, image=map_image) -> None:
                    fill_rect.pos = image.pos
                    fill_rect.size = image.size
                    border.rectangle = (*image.pos, *image.size)

                map_image.bind(pos=_update_goal_decoration, size=_update_goal_decoration)

            self.map_images.append(map_image)

            map_layout.add_widget(map_image)

            map_logic_label: Label = Label(
                text="In Logic: [color=888888]0[/color]\nOut of Logic: [color=888888]0[/color]",
                markup=True,
                font_size="12dp",
                size_hint_y=None,
                height="32dp",
                halign="left",
                valign="top",
            )

            _bind_text_size(map_logic_label)

            self.map_logic_labels.append(map_logic_label)

            if self.ctx.tracker_loaded:
                map_layout.add_widget(map_logic_label)

            map_timer_label: Label = Label(
                text="Timer: [color=888888]4[/color] / [color=888888]12[/color] Minutes",
                markup=True,
                font_size="12dp",
                size_hint_y=None,
                height="18dp",
                halign="left",
                valign="top",
            )

            _bind_text_size(map_timer_label)

            self.map_timer_labels.append(map_timer_label)

            map_layout.add_widget(map_timer_label)

            grid_layout.add_widget(map_layout)

        self.add_widget(grid_layout)

    def update(self) -> None:
        received_items: Dict[str, int] = _get_received_items(self.ctx)

        starting_darkness: int = self.ctx.game_controller.option_starting_darkness or 0
        darkness_reduction_count: int = received_items.get("Progressive Darkness Reduction", 0)
        current_darkness: int = max(0, starting_darkness - darkness_reduction_count)
        maximum_clearable_darkness: int = self.ctx.game_controller.option_maximum_survivable_darkness or 0

        self.darkness_label.text = (
            f"[color=888888]Starting Darkness:[/color] [b]{starting_darkness}[/b]\n"
            f"[color=888888]Current Darkness:[/color] [b]{current_darkness}[/b]\n"
            f"[color=888888]Expected Darkness to Clear:[/color] [b]{maximum_clearable_darkness}[/b]"
        )

        map_: TwentyMinutesMaps
        data: Dict[str, Any]
        for i, (map_, data) in enumerate(self.map_data.items()):
            is_unlocked: bool = received_items.get(data["unlock_item"], 0) > 0

            has_texture: bool = self.map_images[i].texture is not None
            self.map_images[i].opacity = _unlocked_opacity(is_unlocked, has_texture)

            progressive_timer_count: int = received_items.get(f"Progressive Timer: {map_.value}", 0)
            current_timer_minutes: int = 4 * (1 + progressive_timer_count)
            max_timer_minutes: int = 20 if data["is_full_run_map"] else 12

            timer_color: str = "00FA9A" if is_unlocked else "888888"

            timer_text: str = (
                f"Timer: [color={timer_color}]{current_timer_minutes}[/color] / "
                f"[color={timer_color}]{max_timer_minutes}[/color] Minutes"
            )

            self.map_timer_labels[i].text = _apply_lock_gray(timer_text, is_unlocked)

            if self.ctx.tracker_loaded:
                map_name: str = map_.value

                in_logic_count: int = sum(
                    1 for location_name in self.ctx.locations_in_logic if location_name.startswith(f"{map_name} - ")
                )
                out_of_logic_count: int = sum(
                    1 for location_name in self.ctx.locations_out_of_logic if location_name.startswith(f"{map_name} - ")
                )

                if is_unlocked:
                    in_logic_color: str = "00FA9A" if in_logic_count > 0 else "888888"
                    out_of_logic_color: str = "FFD300" if out_of_logic_count > 0 else "888888"
                else:
                    in_logic_color = out_of_logic_color = "888888"

                logic_text: str = (
                    f"In Logic: [color={in_logic_color}]{in_logic_count}[/color]\n"
                    f"Out of Logic: [color={out_of_logic_color}]{out_of_logic_count}[/color]"
                )

                self.map_logic_labels[i].text = _apply_lock_gray(logic_text, is_unlocked)


class CharactersLayout(BoxLayout):
    ctx: TwentyMinutesContext

    characters_label: Label

    character_images: List[Image]
    character_location_labels: List[Label]
    character_stats_labels: List[Label]

    character_data: Dict[TwentyMinutesCharacters, Dict[str, Any]]

    def __init__(self, ctx: TwentyMinutesContext) -> None:
        super().__init__(orientation="vertical", size_hint_y=None, height="40dp", spacing="8dp")

        self.bind(minimum_height=self.setter("height"))

        self.ctx = ctx

        self.characters_label = Label(
            text="[b]Characters[/b]",
            markup=True,
            font_size="32dp",
            size_hint_y=None,
            height="70dp",
            halign="left",
            valign="bottom",
        )

        _bind_text_size(self.characters_label)

        self.add_widget(self.characters_label)

        self.character_images = list()
        self.character_location_labels = list()
        self.character_stats_labels = list()

        self.character_data = dict()

        character: TwentyMinutesCharacters
        for character in self.ctx.game_controller.selected_characters:
            self.character_data[character] = {
                "image_path": f"assets/{character.value}.png",
                "unlock_item": f"Character Unlock: {character.value}",
            }

        grid_layout: GridLayout = GridLayout(
            cols=4,
            spacing=12,
            padding=0,
            size_hint_y=None,
        )

        grid_layout.bind(minimum_height=grid_layout.setter("height"))

        character: TwentyMinutesCharacters
        data: Dict[str, Any]
        for character, data in self.character_data.items():
            character_layout: BoxLayout = BoxLayout(
                orientation="vertical",
                size_hint_x=None,
                size_hint_y=None,
                width="158dp",
                height="246dp",
                spacing="4dp",
            )

            character_layout.bind(minimum_height=character_layout.setter("height"))

            character_image: Image = Image(
                texture=_load_texture(data["image_path"]),
                size=(158, 158),
                size_hint=(None, None),
                allow_stretch=True,
                opacity=0.15,
            )

            self.character_images.append(character_image)

            character_layout.add_widget(character_image)

            character_location_label: Label = Label(
                text="In Logic: [color=888888]0[/color]\nOut of Logic: [color=888888]0[/color]",
                markup=True,
                font_size="12dp",
                size_hint_y=None,
                height="32dp",
                halign="left",
                valign="top",
            )

            _bind_text_size(character_location_label)

            self.character_location_labels.append(character_location_label)

            if self.ctx.tracker_loaded:
                character_layout.add_widget(character_location_label)

            character_stats_label: Label = Label(
                text=(
                    "Powerup Choices: [color=888888]1[/color] / [color=888888]5[/color]\n"
                    "Heart Containers: [color=888888]0[/color] / [color=888888]5[/color]\n"
                    "Soul Heart Capacity: [color=888888]0[/color] / [color=888888]3[/color]"
                ),
                markup=True,
                font_size="12dp",
                size_hint_y=None,
                height="48dp",
                halign="left",
                valign="top",
            )

            _bind_text_size(character_stats_label)

            self.character_stats_labels.append(character_stats_label)

            character_layout.add_widget(character_stats_label)

            grid_layout.add_widget(character_layout)

        self.add_widget(grid_layout)

    def update(self) -> None:
        received_items: Dict[str, int] = _get_received_items(self.ctx)

        character: TwentyMinutesCharacters
        data: Dict[str, Any]
        for i, (character, data) in enumerate(self.character_data.items()):
            is_unlocked: bool = received_items.get(data["unlock_item"], 0) > 0

            has_texture: bool = self.character_images[i].texture is not None
            self.character_images[i].opacity = _unlocked_opacity(is_unlocked, has_texture)

            if self.ctx.tracker_loaded:
                character_name: str = character.value

                in_logic_count: int = sum(
                    1 for location_name in self.ctx.locations_in_logic if f" - {character_name} - " in location_name
                )
                out_of_logic_count: int = sum(
                    1 for location_name in self.ctx.locations_out_of_logic if f" - {character_name} - " in location_name
                )

                if is_unlocked:
                    in_logic_color: str = "00FA9A" if in_logic_count > 0 else "888888"
                    out_of_logic_color: str = "FFD300" if out_of_logic_count > 0 else "888888"
                else:
                    in_logic_color = out_of_logic_color = "888888"

                location_text: str = (
                    f"In Logic: [color={in_logic_color}]{in_logic_count}[/color]\n"
                    f"Out of Logic: [color={out_of_logic_color}]{out_of_logic_count}[/color]"
                )

                self.character_location_labels[i].text = _apply_lock_gray(location_text, is_unlocked)

            powerup_choice_count: int = 1 + received_items.get(f"Progressive Powerup Choices: {character.value}", 0)
            heart_container_count: int = received_items.get(f"Heart Container: {character.value}", 0)
            soul_heart_capacity_count: int = received_items.get(f"Soul Heart Capacity: {character.value}", 0)

            stats_color: str = "00FA9A" if is_unlocked else "888888"

            stats_text: str = (
                f"Powerup Choices: [color={stats_color}]{powerup_choice_count}[/color] / [color={stats_color}]5[/color]\n"
                f"Heart Containers: [color={stats_color}]{heart_container_count}[/color] / [color={stats_color}]5[/color]\n"
                f"Soul Heart Capacity: [color={stats_color}]{soul_heart_capacity_count}[/color] / [color={stats_color}]3[/color]"
            )

            self.character_stats_labels[i].text = _apply_lock_gray(stats_text, is_unlocked)


class WeaponsLayout(BoxLayout):
    ctx: TwentyMinutesContext

    weapons_label: Label

    weapon_images: List[Image]
    weapon_location_labels: List[Label]
    weapon_stats_left_labels: List[Label]
    weapon_stats_right_labels: List[Label]

    weapon_data_by_weapon: Dict[TwentyMinutesWeapons, Dict[str, Any]]

    def __init__(self, ctx: TwentyMinutesContext) -> None:
        super().__init__(orientation="vertical", size_hint_y=None, height="40dp", spacing="8dp")

        self.bind(minimum_height=self.setter("height"))

        self.ctx = ctx

        self.weapons_label = Label(
            text="[b]Weapons[/b]",
            markup=True,
            font_size="32dp",
            size_hint_y=None,
            height="70dp",
            halign="left",
            valign="bottom",
        )

        _bind_text_size(self.weapons_label)

        self.add_widget(self.weapons_label)

        self.weapon_images = list()
        self.weapon_location_labels = list()
        self.weapon_stats_left_labels = list()
        self.weapon_stats_right_labels = list()

        self.weapon_data_by_weapon = dict()

        weapon: TwentyMinutesWeapons
        for weapon in self.ctx.game_controller.selected_weapons:
            self.weapon_data_by_weapon[weapon] = {
                "image_path": f"assets/{weapon.value}.png",
                "unlock_item": f"Weapon Unlock: {weapon.value}",
            }

        grid_layout: GridLayout = GridLayout(
            cols=1,
            spacing=12,
            padding=0,
            size_hint_y=None,
        )

        grid_layout.bind(minimum_height=grid_layout.setter("height"))

        weapon: TwentyMinutesWeapons
        data: Dict[str, Any]
        for weapon, data in self.weapon_data_by_weapon.items():
            weapon_layout: BoxLayout = BoxLayout(
                orientation="horizontal",
                size_hint_y=None,
                height="140dp",
                spacing="12dp",
            )

            weapon_layout.bind(minimum_height=weapon_layout.setter("height"))

            weapon_image: Image = Image(
                texture=_load_texture(data["image_path"]),
                size=(140, 140),
                size_hint=(None, None),
                pos_hint={"top": 1},
                allow_stretch=True,
                opacity=0.15,
            )

            self.weapon_images.append(weapon_image)

            weapon_layout.add_widget(weapon_image)

            stats_column: BoxLayout = BoxLayout(
                orientation="vertical", size_hint_y=None, height="140dp", spacing="4dp", pos_hint={"top": 1}
            )

            stats_column.bind(minimum_height=stats_column.setter("height"))

            weapon_location_label: Label = Label(
                text="In Logic: [color=888888]0[/color]\nOut of Logic: [color=888888]0[/color]",
                markup=True,
                font_size="12dp",
                size_hint_y=None,
                height="32dp",
                halign="left",
                valign="top",
            )

            _bind_text_size(weapon_location_label)

            self.weapon_location_labels.append(weapon_location_label)

            if self.ctx.tracker_loaded:
                stats_column.add_widget(weapon_location_label)

            stats_row: BoxLayout = BoxLayout(orientation="horizontal", size_hint_y=None, height="104dp", spacing="24dp")

            weapon_stats_left_label: Label = Label(
                text="",
                markup=True,
                font_size="13dp",
                size_hint_y=None,
                height="104dp",
                halign="left",
                valign="top",
            )

            _bind_text_size(weapon_stats_left_label)

            self.weapon_stats_left_labels.append(weapon_stats_left_label)

            stats_row.add_widget(weapon_stats_left_label)

            weapon_stats_right_label: Label = Label(
                text="",
                markup=True,
                font_size="13dp",
                size_hint_y=None,
                height="104dp",
                halign="left",
                valign="top",
            )

            _bind_text_size(weapon_stats_right_label)

            self.weapon_stats_right_labels.append(weapon_stats_right_label)

            stats_row.add_widget(weapon_stats_right_label)

            stats_column.add_widget(stats_row)

            weapon_layout.add_widget(stats_column)

            grid_layout.add_widget(weapon_layout)

        self.add_widget(grid_layout)

    def update(self) -> None:
        received_items: Dict[str, int] = _get_received_items(self.ctx)

        weapon: TwentyMinutesWeapons
        data: Dict[str, Any]
        for i, (weapon, data) in enumerate(self.weapon_data_by_weapon.items()):
            is_unlocked: bool = received_items.get(data["unlock_item"], 0) > 0

            has_texture: bool = self.weapon_images[i].texture is not None
            self.weapon_images[i].opacity = _unlocked_opacity(is_unlocked, has_texture)

            if self.ctx.tracker_loaded:
                weapon_name: str = weapon.value

                in_logic_count: int = sum(
                    1 for location_name in self.ctx.locations_in_logic if f" - {weapon_name} - " in location_name
                )
                out_of_logic_count: int = sum(
                    1 for location_name in self.ctx.locations_out_of_logic if f" - {weapon_name} - " in location_name
                )

                if is_unlocked:
                    in_logic_color: str = "00FA9A" if in_logic_count > 0 else "888888"
                    out_of_logic_color: str = "FFD300" if out_of_logic_count > 0 else "888888"
                else:
                    in_logic_color = out_of_logic_color = "888888"

                location_text: str = (
                    f"In Logic: [color={in_logic_color}]{in_logic_count}[/color]\n"
                    f"Out of Logic: [color={out_of_logic_color}]{out_of_logic_count}[/color]"
                )

                self.weapon_location_labels[i].text = _apply_lock_gray(location_text, is_unlocked)

            vanilla_stats: TwentyMinutesWeaponData = weapon_to_vanilla_weapon_data[weapon]

            weapon_stats: TwentyMinutesWeaponData = (self.ctx.game_controller.weapon_data or dict()).get(
                weapon, vanilla_stats
            )

            stats_color: str = "00FA9A" if is_unlocked else "888888"

            left_text: str = (
                f"Damage: {_format_weapon_attribute(weapon_stats.damage, vanilla_stats.damage, stats_color)}\n"
                f"Shot Cooldown: {_format_weapon_attribute(weapon_stats.shot_cooldown, vanilla_stats.shot_cooldown, stats_color, 's')}\n"
                f"Max Ammo: {_format_weapon_attribute(weapon_stats.maximum_ammunition, vanilla_stats.maximum_ammunition, stats_color)}\n"
                f"Reload Time: {_format_weapon_attribute(weapon_stats.reload_time, vanilla_stats.reload_time, stats_color, 's')}\n"
                f"Projectiles: {_format_weapon_attribute(weapon_stats.number_of_projectiles, vanilla_stats.number_of_projectiles, stats_color)}\n"
                f"Spread: {_format_weapon_attribute(weapon_stats.spread, vanilla_stats.spread, stats_color)}"
            )

            self.weapon_stats_left_labels[i].text = _apply_lock_gray(left_text, is_unlocked)

            right_text: str = (
                f"Knockback: {_format_weapon_attribute(weapon_stats.knockback, vanilla_stats.knockback, stats_color)}\n"
                f"Projectile Speed: {_format_weapon_attribute(weapon_stats.projectile_speed, vanilla_stats.projectile_speed, stats_color)}\n"
                f"Bounce: {_format_weapon_attribute(weapon_stats.bounce, vanilla_stats.bounce, stats_color)}\n"
                f"Piercing: {_format_weapon_attribute(weapon_stats.piercing, vanilla_stats.piercing, stats_color)}\n"
                f"Inaccuracy: {_format_weapon_attribute(weapon_stats.inaccuracy, vanilla_stats.inaccuracy, stats_color)}"
            )

            self.weapon_stats_right_labels[i].text = _apply_lock_gray(right_text, is_unlocked)


class TwentyMinutesContent(ScrollView):
    ctx: TwentyMinutesContext

    layout: BoxLayout

    layout_game_information: GameInformationLayout
    layout_maps: MapsLayout
    layout_characters: CharactersLayout
    layout_weapons: WeaponsLayout

    timer: Clock

    def __init__(self, ctx: TwentyMinutesContext) -> None:
        super().__init__()

        self.ctx = ctx

        self.layout = BoxLayout(orientation="vertical", size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter("height"))

        self.layout_game_information = GameInformationLayout(ctx=self.ctx)
        self.layout.add_widget(self.layout_game_information)

        self.layout_maps = MapsLayout(ctx=self.ctx)
        self.layout.add_widget(self.layout_maps)

        self.layout_characters = CharactersLayout(ctx=self.ctx)
        self.layout.add_widget(self.layout_characters)

        self.layout_weapons = WeaponsLayout(ctx=self.ctx)
        self.layout.add_widget(self.layout_weapons)

        self.add_widget(self.layout)

        self.timer = Clock.schedule_interval(self.update, 1.0 / 10.0)

    def update(self, *_) -> None:
        try:
            self.layout_game_information.update()
            self.layout_maps.update()
            self.layout_characters.update()
            self.layout_weapons.update()
        except Exception:
            import traceback

            with open("20_minutes_till_dawn_errors.log", "a") as f:
                f.write(traceback.format_exc() + "\n\n")


class TwentyMinutesTabLayout(BoxLayout):
    ctx: TwentyMinutesContext

    layout_content: BoxLayout
    layout_content_twenty_minutes: TwentyMinutesContent

    layout_not_connected: NotConnectedLayout

    def __init__(self, ctx: TwentyMinutesContext) -> None:
        super().__init__(orientation="vertical", padding="8dp")

        self.bind(minimum_height=self.setter("height"))

        self.ctx = ctx

        self.layout_not_connected = NotConnectedLayout(self.ctx)
        self.add_widget(self.layout_not_connected)

        self.layout_content = BoxLayout(orientation="horizontal", spacing="16dp", padding=["8dp", "0dp"])
        self.add_widget(self.layout_content)

        self.update()

    def update(self) -> None:
        if self.ctx.game_controller.selected_characters is None:
            self.layout_not_connected.show()

            if hasattr(self, "layout_content_twenty_minutes"):
                self.layout_content_twenty_minutes.timer.cancel()

            self.layout_content.clear_widgets()

            return

        self.layout_not_connected.hide()

        if not len(self.layout_content.children):
            self.layout_content_twenty_minutes = TwentyMinutesContent(ctx=self.ctx)
            self.layout_content.add_widget(self.layout_content_twenty_minutes)

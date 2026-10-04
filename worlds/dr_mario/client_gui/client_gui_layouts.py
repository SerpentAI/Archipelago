from typing import Dict, List, Optional, Set, Tuple

import copy
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

from ..client import DrMarioContext

from ..data.item_data import pill_color_order

from ..enums import (
    DrMarioColors,
    DrMarioGoalOptions,
    DrMarioLevels,
    DrMarioModes,
    DrMarioSpeeds,
)

from ..game_state_manager import GameState

from .. import client_gui


def _load_texture(image_path: str) -> Texture:
    image_bytes: bytes = pkgutil.get_data(client_gui.__name__, image_path)
    image: CoreImage = CoreImage(io.BytesIO(image_bytes), ext="png")

    image.texture.mag_filter = "nearest"
    image.texture.min_filter = "nearest"

    return image.texture


def _make_location_label(text: str) -> Label:
    label: Label = Label(
        text=text,
        markup=True,
        size_hint_y=None,
        font_size="12dp",
        height="16dp",
        halign="left",
        valign="middle",
        shorten=True,
        shorten_from="right",
        max_lines=1,
    )

    label.bind(size=lambda label, size: setattr(label, "text_size", size))

    return label


def _format_owned(is_owned: bool) -> str:
    return "[color=00FA9A]+[/color]" if is_owned else "[color=FF4C4C]-[/color]"


class NotConnectedLayout(BoxLayout):
    def __init__(self) -> None:
        super().__init__(orientation="horizontal", size_hint_y=0.12)

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


class ItemsFeedLayout(BoxLayout):
    ctx: DrMarioContext

    message_labels: List[Label]

    last_seen_messages: Optional[List[List[Dict]]]

    def __init__(self, ctx: DrMarioContext) -> None:
        super().__init__(orientation="vertical", size_hint_y=None, height="0dp", padding=[0, 0, 0, 20])

        self.bind(minimum_height=self.setter("height"))

        self.ctx = ctx

        self.message_labels = list()

        _: int
        for _ in range(self.ctx.item_messages.maxlen):
            message_label: Label = _make_location_label("")
            message_label.height = "0dp"

            self.message_labels.append(message_label)
            self.add_widget(message_label)

        self.last_seen_messages = None

    def update(self) -> None:
        messages: List[List[Dict]] = list(self.ctx.item_messages)

        if messages == self.last_seen_messages:
            return

        i: int
        message_label: Label
        for i, message_label in enumerate(self.message_labels):
            if i < len(messages):
                message_label.text = self.ctx.ui.json_to_kivy_parser(copy.deepcopy(messages[i]))
                message_label.height = "16dp"
            else:
                message_label.text = ""
                message_label.height = "0dp"

        self.last_seen_messages = messages


class GameInformationLayout(BoxLayout):
    ctx: DrMarioContext

    antiviral_serum_label: Label

    level_image: Image

    title_label: Label
    subtitle_label: Label
    loadout_label: Label

    locations_in_logic_label: Label
    locations_out_of_logic_label: Label

    last_seen_level: Optional[DrMarioLevels]

    def __init__(self, ctx: DrMarioContext) -> None:
        super().__init__(orientation="vertical", size_hint_y=None, height="280dp", spacing="8dp")

        self.bind(minimum_height=self.setter("height"))

        self.ctx = ctx

        # Header
        information_label: Label = Label(
            text="[b]Game Information[/b]",
            markup=True,
            font_size="32dp",
            size_hint_y=None,
            height="38dp",
            halign="left",
            valign="middle",
        )

        information_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.add_widget(information_label)

        # Antiviral Serum / Goal
        goal_header_layout: BoxLayout = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height="60dp",
            spacing="8dp",
            padding=[0, 0, 0, 10],
        )

        goal_header_layout.bind(minimum_height=goal_header_layout.setter("height"))

        self.antiviral_serum_label = Label(
            text="",
            markup=True,
            size_hint_x=40,
            size_hint_y=None,
            height="60dp",
            halign="left",
            valign="middle",
        )

        self.antiviral_serum_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        goal_header_layout.add_widget(self.antiviral_serum_label)

        goal_text: str = "[b]Goal[/b]\n?"

        if self.ctx.game_controller.option_goal == DrMarioGoalOptions.ANTIVIRAL_SERUM_HUNT:
            goal_text = "[b]Goal[/b]\nCollect the Antiviral Serum!"
        elif self.ctx.game_controller.option_goal == DrMarioGoalOptions.ANTIVIRAL_SERUM_FINAL_LEVEL:
            goal_text = (
                "[b]Goal[/b]\n"
                f"Collect the Antiviral Serum and clear {self.ctx.game_controller.selected_final_level.value} "
                f"on {self.ctx.game_controller.option_final_level_speed.name.title()}!"
            )

        goal_label: Label = Label(
            text=goal_text,
            markup=True,
            size_hint_x=60,
            size_hint_y=None,
            height="60dp",
            halign="left",
            valign="middle",
        )

        goal_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        goal_header_layout.add_widget(goal_label)

        self.add_widget(goal_header_layout)

        # Current Level
        level_information_layout: BoxLayout = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height="135dp",
            spacing="16dp",
            padding=[0, 0, 0, 10],
        )

        level_information_layout.bind(minimum_height=level_information_layout.setter("height"))

        self.level_image = Image(size=(180, 125), size_hint=(None, None), pos_hint={"top": 1}, allow_stretch=True, opacity=0.15)
        level_information_layout.add_widget(self.level_image)

        text_layout: BoxLayout = BoxLayout(orientation="vertical", size_hint_y=None, height="125dp", spacing="4dp")
        text_layout.bind(minimum_height=text_layout.setter("height"))

        self.title_label = Label(
            text="[b]No level selected...[/b]",
            markup=True,
            size_hint_y=None,
            font_size="16dp",
            height="20dp",
            halign="left",
            valign="middle",
        )

        self.title_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        text_layout.add_widget(self.title_label)

        self.subtitle_label = Label(
            text="",
            markup=True,
            size_hint_y=None,
            font_size="13dp",
            height="17dp",
            halign="left",
            valign="middle",
        )

        self.subtitle_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        text_layout.add_widget(self.subtitle_label)

        text_layout.add_widget(Widget(size_hint_y=None, height="6dp"))

        loadout_line_count: int = 1

        if self.ctx.game_controller.option_lock_next_pill_preview or self.ctx.game_controller.option_restrict_rotations:
            loadout_line_count += 1

        if self.ctx.game_controller.option_starting_garbage_levels > 0:
            loadout_line_count += 1

        self.loadout_label = Label(
            text="",
            markup=True,
            size_hint_y=None,
            font_size="15dp",
            line_height=1.3,
            height=f"{loadout_line_count * 25}dp",
            halign="left",
            valign="top",
        )

        self.loadout_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        text_layout.add_widget(self.loadout_label)

        level_information_layout.add_widget(text_layout)

        self.add_widget(level_information_layout)

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

        locations_in_logic_header.bind(size=lambda label, size: setattr(label, "text_size", size))

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

        locations_out_of_logic_header.bind(size=lambda label, size: setattr(label, "text_size", size))

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

        self.last_seen_level = None

    def update(self, received_items: Dict[str, int]) -> None:
        # Antiviral Serum
        self.antiviral_serum_label.text = (
            "[b]Antiviral Serum[/b]\n"
            f"Collected [color=00FA9A]{received_items.get('Antiviral Serum', 0)}[/color] of "
            f"[color=00FA9A]{self.ctx.game_controller.option_antiviral_serum_required}[/color] needed "
            f"([color=888888]{self.ctx.game_controller.option_antiviral_serum_total} total[/color])"
        )

        # Current Level
        game_state: Optional[GameState] = self.ctx.game_controller.game_state

        if (
            game_state is None
            or not game_state.is_valid
            or game_state.mode not in (DrMarioModes.OPTIONS, DrMarioModes.VIRUS_PLACEMENT, DrMarioModes.PLAYING)
            or game_state.level > 20
        ):
            self._clear_live_current_state()
            return

        current_level: DrMarioLevels = list(DrMarioLevels)[game_state.level]

        if game_state.is_between_levels and self.ctx.game_controller.tracked_level is not None:
            current_level = self.ctx.game_controller.tracked_level

        if self.last_seen_level != current_level:
            self.level_image.texture = _load_texture(f"assets/{list(DrMarioLevels).index(current_level)}.png")
            self.level_image.opacity = 1.0

            self.last_seen_level = current_level

        is_in_seed: bool = current_level in self.ctx.game_controller.selected_levels or current_level == self.ctx.game_controller.selected_final_level

        levels: List[DrMarioLevels] = list(DrMarioLevels)

        unlocked_levels: List[DrMarioLevels]

        if self.ctx.game_controller.option_progressive_level_unlocks:
            progressive_level_unlocks: int = received_items.get("Progressive Level Unlock", 0)
            unlocked_levels = [level for level in self.ctx.game_controller.selected_levels if levels.index(level) <= progressive_level_unlocks + 2]
        else:
            unlocked_levels = [level for level in self.ctx.game_controller.selected_levels if received_items.get(f"Level Unlock: {level.value}", 0) > 0]

        if self.ctx.game_controller.option_goal == DrMarioGoalOptions.ANTIVIRAL_SERUM_FINAL_LEVEL:
            if received_items.get("Antiviral Serum", 0) >= self.ctx.game_controller.option_antiviral_serum_required:
                unlocked_levels.append(self.ctx.game_controller.selected_final_level)

        is_unlocked: bool = current_level in unlocked_levels

        title_text: str = f"[b]{current_level.value} - {game_state.speed.value}[/b]"

        if game_state.mode == DrMarioModes.OPTIONS:
            title_text += " [color=888888](Options)[/color]"

        self.title_label.text = title_text
        self.subtitle_label.text = f"In Seed? {_format_owned(is_in_seed)}    Unlocked? {_format_owned(is_unlocked)}"

        loadout_text: str = self._build_loadout_text(current_level, received_items)

        if not is_in_seed:
            loadout_text = f"[color=888888]{loadout_text}[/color]"

        self.loadout_label.text = loadout_text

        # Locations In / Out of Logic
        if self.ctx.tracker_loaded:
            level_name: str = current_level.value

            in_logic_lines: List[str] = list()
            out_of_logic_lines: List[str] = list()

            location_name: str
            for location_name in sorted(self.ctx.locations_in_logic + self.ctx.locations_out_of_logic):
                if not location_name.startswith(f"{level_name} - "):
                    continue

                display_name: str = location_name.split(" - ", 1)[-1]

                if self.ctx.game_controller.option_randomize_virus_colors:
                    color: DrMarioColors
                    for color in DrMarioColors:
                        if f" {color.value} " in display_name:
                            display_name += f"  ({self.ctx.game_controller.selected_virus_colors[color].name.replace('_', ' ').title()})"

                if location_name in self.ctx.locations_in_logic:
                    in_logic_lines.append(f"[color=00FA9A]{display_name}[/color]")
                else:
                    out_of_logic_lines.append(f"[color=FFD300]{display_name}[/color]")

            if in_logic_lines:
                self.locations_in_logic_label.text = "\n".join(in_logic_lines)
            else:
                self.locations_in_logic_label.text = "[color=888888]No locations accessible in logic[/color]"

            if out_of_logic_lines:
                self.locations_out_of_logic_label.text = "\n".join(out_of_logic_lines)
            else:
                self.locations_out_of_logic_label.text = "[color=888888]No locations accessible out of logic[/color]"

    def _build_loadout_text(self, level: Optional[DrMarioLevels], received_items: Dict[str, int]) -> str:
        pill_texts: List[str] = list()

        index: int
        left_color: DrMarioColors
        for index, left_color in enumerate(pill_color_order):
            right_color: DrMarioColors
            for right_color in pill_color_order[index:]:
                pill_abbreviation: str = f"{left_color.value[0]}{right_color.value[0]}"

                if level is None:
                    pill_texts.append(f"{pill_abbreviation} -")
                else:
                    pill_item: str = f"{level.value}: {left_color.value}-{right_color.value} Pill"
                    pill_texts.append(f"{pill_abbreviation} {_format_owned(received_items.get(pill_item, 0) > 0)}")

        loadout_lines: List[str] = [f"[b]Pills:[/b] {'   '.join(pill_texts)}"]

        control_items: List[Tuple[str, str]] = list()

        if self.ctx.game_controller.option_lock_next_pill_preview:
            control_items.append(("Next Pill Preview", "Next Pill Preview"))

        if self.ctx.game_controller.option_restrict_rotations:
            control_items.append(("Clockwise Rotation", "Clockwise Spin"))
            control_items.append(("Counterclockwise Rotation", "Counterclockwise Spin"))

        control_texts: List[str] = list()

        control_item: str
        control_label: str
        for control_item, control_label in control_items:
            if level is None:
                control_texts.append(f"[b]{control_label}:[/b] -")
            else:
                control_texts.append(f"[b]{control_label}:[/b] {_format_owned(received_items.get(f'{level.value}: {control_item}', 0) > 0)}")

        if control_texts:
            loadout_lines.append("    ".join(control_texts))

        if self.ctx.game_controller.option_starting_garbage_levels > 0:
            if level is None:
                loadout_lines.append("[b]Starting Garbage Levels:[/b] -  Starting: -")
            else:
                garbage_levels: int = max(0, 3 - received_items.get(f"{level.value}: Progressive Starting Garbage Reduction", 0))

                loadout_lines.append(
                    f"[b]Starting Garbage Levels:[/b] [color=00FA9A]{garbage_levels}[/color]  "
                    f"[color=888888]Starting: {self.ctx.game_controller.level_to_starting_garbage_levels[level]}[/color]"
                )

        loadout_text: str = "\n".join(loadout_lines)

        if level is None:
            return f"[color=888888]{loadout_text}[/color]"

        return loadout_text

    def _clear_live_current_state(self) -> None:
        self.level_image.texture = None
        self.level_image.opacity = 0.15

        self.title_label.text = "[b]No level selected...[/b]"
        self.subtitle_label.text = ""
        self.loadout_label.text = self._build_loadout_text(None, dict())

        self.locations_in_logic_label.text = "[color=888888]No locations accessible in logic[/color]"
        self.locations_out_of_logic_label.text = "[color=888888]No locations accessible out of logic[/color]"

        self.last_seen_level = None


class GlobalItemsLayout(BoxLayout):
    ctx: DrMarioContext

    global_items_text_label: Label

    is_match_length_shown: bool
    is_speeds_shown: bool
    is_music_shown: bool

    def __init__(self, ctx: DrMarioContext) -> None:
        super().__init__(orientation="vertical", size_hint_y=None, height="40dp", spacing="8dp")

        self.bind(minimum_height=self.setter("height"))

        self.ctx = ctx

        self.is_match_length_shown = self.ctx.game_controller.option_starting_match_length > 3
        self.is_speeds_shown = self.ctx.game_controller.option_final_level_speed.value > 0
        self.is_music_shown = bool(self.ctx.game_controller.option_lock_music_choices)

        global_items_label: Label = Label(
            text="[b]Global Items[/b]",
            markup=True,
            font_size="32dp",
            size_hint_y=None,
            height="70dp",
            halign="left",
            valign="bottom",
        )

        global_items_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.add_widget(global_items_label)

        line_count: int = sum((self.is_match_length_shown, self.is_speeds_shown, self.is_music_shown))

        self.global_items_text_label = Label(
            text="",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            line_height=1.3,
            height=f"{line_count * 23}dp",
            halign="left",
            valign="top",
        )

        self.global_items_text_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.add_widget(self.global_items_text_label)

    def update(self, received_items: Dict[str, int]) -> None:
        lines: List[str] = list()

        if self.is_match_length_shown:
            match_length: int = max(3, 7 - received_items.get("Progressive Match Length Reduction", 0))

            lines.append(
                f"[b]Match Length:[/b] [color=00FA9A]{match_length}[/color]  "
                f"[color=888888]Starting: {self.ctx.game_controller.option_starting_match_length}[/color]"
            )

        if self.is_speeds_shown:
            progressive_speed_unlocks: int = received_items.get("Progressive Speed Unlock", 0)

            speed_texts: List[str] = [
                f"{speed.value} {_format_owned(index <= progressive_speed_unlocks)}"
                for index, speed in enumerate([DrMarioSpeeds.LOW, DrMarioSpeeds.MEDIUM, DrMarioSpeeds.HIGH][:1 + self.ctx.game_controller.option_final_level_speed.value])
            ]

            lines.append(f"[b]Speeds:[/b] {'    '.join(speed_texts)}")

        if self.is_music_shown:
            music_texts: List[str] = [
                f"{music_type} {_format_owned(received_items.get(f'Music Unlock: {music_type}', 0) > 0)}"
                for music_type in ("Fever", "Chill")
            ]

            lines.append(f"[b]Music:[/b] {'    '.join(music_texts)}")

        self.global_items_text_label.text = "\n".join(lines)


class LevelsLayout(BoxLayout):
    ctx: DrMarioContext

    levels: List[DrMarioLevels]

    level_images: List[Image]
    level_logic_labels: List[Label]

    def __init__(self, ctx: DrMarioContext) -> None:
        super().__init__(orientation="vertical", size_hint_y=None, height="40dp", spacing="8dp")

        self.bind(minimum_height=self.setter("height"))

        self.ctx = ctx

        levels_label: Label = Label(
            text="[b]Levels[/b]",
            markup=True,
            font_size="32dp",
            size_hint_y=None,
            height="70dp",
            halign="left",
            valign="bottom",
        )

        levels_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.add_widget(levels_label)

        self.levels = [
            level for level in DrMarioLevels
            if level in self.ctx.game_controller.selected_levels or level == self.ctx.game_controller.selected_final_level
        ]

        self.level_images = list()
        self.level_logic_labels = list()

        grid_layout: GridLayout = GridLayout(
            cols=6,
            spacing=12,
            padding=0,
            size_hint_y=None,
        )

        grid_layout.bind(minimum_height=grid_layout.setter("height"))

        level: DrMarioLevels
        for level in self.levels:
            is_goal: bool = (
                self.ctx.game_controller.option_goal == DrMarioGoalOptions.ANTIVIRAL_SERUM_FINAL_LEVEL
                and level == self.ctx.game_controller.selected_final_level
            )

            level_layout: BoxLayout = BoxLayout(
                orientation="vertical",
                size_hint_x=None,
                size_hint_y=None,
                width="104dp",
                height="72dp",
                spacing="4dp",
            )

            level_layout.bind(minimum_height=level_layout.setter("height"))

            level_image: Image = Image(
                texture=_load_texture(f"assets/{list(DrMarioLevels).index(level)}.png"),
                size=(104, 72),
                size_hint=(None, None),
                allow_stretch=True,
                opacity=0.3,
            )

            if is_goal:
                with level_image.canvas.after:
                    Color(1, 0.85, 0.2, 0.15)
                    fill_rect: Rectangle = Rectangle(pos=level_image.pos, size=level_image.size)

                    Color(1, 0.85, 0.2, 1.0)
                    border: Line = Line(rectangle=(*level_image.pos, *level_image.size), width=2)

                def _update_goal_decoration(*_, fill_rect=fill_rect, border=border, image=level_image) -> None:
                    fill_rect.pos = image.pos
                    fill_rect.size = image.size
                    border.rectangle = (*image.pos, *image.size)

                level_image.bind(pos=_update_goal_decoration, size=_update_goal_decoration)

            self.level_images.append(level_image)

            level_layout.add_widget(level_image)

            level_logic_label: Label = Label(
                text="In Logic: [color=888888]0[/color]\nOut of Logic: [color=888888]0[/color]",
                markup=True,
                font_size="12dp",
                size_hint_y=None,
                height="32dp",
                halign="left",
                valign="top",
            )

            level_logic_label.bind(size=lambda label, size: setattr(label, "text_size", size))

            self.level_logic_labels.append(level_logic_label)

            if self.ctx.tracker_loaded:
                if is_goal:
                    level_layout.add_widget(Widget(size_hint_y=None, height="32dp"))
                else:
                    level_layout.add_widget(level_logic_label)

            grid_layout.add_widget(level_layout)

        self.add_widget(grid_layout)

    def update(self, received_items: Dict[str, int]) -> None:
        levels: List[DrMarioLevels] = list(DrMarioLevels)

        unlocked_levels: List[DrMarioLevels]

        if self.ctx.game_controller.option_progressive_level_unlocks:
            progressive_level_unlocks: int = received_items.get("Progressive Level Unlock", 0)
            unlocked_levels = [level for level in self.ctx.game_controller.selected_levels if levels.index(level) <= progressive_level_unlocks + 2]
        else:
            unlocked_levels = [level for level in self.ctx.game_controller.selected_levels if received_items.get(f"Level Unlock: {level.value}", 0) > 0]

        if self.ctx.game_controller.option_goal == DrMarioGoalOptions.ANTIVIRAL_SERUM_FINAL_LEVEL:
            if received_items.get("Antiviral Serum", 0) >= self.ctx.game_controller.option_antiviral_serum_required:
                unlocked_levels.append(self.ctx.game_controller.selected_final_level)

        i: int
        level: DrMarioLevels
        for i, level in enumerate(self.levels):
            is_unlocked: bool = level in unlocked_levels

            self.level_images[i].opacity = 1.0 if is_unlocked else 0.3

            if self.ctx.tracker_loaded:
                level_name: str = level.value

                in_logic_count: int = sum(
                    1 for location_name in self.ctx.locations_in_logic if location_name.startswith(f"{level_name} - ")
                )
                out_of_logic_count: int = sum(
                    1 for location_name in self.ctx.locations_out_of_logic if location_name.startswith(f"{level_name} - ")
                )

                in_logic_color: str = "00FA9A" if is_unlocked and in_logic_count > 0 else "888888"
                out_of_logic_color: str = "FFD300" if is_unlocked and out_of_logic_count > 0 else "888888"

                logic_text: str = (
                    f"In Logic: [color={in_logic_color}]{in_logic_count}[/color]\n"
                    f"Out of Logic: [color={out_of_logic_color}]{out_of_logic_count}[/color]"
                )

                if not is_unlocked:
                    logic_text = f"[color=888888]{logic_text}[/color]"

                self.level_logic_labels[i].text = logic_text


class DrMarioContent(ScrollView):
    ctx: DrMarioContext

    layout: BoxLayout

    layout_items_feed: ItemsFeedLayout
    layout_game_information: GameInformationLayout
    layout_global_items: GlobalItemsLayout
    layout_levels: LevelsLayout

    timer: Clock

    logged_errors: Set[str]

    def __init__(self, ctx: DrMarioContext) -> None:
        super().__init__()

        self.ctx = ctx

        self.layout = BoxLayout(orientation="vertical", size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter("height"))

        self.layout_items_feed = ItemsFeedLayout(ctx=self.ctx)
        self.layout.add_widget(self.layout_items_feed)

        self.layout_game_information = GameInformationLayout(ctx=self.ctx)
        self.layout.add_widget(self.layout_game_information)

        self.layout_global_items = GlobalItemsLayout(ctx=self.ctx)

        if self.layout_global_items.is_match_length_shown or self.layout_global_items.is_speeds_shown or self.layout_global_items.is_music_shown:
            self.layout.add_widget(self.layout_global_items)

        self.layout_levels = LevelsLayout(ctx=self.ctx)
        self.layout.add_widget(self.layout_levels)

        self.add_widget(self.layout)

        self.logged_errors = set()

        self.timer = Clock.schedule_interval(self.update, 1.0 / 10.0)

    def update(self, *_) -> None:
        try:
            received_items: Dict[str, int] = dict()

            network_item: NetUtils.NetworkItem
            for network_item in self.ctx.items_received:
                if network_item.item in self.ctx.id_to_items:
                    item_name: str = self.ctx.id_to_items[network_item.item]

                    if item_name not in received_items:
                        received_items[item_name] = 0

                    received_items[item_name] += 1

            self.layout_items_feed.update()
            self.layout_game_information.update(received_items)
            self.layout_global_items.update(received_items)
            self.layout_levels.update(received_items)
        except Exception:
            import traceback

            error: str = traceback.format_exc()

            if error not in self.logged_errors:
                self.logged_errors.add(error)

                with open("dr_mario_errors.log", "a") as f:
                    f.write(error + "\n\n")


class DrMarioTabLayout(BoxLayout):
    ctx: DrMarioContext

    layout_content: BoxLayout
    layout_content_dr_mario: Optional[DrMarioContent]

    layout_not_connected: NotConnectedLayout

    def __init__(self, ctx: DrMarioContext) -> None:
        super().__init__(orientation="vertical", padding="8dp")

        self.bind(minimum_height=self.setter("height"))

        self.ctx = ctx

        self.layout_content_dr_mario = None

        self.layout_not_connected = NotConnectedLayout()
        self.add_widget(self.layout_not_connected)

        self.layout_content = BoxLayout(orientation="horizontal", spacing="16dp", padding=["8dp", "0dp"])
        self.add_widget(self.layout_content)

        self.update()

    def update(self) -> None:
        if self.ctx.game_controller.option_goal is None:
            self.layout_not_connected.show()

            if self.layout_content_dr_mario is not None:
                self.layout_content_dr_mario.timer.cancel()
                self.layout_content_dr_mario = None

            self.layout_content.clear_widgets()

            return

        self.layout_not_connected.hide()

        if not len(self.layout_content.children):
            self.layout_content_dr_mario = DrMarioContent(ctx=self.ctx)
            self.layout_content.add_widget(self.layout_content_dr_mario)

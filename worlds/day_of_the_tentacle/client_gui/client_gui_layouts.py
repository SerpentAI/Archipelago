from typing import Dict, List, Optional, Set

import copy
import io
import pkgutil

import NetUtils

from kivy.clock import Clock
from kivy.core.image import Image as CoreImage

from kivy.graphics.texture import Texture

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

from ..client import DayOfTheTentacleContext

from ..data.game_data import character_to_era
from ..data.location_data import location_data

from ..data_funcs import items_with_tag

from ..enums import (
    DayOfTheTentacleCharacters,
    DayOfTheTentacleGoalOptions,
    DayOfTheTentacleItems,
    DayOfTheTentacleLocations,
    DayOfTheTentacleRooms,
    DayOfTheTentacleTags,
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
    ctx: DayOfTheTentacleContext

    message_labels: List[Label]

    last_seen_messages: Optional[List[List[Dict]]]

    def __init__(self, ctx: DayOfTheTentacleContext) -> None:
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
    ctx: DayOfTheTentacleContext

    swiss_deposits_label: Label

    character_image: Image

    title_label: Label
    subtitle_label: Label

    locations_in_logic_header: Label
    locations_in_logic_list: BoxLayout

    last_seen_character: Optional[DayOfTheTentacleCharacters]
    last_seen_locations_in_logic: Optional[List[str]]

    def __init__(self, ctx: DayOfTheTentacleContext) -> None:
        super().__init__(orientation="vertical", size_hint_y=None, height="280dp", spacing="8dp")

        self.bind(minimum_height=self.setter("height"))

        self.ctx = ctx

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

        goal_header_layout: BoxLayout = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height="60dp",
            spacing="8dp",
            padding=[0, 0, 0, 10],
        )

        goal_header_layout.bind(minimum_height=goal_header_layout.setter("height"))

        self.swiss_deposits_label = Label(
            text="",
            markup=True,
            size_hint_x=40,
            size_hint_y=None,
            height="60dp",
            halign="left",
            valign="middle",
        )

        self.swiss_deposits_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        goal_header_layout.add_widget(self.swiss_deposits_label)

        goal_text: str = "[b]Goal[/b]\n?"

        if self.ctx.game_controller.option_goal == DayOfTheTentacleGoalOptions.STOP_PURPLE_TENTACLE:
            goal_text = "[b]Goal[/b]\nCollect the Swiss Deposits and Stop Purple Tentacle!"
        elif self.ctx.game_controller.option_goal == DayOfTheTentacleGoalOptions.SWISS_BANK_HEIST:
            goal_text = "[b]Goal[/b]\nGrab the Deposits and Bankbook, then Flee as Bernard!"

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

        character_information_layout: BoxLayout = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height="147dp",
            spacing="12dp",
            padding=[0, 0, 0, 10],
        )

        self.character_image = Image(
            size=(191, 137),
            size_hint=(None, None),
            allow_stretch=True,
            opacity=0.15,
        )

        character_information_layout.add_widget(self.character_image)

        text_layout: BoxLayout = BoxLayout(orientation="vertical", size_hint_y=None, height="137dp", spacing="4dp")

        self.title_label = Label(
            text="[b]Waiting for Day of the Tentacle...[/b]",
            markup=True,
            size_hint_y=None,
            font_size="20dp",
            height="26dp",
            halign="left",
            valign="middle",
        )

        self.title_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        text_layout.add_widget(self.title_label)

        self.subtitle_label = Label(
            text="",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="18dp",
            halign="left",
            valign="middle",
        )

        self.subtitle_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        text_layout.add_widget(self.subtitle_label)

        text_layout.add_widget(BoxLayout())

        character_information_layout.add_widget(text_layout)

        self.add_widget(character_information_layout)

        logic_layout: BoxLayout = BoxLayout(orientation="vertical", size_hint_y=None, spacing="4dp")

        logic_layout.bind(minimum_height=logic_layout.setter("height"))

        self.locations_in_logic_header = Label(
            text="[b]In Logic Locations[/b]",
            markup=True,
            size_hint_y=None,
            font_size="16dp",
            height="20dp",
            halign="left",
            valign="middle",
        )

        self.locations_in_logic_header.bind(size=lambda label, size: setattr(label, "text_size", size))

        logic_layout.add_widget(self.locations_in_logic_header)

        self.locations_in_logic_list = BoxLayout(orientation="vertical", size_hint_y=None)
        self.locations_in_logic_list.bind(minimum_height=self.locations_in_logic_list.setter("height"))

        logic_layout.add_widget(self.locations_in_logic_list)

        if self.ctx.tracker_loaded:
            self.add_widget(logic_layout)

        self.last_seen_locations_in_logic = None
        self._show_locations_in_logic(list())

        self.last_seen_character = None

    def update(self, received_items: Dict[DayOfTheTentacleItems, int]) -> None:
        self.swiss_deposits_label.text = (
            "[b]Swiss Deposits[/b]\n"
            f"Retrieved [color=00FA9A]{received_items.get(DayOfTheTentacleItems.SWISS_DEPOSIT, 0)}[/color] of "
            f"[color=00FA9A]{self.ctx.game_controller.option_swiss_deposits_required}[/color] needed "
            f"([color=888888]{self.ctx.game_controller.option_swiss_deposits_total} total[/color])"
        )

        game_state: Optional[GameState] = self.ctx.game_controller.game_state

        if game_state is None or not game_state.is_valid:
            self._clear_current_character()
            return

        current_character: Optional[DayOfTheTentacleCharacters] = game_state.character or self.last_seen_character

        if current_character is None:
            self._clear_current_character()
            return

        if self.last_seen_character != current_character:
            self.character_image.texture = _load_texture(f"assets/{current_character.value}.png")
            self.character_image.opacity = 1.0

            self.last_seen_character = current_character

        era_name: str
        era_tag: DayOfTheTentacleTags
        era_name, era_tag = character_to_era[current_character]

        subtitle: str = era_name

        if game_state.room is not None:
            subtitle = game_state.room.value

        if game_state.is_in_intro:
            subtitle += "  [color=888888](Intro)[/color]"

        self.title_label.text = f"[b]{current_character.value}[/b]"
        self.subtitle_label.text = subtitle

        if self.ctx.tracker_loaded:
            self.locations_in_logic_header.text = f"[b]In Logic Locations[/b]  [color=888888]{era_name}[/color]"

            self._show_locations_in_logic(sorted(
                location_name for location_name in self.ctx.locations_in_logic
                if era_tag in location_data[DayOfTheTentacleLocations(location_name)].tags
            ))

    def _show_locations_in_logic(self, location_names: List[str]) -> None:
        if location_names == self.last_seen_locations_in_logic:
            return

        self.locations_in_logic_list.clear_widgets()

        if not location_names:
            self.locations_in_logic_list.add_widget(_make_location_label("[color=888888]No locations accessible in logic[/color]"))

        location_name: str
        for location_name in location_names:
            self.locations_in_logic_list.add_widget(_make_location_label(f"[color=00FA9A]{location_name.split(' - ', 1)[-1]}[/color]"))

        self.last_seen_locations_in_logic = location_names

    def _clear_current_character(self) -> None:
        self.character_image.texture = None
        self.character_image.opacity = 0.15

        self.title_label.text = "[b]Waiting for Day of the Tentacle...[/b]"
        self.subtitle_label.text = ""

        self.locations_in_logic_header.text = "[b]In Logic Locations[/b]"

        self._show_locations_in_logic(list())

        self.last_seen_character = None


class CharactersLayout(BoxLayout):
    ctx: DayOfTheTentacleContext

    character_images: List[Image]
    character_location_labels: List[Label]
    character_room_labels: List[Label]

    def __init__(self, ctx: DayOfTheTentacleContext) -> None:
        super().__init__(orientation="vertical", size_hint_y=None, height="40dp", spacing="8dp")

        self.bind(minimum_height=self.setter("height"))

        self.ctx = ctx

        characters_label: Label = Label(
            text="[b]Characters[/b]",
            markup=True,
            font_size="32dp",
            size_hint_y=None,
            height="70dp",
            halign="left",
            valign="bottom",
        )

        characters_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.add_widget(characters_label)

        self.character_images = list()
        self.character_location_labels = list()
        self.character_room_labels = list()

        grid_layout: GridLayout = GridLayout(
            cols=len(character_to_era),
            spacing=12,
            padding=0,
            size_hint_y=None,
        )

        grid_layout.bind(minimum_height=grid_layout.setter("height"))

        character: DayOfTheTentacleCharacters
        for character in character_to_era:
            character_layout: BoxLayout = BoxLayout(
                orientation="vertical",
                size_hint_x=None,
                size_hint_y=None,
                width="191dp",
                height="181dp",
                spacing="4dp",
            )

            character_image: Image = Image(
                texture=_load_texture(f"assets/{character.value}.png"),
                size=(191, 137),
                size_hint=(None, None),
                allow_stretch=True,
                opacity=0.15,
            )

            self.character_images.append(character_image)

            character_layout.add_widget(character_image)

            character_location_label: Label = Label(
                text="In Logic: [color=888888]0[/color]",
                markup=True,
                font_size="12dp",
                size_hint_y=None,
                height="16dp",
                halign="left",
                valign="top",
            )

            character_location_label.bind(size=lambda label, size: setattr(label, "text_size", size))

            self.character_location_labels.append(character_location_label)

            if self.ctx.tracker_loaded:
                character_layout.add_widget(character_location_label)

            character_room_label: Label = Label(
                text="",
                font_size="12dp",
                size_hint_y=None,
                height="16dp",
                halign="left",
                valign="top",
                shorten=True,
                shorten_from="right",
                max_lines=1,
            )

            character_room_label.bind(size=lambda label, size: setattr(label, "text_size", size))

            self.character_room_labels.append(character_room_label)

            character_layout.add_widget(character_room_label)

            grid_layout.add_widget(character_layout)

        self.add_widget(grid_layout)

    def update(self, received_items: Dict[DayOfTheTentacleItems, int]) -> None:
        character_rooms: Dict[DayOfTheTentacleCharacters, Optional[DayOfTheTentacleRooms]] = dict()

        game_state: Optional[GameState] = self.ctx.game_controller.game_state

        if game_state is not None and game_state.is_valid and game_state.character_rooms is not None:
            character_rooms = game_state.character_rooms

        i: int
        character: DayOfTheTentacleCharacters
        era_tag: DayOfTheTentacleTags
        for i, (character, (_, era_tag)) in enumerate(character_to_era.items()):
            is_unlocked: bool = received_items.get(DayOfTheTentacleItems[f"CHARACTER_{character.name}"], 0) > 0

            self.character_images[i].opacity = 1.0 if is_unlocked else 0.15

            if self.ctx.tracker_loaded:
                in_logic_count: int = sum(
                    1 for location_name in self.ctx.locations_in_logic
                    if era_tag in location_data[DayOfTheTentacleLocations(location_name)].tags
                )

                in_logic_color: str = "00FA9A" if is_unlocked and in_logic_count > 0 else "888888"

                location_text: str = f"In Logic: [color={in_logic_color}]{in_logic_count}[/color]"

                if not is_unlocked:
                    location_text = f"[color=888888]{location_text}[/color]"

                self.character_location_labels[i].text = location_text

            room: Optional[DayOfTheTentacleRooms] = character_rooms.get(character)

            if is_unlocked and room is not None:
                self.character_room_labels[i].text = room.value.split(" - ", 1)[-1]
            else:
                self.character_room_labels[i].text = ""


class ReceivedItemsLayout(BoxLayout):
    ctx: DayOfTheTentacleContext

    items: List[DayOfTheTentacleItems]
    item_labels: List[Label]

    def __init__(self, ctx: DayOfTheTentacleContext) -> None:
        super().__init__(orientation="vertical", size_hint_y=None, height="40dp", spacing="8dp")

        self.bind(minimum_height=self.setter("height"))

        self.ctx = ctx

        received_items_label: Label = Label(
            text="[b]Received Items[/b]",
            markup=True,
            font_size="32dp",
            size_hint_y=None,
            height="70dp",
            halign="left",
            valign="bottom",
        )

        received_items_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.add_widget(received_items_label)

        self.items = sorted(items_with_tag(DayOfTheTentacleTags.INVENTORY_ITEM), key=lambda item: item.value)

        self.item_labels = list()

        item: DayOfTheTentacleItems
        for item in self.items:
            item_label: Label = Label(
                text=item.value,
                font_size="16dp",
                halign="left",
                valign="middle",
                opacity=0.2,
            )

            item_label.bind(size=lambda label, size: setattr(label, "text_size", size))

            self.item_labels.append(item_label)

        column_count: int = 2
        row_count: int = -(-len(self.items) // column_count)

        grid_layout: GridLayout = GridLayout(
            cols=column_count,
            size_hint_x=None,
            size_hint_y=None,
            width=f"{column_count * 300}dp",
            col_force_default=True,
            col_default_width="300dp",
            row_force_default=True,
            row_default_height="22dp",
        )

        grid_layout.bind(minimum_height=grid_layout.setter("height"))

        row: int
        for row in range(row_count):
            column: int
            for column in range(column_count):
                index: int = row + column * row_count

                grid_layout.add_widget(self.item_labels[index] if index < len(self.item_labels) else Label())

        self.add_widget(grid_layout)

    def update(self, received_items: Dict[DayOfTheTentacleItems, int]) -> None:
        item: DayOfTheTentacleItems
        item_label: Label
        for item, item_label in zip(self.items, self.item_labels):
            item_label.opacity = 1.0 if received_items.get(item, 0) > 0 else 0.2


class DayOfTheTentacleContent(ScrollView):
    ctx: DayOfTheTentacleContext

    layout: BoxLayout

    layout_items_feed: ItemsFeedLayout
    layout_game_information: GameInformationLayout
    layout_characters: CharactersLayout
    layout_received_items: ReceivedItemsLayout

    timer: Clock

    logged_errors: Set[str]

    def __init__(self, ctx: DayOfTheTentacleContext) -> None:
        super().__init__()

        self.ctx = ctx

        self.layout = BoxLayout(orientation="vertical", size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter("height"))

        self.layout_items_feed = ItemsFeedLayout(ctx=self.ctx)
        self.layout.add_widget(self.layout_items_feed)

        self.layout_game_information = GameInformationLayout(ctx=self.ctx)
        self.layout.add_widget(self.layout_game_information)

        self.layout_characters = CharactersLayout(ctx=self.ctx)
        self.layout.add_widget(self.layout_characters)

        self.layout_received_items = ReceivedItemsLayout(ctx=self.ctx)
        self.layout.add_widget(self.layout_received_items)

        self.add_widget(self.layout)

        self.logged_errors = set()

        self.timer = Clock.schedule_interval(self.update, 1.0 / 10.0)

    def update(self, *_) -> None:
        try:
            received_items: Dict[DayOfTheTentacleItems, int] = dict()

            network_item: NetUtils.NetworkItem
            for network_item in self.ctx.items_received:
                if network_item.item in self.ctx.id_to_items:
                    item: DayOfTheTentacleItems = self.ctx.id_to_items[network_item.item]

                    if item not in received_items:
                        received_items[item] = 0

                    received_items[item] += 1

            self.layout_items_feed.update()
            self.layout_game_information.update(received_items)
            self.layout_characters.update(received_items)
            self.layout_received_items.update(received_items)
        except Exception:
            import traceback

            error: str = traceback.format_exc()

            if error not in self.logged_errors:
                self.logged_errors.add(error)

                with open("day_of_the_tentacle_errors.log", "a") as f:
                    f.write(error + "\n\n")


class DayOfTheTentacleTabLayout(BoxLayout):
    ctx: DayOfTheTentacleContext

    layout_content: BoxLayout
    layout_content_day_of_the_tentacle: Optional[DayOfTheTentacleContent]

    layout_not_connected: NotConnectedLayout

    def __init__(self, ctx: DayOfTheTentacleContext) -> None:
        super().__init__(orientation="vertical", padding="8dp")

        self.bind(minimum_height=self.setter("height"))

        self.ctx = ctx

        self.layout_content_day_of_the_tentacle = None

        self.layout_not_connected = NotConnectedLayout()
        self.add_widget(self.layout_not_connected)

        self.layout_content = BoxLayout(orientation="horizontal", spacing="16dp", padding=["8dp", "0dp"])
        self.add_widget(self.layout_content)

        self.update()

    def update(self) -> None:
        if self.ctx.game_controller.option_goal is None:
            self.layout_not_connected.show()

            if self.layout_content_day_of_the_tentacle is not None:
                self.layout_content_day_of_the_tentacle.timer.cancel()
                self.layout_content_day_of_the_tentacle = None

            self.layout_content.clear_widgets()

            return

        self.layout_not_connected.hide()

        if not len(self.layout_content.children):
            self.layout_content_day_of_the_tentacle = DayOfTheTentacleContent(ctx=self.ctx)
            self.layout_content.add_widget(self.layout_content_day_of_the_tentacle)

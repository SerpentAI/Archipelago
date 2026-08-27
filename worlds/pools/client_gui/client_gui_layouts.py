from typing import Any, Dict, List, Optional

import io
import pkgutil

import NetUtils

from kivy.clock import Clock
from kivy.core.image import Image as CoreImage

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

from ..client import PoolsContext

from ..data.game_data import level_to_scene_internal_name

from ..enums import (
    PoolsGoals,
    PoolsItems,
    PoolsLevels,
)

from ..game_state_manager import GameStateManager, GameState

from .. import client_gui


class NotConnectedLayout(BoxLayout):
    ctx: PoolsContext

    def __init__(self, ctx: PoolsContext) -> None:
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


class PoolsGameInformationLayout(BoxLayout):
    ctx: PoolsContext

    game_state_manager: GameStateManager

    information_label: Label

    rubber_ducks_label: Label
    goal_label: Label

    level_information_level_image: Image

    run_label: Label

    ground_speed_label: Label
    water_speed_label: Label

    level_information_title: Label
    level_information_subtitle: Label

    pools_1t_label: Label
    pools_2t_label: Label
    pools_3t_label: Label
    pools_4t_label: Label
    pools_5t_label: Label
    pools_6t_label: Label
    pools_7t_label: Label
    pools_8t_label: Label
    pools_9t_label: Label
    pools_10t_label: Label
    pools_11t_label: Label

    slides_red_label: Label
    slides_yellow_label: Label
    slides_green_label: Label
    slides_blue_label: Label
    slides_extra_label: Label

    diving_boards_label: Label

    chairs_plastic_label: Label
    chairs_sauna_label: Label
    chairs_armchair_label: Label
    chairs_wooden_label: Label
    chairs_subway_label: Label
    chairs_park_label: Label
    chairs_sofa_label: Label

    last_seen_level: Optional[PoolsLevels]

    def __init__(self, ctx: PoolsContext) -> None:
        super().__init__(orientation="vertical", size_hint_y=None, height="400dp", spacing="8dp",)

        self.bind(minimum_height=self.setter("height"))

        self.ctx = ctx

        self.game_state_manager = GameStateManager()

        # Game Information
        self.information_label = Label(
            text=f"[b]Game Information[/b]",
            markup=True,
            font_size="32dp",
            size_hint_y=None,
            height="38dp",
            halign="left",
            valign="middle",
        )

        self.information_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.add_widget(self.information_label)

        goal_header_layout: BoxLayout = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height="74dp",
            spacing="8dp",
            padding=[0, 0, 0, 10]
        )

        goal_header_layout.bind(minimum_height=goal_header_layout.setter("height"))

        # Rubber Ducks
        self.rubber_ducks_label: Label = Label(
            text=(
                f"[b]Rubber Ducks[/b]\n"
                f"Retrieved [color=00FA9A]0[/color] of "
                f"[color=00FA9A]{self.ctx.game_controller.option_rubber_ducks_required}[/color] needed "
                f"([color=888888]{self.ctx.game_controller.option_rubber_ducks_total} total[/color])"
            ),
            markup=True,
            size_hint_x=40,
            size_hint_y=None,
            height="60dp",
            halign="left",
            valign="middle",
        )

        self.rubber_ducks_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        goal_header_layout.add_widget(self.rubber_ducks_label)

        # Goal
        self.goal_label: Label = Label(
            text=(
                f"[b]Goal[/b]\n"
                f"Retrieve the Rubber Ducks and Complete Level 6!"
            ),
            markup=True,
            size_hint_x=60,
            size_hint_y=None,
            height="60dp",
            halign="left",
            valign="middle",
        )

        self.goal_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        goal_header_layout.add_widget(self.goal_label)

        self.add_widget(goal_header_layout)

        # Level Information / Items / Movement Speed
        level_information_header_layout: BoxLayout = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height="256dp",
            spacing="16dp",
        )

        level_information_header_layout.bind(minimum_height=level_information_header_layout.setter("height"))

        level_information_image_subheader_layout: BoxLayout = BoxLayout(
            orientation="vertical",
            size_hint_x=None,
            size_hint_y=None,
            pos_hint={"top": 1},
            height="256dp",
            width="192dp",
            spacing="16dp",
        )

        level_information_image_subheader_layout.bind(minimum_height=level_information_image_subheader_layout.setter("height"))

        self.level_information_level_image = Image(
            size=(192, 128),
            size_hint=(None, None),
            allow_stretch=True,
            opacity=0.1
        )

        level_information_image_subheader_layout.add_widget(self.level_information_level_image)

        movement_speed_layout: BoxLayout = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            pos_hint={"top": 1},
            height="120dp",
            spacing="8dp",
        )

        movement_speed_layout.bind(minimum_height=movement_speed_layout.setter("height"))

        movement_speed_label: Label = Label(
            text="[b]Movement Speed[/b]",
            markup=True,
            size_hint_y=None,
            font_size="16dp",
            height="20dp",
            halign="left",
            valign="middle",
        )

        movement_speed_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        movement_speed_layout.add_widget(movement_speed_label)

        self.run_label = Label(
            text="Run: [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.run_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        movement_speed_layout.add_widget(self.run_label)

        self.ground_speed_label = Label(
            text="Ground Speed: [color=00FA9A]100%[/color] -> [color=00FA9A]100%[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.ground_speed_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        movement_speed_layout.add_widget(self.ground_speed_label)

        self.water_speed_label = Label(
            text="Water Speed: [color=00FA9A]100%[/color] -> [color=00FA9A]100%[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.water_speed_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        movement_speed_layout.add_widget(self.water_speed_label)

        level_information_image_subheader_layout.add_widget(movement_speed_layout)

        level_information_header_layout.add_widget(level_information_image_subheader_layout)

        level_information_subheader_layout: BoxLayout = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            pos_hint={"top": 1},
            height="256dp",
            spacing="8dp",
        )

        self.level_information_title = Label(
            text=f"[b]Begin Playing a POOLS Level...[/b]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="18dp",
            halign="left",
            valign="middle",
        )

        self.level_information_title.bind(size=lambda label, size: setattr(label, "text_size", size))

        level_information_subheader_layout.add_widget(self.level_information_title)

        self.level_information_subtitle = Label(
            text=f"[b]This level is not unlocked.[/b]",
            markup=True,
            size_hint_y=None,
            font_size="12dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.level_information_subtitle.bind(size=lambda label, size: setattr(label, "text_size", size))

        level_information_subheader_layout.add_widget(self.level_information_subtitle)

        item_unlocks_layout: BoxLayout = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height="206dp",
            spacing="8dp",
        )

        item_unlocks_layout.bind(minimum_height=item_unlocks_layout.setter("height"))

        pools_1_layout: BoxLayout = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            pos_hint={"top": 1},
            height="206dp",
            spacing="8dp",
        )

        pools_1_layout.bind(minimum_height=pools_1_layout.setter("height"))

        pool_depths_label: Label = Label(
            text="[b]Pool Depths[/b]",
            markup=True,
            size_hint_y=None,
            font_size="16dp",
            height="36dp",
            pos_hint={"top": 1},
            halign="left",
            valign="middle",
            padding=[0, 16, 0, 0]
        )

        pool_depths_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.pools_1t_label = Label(
            text="1 Tile Deep: [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.pools_1t_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.pools_2t_label = Label(
            text="2 Tiles Deep: [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.pools_2t_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.pools_3t_label = Label(
            text="3 Tiles Deep: [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.pools_3t_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.pools_4t_label = Label(
            text="4 Tiles Deep: [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.pools_4t_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.pools_5t_label = Label(
            text="5 Tiles Deep: [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.pools_5t_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.pools_6t_label = Label(
            text="6 Tiles Deep: [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.pools_6t_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        pools_1_layout.add_widget(pool_depths_label)
        pools_1_layout.add_widget(self.pools_1t_label)
        pools_1_layout.add_widget(self.pools_2t_label)
        pools_1_layout.add_widget(self.pools_3t_label)
        pools_1_layout.add_widget(self.pools_4t_label)
        pools_1_layout.add_widget(self.pools_5t_label)
        pools_1_layout.add_widget(self.pools_6t_label)

        pools_2_layout: BoxLayout = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            pos_hint={"top": 1},
            height="206dp",
            spacing="8dp",
        )

        pools_2_layout.bind(minimum_height=pools_2_layout.setter("height"))

        pool_depths_spacing_label: Label = Label(
            text="",
            markup=True,
            size_hint_y=None,
            font_size="16dp",
            height="36dp",
            pos_hint={"top": 1},
            halign="left",
            valign="middle",
            padding=[0, 16, 0, 0]
        )

        pool_depths_spacing_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.pools_7t_label = Label(
            text="7 Tiles Deep: [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.pools_7t_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.pools_8t_label = Label(
            text="8 Tiles Deep: [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.pools_8t_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.pools_9t_label = Label(
            text="9 Tiles Deep: [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.pools_9t_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.pools_10t_label = Label(
            text="10 Tiles Deep: [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.pools_10t_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.pools_11t_label = Label(
            text="11 Tiles Deep: [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.pools_11t_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        pools_2_layout.add_widget(pool_depths_spacing_label)
        pools_2_layout.add_widget(self.pools_7t_label)
        pools_2_layout.add_widget(self.pools_8t_label)
        pools_2_layout.add_widget(self.pools_9t_label)
        pools_2_layout.add_widget(self.pools_10t_label)
        pools_2_layout.add_widget(self.pools_11t_label)

        slides_layout: BoxLayout = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            pos_hint={"top": 1},
            height="206dp",
            spacing="8dp",
        )

        slides_layout.bind(minimum_height=slides_layout.setter("height"))

        slides_label: Label = Label(
            text="[b]Slides / Boards[/b]",
            markup=True,
            size_hint_y=None,
            font_size="16dp",
            height="36dp",
            pos_hint={"top": 1},
            halign="left",
            valign="middle",
            padding=[0, 16, 0, 0]
        )

        slides_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.slides_red_label = Label(
            text="Red Slides: [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.slides_red_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.slides_yellow_label = Label(
            text="Yellow Slides: [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.slides_yellow_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.slides_green_label = Label(
            text="Green Slides: [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.slides_green_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.slides_blue_label = Label(
            text="Blue Slides: [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.slides_blue_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.slides_extra_label = Label(
            text="Extra Slides: [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.slides_extra_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.diving_boards_label = Label(
            text="Diving Boards: [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="36dp",
            halign="left",
            valign="middle",
            padding=[0, 20, 0, 0]
        )

        self.diving_boards_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        slides_layout.add_widget(slides_label)
        slides_layout.add_widget(self.slides_red_label)
        slides_layout.add_widget(self.slides_yellow_label)
        slides_layout.add_widget(self.slides_green_label)
        slides_layout.add_widget(self.slides_blue_label)

        if self.ctx.game_controller.option_include_level_0:
            slides_layout.add_widget(self.slides_extra_label)

        slides_layout.add_widget(self.diving_boards_label)

        chairs_layout: BoxLayout = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            pos_hint={"top": 1},
            height="206dp",
            spacing="8dp",
        )

        chairs_layout.bind(minimum_height=chairs_layout.setter("height"))

        chairs_label: Label = Label(
            text="[b]Chair Types[/b]",
            markup=True,
            size_hint_y=None,
            font_size="16dp",
            height="36dp",
            pos_hint={"top": 1},
            halign="left",
            valign="middle",
            padding=[0, 16, 0, 0]
        )

        chairs_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.chairs_plastic_label = Label(
            text="Plastic Chairs: [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.chairs_plastic_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.chairs_sauna_label = Label(
            text="Sauna Benches: [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.chairs_sauna_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.chairs_armchair_label = Label(
            text="Armchairs: [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.chairs_armchair_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.chairs_wooden_label = Label(
            text="Wooden Chairs: [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.chairs_wooden_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.chairs_subway_label = Label(
            text="Subway Chairs: [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.chairs_subway_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.chairs_park_label = Label(
            text="Park Benches: [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.chairs_park_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.chairs_sofa_label = Label(
            text="Sofas: [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.chairs_sofa_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        chairs_layout.add_widget(chairs_label)
        chairs_layout.add_widget(self.chairs_plastic_label)
        chairs_layout.add_widget(self.chairs_sauna_label)
        chairs_layout.add_widget(self.chairs_armchair_label)
        chairs_layout.add_widget(self.chairs_wooden_label)
        chairs_layout.add_widget(self.chairs_subway_label)

        if self.ctx.game_controller.option_include_level_0:
            chairs_layout.add_widget(self.chairs_park_label)
            chairs_layout.add_widget(self.chairs_sofa_label)

        item_unlocks_layout.add_widget(pools_1_layout)
        item_unlocks_layout.add_widget(pools_2_layout)
        item_unlocks_layout.add_widget(slides_layout)

        if self.ctx.game_controller.option_include_chairs:
            item_unlocks_layout.add_widget(chairs_layout)

        level_information_subheader_layout.add_widget(item_unlocks_layout)

        level_information_header_layout.add_widget(level_information_subheader_layout)

        self.add_widget(level_information_header_layout)

        self.last_seen_level = None

    def update(self) -> None:
        ## Received Items
        received_items: Dict[PoolsItems, int] = dict()

        network_item: NetUtils.NetworkItem
        for network_item in self.ctx.items_received:
            if network_item.item in self.ctx.id_to_items:
                item: PoolsItems = self.ctx.id_to_items[network_item.item]

                if item not in received_items:
                    received_items[item] = 0

                received_items[item] += 1

        ## Game State
        game_state: GameState = None

        try:
            self.game_state_manager.is_process_still_running()

            if not self.game_state_manager.is_process_running:
                try:
                    self.game_state_manager.open_process_handle()
                except Exception:
                    pass

            if self.game_state_manager.is_process_running:
                game_state = self.game_state_manager.determine_game_state()
        except Exception:
            pass

        ## Updates

        # Rubber Ducks
        rubber_ducks_obtained: int = received_items.get(PoolsItems.RUBBER_DUCK, 0)

        self.rubber_ducks_label.text = (
            "[b]Rubber Ducks[/b]\n"
            f"Retrieved [color=00FA9A]{rubber_ducks_obtained}[/color] of "
            f"[color=00FA9A]{self.ctx.game_controller.option_rubber_ducks_required}[/color] needed "
            f"([color=888888]{self.ctx.game_controller.option_rubber_ducks_total} total[/color])"
        )

        # Goal
        if self.ctx.game_controller.option_goal == PoolsGoals.RUBBER_DUCKS_COMPLETE_LEVEL_6:
            self.goal_label.text = (
                "[b]Goal[/b]\n"
                f"Retrieve the Rubber Ducks and Complete Level 6!"
            )

        # Level
        if game_state is None or not game_state.is_valid or not game_state.is_in_level:
            self.level_information_level_image.texture = None
            self.level_information_level_image.opacity = 0.1

            self.level_information_title.text = f"[b]Begin Playing a POOLS Level...[/b]"
            self.level_information_subtitle.text = f"[b]This level is NOT unlocked.[/b]"

            self.last_seen_level = None
        else:
            if self.last_seen_level != game_state.level:
                image_path: str = f"assets/{level_to_scene_internal_name[game_state.level]}.png"
                image_bytes: bytes = pkgutil.get_data(client_gui.__name__, image_path)

                image: CoreImage = CoreImage(io.BytesIO(image_bytes), ext="png")

                self.level_information_level_image.texture = image.texture
                self.level_information_level_image.opacity = 1.0

                self.last_seen_level = game_state.level

            self.level_information_title.text = f"[b]{game_state.level.value}[/b]"

            level_unlock_item: PoolsItems = getattr(PoolsItems, f"{game_state.level.name}_UNLOCK")
            is_level_unlocked: bool = False

            if level_unlock_item in received_items and received_items[level_unlock_item] > 0:
                is_level_unlocked = True

            self.level_information_subtitle.text = f"[b]This level is unlocked.[/b]"

        mapping: Dict[bool, str] = {
            False: "[color=FF4C4C]-[/color]",
            True: "[color=00FA9A]+[/color]"
        }

        item_count_run: int = received_items.get(PoolsItems.RUN, 0)
        self.run_label.text = f"Run: {mapping[item_count_run > 0]}"

        item_count_ground: int = received_items.get(PoolsItems.PROGRESSIVE_MOVEMENT_SPEED, 0)
        item_count_water: int = received_items.get(PoolsItems.PROGRESSIVE_WATER_SPEED, 0)

        run_multiplier: float = 1.0

        if item_count_run > 0:
            run_multiplier = 1.5

        speed_ground_walk: int = int(round(((6 + item_count_ground) / 12) * 100.0))
        speed_ground_run: int = int(round((((6 + item_count_ground) * run_multiplier) / 12) * 100.0))

        speed_water_walk: int = int(round(((6 + item_count_water) / 12) * 100.0))
        speed_water_run: int = int(round((((6 + item_count_water) * run_multiplier) / 12) * 100.0))

        self.ground_speed_label.text = f"Ground Speed: [color=00FA9A]{speed_ground_walk}%[/color] -> [color=00FA9A]{speed_ground_run}%[/color]"
        self.water_speed_label.text = f"Water Speed: [color=00FA9A]{speed_water_walk}%[/color] -> [color=00FA9A]{speed_water_run}%[/color]"

        item_count: int = received_items.get(PoolsItems.POOLS_1T, 0)
        self.pools_1t_label.text = f"1 Tile Deep: {mapping[item_count > 0]}"

        item_count: int = received_items.get(PoolsItems.POOLS_2T, 0)
        self.pools_2t_label.text = f"2 Tiles Deep: {mapping[item_count > 0]}"

        item_count: int = received_items.get(PoolsItems.POOLS_3T, 0)
        self.pools_3t_label.text = f"3 Tiles Deep: {mapping[item_count > 0]}"

        item_count: int = received_items.get(PoolsItems.POOLS_4T, 0)
        self.pools_4t_label.text = f"4 Tiles Deep: {mapping[item_count > 0]}"

        item_count: int = received_items.get(PoolsItems.POOLS_5T, 0)
        self.pools_5t_label.text = f"5 Tiles Deep: {mapping[item_count > 0]}"

        item_count: int = received_items.get(PoolsItems.POOLS_6T, 0)
        self.pools_6t_label.text = f"6 Tiles Deep: {mapping[item_count > 0]}"

        item_count: int = received_items.get(PoolsItems.POOLS_7T, 0)
        self.pools_7t_label.text = f"7 Tiles Deep: {mapping[item_count > 0]}"

        item_count: int = received_items.get(PoolsItems.POOLS_8T, 0)
        self.pools_8t_label.text = f"8 Tiles Deep: {mapping[item_count > 0]}"

        item_count: int = received_items.get(PoolsItems.POOLS_9T, 0)
        self.pools_9t_label.text = f"9 Tiles Deep: {mapping[item_count > 0]}"

        item_count: int = received_items.get(PoolsItems.POOLS_10T, 0)
        self.pools_10t_label.text = f"10 Tiles Deep: {mapping[item_count > 0]}"

        item_count: int = received_items.get(PoolsItems.POOLS_11T, 0)
        self.pools_11t_label.text = f"11 Tiles Deep: {mapping[item_count > 0]}"

        item_count: int = received_items.get(PoolsItems.SLIDES_RED, 0)
        self.slides_red_label.text = f"Red Slides: {mapping[item_count > 0]}"

        item_count: int = received_items.get(PoolsItems.SLIDES_YELLOW, 0)
        self.slides_yellow_label.text = f"Yellow Slides: {mapping[item_count > 0]}"

        item_count: int = received_items.get(PoolsItems.SLIDES_GREEN, 0)
        self.slides_green_label.text = f"Green Slides: {mapping[item_count > 0]}"

        item_count: int = received_items.get(PoolsItems.SLIDES_BLUE, 0)
        self.slides_blue_label.text = f"Blue Slides: {mapping[item_count > 0]}"

        item_count: int = received_items.get(PoolsItems.SLIDES_EXTRA, 0)
        self.slides_extra_label.text = f"Extra Slides: {mapping[item_count > 0]}"

        item_count: int = received_items.get(PoolsItems.DIVING_BOARDS, 0)
        self.diving_boards_label.text = f"Diving Boards: {mapping[item_count > 0]}"

        item_count: int = received_items.get(PoolsItems.CHAIRS_PLASTIC, 0)
        self.chairs_plastic_label.text = f"Plastic Chairs: {mapping[item_count > 0]}"

        item_count: int = received_items.get(PoolsItems.CHAIRS_SAUNA, 0)
        self.chairs_sauna_label.text = f"Sauna Benches: {mapping[item_count > 0]}"

        item_count: int = received_items.get(PoolsItems.CHAIRS_ARMCHAIR, 0)
        self.chairs_armchair_label.text = f"Armchairs: {mapping[item_count > 0]}"

        item_count: int = received_items.get(PoolsItems.CHAIRS_WOODEN, 0)
        self.chairs_wooden_label.text = f"Wooden Chairs: {mapping[item_count > 0]}"

        item_count: int = received_items.get(PoolsItems.CHAIRS_SUBWAY, 0)
        self.chairs_subway_label.text = f"Subway Chairs: {mapping[item_count > 0]}"

        item_count: int = received_items.get(PoolsItems.CHAIRS_PARK, 0)
        self.chairs_park_label.text = f"Park Benches: {mapping[item_count > 0]}"

        item_count: int = received_items.get(PoolsItems.CHAIRS_SOFA, 0)
        self.chairs_sofa_label.text = f"Sofas: {mapping[item_count > 0]}"


class PoolsLevelsLayout(BoxLayout):
    ctx: PoolsContext

    level_label: Label
    level_images: List[Image]

    level_data: Dict[PoolsLevels, Dict[str, Any]]

    def __init__(self, ctx: PoolsContext) -> None:
        super().__init__(orientation="vertical", size_hint_y=None, height="40dp", spacing="8dp")

        self.bind(minimum_height=self.setter("height"))

        self.ctx = ctx

        self.level_label = Label(
            text=f"[b]Levels[/b]",
            markup=True,
            font_size="32dp",
            size_hint_y=None,
            height="70dp",
            halign="left",
            valign="bottom",
        )

        self.level_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.add_widget(self.level_label)

        self.level_images = list()
        self.level_data = dict()

        offset: int = -2

        if self.ctx.game_controller.option_include_level_0:
            offset = -1

        levels: List[PoolsLevels] = list(PoolsLevels)[:offset]

        level: PoolsLevels
        for level in levels:
            self.level_data[level] = {
                "image_path": f"assets/{level_to_scene_internal_name[level]}.png",
                "unlock_item": getattr(PoolsItems, f"{level.name}_UNLOCK"),
            }

        grid_layout: GridLayout = GridLayout(
            cols=3,
            spacing=[16, 16],
            padding=0,
            size_hint_y=None,
        )

        grid_layout.bind(minimum_height=grid_layout.setter("height"))

        level: PoolsLevels
        data: Dict[str, Any]
        for level, data in self.level_data.items():
            image_bytes: bytes = pkgutil.get_data(client_gui.__name__, data["image_path"])
            image: CoreImage = CoreImage(io.BytesIO(image_bytes), ext="png")

            level_image = Image(
                texture=image.texture,
                size=(192, 128),
                size_hint=(None, None),
                allow_stretch=True,
                opacity=0.3
            )

            self.level_images.append(level_image)

            grid_layout.add_widget(level_image)

        self.add_widget(grid_layout)

    def update(self) -> None:
        received_items: Dict[PoolsItems, int] = dict()

        network_item: NetUtils.NetworkItem
        for network_item in self.ctx.items_received:
            if network_item.item in self.ctx.id_to_items:
                item: PoolsItems = self.ctx.id_to_items[network_item.item]

                if item not in received_items:
                    received_items[item] = 0

                received_items[item] += 1

        level: PoolsLevels
        data: Dict[str, Any]
        for i, (level, data) in enumerate(self.level_data.items()):
            is_unlocked: bool = False

            if data["unlock_item"] in received_items and received_items[data["unlock_item"]] > 0:
                is_unlocked = True

            self.level_images[i].opacity = 1.0 if is_unlocked else 0.3


class PoolsContent(ScrollView):
    ctx: PoolsContext

    layout: BoxLayout

    layout_game_information: PoolsGameInformationLayout
    layout_levels: PoolsLevelsLayout

    timer: Clock

    def __init__(self, ctx: PoolsContext) -> None:
        super().__init__()

        self.ctx = ctx

        self.layout = BoxLayout(orientation="vertical", size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter("height"))

        self.layout_game_information = PoolsGameInformationLayout(ctx=self.ctx)
        self.layout.add_widget(self.layout_game_information)

        self.layout_levels = PoolsLevelsLayout(ctx=self.ctx)
        self.layout.add_widget(self.layout_levels)

        self.add_widget(self.layout)

        self.timer = Clock.schedule_interval(self.update, 1.0 / 10.0)

    def update(self, *_) -> None:
        try:
            self.layout_game_information.update()
            self.layout_levels.update()
        except Exception:
            import traceback

            with open("pools_errors.log", "a") as f:
                f.write(traceback.format_exc() + "\n\n")


class PoolsTabLayout(BoxLayout):
    ctx: PoolsContext

    layout_content: BoxLayout
    layout_content_pools: PoolsContent

    layout_not_connected: NotConnectedLayout

    def __init__(self, ctx: PoolsContext) -> None:
        super().__init__(orientation="vertical", padding="8dp")

        self.bind(minimum_height=self.setter('height'))

        self.ctx = ctx

        self.layout_not_connected = NotConnectedLayout(self.ctx)
        self.add_widget(self.layout_not_connected)

        self.layout_content = BoxLayout(orientation="horizontal", spacing="16dp", padding=["8dp", "0dp"])
        self.add_widget(self.layout_content)

        self.update()

    def update(self) -> None:
        if self.ctx.game_controller.selected_starting_level is None:
            self.layout_not_connected.show()

            if hasattr(self, "layout_content_pools"):
                self.layout_content_pools.timer.cancel()

            self.layout_content.clear_widgets()

            return

        self.layout_not_connected.hide()

        if not len(self.layout_content.children):
            self.layout_content_pools = PoolsContent(ctx=self.ctx)
            self.layout_content.add_widget(self.layout_content_pools)

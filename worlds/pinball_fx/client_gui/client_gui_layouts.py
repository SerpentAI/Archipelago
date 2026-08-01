from typing import Any, Dict, List, Optional

import io
import pkgutil

import NetUtils

from kivy.clock import Clock
from kivy.core.image import Image as CoreImage

from kivy.graphics import Color, Line, Rectangle

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

from ..client import PinballFXContext

from ..data.game_data import table_to_table_internal_name

from ..enums import (
    PinballFXAPGoals,
    PinballFXTables,
    PinballFXGameModes,
)

from ..game_state_manager import GameStateManager, GameState

from .. import client_gui


class NotConnectedLayout(BoxLayout):
    ctx: PinballFXContext

    def __init__(self, ctx: PinballFXContext) -> None:
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


class PinballFXTableInformationLayout(BoxLayout):
    ctx: PinballFXContext

    game_state_manager: GameStateManager

    information_label: Label

    shiny_quarters_label: Label
    goal_label: Label

    table_information_image: Image
    table_information_title: Label
    table_information_subtitle: Label

    target_score_low_label: Label
    target_score_mid_label: Label
    target_score_high_label: Label
    target_score_very_high_label: Label

    item_score_multiplier_label: Label
    item_target_score_discount_label: Label

    score_label: Label

    last_seen_table: Optional[PinballFXTables]

    def __init__(self, ctx: PinballFXContext) -> None:
        super().__init__(orientation="vertical", size_hint_y=None, height="200dp", spacing="8dp",)

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
            height="64dp",
            spacing="8dp",
        )

        goal_header_layout.bind(minimum_height=goal_header_layout.setter("height"))

        # Shiny Quarters
        self.shiny_quarters_label: Label = Label(
            text=(
                f"[b]Shiny Quarters[/b]\n"
                f"Retrieved [color=00FA9A]0[/color] of "
                f"[color=00FA9A]{self.ctx.game_controller.option_shiny_quarters_required}[/color] needed "
                f"([color=888888]{self.ctx.game_controller.option_shiny_quarters_total} total[/color])"
            ),
            markup=True,
            size_hint_x=33,
            size_hint_y=None,
            height="60dp",
            halign="left",
            valign="middle",
        )

        self.shiny_quarters_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        goal_header_layout.add_widget(self.shiny_quarters_label)

        # Goal
        self.goal_label: Label = Label(
            text=(
                f"[b]Goal[/b]\n"
                f"Retrieve the Shiny Quarters!"
            ),
            markup=True,
            size_hint_x=67,
            size_hint_y=None,
            height="60dp",
            halign="left",
            valign="middle",
        )

        self.goal_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        goal_header_layout.add_widget(self.goal_label)

        self.add_widget(goal_header_layout)

        # Table Information
        table_information_layout: BoxLayout = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height="140dp",
            spacing="8dp",
        )

        table_information_layout.bind(minimum_height=table_information_layout.setter("height"))

        self.table_information_image = Image(
            size=(155, 155),
            size_hint=(None, None),
            allow_stretch=True,
            opacity=0.1
        )

        table_information_layout.add_widget(self.table_information_image)

        table_information_text_layout: BoxLayout = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            height="140dp",
            spacing="5dp",
        )

        table_information_text_layout.bind(minimum_height=table_information_text_layout.setter("height"))

        self.table_information_title = Label(
            text=f"[b]Begin Playing a Pinball Table...[/b]",
            markup=True,
            size_hint_y=None,
            font_size="18dp",
            height="22dp",
            halign="left",
            valign="middle",
        )

        self.table_information_title.bind(size=lambda label, size: setattr(label, "text_size", size))

        table_information_text_layout.add_widget(self.table_information_title)

        self.table_information_subtitle = Label(
            text=f"[b]This table is not included this seed.[/b]",
            markup=True,
            size_hint_y=None,
            font_size="12dp",
            height="24dp",
            halign="left",
            valign="middle",
            padding=[0, 0, 0, 10]
        )

        self.table_information_subtitle.bind(size=lambda label, size: setattr(label, "text_size", size))

        table_information_text_layout.add_widget(self.table_information_subtitle)

        table_information_text_sublayout: BoxLayout = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height="78dp",
            spacing="8dp",
        )

        table_information_text_sublayout.bind(minimum_height=table_information_text_sublayout.setter("height"))

        table_information_targets_layout: BoxLayout = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            height="78dp",
            spacing="4dp",
            size_hint_x=70,
        )

        table_information_targets_layout.bind(minimum_height=table_information_targets_layout.setter("height"))

        targets_label: Label = Label(
            text="[b]Target Scores[/b]",
            markup=True,
            size_hint_y=None,
            font_size="16dp",
            height="20dp",
            halign="left",
            valign="middle",
        )

        targets_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        table_information_targets_layout.add_widget(targets_label)

        self.target_score_low_label = Label(
            text="Low: [color=00FA9A]X,XXX,XXX[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.target_score_low_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        table_information_targets_layout.add_widget(self.target_score_low_label)

        self.target_score_mid_label = Label(
            text="Mid: [color=00FA9A]X,XXX,XXX[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.target_score_mid_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        table_information_targets_layout.add_widget(self.target_score_mid_label)

        self.target_score_high_label = Label(
            text="High: [color=00FA9A]X,XXX,XXX[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.target_score_high_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        table_information_targets_layout.add_widget(self.target_score_high_label)

        self.target_score_very_high_label = Label(
            text="Very High: [color=00FA9A]X,XXX,XXX[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.target_score_very_high_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        if self.ctx.game_controller.option_include_very_high_tier_scores:
            table_information_targets_layout.add_widget(self.target_score_very_high_label)

        table_information_items_layout: BoxLayout = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            height="78dp",
            spacing="8dp",
            size_hint_x=30,
        )

        table_information_items_layout.bind(minimum_height=table_information_items_layout.setter("height"))

        items_label: Label = Label(
            text="[b]Useful Items[/b]",
            markup=True,
            size_hint_y=None,
            font_size="12dp",
            height="14dp",
            halign="left",
            valign="middle",
        )

        items_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        table_information_items_layout.add_widget(items_label)

        self.item_score_multiplier_label = Label(
            text="Score Multiplier: [color=00FA9A]Xx[/color]",
            markup=True,
            size_hint_y=None,
            font_size="12dp",
            height="14dp",
            halign="left",
            valign="middle",
        )

        self.item_score_multiplier_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        table_information_items_layout.add_widget(self.item_score_multiplier_label)

        self.item_target_score_discount_label = Label(
            text="Target Score Discount: [color=00FA9A]Xx[/color]",
            markup=True,
            size_hint_y=None,
            font_size="12dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.item_target_score_discount_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        table_information_items_layout.add_widget(self.item_target_score_discount_label)

        table_information_text_sublayout.add_widget(table_information_targets_layout)
        table_information_text_sublayout.add_widget(table_information_items_layout)
        table_information_text_layout.add_widget(table_information_text_sublayout)
        table_information_layout.add_widget(table_information_text_layout)

        self.add_widget(table_information_layout)

        self.score_label = Label(
            text="[b]Score:[/b] 0  [color=888888]0[/color]",
            markup=True,
            size_hint_y=None,
            font_size="22dp",
            height="28dp",
            halign="left",
            valign="middle",
        )

        self.score_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.add_widget(self.score_label)

        self.last_seen_table = None

    def update(self) -> None:
        ## Received Items
        received_items: Dict[str, int] = dict()

        network_item: NetUtils.NetworkItem
        for network_item in self.ctx.items_received:
            if network_item.item in self.ctx.id_to_items:
                item_name: str = self.ctx.id_to_items[network_item.item]

                if item_name not in received_items:
                    received_items[item_name] = 0

                received_items[item_name] += 1

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

        # Shiny Quarters
        shiny_quarters_obtained: int = received_items.get("Shiny Quarter", 0)

        self.shiny_quarters_label.text = (
            f"[b]Shiny Quarters[/b]\n"
            f"Retrieved [color=00FA9A]{shiny_quarters_obtained}[/color] of "
            f"[color=00FA9A]{self.ctx.game_controller.option_shiny_quarters_required}[/color] needed "
            f"([color=888888]{self.ctx.game_controller.option_shiny_quarters_total} total[/color])"
        )

        # Goal
        if self.ctx.game_controller.option_goal == PinballFXAPGoals.SHINY_QUARTERS_FINAL_TABLE:
            self.goal_label.text = (
                "[b]Goal[/b]\n"
                f"Retrieve the Shiny Quarters, then meet the High score on the goal table!"
            )
        elif self.ctx.game_controller.option_goal == PinballFXAPGoals.SHINY_QUARTERS_HUNT:
            self.goal_label.text = (
                "[b]Goal[/b]\n"
                "Retrieve the Shiny Quarters!"
            )

        # Table
        if game_state is None or not game_state.is_valid or not game_state.is_on_table:
            self.table_information_image.texture = None
            self.table_information_image.opacity = 0.1

            self.table_information_title.text = f"[b]Begin Playing a Pinball Table...[/b]"
            self.table_information_subtitle.text = f"[b]This table is not included this seed.[/b]"

            self.target_score_low_label.text = "Low: [color=888888]X,XXX,XXX[/color]"
            self.target_score_mid_label.text = "Mid: [color=888888]X,XXX,XXX[/color]"
            self.target_score_high_label.text = "High: [color=888888]X,XXX,XXX[/color]"
            self.target_score_very_high_label.text = "Very High: [color=888888]X,XXX,XXX[/color]"

            self.item_score_multiplier_label.text = "Score Multiplier: [color=888888]Xx[/color]"
            self.item_target_score_discount_label.text = "Target Score Discount: [color=888888]Xx[/color]"

            self.score_label.text = "[b]Score:[/b] 0  [color=888888]0[/color]"

            self.last_seen_table = None
        else:
            if self.last_seen_table != game_state.table:
                image_path: str = f"assets/{table_to_table_internal_name[game_state.table]}.png"
                image_bytes: bytes = pkgutil.get_data(client_gui.__name__, image_path)

                image: CoreImage = CoreImage(io.BytesIO(image_bytes), ext="png")

                self.table_information_image.texture = image.texture
                self.table_information_image.opacity = 1.0

                self.last_seen_table = game_state.table

            if game_state.game_mode is None:
                self.table_information_title.text = f"[b]{game_state.table.value}: Unsupported Game Mode[/b]"
            else:
                self.table_information_title.text = f"[b]{game_state.table.value}: {game_state.game_mode.value}[/b]"

            is_table_in_seed: bool = False
            is_table_goal: bool = False
            is_table_game_mode_unlocked: bool = False

            if game_state.table in (self.ctx.game_controller.selected_tables + [self.ctx.game_controller.selected_goal_table]):
                is_table_in_seed = True

            if game_state.table == self.ctx.game_controller.selected_goal_table:
                is_table_goal = True

            if game_state.game_mode is not None:
                table_game_mode_unlock_item_name: str = f"{game_state.game_mode.value} Unlock: {game_state.table.value}"
                table_game_mode_unlock_item_count: int = received_items.get(table_game_mode_unlock_item_name, 0)

                if table_game_mode_unlock_item_count > 0:
                    if is_table_goal:
                        if shiny_quarters_obtained >= self.ctx.game_controller.option_shiny_quarters_required:
                            is_table_game_mode_unlocked = True
                    else:
                        is_table_game_mode_unlocked = True

            mapping: Dict[bool, str] = {
                False: "[color=FF4C4C]-[/color]",
                True: "[color=00FA9A]+[/color]"
            }

            self.table_information_subtitle.text = f"In Seed? {mapping[is_table_in_seed]}    Unlocked? {mapping[is_table_game_mode_unlocked]}"

            if is_table_in_seed and is_table_game_mode_unlocked:
                score_multiplier_item_name: str = f"{game_state.table.value} - {game_state.game_mode.value}: Score Multiplier"
                score_multiplier_item_count: int = received_items.get(score_multiplier_item_name, 0)

                target_score_discount_item_name: str = f"{game_state.table.value} - {game_state.game_mode.value}: Target Score Discount"
                target_score_discount_item_count: int = received_items.get(target_score_discount_item_name, 0)

                target_score_ratio: float = self.ctx.game_controller.target_score_ratios[game_state.table]

                if is_table_goal:
                    self.target_score_low_label.text = "Low: [color=888888]X,XXX,XXX[/color]"
                    self.target_score_mid_label.text = "Mid: [color=888888]X,XXX,XXX[/color]"

                    target_score: int = self.ctx.game_controller.target_scores[game_state.table][game_state.game_mode][2]
                    adjusted_target_score: int = int(target_score * (1.0 - (0.05 * target_score_discount_item_count)))

                    self.target_score_high_label.text = f"High: [color=00FA9A]{adjusted_target_score:,}[/color]  [color=888888][size=11]{round(target_score_ratio, 2)}x Base + Items[/size][/color]"

                    self.target_score_very_high_label.text = "Very High: [color=888888]X,XXX,XXX[/color]"
                else:
                    target_score: int = self.ctx.game_controller.target_scores[game_state.table][game_state.game_mode][0]
                    adjusted_target_score: int = int(target_score * (1.0 - (0.05 * target_score_discount_item_count)))

                    self.target_score_low_label.text = f"Low: [color=00FA9A]{adjusted_target_score:,}[/color]  [color=888888][size=11]{round(target_score_ratio, 2)}x Base + Items[/size][/color]"

                    target_score: int = self.ctx.game_controller.target_scores[game_state.table][game_state.game_mode][1]
                    adjusted_target_score: int = int(target_score * (1.0 - (0.05 * target_score_discount_item_count)))

                    self.target_score_mid_label.text = f"Mid: [color=00FA9A]{adjusted_target_score:,}[/color]  [color=888888][size=11]{round(target_score_ratio, 2)}x Base + Items[/size][/color]"

                    target_score: int = self.ctx.game_controller.target_scores[game_state.table][game_state.game_mode][2]
                    adjusted_target_score: int = int(target_score * (1.0 - (0.05 * target_score_discount_item_count)))

                    self.target_score_high_label.text = f"High: [color=00FA9A]{adjusted_target_score:,}[/color]  [color=888888][size=11]{round(target_score_ratio, 2)}x Base + Items[/size][/color]"

                    target_score: int = self.ctx.game_controller.target_scores[game_state.table][game_state.game_mode][3]
                    adjusted_target_score: int = int(target_score * (1.0 - (0.05 * target_score_discount_item_count)))

                    self.target_score_very_high_label.text = f"Very High: [color=00FA9A]{adjusted_target_score:,}[/color]  [color=888888][size=11]{round(target_score_ratio, 2)}x Base + Items[/size][/color]"

                self.item_score_multiplier_label.text = f"Score Multiplier: [color=00FA9A]{score_multiplier_item_count}x[/color]"
                self.item_target_score_discount_label.text = f"Target Score Discount: [color=00FA9A]{target_score_discount_item_count}x[/color]"

                adjusted_score: int = int(game_state.score * (1.0 + (0.05 * score_multiplier_item_count)))

                self.score_label.text = f"[b]Score:[/b] {adjusted_score:,}  [color=888888]{game_state.score:,}[/color]"
            else:
                self.target_score_low_label.text = "Low: [color=888888]X,XXX,XXX[/color]"
                self.target_score_mid_label.text = "Mid: [color=888888]X,XXX,XXX[/color]"
                self.target_score_high_label.text = "High: [color=888888]X,XXX,XXX[/color]"
                self.target_score_very_high_label.text = "Very High: [color=888888]X,XXX,XXX[/color]"

                self.item_score_multiplier_label.text = "Score Multiplier: [color=888888]Xx[/color]"
                self.item_target_score_discount_label.text = "Target Score Discount: [color=888888]Xx[/color]"

                self.score_label.text = "[b]Score:[/b] 0  [color=888888]0[/color]"


class PinballFXTablesLayout(BoxLayout):
    ctx: PinballFXContext

    table_label: Label
    table_images: List[Image]
    table_game_mode_labels: Dict[PinballFXTables, List[Label]]

    table_data: Dict[PinballFXTables, Dict[str, Any]]

    def __init__(self, ctx: PinballFXContext) -> None:
        super().__init__(orientation="vertical", size_hint_y=None, height="40dp", spacing="8dp")

        self.bind(minimum_height=self.setter("height"))

        self.ctx = ctx

        self.table_label = Label(
            text=f"[b]Pinball Tables[/b]",
            markup=True,
            font_size="32dp",
            size_hint_y=None,
            height="70dp",
            halign="left",
            valign="bottom",
        )

        self.table_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.add_widget(self.table_label)

        self.table_images = list()
        self.table_game_mode_labels = dict()

        self.table_data = dict()

        table: PinballFXTables
        for table in self.ctx.game_controller.selected_tables + [self.ctx.game_controller.selected_goal_table]:
            if table is None:
                continue

            self.table_data[table] = {
                "image_path": f"assets/{table_to_table_internal_name[table]}.png",
                "is_goal": False,
            }

            if self.ctx.game_controller.selected_goal_table is not None:
                if table == self.ctx.game_controller.selected_goal_table:
                    self.table_data[table]["is_goal"] = True

        grid_layout: GridLayout = GridLayout(
            cols=3,
            spacing=16,
            padding=0,
            size_hint_y=None,
        )

        grid_layout.bind(minimum_height=grid_layout.setter("height"))

        table: PinballFXTables
        data: Dict[str, Any]
        for table, data in self.table_data.items():
            table_layout: BoxLayout = BoxLayout(orientation="horizontal", size_hint_y=None, height="96dp", spacing="8dp")
            table_layout.bind(minimum_height=table_layout.setter("height"))

            image_bytes: bytes = pkgutil.get_data(client_gui.__name__, data["image_path"])
            image: CoreImage = CoreImage(io.BytesIO(image_bytes), ext="png")

            table_image = Image(
                texture=image.texture,
                size=(96, 96),
                size_hint=(None, None),
                allow_stretch=True,
                opacity=0.3
            )

            if data["is_goal"]:
                with table_image.canvas.after:
                    fill_color = Color(1, 0.85, 0.2, 0.15)
                    fill_rect = Rectangle(pos=table_image.pos, size=table_image.size)

                    line_color = Color(1, 0.85, 0.2, 1.0)
                    border = Line(rectangle=(*table_image.pos, *table_image.size), width=2)

                def _update_goal_decoration(*_) -> None:
                    fill_rect.pos = table_image.pos
                    fill_rect.size = table_image.size
                    border.rectangle = (*table_image.pos, *table_image.size)

                table_image.bind(pos=_update_goal_decoration, size=_update_goal_decoration)

            self.table_images.append(table_image)

            table_layout.add_widget(table_image)

            table_game_mode_labels_layout: BoxLayout = BoxLayout(orientation="vertical", size_hint_y=None, height="96dp", spacing="4dp")

            self.table_game_mode_labels[table] = list()

            game_mode: PinballFXGameModes
            for game_mode in PinballFXGameModes:
                if data["is_goal"] and game_mode != PinballFXGameModes.CLASSIC:
                    continue

                game_mode_label: Label = Label(
                    text=f"{game_mode.value}",
                    font_size="14dp",
                    size_hint_y=None,
                    height="16dp",
                    halign="left",
                    valign="bottom",
                    opacity=0.05,
                )

                game_mode_label.bind(size=lambda label, size: setattr(label, "text_size", size))

                self.table_game_mode_labels[table].append(game_mode_label)

                table_game_mode_labels_layout.add_widget(game_mode_label)

            table_layout.add_widget(table_game_mode_labels_layout)

            grid_layout.add_widget(table_layout)

        self.add_widget(grid_layout)

    def update(self) -> None:
        received_items: Dict[str, int] = dict()

        network_item: NetUtils.NetworkItem
        for network_item in self.ctx.items_received:
            if network_item.item in self.ctx.id_to_items:
                item_name: str = self.ctx.id_to_items[network_item.item]

                if item_name not in received_items:
                    received_items[item_name] = 0

                received_items[item_name] += 1

        table: PinballFXTables
        data: Dict[str, Any]
        for i, (table, data) in enumerate(self.table_data.items()):
            classic_unlock_item_name: str = f"Classic Mode Unlock: {table.value}"
            classic_unlock_item_count: int = received_items.get(classic_unlock_item_name, 0)

            one_ball_unlock_item_name: str = f"1 Ball Challenge Unlock: {table.value}"
            one_ball_unlock_item_count: int = received_items.get(one_ball_unlock_item_name, 0)

            flips_unlock_item_name: str = f"Flips Challenge Unlock: {table.value}"
            flips_unlock_item_count: int = received_items.get(flips_unlock_item_name, 0)

            time_unlock_item_name: str = f"Time Challenge Unlock: {table.value}"
            time_unlock_item_count: int = received_items.get(time_unlock_item_name, 0)

            distance_unlock_item_name: str = f"Distance Challenge Unlock: {table.value}"
            distance_unlock_item_count: int = received_items.get(distance_unlock_item_name, 0)

            has_at_least_one_game_mode: bool = sum([
                classic_unlock_item_count,
                one_ball_unlock_item_count,
                flips_unlock_item_count,
                time_unlock_item_count,
                distance_unlock_item_count,
            ]) > 0

            if data["is_goal"]:
                if classic_unlock_item_count > 0:
                    self.table_game_mode_labels[table][0].opacity = 1.0

                    shiny_quarter_item_count: int = received_items.get("Shiny Quarter", 0)

                    if shiny_quarter_item_count >= self.ctx.game_controller.option_shiny_quarters_required:
                        self.table_images[i].opacity = 1.0
                    else:
                        self.table_images[i].opacity = 0.3
                else:
                    self.table_images[i].opacity = 0.3
                    self.table_game_mode_labels[table][0].opacity = 0.05
            else:
                if has_at_least_one_game_mode:
                    self.table_images[i].opacity = 1.0

                    self.table_game_mode_labels[table][0].opacity = 1.0 if classic_unlock_item_count > 0 else 0.3

                    if one_ball_unlock_item_count > 0:
                        self.table_game_mode_labels[table][1].opacity = 1.0
                    else:
                        if self.ctx.game_controller.option_include_one_ball_challenges:
                            self.table_game_mode_labels[table][1].opacity = 0.3
                        else:
                            self.table_game_mode_labels[table][1].opacity = 0.05

                    if flips_unlock_item_count > 0:
                        self.table_game_mode_labels[table][2].opacity = 1.0
                    else:
                        if self.ctx.game_controller.option_include_flips_challenges:
                            self.table_game_mode_labels[table][2].opacity = 0.3
                        else:
                            self.table_game_mode_labels[table][2].opacity = 0.05

                    self.table_game_mode_labels[table][3].opacity = 1.0 if time_unlock_item_count > 0 else 0.3

                    if distance_unlock_item_count > 0:
                        self.table_game_mode_labels[table][4].opacity = 1.0
                    else:
                        if self.ctx.game_controller.option_include_distance_challenges:
                            self.table_game_mode_labels[table][4].opacity = 0.3
                        else:
                            self.table_game_mode_labels[table][4].opacity = 0.05
                else:
                    self.table_images[i].opacity = 0.3

                    self.table_game_mode_labels[table][0].opacity = 0.05
                    self.table_game_mode_labels[table][1].opacity = 0.05
                    self.table_game_mode_labels[table][2].opacity = 0.05
                    self.table_game_mode_labels[table][3].opacity = 0.05
                    self.table_game_mode_labels[table][4].opacity = 0.05


class PinballFXContent(ScrollView):
    ctx: PinballFXContext

    layout: BoxLayout

    layout_table_information: PinballFXTableInformationLayout
    layout_tables: PinballFXTablesLayout

    timer: Clock

    def __init__(self, ctx: PinballFXContext) -> None:
        super().__init__()

        self.ctx = ctx

        self.layout = BoxLayout(orientation="vertical", size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter("height"))

        self.layout_table_information = PinballFXTableInformationLayout(ctx=self.ctx)
        self.layout.add_widget(self.layout_table_information)

        self.layout_tables = PinballFXTablesLayout(ctx=self.ctx)
        self.layout.add_widget(self.layout_tables)

        self.add_widget(self.layout)

        self.timer = Clock.schedule_interval(self.update, 1.0 / 10.0)

    def update(self, *_) -> None:
        try:
            self.layout_table_information.update()
            self.layout_tables.update()
        except Exception:
            import traceback

            with open("pinball_fx_errors.log", "a") as f:
                f.write(traceback.format_exc() + "\n\n")


class PinballFXTabLayout(BoxLayout):
    ctx: PinballFXContext

    layout_content: BoxLayout
    layout_content_pinball_fx: PinballFXContent

    layout_not_connected: NotConnectedLayout

    def __init__(self, ctx: PinballFXContext) -> None:
        super().__init__(orientation="vertical", padding="8dp")

        self.bind(minimum_height=self.setter('height'))

        self.ctx = ctx

        self.layout_not_connected = NotConnectedLayout(self.ctx)
        self.add_widget(self.layout_not_connected)

        self.layout_content = BoxLayout(orientation="horizontal", spacing="16dp", padding=["8dp", "0dp"])
        self.add_widget(self.layout_content)

        self.update()

    def update(self) -> None:
        if self.ctx.game_controller.target_scores is None:
            self.layout_not_connected.show()

            if hasattr(self, "layout_content_pinball_fx"):
                self.layout_content_pinball_fx.timer.cancel()

            self.layout_content.clear_widgets()

            return

        self.layout_not_connected.hide()

        if not len(self.layout_content.children):
            self.layout_content_pinball_fx = PinballFXContent(ctx=self.ctx)
            self.layout_content.add_widget(self.layout_content_pinball_fx)

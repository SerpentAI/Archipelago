from typing import Any, Dict, List, Optional

import io
import pkgutil

import NetUtils

from kivy.clock import Clock
from kivy.core.image import Image as CoreImage

from kivy.graphics import Color, Line, Rectangle

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView

from ..client import TonyHawksProSkater12Context

from ..data.game_data import (
    gap_to_descriptions,
    skater_to_specials,
)

from ..enums import (
    TonyHawksProSkater12APGoals,
    TonyHawksProSkater12Contexts,
    TonyHawksProSkater12Gaps,
    TonyHawksProSkater12Levels,
    TonyHawksProSkater12Skaters,
)

from ..game_state_manager import GameStateManager, GameState

from .. import client_gui


class ExplainButton(Button):
    popup: Popup

    def __init__(self, popup: Popup = None, **kwargs) -> None:
        super().__init__(**kwargs)
        self.popup = popup

    def on_press(self):
        self.popup.open()


class NotConnectedLayout(BoxLayout):
    ctx: TonyHawksProSkater12Context

    def __init__(self, ctx: TonyHawksProSkater12Context) -> None:
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


class TonyHawksProSkater12GameInformationLayout(BoxLayout):
    ctx: TonyHawksProSkater12Context

    game_state_manager: GameStateManager

    information_label: Label

    secret_tapes_label: Label
    goal_label: Label

    level_information_level_image: Image

    level_information_title: Label
    level_information_subtitle: Label

    target_score_high_label: Label
    target_score_pro_label: Label
    target_score_sick_label: Label
    target_score_platinum_label: Label

    target_combo_score_high_label: Label
    target_combo_score_pro_label: Label
    target_combo_score_sick_label: Label
    target_combo_score_platinum_label: Label

    long_trick_grind_label: Label
    long_trick_lip_label: Label
    long_trick_manual_label: Label

    gap_1_label: Label
    gap_2_label: Label
    gap_3_label: Label
    gap_4_label: Label
    gap_5_label: Label

    gap_1_popup: Popup
    gap_2_popup: Popup
    gap_3_popup: Popup
    gap_4_popup: Popup
    gap_5_popup: Popup

    skater_information_skater_image: Image
    skater_name_label: Label

    stats_label: Label
    special_meter_label: Label

    flip_tricks_label: Label
    grab_tricks_label: Label
    grind_tricks_label: Label
    lip_tricks_label: Label

    manual_tricks_label: Label
    spin_tricks_label: Label
    transfers_label: Label
    wallplants_label: Label

    extra_tricks_label: Label
    stance_switching_label: Label
    double_score_label: Label

    signature_special_1_label: Label
    signature_special_2_label: Label
    signature_special_3_label: Label

    current_score_label: Label
    current_combo_score_label: Label

    current_long_grind_label: Label
    current_long_lip_label: Label
    current_long_manual_label: Label

    last_seen_level: Optional[TonyHawksProSkater12Levels]
    last_seen_skater: Optional[TonyHawksProSkater12Skaters]

    def __init__(self, ctx: TonyHawksProSkater12Context) -> None:
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
            height="64dp",
            spacing="8dp",
        )

        goal_header_layout.bind(minimum_height=goal_header_layout.setter("height"))

        # Secret Tapes
        self.secret_tapes_label: Label = Label(
            text=(
                f"[b]Secret Tapes[/b]\n"
                f"Retrieved [color=00FA9A]0[/color] of "
                f"[color=00FA9A]{self.ctx.game_controller.option_secret_tapes_required}[/color] needed "
                f"([color=888888]{self.ctx.game_controller.option_secret_tapes_total} total[/color])"
            ),
            markup=True,
            size_hint_x=40,
            size_hint_y=None,
            height="60dp",
            halign="left",
            valign="middle",
        )

        self.secret_tapes_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        goal_header_layout.add_widget(self.secret_tapes_label)

        # Goal
        self.goal_label: Label = Label(
            text=(
                f"[b]Goal[/b]\n"
                f"Retrieve the Secret Tapes!"
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

        # Level Information
        level_information_header_layout: BoxLayout = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height="52dp",
            spacing="8dp",
        )

        self.level_information_level_image = Image(
            size=(204, 52),
            size_hint=(None, None),
            allow_stretch=True,
            opacity=0.1
        )

        level_information_header_layout.add_widget(self.level_information_level_image)

        level_information_subheader_layout: BoxLayout = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            height="52dp",
            spacing="8dp",
        )

        self.level_information_title = Label(
            text=f"[b]Begin Playing a Ranked & Free Skate Level...[/b]",
            markup=True,
            size_hint_y=None,
            font_size="18dp",
            height="28dp",
            halign="left",
            valign="middle",
        )

        self.level_information_title.bind(size=lambda label, size: setattr(label, "text_size", size))

        level_information_subheader_layout.add_widget(self.level_information_title)

        self.level_information_subtitle = Label(
            text=f"[b]This level is not included in this seed.[/b]",
            markup=True,
            size_hint_y=None,
            font_size="12dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.level_information_subtitle.bind(size=lambda label, size: setattr(label, "text_size", size))

        level_information_subheader_layout.add_widget(self.level_information_subtitle)

        level_information_header_layout.add_widget(level_information_subheader_layout)

        self.add_widget(level_information_header_layout)

        level_information_layout: BoxLayout = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height="140dp",
            spacing="8dp",
            padding=[0, 20, 0, 0]
        )

        level_information_layout.bind(minimum_height=level_information_layout.setter("height"))

        target_scores_layout: BoxLayout = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            height="140dp",
            spacing="5dp",
            size_hint_x=20,
        )

        target_scores_layout.bind(minimum_height=target_scores_layout.setter("height"))

        target_scores_label: Label = Label(
            text="[b]Scores[/b]",
            markup=True,
            size_hint_y=None,
            font_size="16dp",
            height="20dp",
            halign="left",
            valign="middle",
        )

        target_scores_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        target_scores_layout.add_widget(target_scores_label)

        self.target_score_high_label = Label(
            text="High: [color=00FA9A]XXX,XXX[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.target_score_high_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.target_score_pro_label = Label(
            text="Pro: [color=00FA9A]XXX,XXX[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.target_score_pro_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.target_score_sick_label = Label(
            text="Sick: [color=00FA9A]XXX,XXX[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.target_score_sick_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        target_scores_layout.add_widget(self.target_score_high_label)
        target_scores_layout.add_widget(self.target_score_pro_label)
        target_scores_layout.add_widget(self.target_score_sick_label)

        self.target_score_platinum_label = Label(
            text="Platinum: [color=00FA9A]XXX,XXX[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.target_score_platinum_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        if self.ctx.game_controller.option_include_platinum_scores:
            target_scores_layout.add_widget(self.target_score_platinum_label)

        level_information_layout.add_widget(target_scores_layout)

        target_combo_scores_layout: BoxLayout = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            height="140dp",
            spacing="5dp",
            size_hint_x=20,
        )

        target_combo_scores_layout.bind(minimum_height=target_combo_scores_layout.setter("height"))

        target_combo_scores_label: Label = Label(
            text="[b]Combo Scores[/b]",
            markup=True,
            size_hint_y=None,
            font_size="16dp",
            height="20dp",
            halign="left",
            valign="middle",
        )

        target_combo_scores_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        target_combo_scores_layout.add_widget(target_combo_scores_label)

        self.target_combo_score_high_label = Label(
            text="High: [color=00FA9A]XXX,XXX[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.target_combo_score_high_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.target_combo_score_pro_label = Label(
            text="Pro: [color=00FA9A]XXX,XXX[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.target_combo_score_pro_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.target_combo_score_sick_label = Label(
            text="Sick: [color=00FA9A]XXX,XXX[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.target_combo_score_sick_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        target_combo_scores_layout.add_widget(self.target_combo_score_high_label)
        target_combo_scores_layout.add_widget(self.target_combo_score_pro_label)
        target_combo_scores_layout.add_widget(self.target_combo_score_sick_label)

        self.target_combo_score_platinum_label = Label(
            text="Platinum: [color=00FA9A]XXX,XXX[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.target_combo_score_platinum_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        if self.ctx.game_controller.option_include_platinum_combo_scores:
            target_combo_scores_layout.add_widget(self.target_combo_score_platinum_label)

        level_information_layout.add_widget(target_combo_scores_layout)

        target_long_tricks_layout: BoxLayout = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            height="140dp",
            spacing="5dp",
            size_hint_x=20,
        )

        target_long_tricks_layout.bind(minimum_height=target_long_tricks_layout.setter("height"))

        target_long_tricks_label: Label = Label(
            text="[b]Long Tricks[/b]",
            markup=True,
            size_hint_y=None,
            font_size="16dp",
            height="20dp",
            halign="left",
            valign="middle",
        )

        target_long_tricks_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        target_long_tricks_layout.add_widget(target_long_tricks_label)

        self.long_trick_grind_label = Label(
            text="Grind: [color=00FA9A]X.X seconds[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.long_trick_grind_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.long_trick_lip_label = Label(
            text="Lip: [color=00FA9A]X.X seconds[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.long_trick_lip_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.long_trick_manual_label = Label(
            text="Manual: [color=00FA9A]X.X seconds[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.long_trick_manual_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        target_long_tricks_layout.add_widget(self.long_trick_grind_label)
        target_long_tricks_layout.add_widget(self.long_trick_lip_label)
        target_long_tricks_layout.add_widget(self.long_trick_manual_label)

        if self.ctx.game_controller.option_include_long_tricks:
            level_information_layout.add_widget(target_long_tricks_layout)

        self.add_widget(level_information_layout)

        target_gaps_layout: BoxLayout = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            height="140dp",
            spacing="5dp",
            size_hint_x=40,
        )

        target_gaps_layout.bind(minimum_height=target_gaps_layout.setter("height"))

        target_gaps_label: Label = Label(
            text="[b]Gaps[/b]",
            markup=True,
            size_hint_y=None,
            font_size="16dp",
            height="20dp",
            halign="left",
            valign="middle",
        )

        target_gaps_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        target_gaps_layout.add_widget(target_gaps_label)

        gap_1_row_layout: BoxLayout = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height="16dp",
            spacing="8dp",
        )

        gap_1_row_layout.bind(minimum_height=gap_1_row_layout.setter("height"))

        self.gap_1_popup = Popup(
            title="How do I land GAP?",
            content=Label(text="Lorem Ipsum Dolor"),
            size_hint=(0.9, 0.2),
        )

        gap_1_button: ExplainButton = ExplainButton(
            text="?",
            width="16dp",
            size_hint_x=None,
            popup=self.gap_1_popup,
        )

        gap_1_row_layout.add_widget(gap_1_button)

        self.gap_1_label = Label(
            text="#1: [color=00FA9A]Lorem Ipsum Dolor[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.gap_1_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        gap_1_row_layout.add_widget(self.gap_1_label)

        gap_2_row_layout: BoxLayout = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height="16dp",
            spacing="8dp",
        )

        gap_2_row_layout.bind(minimum_height=gap_2_row_layout.setter("height"))

        self.gap_2_popup = Popup(
            title="How do I land GAP?",
            content=Label(text="Lorem Ipsum Dolor"),
            size_hint=(0.9, 0.2),
        )

        gap_2_button: ExplainButton = ExplainButton(
            text="?",
            width="16dp",
            size_hint_x=None,
            popup=self.gap_2_popup,
        )

        gap_2_row_layout.add_widget(gap_2_button)

        self.gap_2_label = Label(
            text="#2: [color=00FA9A]Lorem Ipsum Dolor[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.gap_2_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        gap_2_row_layout.add_widget(self.gap_2_label)

        gap_3_row_layout: BoxLayout = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height="16dp",
            spacing="8dp",
        )

        gap_3_row_layout.bind(minimum_height=gap_3_row_layout.setter("height"))

        self.gap_3_popup = Popup(
            title="How do I land GAP?",
            content=Label(text="Lorem Ipsum Dolor"),
            size_hint=(0.9, 0.2),
        )

        gap_3_button: ExplainButton = ExplainButton(
            text="?",
            width="16dp",
            size_hint_x=None,
            popup=self.gap_3_popup,
        )

        gap_3_row_layout.add_widget(gap_3_button)

        self.gap_3_label = Label(
            text="#3: [color=00FA9A]Lorem Ipsum Dolor[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.gap_3_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        gap_3_row_layout.add_widget(self.gap_3_label)

        gap_4_row_layout: BoxLayout = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height="16dp",
            spacing="8dp",
        )

        gap_4_row_layout.bind(minimum_height=gap_4_row_layout.setter("height"))

        self.gap_4_popup = Popup(
            title="How do I land GAP?",
            content=Label(text="Lorem Ipsum Dolor"),
            size_hint=(0.9, 0.2),
        )

        gap_4_button: ExplainButton = ExplainButton(
            text="?",
            width="16dp",
            size_hint_x=None,
            popup=self.gap_4_popup,
        )

        gap_4_row_layout.add_widget(gap_4_button)

        self.gap_4_label = Label(
            text="#4: [color=00FA9A]Lorem Ipsum Dolor[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.gap_4_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        gap_4_row_layout.add_widget(self.gap_4_label)

        gap_5_row_layout: BoxLayout = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height="16dp",
            spacing="8dp",
        )

        gap_5_row_layout.bind(minimum_height=gap_5_row_layout.setter("height"))

        self.gap_5_popup = Popup(
            title="How do I land GAP?",
            content=Label(text="Lorem Ipsum Dolor"),
            size_hint=(0.9, 0.2),
        )

        gap_5_button: ExplainButton = ExplainButton(
            text="?",
            width="16dp",
            size_hint_x=None,
            popup=self.gap_4_popup,
        )

        gap_5_row_layout.add_widget(gap_5_button)

        self.gap_5_label = Label(
            text="#5: [color=00FA9A]Lorem Ipsum Dolor[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.gap_5_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        gap_5_row_layout.add_widget(self.gap_5_label)

        target_gaps_layout.add_widget(gap_1_row_layout)

        if self.ctx.game_controller.option_gap_count_per_level > 1:
            target_gaps_layout.add_widget(gap_2_row_layout)

        if self.ctx.game_controller.option_gap_count_per_level > 2:
            target_gaps_layout.add_widget(gap_3_row_layout)

        if self.ctx.game_controller.option_gap_count_per_level > 3:
            target_gaps_layout.add_widget(gap_4_row_layout)

        if self.ctx.game_controller.option_gap_count_per_level > 4:
            target_gaps_layout.add_widget(gap_5_row_layout)

        if self.ctx.game_controller.option_include_gaps:
            level_information_layout.add_widget(target_gaps_layout)

        skater_information_layout: BoxLayout = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height="110dp",
            spacing="8dp",
            padding=[0, 20, 0, 0]
        )

        skater_information_layout.bind(minimum_height=skater_information_layout.setter("height"))

        self.skater_information_skater_image = Image(
            size=(97, 110),
            size_hint=(None, None),
            allow_stretch=True,
            opacity=0.1
        )

        skater_information_layout.add_widget(self.skater_information_skater_image)

        skater_information_sublayout: BoxLayout = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height="110dp",
            spacing="8dp",
            size_hint_x=90,
        )

        skater_information_sublayout.bind(minimum_height=skater_information_sublayout.setter("height"))

        skater_information_column_1_layout: BoxLayout = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            height="110dp",
            spacing="5dp",
        )

        skater_information_column_1_layout.bind(minimum_height=skater_information_column_1_layout.setter("height"))

        self.skater_name_label = Label(
            text="[b]Skater Name[/b]",
            markup=True,
            size_hint_y=None,
            font_size="18dp",
            height="42dp",
            halign="left",
            valign="middle",
            padding=[0, 0, 0, 20],
        )

        self.skater_name_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        skater_information_column_1_layout.add_widget(self.skater_name_label)

        self.stats_label = Label(
            text="[b]Stats:[/b] [color=00FA9A]+[/color] [color=FF4C4C]-[/color] [color=FF4C4C]-[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="18dp",
            halign="left",
            valign="middle",
        )

        self.stats_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        skater_information_column_1_layout.add_widget(self.stats_label)

        self.special_meter_label = Label(
            text="[b]Special Meter:[/b] [color=00FA9A]+[/color] [color=FF4C4C]-[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="18dp",
            halign="left",
            valign="middle",
        )

        self.special_meter_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        skater_information_column_1_layout.add_widget(self.special_meter_label)

        skater_information_sublayout.add_widget(skater_information_column_1_layout)

        skater_information_column_2_layout: BoxLayout = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            height="110dp",
            spacing="5dp",
        )

        skater_information_column_2_layout.bind(minimum_height=skater_information_column_2_layout.setter("height"))

        self.flip_tricks_label = Label(
            text="[b]Flip Tricks:[/b] [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="18dp",
            halign="left",
            valign="middle",
        )

        self.flip_tricks_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        skater_information_column_2_layout.add_widget(self.flip_tricks_label)

        self.grab_tricks_label = Label(
            text="[b]Grab Tricks:[/b] [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="18dp",
            halign="left",
            valign="middle",
        )

        self.grab_tricks_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        skater_information_column_2_layout.add_widget(self.grab_tricks_label)

        self.grind_tricks_label = Label(
            text="[b]Grind Tricks:[/b] [color=00FA9A]+[/color] [color=FF4C4C]-[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="18dp",
            halign="left",
            valign="middle",
        )

        self.grind_tricks_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        skater_information_column_2_layout.add_widget(self.grind_tricks_label)

        self.lip_tricks_label = Label(
            text="[b]Lip Tricks:[/b] [color=00FA9A]+[/color] [color=FF4C4C]-[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="18dp",
            halign="left",
            valign="middle",
        )

        self.lip_tricks_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        skater_information_column_2_layout.add_widget(self.lip_tricks_label)

        skater_information_sublayout.add_widget(skater_information_column_2_layout)

        skater_information_column_3_layout: BoxLayout = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            height="110dp",
            spacing="5dp",
        )

        skater_information_column_3_layout.bind(minimum_height=skater_information_column_3_layout.setter("height"))

        self.manual_tricks_label = Label(
            text="[b]Manual Tricks:[/b] [color=00FA9A]+[/color] [color=FF4C4C]-[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="18dp",
            halign="left",
            valign="middle",
        )

        self.manual_tricks_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        skater_information_column_3_layout.add_widget(self.manual_tricks_label)

        self.spin_tricks_label = Label(
            text="[b]Spin Tricks:[/b] [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="18dp",
            halign="left",
            valign="middle",
        )

        self.spin_tricks_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        skater_information_column_3_layout.add_widget(self.spin_tricks_label)

        self.transfers_label = Label(
            text="[b]Transfers:[/b] [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="18dp",
            halign="left",
            valign="middle",
        )

        self.transfers_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        skater_information_column_3_layout.add_widget(self.transfers_label)

        self.wallplants_label = Label(
            text="[b]Wallplants:[/b] [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="18dp",
            halign="left",
            valign="middle",
        )

        self.wallplants_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        skater_information_column_3_layout.add_widget(self.wallplants_label)

        skater_information_sublayout.add_widget(skater_information_column_3_layout)

        skater_information_column_4_layout: BoxLayout = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            height="110dp",
            spacing="5dp",
        )

        skater_information_column_4_layout.bind(minimum_height=skater_information_column_4_layout.setter("height"))

        self.extra_tricks_label = Label(
            text="[b]Extra Tricks:[/b] [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="18dp",
            halign="left",
            valign="middle",
        )

        self.extra_tricks_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        skater_information_column_4_layout.add_widget(self.extra_tricks_label)

        self.stance_switching_label = Label(
            text="[b]Stance Switching:[/b] [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="18dp",
            halign="left",
            valign="middle",
        )

        self.stance_switching_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        skater_information_column_4_layout.add_widget(self.stance_switching_label)

        self.double_score_label = Label(
            text="[b]Double Score:[/b] [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="18dp",
            halign="left",
            valign="middle",
        )

        self.double_score_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        skater_information_column_4_layout.add_widget(self.double_score_label)

        skater_information_sublayout.add_widget(skater_information_column_4_layout)

        skater_information_layout.add_widget(skater_information_sublayout)

        self.add_widget(skater_information_layout)

        signature_specials_layout: BoxLayout = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height="20dp",
            spacing="8dp",
            padding=[0, 6, 0, 0]
        )

        signature_specials_layout.bind(minimum_height=signature_specials_layout.setter("height"))

        signature_specials_label: Label = Label(
            text="[b]Signature Specials:[/b]",
            markup=True,
            size_hint_y=None,
            font_size="16dp",
            height="20dp",
            halign="left",
            valign="middle",
        )

        signature_specials_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        signature_specials_layout.add_widget(signature_specials_label)

        self.signature_special_1_label: Label = Label(
            text="[color=888888]Signature Special 1[/color]",
            markup=True,
            size_hint_y=None,
            font_size="16dp",
            height="20dp",
            halign="left",
            valign="middle",
        )

        self.signature_special_1_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        signature_specials_layout.add_widget(self.signature_special_1_label)

        self.signature_special_2_label: Label = Label(
            text="[color=888888]Signature Special 2[/color]",
            markup=True,
            size_hint_y=None,
            font_size="16dp",
            height="20dp",
            halign="left",
            valign="middle",
        )

        self.signature_special_2_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        signature_specials_layout.add_widget(self.signature_special_2_label)

        self.signature_special_3_label: Label = Label(
            text="[color=888888]Signature Special 3[/color]",
            markup=True,
            size_hint_y=None,
            font_size="16dp",
            height="20dp",
            halign="left",
            valign="middle",
        )

        self.signature_special_3_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        signature_specials_layout.add_widget(self.signature_special_3_label)

        if self.ctx.game_controller.option_include_signature_specials:
            self.add_widget(signature_specials_layout)

        current_scores_layout: BoxLayout = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height="20dp",
            spacing="8dp",
            padding=[0, 20, 0, 0]
        )

        current_scores_layout.bind(minimum_height=current_scores_layout.setter("height"))

        self.current_score_label: Label = Label(
            text="[b]Score:[/b] XXX,XXX",
            markup=True,
            size_hint_x=33,
            size_hint_y=None,
            font_size="16dp",
            height="20dp",
            halign="left",
            valign="middle",
        )

        self.current_score_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        current_scores_layout.add_widget(self.current_score_label)

        self.current_combo_score_label: Label = Label(
            text="[b]Best Combo Score:[/b] XX,XXX",
            markup=True,
            size_hint_x=67,
            size_hint_y=None,
            font_size="16dp",
            height="20dp",
            halign="left",
            valign="middle",
        )

        self.current_combo_score_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        current_scores_layout.add_widget(self.current_combo_score_label)

        self.add_widget(current_scores_layout)

        current_long_tricks_layout: BoxLayout = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height="20dp",
            spacing="8dp",
            padding=[0, 8, 0, 0]
        )

        current_long_tricks_layout.bind(minimum_height=current_long_tricks_layout.setter("height"))

        self.current_long_grind_label: Label = Label(
            text="[b]Longest Grind:[/b] X.X seconds",
            markup=True,
            size_hint_x=33,
            size_hint_y=None,
            font_size="16dp",
            height="20dp",
            halign="left",
            valign="middle",
        )

        self.current_long_grind_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        current_long_tricks_layout.add_widget(self.current_long_grind_label)

        self.current_long_lip_label: Label = Label(
            text="[b]Longest Lip:[/b] X.X seconds",
            markup=True,
            size_hint_x=33,
            size_hint_y=None,
            font_size="16dp",
            height="20dp",
            halign="left",
            valign="middle",
        )

        self.current_long_lip_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        current_long_tricks_layout.add_widget(self.current_long_lip_label)

        self.current_long_manual_label: Label = Label(
            text="[b]Longest Manual:[/b] X.X seconds",
            markup=True,
            size_hint_x=33,
            size_hint_y=None,
            font_size="16dp",
            height="20dp",
            halign="left",
            valign="middle",
        )

        self.current_long_manual_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        current_long_tricks_layout.add_widget(self.current_long_manual_label)

        self.add_widget(current_long_tricks_layout)

        self.last_seen_level = None
        self.last_seen_skater = None

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

        # Secret Tapes
        secret_tapes_obtained: int = received_items.get("Secret Tape", 0)

        self.secret_tapes_label.text = (
            "[b]Secret Tapes[/b]\n"
            f"Retrieved [color=00FA9A]{secret_tapes_obtained}[/color] of "
            f"[color=00FA9A]{self.ctx.game_controller.option_secret_tapes_required}[/color] needed "
            f"([color=888888]{self.ctx.game_controller.option_secret_tapes_total} total[/color])"
        )

        # Goal
        if self.ctx.game_controller.option_goal == TonyHawksProSkater12APGoals.SECRET_TAPES_FINAL_LEVEL:
            self.goal_label.text = (
                "[b]Goal[/b]\n"
                f"Retrieve the Secret Tapes, then score 1M points on {self.ctx.game_controller.selected_goal_level.value}!"
            )
        elif self.ctx.game_controller.option_goal == TonyHawksProSkater12APGoals.SECRET_TAPE_HUNT:
            self.goal_label.text = (
                "[b]Goal[/b]\n"
                "Retrieve the Secret Tapes!"
            )

        # Level
        if game_state is None or game_state.context != TonyHawksProSkater12Contexts.LEVEL or game_state.level is None:
            self.level_information_level_image.texture = None
            self.level_information_level_image.opacity = 0.1

            self.level_information_title.text = "[b]Begin Playing a Ranked & Free Skate Level...[/b]"
            self.level_information_subtitle.text = "[b]This level is not included in this seed.[/b]"

            self.target_score_high_label.text = "High: [color=888888]XXX,XXX[/color]"
            self.target_score_pro_label.text = "Pro: [color=888888]XXX,XXX[/color]"
            self.target_score_sick_label.text = "Sick: [color=888888]XXX,XXX[/color]"
            self.target_score_platinum_label.text = "Platinum: [color=888888]XXX,XXX[/color]"

            self.target_combo_score_high_label.text = "High: [color=888888]XXX,XXX[/color]"
            self.target_combo_score_pro_label.text = "Pro: [color=888888]XXX,XXX[/color]"
            self.target_combo_score_sick_label.text = "Sick: [color=888888]XXX,XXX[/color]"
            self.target_combo_score_platinum_label.text = "Platinum: [color=888888]XXX,XXX[/color]"

            self.long_trick_grind_label.text = "Grind: [color=888888]X.X seconds[/color]"
            self.long_trick_lip_label.text = "Lip: [color=888888]X.X seconds[/color]"
            self.long_trick_manual_label.text = "Manual: [color=888888]X.X seconds[/color]"

            self.gap_1_label.text = "#1: [color=888888]Gap Name[/color]"
            self.gap_2_label.text = "#2: [color=888888]Gap Name[/color]"
            self.gap_3_label.text = "#3: [color=888888]Gap Name[/color]"
            self.gap_4_label.text = "#4: [color=888888]Gap Name[/color]"
            self.gap_5_label.text = "#5: [color=888888]Gap Name[/color]"

            self.gap_1_popup.title = "How do I land Gap Name?"
            self.gap_2_popup.title = "How do I land Gap Name?"
            self.gap_3_popup.title = "How do I land Gap Name?"
            self.gap_4_popup.title = "How do I land Gap Name?"
            self.gap_5_popup.title = "How do I land Gap Name?"

            self.gap_1_popup.content.text = "Gap Description"
            self.gap_2_popup.content.text = "Gap Description"
            self.gap_3_popup.content.text = "Gap Description"
            self.gap_4_popup.content.text = "Gap Description"
            self.gap_5_popup.content.text = "Gap Description"

            self.skater_information_skater_image.texture = None
            self.skater_information_skater_image.opacity = 0.1

            self.skater_name_label.text = "Skater Name"

            if self.ctx.game_controller.option_include_overpowered_abilities:
                self.stats_label.text = "[b]Stats:[/b] [color=888888]-[/color] [color=888888]-[/color] [color=888888]-[/color]"
            else:
                self.stats_label.text = "[b]Stats:[/b] [color=888888]-[/color] [color=888888]-[/color]"

            self.special_meter_label.text = "[b]Special Meter:[/b] [color=888888]-[/color] [color=888888]-[/color]"

            self.flip_tricks_label.text = "[b]Flip Tricks:[/b] [color=888888]-[/color]"
            self.grab_tricks_label.text = "[b]Grab Tricks:[/b] [color=888888]-[/color]"

            if self.ctx.game_controller.option_include_overpowered_abilities:
                self.grind_tricks_label.text = "[b]Grind Tricks:[/b] [color=888888]-[/color] [color=888888]-[/color]"
            else:
                self.grind_tricks_label.text = "[b]Grind Tricks:[/b] [color=888888]-[/color]"

            if self.ctx.game_controller.option_include_overpowered_abilities:
                self.lip_tricks_label.text = "[b]Lip Tricks:[/b] [color=888888]-[/color] [color=888888]-[/color]"
            else:
                self.lip_tricks_label.text = "[b]Lip Tricks:[/b] [color=888888]-[/color]"

            if self.ctx.game_controller.option_include_overpowered_abilities:
                self.manual_tricks_label.text = "[b]Manual Tricks:[/b] [color=888888]-[/color] [color=888888]-[/color]"
            else:
                self.manual_tricks_label.text = "[b]Manual Tricks:[/b] [color=888888]-[/color]"

            self.spin_tricks_label.text = "[b]Spin Tricks:[/b] [color=888888]-[/color]"
            self.transfers_label.text = "[b]Transfers:[/b] [color=888888]-[/color]"
            self.wallplants_label.text = "[b]Wallplants:[/b] [color=888888]-[/color]"

            self.extra_tricks_label.text = "[b]Extra Tricks:[/b] [color=888888]-[/color]"
            self.stance_switching_label.text = "[b]Stance Switching:[/b] [color=888888]-[/color]"
            self.double_score_label.text = "[b]Double Score:[/b] [color=888888]-[/color]"

            self.signature_special_1_label.text = "[color=888888]Signature Special 1[/color]"
            self.signature_special_2_label.text = "[color=888888]Signature Special 2[/color]"
            self.signature_special_3_label.text = "[color=888888]Signature Special 3[/color]"

            self.current_score_label.text = "[b]Score:[/b] [color=888888]XXX,XXX[/color]"
            self.current_combo_score_label.text = "[b]Best Combo Score:[/b] [color=888888]XX,XXX[/color]"

            self.current_long_grind_label.text = "[b]Longest Grind:[/b] [color=888888]X.X seconds[/color]"
            self.current_long_lip_label.text = "[b]Longest Lip:[/b] [color=888888]X.X seconds[/color]"
            self.current_long_manual_label.text = "[b]Longest Manual:[/b] [color=888888]X.X seconds[/color]"

            self.last_seen_level = None
            self.last_seen_skater = None

            return

        if self.last_seen_level != game_state.level:
            image_path: str = f"assets/{game_state.level.value}.png"
            image_bytes: bytes = pkgutil.get_data(client_gui.__name__, image_path)

            image: CoreImage = CoreImage(io.BytesIO(image_bytes), ext="png")

            self.level_information_level_image.texture = image.texture
            self.level_information_level_image.opacity = 1.0

            self.last_seen_level = game_state.level

        self.level_information_title.text = game_state.level.value

        level_unlock_item: str = f"Level Unlock: {game_state.level.value}"
        skater_unlock_item: str = f"Skater Unlock: {game_state.skater.value}"

        is_level_in_seed: bool = False
        is_level_goal: bool = False
        is_level_unlocked: bool = False

        is_skater_unlocked: bool = False

        if game_state.level in (self.ctx.game_controller.selected_levels + [self.ctx.game_controller.selected_goal_level]):
            is_level_in_seed = True

        if game_state.level == self.ctx.game_controller.selected_goal_level:
            is_level_goal = True

        if level_unlock_item in received_items and received_items[level_unlock_item] > 0:
            if is_level_goal:
                if secret_tapes_obtained >= self.ctx.game_controller.option_secret_tapes_required:
                    is_level_unlocked = True
            else:
                is_level_unlocked = True

        if skater_unlock_item in received_items and received_items[skater_unlock_item] > 0:
            is_skater_unlocked = True

        if is_level_in_seed:
            if is_level_unlocked:
                if is_skater_unlocked:
                    self.level_information_subtitle.text = f"[b]This level is included in this seed, is unlocked and the skater is available to play.[/b]"
                else:
                    self.level_information_subtitle.text = f"[b]This level is included in this seed, is unlocked, but the skater is not available to play[/b]"
            else:
                self.level_information_subtitle.text = f"[b]This level is included in this seed but has not been unlocked yet.[/b]"

            if not is_level_goal and game_state.skater in self.ctx.game_controller.selected_skaters:
                target_score_high: int = self.ctx.game_controller.target_scores[game_state.level][game_state.skater][0]
                target_score_pro: int = self.ctx.game_controller.target_scores[game_state.level][game_state.skater][1]
                target_score_sick: int = self.ctx.game_controller.target_scores[game_state.level][game_state.skater][2]

                self.target_score_high_label.text = f"High: [color=00FA9A]{target_score_high:,}[/color]"
                self.target_score_pro_label.text = f"Pro: [color=00FA9A]{target_score_pro:,}[/color]"
                self.target_score_sick_label.text = f"Sick: [color=00FA9A]{target_score_sick:,}[/color]"

                if self.ctx.game_controller.option_include_platinum_scores:
                    target_score_platinum: int = self.ctx.game_controller.target_scores[game_state.level][game_state.skater][3]
                    self.target_score_platinum_label.text = f"Platinum: [color=00FA9A]{target_score_platinum:,}[/color]"

                target_combo_score_high: int = self.ctx.game_controller.target_combo_scores[game_state.level][game_state.skater][0]
                target_combo_score_pro: int = self.ctx.game_controller.target_combo_scores[game_state.level][game_state.skater][1]
                target_combo_score_sick: int = self.ctx.game_controller.target_combo_scores[game_state.level][game_state.skater][2]

                self.target_combo_score_high_label.text = f"High: [color=00FA9A]{target_combo_score_high:,}[/color]"
                self.target_combo_score_pro_label.text = f"Pro: [color=00FA9A]{target_combo_score_pro:,}[/color]"
                self.target_combo_score_sick_label.text = f"Sick: [color=00FA9A]{target_combo_score_sick:,}[/color]"

                if self.ctx.game_controller.option_include_platinum_combo_scores:
                    target_combo_score_platinum: int = self.ctx.game_controller.target_combo_scores[game_state.level][game_state.skater][3]
                    self.target_combo_score_platinum_label.text = f"Platinum: [color=00FA9A]{target_combo_score_platinum:,}[/color]"

                if self.ctx.game_controller.option_include_long_tricks:
                    long_grind_duration: float = round(self.ctx.game_controller.target_long_tricks[game_state.level][game_state.skater][0], 1)
                    long_lip_duration: float = round(self.ctx.game_controller.target_long_tricks[game_state.level][game_state.skater][1], 1)
                    long_manual_duration: float = round(self.ctx.game_controller.target_long_tricks[game_state.level][game_state.skater][2], 1)

                    self.long_trick_grind_label.text = f"Grind: [color=00FA9A]{long_grind_duration} seconds[/color]"
                    self.long_trick_lip_label.text = f"Lip: [color=00FA9A]{long_lip_duration} seconds[/color]"
                    self.long_trick_manual_label.text = f"Manual: [color=00FA9A]{long_manual_duration} seconds[/color]"

                if self.ctx.game_controller.option_include_gaps:
                    gap_count: int = len(self.ctx.game_controller.target_gaps[game_state.level][game_state.skater])

                    gap_1: TonyHawksProSkater12Gaps = self.ctx.game_controller.target_gaps[game_state.level][game_state.skater][0]
                    gap_1_name: str = gap_1.value.split(" (")[0]

                    self.gap_1_label.text = f"#1: [color=00FA9A]{gap_1_name}[/color]"
                    self.gap_1_popup.title = f"How do I land {gap_1_name}?"
                    self.gap_1_popup.content.text = gap_to_descriptions[gap_1].replace(", ", ",\n")

                    if gap_count > 1:
                        gap_2: TonyHawksProSkater12Gaps = self.ctx.game_controller.target_gaps[game_state.level][game_state.skater][1]
                        gap_2_name: str = gap_2.value.split(" (")[0]

                        self.gap_2_label.text = f"#2: [color=00FA9A]{gap_2_name}[/color]"
                        self.gap_2_popup.title = f"How do I land {gap_2_name}?"
                        self.gap_2_popup.content.text = gap_to_descriptions[gap_2].replace(", ", ",\n")

                    if gap_count > 2:
                        gap_3: TonyHawksProSkater12Gaps = self.ctx.game_controller.target_gaps[game_state.level][game_state.skater][2]
                        gap_3_name: str = gap_3.value.split(" (")[0]

                        self.gap_3_label.text = f"#3: [color=00FA9A]{gap_3_name}[/color]"
                        self.gap_3_popup.title = f"How do I land {gap_3_name}?"
                        self.gap_3_popup.content.text = gap_to_descriptions[gap_3].replace(", ", ",\n")

                    if gap_count > 3:
                        gap_4: TonyHawksProSkater12Gaps = self.ctx.game_controller.target_gaps[game_state.level][game_state.skater][3]
                        gap_4_name: str = gap_4.value.split(" (")[0]

                        self.gap_4_label.text = f"#3: [color=00FA9A]{gap_4_name}[/color]"
                        self.gap_4_popup.title = f"How do I land {gap_4_name}?"
                        self.gap_4_popup.content.text = gap_to_descriptions[gap_4].replace(", ", ",\n")

                    if gap_count > 4:
                        gap_5: TonyHawksProSkater12Gaps = self.ctx.game_controller.target_gaps[game_state.level][game_state.skater][4]
                        gap_5_name: str = gap_5.value.split(" (")[0]

                        self.gap_5_label.text = f"#3: [color=00FA9A]{gap_5_name}[/color]"
                        self.gap_5_popup.title = f"How do I land {gap_5_name}?"
                        self.gap_5_popup.content.text = gap_to_descriptions[gap_5].replace(", ", ",\n")
            else:
                self.target_score_high_label.text = "High: [color=888888]XXX,XXX[/color]"
                self.target_score_pro_label.text = "Pro: [color=888888]XXX,XXX[/color]"
                self.target_score_sick_label.text = "Sick: [color=888888]XXX,XXX[/color]"
                self.target_score_platinum_label.text = "Platinum: [color=888888]XXX,XXX[/color]"

                self.target_combo_score_high_label.text = "High: [color=888888]XXX,XXX[/color]"
                self.target_combo_score_pro_label.text = "Pro: [color=888888]XXX,XXX[/color]"
                self.target_combo_score_sick_label.text = "Sick: [color=888888]XXX,XXX[/color]"
                self.target_combo_score_platinum_label.text = "Platinum: [color=888888]XXX,XXX[/color]"

                self.long_trick_grind_label.text = "Grind: [color=888888]X.X seconds[/color]"
                self.long_trick_lip_label.text = "Lip: [color=888888]X.X seconds[/color]"
                self.long_trick_manual_label.text = "Manual: [color=888888]X.X seconds[/color]"

                self.gap_1_label.text = "#1: [color=888888]Gap Name[/color]"
                self.gap_2_label.text = "#2: [color=888888]Gap Name[/color]"
                self.gap_3_label.text = "#3: [color=888888]Gap Name[/color]"
                self.gap_4_label.text = "#4: [color=888888]Gap Name[/color]"
                self.gap_5_label.text = "#5: [color=888888]Gap Name[/color]"

                self.gap_1_popup.title = "How do I land Gap Name?"
                self.gap_2_popup.title = "How do I land Gap Name?"
                self.gap_3_popup.title = "How do I land Gap Name?"
                self.gap_4_popup.title = "How do I land Gap Name?"
                self.gap_5_popup.title = "How do I land Gap Name?"

                self.gap_1_popup.content.text = "Gap Description"
                self.gap_2_popup.content.text = "Gap Description"
                self.gap_3_popup.content.text = "Gap Description"
                self.gap_4_popup.content.text = "Gap Description"
                self.gap_5_popup.content.text = "Gap Description"
        else:
            self.level_information_subtitle.text = f"[b]This level is not included in this seed.[/b]"

            self.target_score_high_label.text = "High: [color=888888]XXX,XXX[/color]"
            self.target_score_pro_label.text = "Pro: [color=888888]XXX,XXX[/color]"
            self.target_score_sick_label.text = "Sick: [color=888888]XXX,XXX[/color]"
            self.target_score_platinum_label.text = "Platinum: [color=888888]XXX,XXX[/color]"

            self.target_combo_score_high_label.text = "High: [color=888888]XXX,XXX[/color]"
            self.target_combo_score_pro_label.text = "Pro: [color=888888]XXX,XXX[/color]"
            self.target_combo_score_sick_label.text = "Sick: [color=888888]XXX,XXX[/color]"
            self.target_combo_score_platinum_label.text = "Platinum: [color=888888]XXX,XXX[/color]"

            self.long_trick_grind_label.text = "Grind: [color=888888]X.X seconds[/color]"
            self.long_trick_lip_label.text = "Lip: [color=888888]X.X seconds[/color]"
            self.long_trick_manual_label.text = "Manual: [color=888888]X.X seconds[/color]"

            self.gap_1_label.text = "#1: [color=888888]Gap Name[/color]"
            self.gap_2_label.text = "#2: [color=888888]Gap Name[/color]"
            self.gap_3_label.text = "#3: [color=888888]Gap Name[/color]"
            self.gap_4_label.text = "#4: [color=888888]Gap Name[/color]"
            self.gap_5_label.text = "#5: [color=888888]Gap Name[/color]"

            self.gap_1_popup.title = "How do I land Gap Name?"
            self.gap_2_popup.title = "How do I land Gap Name?"
            self.gap_3_popup.title = "How do I land Gap Name?"
            self.gap_4_popup.title = "How do I land Gap Name?"
            self.gap_5_popup.title = "How do I land Gap Name?"

            self.gap_1_popup.content.text = "Gap Description"
            self.gap_2_popup.content.text = "Gap Description"
            self.gap_3_popup.content.text = "Gap Description"
            self.gap_4_popup.content.text = "Gap Description"
            self.gap_5_popup.content.text = "Gap Description"

        # Skater
        if game_state is None or game_state.context != TonyHawksProSkater12Contexts.LEVEL or game_state.skater is None:
            self.skater_information_skater_image.texture = None
            self.skater_information_skater_image.opacity = 0.1

            self.skater_name_label.text = "Skater Name"

            if self.ctx.game_controller.option_include_overpowered_abilities:
                self.stats_label.text = "[b]Stats:[/b] [color=888888]-[/color] [color=888888]-[/color] [color=888888]-[/color]"
            else:
                self.stats_label.text = "[b]Stats:[/b] [color=888888]-[/color] [color=888888]-[/color]"

            self.special_meter_label.text = "[b]Special Meter:[/b] [color=888888]-[/color] [color=888888]-[/color]"

            self.flip_tricks_label.text = "[b]Flip Tricks:[/b] [color=888888]-[/color]"
            self.grab_tricks_label.text = "[b]Grab Tricks:[/b] [color=888888]-[/color]"

            if self.ctx.game_controller.option_include_overpowered_abilities:
                self.grind_tricks_label.text = "[b]Grind Tricks:[/b] [color=888888]-[/color] [color=888888]-[/color]"
            else:
                self.grind_tricks_label.text = "[b]Grind Tricks:[/b] [color=888888]-[/color]"

            if self.ctx.game_controller.option_include_overpowered_abilities:
                self.lip_tricks_label.text = "[b]Lip Tricks:[/b] [color=888888]-[/color] [color=888888]-[/color]"
            else:
                self.lip_tricks_label.text = "[b]Lip Tricks:[/b] [color=888888]-[/color]"

            if self.ctx.game_controller.option_include_overpowered_abilities:
                self.manual_tricks_label.text = "[b]Manual Tricks:[/b] [color=888888]-[/color] [color=888888]-[/color]"
            else:
                self.manual_tricks_label.text = "[b]Manual Tricks:[/b] [color=888888]-[/color]"

            self.spin_tricks_label.text = "[b]Spin Tricks:[/b] [color=888888]-[/color]"
            self.transfers_label.text = "[b]Transfers:[/b] [color=888888]-[/color]"
            self.wallplants_label.text = "[b]Wallplants:[/b] [color=888888]-[/color]"

            self.extra_tricks_label.text = "[b]Extra Tricks:[/b] [color=888888]-[/color]"
            self.stance_switching_label.text = "[b]Stance Switching:[/b] [color=888888]-[/color]"
            self.double_score_label.text = "[b]Double Score:[/b] [color=888888]-[/color]"

            self.signature_special_1_label.text = "[color=888888]Signature Special 1[/color]"
            self.signature_special_2_label.text = "[color=888888]Signature Special 2[/color]"
            self.signature_special_3_label.text = "[color=888888]Signature Special 3[/color]"

            self.last_seen_skater = None

            return

        if self.last_seen_skater != game_state.skater:
            image_path: str = f"assets/{game_state.skater.value}.png"
            image_bytes: bytes = pkgutil.get_data(client_gui.__name__, image_path)

            image: CoreImage = CoreImage(io.BytesIO(image_bytes), ext="png")

            self.skater_information_skater_image.texture = image.texture
            self.skater_information_skater_image.opacity = 1.0

            self.last_seen_skater = game_state.skater

        self.skater_name_label.text = game_state.skater.value

        skater_unlock_item: str = f"Skater Unlock: {game_state.skater.value}"

        is_skater_unlocked: bool = False

        if skater_unlock_item in received_items and received_items[skater_unlock_item] > 0:
            is_skater_unlocked = True

        if is_skater_unlocked:
            unlocked_string: str = "[color=00FA9A]+[/color] "
            locked_string: str = "[color=FF4C4C]-[/color] "

            stats_item_name: str = f"Progressive Stats: {game_state.skater.value}"
            stats_item_count: int = received_items.get(stats_item_name, 0)

            stats_text: str = "[b]Stats:[/b] "

            stats_text += unlocked_string if stats_item_count > 0 else locked_string
            stats_text += unlocked_string if stats_item_count > 1 else locked_string

            if self.ctx.game_controller.option_include_overpowered_abilities:
                stats_text += unlocked_string if stats_item_count > 2 else locked_string

            self.stats_label.text = stats_text

            special_meter_item_name: str = f"Progressive Special Meter: {game_state.skater.value}"
            special_meter_item_count: int = received_items.get(special_meter_item_name, 0)

            special_meter_text: str = "[b]Special Meter:[/b] "

            special_meter_text += unlocked_string if special_meter_item_count > 0 else locked_string
            special_meter_text += unlocked_string if special_meter_item_count > 1 else locked_string

            self.special_meter_label.text = special_meter_text

            flip_tricks_item_name: str = f"Flip Tricks: {game_state.skater.value}"
            flip_tricks_item_count: int = received_items.get(flip_tricks_item_name, 0)

            self.flip_tricks_label.text = "[b]Flip Tricks:[/b] " + (unlocked_string if flip_tricks_item_count > 0 else locked_string)

            grab_tricks_item_name: str = f"Grab Tricks: {game_state.skater.value}"
            grab_tricks_item_count: int = received_items.get(grab_tricks_item_name, 0)

            self.grab_tricks_label.text = "[b]Grab Tricks:[/b] " + (unlocked_string if grab_tricks_item_count > 0 else locked_string)

            grind_tricks_item_name: str = f"Progressive Grind Tricks: {game_state.skater.value}"
            grind_tricks_item_count: int = received_items.get(grind_tricks_item_name, 0)

            grind_tricks_text: str = "[b]Grind Tricks:[/b] "

            grind_tricks_text += unlocked_string if grind_tricks_item_count > 0 else locked_string

            if self.ctx.game_controller.option_include_overpowered_abilities:
                grind_tricks_text += unlocked_string if grind_tricks_item_count > 1 else locked_string

            self.grind_tricks_label.text = grind_tricks_text

            lip_tricks_item_name: str = f"Progressive Lip Tricks: {game_state.skater.value}"
            lip_tricks_item_count: int = received_items.get(lip_tricks_item_name, 0)

            lip_tricks_text: str = "[b]Lip Tricks:[/b] "

            lip_tricks_text += unlocked_string if lip_tricks_item_count > 0 else locked_string

            if self.ctx.game_controller.option_include_overpowered_abilities:
                lip_tricks_text += unlocked_string if lip_tricks_item_count > 1 else locked_string

            self.lip_tricks_label.text = lip_tricks_text

            manual_tricks_item_name: str = f"Progressive Manual Tricks: {game_state.skater.value}"
            manual_tricks_item_count: int = received_items.get(manual_tricks_item_name, 0)

            manual_tricks_text: str = "[b]Manual Tricks:[/b] "

            manual_tricks_text += unlocked_string if manual_tricks_item_count > 0 else locked_string

            if self.ctx.game_controller.option_include_overpowered_abilities:
                manual_tricks_text += unlocked_string if manual_tricks_item_count > 1 else locked_string

            self.manual_tricks_label.text = manual_tricks_text

            spin_tricks_item_name: str = f"Spin Tricks: {game_state.skater.value}"
            spin_tricks_item_count: int = received_items.get(spin_tricks_item_name, 0)

            self.spin_tricks_label.text = "[b]Spin Tricks:[/b] " + (unlocked_string if spin_tricks_item_count > 0 else locked_string)

            transfers_item_name: str = f"Transfers: {game_state.skater.value}"
            transfers_item_count: int = received_items.get(transfers_item_name, 0)

            self.transfers_label.text = "[b]Transfers:[/b] " + (unlocked_string if transfers_item_count > 0 else locked_string)

            wallplants_item_name: str = f"Wallplants: {game_state.skater.value}"
            wallplants_item_count: int = received_items.get(wallplants_item_name, 0)

            self.wallplants_label.text = "[b]Wallplants:[/b] " + (unlocked_string if wallplants_item_count > 0 else locked_string)

            extra_tricks_item_name: str = f"Extra Tricks: {game_state.skater.value}"
            extra_tricks_item_count: int = received_items.get(extra_tricks_item_name, 0)

            self.extra_tricks_label.text = "[b]Extra Tricks:[/b] " + (unlocked_string if extra_tricks_item_count > 0 else locked_string)

            stance_switching_item_name: str = f"Stance Switching: {game_state.skater.value}"
            stance_switching_item_count: int = received_items.get(stance_switching_item_name, 0)

            self.stance_switching_label.text = "[b]Stance Switching:[/b] " + (unlocked_string if stance_switching_item_count > 0 else locked_string)

            double_score_item_name: str = f"Double Score: {game_state.skater.value}"
            double_score_item_count: int = received_items.get(double_score_item_name, 0)

            self.double_score_label.text = "[b]Double Score:[/b] " + (unlocked_string if double_score_item_count > 0 else locked_string)

            self.signature_special_1_label.text = f"[color=888888]{skater_to_specials[game_state.skater][0].value}[/color]"
            self.signature_special_2_label.text = f"[color=888888]{skater_to_specials[game_state.skater][1].value}[/color]"
            self.signature_special_3_label.text = f"[color=888888]{skater_to_specials[game_state.skater][2].value}[/color]"
        else:
            if self.ctx.game_controller.option_include_overpowered_abilities:
                self.stats_label.text = "[b]Stats:[/b] [color=888888]-[/color] [color=888888]-[/color] [color=888888]-[/color]"
            else:
                self.stats_label.text = "[b]Stats:[/b] [color=888888]-[/color] [color=888888]-[/color]"

            self.special_meter_label.text = "[b]Special Meter:[/b] [color=888888]-[/color] [color=888888]-[/color]"

            self.flip_tricks_label.text = "[b]Flip Tricks:[/b] [color=888888]-[/color]"
            self.grab_tricks_label.text = "[b]Grab Tricks:[/b] [color=888888]-[/color]"

            if self.ctx.game_controller.option_include_overpowered_abilities:
                self.grind_tricks_label.text = "[b]Grind Tricks:[/b] [color=888888]-[/color] [color=888888]-[/color]"
            else:
                self.grind_tricks_label.text = "[b]Grind Tricks:[/b] [color=888888]-[/color]"

            if self.ctx.game_controller.option_include_overpowered_abilities:
                self.lip_tricks_label.text = "[b]Lip Tricks:[/b] [color=888888]-[/color] [color=888888]-[/color]"
            else:
                self.lip_tricks_label.text = "[b]Lip Tricks:[/b] [color=888888]-[/color]"

            if self.ctx.game_controller.option_include_overpowered_abilities:
                self.manual_tricks_label.text = "[b]Manual Tricks:[/b] [color=888888]-[/color] [color=888888]-[/color]"
            else:
                self.manual_tricks_label.text = "[b]Manual Tricks:[/b] [color=888888]-[/color]"

            self.spin_tricks_label.text = "[b]Spin Tricks:[/b] [color=888888]-[/color]"
            self.transfers_label.text = "[b]Transfers:[/b] [color=888888]-[/color]"
            self.wallplants_label.text = "[b]Wallplants:[/b] [color=888888]-[/color]"

            self.extra_tricks_label.text = "[b]Extra Tricks:[/b] [color=888888]-[/color]"
            self.stance_switching_label.text = "[b]Stance Switching:[/b] [color=888888]-[/color]"
            self.double_score_label.text = "[b]Double Score:[/b] [color=888888]-[/color]"

            self.signature_special_1_label.text = "[color=888888]Signature Special 1[/color]"
            self.signature_special_2_label.text = "[color=888888]Signature Special 2[/color]"
            self.signature_special_3_label.text = "[color=888888]Signature Special 3[/color]"

        # Data
        if game_state is None or game_state.context != TonyHawksProSkater12Contexts.LEVEL or game_state.score is None:
            self.current_score_label.text = "[b]Score:[/b] [color=888888]XXX,XXX[/color]"
            self.current_combo_score_label.text = "[b]Best Combo Score:[/b] [color=888888]XX,XXX[/color]"

            self.current_long_grind_label.text = "[b]Longest Grind:[/b] [color=888888]X.X seconds[/color]"
            self.current_long_lip_label.text = "[b]Longest Lip:[/b] [color=888888]X.X seconds[/color]"
            self.current_long_manual_label.text = "[b]Longest Manual:[/b] [color=888888]X.X seconds[/color]"

            return

        self.current_score_label.text = f"[b]Score:[/b] {game_state.score:,}"
        self.current_combo_score_label.text = f"[b]Best Combo Score:[/b] {game_state.best_combo_score:,}"

        self.current_long_grind_label.text = f"[b]Longest Grind:[/b] {round(game_state.longest_grind, 1)} seconds"
        self.current_long_lip_label.text = f"[b]Longest Lip:[/b] {round(game_state.longest_lip, 1)} seconds"
        self.current_long_manual_label.text = f"[b]Longest Manual:[/b] {round(game_state.longest_manual, 1)} seconds"


class TonyHawksProSkater12SkatersLayout(BoxLayout):
    ctx: TonyHawksProSkater12Context

    skater_label: Label
    skater_images: List[Image]

    skater_data: Dict[TonyHawksProSkater12Skaters, Dict[str, Any]]

    def __init__(self, ctx: TonyHawksProSkater12Context) -> None:
        super().__init__(orientation="vertical", size_hint_y=None, height="40dp", spacing="8dp")

        self.bind(minimum_height=self.setter("height"))

        self.ctx = ctx

        self.skater_label = Label(
            text=f"[b]Skaters[/b]",
            markup=True,
            font_size="32dp",
            size_hint_y=None,
            height="70dp",
            halign="left",
            valign="bottom",
        )

        self.skater_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.add_widget(self.skater_label)

        self.skater_images = list()

        self.skater_data = dict()

        skater: TonyHawksProSkater12Skaters
        for skater in self.ctx.game_controller.selected_skaters:
            self.skater_data[skater] = {
                "image_path": f"assets/{skater.value}.png",
                "unlock_item": f"Skater Unlock: {skater.value}",
            }

        grid_layout: GridLayout = GridLayout(
            cols=8,
            spacing=8,
            padding=0,
            size_hint_y=None,
        )

        grid_layout.bind(minimum_height=grid_layout.setter("height"))

        skater: TonyHawksProSkater12Skaters
        data: Dict[str, Any]
        for skater, data in self.skater_data.items():
            image_bytes: bytes = pkgutil.get_data(client_gui.__name__, data["image_path"])
            image: CoreImage = CoreImage(io.BytesIO(image_bytes), ext="png")

            skater_image = Image(
                texture=image.texture,
                size=(87, 98),
                size_hint=(None, None),
                allow_stretch=True,
                opacity=0.4
            )

            self.skater_images.append(skater_image)
            grid_layout.add_widget(skater_image)

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

        skater: TonyHawksProSkater12Skaters
        data: Dict[str, Any]
        for i, (skater, data) in enumerate(self.skater_data.items()):
            is_unlocked: bool = False

            if data["unlock_item"] in received_items and received_items[data["unlock_item"]] > 0:
                is_unlocked = True

            self.skater_images[i].opacity = 1.0 if is_unlocked else 0.4


class TonyHawksProSkater12LevelsLayout(BoxLayout):
    ctx: TonyHawksProSkater12Context

    level_label: Label
    level_images: List[Image]

    level_data: Dict[TonyHawksProSkater12Levels, Dict[str, Any]]

    def __init__(self, ctx: TonyHawksProSkater12Context) -> None:
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

        levels: List[TonyHawksProSkater12Levels] = self.ctx.game_controller.selected_levels[:]

        if self.ctx.game_controller.selected_goal_level is not None:
            levels.append(self.ctx.game_controller.selected_goal_level)

        level: TonyHawksProSkater12Levels
        for level in levels:
            self.level_data[level] = {
                "image_path": f"assets/{level.value}.png",
                "unlock_item": f"Level Unlock: {level.value}",
                "is_goal": False,
            }

            if self.ctx.game_controller.selected_goal_level is not None:
                if level == self.ctx.game_controller.selected_goal_level:
                    self.level_data[level]["is_goal"] = True

        grid_layout: GridLayout = GridLayout(
            cols=3,
            spacing=8,
            padding=0,
            size_hint_y=None,
        )

        grid_layout.bind(minimum_height=grid_layout.setter("height"))

        level: TonyHawksProSkater12Levels
        data: Dict[str, Any]
        for level, data in self.level_data.items():
            image_bytes: bytes = pkgutil.get_data(client_gui.__name__, data["image_path"])
            image: CoreImage = CoreImage(io.BytesIO(image_bytes), ext="png")

            level_image = Image(
                texture=image.texture,
                size=(204, 52),
                size_hint=(None, None),
                allow_stretch=True,
                opacity=0.4
            )

            if data["is_goal"]:
                with level_image.canvas.after:
                    fill_color = Color(1, 0.85, 0.2, 0.15)
                    fill_rect = Rectangle(pos=level_image.pos, size=level_image.size)

                    line_color = Color(1, 0.85, 0.2, 1.0)
                    border = Line(rectangle=(*level_image.pos, *level_image.size), width=2)

                def _update_goal_decoration(*_) -> None:
                    fill_rect.pos = level_image.pos
                    fill_rect.size = level_image.size
                    border.rectangle = (*level_image.pos, *level_image.size)

                level_image.bind(pos=_update_goal_decoration, size=_update_goal_decoration)

            self.level_images.append(level_image)
            grid_layout.add_widget(level_image)

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

        level: TonyHawksProSkater12Levels
        data: Dict[str, Any]
        for i, (level, data) in enumerate(self.level_data.items()):
            is_unlocked: bool = False

            if data["unlock_item"] in received_items and received_items[data["unlock_item"]] > 0:
                if data["is_goal"]:
                    secret_tapes_required: int = self.ctx.game_controller.option_secret_tapes_required
                    secret_tapes_obtained: int = received_items.get("Secret Tape", 0)

                    if secret_tapes_obtained >= secret_tapes_required:
                        is_unlocked = True
                else:
                    is_unlocked = True

            self.level_images[i].opacity = 1.0 if is_unlocked else 0.4


class TonyHawksProSkater12Content(ScrollView):
    ctx: TonyHawksProSkater12Context

    layout: BoxLayout

    layout_game_information: TonyHawksProSkater12GameInformationLayout
    layout_skaters: TonyHawksProSkater12SkatersLayout
    layout_levels: TonyHawksProSkater12LevelsLayout

    timer: Clock

    def __init__(self, ctx: TonyHawksProSkater12Context) -> None:
        super().__init__()

        self.ctx = ctx

        self.layout = BoxLayout(orientation="vertical", size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter("height"))

        self.layout_game_information = TonyHawksProSkater12GameInformationLayout(ctx=self.ctx)
        self.layout.add_widget(self.layout_game_information)

        self.layout_skaters = TonyHawksProSkater12SkatersLayout(ctx=self.ctx)
        self.layout.add_widget(self.layout_skaters)

        self.layout_levels = TonyHawksProSkater12LevelsLayout(ctx=self.ctx)
        self.layout.add_widget(self.layout_levels)

        self.add_widget(self.layout)

        self.timer = Clock.schedule_interval(self.update, 1.0 / 10.0)

    def update(self, *_) -> None:
        try:
            self.layout_game_information.update()
            self.layout_skaters.update()
            self.layout_levels.update()
        except Exception:
            import traceback

            with open("tony_hawks_pro_skater_1_2_errors.log", "a") as f:
                f.write(traceback.format_exc() + "\n\n")


class TonyHawksProSkater12TabLayout(BoxLayout):
    ctx: TonyHawksProSkater12Context

    layout_content: BoxLayout
    layout_content_tony_hawks_pro_skater_1_2: TonyHawksProSkater12Content

    layout_not_connected: NotConnectedLayout

    def __init__(self, ctx: TonyHawksProSkater12Context) -> None:
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

            if hasattr(self, "layout_content_tony_hawks_pro_skater_1_2"):
                self.layout_content_tony_hawks_pro_skater_1_2.timer.cancel()

            self.layout_content.clear_widgets()

            return

        self.layout_not_connected.hide()

        if not len(self.layout_content.children):
            self.layout_content_tony_hawks_pro_skater_1_2 = TonyHawksProSkater12Content(ctx=self.ctx)
            self.layout_content.add_widget(self.layout_content_tony_hawks_pro_skater_1_2)

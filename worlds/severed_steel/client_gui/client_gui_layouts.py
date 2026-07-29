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

from ..client import SeveredSteelContext

from ..enums import (
    SeveredSteelAPGoals,
    SeveredSteelLevels,
    SeveredSteelMutators,
    SeveredSteelStylishActions,
)

from ..game_state_manager import GameStateManager, GameState

from .. import client_gui


class NotConnectedLayout(BoxLayout):
    ctx: SeveredSteelContext

    def __init__(self, ctx: SeveredSteelContext) -> None:
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


class SeveredSteelGameInformationLayout(BoxLayout):
    ctx: SeveredSteelContext

    game_state_manager: GameStateManager

    information_label: Label

    edensys_root_keys_label: Label
    goal_label: Label

    level_information_level_image: Image

    level_information_title: Label
    level_information_subtitle: Label

    target_time_label: Label

    target_rank_score_b_label: Label
    target_rank_score_a_label: Label
    target_rank_score_s_label: Label
    target_rank_score_s_plus_label: Label
    target_rank_score_s_plus_plus_label: Label

    stylish_action_challenge_1_label: Label
    stylish_action_challenge_2_label: Label
    stylish_action_challenge_3_label: Label
    stylish_action_challenge_4_label: Label
    stylish_action_challenge_5_label: Label

    useful_time_discount_label: Label
    useful_double_score_label: Label
    useful_unlimited_ammo_label: Label
    useful_unlimited_cannon_label: Label
    useful_invincibility_label: Label

    burn_rate_reduction_label: Label
    fresh_cooldown_reduction_label: Label

    license_dive_frag_label: Label
    license_wall_run_frag_label: Label
    license_flip_frag_label: Label
    license_kickslide_label: Label
    license_slide_frag_label: Label
    license_quick_shot_label: Label
    license_multikill_label: Label
    license_throw_hit_label: Label
    license_cannon_frag_label: Label
    license_drop_kick_label: Label
    license_wall_bang_label: Label
    license_stole_weapon_label: Label
    license_air_shot_label: Label
    license_kick_label: Label
    license_nice_throw_label: Label

    last_seen_level: Optional[SeveredSteelLevels]

    def __init__(self, ctx: SeveredSteelContext) -> None:
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

        # EdenSys Root Keys
        self.edensys_root_keys_label: Label = Label(
            text=(
                f"[b]EdenSys Root Keys[/b]\n"
                f"Retrieved [color=00FA9A]0[/color] of "
                f"[color=00FA9A]{self.ctx.game_controller.option_edensys_root_keys_required}[/color] needed "
                f"([color=888888]{self.ctx.game_controller.option_edensys_root_keys_total} total[/color])"
            ),
            markup=True,
            size_hint_x=40,
            size_hint_y=None,
            height="60dp",
            halign="left",
            valign="middle",
        )

        self.edensys_root_keys_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        goal_header_layout.add_widget(self.edensys_root_keys_label)

        # Goal
        self.goal_label: Label = Label(
            text=(
                f"[b]Goal[/b]\n"
                f"Retrieve the EdenSys Root Keys!"
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
            size=(269, 43),
            size_hint=(None, None),
            allow_stretch=True,
            opacity=0.1
        )

        level_information_header_layout.add_widget(self.level_information_level_image)

        level_information_subheader_layout: BoxLayout = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            height="43dp",
            spacing="8dp",
        )

        self.level_information_title = Label(
            text=f"[b]Begin Playing a Firefight 2.0 Level...[/b]",
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

        target_time_layout: BoxLayout = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            height="140dp",
            spacing="5dp",
            size_hint_x=20,
            padding=[0, 20, 0, 0]
        )

        target_time_layout.bind(minimum_height=target_time_layout.setter("height"))

        target_time_label: Label = Label(
            text="[b]Target Time[/b]",
            markup=True,
            size_hint_y=None,
            font_size="16dp",
            height="20dp",
            halign="left",
            valign="middle",
        )

        target_time_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        target_time_layout.add_widget(target_time_label)

        self.target_time_label = Label(
            text="[color=00FA9A]XX:XX[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.target_time_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        target_time_layout.add_widget(self.target_time_label)

        if self.ctx.game_controller.option_include_target_times:
            self.add_widget(target_time_layout)

        level_information_layout: BoxLayout = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height="140dp",
            spacing="8dp",
            padding=[0, 10, 0, 0]
        )

        level_information_layout.bind(minimum_height=level_information_layout.setter("height"))

        target_rank_scores_layout: BoxLayout = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            height="140dp",
            spacing="5dp",
            size_hint_x=1,
        )

        target_rank_scores_layout.bind(minimum_height=target_rank_scores_layout.setter("height"))

        target_rank_scores_label: Label = Label(
            text="[b]Rank Scores[/b]",
            markup=True,
            size_hint_y=None,
            font_size="16dp",
            height="20dp",
            halign="left",
            valign="middle",
        )

        target_rank_scores_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        target_rank_scores_layout.add_widget(target_rank_scores_label)

        self.target_rank_score_b_label = Label(
            text="B: [color=00FA9A]XX,XXX[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.target_rank_score_b_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.target_rank_score_a_label = Label(
            text="A: [color=00FA9A]XX,XXX[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.target_rank_score_a_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.target_rank_score_s_label = Label(
            text="S: [color=00FA9A]XX,XXX[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.target_rank_score_s_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.target_rank_score_s_plus_label = Label(
            text="S+: [color=00FA9A]XX,XXX[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.target_rank_score_s_plus_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.target_rank_score_s_plus_plus_label = Label(
            text="S++: [color=00FA9A]XX,XXX[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.target_rank_score_s_plus_plus_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        target_rank_scores_layout.add_widget(self.target_rank_score_b_label)
        target_rank_scores_layout.add_widget(self.target_rank_score_a_label)
        target_rank_scores_layout.add_widget(self.target_rank_score_s_label)
        target_rank_scores_layout.add_widget(self.target_rank_score_s_plus_label)
        target_rank_scores_layout.add_widget(self.target_rank_score_s_plus_plus_label)

        level_information_layout.add_widget(target_rank_scores_layout)

        stylish_action_challenges_layout: BoxLayout = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            height="140dp",
            spacing="5dp",
            size_hint_x=1,
        )

        stylish_action_challenges_layout.bind(minimum_height=stylish_action_challenges_layout.setter("height"))

        stylish_action_challenges_label: Label = Label(
            text="[b]Stylish Action Challenges[/b]",
            markup=True,
            size_hint_y=None,
            font_size="16dp",
            height="20dp",
            halign="left",
            valign="middle",
        )

        stylish_action_challenges_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        stylish_action_challenges_layout.add_widget(stylish_action_challenges_label)

        self.stylish_action_challenge_1_label = Label(
            text="#1: [color=00FA9A]Xx Stylish Action[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.stylish_action_challenge_1_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.stylish_action_challenge_2_label = Label(
            text="#2: [color=00FA9A]Xx Stylish Action[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.stylish_action_challenge_2_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.stylish_action_challenge_3_label = Label(
            text="#3: [color=00FA9A]Xx Stylish Action[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.stylish_action_challenge_3_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.stylish_action_challenge_3_label = Label(
            text="#3: [color=00FA9A]Xx Stylish Action[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.stylish_action_challenge_3_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.stylish_action_challenge_4_label = Label(
            text="#4: [color=00FA9A]Xx Stylish Action[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.stylish_action_challenge_4_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.stylish_action_challenge_5_label = Label(
            text="#5: [color=00FA9A]Xx Stylish Action[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.stylish_action_challenge_5_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        stylish_action_challenges_layout.add_widget(self.stylish_action_challenge_1_label)

        if self.ctx.game_controller.option_stylish_action_challenge_count_per_level > 1:
            stylish_action_challenges_layout.add_widget(self.stylish_action_challenge_2_label)

        if self.ctx.game_controller.option_stylish_action_challenge_count_per_level > 2:
            stylish_action_challenges_layout.add_widget(self.stylish_action_challenge_3_label)

        if self.ctx.game_controller.option_stylish_action_challenge_count_per_level > 3:
            stylish_action_challenges_layout.add_widget(self.stylish_action_challenge_4_label)

        if self.ctx.game_controller.option_stylish_action_challenge_count_per_level > 4:
            stylish_action_challenges_layout.add_widget(self.stylish_action_challenge_5_label)

        if self.ctx.game_controller.option_include_stylish_action_challenges:
            level_information_layout.add_widget(stylish_action_challenges_layout)

        useful_items_layout: BoxLayout = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            height="140dp",
            spacing="5dp",
            size_hint_x=1,
        )

        useful_items_layout.bind(minimum_height=useful_items_layout.setter("height"))

        useful_items_label: Label = Label(
            text="[b]Useful Items[/b]",
            markup=True,
            size_hint_y=None,
            font_size="16dp",
            height="20dp",
            halign="left",
            valign="middle",
        )

        useful_items_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        useful_items_layout.add_widget(useful_items_label)

        self.useful_time_discount_label = Label(
            text="10% Time Discount: [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.useful_time_discount_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.useful_double_score_label = Label(
            text="Double Score: [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.useful_double_score_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.useful_unlimited_ammo_label = Label(
            text="Unlimited Ammo: [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.useful_unlimited_ammo_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.useful_unlimited_cannon_label = Label(
            text="Unlimited Cannon: [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.useful_unlimited_cannon_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.useful_invincibility_label = Label(
            text="Invincibility: [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.useful_invincibility_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        useful_items_layout.add_widget(self.useful_time_discount_label)
        useful_items_layout.add_widget(self.useful_double_score_label)

        if self.ctx.game_controller.option_include_overpowered_items:
            useful_items_layout.add_widget(self.useful_unlimited_ammo_label)
            useful_items_layout.add_widget(self.useful_unlimited_cannon_label)

            if not self.ctx.game_controller.option_invincible_mode:
                useful_items_layout.add_widget(self.useful_invincibility_label)

        level_information_layout.add_widget(useful_items_layout)

        self.add_widget(level_information_layout)

        progressive_items_layout: BoxLayout = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            height="140dp",
            spacing="5dp",
            size_hint_x=1,
            padding=[0, 15, 0, 0],
        )

        progressive_items_layout.bind(minimum_height=progressive_items_layout.setter("height"))

        progressive_items_label: Label = Label(
            text="[b]Progressive Items[/b]",
            markup=True,
            size_hint_y=None,
            font_size="16dp",
            height="20dp",
            halign="left",
            valign="middle",
        )

        progressive_items_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        progressive_items_layout.add_widget(progressive_items_label)

        self.burn_rate_reduction_label = Label(
            text="Multiplier Burn Rate Reduction: [color=00FA9A]+++++[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.burn_rate_reduction_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.fresh_cooldown_reduction_label = Label(
            text="Fresh Cooldown Reduction: [color=00FA9A]+++++[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.fresh_cooldown_reduction_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        progressive_items_layout.add_widget(self.burn_rate_reduction_label)
        progressive_items_layout.add_widget(self.fresh_cooldown_reduction_label)

        self.add_widget(progressive_items_layout)

        license_items_label: Label = Label(
            text="[b]Stylish Action Licenses[/b]",
            markup=True,
            size_hint_y=None,
            font_size="16dp",
            height="40dp",
            halign="left",
            valign="middle",
            padding=[0, 20, 0, 0]
        )

        license_items_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        if self.ctx.game_controller.option_include_stylish_action_challenges:
            self.add_widget(license_items_label)

        license_items_layout: BoxLayout = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height="100dp",
            spacing="8dp",
        )

        license_items_layout.bind(minimum_height=license_items_layout.setter("height"))

        license_items_1_layout: BoxLayout = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            height="100dp",
            spacing="5dp",
            size_hint_x=1,
        )

        license_items_1_layout.bind(minimum_height=useful_items_layout.setter("height"))

        self.license_dive_frag_label = Label(
            text="Dive Frag: [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.license_dive_frag_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.license_wall_run_frag_label = Label(
            text="Wall Run Frag: [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.license_wall_run_frag_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.license_flip_frag_label = Label(
            text="Flip Frag: [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.license_flip_frag_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.license_kickslide_label = Label(
            text="Kickslide: [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.license_kickslide_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.license_slide_frag_label = Label(
            text="Slide Frag: [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.license_slide_frag_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        license_items_1_layout.add_widget(self.license_dive_frag_label)
        license_items_1_layout.add_widget(self.license_wall_run_frag_label)
        license_items_1_layout.add_widget(self.license_flip_frag_label)
        license_items_1_layout.add_widget(self.license_kickslide_label)
        license_items_1_layout.add_widget(self.license_slide_frag_label)

        license_items_layout.add_widget(license_items_1_layout)

        license_items_2_layout: BoxLayout = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            height="100dp",
            spacing="5dp",
            size_hint_x=1,
        )

        license_items_2_layout.bind(minimum_height=useful_items_layout.setter("height"))

        self.license_quick_shot_label = Label(
            text="Quick Shot: [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.license_quick_shot_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.license_multikill_label = Label(
            text="Multikill: [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.license_multikill_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.license_throw_hit_label = Label(
            text="Throw Hit: [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.license_throw_hit_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.license_cannon_frag_label = Label(
            text="Cannon Frag: [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.license_cannon_frag_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.license_drop_kick_label = Label(
            text="Drop Kick: [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.license_drop_kick_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        license_items_2_layout.add_widget(self.license_quick_shot_label)
        license_items_2_layout.add_widget(self.license_multikill_label)
        license_items_2_layout.add_widget(self.license_throw_hit_label)
        license_items_2_layout.add_widget(self.license_cannon_frag_label)
        license_items_2_layout.add_widget(self.license_drop_kick_label)

        license_items_layout.add_widget(license_items_2_layout)

        license_items_3_layout: BoxLayout = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            height="100dp",
            spacing="5dp",
            size_hint_x=1,
        )

        license_items_3_layout.bind(minimum_height=useful_items_layout.setter("height"))

        self.license_wall_bang_label = Label(
            text="Wall Bang: [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.license_wall_bang_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.license_stole_weapon_label = Label(
            text="Stole Weapon: [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.license_stole_weapon_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.license_air_shot_label = Label(
            text="Air Shot: [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.license_air_shot_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.license_kick_label = Label(
            text="Kick: [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.license_kick_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.license_nice_throw_label = Label(
            text="Nice Throw: [color=00FA9A]+[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.license_nice_throw_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        license_items_3_layout.add_widget(self.license_wall_bang_label)
        license_items_3_layout.add_widget(self.license_stole_weapon_label)
        license_items_3_layout.add_widget(self.license_air_shot_label)
        license_items_3_layout.add_widget(self.license_kick_label)
        license_items_3_layout.add_widget(self.license_nice_throw_label)

        license_items_layout.add_widget(license_items_3_layout)

        if self.ctx.game_controller.option_include_stylish_action_challenges:
            self.add_widget(license_items_layout)

        self.last_seen_level = None

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

        # EdenSys Root Keys
        edensys_root_keys_obtained: int = received_items.get("EdenSys Root Key", 0)

        self.edensys_root_keys_label.text = (
            "[b]EdenSys Root Keys[/b]\n"
            f"Retrieved [color=00FA9A]{edensys_root_keys_obtained}[/color] of "
            f"[color=00FA9A]{self.ctx.game_controller.option_edensys_root_keys_required}[/color] needed "
            f"([color=888888]{self.ctx.game_controller.option_edensys_root_keys_total} total[/color])"
        )

        # Goal
        if self.ctx.game_controller.option_goal == SeveredSteelAPGoals.EDENSYS_ROOT_KEYS_FINAL_LEVEL:
            self.goal_label.text = (
                "[b]Goal[/b]\n"
                f"Retrieve the EdenSys Root Keys, then clear {self.ctx.game_controller.selected_goal_level.value}!"
            )
        elif self.ctx.game_controller.option_goal == SeveredSteelAPGoals.EDENSYS_ROOT_KEY_HUNT:
            self.goal_label.text = (
                "[b]Goal[/b]\n"
                "Retrieve the EdenSys Root Keys!"
            )

        # Level
        if game_state is None or not game_state.is_valid or not game_state.is_in_level:
            self.level_information_level_image.texture = None
            self.level_information_level_image.opacity = 0.1

            self.level_information_title.text = f"[b]Begin Playing a Firefight 2.0 Level...[/b]"
            self.level_information_subtitle.text = f"[b]This level is not included in this seed.[/b]"

            self.target_time_label.text = "[color=888888]XX:XX[/color]"

            self.target_rank_score_b_label.text = "B: [color=888888]XX,XXX[/color]"
            self.target_rank_score_a_label.text = "A: [color=888888]XX,XXX[/color]"
            self.target_rank_score_s_label.text = "S: [color=888888]XX,XXX[/color]"
            self.target_rank_score_s_plus_label.text = "S+: [color=888888]XX,XXX[/color]"
            self.target_rank_score_s_plus_plus_label.text = "S++: [color=888888]XX,XXX[/color]"

            self.stylish_action_challenge_1_label.text = "#1: [color=888888]Xx Stylish Action[/color]"
            self.stylish_action_challenge_2_label.text = "#2: [color=888888]Xx Stylish Action[/color]"
            self.stylish_action_challenge_3_label.text = "#3: [color=888888]Xx Stylish Action[/color]"
            self.stylish_action_challenge_4_label.text = "#4: [color=888888]Xx Stylish Action[/color]"
            self.stylish_action_challenge_5_label.text = "#5: [color=888888]Xx Stylish Action[/color]"

            self.useful_time_discount_label.text = "10% Time Discount: [color=888888]-[/color]"
            self.useful_double_score_label.text = "Double Score: [color=888888]-[/color]"
            self.useful_unlimited_ammo_label.text = "Unlimited Ammo: [color=888888]-[/color]"
            self.useful_unlimited_cannon_label.text = "Unlimited Cannon: [color=888888]-[/color]"
            self.useful_invincibility_label.text = "Invincibility: [color=888888]-[/color]"

            self.last_seen_level = None
        else:
            if self.last_seen_level != game_state.level:
                image_path: str = f"assets/{game_state.level.value}.png"
                image_bytes: bytes = pkgutil.get_data(client_gui.__name__, image_path)

                image: CoreImage = CoreImage(io.BytesIO(image_bytes), ext="png")

                self.level_information_level_image.texture = image.texture
                self.level_information_level_image.opacity = 1.0

                self.last_seen_level = game_state.level

            self.level_information_title.text = f"[b]{game_state.level.value}[/b]"

            level_unlock_item: str = f"Level Unlock: {game_state.level.value}"

            is_level_in_seed: bool = False
            is_level_goal: bool = False
            is_level_unlocked: bool = False
            are_level_conditions_valid: bool = False

            if game_state.level in (self.ctx.game_controller.selected_levels + [self.ctx.game_controller.selected_goal_level]):
                is_level_in_seed = True

            if game_state.level == self.ctx.game_controller.selected_goal_level:
                is_level_goal = True

            if level_unlock_item in received_items and received_items[level_unlock_item] > 0:
                if is_level_goal:
                    if edensys_root_keys_obtained >= self.ctx.game_controller.option_edensys_root_keys_required:
                        is_level_unlocked = True
                else:
                    is_level_unlocked = True

            if is_level_in_seed and is_level_unlocked:
                are_level_conditions_valid = True

                if not is_level_goal:
                    if self.ctx.game_controller.option_mutator_percentage > 0:
                        mutator: Optional[SeveredSteelMutators] = self.ctx.game_controller.level_to_mutator[game_state.level]

                        if mutator is not None and mutator not in game_state.mutators:
                            are_level_conditions_valid = False

                    if self.ctx.game_controller.option_mirrored_percentage > 0:
                        is_mirrored: bool = self.ctx.game_controller.level_to_is_mirrored[game_state.level]

                        if game_state.is_mirrored != is_mirrored:
                            are_level_conditions_valid = False

            mapping: Dict[bool, str] = {
                False: "[color=FF4C4C]-[/color]",
                True: "[color=00FA9A]+[/color]"
            }

            self.level_information_subtitle.text = f"In Seed? {mapping[is_level_in_seed]}    Unlocked? {mapping[is_level_unlocked]}    Valid Mutator / Mirrored? {mapping[are_level_conditions_valid]}"

            if is_level_in_seed and is_level_unlocked and not is_level_goal and are_level_conditions_valid:
                if self.ctx.game_controller.option_include_target_times:
                    target_time_ratio: float = round(self.ctx.game_controller.target_time_ratios[game_state.level], 2)

                    target_time: int = self.ctx.game_controller.target_times[game_state.level]
                    formatted_target_time: str = f"{target_time // 60:1d}:{target_time % 60:02d}"

                    self.target_time_label.text = f"[color=00FA9A]{formatted_target_time}[/color] [color=888888][size=11]{target_time_ratio}x Base[/size][/color]"

                target_rank_score_ratio: float = round(self.ctx.game_controller.target_rank_score_ratios[game_state.level], 2)

                self.target_rank_score_b_label.text = f"B: [color=00FA9A]{self.ctx.game_controller.target_rank_scores[game_state.level][0]:,}[/color] [color=888888][size=11]{target_rank_score_ratio}x Base[/size][/color]"
                self.target_rank_score_a_label.text = f"A: [color=00FA9A]{self.ctx.game_controller.target_rank_scores[game_state.level][1]:,}[/color] [color=888888][size=11]{target_rank_score_ratio}x Base[/size][/color]"
                self.target_rank_score_s_label.text = f"S: [color=00FA9A]{self.ctx.game_controller.target_rank_scores[game_state.level][2]:,}[/color] [color=888888][size=11]{target_rank_score_ratio}x Base[/size][/color]"
                self.target_rank_score_s_plus_label.text = f"S+: [color=00FA9A]{self.ctx.game_controller.target_rank_scores[game_state.level][3]:,}[/color] [color=888888][size=11]{target_rank_score_ratio}x Base[/size][/color]"
                self.target_rank_score_s_plus_plus_label.text = f"S++: [color=00FA9A]{self.ctx.game_controller.target_rank_scores[game_state.level][4]:,}[/color] [color=888888][size=11]{target_rank_score_ratio}x Base[/size][/color]"

                if self.ctx.game_controller.option_include_stylish_action_challenges:
                    stylish_action, count = self.ctx.game_controller.level_to_stylish_action_challenges[game_state.level][0]
                    self.stylish_action_challenge_1_label.text = f"#1: [color=00FA9A]{count}x {stylish_action.value}[/color]"

                    if self.ctx.game_controller.option_stylish_action_challenge_count_per_level > 1:
                        stylish_action, count = self.ctx.game_controller.level_to_stylish_action_challenges[game_state.level][1]
                        self.stylish_action_challenge_2_label.text = f"#2: [color=00FA9A]{count}x {stylish_action.value}[/color]"

                    if self.ctx.game_controller.option_stylish_action_challenge_count_per_level > 2:
                        stylish_action, count = self.ctx.game_controller.level_to_stylish_action_challenges[game_state.level][2]
                        self.stylish_action_challenge_3_label.text = f"#3: [color=00FA9A]{count}x {stylish_action.value}[/color]"

                    if self.ctx.game_controller.option_stylish_action_challenge_count_per_level > 3:
                        stylish_action, count = self.ctx.game_controller.level_to_stylish_action_challenges[game_state.level][3]
                        self.stylish_action_challenge_4_label.text = f"#4: [color=00FA9A]{count}x {stylish_action.value}[/color]"

                    if self.ctx.game_controller.option_stylish_action_challenge_count_per_level > 4:
                        stylish_action, count = self.ctx.game_controller.level_to_stylish_action_challenges[game_state.level][4]
                        self.stylish_action_challenge_5_label.text = f"#5: [color=00FA9A]{count}x {stylish_action.value}[/color]"

                item_count: int = received_items.get(f"{game_state.level.value}: 10% Target Time Discount", 0)
                self.useful_time_discount_label.text = f"10% Time Discount: {mapping[item_count > 0]}"

                item_count: int = received_items.get(f"{game_state.level.value}: Double Score", 0)
                self.useful_double_score_label.text = f"Double Score: {mapping[item_count > 0]}"

                if self.ctx.game_controller.option_include_overpowered_items:
                    item_count: int = received_items.get(f"{game_state.level.value}: Unlimited Ammo Unlocked", 0)
                    self.useful_unlimited_ammo_label.text = f"Unlimited Ammo: {mapping[item_count > 0]}"

                    item_count: int = received_items.get(f"{game_state.level.value}: Unlimited Cannon Ammo Unlocked", 0)
                    self.useful_unlimited_cannon_label.text = f"Unlimited Cannon: {mapping[item_count > 0]}"

                    if not self.ctx.game_controller.option_invincible_mode:
                        item_count: int = received_items.get(f"{game_state.level.value}: Invincibility Unlocked", 0)
                        self.useful_invincibility_label.text = f"Invincibility: {mapping[item_count > 0]}"
            else:
                self.target_time_label.text = "[color=888888]XX:XX[/color]"

                self.target_rank_score_b_label.text = "B: [color=888888]XX,XXX[/color]"
                self.target_rank_score_a_label.text = "A: [color=888888]XX,XXX[/color]"
                self.target_rank_score_s_label.text = "S: [color=888888]XX,XXX[/color]"
                self.target_rank_score_s_plus_label.text = "S+: [color=888888]XX,XXX[/color]"
                self.target_rank_score_s_plus_plus_label.text = "S++: [color=888888]XX,XXX[/color]"

                self.stylish_action_challenge_1_label.text = "#1: [color=888888]Xx Stylish Action[/color]"
                self.stylish_action_challenge_2_label.text = "#2: [color=888888]Xx Stylish Action[/color]"
                self.stylish_action_challenge_3_label.text = "#3: [color=888888]Xx Stylish Action[/color]"
                self.stylish_action_challenge_4_label.text = "#4: [color=888888]Xx Stylish Action[/color]"
                self.stylish_action_challenge_5_label.text = "#5: [color=888888]Xx Stylish Action[/color]"

                self.useful_time_discount_label.text = "10% Time Discount: [color=888888]-[/color]"
                self.useful_double_score_label.text = "Double Score: [color=888888]-[/color]"
                self.useful_unlimited_ammo_label.text = "Unlimited Ammo: [color=888888]-[/color]"
                self.useful_unlimited_cannon_label.text = "Unlimited Cannon: [color=888888]-[/color]"
                self.useful_invincibility_label.text = "Invincibility: [color=888888]-[/color]"

        mapping: Dict[bool, str] = {
            False: "[color=FF4C4C]-[/color]",
            True: "[color=00FA9A]+[/color]"
        }

        item_count: int = received_items.get("Progressive Multiplier Burn Rate Reduction", 0)
        self.burn_rate_reduction_label.text = f"Multiplier Burn Rate Reduction: {mapping[item_count > 0]} {mapping[item_count > 1]} {mapping[item_count > 2]} {mapping[item_count > 3]} {mapping[item_count > 4]}"

        item_count: int = received_items.get("Progressive Fresh Cooldown Reduction", 0)
        self.fresh_cooldown_reduction_label.text = f"Fresh Cooldown Reduction: {mapping[item_count > 0]} {mapping[item_count > 1]} {mapping[item_count > 2]} {mapping[item_count > 3]} {mapping[item_count > 4]}"

        if self.ctx.game_controller.option_include_stylish_action_challenges:
            item_count: int = received_items.get(f"Stylish Action License: {SeveredSteelStylishActions.DIVE_FRAG.value}", 0)
            self.license_dive_frag_label.text = f"Dive Frag: {mapping[item_count > 0]}"

            item_count: int = received_items.get(f"Stylish Action License: {SeveredSteelStylishActions.WALL_RUN_FRAG.value}", 0)
            self.license_wall_run_frag_label.text = f"Wall Run Frag: {mapping[item_count > 0]}"

            item_count: int = received_items.get(f"Stylish Action License: {SeveredSteelStylishActions.FLIP_FRAG.value}", 0)
            self.license_flip_frag_label.text = f"Flip Frag: {mapping[item_count > 0]}"

            item_count: int = received_items.get(f"Stylish Action License: {SeveredSteelStylishActions.KICKSLIDE.value}", 0)
            self.license_kickslide_label.text = f"Kickslide: {mapping[item_count > 0]}"

            item_count: int = received_items.get(f"Stylish Action License: {SeveredSteelStylishActions.SLIDE_FRAG.value}", 0)
            self.license_slide_frag_label.text = f"Slide Frag: {mapping[item_count > 0]}"

            item_count: int = received_items.get(f"Stylish Action License: {SeveredSteelStylishActions.QUICK_SHOT.value}", 0)
            self.license_quick_shot_label.text = f"Quick Shot: {mapping[item_count > 0]}"

            item_count: int = received_items.get(f"Stylish Action License: {SeveredSteelStylishActions.MULTIKILL.value}", 0)
            self.license_multikill_label.text = f"Multikill: {mapping[item_count > 0]}"

            item_count: int = received_items.get(f"Stylish Action License: {SeveredSteelStylishActions.THROW_HIT.value}", 0)
            self.license_throw_hit_label.text = f"Throw Hit: {mapping[item_count > 0]}"

            item_count: int = received_items.get(f"Stylish Action License: {SeveredSteelStylishActions.CANNON_FRAG.value}", 0)
            self.license_cannon_frag_label.text = f"Cannon Frag: {mapping[item_count > 0]}"

            item_count: int = received_items.get(f"Stylish Action License: {SeveredSteelStylishActions.DROP_KICK.value}", 0)
            self.license_drop_kick_label.text = f"Drop Kick: {mapping[item_count > 0]}"

            item_count: int = received_items.get(f"Stylish Action License: {SeveredSteelStylishActions.WALL_BANG.value}", 0)
            self.license_wall_bang_label.text = f"Wall Bang: {mapping[item_count > 0]}"

            item_count: int = received_items.get(f"Stylish Action License: {SeveredSteelStylishActions.STOLE_WEAPON.value}", 0)
            self.license_stole_weapon_label.text = f"Stole Weapon: {mapping[item_count > 0]}"

            item_count: int = received_items.get(f"Stylish Action License: {SeveredSteelStylishActions.AIR_SHOT.value}", 0)
            self.license_air_shot_label.text = f"Air Shot: {mapping[item_count > 0]}"

            item_count: int = received_items.get(f"Stylish Action License: {SeveredSteelStylishActions.KICK.value}", 0)
            self.license_kick_label.text = f"Kick: {mapping[item_count > 0]}"

            item_count: int = received_items.get(f"Stylish Action License: {SeveredSteelStylishActions.NICE_THROW.value}", 0)
            self.license_nice_throw_label.text = f"Nice Throw: {mapping[item_count > 0]}"


class SeveredSteelLevelsLayout(BoxLayout):
    ctx: SeveredSteelContext

    level_label: Label
    level_images: List[Image]
    level_mutator_labels: List[Label]
    level_is_mirrored_labels: List[Label]

    level_data: Dict[SeveredSteelLevels, Dict[str, Any]]

    def __init__(self, ctx: SeveredSteelContext) -> None:
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
        self.level_mutator_labels = list()
        self.level_is_mirrored_labels = list()

        self.level_data = dict()

        levels: List[SeveredSteelLevels] = self.ctx.game_controller.selected_levels[:]

        if self.ctx.game_controller.selected_goal_level is not None:
            levels.append(self.ctx.game_controller.selected_goal_level)

        level: SeveredSteelLevels
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
            cols=2,
            spacing=[0, 8],
            padding=0,
            size_hint_y=None,
        )

        grid_layout.bind(minimum_height=grid_layout.setter("height"))

        level: SeveredSteelLevels
        data: Dict[str, Any]
        for level, data in self.level_data.items():
            level_layout: BoxLayout = BoxLayout(orientation="horizontal", size_hint_y=None, height="36dp", spacing="8dp")
            level_layout.bind(minimum_height=level_layout.setter("height"))

            image_bytes: bytes = pkgutil.get_data(client_gui.__name__, data["image_path"])
            image: CoreImage = CoreImage(io.BytesIO(image_bytes), ext="png")

            level_image = Image(
                texture=image.texture,
                size=(224, 36),
                size_hint=(None, None),
                allow_stretch=True,
                opacity=0.3
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

            level_layout.add_widget(level_image)

            level_labels_layout: BoxLayout = BoxLayout(orientation="vertical", size_hint_y=None, height="36dp", spacing="0dp")

            level_mutator_label: Label = Label(
                text=f"No Mutator",
                font_size="12dp",
                size_hint_y=None,
                height="14dp",
                halign="left",
                valign="bottom",
                opacity=0.1,
            )

            level_mutator_label.bind(size=lambda label, size: setattr(label, "text_size", size))

            self.level_mutator_labels.append(level_mutator_label)

            level_labels_layout.add_widget(level_mutator_label)

            level_is_mirrored_label: Label = Label(
                text=f"Not Mirrored",
                font_size="12dp",
                size_hint_y=None,
                height="18dp",
                halign="left",
                valign="bottom",
                opacity=0.1,
            )

            level_is_mirrored_label.bind(size=lambda label, size: setattr(label, "text_size", size))

            self.level_is_mirrored_labels.append(level_is_mirrored_label)

            level_labels_layout.add_widget(level_is_mirrored_label)

            level_layout.add_widget(level_labels_layout)

            grid_layout.add_widget(level_layout)

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

        level: SeveredSteelLevels
        data: Dict[str, Any]
        for i, (level, data) in enumerate(self.level_data.items()):
            is_unlocked: bool = False

            if data["unlock_item"] in received_items and received_items[data["unlock_item"]] > 0:
                if data["is_goal"]:
                    edensys_root_keys_required: int = self.ctx.game_controller.option_edensys_root_keys_required
                    edensys_root_keys_obtained: int = received_items.get("EdenSys Root Key", 0)

                    if edensys_root_keys_obtained >= edensys_root_keys_required:
                        is_unlocked = True
                else:
                    is_unlocked = True

            self.level_images[i].opacity = 1.0 if is_unlocked else 0.3

            if is_unlocked and not data["is_goal"]:
                if self.ctx.game_controller.level_to_mutator[level] is None:
                    self.level_mutator_labels[i].text = "No Mutator"
                    self.level_mutator_labels[i].opacity = 0.1
                else:
                    self.level_mutator_labels[i].text = self.ctx.game_controller.level_to_mutator[level].value
                    self.level_mutator_labels[i].opacity = 1.0

                if self.ctx.game_controller.level_to_is_mirrored[level] in [False, None]:
                    self.level_is_mirrored_labels[i].text = "Not Mirrored"
                    self.level_is_mirrored_labels[i].opacity = 0.1
                else:
                    self.level_is_mirrored_labels[i].text = "Mirrored"
                    self.level_is_mirrored_labels[i].opacity = 1.0
            else:
                self.level_mutator_labels[i].text = "No Mutator"
                self.level_mutator_labels[i].opacity = 0.1

                self.level_is_mirrored_labels[i].text = "Not Mirrored"
                self.level_is_mirrored_labels[i].opacity = 0.1


class SeveredSteelContent(ScrollView):
    ctx: SeveredSteelContext

    layout: BoxLayout

    layout_game_information: SeveredSteelGameInformationLayout
    layout_levels: SeveredSteelLevelsLayout

    timer: Clock

    def __init__(self, ctx: SeveredSteelContext) -> None:
        super().__init__()

        self.ctx = ctx

        self.layout = BoxLayout(orientation="vertical", size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter("height"))

        self.layout_game_information = SeveredSteelGameInformationLayout(ctx=self.ctx)
        self.layout.add_widget(self.layout_game_information)

        self.layout_levels = SeveredSteelLevelsLayout(ctx=self.ctx)
        self.layout.add_widget(self.layout_levels)

        self.add_widget(self.layout)

        self.timer = Clock.schedule_interval(self.update, 1.0 / 10.0)

    def update(self, *_) -> None:
        try:
            self.layout_game_information.update()
            self.layout_levels.update()
        except Exception:
            import traceback

            with open("severed_steel_errors.log", "a") as f:
                f.write(traceback.format_exc() + "\n\n")


class SeveredSteelTabLayout(BoxLayout):
    ctx: SeveredSteelContext

    layout_content: BoxLayout
    layout_content_severed_steel: SeveredSteelContent

    layout_not_connected: NotConnectedLayout

    def __init__(self, ctx: SeveredSteelContext) -> None:
        super().__init__(orientation="vertical", padding="8dp")

        self.bind(minimum_height=self.setter('height'))

        self.ctx = ctx

        self.layout_not_connected = NotConnectedLayout(self.ctx)
        self.add_widget(self.layout_not_connected)

        self.layout_content = BoxLayout(orientation="horizontal", spacing="16dp", padding=["8dp", "0dp"])
        self.add_widget(self.layout_content)

        self.update()

    def update(self) -> None:
        if self.ctx.game_controller.target_times is None:
            self.layout_not_connected.show()

            if hasattr(self, "layout_content_severed_steel"):
                self.layout_content_severed_steel.timer.cancel()

            self.layout_content.clear_widgets()

            return

        self.layout_not_connected.hide()

        if not len(self.layout_content.children):
            self.layout_content_severed_steel = SeveredSteelContent(ctx=self.ctx)
            self.layout_content.add_widget(self.layout_content_severed_steel)

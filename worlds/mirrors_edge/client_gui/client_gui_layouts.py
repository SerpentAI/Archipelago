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

from ..client import MirrorsEdgeContext

from ..enums import (
    MirrorsEdgeAPGoals,
    MirrorsEdgeContexts,
    MirrorsEdgeLevels,
    MirrorsEdgeAbilities,
)

from ..game_state_manager import GameStateManager, GameState

from .. import client_gui


class NotConnectedLayout(BoxLayout):
    ctx: MirrorsEdgeContext

    def __init__(self, ctx: MirrorsEdgeContext) -> None:
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


class MirrorsEdgeGameInformationLayout(BoxLayout):
    ctx: MirrorsEdgeContext

    game_state_manager: GameStateManager

    information_label: Label

    runner_bags_label: Label
    goal_label: Label

    level_information_level_image: Image

    level_information_title: Label
    level_information_subtitle: Label

    target_time_1_star_label: Label
    target_time_2_star_label: Label
    target_time_3_star_label: Label

    item_time_bonus_1_second_label: Label
    item_time_bonus_3_seconds_label: Label
    item_time_bonus_5_seconds_label: Label

    ability_information_faith_image: Image
    faiths_abilities_label: Label

    one_eighty_turn_label: Label
    airborne_one_eighty_turn_label: Label

    balance_label: Label
    barge_label: Label
    climb_label: Label
    coil_label: Label

    dodge_jump_label: Label
    grab_label: Label
    melee_attack_label: Label
    springboard_label: Label

    sprint_label: Label
    swing_label: Label
    vault_label: Label
    wall_climb_label: Label

    wall_run_label: Label
    zipline_label: Label

    checkpoints_passed_label: Label
    checkpoints_total_label: Label

    last_seen_level: Optional[MirrorsEdgeLevels]

    def __init__(self, ctx: MirrorsEdgeContext) -> None:
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

        # Runner Bags
        self.runner_bags_label: Label = Label(
            text=(
                f"[b]Runner Bags[/b]\n"
                f"Retrieved [color=00FA9A]0[/color] of "
                f"[color=00FA9A]{self.ctx.game_controller.option_runner_bags_required}[/color] needed "
                f"([color=888888]{self.ctx.game_controller.option_runner_bags_total} total[/color])"
            ),
            markup=True,
            size_hint_x=40,
            size_hint_y=None,
            height="60dp",
            halign="left",
            valign="middle",
        )

        self.runner_bags_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        goal_header_layout.add_widget(self.runner_bags_label)

        # Goal
        self.goal_label: Label = Label(
            text=(
                f"[b]Goal[/b]\n"
                f"Retrieve the Runner Bags!"
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
            size=(245, 51),
            size_hint=(None, None),
            allow_stretch=True,
            opacity=0.1
        )

        level_information_header_layout.add_widget(self.level_information_level_image)

        level_information_subheader_layout: BoxLayout = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            height="51dp",
            spacing="8dp",
        )

        self.level_information_title = Label(
            text=f"[b]Begin Playing a Time Trial Level...[/b]",
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

        target_times_layout: BoxLayout = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            height="140dp",
            spacing="5dp",
            size_hint_x=50,
        )

        target_times_layout.bind(minimum_height=target_times_layout.setter("height"))

        target_times_label: Label = Label(
            text="[b]Star Rating Targets[/b]",
            markup=True,
            size_hint_y=None,
            font_size="16dp",
            height="20dp",
            halign="left",
            valign="middle",
        )

        target_times_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        target_times_layout.add_widget(target_times_label)

        self.target_time_1_star_label = Label(
            text=f"1 Star: [color=888888]X:XX[/color] [color=888888][size=11]{self.ctx.game_controller.option_target_time_adjustment_percentage}% Base[/size][/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.target_time_1_star_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.target_time_2_star_label = Label(
            text=f"2 Stars: [color=888888]X:XX[/color] [color=888888][size=11]{self.ctx.game_controller.option_target_time_adjustment_percentage}% Base[/size][/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.target_time_2_star_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.target_time_3_star_label = Label(
            text=f"3 Stars: [color=888888]X:XX[/color] [color=888888][size=11]{self.ctx.game_controller.option_target_time_adjustment_percentage}% Base[/size][/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.target_time_3_star_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        target_times_layout.add_widget(self.target_time_1_star_label)

        if self.ctx.game_controller.option_include_2_star_ratings:
            target_times_layout.add_widget(self.target_time_2_star_label)

        if self.ctx.game_controller.option_include_3_star_ratings:
            target_times_layout.add_widget(self.target_time_3_star_label)

        level_information_layout.add_widget(target_times_layout)

        time_bonus_items_layout: BoxLayout = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            height="140dp",
            spacing="5dp",
            size_hint_x=50,
        )

        time_bonus_items_layout.bind(minimum_height=time_bonus_items_layout.setter("height"))

        time_bonus_items_label: Label = Label(
            text="[b]Time Bonus Items[/b]",
            markup=True,
            size_hint_y=None,
            font_size="16dp",
            height="20dp",
            halign="left",
            valign="middle",
        )

        time_bonus_items_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        time_bonus_items_layout.add_widget(time_bonus_items_label)

        self.item_time_bonus_1_second_label = Label(
            text="1 Second Time Bonus: [color=888888]Xx[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.item_time_bonus_1_second_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.item_time_bonus_3_seconds_label = Label(
            text="3 Seconds Time Bonus: [color=888888]Xx[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.item_time_bonus_3_seconds_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.item_time_bonus_5_seconds_label = Label(
            text="5 Seconds Time Bonus: [color=888888]Xx[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="16dp",
            halign="left",
            valign="middle",
        )

        self.item_time_bonus_5_seconds_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        time_bonus_items_layout.add_widget(self.item_time_bonus_1_second_label)
        time_bonus_items_layout.add_widget(self.item_time_bonus_3_seconds_label)
        time_bonus_items_layout.add_widget(self.item_time_bonus_5_seconds_label)

        level_information_layout.add_widget(time_bonus_items_layout)

        self.add_widget(level_information_layout)

        ability_information_layout: BoxLayout = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height="110dp",
            spacing="8dp",
            padding=[0, 20, 0, 0]
        )

        ability_information_layout.bind(minimum_height=ability_information_layout.setter("height"))

        image_path: str = f"assets/Faith.png"
        image_bytes: bytes = pkgutil.get_data(client_gui.__name__, image_path)

        image: CoreImage = CoreImage(io.BytesIO(image_bytes), ext="png")

        self.ability_information_faith_image = Image(
            size=(110, 110),
            size_hint=(None, None),
            allow_stretch=True,
            texture=image.texture,
            opacity=1.0
        )

        ability_information_layout.add_widget(self.ability_information_faith_image)

        ability_information_sublayout: BoxLayout = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height="110dp",
            spacing="8dp",
            size_hint_x=90,
        )

        ability_information_sublayout.bind(minimum_height=ability_information_sublayout.setter("height"))

        ability_information_column_1_layout: BoxLayout = BoxLayout(
            orientation="vertical",
            size_hint_x=37,
            size_hint_y=None,
            height="110dp",
            spacing="5dp",
        )

        ability_information_column_1_layout.bind(minimum_height=ability_information_column_1_layout.setter("height"))

        self.faiths_abilities_label = Label(
            text="[b]Faith's Abilities[/b]",
            markup=True,
            size_hint_y=None,
            font_size="18dp",
            height="42dp",
            halign="left",
            valign="middle",
            padding=[0, 0, 0, 20],
        )

        self.faiths_abilities_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        ability_information_column_1_layout.add_widget(self.faiths_abilities_label)

        self.one_eighty_turn_label = Label(
            text="[b]180 Turn:[/b] [color=888888]-[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="18dp",
            halign="left",
            valign="middle",
        )

        self.one_eighty_turn_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        ability_information_column_1_layout.add_widget(self.one_eighty_turn_label)

        self.airborne_one_eighty_turn_label = Label(
            text="[b]Airborne 180 Turn:[/b] [color=888888]-[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="18dp",
            halign="left",
            valign="middle",
        )

        self.airborne_one_eighty_turn_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        ability_information_column_1_layout.add_widget(self.airborne_one_eighty_turn_label)

        self.balance_label = Label(
            text="[b]Balance:[/b] [color=888888]-[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="18dp",
            halign="left",
            valign="middle",
        )

        self.balance_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        ability_information_column_1_layout.add_widget(self.balance_label)

        ability_information_layout.add_widget(ability_information_column_1_layout)

        ability_information_column_2_layout: BoxLayout = BoxLayout(
            orientation="vertical",
            size_hint_x=21,
            size_hint_y=None,
            height="110dp",
            spacing="5dp",
        )

        ability_information_column_2_layout.bind(minimum_height=ability_information_column_2_layout.setter("height"))

        self.barge_label = Label(
            text="[b]Barge:[/b] [color=888888]-[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="18dp",
            halign="left",
            valign="middle",
        )

        self.barge_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        ability_information_column_2_layout.add_widget(self.barge_label)

        self.climb_label = Label(
            text="[b]Climb:[/b] [color=888888]-[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="18dp",
            halign="left",
            valign="middle",
        )

        self.climb_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        ability_information_column_2_layout.add_widget(self.climb_label)

        self.coil_label = Label(
            text="[b]Coil:[/b] [color=888888]-[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="18dp",
            halign="left",
            valign="middle",
        )

        self.coil_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        ability_information_column_2_layout.add_widget(self.coil_label)

        self.dodge_jump_label = Label(
            text="[b]Dodge Jump:[/b] [color=888888]-[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="18dp",
            halign="left",
            valign="middle",
        )

        self.dodge_jump_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        ability_information_column_2_layout.add_widget(self.dodge_jump_label)

        self.grab_label = Label(
            text="[b]Grab:[/b] [color=888888]-[/color] [color=888888]-[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="18dp",
            halign="left",
            valign="middle",
        )

        self.grab_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        ability_information_column_2_layout.add_widget(self.grab_label)

        ability_information_sublayout.add_widget(ability_information_column_2_layout)

        ability_information_column_3_layout: BoxLayout = BoxLayout(
            orientation="vertical",
            size_hint_x=21,
            size_hint_y=None,
            height="110dp",
            spacing="5dp",
        )

        ability_information_column_3_layout.bind(minimum_height=ability_information_column_3_layout.setter("height"))

        self.melee_attack_label = Label(
            text="[b]Melee Attack:[/b] [color=888888]-[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="18dp",
            halign="left",
            valign="middle",
        )

        self.melee_attack_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        ability_information_column_3_layout.add_widget(self.melee_attack_label)

        self.springboard_label = Label(
            text="[b]Springboard:[/b] [color=888888]-[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="18dp",
            halign="left",
            valign="middle",
        )

        self.springboard_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        ability_information_column_3_layout.add_widget(self.springboard_label)

        self.sprint_label = Label(
            text="[b]Sprint:[/b] [color=888888]-[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="18dp",
            halign="left",
            valign="middle",
        )

        self.sprint_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        ability_information_column_3_layout.add_widget(self.sprint_label)

        self.swing_label = Label(
            text="[b]Swing:[/b] [color=888888]-[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="18dp",
            halign="left",
            valign="middle",
        )

        self.swing_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        ability_information_column_3_layout.add_widget(self.swing_label)

        self.vault_label = Label(
            text="[b]Vault:[/b] [color=888888]-[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="18dp",
            halign="left",
            valign="middle",
        )

        self.vault_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        ability_information_column_3_layout.add_widget(self.vault_label)

        ability_information_sublayout.add_widget(ability_information_column_3_layout)

        ability_information_column_4_layout: BoxLayout = BoxLayout(
            orientation="vertical",
            size_hint_x=21,
            size_hint_y=None,
            height="110dp",
            spacing="5dp",
        )

        ability_information_column_4_layout.bind(minimum_height=ability_information_column_4_layout.setter("height"))

        self.wall_climb_label = Label(
            text="[b]Wall Climb:[/b] [color=888888]-[/color] [color=888888]-[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="18dp",
            halign="left",
            valign="middle",
        )

        self.wall_climb_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        ability_information_column_4_layout.add_widget(self.wall_climb_label)

        self.wall_run_label = Label(
            text="[b]Wall Run:[/b] [color=888888]-[/color] [color=888888]-[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="18dp",
            halign="left",
            valign="middle",
        )

        self.wall_run_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        ability_information_column_4_layout.add_widget(self.wall_run_label)

        self.zipline_label = Label(
            text="[b]Zipline:[/b] [color=888888]-[/color]",
            markup=True,
            size_hint_y=None,
            font_size="14dp",
            height="18dp",
            halign="left",
            valign="middle",
        )

        self.zipline_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        ability_information_column_4_layout.add_widget(self.zipline_label)

        ability_information_sublayout.add_widget(ability_information_column_4_layout)

        ability_information_layout.add_widget(ability_information_sublayout)

        self.add_widget(ability_information_layout)

        self.checkpoints_passed_label = Label(
            text="[b]Checkpoints Passed:[/b] 0",
            markup=True,
            size_hint_y=None,
            font_size="16dp",
            height="40dp",
            halign="left",
            valign="middle",
            padding=[0, 20, 0, 0],
        )

        self.checkpoints_passed_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.add_widget(self.checkpoints_passed_label)

        self.checkpoints_total_label = Label(
            text="[b]Checkpoints Total:[/b] 0",
            markup=True,
            size_hint_y=None,
            font_size="16dp",
            height="20dp",
            halign="left",
            valign="middle",
        )

        self.checkpoints_total_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.add_widget(self.checkpoints_total_label)

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

        # Runner Bags
        runner_bags_obtained: int = received_items.get("Runner Bag", 0)

        self.runner_bags_label.text = (
            "[b]Runner Bags[/b]\n"
            f"Retrieved [color=00FA9A]{runner_bags_obtained}[/color] of "
            f"[color=00FA9A]{self.ctx.game_controller.option_runner_bags_required}[/color] needed "
            f"([color=888888]{self.ctx.game_controller.option_runner_bags_total} total[/color])"
        )

        # Goal
        if self.ctx.game_controller.option_goal == MirrorsEdgeAPGoals.RUNNER_BAGS_FINAL_LEVEL:
            self.goal_label.text = (
                "[b]Goal[/b]\n"
                f"Retrieve the Runner Bags, then finish {self.ctx.game_controller.goal_level.value}!"
            )
        elif self.ctx.game_controller.option_goal == MirrorsEdgeAPGoals.RUNNER_BAG_HUNT:
            self.goal_label.text = (
                "[b]Goal[/b]\n"
                "Retrieve the Runner Bags!"
            )

        # Level
        if game_state is None or game_state.context != MirrorsEdgeContexts.LEVEL or game_state.level is None:
            self.level_information_level_image.texture = None
            self.level_information_level_image.opacity = 0.1

            self.level_information_title.text = "[b]Begin Playing a Time Trial Level...[/b]"
            self.level_information_subtitle.text = "[b]This level is not included in this seed.[/b]"

            self.target_time_1_star_label.text = f"1 Star: [color=888888]X:XX[/color] [color=888888][size=11]{self.ctx.game_controller.option_target_time_adjustment_percentage}% Base[/size][/color]"
            self.target_time_2_star_label.text = f"2 Stars: [color=888888]X:XX[/color] [color=888888][size=11]{self.ctx.game_controller.option_target_time_adjustment_percentage}% Base[/size][/color]"
            self.target_time_3_star_label.text = f"3 Stars: [color=888888]X:XX[/color] [color=888888][size=11]{self.ctx.game_controller.option_target_time_adjustment_percentage}% Base[/size][/color]"

            self.item_time_bonus_1_second_label.text = "1 Second Time Bonus: [color=888888]Xx[/color]"
            self.item_time_bonus_3_seconds_label.text = "3 Seconds Time Bonus: [color=888888]Xx[/color]"
            self.item_time_bonus_5_seconds_label.text = "5 Seconds Time Bonus: [color=888888]Xx[/color]"

            unlocked_string: str = "[color=00FA9A]+[/color] "
            locked_string: str = "[color=FF4C4C]-[/color] "

            one_eighty_turn_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.ONE_EIGHTY_TURN.value}"
            one_eighty_turn_item_count: int = received_items.get(one_eighty_turn_item_name, 0)

            self.one_eighty_turn_label.text = "[b]180 Turn:[/b] " + (unlocked_string if one_eighty_turn_item_count > 0 else locked_string)

            airborne_one_eighty_turn_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.AIRBORNE_ONE_EIGHTY_TURN.value}"
            airborne_one_eighty_turn_item_count: int = received_items.get(airborne_one_eighty_turn_item_name, 0)

            self.airborne_one_eighty_turn_label.text = "[b]Airborne 180 Turn:[/b] " + (unlocked_string if airborne_one_eighty_turn_item_count > 0 else locked_string)

            balance_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.BALANCE.value}"
            balance_item_count: int = received_items.get(balance_item_name, 0)

            self.balance_label.text = "[b]Balance:[/b] " + (unlocked_string if balance_item_count > 0 else locked_string)

            barge_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.BARGE.value}"
            barge_item_count: int = received_items.get(barge_item_name, 0)

            self.barge_label.text = "[b]Barge:[/b] " + (unlocked_string if barge_item_count > 0 else locked_string)

            climb_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.CLIMB.value}"
            climb_item_count: int = received_items.get(climb_item_name, 0)

            self.climb_label.text = "[b]Climb:[/b] " + (unlocked_string if climb_item_count > 0 else locked_string)

            coil_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.COIL.value}"
            coil_item_count: int = received_items.get(coil_item_name, 0)

            self.coil_label.text = "[b]Coil:[/b] " + (unlocked_string if coil_item_count > 0 else locked_string)

            dodge_jump_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.DODGE_JUMP.value}"
            dodge_jump_item_count: int = received_items.get(dodge_jump_item_name, 0)

            self.dodge_jump_label.text = "[b]Dodge Jump:[/b] " + (unlocked_string if dodge_jump_item_count > 0 else locked_string)

            grab_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"
            grab_item_count: int = received_items.get(grab_item_name, 0)

            grab_jump_item_name: str = f"Ability Extension Unlock: {MirrorsEdgeAbilities.GRAB_JUMP.value}"
            grab_jump_item_count: int = received_items.get(grab_jump_item_name, 0)

            grab_text: str = "[b]Grab:[/b] "

            grab_text += unlocked_string if grab_item_count > 0 else locked_string
            grab_text += unlocked_string if grab_jump_item_count > 0 else locked_string

            self.grab_label.text = grab_text

            melee_attack_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.MELEE_ATTACK.value}"
            melee_attack_item_count: int = received_items.get(melee_attack_item_name, 0)

            self.melee_attack_label.text = "[b]Melee Attack:[/b] " + (unlocked_string if melee_attack_item_count > 0 else locked_string)

            springboard_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.SPRINGBOARD.value}"
            springboard_item_count: int = received_items.get(springboard_item_name, 0)

            self.springboard_label.text = "[b]Springboard:[/b] " + (unlocked_string if springboard_item_count > 0 else locked_string)

            sprint_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.SPRINT.value}"
            sprint_item_count: int = received_items.get(sprint_item_name, 0)

            self.sprint_label.text = "[b]Sprint:[/b] " + (unlocked_string if sprint_item_count > 0 else locked_string)

            swing_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.SWING.value}"
            swing_item_count: int = received_items.get(swing_item_name, 0)

            self.swing_label.text = "[b]Swing:[/b] " + (unlocked_string if swing_item_count > 0 else locked_string)

            vault_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"
            vault_item_count: int = received_items.get(vault_item_name, 0)

            self.vault_label.text = "[b]Vault:[/b] " + (unlocked_string if vault_item_count > 0 else locked_string)

            wall_climb_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.WALL_CLIMB.value}"
            wall_climb_item_count: int = received_items.get(wall_climb_item_name, 0)

            wall_climb_180_turn_jump_item_name: str = f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_CLIMB_ONE_EIGHTY_TURN_JUMP.value}"
            wall_climb_180_turn_jump_item_count: int = received_items.get(wall_climb_180_turn_jump_item_name, 0)

            wall_climb_text: str = "[b]Wall Climb:[/b] "

            wall_climb_text += unlocked_string if wall_climb_item_count > 0 else locked_string
            wall_climb_text += unlocked_string if wall_climb_180_turn_jump_item_count > 0 else locked_string

            self.wall_climb_label.text = wall_climb_text

            wall_run_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.WALL_RUN.value}"
            wall_run_item_count: int = received_items.get(wall_run_item_name, 0)

            wall_run_jump_item_name: str = f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_RUN_JUMP.value}"
            wall_run_jump_item_count: int = received_items.get(wall_run_jump_item_name, 0)

            wall_run_text: str = "[b]Wall Run:[/b] "

            wall_run_text += unlocked_string if wall_run_item_count > 0 else locked_string
            wall_run_text += unlocked_string if wall_run_jump_item_count > 0 else locked_string

            self.wall_run_label.text = wall_run_text

            zipline_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.ZIPLINE.value}"
            zipline_item_count: int = received_items.get(zipline_item_name, 0)

            self.zipline_label.text = "[b]Zipline:[/b] " + (unlocked_string if zipline_item_count > 0 else locked_string)

            self.checkpoints_passed_label.text = "[b]Checkpoints Passed:[/b] 0"
            self.checkpoints_total_label.text = "[b]Checkpoints Total:[/b] 0"

            self.last_seen_level = None

            return

        if self.last_seen_level != game_state.level:
            image_path: str = f"assets/{game_state.level.value}.png"
            image_bytes: bytes = pkgutil.get_data(client_gui.__name__, image_path)

            image: CoreImage = CoreImage(io.BytesIO(image_bytes), ext="png")

            self.level_information_level_image.texture = image.texture
            self.level_information_level_image.opacity = 1.0

            self.last_seen_level = game_state.level

            self.game_state_manager.prepare_for_level_routine()

        self.level_information_title.text = game_state.level.value

        level_unlock_item: str = f"Level Unlock: {game_state.level.value}"

        is_level_in_seed: bool = False
        is_level_goal: bool = False
        is_level_unlocked: bool = False

        if game_state.level in (self.ctx.game_controller.levels + [self.ctx.game_controller.goal_level]):
            is_level_in_seed = True

        if game_state.level == self.ctx.game_controller.goal_level:
            is_level_goal = True

        if level_unlock_item in received_items and received_items[level_unlock_item] > 0:
            if is_level_goal:
                if runner_bags_obtained >= self.ctx.game_controller.option_runner_bags_required:
                    is_level_unlocked = True
            else:
                is_level_unlocked = True

        if is_level_in_seed:
            if is_level_unlocked:
                self.level_information_subtitle.text = f"[b]This level is included in this seed and is unlocked![/b]"
            else:
                self.level_information_subtitle.text = f"[b]This level is included in this seed but has not been unlocked yet.[/b]"

            if not is_level_goal:
                target_time_1_star: int = self.ctx.game_controller.target_times[game_state.level][0]
                formatted_target_time_1_star: str = f"{target_time_1_star // 60:1d}:{target_time_1_star % 60:02d}"

                target_time_2_star: int = self.ctx.game_controller.target_times[game_state.level][1]
                formatted_target_time_2_star: str = f"{target_time_2_star // 60:1d}:{target_time_2_star % 60:02d}"

                target_time_3_star: int = self.ctx.game_controller.target_times[game_state.level][2]
                formatted_target_time_3_star: str = f"{target_time_3_star // 60:1d}:{target_time_3_star % 60:02d}"

                self.target_time_1_star_label.text = f"1 Star: [color=00FA9A]{formatted_target_time_1_star}[/color] [color=888888][size=11]{self.ctx.game_controller.option_target_time_adjustment_percentage}% Base[/size][/color]"
                self.target_time_2_star_label.text = f"2 Stars: [color=00FA9A]{formatted_target_time_2_star}[/color] [color=888888][size=11]{self.ctx.game_controller.option_target_time_adjustment_percentage}% Base[/size][/color]"
                self.target_time_3_star_label.text = f"3 Stars: [color=00FA9A]{formatted_target_time_3_star}[/color] [color=888888][size=11]{self.ctx.game_controller.option_target_time_adjustment_percentage}% Base[/size][/color]"

                time_bonus_1_second_item_name: str = f"{game_state.level.value}: 1 Second Time Bonus"
                time_bonus_1_second_item_count: int = received_items.get(time_bonus_1_second_item_name, 0)

                time_bonus_3_seconds_item_name: str = f"{game_state.level.value}: 3 Seconds Time Bonus"
                time_bonus_3_seconds_item_count: int = received_items.get(time_bonus_3_seconds_item_name, 0)

                time_bonus_5_seconds_item_name: str = f"{game_state.level.value}: 5 Seconds Time Bonus"
                time_bonus_5_seconds_item_count: int = received_items.get(time_bonus_5_seconds_item_name, 0)

                self.item_time_bonus_1_second_label.text = f"1 Second Time Bonus: [color=00FA9A]{time_bonus_1_second_item_count}x[/color]"
                self.item_time_bonus_3_seconds_label.text = f"3 Seconds Time Bonus: [color=00FA9A]{time_bonus_3_seconds_item_count}x[/color]"
                self.item_time_bonus_5_seconds_label.text = f"5 Seconds Time Bonus: [color=00FA9A]{time_bonus_5_seconds_item_count}x[/color]"
            else:
                self.target_time_1_star_label.text = f"1 Star: [color=888888]X:XX[/color] [color=888888][size=11]{self.ctx.game_controller.option_target_time_adjustment_percentage}% Base[/size][/color]"
                self.target_time_2_star_label.text = f"2 Stars: [color=888888]X:XX[/color] [color=888888][size=11]{self.ctx.game_controller.option_target_time_adjustment_percentage}% Base[/size][/color]"
                self.target_time_3_star_label.text = f"3 Stars: [color=888888]X:XX[/color] [color=888888][size=11]{self.ctx.game_controller.option_target_time_adjustment_percentage}% Base[/size][/color]"

                self.item_time_bonus_1_second_label.text = "1 Second Time Bonus: [color=888888]Xx[/color]"
                self.item_time_bonus_3_seconds_label.text = "3 Seconds Time Bonus: [color=888888]Xx[/color]"
                self.item_time_bonus_5_seconds_label.text = "5 Seconds Time Bonus: [color=888888]Xx[/color]"

            self.checkpoints_passed_label.text = f"[b]Checkpoints Passed:[/b] {self.game_state_manager.get_passed_checkpoints() or 0}"
            self.checkpoints_total_label.text = f"[b]Checkpoints Total:[/b] {self.game_state_manager.get_total_checkpoints() or 0}"
        else:
            self.level_information_subtitle.text = "[b]This level is not included in this seed.[/b]"

            self.target_time_1_star_label.text = f"1 Star: [color=888888]X:XX[/color] [color=888888][size=11]{self.ctx.game_controller.option_target_time_adjustment_percentage}% Base[/size][/color]"
            self.target_time_2_star_label.text = f"2 Stars: [color=888888]X:XX[/color] [color=888888][size=11]{self.ctx.game_controller.option_target_time_adjustment_percentage}% Base[/size][/color]"
            self.target_time_3_star_label.text = f"3 Stars: [color=888888]X:XX[/color] [color=888888][size=11]{self.ctx.game_controller.option_target_time_adjustment_percentage}% Base[/size][/color]"

            self.item_time_bonus_1_second_label.text = "1 Second Time Bonus: [color=888888]Xx[/color]"
            self.item_time_bonus_3_seconds_label.text = "3 Seconds Time Bonus: [color=888888]Xx[/color]"
            self.item_time_bonus_5_seconds_label.text = "5 Seconds Time Bonus: [color=888888]Xx[/color]"

            self.checkpoints_passed_label.text = "[b]Checkpoints Passed:[/b] 0"
            self.checkpoints_total_label.text = "[b]Checkpoints Total:[/b] 0"

        unlocked_string: str = "[color=00FA9A]+[/color] "
        locked_string: str = "[color=FF4C4C]-[/color] "

        one_eighty_turn_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.ONE_EIGHTY_TURN.value}"
        one_eighty_turn_item_count: int = received_items.get(one_eighty_turn_item_name, 0)

        self.one_eighty_turn_label.text = "[b]180 Turn:[/b] " + (unlocked_string if one_eighty_turn_item_count > 0 else locked_string)

        airborne_one_eighty_turn_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.AIRBORNE_ONE_EIGHTY_TURN.value}"
        airborne_one_eighty_turn_item_count: int = received_items.get(airborne_one_eighty_turn_item_name, 0)

        self.airborne_one_eighty_turn_label.text = "[b]Airborne 180 Turn:[/b] " + (unlocked_string if airborne_one_eighty_turn_item_count > 0 else locked_string)

        balance_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.BALANCE.value}"
        balance_item_count: int = received_items.get(balance_item_name, 0)

        self.balance_label.text = "[b]Balance:[/b] " + (unlocked_string if balance_item_count > 0 else locked_string)

        barge_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.BARGE.value}"
        barge_item_count: int = received_items.get(barge_item_name, 0)

        self.barge_label.text = "[b]Barge:[/b] " + (unlocked_string if barge_item_count > 0 else locked_string)

        climb_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.CLIMB.value}"
        climb_item_count: int = received_items.get(climb_item_name, 0)

        self.climb_label.text = "[b]Climb:[/b] " + (unlocked_string if climb_item_count > 0 else locked_string)

        coil_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.COIL.value}"
        coil_item_count: int = received_items.get(coil_item_name, 0)

        self.coil_label.text = "[b]Coil:[/b] " + (unlocked_string if coil_item_count > 0 else locked_string)

        dodge_jump_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.DODGE_JUMP.value}"
        dodge_jump_item_count: int = received_items.get(dodge_jump_item_name, 0)

        self.dodge_jump_label.text = "[b]Dodge Jump:[/b] " + (unlocked_string if dodge_jump_item_count > 0 else locked_string)

        grab_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.GRAB.value}"
        grab_item_count: int = received_items.get(grab_item_name, 0)

        grab_jump_item_name: str = f"Ability Extension Unlock: {MirrorsEdgeAbilities.GRAB_JUMP.value}"
        grab_jump_item_count: int = received_items.get(grab_jump_item_name, 0)

        grab_text: str = "[b]Grab:[/b] "

        grab_text += unlocked_string if grab_item_count > 0 else locked_string
        grab_text += unlocked_string if grab_jump_item_count > 0 else locked_string

        self.grab_label.text = grab_text

        melee_attack_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.MELEE_ATTACK.value}"
        melee_attack_item_count: int = received_items.get(melee_attack_item_name, 0)

        self.melee_attack_label.text = "[b]Melee Attack:[/b] " + (unlocked_string if melee_attack_item_count > 0 else locked_string)

        springboard_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.SPRINGBOARD.value}"
        springboard_item_count: int = received_items.get(springboard_item_name, 0)

        self.springboard_label.text = "[b]Springboard:[/b] " + (unlocked_string if springboard_item_count > 0 else locked_string)

        sprint_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.SPRINT.value}"
        sprint_item_count: int = received_items.get(sprint_item_name, 0)

        self.sprint_label.text = "[b]Sprint:[/b] " + (unlocked_string if sprint_item_count > 0 else locked_string)

        swing_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.SWING.value}"
        swing_item_count: int = received_items.get(swing_item_name, 0)

        self.swing_label.text = "[b]Swing:[/b] " + (unlocked_string if swing_item_count > 0 else locked_string)

        vault_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.VAULT.value}"
        vault_item_count: int = received_items.get(vault_item_name, 0)

        self.vault_label.text = "[b]Vault:[/b] " + (unlocked_string if vault_item_count > 0 else locked_string)

        wall_climb_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.WALL_CLIMB.value}"
        wall_climb_item_count: int = received_items.get(wall_climb_item_name, 0)

        wall_climb_180_turn_jump_item_name: str = f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_CLIMB_ONE_EIGHTY_TURN_JUMP.value}"
        wall_climb_180_turn_jump_item_count: int = received_items.get(wall_climb_180_turn_jump_item_name, 0)

        wall_climb_text: str = "[b]Wall Climb:[/b] "

        wall_climb_text += unlocked_string if wall_climb_item_count > 0 else locked_string
        wall_climb_text += unlocked_string if wall_climb_180_turn_jump_item_count > 0 else locked_string

        self.wall_climb_label.text = wall_climb_text

        wall_run_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.WALL_RUN.value}"
        wall_run_item_count: int = received_items.get(wall_run_item_name, 0)

        wall_run_jump_item_name: str = f"Ability Extension Unlock: {MirrorsEdgeAbilities.WALL_RUN_JUMP.value}"
        wall_run_jump_item_count: int = received_items.get(wall_run_jump_item_name, 0)

        wall_run_text: str = "[b]Wall Run:[/b] "

        wall_run_text += unlocked_string if wall_run_item_count > 0 else locked_string
        wall_run_text += unlocked_string if wall_run_jump_item_count > 0 else locked_string

        self.wall_run_label.text = wall_run_text

        zipline_item_name: str = f"Ability Unlock: {MirrorsEdgeAbilities.ZIPLINE.value}"
        zipline_item_count: int = received_items.get(zipline_item_name, 0)

        self.zipline_label.text = "[b]Zipline:[/b] " + (unlocked_string if zipline_item_count > 0 else locked_string)


class MirrorsEdgeLevelsLayout(BoxLayout):
    ctx: MirrorsEdgeContext

    level_label: Label
    level_images: List[Image]

    level_data: Dict[MirrorsEdgeLevels, Dict[str, Any]]

    def __init__(self, ctx: MirrorsEdgeContext) -> None:
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

        levels: List[MirrorsEdgeLevels] = self.ctx.game_controller.levels[:]

        if self.ctx.game_controller.goal_level is not None:
            levels.append(self.ctx.game_controller.goal_level)

        level: MirrorsEdgeLevels
        for level in levels:
            self.level_data[level] = {
                "image_path": f"assets/{level.value}.png",
                "unlock_item": f"Level Unlock: {level.value}",
                "is_goal": False,
            }

            if self.ctx.game_controller.goal_level is not None:
                if level == self.ctx.game_controller.goal_level:
                    self.level_data[level]["is_goal"] = True

        grid_layout: GridLayout = GridLayout(
            cols=4,
            spacing=8,
            padding=0,
            size_hint_y=None,
        )

        grid_layout.bind(minimum_height=grid_layout.setter("height"))

        level: MirrorsEdgeLevels
        data: Dict[str, Any]
        for level, data in self.level_data.items():
            image_bytes: bytes = pkgutil.get_data(client_gui.__name__, data["image_path"])
            image: CoreImage = CoreImage(io.BytesIO(image_bytes), ext="png")

            level_image = Image(
                texture=image.texture,
                size=(173, 36),
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

        level: MirrorsEdgeLevels
        data: Dict[str, Any]
        for i, (level, data) in enumerate(self.level_data.items()):
            is_unlocked: bool = False

            if data["unlock_item"] in received_items and received_items[data["unlock_item"]] > 0:
                if data["is_goal"]:
                    runner_bags_required: int = self.ctx.game_controller.option_runner_bags_required
                    runner_bags_obtained: int = received_items.get("Runner Bag", 0)

                    if runner_bags_obtained >= runner_bags_required:
                        is_unlocked = True
                else:
                    is_unlocked = True

            self.level_images[i].opacity = 1.0 if is_unlocked else 0.4


class MirrorsEdgeContent(ScrollView):
    ctx: MirrorsEdgeContext

    layout: BoxLayout

    layout_game_information: MirrorsEdgeGameInformationLayout
    layout_levels: MirrorsEdgeLevelsLayout

    timer: Clock

    def __init__(self, ctx: MirrorsEdgeContext) -> None:
        super().__init__()

        self.ctx = ctx

        self.layout = BoxLayout(orientation="vertical", size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter("height"))

        self.layout_game_information = MirrorsEdgeGameInformationLayout(ctx=self.ctx)
        self.layout.add_widget(self.layout_game_information)

        self.layout_levels = MirrorsEdgeLevelsLayout(ctx=self.ctx)
        self.layout.add_widget(self.layout_levels)

        self.add_widget(self.layout)

        self.timer = Clock.schedule_interval(self.update, 1.0 / 10.0)

    def update(self, *_) -> None:
        try:
            self.layout_game_information.update()
            self.layout_levels.update()
        except Exception:
            import traceback

            with open("mirrors_edge_errors.log", "a") as f:
                f.write(traceback.format_exc() + "\n\n")


class MirrorsEdgeTabLayout(BoxLayout):
    ctx: MirrorsEdgeContext

    layout_content: BoxLayout
    layout_content_mirrors_edge: MirrorsEdgeContent

    layout_not_connected: NotConnectedLayout

    def __init__(self, ctx: MirrorsEdgeContext) -> None:
        super().__init__(orientation="vertical", padding="8dp")

        self.bind(minimum_height=self.setter("height"))

        self.ctx = ctx

        self.layout_not_connected = NotConnectedLayout(self.ctx)
        self.add_widget(self.layout_not_connected)

        self.layout_content = BoxLayout(orientation="horizontal", spacing="16dp", padding=["8dp", "0dp"])
        self.add_widget(self.layout_content)

        self.update()

    def update(self) -> None:
        if self.ctx.game_controller.target_times is None:
            self.layout_not_connected.show()

            if hasattr(self, "layout_content_mirrors_edge"):
                self.layout_content_mirrors_edge.timer.cancel()

            self.layout_content.clear_widgets()

            return

        self.layout_not_connected.hide()

        if not len(self.layout_content.children):
            self.layout_content_mirrors_edge = MirrorsEdgeContent(ctx=self.ctx)
            self.layout_content.add_widget(self.layout_content_mirrors_edge)

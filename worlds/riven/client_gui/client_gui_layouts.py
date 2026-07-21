from typing import Dict, List

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

from ..client import RivenContext

from ..enums import RivenAPGoals, RivenItems

from ..game_state_manager import GameStateManager, GameState

from .. import client_gui


class NotConnectedLayout(BoxLayout):
    ctx: RivenContext

    def __init__(self, ctx: RivenContext) -> None:
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


class RivenPuzzleSolutionsLayout(BoxLayout):
    ctx: RivenContext

    game_state_manager: GameStateManager

    puzzle_solutions_label: Label

    bolu_off: CoreImage
    bolu_on: CoreImage

    bolu_label: Label
    bolu_sub_label: Label
    bolu_images: List[Image]

    animal_0: CoreImage
    animal_3: CoreImage
    animal_10: CoreImage
    animal_15: CoreImage
    animal_17: CoreImage
    animal_21: CoreImage

    animal_label: Label
    animal_images: List[Image]

    slider_notch: CoreImage
    slider_purple: CoreImage
    slider_blue: CoreImage
    slider_green: CoreImage
    slider_orange: CoreImage
    slider_red: CoreImage

    sliders_label: Label
    sliders_images: List[Image]

    elevator_1: CoreImage
    elevator_2: CoreImage
    elevator_3: CoreImage

    elevator_label: Label
    elevator_images: List[Image]

    telescope_1: CoreImage
    telescope_2: CoreImage
    telescope_3: CoreImage
    telescope_4: CoreImage
    telescope_5: CoreImage
    telescope_6: CoreImage
    telescope_7: CoreImage
    telescope_8: CoreImage
    telescope_9: CoreImage
    telescope_10: CoreImage

    telescope_label: Label
    telescope_images: List[Image]

    def __init__(self, ctx: RivenContext) -> None:
        super().__init__(orientation="vertical", size_hint_y=None, height="40dp", spacing="8dp")

        self.bind(minimum_height=self.setter("height"))

        self.ctx = ctx

        self.game_state_manager = GameStateManager()

        self.puzzle_solutions_label = Label(
            text=f"[b]Randomized Puzzle Solutions[/b]",
            markup=True,
            font_size="32dp",
            size_hint_y=None,
            height="70dp",
            halign="left",
            valign="bottom",
        )

        self.puzzle_solutions_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.add_widget(self.puzzle_solutions_label)

        self.bolu_off = CoreImage(io.BytesIO(pkgutil.get_data(client_gui.__name__, "assets/bolu_off.png")), ext="png")
        self.bolu_on = CoreImage(io.BytesIO(pkgutil.get_data(client_gui.__name__, "assets/bolu_on.png")), ext="png")

        self.bolu_label = Label(
            text=f"[b]Bolu Sticks Solution[/b]",
            markup=True,
            font_size="24dp",
            size_hint_y=None,
            height="54dp",
            halign="left",
            valign="bottom",
        )

        self.bolu_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.add_widget(self.bolu_label)

        self.bolu_sub_label = Label(
            text=f"Starting from the one closest to the window; clockwise order",
            font_size="12dp",
            size_hint_y=None,
            height="14dp",
            halign="left",
            valign="bottom",
        )

        self.bolu_sub_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.add_widget(self.bolu_sub_label)

        bolu_grid_layout: GridLayout = GridLayout(
            cols=9,
            spacing=16,
            padding=0,
            size_hint_y=None,
        )

        bolu_grid_layout.bind(minimum_height=bolu_grid_layout.setter("height"))

        self.bolu_images = list()

        for _ in range(9):
            bolu_image: Image = Image(
                texture=self.bolu_off.texture,
                size=(43, 93),
                size_hint=(None, None),
                allow_stretch=True,
                opacity=0.4
            )

            self.bolu_images.append(bolu_image)
            bolu_grid_layout.add_widget(bolu_image)

        self.add_widget(bolu_grid_layout)

        self.animal_0 = CoreImage(io.BytesIO(pkgutil.get_data(client_gui.__name__, "assets/at_0.png")), ext="png")
        self.animal_3 = CoreImage(io.BytesIO(pkgutil.get_data(client_gui.__name__, "assets/at_3.png")), ext="png")
        self.animal_10 = CoreImage(io.BytesIO(pkgutil.get_data(client_gui.__name__, "assets/at_10.png")), ext="png")
        self.animal_15 = CoreImage(io.BytesIO(pkgutil.get_data(client_gui.__name__, "assets/at_15.png")), ext="png")
        self.animal_17 = CoreImage(io.BytesIO(pkgutil.get_data(client_gui.__name__, "assets/at_17.png")), ext="png")
        self.animal_21 = CoreImage(io.BytesIO(pkgutil.get_data(client_gui.__name__, "assets/at_21.png")), ext="png")

        self.animal_label = Label(
            text=f"[b]Animal Circle Solution[/b]",
            markup=True,
            font_size="24dp",
            size_hint_y=None,
            height="54dp",
            halign="left",
            valign="bottom",
        )

        self.animal_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.add_widget(self.animal_label)

        animal_grid_layout: GridLayout = GridLayout(
            cols=6,
            spacing=16,
            padding=0,
            size_hint_y=None,
        )

        animal_grid_layout.bind(minimum_height=animal_grid_layout.setter("height"))

        self.animal_images = list()

        for _ in range(6):
            animal_image: Image = Image(
                texture=self.animal_0.texture,
                size=(75, 75),
                size_hint=(None, None),
                allow_stretch=True,
                opacity=0.2
            )

            self.animal_images.append(animal_image)
            animal_grid_layout.add_widget(animal_image)

        self.add_widget(animal_grid_layout)

        self.slider_notch = CoreImage(io.BytesIO(pkgutil.get_data(client_gui.__name__, "assets/slider_notch.png")), ext="png")
        self.slider_purple = CoreImage(io.BytesIO(pkgutil.get_data(client_gui.__name__, "assets/slider_purple.png")), ext="png")
        self.slider_blue = CoreImage(io.BytesIO(pkgutil.get_data(client_gui.__name__, "assets/slider_blue.png")), ext="png")
        self.slider_green = CoreImage(io.BytesIO(pkgutil.get_data(client_gui.__name__, "assets/slider_green.png")), ext="png")
        self.slider_orange = CoreImage(io.BytesIO(pkgutil.get_data(client_gui.__name__, "assets/slider_orange.png")), ext="png")
        self.slider_red = CoreImage(io.BytesIO(pkgutil.get_data(client_gui.__name__, "assets/slider_red.png")), ext="png")

        self.sliders_label = Label(
            text=f"[b]Golden Dome Sliders Solution[/b]",
            markup=True,
            font_size="24dp",
            size_hint_y=None,
            height="54dp",
            halign="left",
            valign="bottom",
        )

        self.sliders_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.add_widget(self.sliders_label)

        sliders_grid_layout: GridLayout = GridLayout(
            cols=26,
            spacing=4,
            padding=0,
            size_hint_y=None,
        )

        sliders_grid_layout.bind(minimum_height=sliders_grid_layout.setter("height"))

        self.sliders_images = list()

        for _ in range(26):
            slider_image: Image = Image(
                texture=self.slider_notch.texture,
                size=(23, 77),
                size_hint=(None, None),
                allow_stretch=True,
                opacity=0.2
            )

            self.sliders_images.append(slider_image)
            sliders_grid_layout.add_widget(slider_image)

        self.add_widget(sliders_grid_layout)

        if self.ctx.game_controller.option_goal == RivenAPGoals.GOOD_ENDING:
            self.elevator_1 = CoreImage(io.BytesIO(pkgutil.get_data(client_gui.__name__, "assets/elevator_1.png")), ext="png")
            self.elevator_2 = CoreImage(io.BytesIO(pkgutil.get_data(client_gui.__name__, "assets/elevator_2.png")), ext="png")
            self.elevator_3 = CoreImage(io.BytesIO(pkgutil.get_data(client_gui.__name__, "assets/elevator_3.png")), ext="png")

            self.elevator_label = Label(
                text=f"[b]Prison Elevator Solution[/b]",
                markup=True,
                font_size="24dp",
                size_hint_y=None,
                height="54dp",
                halign="left",
                valign="bottom",
            )

            self.elevator_label.bind(size=lambda label, size: setattr(label, "text_size", size))

            self.add_widget(self.elevator_label)

            elevator_grid_layout: GridLayout = GridLayout(
                cols=5,
                spacing=16,
                padding=0,
                size_hint_y=None,
            )

            elevator_grid_layout.bind(minimum_height=elevator_grid_layout.setter("height"))

            self.elevator_images = list()

            for _ in range(5):
                elevator_image: Image = Image(
                    texture=self.elevator_1.texture,
                    size=(109, 174),
                    size_hint=(None, None),
                    allow_stretch=True,
                    opacity=0.2
                )

                self.elevator_images.append(elevator_image)
                elevator_grid_layout.add_widget(elevator_image)

            self.add_widget(elevator_grid_layout)

        self.telescope_1 = CoreImage(io.BytesIO(pkgutil.get_data(client_gui.__name__, "assets/telescope_1.png")), ext="png")
        self.telescope_2 = CoreImage(io.BytesIO(pkgutil.get_data(client_gui.__name__, "assets/telescope_2.png")), ext="png")
        self.telescope_3 = CoreImage(io.BytesIO(pkgutil.get_data(client_gui.__name__, "assets/telescope_3.png")), ext="png")
        self.telescope_4 = CoreImage(io.BytesIO(pkgutil.get_data(client_gui.__name__, "assets/telescope_4.png")), ext="png")
        self.telescope_5 = CoreImage(io.BytesIO(pkgutil.get_data(client_gui.__name__, "assets/telescope_5.png")), ext="png")
        self.telescope_6 = CoreImage(io.BytesIO(pkgutil.get_data(client_gui.__name__, "assets/telescope_6.png")), ext="png")
        self.telescope_7 = CoreImage(io.BytesIO(pkgutil.get_data(client_gui.__name__, "assets/telescope_7.png")), ext="png")
        self.telescope_8 = CoreImage(io.BytesIO(pkgutil.get_data(client_gui.__name__, "assets/telescope_8.png")), ext="png")
        self.telescope_9 = CoreImage(io.BytesIO(pkgutil.get_data(client_gui.__name__, "assets/telescope_9.png")), ext="png")
        self.telescope_10 = CoreImage(io.BytesIO(pkgutil.get_data(client_gui.__name__, "assets/telescope_10.png")), ext="png")

        self.telescope_label = Label(
            text=f"[b]Star Fissure Telescope Solution[/b]",
            markup=True,
            font_size="24dp",
            size_hint_y=None,
            height="54dp",
            halign="left",
            valign="bottom",
        )

        self.telescope_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.add_widget(self.telescope_label)

        telescope_grid_layout: GridLayout = GridLayout(
            cols=10,
            spacing=8,
            padding=0,
            size_hint_y=None,
        )

        telescope_grid_layout.bind(minimum_height=telescope_grid_layout.setter("height"))

        self.telescope_images = list()

        for _ in range(10):
            telescope_image: Image = Image(
                texture=self.telescope_1.texture,
                size=(60, 60),
                size_hint=(None, None),
                allow_stretch=True,
                opacity=0.2
            )

            self.telescope_images.append(telescope_image)
            telescope_grid_layout.add_widget(telescope_image)

        self.add_widget(telescope_grid_layout)

    def update(self) -> None:
        received_items: Dict[RivenItems, int] = dict()

        network_item: NetUtils.NetworkItem
        for network_item in self.ctx.items_received:
            if network_item.item in self.ctx.id_to_items:
                item: RivenItems = self.ctx.id_to_items[network_item.item]

                if item not in received_items:
                    received_items[item] = 0

                received_items[item] += 1

        game_state: GameState = GameState(is_valid=False)

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

        if game_state.is_valid and received_items.get(RivenItems.SOLUTION_BOLU_STICKS, 0) > 0:
            solution: List[int] = [
                game_state.light_post_solution_1,
                game_state.light_post_solution_2,
                game_state.light_post_solution_3,
            ]

            if None not in solution:
                i: int
                image: Image
                for i, image in enumerate(self.bolu_images):
                    if i in solution:
                        image.texture = self.bolu_on.texture
                        image.opacity = 1.0
                    else:
                        image.texture = self.bolu_off.texture
                        image.opacity = 1.0
        else:
            image: Image
            for image in self.bolu_images:
                image.texture = self.bolu_off.texture
                image.opacity = 0.4

        if game_state.is_valid and received_items.get(RivenItems.SOLUTION_ANIMAL_CIRCLE, 0) > 0:
            solution: List[int] = [
                game_state.animal_totem_solution_one,
                game_state.animal_totem_solution_two,
                game_state.animal_totem_solution_three,
                game_state.animal_totem_solution_four,
                game_state.animal_totem_solution_five,
                game_state.animal_totem_solution_six,
            ]

            if None not in solution:
                i: int
                solution_component: int
                for i, solution_component in enumerate(solution):
                    if solution_component == 0:
                        self.animal_images[i].texture = self.animal_0.texture

                    elif solution_component == 3:
                        self.animal_images[i].texture = self.animal_3.texture
                    elif solution_component == 10:
                        self.animal_images[i].texture = self.animal_10.texture
                    elif solution_component == 15:
                        self.animal_images[i].texture = self.animal_15.texture
                    elif solution_component == 17:
                        self.animal_images[i].texture = self.animal_17.texture
                    elif solution_component == 21:
                        self.animal_images[i].texture = self.animal_21.texture

                    self.animal_images[i].opacity = 1.0
        else:
            image: Image
            for image in self.animal_images:
                image.texture = self.animal_0.texture
                image.opacity = 0.2

        if game_state.is_valid and received_items.get(RivenItems.SOLUTION_GOLDEN_DOME_SLIDERS, 0) > 0:
            solution: List[int] = [
                game_state.slider_solution_violet,
                game_state.slider_solution_blue,
                game_state.slider_solution_green,
                game_state.slider_solution_orange,
                game_state.slider_solution_red,
            ]

            if None not in solution:
                for i in range(26):
                    reverse_i: int = abs(i - 25)

                    if reverse_i in solution:
                        if solution[0] == reverse_i:
                            self.sliders_images[i].texture = self.slider_purple.texture
                        elif solution[1] == reverse_i:
                            self.sliders_images[i].texture = self.slider_blue.texture
                        elif solution[2] == reverse_i:
                            self.sliders_images[i].texture = self.slider_green.texture
                        elif solution[3] == reverse_i:
                            self.sliders_images[i].texture = self.slider_orange.texture
                        elif solution[4] == reverse_i:
                            self.sliders_images[i].texture = self.slider_red.texture
                    else:
                        self.sliders_images[i].texture = self.slider_notch.texture

                    self.sliders_images[i].opacity = 1.0
        else:
            image: Image
            for image in self.sliders_images:
                image.texture = self.slider_notch.texture
                image.opacity = 0.2

        if self.ctx.game_controller.option_goal == RivenAPGoals.GOOD_ENDING:
            if game_state.is_valid and received_items.get(RivenItems.SOLUTION_PRISON_ELEVATOR, 0) > 0:
                solution: List[int] = [
                    game_state.elevator_solution_one,
                    game_state.elevator_solution_two,
                    game_state.elevator_solution_three,
                    game_state.elevator_solution_four,
                    game_state.elevator_solution_five,
                ]

                if None not in solution:
                    i: int
                    solution_component: int
                    for i, solution_component in enumerate(solution):
                        if solution_component == 1:
                            self.elevator_images[i].texture = self.elevator_1.texture
                        elif solution_component == 2:
                            self.elevator_images[i].texture = self.elevator_2.texture
                        elif solution_component == 3:
                            self.elevator_images[i].texture = self.elevator_3.texture

                        self.elevator_images[i].opacity = 1.0
            else:
                image: Image
                for image in self.elevator_images:
                    image.texture = self.elevator_1.texture
                    image.opacity = 0.2

        progressive_telescope_solution_count: int = received_items.get(RivenItems.SOLUTION_STAR_FISSURE_TELESCOPE, 0)

        if progressive_telescope_solution_count > 0:
            solution: List[int] = [
                game_state.telescope_solution_one,
                game_state.telescope_solution_two,
                game_state.telescope_solution_three,
                game_state.telescope_solution_four,
                game_state.telescope_solution_five,
                game_state.telescope_solution_six,
                game_state.telescope_solution_seven,
                game_state.telescope_solution_eight,
                game_state.telescope_solution_nine,
                game_state.telescope_solution_ten,
            ]

            if None not in solution:
                i: int
                solution_component: int
                for i, solution_component in enumerate(solution):
                    if i + 1 <= progressive_telescope_solution_count:
                        if solution_component == 1:
                            self.telescope_images[i].texture = self.telescope_1.texture
                        elif solution_component == 2:
                            self.telescope_images[i].texture = self.telescope_2.texture
                        elif solution_component == 3:
                            self.telescope_images[i].texture = self.telescope_3.texture
                        elif solution_component == 4:
                            self.telescope_images[i].texture = self.telescope_4.texture
                        elif solution_component == 5:
                            self.telescope_images[i].texture = self.telescope_5.texture
                        elif solution_component == 6:
                            self.telescope_images[i].texture = self.telescope_6.texture
                        elif solution_component == 7:
                            self.telescope_images[i].texture = self.telescope_7.texture
                        elif solution_component == 8:
                            self.telescope_images[i].texture = self.telescope_8.texture
                        elif solution_component == 9:
                            self.telescope_images[i].texture = self.telescope_9.texture
                        elif solution_component == 10:
                            self.telescope_images[i].texture = self.telescope_10.texture

                        self.telescope_images[i].opacity = 1.0
                    else:
                        self.telescope_images[i].texture = self.telescope_1.texture
                        self.telescope_images[i].opacity = 0.2
        else:
            image: Image
            for image in self.telescope_images:
                image.texture = self.telescope_1.texture
                image.opacity = 0.2


class RivenReferenceLayout(BoxLayout):
    ctx: RivenContext

    def __init__(self, ctx: RivenContext) -> None:
        super().__init__(orientation="vertical", size_hint_y=None, height="40dp", spacing="8dp")

        self.bind(minimum_height=self.setter("height"))

        self.ctx = ctx

        reference_label = Label(
            text=f"[b]Reference[/b]",
            markup=True,
            font_size="32dp",
            size_hint_y=None,
            height="70dp",
            halign="left",
            valign="bottom",
        )

        reference_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.add_widget(reference_label)

        symbols_grid_layout: GridLayout = GridLayout(
            cols=5,
            spacing=16,
            padding=0,
            size_hint_y=None,
        )

        symbol_temple_layout: BoxLayout = BoxLayout(orientation="vertical", size_hint_y=None, height="100dp", size_hint_x=None, width="64dp", spacing="8dp")

        symbol_temple_image: Image = Image(
            texture=CoreImage(io.BytesIO(pkgutil.get_data(client_gui.__name__, "assets/ref_symbol_temple.png")), ext="png").texture,
            size=(64, 64),
            size_hint=(None, None),
            allow_stretch=True,
            opacity=1.0,
        )

        symbol_temple_layout.add_widget(symbol_temple_image)

        symbol_temple_label: Label = Label(
            text=f"[b]Temple[/b]",
            markup=True,
            font_size="14dp",
            size_hint_y=None,
            height="16dp",
            size_hint_x=None,
            width="64dp",
            halign="center",
            valign="bottom",
        )

        symbol_temple_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        symbol_temple_layout.add_widget(symbol_temple_label)

        symbols_grid_layout.add_widget(symbol_temple_layout)

        symbol_jungle_layout: BoxLayout = BoxLayout(orientation="vertical", size_hint_y=None, height="100dp", size_hint_x=None, width="64dp", spacing="8dp")

        symbol_jungle_image: Image = Image(
            texture=CoreImage(io.BytesIO(pkgutil.get_data(client_gui.__name__, "assets/ref_symbol_jungle.png")), ext="png").texture,
            size=(64, 64),
            size_hint=(None, None),
            allow_stretch=True,
            opacity=1.0,
        )

        symbol_jungle_layout.add_widget(symbol_jungle_image)

        symbol_jungle_label: Label = Label(
            text=f"[b]Jungle[/b]",
            markup=True,
            font_size="14dp",
            size_hint_y=None,
            height="16dp",
            size_hint_x=None,
            width="64dp",
            halign="center",
            valign="bottom",
        )

        symbol_jungle_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        symbol_jungle_layout.add_widget(symbol_jungle_label)

        symbols_grid_layout.add_widget(symbol_jungle_layout)
        
        symbol_boiler_layout: BoxLayout = BoxLayout(orientation="vertical", size_hint_y=None, height="100dp", size_hint_x=None, width="64dp", spacing="8dp")

        symbol_boiler_image: Image = Image(
            texture=CoreImage(io.BytesIO(pkgutil.get_data(client_gui.__name__, "assets/ref_symbol_boiler.png")), ext="png").texture,
            size=(64, 64),
            size_hint=(None, None),
            allow_stretch=True,
            opacity=1.0,
        )

        symbol_boiler_layout.add_widget(symbol_boiler_image)

        symbol_boiler_label: Label = Label(
            text=f"[b]Boiler[/b]",
            markup=True,
            font_size="14dp",
            size_hint_y=None,
            height="16dp",
            size_hint_x=None,
            width="64dp",
            halign="center",
            valign="bottom",
        )

        symbol_boiler_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        symbol_boiler_layout.add_widget(symbol_boiler_label)

        symbols_grid_layout.add_widget(symbol_boiler_layout)
        
        symbol_survey_layout: BoxLayout = BoxLayout(orientation="vertical", size_hint_y=None, height="100dp", size_hint_x=None, width="64dp", spacing="8dp")

        symbol_survey_image: Image = Image(
            texture=CoreImage(io.BytesIO(pkgutil.get_data(client_gui.__name__, "assets/ref_symbol_survey.png")), ext="png").texture,
            size=(64, 64),
            size_hint=(None, None),
            allow_stretch=True,
            opacity=1.0,
        )

        symbol_survey_layout.add_widget(symbol_survey_image)

        symbol_survey_label: Label = Label(
            text=f"[b]Survey[/b]",
            markup=True,
            font_size="14dp",
            size_hint_y=None,
            height="16dp",
            size_hint_x=None,
            width="64dp",
            halign="center",
            valign="bottom",
        )

        symbol_survey_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        symbol_survey_layout.add_widget(symbol_survey_label)

        symbols_grid_layout.add_widget(symbol_survey_layout)

        symbol_prison_layout: BoxLayout = BoxLayout(orientation="vertical", size_hint_y=None, height="100dp", size_hint_x=None, width="64dp", spacing="8dp")

        symbol_prison_image: Image = Image(
            texture=CoreImage(io.BytesIO(pkgutil.get_data(client_gui.__name__, "assets/ref_symbol_prison.png")), ext="png").texture,
            size=(64, 64),
            size_hint=(None, None),
            allow_stretch=True,
            opacity=1.0,
        )

        symbol_prison_layout.add_widget(symbol_prison_image)

        symbol_prison_label: Label = Label(
            text=f"[b]Prison[/b]",
            markup=True,
            font_size="14dp",
            size_hint_y=None,
            height="16dp",
            size_hint_x=None,
            width="64dp",
            halign="center",
            valign="bottom",
        )

        symbol_prison_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        symbol_prison_layout.add_widget(symbol_prison_label)

        symbols_grid_layout.add_widget(symbol_prison_layout)

        self.add_widget(symbols_grid_layout)

        recall_label = Label(
            text=f"[b]Recall a Specific Moiety Code[/b]",
            markup=True,
            font_size="24dp",
            size_hint_y=None,
            height="54dp",
            halign="left",
            valign="bottom",
        )

        recall_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.add_widget(recall_label)

        recall_grid_layout: GridLayout = GridLayout(
            cols=5,
            spacing=16,
            padding=0,
            size_hint_y=None,
            height="64dp",
        )

        fish_image: Image = Image(
            texture=CoreImage(io.BytesIO(pkgutil.get_data(client_gui.__name__, "assets/at_15.png")), ext="png").texture,
            size=(64, 64),
            size_hint=(None, None),
            allow_stretch=True,
            opacity=1.0,
        )

        recall_grid_layout.add_widget(fish_image)

        beetle_image: Image = Image(
            texture=CoreImage(io.BytesIO(pkgutil.get_data(client_gui.__name__, "assets/at_10.png")), ext="png").texture,
            size=(64, 64),
            size_hint=(None, None),
            allow_stretch=True,
            opacity=1.0,
        )

        recall_grid_layout.add_widget(beetle_image)

        ytram_image: Image = Image(
            texture=CoreImage(io.BytesIO(pkgutil.get_data(client_gui.__name__, "assets/at_17.png")), ext="png").texture,
            size=(64, 64),
            size_hint=(None, None),
            allow_stretch=True,
            opacity=1.0,
        )

        recall_grid_layout.add_widget(ytram_image)

        sunner_image: Image = Image(
            texture=CoreImage(io.BytesIO(pkgutil.get_data(client_gui.__name__, "assets/at_3.png")), ext="png").texture,
            size=(64, 64),
            size_hint=(None, None),
            allow_stretch=True,
            opacity=1.0,
        )

        recall_grid_layout.add_widget(sunner_image)

        wahrk_image: Image = Image(
            texture=CoreImage(io.BytesIO(pkgutil.get_data(client_gui.__name__, "assets/at_0.png")), ext="png").texture,
            size=(64, 64),
            size_hint=(None, None),
            allow_stretch=True,
            opacity=1.0,
        )

        recall_grid_layout.add_widget(wahrk_image)

        self.add_widget(recall_grid_layout)

        elevator_label = Label(
            text=f"[b]Survey Island Plateau Elevator[/b]",
            markup=True,
            font_size="24dp",
            size_hint_y=None,
            height="54dp",
            halign="left",
            valign="bottom",
        )

        elevator_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.add_widget(elevator_label)

        elevator_image: Image = Image(
            texture=CoreImage(io.BytesIO(pkgutil.get_data(client_gui.__name__, "assets/ref_elevator.png")), ext="png").texture,
            size=(128, 128),
            size_hint=(None, None),
            allow_stretch=True,
            opacity=1.0,
        )

        self.add_widget(elevator_image)

        waffle_label = Label(
            text=f"[b]Golden Dome Waffle Iron Marbles[/b]",
            markup=True,
            font_size="24dp",
            size_hint_y=None,
            height="54dp",
            halign="left",
            valign="bottom",
        )

        waffle_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.add_widget(waffle_label)

        waffle_image: Image = Image(
            texture=CoreImage(io.BytesIO(pkgutil.get_data(client_gui.__name__, "assets/ref_waffle.png")), ext="png").texture,
            size=(256, 256),
            size_hint=(None, None),
            allow_stretch=True,
            opacity=1.0,
        )

        self.add_widget(waffle_image)


class RivenContent(ScrollView):
    ctx: RivenContext

    layout: BoxLayout

    layout_puzzle_solutions: RivenPuzzleSolutionsLayout
    layout_reference: RivenReferenceLayout

    timer: Clock

    def __init__(self, ctx: RivenContext) -> None:
        super().__init__()

        self.ctx = ctx

        self.layout = BoxLayout(orientation="vertical", size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter("height"))

        self.layout_puzzle_solutions = RivenPuzzleSolutionsLayout(ctx=self.ctx)
        self.layout.add_widget(self.layout_puzzle_solutions)

        self.layout_reference = RivenReferenceLayout(ctx=self.ctx)
        self.layout.add_widget(self.layout_reference)

        self.add_widget(self.layout)

        self.timer = Clock.schedule_interval(self.update, 1.0 / 10.0)

    def update(self, *_) -> None:
        try:
            self.layout_puzzle_solutions.update()
        except Exception:
            import traceback

            with open("riven_errors.log", "a") as f:
                f.write(traceback.format_exc() + "\n\n")


class RivenTabLayout(BoxLayout):
    ctx: RivenContext

    layout_content: BoxLayout
    layout_content_riven: RivenContent

    layout_not_connected: NotConnectedLayout

    def __init__(self, ctx: RivenContext) -> None:
        super().__init__(orientation="vertical", padding="8dp")

        self.bind(minimum_height=self.setter("height"))

        self.ctx = ctx

        self.layout_not_connected = NotConnectedLayout(self.ctx)
        self.add_widget(self.layout_not_connected)

        self.layout_content = BoxLayout(orientation="horizontal", spacing="16dp", padding=["8dp", "0dp"])
        self.add_widget(self.layout_content)

        self.update()

    def update(self) -> None:
        if self.ctx.game_controller.selected_starting_route is None:
            self.layout_not_connected.show()

            if hasattr(self, "layout_content_riven"):
                self.layout_content_riven.timer.cancel()

            self.layout_content.clear_widgets()

            return

        self.layout_not_connected.hide()

        if not len(self.layout_content.children):
            self.layout_content_riven = RivenContent(ctx=self.ctx)
            self.layout_content.add_widget(self.layout_content_riven)

from typing import Dict, List, Set, Tuple

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

from kivymd.uix.scrollview import MDScrollView

from ..client import ZorkGrandInquisitorContext
from ..data.entrance_randomizer_data import randomizable_entrances, randomizable_entrances_subway
from ..data.mapping_data import entrance_names, entrance_names_reverse
from ..enums import ZorkGrandInquisitorEntranceRandomizer, ZorkGrandInquisitorRegions


class NotConnectedLayout(BoxLayout):
    ctx: ZorkGrandInquisitorContext

    def __init__(self, ctx: ZorkGrandInquisitorContext) -> None:
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


class TrackerTabLayout(BoxLayout):
    ctx: ZorkGrandInquisitorContext

    layout_content: BoxLayout

    layout_not_connected: NotConnectedLayout

    def __init__(self, ctx: ZorkGrandInquisitorContext) -> None:
        super().__init__(orientation="vertical")

        self.ctx = ctx

        self.layout_not_connected = NotConnectedLayout(self.ctx)
        self.add_widget(self.layout_not_connected)

        self.layout_content = BoxLayout(orientation="horizontal", spacing="16dp", padding=["8dp", "0dp"])
        self.add_widget(self.layout_content)

        self.update()

    def update(self) -> None:
        if self.ctx.game_controller.save_ids is None:
            self.layout_not_connected.show()
            self.layout_content.clear_widgets()

            return

        self.layout_not_connected.hide()

        # ...


class NoEntranceRandomizerLayout(BoxLayout):
    ctx: ZorkGrandInquisitorContext

    def __init__(self, ctx: ZorkGrandInquisitorContext) -> None:
        super().__init__(orientation="horizontal", size_hint_y=0.08)

        self.ctx = ctx

        self.add_widget(
            Label(text="No entrances to track. This seed doesn't use the entrance randomizer.", font_size="24dp")
        )

    def show(self):
        self.opacity = 1.0
        self.size_hint_y = 0.08
        self.disabled = False

    def hide(self):
        self.opacity = 0.0
        self.size_hint_y = None
        self.height = "0dp"
        self.disabled = True


class EntranceLabel(Label):
    ctx: ZorkGrandInquisitorContext

    entrance_name: str
    entrance_markup: str

    def __init__(self, ctx: ZorkGrandInquisitorContext, entrance_name: str, entrance_markup: str) -> None:
        super().__init__(
            text=entrance_markup,
            markup=True,
            font_size="16dp",
            size_hint_y=None,
            height="22dp",
            halign="left",
            valign="bottom",
        )

        self.ctx = ctx

        self.entrance_name = entrance_name
        self.entrance_markup = entrance_markup

        self.bind(size=lambda label, size: setattr(label, "text_size", size))

    def update(self) -> None:
        if self.ctx.data_storage_key is not None and self.ctx.data_storage_key in self.ctx.stored_data:
            if self.entrance_name in self.ctx.stored_data[self.ctx.data_storage_key].get("discovered_entrances", []):
                destination_entrance_name: str = self.ctx.entrance_randomizer_data_by_name[self.entrance_name]
                destination_region: ZorkGrandInquisitorRegions = entrance_names_reverse[destination_entrance_name][1]

                self.text = self.entrance_markup + f" [b][color=B070E0]{destination_region.value}[/color][/b]"
            else:
                self.text = self.entrance_markup


class EntrancesContent(MDScrollView):
    ctx: ZorkGrandInquisitorContext

    layout: BoxLayout

    entrance_labels: Dict[str, EntranceLabel]

    def __init__(self, ctx: ZorkGrandInquisitorContext) -> None:
        super().__init__()

        self.ctx = ctx

        self.layout = BoxLayout(orientation="vertical", size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter("height"))

        self.entrance_labels = dict()

        allowable_entrances: Set[Tuple[ZorkGrandInquisitorRegions, ZorkGrandInquisitorRegions]] = set(
            randomizable_entrances
        )

        if self.ctx.game_controller.option_entrance_randomizer_include_subway_destinations:
            allowable_entrances.update(randomizable_entrances_subway)

        entrance_data: List[Tuple[str, str]] = list()

        regions: Tuple[ZorkGrandInquisitorRegions, ZorkGrandInquisitorRegions]
        entrance_name: str
        for regions, entrance_name in entrance_names.items():
            if regions in allowable_entrances:
                entrance_data.append(
                    (
                        entrance_name,
                        f"[b][color=00FA9A]{regions[0].value}:[/color][/b] {entrance_name} >>>",
                    )
                )

        data: Tuple[str, str]
        for data in sorted(entrance_data, key=lambda x: x[1]):
            entrance_label: EntranceLabel = EntranceLabel(self.ctx, data[0], data[1])

            self.layout.add_widget(entrance_label)
            self.entrance_labels[data[0]] = entrance_label

        self.add_widget(self.layout)

    def update(self) -> None:
        entrance_name: str
        entrance_label: EntranceLabel
        for entrance_name, entrance_label in self.entrance_labels.items():
            entrance_label.update()


class EntrancesTabLayout(BoxLayout):
    ctx: ZorkGrandInquisitorContext

    layout_content: BoxLayout
    layout_content_entrances: EntrancesContent

    layout_not_connected: NotConnectedLayout
    layout_no_entrance_randomizer: NoEntranceRandomizerLayout

    def __init__(self, ctx: ZorkGrandInquisitorContext) -> None:
        super().__init__(orientation="vertical")

        self.ctx = ctx

        self.layout_not_connected = NotConnectedLayout(self.ctx)
        self.add_widget(self.layout_not_connected)

        self.layout_no_entrance_randomizer = NoEntranceRandomizerLayout(self.ctx)
        self.layout_no_entrance_randomizer.hide()
        self.add_widget(self.layout_no_entrance_randomizer)

        self.layout_content = BoxLayout(orientation="horizontal", spacing="16dp", padding=["8dp", "0dp"])
        self.add_widget(self.layout_content)

        self.update()

    def update(self) -> None:
        if self.ctx.game_controller.save_ids is None:
            self.layout_not_connected.show()

            self.layout_content.clear_widgets()
            self.layout_no_entrance_randomizer.hide()

            return

        allowable_entrance_randomizer_values: Set[ZorkGrandInquisitorEntranceRandomizer] = {
            ZorkGrandInquisitorEntranceRandomizer.COUPLED,
            ZorkGrandInquisitorEntranceRandomizer.UNCOUPLED,
        }

        if self.ctx.game_controller.option_entrance_randomizer not in allowable_entrance_randomizer_values:
            self.layout_no_entrance_randomizer.show()

            self.layout_content.clear_widgets()
            self.layout_not_connected.hide()

            return

        self.layout_not_connected.hide()
        self.layout_no_entrance_randomizer.hide()

        if not len(self.layout_content.children):
            self.layout_content_entrances = EntrancesContent(self.ctx)
            self.layout_content.add_widget(self.layout_content_entrances)

        self.layout_content_entrances.update()

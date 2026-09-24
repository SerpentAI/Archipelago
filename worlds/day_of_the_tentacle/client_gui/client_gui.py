from typing import List, Optional, Tuple

from kvui import GameManager

from kivy.uix.layout import Layout
from kivy.uix.widget import Widget

from ..client import DayOfTheTentacleContext

from .client_gui_layouts import DayOfTheTentacleTabLayout


def bootstrap_client_gui(gui: Optional[type[GameManager]]) -> type[GameManager]:
    class DayOfTheTentacleManager(gui):
        ctx: DayOfTheTentacleContext

        logging_pairs: List[Tuple[str, str]] = [("Client", "Archipelago")]
        base_title: str = "Archipelago Day of the Tentacle Client"

        day_of_the_tentacle_tab_layout: DayOfTheTentacleTabLayout

        day_of_the_tentacle_tab: Widget

        def build(self) -> Layout:
            container: Layout = super().build()

            self.day_of_the_tentacle_tab_layout = DayOfTheTentacleTabLayout(self.ctx)
            self.day_of_the_tentacle_tab = self.add_client_tab("Day of the Tentacle", self.day_of_the_tentacle_tab_layout)

            return container

        def update_tabs(self) -> None:
            self.day_of_the_tentacle_tab_layout.update()

    return DayOfTheTentacleManager

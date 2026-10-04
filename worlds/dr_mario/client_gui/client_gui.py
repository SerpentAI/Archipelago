from typing import List, Optional, Tuple

from kvui import GameManager

from kivy.uix.layout import Layout
from kivy.uix.widget import Widget

from ..client import DrMarioContext

from .client_gui_layouts import DrMarioTabLayout


def bootstrap_client_gui(gui: Optional[type[GameManager]]) -> type[GameManager]:
    class DrMarioManager(gui):
        ctx: DrMarioContext

        logging_pairs: List[Tuple[str, str]] = [("Client", "Archipelago")]
        base_title: str = "Archipelago Dr. Mario Client"

        dr_mario_tab_layout: DrMarioTabLayout

        dr_mario_tab: Widget

        def build(self) -> Layout:
            container: Layout = super().build()

            self.dr_mario_tab_layout = DrMarioTabLayout(self.ctx)
            self.dr_mario_tab = self.add_client_tab("Dr. Mario", self.dr_mario_tab_layout)

            return container

        def update_tabs(self) -> None:
            self.dr_mario_tab_layout.update()

    return DrMarioManager

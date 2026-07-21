from typing import List, Optional, Tuple

from kvui import GameManager

from kivy.uix.layout import Layout
from kivy.uix.widget import Widget

from ..client import RivenContext

from .client_gui_layouts import RivenTabLayout


def bootstrap_client_gui(gui: Optional[type[GameManager]]) -> type[GameManager]:
    class RivenManager(gui):
        ctx: RivenContext

        logging_pairs: List[Tuple[str, str]] = [("Client", "Archipelago")]
        base_title: str = "Archipelago Riven Client"

        riven_tab_layout: RivenTabLayout

        riven_tab: Widget

        def build(self) -> Layout:
            container: Layout = super().build()

            self.riven_tab_layout = RivenTabLayout(self.ctx)
            self.riven_tab = self.add_client_tab("Riven", self.riven_tab_layout)

            return container

        def update_tabs(self) -> None:
            self.riven_tab_layout.update()

    return RivenManager

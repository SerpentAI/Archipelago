from typing import List, Optional, Tuple

from kvui import GameManager

from kivy.uix.layout import Layout
from kivy.uix.widget import Widget

from ..client import SeveredSteelContext

from .client_gui_layouts import SeveredSteelTabLayout


def bootstrap_client_gui(gui: Optional[type[GameManager]]) -> type[GameManager]:
    class SeveredSteelManager(gui):
        ctx: SeveredSteelContext

        logging_pairs: List[Tuple[str, str]] = [("Client", "Archipelago")]
        base_title: str = "Archipelago Severed Steel Client"

        severed_steel_tab_layout: SeveredSteelTabLayout

        severed_steel_tab: Widget

        def build(self) -> Layout:
            container: Layout = super().build()

            self.severed_steel_tab_layout = SeveredSteelTabLayout(self.ctx)
            self.severed_steel_tab = self.add_client_tab("Severed Steel", self.severed_steel_tab_layout)

            return container

        def update_tabs(self) -> None:
            self.severed_steel_tab_layout.update()

    return SeveredSteelManager

from typing import List, Optional, Tuple

from kvui import GameManager

from kivy.uix.layout import Layout
from kivy.uix.widget import Widget

from ..client import PinballFXContext

from .client_gui_layouts import PinballFXTabLayout


def bootstrap_client_gui(gui: Optional[type[GameManager]]) -> type[GameManager]:
    class PinballFXManager(gui):
        ctx: PinballFXContext

        logging_pairs: List[Tuple[str, str]] = [("Client", "Archipelago")]
        base_title: str = "Archipelago Pinball FX Client"

        pinball_fx_tab_layout: PinballFXTabLayout

        pinball_fx_tab: Widget

        def build(self) -> Layout:
            container: Layout = super().build()

            self.pinball_fx_tab_layout = PinballFXTabLayout(self.ctx)
            self.pinball_fx_tab = self.add_client_tab("Pinball FX", self.pinball_fx_tab_layout)

            return container

        def update_tabs(self) -> None:
            self.pinball_fx_tab_layout.update()

    return PinballFXManager

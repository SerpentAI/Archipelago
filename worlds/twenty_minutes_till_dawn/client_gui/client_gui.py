from typing import List, Optional, Tuple

from kvui import GameManager

from kivy.uix.layout import Layout
from kivy.uix.widget import Widget

from ..client import TwentyMinutesContext

from .client_gui_layouts import TwentyMinutesTabLayout


def bootstrap_client_gui(gui: Optional[type[GameManager]]) -> type[GameManager]:
    class TwentyMinutesManager(gui):
        ctx: TwentyMinutesContext

        logging_pairs: List[Tuple[str, str]] = [("Client", "Archipelago")]
        base_title: str = "Archipelago 20 Minutes Till Dawn Client"

        twenty_minutes_tab_layout: TwentyMinutesTabLayout

        twenty_minutes_tab: Widget

        def build(self) -> Layout:
            container: Layout = super().build()

            self.twenty_minutes_tab_layout = TwentyMinutesTabLayout(self.ctx)
            self.twenty_minutes_tab = self.add_client_tab("20 Minutes Till Dawn", self.twenty_minutes_tab_layout)

            return container

        def update_tabs(self) -> None:
            self.twenty_minutes_tab_layout.update()

    return TwentyMinutesManager

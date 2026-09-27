from typing import List, Optional, Tuple

from kvui import GameManager

from kivy.uix.layout import Layout
from kivy.uix.widget import Widget

from ..client import ZorkGrandInquisitorContext

from .client_gui_layouts import TrackerTabLayout, EntrancesTabLayout


def bootstrap_client_gui(gui: Optional[type[GameManager]]) -> type[GameManager]:
    class ZorkGrandInquisitorManager(gui):
        ctx: ZorkGrandInquisitorContext

        logging_pairs: List[Tuple[str, str]] = [("Client", "Archipelago")]
        base_title: str = "Archipelago Zork Grand Inquisitor Client"

        tracker_tab_layout: TrackerTabLayout
        entrances_tab_layout: EntrancesTabLayout

        tracker_tab: Widget
        entrances_tab: Widget

        def build(self) -> Layout:
            container: Layout = super().build()

            self.tracker_tab_layout = TrackerTabLayout(self.ctx)
            self.tracker_tab = self.add_client_tab("Tracker", self.tracker_tab_layout)

            self.entrances_tab_layout = EntrancesTabLayout(self.ctx)
            self.entrances_tab = self.add_client_tab("Entrances", self.entrances_tab_layout)

            return container

        def update_tabs(self) -> None:
            self.tracker_tab_layout.update()
            self.entrances_tab_layout.update()

    return ZorkGrandInquisitorManager

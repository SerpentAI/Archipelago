from typing import List, Tuple

from kvui import GameManager

from kivy.uix.layout import Layout
from kivy.uix.widget import Widget

from kivy.core.window import Window
from kivy.modules import inspector

from ..client import MirrorsEdgeContext

from .client_gui_layouts import MirrorsEdgeTabLayout


class MirrorsEdgeManager(GameManager):
    ctx: MirrorsEdgeContext

    logging_pairs: List[Tuple[str, str]] = [("Client", "Archipelago")]
    base_title: str = "Archipelago Mirror's Edge Client"

    mirrors_edge_tab_layout: MirrorsEdgeTabLayout
    mirrors_edge_tab: Widget

    def build(self) -> Layout:
        container: Layout = super().build()

        self.mirrors_edge_tab_layout = MirrorsEdgeTabLayout(self.ctx)
        self.mirrors_edge_tab = self.add_client_tab("Mirror's Edge", self.mirrors_edge_tab_layout)

        inspector.create_inspector(Window, container)

        return container

    def update_tabs(self) -> None:
        self.mirrors_edge_tab_layout.update()

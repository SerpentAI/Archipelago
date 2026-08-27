from typing import List, Optional, Tuple

from kvui import GameManager

from kivy.uix.layout import Layout
from kivy.uix.widget import Widget

from ..client import PoolsContext

from .client_gui_layouts import PoolsTabLayout


def bootstrap_client_gui(gui: Optional[type[GameManager]]) -> type[GameManager]:
    class PoolsManager(gui):
        ctx: PoolsContext

        logging_pairs: List[Tuple[str, str]] = [("Client", "Archipelago")]
        base_title: str = "Archipelago POOLS Client"

        pools_tab_layout: PoolsTabLayout

        pools_tab: Widget

        def build(self) -> Layout:
            container: Layout = super().build()

            self.pools_tab_layout = PoolsTabLayout(self.ctx)
            self.pools_tab = self.add_client_tab("POOLS", self.pools_tab_layout)

            return container

        def update_tabs(self) -> None:
            self.pools_tab_layout.update()

    return PoolsManager

from typing import List, Tuple

from kvui import GameManager

from kivy.uix.layout import Layout
from kivy.uix.widget import Widget

from kivy.core.window import Window
from kivy.modules import inspector

from ..client import TonyHawksProSkater12Context

from .client_gui_layouts import TonyHawksProSkater12TabLayout


class TonyHawksProSkater12Manager(GameManager):
    ctx: TonyHawksProSkater12Context

    logging_pairs: List[Tuple[str, str]] = [("Client", "Archipelago")]
    base_title: str = "Archipelago Tony Hawk's Pro Skater 1 & 2 Client"

    tony_hawks_pro_skater_1_2_tab_layout: TonyHawksProSkater12TabLayout

    tony_hawks_pro_skater_1_2_tab: Widget

    def build(self) -> Layout:
        container: Layout = super().build()

        self.tony_hawks_pro_skater_1_2_tab_layout = TonyHawksProSkater12TabLayout(self.ctx)
        self.tony_hawks_pro_skater_1_2_tab = self.add_client_tab("Tony Hawk's Pro Skater 1 & 2", self.tony_hawks_pro_skater_1_2_tab_layout)

        inspector.create_inspector(Window, container)

        return container

    def update_tabs(self) -> None:
        self.tony_hawks_pro_skater_1_2_tab_layout.update()

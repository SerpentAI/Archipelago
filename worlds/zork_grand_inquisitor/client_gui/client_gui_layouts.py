from typing import Dict, List, Set, Tuple

import kivy.utils

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget

from kivymd.app import MDApp
from kivymd.uix.scrollview import MDScrollView

from ..client import ZorkGrandInquisitorContext
from ..data.entrance_randomizer_data import randomizable_entrances, randomizable_entrances_subway
from ..data.mapping_data import entrance_names, entrance_names_reverse

from ..enums import (
    ZorkGrandInquisitorEntranceRandomizer,
    ZorkGrandInquisitorGoals,
    ZorkGrandInquisitorItems,
    ZorkGrandInquisitorRegions,
)


class NotConnectedLayout(BoxLayout):
    ctx: ZorkGrandInquisitorContext

    def __init__(self, ctx: ZorkGrandInquisitorContext) -> None:
        super().__init__(orientation="horizontal", size_hint_y=0.12)

        self.ctx = ctx

        self.add_widget(
            Label(text="Please connect to an Archipelago server first to view this tab.", font_size="24dp")
        )

    def show(self):
        self.opacity = 1.0
        self.size_hint_y = 0.12
        self.disabled = False

    def hide(self):
        self.opacity = 0.0
        self.size_hint_y = None
        self.height = "0dp"
        self.disabled = True


class TrackerLocationsLayout(MDScrollView):
    ctx: ZorkGrandInquisitorContext

    layout: BoxLayout

    def __init__(self, ctx: ZorkGrandInquisitorContext) -> None:
        super().__init__(size_hint=(0.45, 1.0))

        self.ctx = ctx

        self.layout = BoxLayout(orientation="vertical", size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter("height"))

        title_label: Label = Label(
            text="[b]Available Locations[/b]",
            markup=True,
            font_size="20dp",
            size_hint_y=None,
            height="40dp",
            halign="left",
            valign="middle",
        )

        title_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.layout.add_widget(title_label)

        self.add_widget(self.layout)

    def update(self) -> None:
        pass


class TrackerItemLabel(Label):
    ctx: ZorkGrandInquisitorContext

    item: ZorkGrandInquisitorItems
    received: bool
    count: int

    def __init__(self, ctx: ZorkGrandInquisitorContext, item: ZorkGrandInquisitorItems) -> None:
        super().__init__(
            text=item.value,
            font_size="16dp",
            size_hint_y=None,
            height="22dp",
            halign="left",
            valign="middle",
        )

        self.ctx = ctx

        self.item = item
        self.received = False
        self.count = 1

        self.bind(size=lambda label, size: setattr(label, "text_size", size))

    @property
    def is_goal_item(self) -> bool:
        return self.item in (
            ZorkGrandInquisitorItems.ARTIFACT_OF_MAGIC,
            ZorkGrandInquisitorItems.DEATH,
            ZorkGrandInquisitorItems.LANDMARK,
        )

    def update(self) -> None:
        if self.is_goal_item:
            self.count = self.ctx.game_controller.goal_item_count
            self.received = self.count > 0
        else:
            is_item_in_received: bool = self.item in self.ctx.game_controller.received_items
            is_item_in_queue: bool = self.item in self.ctx.game_controller.received_items_queue

            self.received = is_item_in_received or is_item_in_queue

        if self.received:
            self.opacity = 1.0
        else:
            self.opacity = 0.25

        if self.count > 1:
            self.text = f"{self.item.value} x{self.count}"
        else:
            self.text = self.item.value


class TrackerItemsLayout(MDScrollView):
    ctx: ZorkGrandInquisitorContext

    layout: BoxLayout

    item_labels: Dict[ZorkGrandInquisitorItems, TrackerItemLabel]

    def __init__(self, ctx: ZorkGrandInquisitorContext) -> None:
        super().__init__(size_hint=(0.2, 1.0))

        self.ctx = ctx

        self.layout = BoxLayout(orientation="vertical", size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter("height"))

        self.item_labels = dict()

        title_label: Label = Label(
            text="[b]Items[/b]",
            markup=True,
            font_size="20dp",
            size_hint_y=None,
            height="40dp",
            halign="left",
            valign="middle",
        )

        title_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.layout.add_widget(title_label)

        items_goal: List[ZorkGrandInquisitorItems] = list()

        if self.ctx.game_controller.option_goal == ZorkGrandInquisitorGoals.ARTIFACT_OF_MAGIC_HUNT:
            items_goal.append(ZorkGrandInquisitorItems.ARTIFACT_OF_MAGIC)
        elif self.ctx.game_controller.option_goal == ZorkGrandInquisitorGoals.ZORK_TOUR:
            items_goal.append(ZorkGrandInquisitorItems.LANDMARK)
        elif self.ctx.game_controller.option_goal == ZorkGrandInquisitorGoals.GRIM_JOURNEY:
            items_goal.append(ZorkGrandInquisitorItems.DEATH)

        if len(items_goal):
            item: ZorkGrandInquisitorItems
            for item in items_goal:
                item_label: TrackerItemLabel = TrackerItemLabel(self.ctx, item)
                item_label.update()

                self.item_labels[item] = item_label
                self.layout.add_widget(item_label)

            self.layout.add_widget(Widget(size_hint_y=None, height="20dp"))

        items_inventory: List[ZorkGrandInquisitorItems] = [
            ZorkGrandInquisitorItems.CIGAR,
            ZorkGrandInquisitorItems.COCOA_INGREDIENTS,
            ZorkGrandInquisitorItems.HAMMER,
            ZorkGrandInquisitorItems.HUNGUS_LARD,
            ZorkGrandInquisitorItems.LARGE_TELEGRAPH_HAMMER,
            ZorkGrandInquisitorItems.MAP,
            ZorkGrandInquisitorItems.MEAD_LIGHT,
            ZorkGrandInquisitorItems.MONASTERY_ROPE,
            ZorkGrandInquisitorItems.OLD_SCRATCH_CARD,
            ZorkGrandInquisitorItems.PERMA_SUCK_MACHINE,
            ZorkGrandInquisitorItems.PLASTIC_SIX_PACK_HOLDER,
            ZorkGrandInquisitorItems.POUCH_OF_ZORKMIDS,
            ZorkGrandInquisitorItems.PROZORK_TABLET,
            ZorkGrandInquisitorItems.SANDWITCH_WRAPPER,
            ZorkGrandInquisitorItems.SCROLL_FRAGMENT_ANS,
            ZorkGrandInquisitorItems.SCROLL_FRAGMENT_GIV,
            ZorkGrandInquisitorItems.SHOVEL,
            ZorkGrandInquisitorItems.SNAPDRAGON,
            ZorkGrandInquisitorItems.STUDENT_ID,
            ZorkGrandInquisitorItems.SUBWAY_TOKEN,
            ZorkGrandInquisitorItems.SWORD,
            ZorkGrandInquisitorItems.WELL_ROPE,
            ZorkGrandInquisitorItems.ZIMDOR_SCROLL,
            ZorkGrandInquisitorItems.ZORK_ROCKS,
        ]

        item: ZorkGrandInquisitorItems
        for item in items_inventory:
            item_label: TrackerItemLabel = TrackerItemLabel(self.ctx, item)
            item_label.update()

            self.item_labels[item] = item_label
            self.layout.add_widget(item_label)

        self.layout.add_widget(Widget(size_hint_y=None, height="20dp"))

        items_spells: List[ZorkGrandInquisitorItems] = [
            ZorkGrandInquisitorItems.SPELL_BEBURTT,
            ZorkGrandInquisitorItems.SPELL_GLORF,
            ZorkGrandInquisitorItems.SPELL_GOLGATEM,
            ZorkGrandInquisitorItems.SPELL_IGRAM,
            ZorkGrandInquisitorItems.SPELL_KENDALL,
            ZorkGrandInquisitorItems.SPELL_OBIDIL,
            ZorkGrandInquisitorItems.SPELL_NARWILE,
            ZorkGrandInquisitorItems.SPELL_REZROV,
            ZorkGrandInquisitorItems.SPELL_SNAVIG,
            ZorkGrandInquisitorItems.SPELL_THROCK,
            ZorkGrandInquisitorItems.SPELL_YASTARD
        ]

        item: ZorkGrandInquisitorItems
        for item in items_spells:
            item_label: TrackerItemLabel = TrackerItemLabel(self.ctx, item)
            item_label.update()

            self.item_labels[item] = item_label
            self.layout.add_widget(item_label)

        self.layout.add_widget(Widget(size_hint_y=None, height="20dp"))

        items_totems: List[ZorkGrandInquisitorItems] = [
            ZorkGrandInquisitorItems.TOTEM_BROG,
            ZorkGrandInquisitorItems.TOTEM_GRIFF,
            ZorkGrandInquisitorItems.TOTEM_LUCY,
        ]

        item: ZorkGrandInquisitorItems
        for item in items_totems:
            item_label: TrackerItemLabel = TrackerItemLabel(self.ctx, item)
            item_label.update()

            self.item_labels[item] = item_label
            self.layout.add_widget(item_label)

        self.layout.add_widget(Widget(size_hint_y=None, height="20dp"))

        items_brog: List[ZorkGrandInquisitorItems] = [
            ZorkGrandInquisitorItems.BROGS_FLICKERING_TORCH,
            ZorkGrandInquisitorItems.BROGS_GRUE_EGG,
            ZorkGrandInquisitorItems.BROGS_PLANK,
        ]

        item: ZorkGrandInquisitorItems
        for item in items_brog:
            item_label: TrackerItemLabel = TrackerItemLabel(self.ctx, item)
            item_label.update()

            self.item_labels[item] = item_label
            self.layout.add_widget(item_label)

        self.layout.add_widget(Widget(size_hint_y=None, height="20dp"))

        items_griff: List[ZorkGrandInquisitorItems] = [
            ZorkGrandInquisitorItems.GRIFFS_AIR_PUMP,
            ZorkGrandInquisitorItems.GRIFFS_DRAGON_TOOTH,
            ZorkGrandInquisitorItems.GRIFFS_INFLATABLE_RAFT,
            ZorkGrandInquisitorItems.GRIFFS_INFLATABLE_SEA_CAPTAIN,
        ]

        item: ZorkGrandInquisitorItems
        for item in items_griff:
            item_label: TrackerItemLabel = TrackerItemLabel(self.ctx, item)
            item_label.update()

            self.item_labels[item] = item_label
            self.layout.add_widget(item_label)

        self.layout.add_widget(Widget(size_hint_y=None, height="20dp"))

        items_lucy: List[ZorkGrandInquisitorItems] = [
            ZorkGrandInquisitorItems.LUCYS_PLAYING_CARD_1,
            ZorkGrandInquisitorItems.LUCYS_PLAYING_CARD_2,
            ZorkGrandInquisitorItems.LUCYS_PLAYING_CARD_3,
            ZorkGrandInquisitorItems.LUCYS_PLAYING_CARD_4,
        ]

        item: ZorkGrandInquisitorItems
        for item in items_lucy:
            item_label: TrackerItemLabel = TrackerItemLabel(self.ctx, item)
            item_label.update()

            self.item_labels[item] = item_label
            self.layout.add_widget(item_label)

        self.layout.add_widget(Widget(size_hint_y=None, height="20dp"))

        self.add_widget(self.layout)

    def update(self) -> None:
        item_label: TrackerItemLabel
        for item_label in self.item_labels.values():
            item_label.update()


class TrackerDestinationsHotspotsLabel(Label):
    ctx: ZorkGrandInquisitorContext

    item: ZorkGrandInquisitorItems
    received: bool

    def __init__(self, ctx: ZorkGrandInquisitorContext, item: ZorkGrandInquisitorItems) -> None:
        super().__init__(
            text=item.value,
            font_size="16dp",
            size_hint_y=None,
            height="22dp",
            halign="left",
            valign="middle",
        )

        self.ctx = ctx

        self.item = item
        self.received = False

        self.bind(size=lambda label, size: setattr(label, "text_size", size))

    def update(self) -> None:
        is_item_in_received: bool = self.item in self.ctx.game_controller.received_items
        is_item_in_queue: bool = self.item in self.ctx.game_controller.received_items_queue

        self.received = is_item_in_received or is_item_in_queue

        if self.received:
            self.opacity = 1.0
        else:
            self.opacity = 0.25


class TrackerDestinationsHotspotsLayout(MDScrollView):
    ctx: ZorkGrandInquisitorContext

    layout: BoxLayout

    destination_hotspot_labels: Dict[ZorkGrandInquisitorItems, TrackerDestinationsHotspotsLabel]

    def __init__(self, ctx: ZorkGrandInquisitorContext) -> None:
        super().__init__(size_hint=(0.35, 1.0))

        self.ctx = ctx

        self.layout = BoxLayout(orientation="vertical", size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter("height"))

        self.destination_hotspot_labels = dict()

        title_label: Label = Label(
            text="[b]Destinations / Hotspots[/b]",
            markup=True,
            font_size="20dp",
            size_hint_y=None,
            height="40dp",
            halign="left",
            valign="middle",
        )

        title_label.bind(size=lambda label, size: setattr(label, "text_size", size))

        self.layout.add_widget(title_label)

        items_destinations_subway: List[ZorkGrandInquisitorItems] = [
            ZorkGrandInquisitorItems.SUBWAY_DESTINATION_CROSSROADS,
            ZorkGrandInquisitorItems.SUBWAY_DESTINATION_FLOOD_CONTROL_DAM,
            ZorkGrandInquisitorItems.SUBWAY_DESTINATION_HADES,
            ZorkGrandInquisitorItems.SUBWAY_DESTINATION_MONASTERY,
        ]

        item: ZorkGrandInquisitorItems
        for item in items_destinations_subway:
            destination_hotspot_label: TrackerDestinationsHotspotsLabel = TrackerDestinationsHotspotsLabel(
                self.ctx, item
            )

            destination_hotspot_label.update()

            self.destination_hotspot_labels[item] = destination_hotspot_label
            self.layout.add_widget(destination_hotspot_label)

        self.layout.add_widget(Widget(size_hint_y=None, height="20dp"))

        items_destinations_teleporter: List[ZorkGrandInquisitorItems] = [
            ZorkGrandInquisitorItems.TELEPORTER_DESTINATION_CROSSROADS,
            ZorkGrandInquisitorItems.TELEPORTER_DESTINATION_DM_LAIR,
            ZorkGrandInquisitorItems.TELEPORTER_DESTINATION_GUE_TECH,
            ZorkGrandInquisitorItems.TELEPORTER_DESTINATION_HADES,
            ZorkGrandInquisitorItems.TELEPORTER_DESTINATION_MONASTERY,
            ZorkGrandInquisitorItems.TELEPORTER_DESTINATION_SPELL_LAB,
        ]

        item: ZorkGrandInquisitorItems
        for item in items_destinations_teleporter:
            destination_hotspot_label: TrackerDestinationsHotspotsLabel = TrackerDestinationsHotspotsLabel(
                self.ctx, item
            )

            destination_hotspot_label.update()

            self.destination_hotspot_labels[item] = destination_hotspot_label
            self.layout.add_widget(destination_hotspot_label)

        self.layout.add_widget(Widget(size_hint_y=None, height="20dp"))

        items_destinations_totemizer: List[ZorkGrandInquisitorItems] = [
            ZorkGrandInquisitorItems.TOTEMIZER_DESTINATION_HALL_OF_INQUISITION,
            ZorkGrandInquisitorItems.TOTEMIZER_DESTINATION_INFINITY,
            ZorkGrandInquisitorItems.TOTEMIZER_DESTINATION_NEWARK_NEW_JERSEY,
            ZorkGrandInquisitorItems.TOTEMIZER_DESTINATION_STRAIGHT_TO_HELL,
            ZorkGrandInquisitorItems.TOTEMIZER_DESTINATION_SURFACE_OF_MERZ,
        ]

        item: ZorkGrandInquisitorItems
        for item in items_destinations_totemizer:
            destination_hotspot_label: TrackerDestinationsHotspotsLabel = TrackerDestinationsHotspotsLabel(
                self.ctx, item
            )

            destination_hotspot_label.update()

            self.destination_hotspot_labels[item] = destination_hotspot_label
            self.layout.add_widget(destination_hotspot_label)

        self.layout.add_widget(Widget(size_hint_y=None, height="20dp"))

        items_hotspots: List[ZorkGrandInquisitorItems] = [
            ZorkGrandInquisitorItems.HOTSPOT_666_MAILBOX,
            ZorkGrandInquisitorItems.HOTSPOT_ALPINES_QUANDRY_CARD_SLOTS,
            ZorkGrandInquisitorItems.HOTSPOT_BLANK_SCROLL_BOX,
            ZorkGrandInquisitorItems.HOTSPOT_BLINDS,
            ZorkGrandInquisitorItems.HOTSPOT_BUCKET,
            ZorkGrandInquisitorItems.HOTSPOT_CANDY_MACHINE_BUTTONS,
            ZorkGrandInquisitorItems.HOTSPOT_CANDY_MACHINE_COIN_SLOT,
            ZorkGrandInquisitorItems.HOTSPOT_CANDY_MACHINE_VACUUM_SLOT,
            ZorkGrandInquisitorItems.HOTSPOT_CHANGE_MACHINE_SLOT,
            ZorkGrandInquisitorItems.HOTSPOT_CLOSET_DOOR,
            ZorkGrandInquisitorItems.HOTSPOT_CLOSING_THE_TIME_TUNNELS_HAMMER_SLOT,
            ZorkGrandInquisitorItems.HOTSPOT_CLOSING_THE_TIME_TUNNELS_LEVER,
            ZorkGrandInquisitorItems.HOTSPOT_COOKING_POT,
            ZorkGrandInquisitorItems.HOTSPOT_DENTED_LOCKER,
            ZorkGrandInquisitorItems.HOTSPOT_DIRT_MOUND,
            ZorkGrandInquisitorItems.HOTSPOT_DOCK_WINCH,
            ZorkGrandInquisitorItems.HOTSPOT_DRAGON_CLAW,
            ZorkGrandInquisitorItems.HOTSPOT_DRAGON_NOSTRILS,
            ZorkGrandInquisitorItems.HOTSPOT_DUNGEON_MASTERS_LAIR_ENTRANCE,
            ZorkGrandInquisitorItems.HOTSPOT_FLOOD_CONTROL_BUTTONS,
            ZorkGrandInquisitorItems.HOTSPOT_FLOOD_CONTROL_DOORS,
            ZorkGrandInquisitorItems.HOTSPOT_FROZEN_TREAT_MACHINE_COIN_SLOT,
            ZorkGrandInquisitorItems.HOTSPOT_FROZEN_TREAT_MACHINE_DOORS,
            ZorkGrandInquisitorItems.HOTSPOT_GLASS_CASE,
            ZorkGrandInquisitorItems.HOTSPOT_GRAND_INQUISITOR_DOLL,
            ZorkGrandInquisitorItems.HOTSPOT_GUE_TECH_DOOR,
            ZorkGrandInquisitorItems.HOTSPOT_GUE_TECH_GRASS,
            ZorkGrandInquisitorItems.HOTSPOT_GUE_TECH_WINDOWS,
            ZorkGrandInquisitorItems.HOTSPOT_HADES_PHONE_BUTTONS,
            ZorkGrandInquisitorItems.HOTSPOT_HADES_PHONE_RECEIVER,
            ZorkGrandInquisitorItems.HOTSPOT_HARRY,
            ZorkGrandInquisitorItems.HOTSPOT_HARRYS_ASHTRAY,
            ZorkGrandInquisitorItems.HOTSPOT_HARRYS_BIRD_BATH,
            ZorkGrandInquisitorItems.HOTSPOT_IN_MAGIC_WE_TRUST_DOOR,
            ZorkGrandInquisitorItems.HOTSPOT_JACKS_DOOR,
            ZorkGrandInquisitorItems.HOTSPOT_LOUDSPEAKER_VOLUME_BUTTONS,
            ZorkGrandInquisitorItems.HOTSPOT_MAILBOX_DOOR,
            ZorkGrandInquisitorItems.HOTSPOT_MAILBOX_FLAG,
            ZorkGrandInquisitorItems.HOTSPOT_MIRROR,
            ZorkGrandInquisitorItems.HOTSPOT_MOSSY_GRATE,
            ZorkGrandInquisitorItems.HOTSPOT_PORT_FOOZLE_PAST_TAVERN_DOOR,
            ZorkGrandInquisitorItems.HOTSPOT_PURPLE_WORDS,
            ZorkGrandInquisitorItems.HOTSPOT_QUELBEE_HIVE,
            ZorkGrandInquisitorItems.HOTSPOT_ROPE_BRIDGE,
            ZorkGrandInquisitorItems.HOTSPOT_SKULL_CAGE,
            ZorkGrandInquisitorItems.HOTSPOT_SNAPDRAGON,
            ZorkGrandInquisitorItems.HOTSPOT_SODA_MACHINE_BUTTONS,
            ZorkGrandInquisitorItems.HOTSPOT_SODA_MACHINE_COIN_SLOT,
            ZorkGrandInquisitorItems.HOTSPOT_SOUVENIR_COIN_SLOT,
            ZorkGrandInquisitorItems.HOTSPOT_SPELL_CHECKER,
            ZorkGrandInquisitorItems.HOTSPOT_SPELL_LAB_CHASM,
            ZorkGrandInquisitorItems.HOTSPOT_SPRING_MUSHROOM,
            ZorkGrandInquisitorItems.HOTSPOT_STUDENT_ID_MACHINE,
            ZorkGrandInquisitorItems.HOTSPOT_SUBWAY_TOKEN_SLOT,
            ZorkGrandInquisitorItems.HOTSPOT_TAVERN_FLY,
            ZorkGrandInquisitorItems.HOTSPOT_TOTEMIZER_SWITCH,
            ZorkGrandInquisitorItems.HOTSPOT_TOTEMIZER_WHEELS,
        ]

        item: ZorkGrandInquisitorItems
        for item in items_hotspots:
            destination_hotspot_label: TrackerDestinationsHotspotsLabel = TrackerDestinationsHotspotsLabel(
                self.ctx, item
            )

            destination_hotspot_label.update()

            self.destination_hotspot_labels[item] = destination_hotspot_label
            self.layout.add_widget(destination_hotspot_label)

        self.layout.add_widget(Widget(size_hint_y=None, height="20dp"))

        self.add_widget(self.layout)

    def update(self) -> None:
        destination_hotspot_label: TrackerDestinationsHotspotsLabel
        for destination_hotspot_label in self.destination_hotspot_labels.values():
            destination_hotspot_label.update()


class TrackerTabLayout(BoxLayout):
    ctx: ZorkGrandInquisitorContext

    layout_content: BoxLayout

    layout_locations: TrackerLocationsLayout
    layout_items: TrackerItemsLayout
    layout_destinations_hotspots: TrackerDestinationsHotspotsLayout

    layout_not_connected: NotConnectedLayout

    def __init__(self, ctx: ZorkGrandInquisitorContext) -> None:
        super().__init__(orientation="vertical")

        self.ctx = ctx

        self.layout_not_connected = NotConnectedLayout(self.ctx)
        self.add_widget(self.layout_not_connected)

        self.layout_content = BoxLayout(orientation="horizontal", spacing="16dp", padding=["8dp", "0dp"])
        self.add_widget(self.layout_content)

        self.update()

    def update(self) -> None:
        if self.ctx.game_controller.save_ids is None:
            self.layout_not_connected.show()
            self.layout_content.clear_widgets()

            return

        self.layout_not_connected.hide()

        if not len(self.layout_content.children):
            self.layout_locations = TrackerLocationsLayout(self.ctx)
            self.layout_content.add_widget(self.layout_locations)

            self.layout_items = TrackerItemsLayout(self.ctx)
            self.layout_content.add_widget(self.layout_items)

            self.layout_destinations_hotspots = TrackerDestinationsHotspotsLayout(self.ctx)
            self.layout_content.add_widget(self.layout_destinations_hotspots)

        self.layout_locations.update()
        self.layout_items.update()
        self.layout_destinations_hotspots.update()


class NoEntranceRandomizerLayout(BoxLayout):
    ctx: ZorkGrandInquisitorContext

    def __init__(self, ctx: ZorkGrandInquisitorContext) -> None:
        super().__init__(orientation="horizontal", size_hint_y=0.08)

        self.ctx = ctx

        self.add_widget(
            Label(text="No entrances to track. This seed doesn't use the entrance randomizer.", font_size="24dp")
        )

    def show(self):
        self.opacity = 1.0
        self.size_hint_y = 0.08
        self.disabled = False

    def hide(self):
        self.opacity = 0.0
        self.size_hint_y = None
        self.height = "0dp"
        self.disabled = True


class EntranceLabel(Label):
    ctx: ZorkGrandInquisitorContext

    entrance_name: str
    entrance_markup: str

    color_: str

    def __init__(self, ctx: ZorkGrandInquisitorContext, entrance_name: str, entrance_markup: str) -> None:
        super().__init__(
            text=entrance_markup,
            markup=True,
            font_size="16dp",
            size_hint_y=None,
            height="22dp",
            halign="left",
            valign="bottom",
        )

        self.ctx = ctx

        self.entrance_name = entrance_name
        self.entrance_markup = entrance_markup

        theme_color: List[float] = MDApp.get_running_app().theme_cls.secondaryColor
        self.color_ = "".join(["{:02X}".format(round(c * 255)) for c in theme_color[:3]])

        self.bind(size=lambda label, size: setattr(label, "text_size", size))

    def update(self) -> None:
        if self.ctx.data_storage_key is not None and self.ctx.data_storage_key in self.ctx.stored_data:
            if self.entrance_name in self.ctx.stored_data[self.ctx.data_storage_key].get("discovered_entrances", []):
                destination_entrance_name: str = self.ctx.entrance_randomizer_data_by_name[self.entrance_name]
                destination_region: ZorkGrandInquisitorRegions = entrance_names_reverse[destination_entrance_name][1]

                self.text = self.entrance_markup + f" [b][color={self.color_}]{destination_region.value}[/color][/b]"
            else:
                self.text = self.entrance_markup


class EntrancesContent(MDScrollView):
    ctx: ZorkGrandInquisitorContext

    layout: BoxLayout

    entrance_labels: Dict[str, EntranceLabel]

    def __init__(self, ctx: ZorkGrandInquisitorContext) -> None:
        super().__init__()

        self.ctx = ctx

        self.layout = BoxLayout(orientation="vertical", size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter("height"))

        theme_primary_color: str = kivy.utils.hex_colormap.get(
            MDApp.get_running_app().theme_cls.primary_palette.lower(),
            "springgreen",
        )

        self.entrance_labels = dict()

        allowable_entrances: Set[Tuple[ZorkGrandInquisitorRegions, ZorkGrandInquisitorRegions]] = set(
            randomizable_entrances
        )

        if self.ctx.game_controller.option_entrance_randomizer_include_subway_destinations:
            allowable_entrances.update(randomizable_entrances_subway)

        entrance_data: List[Tuple[str, str]] = list()

        regions: Tuple[ZorkGrandInquisitorRegions, ZorkGrandInquisitorRegions]
        entrance_name: str
        for regions, entrance_name in entrance_names.items():
            if regions in allowable_entrances:
                entrance_data.append(
                    (
                        entrance_name,
                        f"[b][color={theme_primary_color}]{regions[0].value}:[/color][/b] {entrance_name} >>>",
                    )
                )

        data: Tuple[str, str]
        for data in sorted(entrance_data, key=lambda x: x[1]):
            entrance_label: EntranceLabel = EntranceLabel(self.ctx, data[0], data[1])

            self.layout.add_widget(entrance_label)
            self.entrance_labels[data[0]] = entrance_label

        self.add_widget(self.layout)

    def update(self) -> None:
        entrance_name: str
        entrance_label: EntranceLabel
        for entrance_name, entrance_label in self.entrance_labels.items():
            entrance_label.update()


class EntrancesTabLayout(BoxLayout):
    ctx: ZorkGrandInquisitorContext

    layout_content: BoxLayout
    layout_content_entrances: EntrancesContent

    layout_not_connected: NotConnectedLayout
    layout_no_entrance_randomizer: NoEntranceRandomizerLayout

    def __init__(self, ctx: ZorkGrandInquisitorContext) -> None:
        super().__init__(orientation="vertical")

        self.ctx = ctx

        self.layout_not_connected = NotConnectedLayout(self.ctx)
        self.add_widget(self.layout_not_connected)

        self.layout_no_entrance_randomizer = NoEntranceRandomizerLayout(self.ctx)
        self.layout_no_entrance_randomizer.hide()
        self.add_widget(self.layout_no_entrance_randomizer)

        self.layout_content = BoxLayout(orientation="horizontal", spacing="16dp", padding=["8dp", "0dp"])
        self.add_widget(self.layout_content)

        self.update()

    def update(self) -> None:
        if self.ctx.game_controller.save_ids is None:
            self.layout_not_connected.show()

            self.layout_content.clear_widgets()
            self.layout_no_entrance_randomizer.hide()

            return

        allowable_entrance_randomizer_values: Set[ZorkGrandInquisitorEntranceRandomizer] = {
            ZorkGrandInquisitorEntranceRandomizer.COUPLED,
            ZorkGrandInquisitorEntranceRandomizer.UNCOUPLED,
        }

        if self.ctx.game_controller.option_entrance_randomizer not in allowable_entrance_randomizer_values:
            self.layout_no_entrance_randomizer.show()

            self.layout_content.clear_widgets()
            self.layout_not_connected.hide()

            return

        self.layout_not_connected.hide()
        self.layout_no_entrance_randomizer.hide()

        if not len(self.layout_content.children):
            self.layout_content_entrances = EntrancesContent(self.ctx)
            self.layout_content.add_widget(self.layout_content_entrances)

        self.layout_content_entrances.update()

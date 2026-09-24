from typing import Dict, NamedTuple, Tuple

from BaseClasses import ItemClassification

from ..enums import DayOfTheTentacleItems, DayOfTheTentacleTags


class DayOfTheTentacleItemData(NamedTuple):
    archipelago_id: int
    classification: ItemClassification
    tags: Tuple[DayOfTheTentacleTags, ...]


item_base_offset: int = 10000

item_data: Dict[DayOfTheTentacleItems, DayOfTheTentacleItemData] = {
    # Goal
    DayOfTheTentacleItems.SWISS_DEPOSIT: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 1,
        classification=ItemClassification.progression_deprioritized_skip_balancing,
        tags=(
            DayOfTheTentacleTags.GOAL_ITEM,
        ),
    ),
    # Characters
    DayOfTheTentacleItems.CHARACTER_BERNARD: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 100 + 1,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.CHARACTER_ITEM,
        ),
    ),
    DayOfTheTentacleItems.CHARACTER_HOAGIE: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 100 + 2,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.CHARACTER_ITEM,
        ),
    ),
    DayOfTheTentacleItems.CHARACTER_LAVERNE: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 100 + 3,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.CHARACTER_ITEM,
        ),
    ),
    # Inventory Items
    DayOfTheTentacleItems.BATTERY: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 1,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.BLANKET: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 2,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.BOOBOO_B_GONE: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 3,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.BOX_O_LAUGHS: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 5,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.BRUSH: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 6,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.BUCKET: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 7,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.CAN_OPENER: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 8,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.CAT: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 9,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.CHATTERING_TEETH: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 10,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.CIGAR_LIGHTER: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 11,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.COFFEE: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 12,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.CONTRACT: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 13,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.CRANK: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 14,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.CROWBAR: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 15,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.DECAF_COFFEE: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 16,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.DENTURES: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 17,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.DIME: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 18,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.DINNER_CERTIFICATE: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 19,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.DISAPPEARING_INK: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 20,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.EXPLODING_CIGAR: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 21,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.EXTENSION_CORD: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 22,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.FAKE_BARF: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 23,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.FLAG: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 24,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.FLAG_GUN: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 25,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.FLIER: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 26,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.FORK: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 27,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.FUNNEL: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 28,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.GOLD_PLATED_QUILL_PEN: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 29,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.GUM_WITH_A_DIME_STUCK_IN_IT: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 30,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.HAMSTER: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 31,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.HELP_WANTED_SIGN: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 32,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.HUBCAP: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 33,
        classification=ItemClassification.filler,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.KEYS: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 34,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.LAB_COAT: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 35,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.LEFT_HANDED_HAMMER: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 36,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.LETTER: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 37,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.NAME_TAG: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 38,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.OIL: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 39,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.PATENT_APPLICATION: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 40,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.QUARTERS: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 41,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.RED_PAINT: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 42,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.RIGHT_HANDED_HAMMER: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 43,
        classification=ItemClassification.filler,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.ROLLER_SKATES: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 44,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.ROPE: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 45,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.SCALPEL: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 46,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.SOAP: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 47,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.SPAGHETTI: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 48,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.SQUEAKY_MOUSE_TOY: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 49,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.STAMP: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 50,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.STAMP_ALBUM: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 51,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.STICKY_DIME: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 52,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.SWEATER: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 53,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.SWISS_BANKBOOK: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 54,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.TENTACLE_CHART: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 55,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.TEXTBOOK: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 56,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.TROPHY: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 57,
        classification=ItemClassification.filler,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.VIDEOTAPE: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 58,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.VINEGAR: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 59,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    DayOfTheTentacleItems.WINE_BOTTLE: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 200 + 60,
        classification=ItemClassification.progression,
        tags=(
            DayOfTheTentacleTags.INVENTORY_ITEM,
        ),
    ),
    # Filler
    DayOfTheTentacleItems.CACTUS_NEEDLE: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 300 + 1,
        classification=ItemClassification.filler,
        tags=(
            DayOfTheTentacleTags.FILLER_ITEM,
        ),
    ),
    DayOfTheTentacleItems.COMPLIMENTARY_MINT: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 300 + 2,
        classification=ItemClassification.filler,
        tags=(
            DayOfTheTentacleTags.FILLER_ITEM,
        ),
    ),
    DayOfTheTentacleItems.CONVENTION_BADGE: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 300 + 3,
        classification=ItemClassification.filler,
        tags=(
            DayOfTheTentacleTags.FILLER_ITEM,
        ),
    ),
    DayOfTheTentacleItems.HUMAN_SHOW_TICKET_STUB: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 300 + 4,
        classification=ItemClassification.filler,
        tags=(
            DayOfTheTentacleTags.FILLER_ITEM,
        ),
    ),
    DayOfTheTentacleItems.KUMQUAT: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 300 + 5,
        classification=ItemClassification.filler,
        tags=(
            DayOfTheTentacleTags.FILLER_ITEM,
        ),
    ),
    DayOfTheTentacleItems.SILVER_SHOE_BUCKLE: DayOfTheTentacleItemData(
        archipelago_id=item_base_offset + 300 + 6,
        classification=ItemClassification.filler,
        tags=(
            DayOfTheTentacleTags.FILLER_ITEM,
        ),
    ),
}

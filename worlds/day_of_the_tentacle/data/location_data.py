from typing import Dict, NamedTuple, Tuple

from ..enums import DayOfTheTentacleLocations, DayOfTheTentacleRegions, DayOfTheTentacleTags


class DayOfTheTentacleLocationData(NamedTuple):
    archipelago_id: int
    region: DayOfTheTentacleRegions
    tags: Tuple[DayOfTheTentacleTags, ...]


location_offset: int = 10000

location_data: Dict[DayOfTheTentacleLocations, DayOfTheTentacleLocationData] = {
    DayOfTheTentacleLocations.PRESENT_LOBBY_PICK_UP_HELP_WANTED_SIGN: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 1,
        region=DayOfTheTentacleRegions.PRESENT_LOBBY,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_LOBBY_PICK_UP_FLIER: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 2,
        region=DayOfTheTentacleRegions.PRESENT_LOBBY,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_LOBBY_PICK_UP_DIME: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 3,
        region=DayOfTheTentacleRegions.PRESENT_LOBBY,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_OFFICE_PICK_UP_SWISS_BANKBOOK: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 4,
        region=DayOfTheTentacleRegions.PRESENT_OFFICE,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_OFFICE_PICK_UP_BOOBOO_B_GONE: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 5,
        region=DayOfTheTentacleRegions.PRESENT_OFFICE,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_FRONT_YARD_PICK_UP_LETTER: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 6,
        region=DayOfTheTentacleRegions.PAST_FRONT_YARD,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_KITCHEN_PICK_UP_OIL: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 7,
        region=DayOfTheTentacleRegions.PAST_KITCHEN,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_KITCHEN_PICK_UP_SPAGHETTI: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 8,
        region=DayOfTheTentacleRegions.PAST_KITCHEN,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_LAUNDRY_ROOM_PICK_UP_BUCKET: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 9,
        region=DayOfTheTentacleRegions.PAST_LAUNDRY_ROOM,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_LAUNDRY_ROOM_PICK_UP_BRUSH: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 10,
        region=DayOfTheTentacleRegions.PAST_LAUNDRY_ROOM,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_KITCHEN_USE_BUCKET_WITH_WATER_PUMP: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 11,
        region=DayOfTheTentacleRegions.PAST_KITCHEN,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_BASEMENT_LAB_PICK_UP_LEFT_HANDED_HAMMER: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 12,
        region=DayOfTheTentacleRegions.PAST_BASEMENT_LAB,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_BASEMENT_LAB_GIVE_PATENT_APPLICATION_TO_RED_EDISON: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 13,
        region=DayOfTheTentacleRegions.PAST_BASEMENT_LAB,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_GEORGE_WASHINGTONS_ROOM_USE_GEORGES_BED: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 14,
        region=DayOfTheTentacleRegions.PAST_GEORGE_WASHINGTONS_ROOM,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_GEORGE_WASHINGTONS_ROOM_PULL_CORD: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 15,
        region=DayOfTheTentacleRegions.PAST_GEORGE_WASHINGTONS_ROOM,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_SECOND_FLOOR_HALLWAY_PICK_UP_SOAP: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 16,
        region=DayOfTheTentacleRegions.PAST_SECOND_FLOOR_HALLWAY,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_BEN_FRANKLINS_ROOM_PICK_UP_WINE_BOTTLE: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 17,
        region=DayOfTheTentacleRegions.PAST_BEN_FRANKLINS_ROOM,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_NED_AND_JEDS_ROOM_USE_LEFT_HANDED_HAMMER_WITH_BARREL: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 18,
        region=DayOfTheTentacleRegions.PAST_NED_AND_JEDS_ROOM,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_ATTIC_USE_NEDS_BED: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 19,
        region=DayOfTheTentacleRegions.PAST_ATTIC,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_ATTIC_USE_SQUEAKY_MATTRESS: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 20,
        region=DayOfTheTentacleRegions.PAST_ATTIC,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_ATTIC_PICK_UP_SQUEAKY_MOUSE_TOY: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 21,
        region=DayOfTheTentacleRegions.PAST_ATTIC,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_ATTIC_PICK_UP_RED_PAINT: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 22,
        region=DayOfTheTentacleRegions.PAST_ATTIC,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_MAIN_HALL_USE_WINE_BOTTLE_WITH_TIME_CAPSULE: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 23,
        region=DayOfTheTentacleRegions.PAST_MAIN_HALL,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_OUTHOUSES_USE_RED_PAINT_WITH_KUMQUAT_TREE: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 24,
        region=DayOfTheTentacleRegions.PAST_OUTHOUSES,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_MAIN_HALL_TALK_TO_GEORGE_WASHINGTON_ABOUT_THE_TREE: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 25,
        region=DayOfTheTentacleRegions.PAST_MAIN_HALL,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_SLEEPING_CONVENTIONEERS_ROOM_PICK_UP_KEYS: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 26,
        region=DayOfTheTentacleRegions.PRESENT_SLEEPING_CONVENTIONEERS_ROOM,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_DWAYNES_ROOM_GIVE_LETTER_TO_DWAYNE: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 27,
        region=DayOfTheTentacleRegions.PRESENT_DWAYNES_ROOM,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_DWAYNES_ROOM_PICK_UP_FLAG_GUN: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 28,
        region=DayOfTheTentacleRegions.PRESENT_DWAYNES_ROOM,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_DWAYNES_ROOM_PICK_UP_DISAPPEARING_INK: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 29,
        region=DayOfTheTentacleRegions.PRESENT_DWAYNES_ROOM,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_GREEN_TENTACLES_ROOM_PUSH_SPEAKER: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 30,
        region=DayOfTheTentacleRegions.PRESENT_GREEN_TENTACLES_ROOM,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_GREEN_TENTACLES_ROOM_USE_STEREO: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 31,
        region=DayOfTheTentacleRegions.PRESENT_GREEN_TENTACLES_ROOM,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_GREEN_TENTACLES_ROOM_PICK_UP_VIDEOTAPE: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 32,
        region=DayOfTheTentacleRegions.PRESENT_GREEN_TENTACLES_ROOM,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_LOBBY_PICK_UP_FAKE_BARF: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 33,
        region=DayOfTheTentacleRegions.PRESENT_LOBBY,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_PARKING_LOT_GIVE_KEYS_TO_MAN_IN_SKI_MASK: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 34,
        region=DayOfTheTentacleRegions.PRESENT_PARKING_LOT,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_LOBBY_USE_CROWBAR_WITH_GUM: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 35,
        region=DayOfTheTentacleRegions.PRESENT_LOBBY,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_USE_GUM_WITH_A_DIME_STUCK_IN_IT: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 36,
        region=DayOfTheTentacleRegions.PRESENT_LOBBY,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_SLEEPING_CONVENTIONEERS_ROOM_USE_DIME_WITH_FICKLEFINGERS: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 37,
        region=DayOfTheTentacleRegions.PRESENT_SLEEPING_CONVENTIONEERS_ROOM,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_SLEEPING_CONVENTIONEERS_ROOM_PICK_UP_SWEATER: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 38,
        region=DayOfTheTentacleRegions.PRESENT_SLEEPING_CONVENTIONEERS_ROOM,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_SECOND_FLOOR_HALLWAY_USE_CROWBAR_WITH_CANDY_MACHINE: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 39,
        region=DayOfTheTentacleRegions.PRESENT_SECOND_FLOOR_HALLWAY,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_SECOND_FLOOR_HALLWAY_PICK_UP_QUARTERS: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 40,
        region=DayOfTheTentacleRegions.PRESENT_SECOND_FLOOR_HALLWAY,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_WEIRD_EDS_ROOM_PICK_UP_HAMSTER: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 41,
        region=DayOfTheTentacleRegions.PRESENT_WEIRD_EDS_ROOM,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_WEIRD_EDS_ROOM_USE_DISAPPEARING_INK_WITH_STAMP_ALBUM: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 42,
        region=DayOfTheTentacleRegions.PRESENT_WEIRD_EDS_ROOM,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_THIRD_FLOOR_HALLWAY_PICK_UP_STAMP: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 43,
        region=DayOfTheTentacleRegions.PRESENT_THIRD_FLOOR_HALLWAY,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_THIRD_FLOOR_HALLWAY_PICK_UP_STAMP_ALBUM: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 44,
        region=DayOfTheTentacleRegions.PRESENT_THIRD_FLOOR_HALLWAY,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_WEIRD_EDS_ROOM_GIVE_STAMP_ALBUM_TO_WEIRD_ED: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 45,
        region=DayOfTheTentacleRegions.PRESENT_WEIRD_EDS_ROOM,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_SECOND_FLOOR_HALLWAY_USE_HAMSTER_WITH_ICE_MACHINE: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 46,
        region=DayOfTheTentacleRegions.PRESENT_SECOND_FLOOR_HALLWAY,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_MAIN_HALL_USE_FLAG_GUN_WITH_CIGAR_LIGHTER: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 47,
        region=DayOfTheTentacleRegions.PRESENT_MAIN_HALL,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_MAIN_HALL_PICK_UP_CHATTERING_TEETH: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 48,
        region=DayOfTheTentacleRegions.PRESENT_MAIN_HALL,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_KITCHEN_PICK_UP_FORK: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 49,
        region=DayOfTheTentacleRegions.PRESENT_KITCHEN,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_KITCHEN_PICK_UP_COFFEE: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 50,
        region=DayOfTheTentacleRegions.PRESENT_KITCHEN,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_KITCHEN_PICK_UP_DECAF_COFFEE: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 51,
        region=DayOfTheTentacleRegions.PRESENT_KITCHEN,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_LAUNDRY_ROOM_PICK_UP_FUNNEL: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 52,
        region=DayOfTheTentacleRegions.PRESENT_LAUNDRY_ROOM,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_LAUNDRY_ROOM_USE_SWEATER_WITH_DRYER: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 53,
        region=DayOfTheTentacleRegions.PRESENT_LAUNDRY_ROOM,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_ROOF_PICK_UP_CRANK: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 54,
        region=DayOfTheTentacleRegions.PRESENT_ROOF,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_MAIN_HALL_TALK_TO_CIGAR_SALESMAN: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 55,
        region=DayOfTheTentacleRegions.PRESENT_MAIN_HALL,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_LAUNDRY_ROOM_USE_QUARTERS_WITH_DRYER_COIN_SLOT: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 56,
        region=DayOfTheTentacleRegions.PRESENT_LAUNDRY_ROOM,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_DOCTORS_OFFICE_PICK_UP_TENTACLE_CHART: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 57,
        region=DayOfTheTentacleRegions.FUTURE_DOCTORS_OFFICE,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_USE_SOAP_WITH_BUCKET: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 58,
        region=DayOfTheTentacleRegions.PAST_SECOND_FLOOR_HALLWAY,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_FRONT_YARD_USE_BUCKET_WITH_CARRIAGE: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 59,
        region=DayOfTheTentacleRegions.PAST_FRONT_YARD,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_MAIN_HALL_USE_FLIER_WITH_SUGGESTION_BOX: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 60,
        region=DayOfTheTentacleRegions.PAST_MAIN_HALL,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_MAIN_HALL_GIVE_EXPLODING_CIGAR_TO_GEORGE_WASHINGTON: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 61,
        region=DayOfTheTentacleRegions.PAST_MAIN_HALL,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_MAIN_HALL_GIVE_CHATTERING_TEETH_TO_GEORGE_WASHINGTON: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 62,
        region=DayOfTheTentacleRegions.PAST_MAIN_HALL,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_MAIN_HALL_PICK_UP_BLANKET: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 63,
        region=DayOfTheTentacleRegions.PAST_MAIN_HALL,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_BETSY_ROSSS_ROOM_USE_TENTACLE_CHART_WITH_PATTERNS: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 64,
        region=DayOfTheTentacleRegions.PAST_BETSY_ROSSS_ROOM,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_THIRD_FLOOR_HALLWAY_USE_TEXTBOOK_WITH_HORSE: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 65,
        region=DayOfTheTentacleRegions.PAST_THIRD_FLOOR_HALLWAY,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_THIRD_FLOOR_HALLWAY_PICK_UP_DENTURES: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 66,
        region=DayOfTheTentacleRegions.PAST_THIRD_FLOOR_HALLWAY,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_ROOF_USE_BLANKET_WITH_CHIMNEY: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 67,
        region=DayOfTheTentacleRegions.PAST_ROOF,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_MAIN_HALL_PICK_UP_GOLD_PLATED_QUILL_PEN: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 68,
        region=DayOfTheTentacleRegions.PAST_MAIN_HALL,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_BETSY_ROSSS_ROOM_TALK_TO_BETSY_ROSS: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 69,
        region=DayOfTheTentacleRegions.PAST_BETSY_ROSSS_ROOM,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_ROOF_USE_CRANK_WITH_CRANK_BOX: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 70,
        region=DayOfTheTentacleRegions.FUTURE_ROOF,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_ROOF_USE_ATTACHED_CRANK: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 71,
        region=DayOfTheTentacleRegions.FUTURE_ROOF,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_ROOF_PICK_UP_FLAG: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 72,
        region=DayOfTheTentacleRegions.FUTURE_ROOF,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_USE_FLAG: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 73,
        region=DayOfTheTentacleRegions.FUTURE_DOCTORS_OFFICE,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_SECOND_FLOOR_HALLWAY_PICK_UP_FROZEN_HAMSTER: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 74,
        region=DayOfTheTentacleRegions.FUTURE_SECOND_FLOOR_HALLWAY,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_TIME_CAPSULE_ROOM_USE_CAN_OPENER_WITH_TIME_CAPSULE: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 75,
        region=DayOfTheTentacleRegions.FUTURE_TIME_CAPSULE_ROOM,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_TIME_CAPSULE_ROOM_PICK_UP_VINEGAR: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 76,
        region=DayOfTheTentacleRegions.FUTURE_TIME_CAPSULE_ROOM,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_DEAD_COUSIN_TEDS_ROOM_PICK_UP_EXTENSION_CORD: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 77,
        region=DayOfTheTentacleRegions.FUTURE_DEAD_COUSIN_TEDS_ROOM,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_DEAD_COUSIN_TEDS_ROOM_PICK_UP_ROLLER_SKATES: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 78,
        region=DayOfTheTentacleRegions.FUTURE_DEAD_COUSIN_TEDS_ROOM,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_DEAD_COUSIN_TEDS_ROOM_USE_ROLLER_SKATES_WITH_MUMMY: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 79,
        region=DayOfTheTentacleRegions.FUTURE_DEAD_COUSIN_TEDS_ROOM,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_DEAD_COUSIN_TEDS_ROOM_PUSH_MUMMY: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 80,
        region=DayOfTheTentacleRegions.FUTURE_DEAD_COUSIN_TEDS_ROOM,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_MAIN_HALL_TALK_TO_TENTACLE: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 81,
        region=DayOfTheTentacleRegions.FUTURE_MAIN_HALL,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_MAIN_HALL_USE_SCALPEL_WITH_OOZO_THE_CLOWN: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 82,
        region=DayOfTheTentacleRegions.PRESENT_MAIN_HALL,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_MAIN_HALL_PICK_UP_BOX_O_LAUGHS: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 83,
        region=DayOfTheTentacleRegions.PRESENT_MAIN_HALL,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_BASEMENT_LAB_USE_DECAF_COFFEE_WITH_MUG: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 84,
        region=DayOfTheTentacleRegions.PRESENT_BASEMENT_LAB,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_NURSE_EDNAS_ROOM_PUSH_NURSE_EDNA: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 85,
        region=DayOfTheTentacleRegions.PRESENT_NURSE_EDNAS_ROOM,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_NURSE_EDNAS_ROOM_USE_VIDEOTAPE_WITH_VCR: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 86,
        region=DayOfTheTentacleRegions.PRESENT_NURSE_EDNAS_ROOM,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_OFFICE_OPEN_SAFE: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 87,
        region=DayOfTheTentacleRegions.PRESENT_OFFICE,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_OFFICE_PICK_UP_CONTRACT: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 88,
        region=DayOfTheTentacleRegions.PRESENT_OFFICE,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_ATTIC_PICK_UP_ROPE: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 89,
        region=DayOfTheTentacleRegions.PRESENT_ATTIC,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_ROOF_USE_ROPE_WITH_PULLEY: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 90,
        region=DayOfTheTentacleRegions.PRESENT_ROOF,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_FRONT_YARD_USE_DANGLING_ROPE_WITH_DEAD_COUSIN_TED: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 91,
        region=DayOfTheTentacleRegions.PRESENT_FRONT_YARD,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_USE_RED_PAINT_WITH_DEAD_COUSIN_TED: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 92,
        region=DayOfTheTentacleRegions.PRESENT_FRONT_YARD,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_ROOF_PULL_ROPE_TO_RAISE_TED: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 93,
        region=DayOfTheTentacleRegions.PRESENT_ROOF,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_ROOF_PULL_ROPE_TO_LOWER_DR_FRED: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 94,
        region=DayOfTheTentacleRegions.PRESENT_ROOF,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_BASEMENT_LAB_USE_FUNNEL_WITH_DR_FRED: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 95,
        region=DayOfTheTentacleRegions.PRESENT_BASEMENT_LAB,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_BASEMENT_LAB_USE_COFFEE_WITH_FUNNEL: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 96,
        region=DayOfTheTentacleRegions.PRESENT_BASEMENT_LAB,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_BASEMENT_LAB_USE_CONTRACT_WITH_DR_FRED: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 97,
        region=DayOfTheTentacleRegions.PRESENT_BASEMENT_LAB,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_BASEMENT_LAB_GIVE_HELP_WANTED_SIGN_TO_RED_EDISON: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 98,
        region=DayOfTheTentacleRegions.PAST_BASEMENT_LAB,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_BASEMENT_LAB_PICK_UP_LAB_COAT: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 99,
        region=DayOfTheTentacleRegions.PAST_BASEMENT_LAB,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_BASEMENT_LAB_GIVE_OIL_TO_RED_EDISON: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 100,
        region=DayOfTheTentacleRegions.PAST_BASEMENT_LAB,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_BASEMENT_LAB_GIVE_VINEGAR_TO_RED_EDISON: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 101,
        region=DayOfTheTentacleRegions.PAST_BASEMENT_LAB,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_BASEMENT_LAB_GIVE_GOLD_PLATED_QUILL_PEN_TO_RED_EDISON: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 102,
        region=DayOfTheTentacleRegions.PAST_BASEMENT_LAB,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_BASEMENT_LAB_PICK_UP_BATTERY: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 103,
        region=DayOfTheTentacleRegions.PAST_BASEMENT_LAB,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_BEN_FRANKLINS_ROOM_GIVE_LAB_COAT_TO_BEN_FRANKLIN: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 104,
        region=DayOfTheTentacleRegions.PAST_BEN_FRANKLINS_ROOM,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_FIELD_PICK_UP_FULLY_CHARGED_BATTERY: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 105,
        region=DayOfTheTentacleRegions.PAST_FIELD_KITE_SCENE,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_USE_STAMP_WITH_CONTRACT: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 106,
        region=DayOfTheTentacleRegions.PRESENT_OFFICE,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_FRONT_YARD_USE_CONTRACT_WITH_MAILBOX: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 107,
        region=DayOfTheTentacleRegions.PAST_FRONT_YARD,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_OUTHOUSES_USE_BATTERY_WITH_PLUG: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 108,
        region=DayOfTheTentacleRegions.PAST_OUTHOUSES,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_LOBBY_USE_NAME_TAG_WITH_MUMMY: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 109,
        region=DayOfTheTentacleRegions.FUTURE_LOBBY,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_HUMAN_SHOW_USE_BOX_O_LAUGHS_WITH_MUMMY: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 110,
        region=DayOfTheTentacleRegions.FUTURE_HUMAN_SHOW,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_HUMAN_SHOW_USE_DENTURES_WITH_MUMMY: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 111,
        region=DayOfTheTentacleRegions.FUTURE_HUMAN_SHOW,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_HUMAN_SHOW_USE_SPAGHETTI_WITH_MUMMY: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 112,
        region=DayOfTheTentacleRegions.FUTURE_HUMAN_SHOW,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_HUMAN_SHOW_USE_FORK_WITH_MUMMYS_HEAD: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 113,
        region=DayOfTheTentacleRegions.FUTURE_HUMAN_SHOW,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_HUMAN_SHOW_USE_FAKE_BARF_WITH_HAROLD: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 114,
        region=DayOfTheTentacleRegions.FUTURE_HUMAN_SHOW,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_FRONT_YARD_USE_BOOBOO_B_GONE_WITH_FENCE: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 115,
        region=DayOfTheTentacleRegions.FUTURE_FRONT_YARD,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_FRONT_YARD_USE_SQUEAKY_MOUSE_TOY_WITH_CAT: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 116,
        region=DayOfTheTentacleRegions.FUTURE_FRONT_YARD,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_KENNEL_GIVE_DINNER_CERTIFICATE_TO_TENTACLE_GUARD: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 117,
        region=DayOfTheTentacleRegions.FUTURE_KENNEL,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_KENNEL_USE_CAT_IN_KENNEL: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 118,
        region=DayOfTheTentacleRegions.FUTURE_KENNEL,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_KITCHEN_USE_FROZEN_HAMSTER_WITH_MICROWAVE: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 119,
        region=DayOfTheTentacleRegions.FUTURE_KITCHEN,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_USE_SWEATER_WITH_HAMSTER: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 120,
        region=DayOfTheTentacleRegions.FUTURE_LAUNDRY_ROOM,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_BASEMENT_LAB_USE_HAMSTER_WITH_GENERATOR: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 121,
        region=DayOfTheTentacleRegions.FUTURE_BASEMENT_LAB,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_BASEMENT_LAB_USE_BUILT_IN_SHOP_VAC_WITH_MOUSE_HOLE: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 122,
        region=DayOfTheTentacleRegions.FUTURE_BASEMENT_LAB,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_BASEMENT_LAB_PICK_UP_DUST_BALL: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 123,
        region=DayOfTheTentacleRegions.FUTURE_BASEMENT_LAB,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_BASEMENT_LAB_PICK_UP_HUBCAP: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 124,
        region=DayOfTheTentacleRegions.FUTURE_BASEMENT_LAB,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_BASEMENT_LAB_USE_EXTENSION_CORD_WITH_OUTLET: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 125,
        region=DayOfTheTentacleRegions.FUTURE_BASEMENT_LAB,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_KUMQUAT_TREE_USE_EXTENSION_CORD_WITH_WINDOW: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 126,
        region=DayOfTheTentacleRegions.FUTURE_KUMQUAT_TREE,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_KUMQUAT_TREE_USE_EXTENSION_CORD_WITH_CHRON_O_JOHN: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 127,
        region=DayOfTheTentacleRegions.FUTURE_KUMQUAT_TREE,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_HUMAN_SHOW_JUDGING_TALK_TO_JUDGES_FOR_TROPHY: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 128,
        region=DayOfTheTentacleRegions.FUTURE_HUMAN_SHOW_JUDGING,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_HUMAN_SHOW_JUDGING_TALK_TO_JUDGES_FOR_DINNER_CERTIFICATE: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 129,
        region=DayOfTheTentacleRegions.FUTURE_HUMAN_SHOW_JUDGING,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_DWAYNES_ROOM_LOOK_AT_TV_SET: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 130,
        region=DayOfTheTentacleRegions.PRESENT_DWAYNES_ROOM,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_DWAYNES_ROOM_USE_PHONE: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 131,
        region=DayOfTheTentacleRegions.PRESENT_DWAYNES_ROOM,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_KENNEL_TALK_TO_TENTACLE_GUARD_ABOUT_FEELING_SICK: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 134,
        region=DayOfTheTentacleRegions.FUTURE_KENNEL,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_KENNEL_TALK_TO_TENTACLE_GUARD_ABOUT_THE_BATHROOM: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 135,
        region=DayOfTheTentacleRegions.FUTURE_KENNEL,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_VCR_CONTROLS_USE_RECORD_BUTTON: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 136,
        region=DayOfTheTentacleRegions.PRESENT_VCR_CONTROLS,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_VCR_CONTROLS_USE_PLAY_BUTTON_AT_SLOW_SPEED: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 137,
        region=DayOfTheTentacleRegions.PRESENT_VCR_CONTROLS,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_ATTIC_USE_TED_WITH_DR_FRED: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 138,
        region=DayOfTheTentacleRegions.PRESENT_ATTIC,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_ATTIC_USE_ROPE_WITH_DR_FRED: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 139,
        region=DayOfTheTentacleRegions.PRESENT_ATTIC,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_HUMAN_SHOW_JUDGING_TALK_TO_JUDGES_ABOUT_BEST_HAIR: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 140,
        region=DayOfTheTentacleRegions.FUTURE_HUMAN_SHOW_JUDGING,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_HUMAN_SHOW_JUDGING_TALK_TO_JUDGES_ABOUT_BEST_SMILE: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 141,
        region=DayOfTheTentacleRegions.FUTURE_HUMAN_SHOW_JUDGING,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_HUMAN_SHOW_JUDGING_TALK_TO_JUDGES_ABOUT_BEST_LAUGH: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 142,
        region=DayOfTheTentacleRegions.FUTURE_HUMAN_SHOW_JUDGING,
        tags=(
            DayOfTheTentacleTags.CORE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_FIELD_VOICE_LINE_IT_LOOKS_PRETTY_MUCH_THE_SAME: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 143,
        region=DayOfTheTentacleRegions.PAST_FIELD,
        tags=(
            DayOfTheTentacleTags.VOICE_LINE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_OUTHOUSES_VOICE_LINE_ID_RATHER_USE_A_TREE: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 144,
        region=DayOfTheTentacleRegions.PAST_OUTHOUSES,
        tags=(
            DayOfTheTentacleTags.VOICE_LINE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_OUTHOUSES_VOICE_LINE_NAH_IT_STINKS: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 145,
        region=DayOfTheTentacleRegions.PAST_OUTHOUSES,
        tags=(
            DayOfTheTentacleTags.VOICE_LINE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_LOBBY_VOICE_LINE_COOL_THE_ROOM_CLERKS_A_MUMMY: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 146,
        region=DayOfTheTentacleRegions.PAST_LOBBY,
        tags=(
            DayOfTheTentacleTags.VOICE_LINE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_BASEMENT_LAB_VOICE_LINE_ITS_COVERED_WITH_PLANS_AND_JUNK: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 147,
        region=DayOfTheTentacleRegions.PAST_BASEMENT_LAB,
        tags=(
            DayOfTheTentacleTags.VOICE_LINE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_SECOND_FLOOR_HALLWAY_VOICE_LINE_THESED_LOOK_BETTER_ON_VELVET: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 148,
        region=DayOfTheTentacleRegions.PAST_SECOND_FLOOR_HALLWAY,
        tags=(
            DayOfTheTentacleTags.VOICE_LINE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_GEORGE_WASHINGTONS_ROOM_VOICE_LINE_WHEEE: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 149,
        region=DayOfTheTentacleRegions.PAST_GEORGE_WASHINGTONS_ROOM,
        tags=(
            DayOfTheTentacleTags.VOICE_LINE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_BEN_FRANKLINS_ROOM_VOICE_LINE_PROBABLY_THE_UNDERWEAR_DRAWER: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 150,
        region=DayOfTheTentacleRegions.PAST_BEN_FRANKLINS_ROOM,
        tags=(
            DayOfTheTentacleTags.VOICE_LINE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_BEN_FRANKLINS_ROOM_VOICE_LINE_I_WOULDNT_KNOW_A_MISTAKE: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 151,
        region=DayOfTheTentacleRegions.PAST_BEN_FRANKLINS_ROOM,
        tags=(
            DayOfTheTentacleTags.VOICE_LINE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_BETSY_ROSSS_ROOM_VOICE_LINE_THAT_WOULD_MAKE_A_KILLER_T_SHIRT: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 152,
        region=DayOfTheTentacleRegions.PAST_BETSY_ROSSS_ROOM,
        tags=(
            DayOfTheTentacleTags.VOICE_LINE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_THIRD_FLOOR_HALLWAY_VOICE_LINE_A_HORSE_IS_A_HORSE_OF_COURSE: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 153,
        region=DayOfTheTentacleRegions.PAST_THIRD_FLOOR_HALLWAY,
        tags=(
            DayOfTheTentacleTags.VOICE_LINE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_NED_AND_JEDS_ROOM_VOICE_LINE_THESE_DUDES_MIGHT_GET_MAD: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 154,
        region=DayOfTheTentacleRegions.PAST_NED_AND_JEDS_ROOM,
        tags=(
            DayOfTheTentacleTags.VOICE_LINE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_ATTIC_VOICE_LINE_VERY_SPARTAN: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 155,
        region=DayOfTheTentacleRegions.PAST_ATTIC,
        tags=(
            DayOfTheTentacleTags.VOICE_LINE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_ROOF_VOICE_LINE_ITS_TOO_COMPLICATED_FOR_ME: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 156,
        region=DayOfTheTentacleRegions.PAST_ROOF,
        tags=(
            DayOfTheTentacleTags.VOICE_LINE_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_MAIN_HALL_VOICE_LINE_USELESS_JUNK_AND_A_GUN: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 157,
        region=DayOfTheTentacleRegions.PRESENT_MAIN_HALL,
        tags=(
            DayOfTheTentacleTags.VOICE_LINE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_KITCHEN_VOICE_LINE_MY_WHAT_A_BIG_COFFEE_MAKER: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 158,
        region=DayOfTheTentacleRegions.PRESENT_KITCHEN,
        tags=(
            DayOfTheTentacleTags.VOICE_LINE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_NURSE_EDNAS_ROOM_VOICE_LINE_IT_LOOKS_LIKE_A_PHYSICS_PROFESSOR: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 159,
        region=DayOfTheTentacleRegions.PRESENT_NURSE_EDNAS_ROOM,
        tags=(
            DayOfTheTentacleTags.VOICE_LINE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_BASEMENT_LAB_VOICE_LINE_IM_SURPRISED_I_EVER_GOT_OUT: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 160,
        region=DayOfTheTentacleRegions.PRESENT_BASEMENT_LAB,
        tags=(
            DayOfTheTentacleTags.VOICE_LINE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_BASEMENT_LAB_VOICE_LINE_WARNING_DO_NOT_TOUCH: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 161,
        region=DayOfTheTentacleRegions.PRESENT_BASEMENT_LAB,
        tags=(
            DayOfTheTentacleTags.VOICE_LINE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_DWAYNES_ROOM_VOICE_LINE_WHAT_DESTROY_ART: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 162,
        region=DayOfTheTentacleRegions.PRESENT_DWAYNES_ROOM,
        tags=(
            DayOfTheTentacleTags.VOICE_LINE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_LAUNDRY_ROOM_VOICE_LINE_THAT_WOULD_MAKE_IT_LOOK_NICER: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 163,
        region=DayOfTheTentacleRegions.PRESENT_LAUNDRY_ROOM,
        tags=(
            DayOfTheTentacleTags.VOICE_LINE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_LOBBY_VOICE_LINE_A_HORTICULTURAL_HORROR: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 164,
        region=DayOfTheTentacleRegions.PRESENT_LOBBY,
        tags=(
            DayOfTheTentacleTags.VOICE_LINE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_OFFICE_VOICE_LINE_SPECTACULARLY_UGLY_FAMILY: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 165,
        region=DayOfTheTentacleRegions.PRESENT_OFFICE,
        tags=(
            DayOfTheTentacleTags.VOICE_LINE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_PARKING_LOT_VOICE_LINE_IT_DIDNT_WORK_FOR_THE_OTHER_GUY: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 166,
        region=DayOfTheTentacleRegions.PRESENT_PARKING_LOT,
        tags=(
            DayOfTheTentacleTags.VOICE_LINE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_PARKING_LOT_VOICE_LINE_THEY_FILMED_MOTEL_SLASHER_3_HERE: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 167,
        region=DayOfTheTentacleRegions.PRESENT_PARKING_LOT,
        tags=(
            DayOfTheTentacleTags.VOICE_LINE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_ROOF_VOICE_LINE_WOW_A_PULLEY: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 168,
        region=DayOfTheTentacleRegions.PRESENT_ROOF,
        tags=(
            DayOfTheTentacleTags.VOICE_LINE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_GREEN_TENTACLES_ROOM_VOICE_LINE_THIS_LOOKS_LIKE_IT_MIGHT_WORK: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 169,
        region=DayOfTheTentacleRegions.PRESENT_GREEN_TENTACLES_ROOM,
        tags=(
            DayOfTheTentacleTags.VOICE_LINE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_THIRD_FLOOR_HALLWAY_VOICE_LINE_JUST_PLAIN_MEAN: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 170,
        region=DayOfTheTentacleRegions.PRESENT_THIRD_FLOOR_HALLWAY,
        tags=(
            DayOfTheTentacleTags.VOICE_LINE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_SLUDGE_RIVER_VOICE_LINE_KEEP_OUT_AREA_CONTAMINATED: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 171,
        region=DayOfTheTentacleRegions.PRESENT_SLUDGE_RIVER,
        tags=(
            DayOfTheTentacleTags.VOICE_LINE_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_TIME_CAPSULE_ROOM_VOICE_LINE_IT_LOOKS_LIKE_A_POODLE: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 172,
        region=DayOfTheTentacleRegions.FUTURE_TIME_CAPSULE_ROOM,
        tags=(
            DayOfTheTentacleTags.VOICE_LINE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_DEAD_COUSIN_TEDS_ROOM_VOICE_LINE_IM_NOT_THAT_CRAZY: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 173,
        region=DayOfTheTentacleRegions.FUTURE_DEAD_COUSIN_TEDS_ROOM,
        tags=(
            DayOfTheTentacleTags.VOICE_LINE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_LOBBY_VOICE_LINE_THIS_FOUR_HUNDRED_YEAR_OLD_CLOCK: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 174,
        region=DayOfTheTentacleRegions.FUTURE_LOBBY,
        tags=(
            DayOfTheTentacleTags.VOICE_LINE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_KITCHEN_VOICE_LINE_OPPRESSIVE_AND_POWER_MAD: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 175,
        region=DayOfTheTentacleRegions.FUTURE_KITCHEN,
        tags=(
            DayOfTheTentacleTags.VOICE_LINE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_FRONT_YARD_VOICE_LINE_I_LIKE_WHAT_THEYVE_DONE: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 176,
        region=DayOfTheTentacleRegions.FUTURE_FRONT_YARD,
        tags=(
            DayOfTheTentacleTags.VOICE_LINE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_BASEMENT_LAB_VOICE_LINE_IM_NOT_INTERESTED_IN_TENTACLE_JUNK: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 177,
        region=DayOfTheTentacleRegions.FUTURE_BASEMENT_LAB,
        tags=(
            DayOfTheTentacleTags.VOICE_LINE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_BASEMENT_LAB_VOICE_LINE_MORE_THAN_A_FRESH_COAT_OF_PAINT: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 178,
        region=DayOfTheTentacleRegions.FUTURE_BASEMENT_LAB,
        tags=(
            DayOfTheTentacleTags.VOICE_LINE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_HUMAN_SHOW_JUDGING_VOICE_LINE_AHHH: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 179,
        region=DayOfTheTentacleRegions.FUTURE_HUMAN_SHOW_JUDGING,
        tags=(
            DayOfTheTentacleTags.VOICE_LINE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_PURPLE_TENTACLES_OFFICE_VOICE_LINE_HE_HASNT_CONQUERED_ANTARCTICA_YET: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 180,
        region=DayOfTheTentacleRegions.FUTURE_PURPLE_TENTACLES_OFFICE,
        tags=(
            DayOfTheTentacleTags.VOICE_LINE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_PURPLE_TENTACLES_OFFICE_VOICE_LINE_ID_LIKE_TO_GUM_UP_HIS_PLANS: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 181,
        region=DayOfTheTentacleRegions.FUTURE_PURPLE_TENTACLES_OFFICE,
        tags=(
            DayOfTheTentacleTags.VOICE_LINE_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_VISITED_FRONT_YARD: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 182,
        region=DayOfTheTentacleRegions.PAST_FRONT_YARD,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_VISITED_FIELD: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 183,
        region=DayOfTheTentacleRegions.PAST_FIELD,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_VISITED_LOBBY: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 184,
        region=DayOfTheTentacleRegions.PAST_LOBBY,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_VISITED_MAIN_HALL: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 185,
        region=DayOfTheTentacleRegions.PAST_MAIN_HALL,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_VISITED_KITCHEN: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 186,
        region=DayOfTheTentacleRegions.PAST_KITCHEN,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_VISITED_LAUNDRY_ROOM: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 187,
        region=DayOfTheTentacleRegions.PAST_LAUNDRY_ROOM,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_VISITED_BASEMENT_LAB: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 188,
        region=DayOfTheTentacleRegions.PAST_BASEMENT_LAB,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_VISITED_SECOND_FLOOR_HALLWAY: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 189,
        region=DayOfTheTentacleRegions.PAST_SECOND_FLOOR_HALLWAY,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_VISITED_GEORGE_WASHINGTONS_ROOM: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 190,
        region=DayOfTheTentacleRegions.PAST_GEORGE_WASHINGTONS_ROOM,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_VISITED_BEN_FRANKLINS_ROOM: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 191,
        region=DayOfTheTentacleRegions.PAST_BEN_FRANKLINS_ROOM,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_VISITED_BETSY_ROSSS_ROOM: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 192,
        region=DayOfTheTentacleRegions.PAST_BETSY_ROSSS_ROOM,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_VISITED_THIRD_FLOOR_HALLWAY: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 193,
        region=DayOfTheTentacleRegions.PAST_THIRD_FLOOR_HALLWAY,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_VISITED_NED_AND_JEDS_ROOM: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 194,
        region=DayOfTheTentacleRegions.PAST_NED_AND_JEDS_ROOM,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_VISITED_ATTIC: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 195,
        region=DayOfTheTentacleRegions.PAST_ATTIC,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PAST_VISITED_ROOF: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 196,
        region=DayOfTheTentacleRegions.PAST_ROOF,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.PAST_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_VISITED_MAIN_HALL: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 197,
        region=DayOfTheTentacleRegions.PRESENT_MAIN_HALL,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_VISITED_KITCHEN: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 198,
        region=DayOfTheTentacleRegions.PRESENT_KITCHEN,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_VISITED_NURSE_EDNAS_ROOM: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 199,
        region=DayOfTheTentacleRegions.PRESENT_NURSE_EDNAS_ROOM,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_VISITED_DWAYNES_ROOM: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 200,
        region=DayOfTheTentacleRegions.PRESENT_DWAYNES_ROOM,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_VISITED_SECOND_FLOOR_HALLWAY: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 201,
        region=DayOfTheTentacleRegions.PRESENT_SECOND_FLOOR_HALLWAY,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_VISITED_SLEEPING_CONVENTIONEERS_ROOM: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 202,
        region=DayOfTheTentacleRegions.PRESENT_SLEEPING_CONVENTIONEERS_ROOM,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_VISITED_LAUNDRY_ROOM: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 203,
        region=DayOfTheTentacleRegions.PRESENT_LAUNDRY_ROOM,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_VISITED_LOBBY: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 204,
        region=DayOfTheTentacleRegions.PRESENT_LOBBY,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_VISITED_VCR_CONTROLS: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 205,
        region=DayOfTheTentacleRegions.PRESENT_VCR_CONTROLS,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_VISITED_FRONT_YARD: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 206,
        region=DayOfTheTentacleRegions.PRESENT_FRONT_YARD,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_VISITED_OFFICE: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 207,
        region=DayOfTheTentacleRegions.PRESENT_OFFICE,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_VISITED_PARKING_LOT: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 208,
        region=DayOfTheTentacleRegions.PRESENT_PARKING_LOT,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_VISITED_ATTIC: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 209,
        region=DayOfTheTentacleRegions.PRESENT_ATTIC,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_VISITED_ROOF: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 210,
        region=DayOfTheTentacleRegions.PRESENT_ROOF,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_VISITED_GREEN_TENTACLES_ROOM: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 211,
        region=DayOfTheTentacleRegions.PRESENT_GREEN_TENTACLES_ROOM,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_VISITED_WEIRD_EDS_ROOM: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 212,
        region=DayOfTheTentacleRegions.PRESENT_WEIRD_EDS_ROOM,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_VISITED_THIRD_FLOOR_HALLWAY: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 213,
        region=DayOfTheTentacleRegions.PRESENT_THIRD_FLOOR_HALLWAY,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_VISITED_SLUDGE_RIVER: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 214,
        region=DayOfTheTentacleRegions.PRESENT_SLUDGE_RIVER,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_VISITED_TIME_CAPSULE_ROOM: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 215,
        region=DayOfTheTentacleRegions.FUTURE_TIME_CAPSULE_ROOM,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_VISITED_DEAD_COUSIN_TEDS_ROOM: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 216,
        region=DayOfTheTentacleRegions.FUTURE_DEAD_COUSIN_TEDS_ROOM,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_VISITED_SECOND_FLOOR_HALLWAY: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 217,
        region=DayOfTheTentacleRegions.FUTURE_SECOND_FLOOR_HALLWAY,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_VISITED_LOBBY: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 218,
        region=DayOfTheTentacleRegions.FUTURE_LOBBY,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_VISITED_KITCHEN: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 219,
        region=DayOfTheTentacleRegions.FUTURE_KITCHEN,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_VISITED_FRONT_YARD: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 220,
        region=DayOfTheTentacleRegions.FUTURE_FRONT_YARD,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_VISITED_DOCTORS_OFFICE: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 221,
        region=DayOfTheTentacleRegions.FUTURE_DOCTORS_OFFICE,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_VISITED_MAIN_HALL: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 222,
        region=DayOfTheTentacleRegions.FUTURE_MAIN_HALL,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_VISITED_BASEMENT_LAB: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 223,
        region=DayOfTheTentacleRegions.FUTURE_BASEMENT_LAB,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_VISITED_HUMAN_SHOW: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 224,
        region=DayOfTheTentacleRegions.FUTURE_HUMAN_SHOW,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_VISITED_HUMAN_SHOW_JUDGING: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 225,
        region=DayOfTheTentacleRegions.FUTURE_HUMAN_SHOW_JUDGING,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_VISITED_ROOF: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 226,
        region=DayOfTheTentacleRegions.FUTURE_ROOF,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_VISITED_KUMQUAT_TREE: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 227,
        region=DayOfTheTentacleRegions.FUTURE_KUMQUAT_TREE,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_VISITED_LAUNDRY_ROOM: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 228,
        region=DayOfTheTentacleRegions.FUTURE_LAUNDRY_ROOM,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_VISITED_PURPLE_TENTACLES_OFFICE: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 229,
        region=DayOfTheTentacleRegions.FUTURE_PURPLE_TENTACLES_OFFICE,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.FUTURE_LOCATION,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_VISITED_ATTIC_LANDING: DayOfTheTentacleLocationData(
        archipelago_id=location_offset + 230,
        region=DayOfTheTentacleRegions.PRESENT_ATTIC_LANDING,
        tags=(
            DayOfTheTentacleTags.VISITED_LOCATION,
            DayOfTheTentacleTags.PRESENT_LOCATION,
        ),
    ),
}

from typing import Dict, Optional

from rule_builder.rules import Rule, And, CanReachLocation, Has, HasAll, HasAny

from ..enums import (
    DayOfTheTentacleItems,
    DayOfTheTentacleLocations,
    DayOfTheTentacleRegions,
)


EntranceRuleData = Dict[DayOfTheTentacleRegions, Dict[DayOfTheTentacleRegions, Optional[Rule]]]

entrance_rule_data: EntranceRuleData = {
    DayOfTheTentacleRegions.PAST_FRONT_YARD: {
        DayOfTheTentacleRegions.PAST_FIELD: None,
        DayOfTheTentacleRegions.PAST_LOBBY: None,
    },
    DayOfTheTentacleRegions.PAST_FIELD: {
        DayOfTheTentacleRegions.PAST_FRONT_YARD: None,
        DayOfTheTentacleRegions.PAST_OUTHOUSES: None,
    },
    DayOfTheTentacleRegions.PAST_FIELD_KITE_SCENE: {
        DayOfTheTentacleRegions.PAST_FIELD: None,
    },
    DayOfTheTentacleRegions.PAST_OUTHOUSES: {
        DayOfTheTentacleRegions.PAST_FIELD: None,
        DayOfTheTentacleRegions.CHRON_O_JOHN_PAST: None,
    },
    DayOfTheTentacleRegions.PAST_LOBBY: {
        DayOfTheTentacleRegions.PAST_FRONT_YARD: None,
        DayOfTheTentacleRegions.PAST_MAIN_HALL: None,
        DayOfTheTentacleRegions.PAST_BASEMENT_LAB: None,
        DayOfTheTentacleRegions.PAST_SECOND_FLOOR_HALLWAY: None,
    },
    DayOfTheTentacleRegions.PAST_MAIN_HALL: {
        DayOfTheTentacleRegions.PAST_LOBBY: None,
        DayOfTheTentacleRegions.PAST_KITCHEN: None,
        DayOfTheTentacleRegions.PAST_ROOF: None,
    },
    DayOfTheTentacleRegions.PAST_KITCHEN: {
        DayOfTheTentacleRegions.PAST_MAIN_HALL: None,
        DayOfTheTentacleRegions.PAST_LAUNDRY_ROOM: None,
    },
    DayOfTheTentacleRegions.PAST_LAUNDRY_ROOM: {
        DayOfTheTentacleRegions.PAST_KITCHEN: None,
    },
    DayOfTheTentacleRegions.PAST_BASEMENT_LAB: {
        DayOfTheTentacleRegions.PAST_LOBBY: None,
    },
    DayOfTheTentacleRegions.PAST_SECOND_FLOOR_HALLWAY: {
        DayOfTheTentacleRegions.PAST_LOBBY: None,
        DayOfTheTentacleRegions.PAST_GEORGE_WASHINGTONS_ROOM: None,
        DayOfTheTentacleRegions.PAST_BEN_FRANKLINS_ROOM: None,
        DayOfTheTentacleRegions.PAST_BETSY_ROSSS_ROOM: None,
        DayOfTheTentacleRegions.PAST_THIRD_FLOOR_HALLWAY: None,
    },
    DayOfTheTentacleRegions.PAST_GEORGE_WASHINGTONS_ROOM: {
        DayOfTheTentacleRegions.PAST_SECOND_FLOOR_HALLWAY: None,
    },
    DayOfTheTentacleRegions.PAST_BEN_FRANKLINS_ROOM: {
        DayOfTheTentacleRegions.PAST_SECOND_FLOOR_HALLWAY: None,
        DayOfTheTentacleRegions.PAST_FIELD_KITE_SCENE: And(
            Has(
                DayOfTheTentacleItems.LAB_COAT.value,
            ),
            CanReachLocation(
                DayOfTheTentacleLocations.PAST_FRONT_YARD_USE_BUCKET_WITH_CARRIAGE.value,
                parent_region_name=DayOfTheTentacleRegions.PAST_FRONT_YARD.value,
            ),
        ),
    },
    DayOfTheTentacleRegions.PAST_BETSY_ROSSS_ROOM: {
        DayOfTheTentacleRegions.PAST_SECOND_FLOOR_HALLWAY: None,
    },
    DayOfTheTentacleRegions.PAST_THIRD_FLOOR_HALLWAY: {
        DayOfTheTentacleRegions.PAST_SECOND_FLOOR_HALLWAY: None,
        DayOfTheTentacleRegions.PAST_NED_AND_JEDS_ROOM: None,
        DayOfTheTentacleRegions.PAST_ATTIC: None,
    },
    DayOfTheTentacleRegions.PAST_NED_AND_JEDS_ROOM: {
        DayOfTheTentacleRegions.PAST_THIRD_FLOOR_HALLWAY: None,
    },
    DayOfTheTentacleRegions.PAST_ATTIC: {
        DayOfTheTentacleRegions.PAST_THIRD_FLOOR_HALLWAY: None,
        DayOfTheTentacleRegions.PAST_ROOF: None,
    },
    DayOfTheTentacleRegions.PAST_ROOF: {
        DayOfTheTentacleRegions.PAST_MAIN_HALL: None,
        DayOfTheTentacleRegions.PAST_ATTIC: None,
    },
    DayOfTheTentacleRegions.PRESENT_MAIN_HALL: {
        DayOfTheTentacleRegions.PRESENT_KITCHEN: None,
        DayOfTheTentacleRegions.PRESENT_LOBBY: None,
        DayOfTheTentacleRegions.PRESENT_ROOF: None,
    },
    DayOfTheTentacleRegions.PRESENT_KITCHEN: {
        DayOfTheTentacleRegions.PRESENT_MAIN_HALL: None,
        DayOfTheTentacleRegions.PRESENT_LAUNDRY_ROOM: None,
    },
    DayOfTheTentacleRegions.PRESENT_NURSE_EDNAS_ROOM: {
        DayOfTheTentacleRegions.PRESENT_VCR_CONTROLS: CanReachLocation(
            DayOfTheTentacleLocations.PRESENT_NURSE_EDNAS_ROOM_PUSH_NURSE_EDNA.value,
            parent_region_name=DayOfTheTentacleRegions.PRESENT_NURSE_EDNAS_ROOM.value,
        ),
        DayOfTheTentacleRegions.PRESENT_THIRD_FLOOR_HALLWAY: None,
    },
    DayOfTheTentacleRegions.PRESENT_BASEMENT_LAB: {
        DayOfTheTentacleRegions.PRESENT_LOBBY: None,
        DayOfTheTentacleRegions.CHRON_O_JOHN_PRESENT: None,
    },
    DayOfTheTentacleRegions.PRESENT_DWAYNES_ROOM: {
        DayOfTheTentacleRegions.PRESENT_SECOND_FLOOR_HALLWAY: None,
    },
    DayOfTheTentacleRegions.PRESENT_SECOND_FLOOR_HALLWAY: {
        DayOfTheTentacleRegions.PRESENT_DWAYNES_ROOM: None,
        DayOfTheTentacleRegions.PRESENT_SLEEPING_CONVENTIONEERS_ROOM: None,
        DayOfTheTentacleRegions.PRESENT_LOBBY: None,
        DayOfTheTentacleRegions.PRESENT_GREEN_TENTACLES_ROOM: None,
        DayOfTheTentacleRegions.PRESENT_THIRD_FLOOR_HALLWAY: None,
    },
    DayOfTheTentacleRegions.PRESENT_SLEEPING_CONVENTIONEERS_ROOM: {
        DayOfTheTentacleRegions.PRESENT_SECOND_FLOOR_HALLWAY: None,
    },
    DayOfTheTentacleRegions.PRESENT_LAUNDRY_ROOM: {
        DayOfTheTentacleRegions.PRESENT_KITCHEN: None,
    },
    DayOfTheTentacleRegions.PRESENT_LOBBY: {
        DayOfTheTentacleRegions.PRESENT_MAIN_HALL: None,
        DayOfTheTentacleRegions.PRESENT_BASEMENT_LAB: None,
        DayOfTheTentacleRegions.PRESENT_SECOND_FLOOR_HALLWAY: None,
        DayOfTheTentacleRegions.PRESENT_FRONT_YARD: None,
        DayOfTheTentacleRegions.PRESENT_OFFICE: None,
    },
    DayOfTheTentacleRegions.PRESENT_VCR_CONTROLS: {
        DayOfTheTentacleRegions.PRESENT_NURSE_EDNAS_ROOM: None,
    },
    DayOfTheTentacleRegions.PRESENT_FRONT_YARD: {
        DayOfTheTentacleRegions.PRESENT_LOBBY: None,
        DayOfTheTentacleRegions.PRESENT_PARKING_LOT: None,
    },
    DayOfTheTentacleRegions.PRESENT_OFFICE: {
        DayOfTheTentacleRegions.PRESENT_LOBBY: None,
    },
    DayOfTheTentacleRegions.PRESENT_PARKING_LOT: {
        DayOfTheTentacleRegions.PRESENT_FRONT_YARD: None,
        DayOfTheTentacleRegions.PRESENT_SLUDGE_RIVER: None,
    },
    DayOfTheTentacleRegions.PRESENT_ATTIC: {
        DayOfTheTentacleRegions.PRESENT_ROOF: None,
        DayOfTheTentacleRegions.PRESENT_ATTIC_LANDING: None,
    },
    DayOfTheTentacleRegions.PRESENT_ATTIC_LANDING: {
        DayOfTheTentacleRegions.PRESENT_ATTIC: None,
        DayOfTheTentacleRegions.PRESENT_THIRD_FLOOR_HALLWAY: None,
    },
    DayOfTheTentacleRegions.PRESENT_ROOF: {
        DayOfTheTentacleRegions.PRESENT_MAIN_HALL: None,
        DayOfTheTentacleRegions.PRESENT_ATTIC: None,
    },
    DayOfTheTentacleRegions.PRESENT_GREEN_TENTACLES_ROOM: {
        DayOfTheTentacleRegions.PRESENT_SECOND_FLOOR_HALLWAY: None,
    },
    DayOfTheTentacleRegions.PRESENT_WEIRD_EDS_ROOM: {
        DayOfTheTentacleRegions.PRESENT_THIRD_FLOOR_HALLWAY: None,
    },
    DayOfTheTentacleRegions.PRESENT_THIRD_FLOOR_HALLWAY: {
        DayOfTheTentacleRegions.PRESENT_ATTIC_LANDING: None,
        DayOfTheTentacleRegions.PRESENT_NURSE_EDNAS_ROOM: None,
        DayOfTheTentacleRegions.PRESENT_SECOND_FLOOR_HALLWAY: None,
        DayOfTheTentacleRegions.PRESENT_WEIRD_EDS_ROOM: Has(
            DayOfTheTentacleItems.STAMP_ALBUM.value,
        ),
    },
    DayOfTheTentacleRegions.PRESENT_SLUDGE_RIVER: {
        DayOfTheTentacleRegions.PRESENT_PARKING_LOT: None,
    },
    DayOfTheTentacleRegions.FUTURE_TIME_CAPSULE_ROOM: {
        DayOfTheTentacleRegions.FUTURE_SECOND_FLOOR_HALLWAY: None,
    },
    DayOfTheTentacleRegions.FUTURE_DEAD_COUSIN_TEDS_ROOM: {
        DayOfTheTentacleRegions.FUTURE_SECOND_FLOOR_HALLWAY: None,
    },
    DayOfTheTentacleRegions.FUTURE_SECOND_FLOOR_HALLWAY: {
        DayOfTheTentacleRegions.FUTURE_TIME_CAPSULE_ROOM: None,
        DayOfTheTentacleRegions.FUTURE_DEAD_COUSIN_TEDS_ROOM: None,
        DayOfTheTentacleRegions.FUTURE_LOBBY: None,
        DayOfTheTentacleRegions.FUTURE_HUMAN_SHOW: None,
        DayOfTheTentacleRegions.FUTURE_PURPLE_TENTACLES_OFFICE: None,
    },
    DayOfTheTentacleRegions.FUTURE_LOBBY: {
        DayOfTheTentacleRegions.FUTURE_SECOND_FLOOR_HALLWAY: CanReachLocation(
            DayOfTheTentacleLocations.FUTURE_USE_FLAG.value,
            parent_region_name=DayOfTheTentacleRegions.FUTURE_DOCTORS_OFFICE.value,
        ),
        DayOfTheTentacleRegions.FUTURE_FRONT_YARD: None,
        DayOfTheTentacleRegions.FUTURE_DOCTORS_OFFICE: None,
        DayOfTheTentacleRegions.FUTURE_MAIN_HALL: None,
        DayOfTheTentacleRegions.FUTURE_BASEMENT_LAB: CanReachLocation(
            DayOfTheTentacleLocations.FUTURE_KENNEL_USE_CAT_IN_KENNEL.value,
            parent_region_name=DayOfTheTentacleRegions.FUTURE_KENNEL.value,
        ),
    },
    DayOfTheTentacleRegions.FUTURE_KITCHEN: {
        DayOfTheTentacleRegions.FUTURE_MAIN_HALL: None,
        DayOfTheTentacleRegions.FUTURE_LAUNDRY_ROOM: None,
    },
    DayOfTheTentacleRegions.FUTURE_FRONT_YARD: {
        DayOfTheTentacleRegions.FUTURE_LOBBY: None,
        DayOfTheTentacleRegions.FUTURE_KUMQUAT_TREE: None,
    },
    DayOfTheTentacleRegions.FUTURE_DOCTORS_OFFICE: {
        DayOfTheTentacleRegions.FUTURE_LOBBY: None,
    },
    DayOfTheTentacleRegions.FUTURE_KENNEL: {
        DayOfTheTentacleRegions.FUTURE_MAIN_HALL: None,
        DayOfTheTentacleRegions.FUTURE_DOCTORS_OFFICE: None,
        DayOfTheTentacleRegions.FUTURE_FRONT_YARD: None,
        DayOfTheTentacleRegions.CHRON_O_JOHN_FUTURE: None,
    },
    DayOfTheTentacleRegions.FUTURE_MAIN_HALL: {
        DayOfTheTentacleRegions.FUTURE_LOBBY: None,
        DayOfTheTentacleRegions.FUTURE_KITCHEN: None,
        DayOfTheTentacleRegions.FUTURE_KENNEL: None,
        DayOfTheTentacleRegions.FUTURE_ROOF: None,
    },
    DayOfTheTentacleRegions.FUTURE_BASEMENT_LAB: {
        DayOfTheTentacleRegions.FUTURE_LOBBY: None,
    },
    DayOfTheTentacleRegions.FUTURE_HUMAN_SHOW: {
        DayOfTheTentacleRegions.FUTURE_SECOND_FLOOR_HALLWAY: None,
        DayOfTheTentacleRegions.FUTURE_HUMAN_SHOW_JUDGING: None,
    },
    DayOfTheTentacleRegions.FUTURE_HUMAN_SHOW_JUDGING: {
        DayOfTheTentacleRegions.FUTURE_HUMAN_SHOW: None,
    },
    DayOfTheTentacleRegions.FUTURE_ROOF: {
        DayOfTheTentacleRegions.FUTURE_MAIN_HALL: None,
    },
    DayOfTheTentacleRegions.FUTURE_KUMQUAT_TREE: {
        DayOfTheTentacleRegions.FUTURE_FRONT_YARD: None,
    },
    DayOfTheTentacleRegions.FUTURE_LAUNDRY_ROOM: {
        DayOfTheTentacleRegions.FUTURE_KITCHEN: None,
    },
    DayOfTheTentacleRegions.FUTURE_PURPLE_TENTACLES_OFFICE: {
        DayOfTheTentacleRegions.FUTURE_SECOND_FLOOR_HALLWAY: None,
    },
    DayOfTheTentacleRegions.CHRON_O_JOHN: {
        DayOfTheTentacleRegions.CHRON_O_JOHN_PAST: Has(
            DayOfTheTentacleItems.CHARACTER_HOAGIE.value,
        ),
        DayOfTheTentacleRegions.CHRON_O_JOHN_PRESENT: Has(
            DayOfTheTentacleItems.CHARACTER_BERNARD.value,
        ),
        DayOfTheTentacleRegions.CHRON_O_JOHN_FUTURE: Has(
            DayOfTheTentacleItems.CHARACTER_LAVERNE.value,
        ),
    },
    DayOfTheTentacleRegions.CHRON_O_JOHN_PAST: {
        DayOfTheTentacleRegions.PAST_OUTHOUSES: None,
        DayOfTheTentacleRegions.CHRON_O_JOHN: None,
    },
    DayOfTheTentacleRegions.CHRON_O_JOHN_PRESENT: {
        DayOfTheTentacleRegions.PRESENT_BASEMENT_LAB: None,
        DayOfTheTentacleRegions.CHRON_O_JOHN: None,
    },
    DayOfTheTentacleRegions.CHRON_O_JOHN_FUTURE: {
        DayOfTheTentacleRegions.CHRON_O_JOHN: None,
        DayOfTheTentacleRegions.FUTURE_KENNEL: None,
    },
}


LocationRuleData = Dict[DayOfTheTentacleLocations, Optional[Rule]]

location_rule_data: LocationRuleData = {
    DayOfTheTentacleLocations.PRESENT_LOBBY_PICK_UP_HELP_WANTED_SIGN: None,
    DayOfTheTentacleLocations.PRESENT_LOBBY_PICK_UP_FLIER: None,
    DayOfTheTentacleLocations.PRESENT_LOBBY_PICK_UP_DIME: None,
    DayOfTheTentacleLocations.PRESENT_OFFICE_PICK_UP_SWISS_BANKBOOK: None,
    DayOfTheTentacleLocations.PRESENT_OFFICE_PICK_UP_BOOBOO_B_GONE: None,
    DayOfTheTentacleLocations.PAST_FRONT_YARD_PICK_UP_LETTER: None,
    DayOfTheTentacleLocations.PAST_KITCHEN_PICK_UP_OIL: None,
    DayOfTheTentacleLocations.PAST_KITCHEN_PICK_UP_SPAGHETTI: None,
    DayOfTheTentacleLocations.PAST_LAUNDRY_ROOM_PICK_UP_BUCKET: None,
    DayOfTheTentacleLocations.PAST_LAUNDRY_ROOM_PICK_UP_BRUSH: None,
    DayOfTheTentacleLocations.PAST_KITCHEN_USE_BUCKET_WITH_WATER_PUMP: Has(
        DayOfTheTentacleItems.BUCKET.value,
    ),
    DayOfTheTentacleLocations.PAST_BASEMENT_LAB_PICK_UP_LEFT_HANDED_HAMMER: None,
    DayOfTheTentacleLocations.PAST_BASEMENT_LAB_GIVE_PATENT_APPLICATION_TO_RED_EDISON: Has(
        DayOfTheTentacleItems.PATENT_APPLICATION.value,
    ),
    DayOfTheTentacleLocations.PAST_GEORGE_WASHINGTONS_ROOM_USE_GEORGES_BED: None,
    DayOfTheTentacleLocations.PAST_GEORGE_WASHINGTONS_ROOM_PULL_CORD: None,
    DayOfTheTentacleLocations.PAST_SECOND_FLOOR_HALLWAY_PICK_UP_SOAP: And(
        CanReachLocation(
            DayOfTheTentacleLocations.PAST_GEORGE_WASHINGTONS_ROOM_USE_GEORGES_BED.value,
            parent_region_name=DayOfTheTentacleRegions.PAST_GEORGE_WASHINGTONS_ROOM.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.PAST_GEORGE_WASHINGTONS_ROOM_PULL_CORD.value,
            parent_region_name=DayOfTheTentacleRegions.PAST_GEORGE_WASHINGTONS_ROOM.value,
        ),
    ),
    DayOfTheTentacleLocations.PAST_BEN_FRANKLINS_ROOM_PICK_UP_WINE_BOTTLE: None,
    DayOfTheTentacleLocations.PAST_NED_AND_JEDS_ROOM_USE_LEFT_HANDED_HAMMER_WITH_BARREL: Has(
        DayOfTheTentacleItems.LEFT_HANDED_HAMMER.value,
    ),
    DayOfTheTentacleLocations.PAST_ATTIC_USE_NEDS_BED: None,
    DayOfTheTentacleLocations.PAST_ATTIC_USE_SQUEAKY_MATTRESS: CanReachLocation(
        DayOfTheTentacleLocations.PAST_ATTIC_USE_NEDS_BED.value,
        parent_region_name=DayOfTheTentacleRegions.PAST_ATTIC.value,
    ),
    DayOfTheTentacleLocations.PAST_ATTIC_PICK_UP_SQUEAKY_MOUSE_TOY: CanReachLocation(
        DayOfTheTentacleLocations.PAST_ATTIC_USE_SQUEAKY_MATTRESS.value,
        parent_region_name=DayOfTheTentacleRegions.PAST_ATTIC.value,
    ),
    DayOfTheTentacleLocations.PAST_ATTIC_PICK_UP_RED_PAINT: None,
    DayOfTheTentacleLocations.PAST_MAIN_HALL_USE_WINE_BOTTLE_WITH_TIME_CAPSULE: Has(
        DayOfTheTentacleItems.WINE_BOTTLE.value,
    ),
    DayOfTheTentacleLocations.PAST_OUTHOUSES_USE_RED_PAINT_WITH_KUMQUAT_TREE: Has(
        DayOfTheTentacleItems.RED_PAINT.value,
    ),
    DayOfTheTentacleLocations.PAST_MAIN_HALL_TALK_TO_GEORGE_WASHINGTON_ABOUT_THE_TREE: CanReachLocation(
        DayOfTheTentacleLocations.PAST_OUTHOUSES_USE_RED_PAINT_WITH_KUMQUAT_TREE.value,
        parent_region_name=DayOfTheTentacleRegions.PAST_OUTHOUSES.value,
    ),
    DayOfTheTentacleLocations.PRESENT_SLEEPING_CONVENTIONEERS_ROOM_PICK_UP_KEYS: None,
    DayOfTheTentacleLocations.PRESENT_DWAYNES_ROOM_GIVE_LETTER_TO_DWAYNE: Has(
        DayOfTheTentacleItems.LETTER.value,
    ),
    DayOfTheTentacleLocations.PRESENT_DWAYNES_ROOM_PICK_UP_FLAG_GUN: CanReachLocation(
        DayOfTheTentacleLocations.PRESENT_DWAYNES_ROOM_GIVE_LETTER_TO_DWAYNE.value,
        parent_region_name=DayOfTheTentacleRegions.PRESENT_DWAYNES_ROOM.value,
    ),
    DayOfTheTentacleLocations.PRESENT_DWAYNES_ROOM_PICK_UP_DISAPPEARING_INK: None,
    DayOfTheTentacleLocations.PRESENT_GREEN_TENTACLES_ROOM_PUSH_SPEAKER: None,
    DayOfTheTentacleLocations.PRESENT_GREEN_TENTACLES_ROOM_USE_STEREO: None,
    DayOfTheTentacleLocations.PRESENT_GREEN_TENTACLES_ROOM_PICK_UP_VIDEOTAPE: None,
    DayOfTheTentacleLocations.PRESENT_LOBBY_PICK_UP_FAKE_BARF: And(
        CanReachLocation(
            DayOfTheTentacleLocations.PRESENT_GREEN_TENTACLES_ROOM_PUSH_SPEAKER.value,
            parent_region_name=DayOfTheTentacleRegions.PRESENT_GREEN_TENTACLES_ROOM.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.PRESENT_GREEN_TENTACLES_ROOM_USE_STEREO.value,
            parent_region_name=DayOfTheTentacleRegions.PRESENT_GREEN_TENTACLES_ROOM.value,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_PARKING_LOT_GIVE_KEYS_TO_MAN_IN_SKI_MASK: Has(
        DayOfTheTentacleItems.KEYS.value,
    ),
    DayOfTheTentacleLocations.PRESENT_LOBBY_USE_CROWBAR_WITH_GUM: Has(
        DayOfTheTentacleItems.CROWBAR.value,
    ),
    DayOfTheTentacleLocations.PRESENT_USE_GUM_WITH_A_DIME_STUCK_IN_IT: Has(
        DayOfTheTentacleItems.GUM_WITH_A_DIME_STUCK_IN_IT.value,
    ),
    DayOfTheTentacleLocations.PRESENT_SLEEPING_CONVENTIONEERS_ROOM_USE_DIME_WITH_FICKLEFINGERS: HasAny(
        DayOfTheTentacleItems.DIME.value,
        DayOfTheTentacleItems.STICKY_DIME.value,
    ),
    DayOfTheTentacleLocations.PRESENT_SLEEPING_CONVENTIONEERS_ROOM_PICK_UP_SWEATER: HasAll(
        DayOfTheTentacleItems.DIME.value,
        DayOfTheTentacleItems.STICKY_DIME.value,
    ),
    DayOfTheTentacleLocations.PRESENT_SECOND_FLOOR_HALLWAY_USE_CROWBAR_WITH_CANDY_MACHINE: Has(
        DayOfTheTentacleItems.CROWBAR.value,
    ),
    DayOfTheTentacleLocations.PRESENT_SECOND_FLOOR_HALLWAY_PICK_UP_QUARTERS: CanReachLocation(
        DayOfTheTentacleLocations.PRESENT_SECOND_FLOOR_HALLWAY_USE_CROWBAR_WITH_CANDY_MACHINE.value,
        parent_region_name=DayOfTheTentacleRegions.PRESENT_SECOND_FLOOR_HALLWAY.value,
    ),
    DayOfTheTentacleLocations.PRESENT_WEIRD_EDS_ROOM_PICK_UP_HAMSTER: None,
    DayOfTheTentacleLocations.PRESENT_WEIRD_EDS_ROOM_USE_DISAPPEARING_INK_WITH_STAMP_ALBUM: Has(
        DayOfTheTentacleItems.DISAPPEARING_INK.value,
    ),
    DayOfTheTentacleLocations.PRESENT_THIRD_FLOOR_HALLWAY_PICK_UP_STAMP: CanReachLocation(
        DayOfTheTentacleLocations.PRESENT_WEIRD_EDS_ROOM_USE_DISAPPEARING_INK_WITH_STAMP_ALBUM.value,
        parent_region_name=DayOfTheTentacleRegions.PRESENT_WEIRD_EDS_ROOM.value,
    ),
    DayOfTheTentacleLocations.PRESENT_THIRD_FLOOR_HALLWAY_PICK_UP_STAMP_ALBUM: CanReachLocation(
        DayOfTheTentacleLocations.PRESENT_WEIRD_EDS_ROOM_USE_DISAPPEARING_INK_WITH_STAMP_ALBUM.value,
        parent_region_name=DayOfTheTentacleRegions.PRESENT_WEIRD_EDS_ROOM.value,
    ),
    DayOfTheTentacleLocations.PRESENT_WEIRD_EDS_ROOM_GIVE_STAMP_ALBUM_TO_WEIRD_ED: And(
        Has(
            DayOfTheTentacleItems.STAMP_ALBUM.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.PRESENT_WEIRD_EDS_ROOM_USE_DISAPPEARING_INK_WITH_STAMP_ALBUM.value,
            parent_region_name=DayOfTheTentacleRegions.PRESENT_WEIRD_EDS_ROOM.value,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_SECOND_FLOOR_HALLWAY_USE_HAMSTER_WITH_ICE_MACHINE: Has(
        DayOfTheTentacleItems.HAMSTER.value,
    ),
    DayOfTheTentacleLocations.PRESENT_MAIN_HALL_USE_FLAG_GUN_WITH_CIGAR_LIGHTER: Has(
        DayOfTheTentacleItems.FLAG_GUN.value,
    ),
    DayOfTheTentacleLocations.PRESENT_MAIN_HALL_PICK_UP_CHATTERING_TEETH: None,
    DayOfTheTentacleLocations.PRESENT_KITCHEN_PICK_UP_FORK: None,
    DayOfTheTentacleLocations.PRESENT_KITCHEN_PICK_UP_COFFEE: None,
    DayOfTheTentacleLocations.PRESENT_KITCHEN_PICK_UP_DECAF_COFFEE: None,
    DayOfTheTentacleLocations.PRESENT_LAUNDRY_ROOM_PICK_UP_FUNNEL: None,
    DayOfTheTentacleLocations.PRESENT_LAUNDRY_ROOM_USE_SWEATER_WITH_DRYER: Has(
        DayOfTheTentacleItems.SWEATER.value,
    ),
    DayOfTheTentacleLocations.PRESENT_ROOF_PICK_UP_CRANK: None,
    DayOfTheTentacleLocations.PRESENT_MAIN_HALL_TALK_TO_CIGAR_SALESMAN: CanReachLocation(
        DayOfTheTentacleLocations.PRESENT_MAIN_HALL_USE_FLAG_GUN_WITH_CIGAR_LIGHTER.value,
        parent_region_name=DayOfTheTentacleRegions.PRESENT_MAIN_HALL.value,
    ),
    DayOfTheTentacleLocations.PRESENT_LAUNDRY_ROOM_USE_QUARTERS_WITH_DRYER_COIN_SLOT: And(
        Has(
            DayOfTheTentacleItems.QUARTERS.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.PRESENT_LAUNDRY_ROOM_USE_SWEATER_WITH_DRYER.value,
            parent_region_name=DayOfTheTentacleRegions.PRESENT_LAUNDRY_ROOM.value,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_DOCTORS_OFFICE_PICK_UP_TENTACLE_CHART: None,
    DayOfTheTentacleLocations.PAST_USE_SOAP_WITH_BUCKET: And(
        HasAll(
            DayOfTheTentacleItems.SOAP.value,
            DayOfTheTentacleItems.BUCKET.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.PAST_KITCHEN_USE_BUCKET_WITH_WATER_PUMP.value,
            parent_region_name=DayOfTheTentacleRegions.PAST_KITCHEN.value,
        ),
    ),
    DayOfTheTentacleLocations.PAST_FRONT_YARD_USE_BUCKET_WITH_CARRIAGE: And(
        HasAll(
            DayOfTheTentacleItems.BUCKET.value,
            DayOfTheTentacleItems.BRUSH.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.PAST_USE_SOAP_WITH_BUCKET.value,
            parent_region_name=DayOfTheTentacleRegions.PAST_SECOND_FLOOR_HALLWAY.value,
        ),
    ),
    DayOfTheTentacleLocations.PAST_MAIN_HALL_USE_FLIER_WITH_SUGGESTION_BOX: Has(
        DayOfTheTentacleItems.FLIER.value,
    ),
    DayOfTheTentacleLocations.PAST_MAIN_HALL_GIVE_EXPLODING_CIGAR_TO_GEORGE_WASHINGTON: HasAll(
        DayOfTheTentacleItems.EXPLODING_CIGAR.value,
        DayOfTheTentacleItems.CIGAR_LIGHTER.value,
    ),
    DayOfTheTentacleLocations.PAST_MAIN_HALL_GIVE_CHATTERING_TEETH_TO_GEORGE_WASHINGTON: And(
        Has(
            DayOfTheTentacleItems.CHATTERING_TEETH.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.PAST_MAIN_HALL_GIVE_EXPLODING_CIGAR_TO_GEORGE_WASHINGTON.value,
            parent_region_name=DayOfTheTentacleRegions.PAST_MAIN_HALL.value,
        ),
    ),
    DayOfTheTentacleLocations.PAST_MAIN_HALL_PICK_UP_BLANKET: CanReachLocation(
        DayOfTheTentacleLocations.PAST_MAIN_HALL_GIVE_CHATTERING_TEETH_TO_GEORGE_WASHINGTON.value,
        parent_region_name=DayOfTheTentacleRegions.PAST_MAIN_HALL.value,
    ),
    DayOfTheTentacleLocations.PAST_BETSY_ROSSS_ROOM_USE_TENTACLE_CHART_WITH_PATTERNS: Has(
        DayOfTheTentacleItems.TENTACLE_CHART.value,
    ),
    DayOfTheTentacleLocations.PAST_THIRD_FLOOR_HALLWAY_USE_TEXTBOOK_WITH_HORSE: Has(
        DayOfTheTentacleItems.TEXTBOOK.value,
    ),
    DayOfTheTentacleLocations.PAST_THIRD_FLOOR_HALLWAY_PICK_UP_DENTURES: CanReachLocation(
        DayOfTheTentacleLocations.PAST_THIRD_FLOOR_HALLWAY_USE_TEXTBOOK_WITH_HORSE.value,
        parent_region_name=DayOfTheTentacleRegions.PAST_THIRD_FLOOR_HALLWAY.value,
    ),
    DayOfTheTentacleLocations.PAST_ROOF_USE_BLANKET_WITH_CHIMNEY: And(
        Has(
            DayOfTheTentacleItems.BLANKET.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.PAST_MAIN_HALL_GIVE_CHATTERING_TEETH_TO_GEORGE_WASHINGTON.value,
            parent_region_name=DayOfTheTentacleRegions.PAST_MAIN_HALL.value,
        ),
    ),
    DayOfTheTentacleLocations.PAST_MAIN_HALL_PICK_UP_GOLD_PLATED_QUILL_PEN: CanReachLocation(
        DayOfTheTentacleLocations.PAST_ROOF_USE_BLANKET_WITH_CHIMNEY.value,
        parent_region_name=DayOfTheTentacleRegions.PAST_ROOF.value,
    ),
    DayOfTheTentacleLocations.PAST_BETSY_ROSSS_ROOM_TALK_TO_BETSY_ROSS: None,
    DayOfTheTentacleLocations.FUTURE_ROOF_USE_CRANK_WITH_CRANK_BOX: Has(
        DayOfTheTentacleItems.CRANK.value,
    ),
    DayOfTheTentacleLocations.FUTURE_ROOF_USE_ATTACHED_CRANK: CanReachLocation(
        DayOfTheTentacleLocations.FUTURE_ROOF_USE_CRANK_WITH_CRANK_BOX.value,
        parent_region_name=DayOfTheTentacleRegions.FUTURE_ROOF.value,
    ),
    DayOfTheTentacleLocations.FUTURE_ROOF_PICK_UP_FLAG: CanReachLocation(
        DayOfTheTentacleLocations.FUTURE_ROOF_USE_ATTACHED_CRANK.value,
        parent_region_name=DayOfTheTentacleRegions.FUTURE_ROOF.value,
    ),
    DayOfTheTentacleLocations.FUTURE_USE_FLAG: And(
        Has(
            DayOfTheTentacleItems.FLAG.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.PAST_BETSY_ROSSS_ROOM_USE_TENTACLE_CHART_WITH_PATTERNS.value,
            parent_region_name=DayOfTheTentacleRegions.PAST_BETSY_ROSSS_ROOM.value,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_SECOND_FLOOR_HALLWAY_PICK_UP_FROZEN_HAMSTER: CanReachLocation(
        DayOfTheTentacleLocations.PRESENT_SECOND_FLOOR_HALLWAY_USE_HAMSTER_WITH_ICE_MACHINE.value,
        parent_region_name=DayOfTheTentacleRegions.PRESENT_SECOND_FLOOR_HALLWAY.value,
    ),
    DayOfTheTentacleLocations.FUTURE_TIME_CAPSULE_ROOM_USE_CAN_OPENER_WITH_TIME_CAPSULE: Has(
        DayOfTheTentacleItems.CAN_OPENER.value,
    ),
    DayOfTheTentacleLocations.FUTURE_TIME_CAPSULE_ROOM_PICK_UP_VINEGAR: And(
        CanReachLocation(
            DayOfTheTentacleLocations.FUTURE_TIME_CAPSULE_ROOM_USE_CAN_OPENER_WITH_TIME_CAPSULE.value,
            parent_region_name=DayOfTheTentacleRegions.FUTURE_TIME_CAPSULE_ROOM.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.PAST_MAIN_HALL_USE_WINE_BOTTLE_WITH_TIME_CAPSULE.value,
            parent_region_name=DayOfTheTentacleRegions.PAST_MAIN_HALL.value,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_DEAD_COUSIN_TEDS_ROOM_PICK_UP_EXTENSION_CORD: None,
    DayOfTheTentacleLocations.FUTURE_DEAD_COUSIN_TEDS_ROOM_PICK_UP_ROLLER_SKATES: None,
    DayOfTheTentacleLocations.FUTURE_DEAD_COUSIN_TEDS_ROOM_USE_ROLLER_SKATES_WITH_MUMMY: Has(
        DayOfTheTentacleItems.ROLLER_SKATES.value,
    ),
    DayOfTheTentacleLocations.FUTURE_DEAD_COUSIN_TEDS_ROOM_PUSH_MUMMY: CanReachLocation(
        DayOfTheTentacleLocations.FUTURE_DEAD_COUSIN_TEDS_ROOM_USE_ROLLER_SKATES_WITH_MUMMY.value,
        parent_region_name=DayOfTheTentacleRegions.FUTURE_DEAD_COUSIN_TEDS_ROOM.value,
    ),
    DayOfTheTentacleLocations.FUTURE_MAIN_HALL_TALK_TO_TENTACLE: CanReachLocation(
        DayOfTheTentacleLocations.FUTURE_USE_FLAG.value,
        parent_region_name=DayOfTheTentacleRegions.FUTURE_DOCTORS_OFFICE.value,
    ),
    DayOfTheTentacleLocations.PRESENT_MAIN_HALL_USE_SCALPEL_WITH_OOZO_THE_CLOWN: Has(
        DayOfTheTentacleItems.SCALPEL.value,
    ),
    DayOfTheTentacleLocations.PRESENT_MAIN_HALL_PICK_UP_BOX_O_LAUGHS: CanReachLocation(
        DayOfTheTentacleLocations.PRESENT_MAIN_HALL_USE_SCALPEL_WITH_OOZO_THE_CLOWN.value,
        parent_region_name=DayOfTheTentacleRegions.PRESENT_MAIN_HALL.value,
    ),
    DayOfTheTentacleLocations.PRESENT_BASEMENT_LAB_USE_DECAF_COFFEE_WITH_MUG: Has(
        DayOfTheTentacleItems.DECAF_COFFEE.value,
    ),
    DayOfTheTentacleLocations.PRESENT_NURSE_EDNAS_ROOM_PUSH_NURSE_EDNA: CanReachLocation(
        DayOfTheTentacleLocations.PAST_NED_AND_JEDS_ROOM_USE_LEFT_HANDED_HAMMER_WITH_BARREL.value,
        parent_region_name=DayOfTheTentacleRegions.PAST_NED_AND_JEDS_ROOM.value,
    ),
    DayOfTheTentacleLocations.PRESENT_NURSE_EDNAS_ROOM_USE_VIDEOTAPE_WITH_VCR: And(
        Has(
            DayOfTheTentacleItems.VIDEOTAPE.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.PRESENT_NURSE_EDNAS_ROOM_PUSH_NURSE_EDNA.value,
            parent_region_name=DayOfTheTentacleRegions.PRESENT_NURSE_EDNAS_ROOM.value,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_OFFICE_OPEN_SAFE: CanReachLocation(
        DayOfTheTentacleLocations.PRESENT_VCR_CONTROLS_USE_PLAY_BUTTON_AT_SLOW_SPEED.value,
        parent_region_name=DayOfTheTentacleRegions.PRESENT_VCR_CONTROLS.value,
    ),
    DayOfTheTentacleLocations.PRESENT_OFFICE_PICK_UP_CONTRACT: CanReachLocation(
        DayOfTheTentacleLocations.PRESENT_OFFICE_OPEN_SAFE.value,
        parent_region_name=DayOfTheTentacleRegions.PRESENT_OFFICE.value,
    ),
    DayOfTheTentacleLocations.PRESENT_ATTIC_PICK_UP_ROPE: CanReachLocation(
        DayOfTheTentacleLocations.PRESENT_VCR_CONTROLS_USE_RECORD_BUTTON.value,
        parent_region_name=DayOfTheTentacleRegions.PRESENT_VCR_CONTROLS.value,
    ),
    DayOfTheTentacleLocations.PRESENT_ROOF_USE_ROPE_WITH_PULLEY: Has(
        DayOfTheTentacleItems.ROPE.value,
    ),
    DayOfTheTentacleLocations.PRESENT_FRONT_YARD_USE_DANGLING_ROPE_WITH_DEAD_COUSIN_TED: CanReachLocation(
        DayOfTheTentacleLocations.PRESENT_ROOF_USE_ROPE_WITH_PULLEY.value,
        parent_region_name=DayOfTheTentacleRegions.PRESENT_ROOF.value,
    ),
    DayOfTheTentacleLocations.PRESENT_USE_RED_PAINT_WITH_DEAD_COUSIN_TED: Has(
        DayOfTheTentacleItems.RED_PAINT.value,
    ),
    DayOfTheTentacleLocations.PRESENT_ROOF_PULL_ROPE_TO_RAISE_TED: CanReachLocation(
        DayOfTheTentacleLocations.PRESENT_FRONT_YARD_USE_DANGLING_ROPE_WITH_DEAD_COUSIN_TED.value,
        parent_region_name=DayOfTheTentacleRegions.PRESENT_FRONT_YARD.value,
    ),
    DayOfTheTentacleLocations.PRESENT_ROOF_PULL_ROPE_TO_LOWER_DR_FRED: CanReachLocation(
        DayOfTheTentacleLocations.PRESENT_ATTIC_USE_ROPE_WITH_DR_FRED.value,
        parent_region_name=DayOfTheTentacleRegions.PRESENT_ATTIC.value,
    ),
    DayOfTheTentacleLocations.PRESENT_BASEMENT_LAB_USE_FUNNEL_WITH_DR_FRED: And(
        Has(
            DayOfTheTentacleItems.FUNNEL.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.PRESENT_ROOF_PULL_ROPE_TO_LOWER_DR_FRED.value,
            parent_region_name=DayOfTheTentacleRegions.PRESENT_ROOF.value,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_BASEMENT_LAB_USE_COFFEE_WITH_FUNNEL: And(
        Has(
            DayOfTheTentacleItems.COFFEE.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.PRESENT_BASEMENT_LAB_USE_FUNNEL_WITH_DR_FRED.value,
            parent_region_name=DayOfTheTentacleRegions.PRESENT_BASEMENT_LAB.value,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_BASEMENT_LAB_USE_CONTRACT_WITH_DR_FRED: And(
        Has(
            DayOfTheTentacleItems.CONTRACT.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.PRESENT_BASEMENT_LAB_USE_COFFEE_WITH_FUNNEL.value,
            parent_region_name=DayOfTheTentacleRegions.PRESENT_BASEMENT_LAB.value,
        ),
    ),
    DayOfTheTentacleLocations.PAST_BASEMENT_LAB_GIVE_HELP_WANTED_SIGN_TO_RED_EDISON: Has(
        DayOfTheTentacleItems.HELP_WANTED_SIGN.value,
    ),
    DayOfTheTentacleLocations.PAST_BASEMENT_LAB_PICK_UP_LAB_COAT: CanReachLocation(
        DayOfTheTentacleLocations.PAST_BASEMENT_LAB_GIVE_HELP_WANTED_SIGN_TO_RED_EDISON.value,
        parent_region_name=DayOfTheTentacleRegions.PAST_BASEMENT_LAB.value,
    ),
    DayOfTheTentacleLocations.PAST_BASEMENT_LAB_GIVE_OIL_TO_RED_EDISON: And(
        Has(
            DayOfTheTentacleItems.OIL.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.PAST_BASEMENT_LAB_GIVE_PATENT_APPLICATION_TO_RED_EDISON.value,
            parent_region_name=DayOfTheTentacleRegions.PAST_BASEMENT_LAB.value,
        ),
    ),
    DayOfTheTentacleLocations.PAST_BASEMENT_LAB_GIVE_VINEGAR_TO_RED_EDISON: And(
        Has(
            DayOfTheTentacleItems.VINEGAR.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.PAST_BASEMENT_LAB_GIVE_PATENT_APPLICATION_TO_RED_EDISON.value,
            parent_region_name=DayOfTheTentacleRegions.PAST_BASEMENT_LAB.value,
        ),
    ),
    DayOfTheTentacleLocations.PAST_BASEMENT_LAB_GIVE_GOLD_PLATED_QUILL_PEN_TO_RED_EDISON: And(
        Has(
            DayOfTheTentacleItems.GOLD_PLATED_QUILL_PEN.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.PAST_BASEMENT_LAB_GIVE_PATENT_APPLICATION_TO_RED_EDISON.value,
            parent_region_name=DayOfTheTentacleRegions.PAST_BASEMENT_LAB.value,
        ),
    ),
    DayOfTheTentacleLocations.PAST_BASEMENT_LAB_PICK_UP_BATTERY: And(
        CanReachLocation(
            DayOfTheTentacleLocations.PAST_BASEMENT_LAB_GIVE_OIL_TO_RED_EDISON.value,
            parent_region_name=DayOfTheTentacleRegions.PAST_BASEMENT_LAB.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.PAST_BASEMENT_LAB_GIVE_VINEGAR_TO_RED_EDISON.value,
            parent_region_name=DayOfTheTentacleRegions.PAST_BASEMENT_LAB.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.PAST_BASEMENT_LAB_GIVE_GOLD_PLATED_QUILL_PEN_TO_RED_EDISON.value,
            parent_region_name=DayOfTheTentacleRegions.PAST_BASEMENT_LAB.value,
        ),
    ),
    DayOfTheTentacleLocations.PAST_BEN_FRANKLINS_ROOM_GIVE_LAB_COAT_TO_BEN_FRANKLIN: And(
        Has(
            DayOfTheTentacleItems.LAB_COAT.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.PAST_FRONT_YARD_USE_BUCKET_WITH_CARRIAGE.value,
            parent_region_name=DayOfTheTentacleRegions.PAST_FRONT_YARD.value,
        ),
    ),
    DayOfTheTentacleLocations.PAST_FIELD_PICK_UP_FULLY_CHARGED_BATTERY: Has(
        DayOfTheTentacleItems.BATTERY.value,
    ),
    DayOfTheTentacleLocations.PRESENT_USE_STAMP_WITH_CONTRACT: HasAll(
        DayOfTheTentacleItems.CONTRACT.value,
        DayOfTheTentacleItems.STAMP.value,
    ),
    DayOfTheTentacleLocations.PAST_FRONT_YARD_USE_CONTRACT_WITH_MAILBOX: And(
        Has(
            DayOfTheTentacleItems.CONTRACT.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.PRESENT_BASEMENT_LAB_USE_CONTRACT_WITH_DR_FRED.value,
            parent_region_name=DayOfTheTentacleRegions.PRESENT_BASEMENT_LAB.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.PRESENT_USE_STAMP_WITH_CONTRACT.value,
            parent_region_name=DayOfTheTentacleRegions.PRESENT_OFFICE.value,
        ),
    ),
    DayOfTheTentacleLocations.PAST_OUTHOUSES_USE_BATTERY_WITH_PLUG: And(
        Has(
            DayOfTheTentacleItems.BATTERY.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.PAST_FIELD_PICK_UP_FULLY_CHARGED_BATTERY.value,
            parent_region_name=DayOfTheTentacleRegions.PAST_FIELD_KITE_SCENE.value,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_LOBBY_USE_NAME_TAG_WITH_MUMMY: And(
        Has(
            DayOfTheTentacleItems.NAME_TAG.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.FUTURE_DEAD_COUSIN_TEDS_ROOM_PUSH_MUMMY.value,
            parent_region_name=DayOfTheTentacleRegions.FUTURE_DEAD_COUSIN_TEDS_ROOM.value,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_HUMAN_SHOW_USE_BOX_O_LAUGHS_WITH_MUMMY: And(
        Has(
            DayOfTheTentacleItems.BOX_O_LAUGHS.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.FUTURE_LOBBY_USE_NAME_TAG_WITH_MUMMY.value,
            parent_region_name=DayOfTheTentacleRegions.FUTURE_LOBBY.value,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_HUMAN_SHOW_USE_DENTURES_WITH_MUMMY: And(
        Has(
            DayOfTheTentacleItems.DENTURES.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.FUTURE_LOBBY_USE_NAME_TAG_WITH_MUMMY.value,
            parent_region_name=DayOfTheTentacleRegions.FUTURE_LOBBY.value,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_HUMAN_SHOW_USE_SPAGHETTI_WITH_MUMMY: And(
        Has(
            DayOfTheTentacleItems.SPAGHETTI.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.FUTURE_LOBBY_USE_NAME_TAG_WITH_MUMMY.value,
            parent_region_name=DayOfTheTentacleRegions.FUTURE_LOBBY.value,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_HUMAN_SHOW_USE_FORK_WITH_MUMMYS_HEAD: And(
        Has(
            DayOfTheTentacleItems.FORK.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.FUTURE_HUMAN_SHOW_USE_SPAGHETTI_WITH_MUMMY.value,
            parent_region_name=DayOfTheTentacleRegions.FUTURE_HUMAN_SHOW.value,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_HUMAN_SHOW_USE_FAKE_BARF_WITH_HAROLD: And(
        Has(
            DayOfTheTentacleItems.FAKE_BARF.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.FUTURE_LOBBY_USE_NAME_TAG_WITH_MUMMY.value,
            parent_region_name=DayOfTheTentacleRegions.FUTURE_LOBBY.value,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_FRONT_YARD_USE_BOOBOO_B_GONE_WITH_FENCE: And(
        Has(
            DayOfTheTentacleItems.BOOBOO_B_GONE.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.FUTURE_USE_FLAG.value,
            parent_region_name=DayOfTheTentacleRegions.FUTURE_DOCTORS_OFFICE.value,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_FRONT_YARD_USE_SQUEAKY_MOUSE_TOY_WITH_CAT: And(
        Has(
            DayOfTheTentacleItems.SQUEAKY_MOUSE_TOY.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.FUTURE_FRONT_YARD_USE_BOOBOO_B_GONE_WITH_FENCE.value,
            parent_region_name=DayOfTheTentacleRegions.FUTURE_FRONT_YARD.value,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_KENNEL_GIVE_DINNER_CERTIFICATE_TO_TENTACLE_GUARD: And(
        Has(
            DayOfTheTentacleItems.DINNER_CERTIFICATE.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.FUTURE_USE_FLAG.value,
            parent_region_name=DayOfTheTentacleRegions.FUTURE_DOCTORS_OFFICE.value,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_KENNEL_USE_CAT_IN_KENNEL: And(
        Has(
            DayOfTheTentacleItems.CAT.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.FUTURE_KENNEL_GIVE_DINNER_CERTIFICATE_TO_TENTACLE_GUARD.value,
            parent_region_name=DayOfTheTentacleRegions.FUTURE_KENNEL.value,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_KITCHEN_USE_FROZEN_HAMSTER_WITH_MICROWAVE: CanReachLocation(
        DayOfTheTentacleLocations.FUTURE_SECOND_FLOOR_HALLWAY_PICK_UP_FROZEN_HAMSTER.value,
        parent_region_name=DayOfTheTentacleRegions.FUTURE_SECOND_FLOOR_HALLWAY.value,
    ),
    DayOfTheTentacleLocations.FUTURE_USE_SWEATER_WITH_HAMSTER: And(
        CanReachLocation(
            DayOfTheTentacleLocations.FUTURE_KITCHEN_USE_FROZEN_HAMSTER_WITH_MICROWAVE.value,
            parent_region_name=DayOfTheTentacleRegions.FUTURE_KITCHEN.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.PRESENT_LAUNDRY_ROOM_USE_QUARTERS_WITH_DRYER_COIN_SLOT.value,
            parent_region_name=DayOfTheTentacleRegions.PRESENT_LAUNDRY_ROOM.value,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_BASEMENT_LAB_USE_HAMSTER_WITH_GENERATOR: CanReachLocation(
        DayOfTheTentacleLocations.FUTURE_BASEMENT_LAB_PICK_UP_DUST_BALL.value,
        parent_region_name=DayOfTheTentacleRegions.FUTURE_BASEMENT_LAB.value,
    ),
    DayOfTheTentacleLocations.FUTURE_BASEMENT_LAB_USE_BUILT_IN_SHOP_VAC_WITH_MOUSE_HOLE: And(
        CanReachLocation(
            DayOfTheTentacleLocations.FUTURE_USE_SWEATER_WITH_HAMSTER.value,
            parent_region_name=DayOfTheTentacleRegions.FUTURE_LAUNDRY_ROOM.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.PAST_MAIN_HALL_USE_FLIER_WITH_SUGGESTION_BOX.value,
            parent_region_name=DayOfTheTentacleRegions.PAST_MAIN_HALL.value,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_BASEMENT_LAB_PICK_UP_DUST_BALL: CanReachLocation(
        DayOfTheTentacleLocations.FUTURE_BASEMENT_LAB_USE_BUILT_IN_SHOP_VAC_WITH_MOUSE_HOLE.value,
        parent_region_name=DayOfTheTentacleRegions.FUTURE_BASEMENT_LAB.value,
    ),
    DayOfTheTentacleLocations.FUTURE_BASEMENT_LAB_PICK_UP_HUBCAP: CanReachLocation(
        DayOfTheTentacleLocations.FUTURE_USE_SWEATER_WITH_HAMSTER.value,
        parent_region_name=DayOfTheTentacleRegions.FUTURE_LAUNDRY_ROOM.value,
    ),
    DayOfTheTentacleLocations.FUTURE_BASEMENT_LAB_USE_EXTENSION_CORD_WITH_OUTLET: Has(
        DayOfTheTentacleItems.EXTENSION_CORD.value,
    ),
    DayOfTheTentacleLocations.FUTURE_KUMQUAT_TREE_USE_EXTENSION_CORD_WITH_WINDOW: Has(
        DayOfTheTentacleItems.EXTENSION_CORD.value,
    ),
    DayOfTheTentacleLocations.FUTURE_KUMQUAT_TREE_USE_EXTENSION_CORD_WITH_CHRON_O_JOHN: CanReachLocation(
        DayOfTheTentacleLocations.FUTURE_KUMQUAT_TREE_USE_EXTENSION_CORD_WITH_WINDOW.value,
        parent_region_name=DayOfTheTentacleRegions.FUTURE_KUMQUAT_TREE.value,
    ),
    DayOfTheTentacleLocations.FUTURE_HUMAN_SHOW_JUDGING_TALK_TO_JUDGES_FOR_TROPHY: And(
        CanReachLocation(
            DayOfTheTentacleLocations.FUTURE_HUMAN_SHOW_JUDGING_TALK_TO_JUDGES_ABOUT_BEST_HAIR.value,
            parent_region_name=DayOfTheTentacleRegions.FUTURE_HUMAN_SHOW_JUDGING.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.FUTURE_HUMAN_SHOW_JUDGING_TALK_TO_JUDGES_ABOUT_BEST_SMILE.value,
            parent_region_name=DayOfTheTentacleRegions.FUTURE_HUMAN_SHOW_JUDGING.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.FUTURE_HUMAN_SHOW_JUDGING_TALK_TO_JUDGES_ABOUT_BEST_LAUGH.value,
            parent_region_name=DayOfTheTentacleRegions.FUTURE_HUMAN_SHOW_JUDGING.value,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_HUMAN_SHOW_JUDGING_TALK_TO_JUDGES_FOR_DINNER_CERTIFICATE: And(
        CanReachLocation(
            DayOfTheTentacleLocations.FUTURE_HUMAN_SHOW_JUDGING_TALK_TO_JUDGES_ABOUT_BEST_HAIR.value,
            parent_region_name=DayOfTheTentacleRegions.FUTURE_HUMAN_SHOW_JUDGING.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.FUTURE_HUMAN_SHOW_JUDGING_TALK_TO_JUDGES_ABOUT_BEST_SMILE.value,
            parent_region_name=DayOfTheTentacleRegions.FUTURE_HUMAN_SHOW_JUDGING.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.FUTURE_HUMAN_SHOW_JUDGING_TALK_TO_JUDGES_ABOUT_BEST_LAUGH.value,
            parent_region_name=DayOfTheTentacleRegions.FUTURE_HUMAN_SHOW_JUDGING.value,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_DWAYNES_ROOM_LOOK_AT_TV_SET: CanReachLocation(
        DayOfTheTentacleLocations.PRESENT_DWAYNES_ROOM_GIVE_LETTER_TO_DWAYNE.value,
        parent_region_name=DayOfTheTentacleRegions.PRESENT_DWAYNES_ROOM.value,
    ),
    DayOfTheTentacleLocations.PRESENT_DWAYNES_ROOM_USE_PHONE: And(
        Has(
            DayOfTheTentacleItems.SWISS_BANKBOOK.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.PRESENT_DWAYNES_ROOM_LOOK_AT_TV_SET.value,
            parent_region_name=DayOfTheTentacleRegions.PRESENT_DWAYNES_ROOM.value,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_KENNEL_TALK_TO_TENTACLE_GUARD_ABOUT_FEELING_SICK: None,
    DayOfTheTentacleLocations.FUTURE_KENNEL_TALK_TO_TENTACLE_GUARD_ABOUT_THE_BATHROOM: None,
    DayOfTheTentacleLocations.PRESENT_VCR_CONTROLS_USE_RECORD_BUTTON: And(
        CanReachLocation(
            DayOfTheTentacleLocations.PRESENT_NURSE_EDNAS_ROOM_USE_VIDEOTAPE_WITH_VCR.value,
            parent_region_name=DayOfTheTentacleRegions.PRESENT_NURSE_EDNAS_ROOM.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.PRESENT_BASEMENT_LAB_USE_DECAF_COFFEE_WITH_MUG.value,
            parent_region_name=DayOfTheTentacleRegions.PRESENT_BASEMENT_LAB.value,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_VCR_CONTROLS_USE_PLAY_BUTTON_AT_SLOW_SPEED: CanReachLocation(
        DayOfTheTentacleLocations.PRESENT_VCR_CONTROLS_USE_RECORD_BUTTON.value,
        parent_region_name=DayOfTheTentacleRegions.PRESENT_VCR_CONTROLS.value,
    ),
    DayOfTheTentacleLocations.PRESENT_ATTIC_USE_TED_WITH_DR_FRED: And(
        CanReachLocation(
            DayOfTheTentacleLocations.PRESENT_ROOF_PULL_ROPE_TO_RAISE_TED.value,
            parent_region_name=DayOfTheTentacleRegions.PRESENT_ROOF.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.PRESENT_USE_RED_PAINT_WITH_DEAD_COUSIN_TED.value,
            parent_region_name=DayOfTheTentacleRegions.PRESENT_FRONT_YARD.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.PRESENT_VCR_CONTROLS_USE_RECORD_BUTTON.value,
            parent_region_name=DayOfTheTentacleRegions.PRESENT_VCR_CONTROLS.value,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_ATTIC_USE_ROPE_WITH_DR_FRED: CanReachLocation(
        DayOfTheTentacleLocations.PRESENT_ATTIC_USE_TED_WITH_DR_FRED.value,
        parent_region_name=DayOfTheTentacleRegions.PRESENT_ATTIC.value,
    ),
    DayOfTheTentacleLocations.FUTURE_HUMAN_SHOW_JUDGING_TALK_TO_JUDGES_ABOUT_BEST_HAIR: And(
        CanReachLocation(
            DayOfTheTentacleLocations.FUTURE_HUMAN_SHOW_USE_FORK_WITH_MUMMYS_HEAD.value,
            parent_region_name=DayOfTheTentacleRegions.FUTURE_HUMAN_SHOW.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.FUTURE_HUMAN_SHOW_USE_FAKE_BARF_WITH_HAROLD.value,
            parent_region_name=DayOfTheTentacleRegions.FUTURE_HUMAN_SHOW.value,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_HUMAN_SHOW_JUDGING_TALK_TO_JUDGES_ABOUT_BEST_SMILE: And(
        CanReachLocation(
            DayOfTheTentacleLocations.FUTURE_HUMAN_SHOW_USE_DENTURES_WITH_MUMMY.value,
            parent_region_name=DayOfTheTentacleRegions.FUTURE_HUMAN_SHOW.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.FUTURE_HUMAN_SHOW_USE_FAKE_BARF_WITH_HAROLD.value,
            parent_region_name=DayOfTheTentacleRegions.FUTURE_HUMAN_SHOW.value,
        ),
    ),
    DayOfTheTentacleLocations.FUTURE_HUMAN_SHOW_JUDGING_TALK_TO_JUDGES_ABOUT_BEST_LAUGH: And(
        CanReachLocation(
            DayOfTheTentacleLocations.FUTURE_HUMAN_SHOW_USE_BOX_O_LAUGHS_WITH_MUMMY.value,
            parent_region_name=DayOfTheTentacleRegions.FUTURE_HUMAN_SHOW.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.FUTURE_HUMAN_SHOW_USE_FAKE_BARF_WITH_HAROLD.value,
            parent_region_name=DayOfTheTentacleRegions.FUTURE_HUMAN_SHOW.value,
        ),
    ),
    DayOfTheTentacleLocations.PAST_FIELD_VOICE_LINE_IT_LOOKS_PRETTY_MUCH_THE_SAME: None,
    DayOfTheTentacleLocations.PAST_OUTHOUSES_VOICE_LINE_ID_RATHER_USE_A_TREE: None,
    DayOfTheTentacleLocations.PAST_OUTHOUSES_VOICE_LINE_NAH_IT_STINKS: None,
    DayOfTheTentacleLocations.PAST_LOBBY_VOICE_LINE_COOL_THE_ROOM_CLERKS_A_MUMMY: None,
    DayOfTheTentacleLocations.PAST_BASEMENT_LAB_VOICE_LINE_ITS_COVERED_WITH_PLANS_AND_JUNK: None,
    DayOfTheTentacleLocations.PAST_SECOND_FLOOR_HALLWAY_VOICE_LINE_THESED_LOOK_BETTER_ON_VELVET: None,
    DayOfTheTentacleLocations.PAST_GEORGE_WASHINGTONS_ROOM_VOICE_LINE_WHEEE: None,
    DayOfTheTentacleLocations.PAST_BEN_FRANKLINS_ROOM_VOICE_LINE_PROBABLY_THE_UNDERWEAR_DRAWER: None,
    DayOfTheTentacleLocations.PAST_BEN_FRANKLINS_ROOM_VOICE_LINE_I_WOULDNT_KNOW_A_MISTAKE: Has(
        DayOfTheTentacleItems.BOOBOO_B_GONE.value,
    ),
    DayOfTheTentacleLocations.PAST_BETSY_ROSSS_ROOM_VOICE_LINE_THAT_WOULD_MAKE_A_KILLER_T_SHIRT: None,
    DayOfTheTentacleLocations.PAST_THIRD_FLOOR_HALLWAY_VOICE_LINE_A_HORSE_IS_A_HORSE_OF_COURSE: None,
    DayOfTheTentacleLocations.PAST_NED_AND_JEDS_ROOM_VOICE_LINE_THESE_DUDES_MIGHT_GET_MAD: Has(
        DayOfTheTentacleItems.CAN_OPENER.value,
    ),
    DayOfTheTentacleLocations.PAST_ATTIC_VOICE_LINE_VERY_SPARTAN: None,
    DayOfTheTentacleLocations.PAST_ROOF_VOICE_LINE_ITS_TOO_COMPLICATED_FOR_ME: None,
    DayOfTheTentacleLocations.PRESENT_MAIN_HALL_VOICE_LINE_USELESS_JUNK_AND_A_GUN: None,
    DayOfTheTentacleLocations.PRESENT_KITCHEN_VOICE_LINE_MY_WHAT_A_BIG_COFFEE_MAKER: None,
    DayOfTheTentacleLocations.PRESENT_NURSE_EDNAS_ROOM_VOICE_LINE_IT_LOOKS_LIKE_A_PHYSICS_PROFESSOR: None,
    DayOfTheTentacleLocations.PRESENT_BASEMENT_LAB_VOICE_LINE_IM_SURPRISED_I_EVER_GOT_OUT: None,
    DayOfTheTentacleLocations.PRESENT_BASEMENT_LAB_VOICE_LINE_WARNING_DO_NOT_TOUCH: None,
    DayOfTheTentacleLocations.PRESENT_DWAYNES_ROOM_VOICE_LINE_WHAT_DESTROY_ART: And(
        Has(
            DayOfTheTentacleItems.DISAPPEARING_INK.value,
        ),
        CanReachLocation(
            DayOfTheTentacleLocations.PRESENT_DWAYNES_ROOM_GIVE_LETTER_TO_DWAYNE.value,
            parent_region_name=DayOfTheTentacleRegions.PRESENT_DWAYNES_ROOM.value,
        ),
    ),
    DayOfTheTentacleLocations.PRESENT_LAUNDRY_ROOM_VOICE_LINE_THAT_WOULD_MAKE_IT_LOOK_NICER: Has(
        DayOfTheTentacleItems.RED_PAINT.value,
    ),
    DayOfTheTentacleLocations.PRESENT_LOBBY_VOICE_LINE_A_HORTICULTURAL_HORROR: None,
    DayOfTheTentacleLocations.PRESENT_OFFICE_VOICE_LINE_SPECTACULARLY_UGLY_FAMILY: None,
    DayOfTheTentacleLocations.PRESENT_PARKING_LOT_VOICE_LINE_IT_DIDNT_WORK_FOR_THE_OTHER_GUY: Has(
        DayOfTheTentacleItems.CROWBAR.value,
    ),
    DayOfTheTentacleLocations.PRESENT_PARKING_LOT_VOICE_LINE_THEY_FILMED_MOTEL_SLASHER_3_HERE: None,
    DayOfTheTentacleLocations.PRESENT_ROOF_VOICE_LINE_WOW_A_PULLEY: None,
    DayOfTheTentacleLocations.PRESENT_GREEN_TENTACLES_ROOM_VOICE_LINE_THIS_LOOKS_LIKE_IT_MIGHT_WORK: None,
    DayOfTheTentacleLocations.PRESENT_THIRD_FLOOR_HALLWAY_VOICE_LINE_JUST_PLAIN_MEAN: CanReachLocation(
        DayOfTheTentacleLocations.PRESENT_USE_GUM_WITH_A_DIME_STUCK_IN_IT.value,
        parent_region_name=DayOfTheTentacleRegions.PRESENT_LOBBY.value,
    ),
    DayOfTheTentacleLocations.PRESENT_SLUDGE_RIVER_VOICE_LINE_KEEP_OUT_AREA_CONTAMINATED: None,
    DayOfTheTentacleLocations.FUTURE_TIME_CAPSULE_ROOM_VOICE_LINE_IT_LOOKS_LIKE_A_POODLE: None,
    DayOfTheTentacleLocations.FUTURE_DEAD_COUSIN_TEDS_ROOM_VOICE_LINE_IM_NOT_THAT_CRAZY: None,
    DayOfTheTentacleLocations.FUTURE_LOBBY_VOICE_LINE_THIS_FOUR_HUNDRED_YEAR_OLD_CLOCK: None,
    DayOfTheTentacleLocations.FUTURE_KITCHEN_VOICE_LINE_OPPRESSIVE_AND_POWER_MAD: None,
    DayOfTheTentacleLocations.FUTURE_FRONT_YARD_VOICE_LINE_I_LIKE_WHAT_THEYVE_DONE: None,
    DayOfTheTentacleLocations.FUTURE_BASEMENT_LAB_VOICE_LINE_IM_NOT_INTERESTED_IN_TENTACLE_JUNK: None,
    DayOfTheTentacleLocations.FUTURE_BASEMENT_LAB_VOICE_LINE_MORE_THAN_A_FRESH_COAT_OF_PAINT: Has(
        DayOfTheTentacleItems.RED_PAINT.value,
    ),
    DayOfTheTentacleLocations.FUTURE_HUMAN_SHOW_JUDGING_VOICE_LINE_AHHH: None,
    DayOfTheTentacleLocations.FUTURE_PURPLE_TENTACLES_OFFICE_VOICE_LINE_HE_HASNT_CONQUERED_ANTARCTICA_YET: None,
    DayOfTheTentacleLocations.FUTURE_PURPLE_TENTACLES_OFFICE_VOICE_LINE_ID_LIKE_TO_GUM_UP_HIS_PLANS: CanReachLocation(
        DayOfTheTentacleLocations.PRESENT_USE_GUM_WITH_A_DIME_STUCK_IN_IT.value,
        parent_region_name=DayOfTheTentacleRegions.PRESENT_LOBBY.value,
    ),
    DayOfTheTentacleLocations.PAST_VISITED_FRONT_YARD: None,
    DayOfTheTentacleLocations.PAST_VISITED_FIELD: None,
    DayOfTheTentacleLocations.PAST_VISITED_LOBBY: None,
    DayOfTheTentacleLocations.PAST_VISITED_MAIN_HALL: None,
    DayOfTheTentacleLocations.PAST_VISITED_KITCHEN: None,
    DayOfTheTentacleLocations.PAST_VISITED_LAUNDRY_ROOM: None,
    DayOfTheTentacleLocations.PAST_VISITED_BASEMENT_LAB: None,
    DayOfTheTentacleLocations.PAST_VISITED_SECOND_FLOOR_HALLWAY: None,
    DayOfTheTentacleLocations.PAST_VISITED_GEORGE_WASHINGTONS_ROOM: None,
    DayOfTheTentacleLocations.PAST_VISITED_BEN_FRANKLINS_ROOM: None,
    DayOfTheTentacleLocations.PAST_VISITED_BETSY_ROSSS_ROOM: None,
    DayOfTheTentacleLocations.PAST_VISITED_THIRD_FLOOR_HALLWAY: None,
    DayOfTheTentacleLocations.PAST_VISITED_NED_AND_JEDS_ROOM: None,
    DayOfTheTentacleLocations.PAST_VISITED_ATTIC: None,
    DayOfTheTentacleLocations.PAST_VISITED_ROOF: None,
    DayOfTheTentacleLocations.PRESENT_VISITED_MAIN_HALL: None,
    DayOfTheTentacleLocations.PRESENT_VISITED_KITCHEN: None,
    DayOfTheTentacleLocations.PRESENT_VISITED_NURSE_EDNAS_ROOM: None,
    DayOfTheTentacleLocations.PRESENT_VISITED_DWAYNES_ROOM: None,
    DayOfTheTentacleLocations.PRESENT_VISITED_SECOND_FLOOR_HALLWAY: None,
    DayOfTheTentacleLocations.PRESENT_VISITED_SLEEPING_CONVENTIONEERS_ROOM: None,
    DayOfTheTentacleLocations.PRESENT_VISITED_LAUNDRY_ROOM: None,
    DayOfTheTentacleLocations.PRESENT_VISITED_LOBBY: None,
    DayOfTheTentacleLocations.PRESENT_VISITED_VCR_CONTROLS: None,
    DayOfTheTentacleLocations.PRESENT_VISITED_FRONT_YARD: None,
    DayOfTheTentacleLocations.PRESENT_VISITED_OFFICE: None,
    DayOfTheTentacleLocations.PRESENT_VISITED_PARKING_LOT: None,
    DayOfTheTentacleLocations.PRESENT_VISITED_ATTIC: None,
    DayOfTheTentacleLocations.PRESENT_VISITED_ATTIC_LANDING: None,
    DayOfTheTentacleLocations.PRESENT_VISITED_ROOF: None,
    DayOfTheTentacleLocations.PRESENT_VISITED_GREEN_TENTACLES_ROOM: None,
    DayOfTheTentacleLocations.PRESENT_VISITED_WEIRD_EDS_ROOM: None,
    DayOfTheTentacleLocations.PRESENT_VISITED_THIRD_FLOOR_HALLWAY: None,
    DayOfTheTentacleLocations.PRESENT_VISITED_SLUDGE_RIVER: None,
    DayOfTheTentacleLocations.FUTURE_VISITED_TIME_CAPSULE_ROOM: None,
    DayOfTheTentacleLocations.FUTURE_VISITED_DEAD_COUSIN_TEDS_ROOM: None,
    DayOfTheTentacleLocations.FUTURE_VISITED_SECOND_FLOOR_HALLWAY: None,
    DayOfTheTentacleLocations.FUTURE_VISITED_LOBBY: None,
    DayOfTheTentacleLocations.FUTURE_VISITED_KITCHEN: None,
    DayOfTheTentacleLocations.FUTURE_VISITED_FRONT_YARD: None,
    DayOfTheTentacleLocations.FUTURE_VISITED_DOCTORS_OFFICE: None,
    DayOfTheTentacleLocations.FUTURE_VISITED_MAIN_HALL: None,
    DayOfTheTentacleLocations.FUTURE_VISITED_BASEMENT_LAB: None,
    DayOfTheTentacleLocations.FUTURE_VISITED_HUMAN_SHOW: None,
    DayOfTheTentacleLocations.FUTURE_VISITED_HUMAN_SHOW_JUDGING: None,
    DayOfTheTentacleLocations.FUTURE_VISITED_ROOF: None,
    DayOfTheTentacleLocations.FUTURE_VISITED_KUMQUAT_TREE: None,
    DayOfTheTentacleLocations.FUTURE_VISITED_LAUNDRY_ROOM: None,
    DayOfTheTentacleLocations.FUTURE_VISITED_PURPLE_TENTACLES_OFFICE: None,
}

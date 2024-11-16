from typing import Dict, Optional, Tuple

from ..enums import (
    ZorkGrandInquisitorGoals,
    ZorkGrandInquisitorItems,
    ZorkGrandInquisitorRegions,
    ZorkGrandInquisitorStartingLocations,
)

# Avoid spells in early items to prevent clash with craftable spells
early_items_for_starting_location: Dict[
    ZorkGrandInquisitorStartingLocations, Optional[Tuple[Tuple[ZorkGrandInquisitorItems, ...], ...]]
] = {
    ZorkGrandInquisitorStartingLocations.PORT_FOOZLE: (
        (
            ZorkGrandInquisitorItems.WELL_ROPE,
        ),
    ),
    ZorkGrandInquisitorStartingLocations.CROSSROADS: None,
    ZorkGrandInquisitorStartingLocations.DM_LAIR: None,
    ZorkGrandInquisitorStartingLocations.DM_LAIR_INTERIOR: (
        (
            ZorkGrandInquisitorItems.HOTSPOT_DUNGEON_MASTERS_HOUSE_EXIT,
        ),
    ),
    ZorkGrandInquisitorStartingLocations.GUE_TECH: None,
    ZorkGrandInquisitorStartingLocations.SPELL_LAB: None,
    ZorkGrandInquisitorStartingLocations.HADES_SHORE: None,
    ZorkGrandInquisitorStartingLocations.SUBWAY_FLOOD_CONTROL_DAM: None,
    ZorkGrandInquisitorStartingLocations.MONASTERY: None,
    ZorkGrandInquisitorStartingLocations.MONASTERY_EXHIBIT: None,
}

endgame_connecting_regions_for_goal: Dict[
    ZorkGrandInquisitorGoals,
    ZorkGrandInquisitorRegions,
] = {
    ZorkGrandInquisitorGoals.THREE_ARTIFACTS: ZorkGrandInquisitorRegions.MENU,
    ZorkGrandInquisitorGoals.ARTIFACT_OF_MAGIC_HUNT: ZorkGrandInquisitorRegions.WALKING_CASTLE,
    ZorkGrandInquisitorGoals.SPELL_HEIST: ZorkGrandInquisitorRegions.PORT_FOOZLE,
    ZorkGrandInquisitorGoals.ZORK_TOUR: ZorkGrandInquisitorRegions.PORT_FOOZLE,
    ZorkGrandInquisitorGoals.NECROMANCER_OF_THE_GREAT_UNDERGROUND_EMPIRE: (
        ZorkGrandInquisitorRegions.HADES_BEYOND_GATES,
    ),
}

starter_kits_for_starting_location: Dict[
    ZorkGrandInquisitorStartingLocations, Optional[Tuple[Tuple[ZorkGrandInquisitorItems, ...], ...]]
] = {
    ZorkGrandInquisitorStartingLocations.PORT_FOOZLE: (
        (
            ZorkGrandInquisitorItems.HOTSPOT_BUCKET,
        ),
    ),
    ZorkGrandInquisitorStartingLocations.CROSSROADS: (
        (
            ZorkGrandInquisitorItems.WELL_ROPE,
            ZorkGrandInquisitorItems.HOTSPOT_BUCKET,
        ),
        (
            ZorkGrandInquisitorItems.SPELL_BEBURTT,
            ZorkGrandInquisitorItems.SUBWAY_TOKEN,
            ZorkGrandInquisitorItems.HOTSPOT_SUBWAY_TOKEN_SLOT,
            ZorkGrandInquisitorItems.OLD_SCRATCH_CARD,
        ),
        (
            ZorkGrandInquisitorItems.SPELL_REZROV,
            ZorkGrandInquisitorItems.HOTSPOT_IN_MAGIC_WE_TRUST_DOOR,
            ZorkGrandInquisitorItems.HOTSPOT_GUE_TECH_WINDOWS,
        ),
        (
            ZorkGrandInquisitorItems.HAMMER,
            ZorkGrandInquisitorItems.HOTSPOT_GLASS_CASE,
            ZorkGrandInquisitorItems.SWORD,
            ZorkGrandInquisitorItems.HOTSPOT_DUNGEON_MASTERS_LAIR_ENTRANCE,
            ZorkGrandInquisitorItems.HOTSPOT_SPRING_MUSHROOM,
            ZorkGrandInquisitorItems.SPELL_THROCK,
        ),
        (
            ZorkGrandInquisitorItems.MAP,
            ZorkGrandInquisitorItems.TELEPORTER_DESTINATION_HADES,
            ZorkGrandInquisitorItems.HOTSPOT_HADES_PHONE_BUTTONS,
            ZorkGrandInquisitorItems.HOTSPOT_HADES_PHONE_RECEIVER,
            ZorkGrandInquisitorItems.POUCH_OF_ZORKMIDS,
            ZorkGrandInquisitorItems.SUBWAY_DESTINATION_CROSSROADS,
        ),
    ),
    ZorkGrandInquisitorStartingLocations.DM_LAIR: (
        (
            ZorkGrandInquisitorItems.SWORD,
            ZorkGrandInquisitorItems.HOTSPOT_HARRY,
            ZorkGrandInquisitorItems.HUNGUS_LARD,
            ZorkGrandInquisitorItems.HOTSPOT_QUELBEE_HIVE,
            ZorkGrandInquisitorItems.HOTSPOT_DUNGEON_MASTERS_LAIR_ENTRANCE,
        ),
        (
            ZorkGrandInquisitorItems.HAMMER,
            ZorkGrandInquisitorItems.SPELL_THROCK,
            ZorkGrandInquisitorItems.HOTSPOT_SNAPDRAGON,
            ZorkGrandInquisitorItems.SNAPDRAGON,
            ZorkGrandInquisitorItems.HOTSPOT_SPRING_MUSHROOM,
        ),
        (
            ZorkGrandInquisitorItems.SWORD,
            ZorkGrandInquisitorItems.HOTSPOT_HARRY,
            ZorkGrandInquisitorItems.CIGAR,
            ZorkGrandInquisitorItems.HOTSPOT_HARRYS_ASHTRAY,
            ZorkGrandInquisitorItems.OLD_SCRATCH_CARD,
            ZorkGrandInquisitorItems.MAP,
            ZorkGrandInquisitorItems.TELEPORTER_DESTINATION_HADES,
        ),
        (
            ZorkGrandInquisitorItems.SWORD,
            ZorkGrandInquisitorItems.HOTSPOT_HARRY,
            ZorkGrandInquisitorItems.HOTSPOT_DUNGEON_MASTERS_LAIR_ENTRANCE,
            ZorkGrandInquisitorItems.MAP,
            ZorkGrandInquisitorItems.TELEPORTER_DESTINATION_GUE_TECH,
            ZorkGrandInquisitorItems.SHOVEL,
            ZorkGrandInquisitorItems.HOTSPOT_DIRT_MOUND,
        ),
        (
            ZorkGrandInquisitorItems.SWORD,
            ZorkGrandInquisitorItems.HOTSPOT_HARRY,
            ZorkGrandInquisitorItems.CIGAR,
            ZorkGrandInquisitorItems.HOTSPOT_HARRYS_ASHTRAY,
            ZorkGrandInquisitorItems.MEAD_LIGHT,
            ZorkGrandInquisitorItems.ZIMDOR_SCROLL,
            ZorkGrandInquisitorItems.HOTSPOT_HARRYS_BIRD_BATH,
        ),
    ),
    ZorkGrandInquisitorStartingLocations.DM_LAIR_INTERIOR: (
        (
            ZorkGrandInquisitorItems.HOTSPOT_BLINDS,
            ZorkGrandInquisitorItems.SPELL_GOLGATEM,
            ZorkGrandInquisitorItems.SPELL_OBIDIL,
            ZorkGrandInquisitorItems.OLD_SCRATCH_CARD,
        ),
        (
            ZorkGrandInquisitorItems.HOTSPOT_MIRROR,
            ZorkGrandInquisitorItems.SCROLL_FRAGMENT_ANS,
            ZorkGrandInquisitorItems.SCROLL_FRAGMENT_GIV,
            ZorkGrandInquisitorItems.COCOA_INGREDIENTS,
            ZorkGrandInquisitorItems.HUNGUS_LARD,
            ZorkGrandInquisitorItems.HOTSPOT_CLOSET_DOOR,
            ZorkGrandInquisitorItems.SPELL_NARWILE,
        ),
        (
            ZorkGrandInquisitorItems.HOTSPOT_CLOSET_DOOR,
            ZorkGrandInquisitorItems.SPELL_NARWILE,
            ZorkGrandInquisitorItems.SPELL_YASTARD,
            ZorkGrandInquisitorItems.TOTEM_GRIFF,
            ZorkGrandInquisitorItems.HOTSPOT_MAILBOX_FLAG,
            ZorkGrandInquisitorItems.HOTSPOT_MIRROR,
        ),
        (
            ZorkGrandInquisitorItems.HOTSPOT_CLOSET_DOOR,
            ZorkGrandInquisitorItems.SPELL_NARWILE,
            ZorkGrandInquisitorItems.SPELL_YASTARD,
            ZorkGrandInquisitorItems.TOTEM_LUCY,
            ZorkGrandInquisitorItems.HOTSPOT_MAILBOX_FLAG,
            ZorkGrandInquisitorItems.HOTSPOT_MAILBOX_DOOR,
        ),
        (
            ZorkGrandInquisitorItems.HOTSPOT_CLOSET_DOOR,
            ZorkGrandInquisitorItems.SPELL_NARWILE,
            ZorkGrandInquisitorItems.SPELL_YASTARD,
            ZorkGrandInquisitorItems.TOTEM_BROG,
            ZorkGrandInquisitorItems.BROGS_FLICKERING_TORCH,
            ZorkGrandInquisitorItems.BROGS_GRUE_EGG,
            ZorkGrandInquisitorItems.HOTSPOT_COOKING_POT,
        ),
    ),
    ZorkGrandInquisitorStartingLocations.GUE_TECH: (
        (
            ZorkGrandInquisitorItems.HOTSPOT_GUE_TECH_DOOR,
            ZorkGrandInquisitorItems.HOTSPOT_DIRT_MOUND,
            ZorkGrandInquisitorItems.SHOVEL,
            ZorkGrandInquisitorItems.HOTSPOT_GUE_TECH_WINDOWS,
        ),
        (
            ZorkGrandInquisitorItems.OLD_SCRATCH_CARD,
            ZorkGrandInquisitorItems.HOTSPOT_CHANGE_MACHINE_SLOT,
            ZorkGrandInquisitorItems.POUCH_OF_ZORKMIDS,
            ZorkGrandInquisitorItems.HOTSPOT_CANDY_MACHINE_BUTTONS,
            ZorkGrandInquisitorItems.HOTSPOT_CANDY_MACHINE_COIN_SLOT,
            ZorkGrandInquisitorItems.HOTSPOT_FROZEN_TREAT_MACHINE_COIN_SLOT,
            ZorkGrandInquisitorItems.HOTSPOT_FROZEN_TREAT_MACHINE_DOORS,
        ),
        (
            ZorkGrandInquisitorItems.POUCH_OF_ZORKMIDS,
            ZorkGrandInquisitorItems.HOTSPOT_CANDY_MACHINE_BUTTONS,
            ZorkGrandInquisitorItems.HOTSPOT_CANDY_MACHINE_COIN_SLOT,
            ZorkGrandInquisitorItems.HOTSPOT_CANDY_MACHINE_VACUUM_SLOT,
            ZorkGrandInquisitorItems.PERMA_SUCK_MACHINE,
            ZorkGrandInquisitorItems.HOTSPOT_SODA_MACHINE_BUTTONS,
            ZorkGrandInquisitorItems.HOTSPOT_SODA_MACHINE_COIN_SLOT,
            ZorkGrandInquisitorItems.ZORK_ROCKS,
            ZorkGrandInquisitorItems.HOTSPOT_FROZEN_TREAT_MACHINE_COIN_SLOT,
            ZorkGrandInquisitorItems.HOTSPOT_FROZEN_TREAT_MACHINE_DOORS,
        ),
        (
            ZorkGrandInquisitorItems.POUCH_OF_ZORKMIDS,
            ZorkGrandInquisitorItems.HOTSPOT_CANDY_MACHINE_BUTTONS,
            ZorkGrandInquisitorItems.HOTSPOT_CANDY_MACHINE_COIN_SLOT,
            ZorkGrandInquisitorItems.HOTSPOT_PURPLE_WORDS,
            ZorkGrandInquisitorItems.SPELL_IGRAM,
        ),
        (
            ZorkGrandInquisitorItems.POUCH_OF_ZORKMIDS,
            ZorkGrandInquisitorItems.HOTSPOT_SODA_MACHINE_BUTTONS,
            ZorkGrandInquisitorItems.HOTSPOT_SODA_MACHINE_COIN_SLOT,
            ZorkGrandInquisitorItems.ZORK_ROCKS,
            ZorkGrandInquisitorItems.HOTSPOT_PURPLE_WORDS,
            ZorkGrandInquisitorItems.SPELL_IGRAM,
            ZorkGrandInquisitorItems.HOTSPOT_DENTED_LOCKER,
            ZorkGrandInquisitorItems.HOTSPOT_STUDENT_ID_MACHINE,
            ZorkGrandInquisitorItems.STUDENT_ID,
        ),
    ),
    ZorkGrandInquisitorStartingLocations.SPELL_LAB: (
        (
            ZorkGrandInquisitorItems.HOTSPOT_SPELL_CHECKER,
            ZorkGrandInquisitorItems.HOTSPOT_BLANK_SCROLL_BOX,
            ZorkGrandInquisitorItems.SANDWITCH_WRAPPER,
            ZorkGrandInquisitorItems.MAP,
            ZorkGrandInquisitorItems.TELEPORTER_DESTINATION_MONASTERY,
            ZorkGrandInquisitorItems.MONASTERY_ROPE,
            ZorkGrandInquisitorItems.HOTSPOT_TOTEMIZER_SWITCH,
            ZorkGrandInquisitorItems.HOTSPOT_TOTEMIZER_WHEELS,
        ),
        (
            ZorkGrandInquisitorItems.HOTSPOT_SPELL_CHECKER,
            ZorkGrandInquisitorItems.SANDWITCH_WRAPPER,
            ZorkGrandInquisitorItems.MAP,
            ZorkGrandInquisitorItems.TELEPORTER_DESTINATION_HADES,
            ZorkGrandInquisitorItems.POUCH_OF_ZORKMIDS,
            ZorkGrandInquisitorItems.HOTSPOT_HADES_PHONE_RECEIVER,
            ZorkGrandInquisitorItems.HOTSPOT_HADES_PHONE_BUTTONS,
            ZorkGrandInquisitorItems.SWORD,
        ),
        (
            ZorkGrandInquisitorItems.HOTSPOT_SPELL_CHECKER,
            ZorkGrandInquisitorItems.HOTSPOT_BLANK_SCROLL_BOX,
            ZorkGrandInquisitorItems.MAP,
            ZorkGrandInquisitorItems.TELEPORTER_DESTINATION_MONASTERY,
            ZorkGrandInquisitorItems.SUBWAY_DESTINATION_FLOOD_CONTROL_DAM,
            ZorkGrandInquisitorItems.SPELL_GOLGATEM,
            ZorkGrandInquisitorItems.HOTSPOT_SOUVENIR_COIN_SLOT,
            ZorkGrandInquisitorItems.POUCH_OF_ZORKMIDS,
            ZorkGrandInquisitorItems.OLD_SCRATCH_CARD,
        ),
        (
            ZorkGrandInquisitorItems.HOTSPOT_SPELL_CHECKER,
            ZorkGrandInquisitorItems.SANDWITCH_WRAPPER,
            ZorkGrandInquisitorItems.POUCH_OF_ZORKMIDS,
            ZorkGrandInquisitorItems.SPELL_IGRAM,
            ZorkGrandInquisitorItems.SPELL_REZROV,
            ZorkGrandInquisitorItems.HOTSPOT_SPELL_LAB_BRIDGE_EXIT,
        ),
        (
            ZorkGrandInquisitorItems.HOTSPOT_SPELL_LAB_BRIDGE_EXIT,
            ZorkGrandInquisitorItems.HOTSPOT_PURPLE_WORDS,
            ZorkGrandInquisitorItems.SPELL_IGRAM,
        ),
    ),
    ZorkGrandInquisitorStartingLocations.HADES_SHORE: (
        (
            ZorkGrandInquisitorItems.HOTSPOT_HADES_PHONE_RECEIVER,
            ZorkGrandInquisitorItems.HOTSPOT_HADES_PHONE_BUTTONS,
            ZorkGrandInquisitorItems.POUCH_OF_ZORKMIDS,
            ZorkGrandInquisitorItems.SWORD,
            ZorkGrandInquisitorItems.SPELL_SNAVIG,
            ZorkGrandInquisitorItems.TOTEM_BROG,
            ZorkGrandInquisitorItems.SPELL_NARWILE,
            ZorkGrandInquisitorItems.SPELL_YASTARD,
        ),
        (
            ZorkGrandInquisitorItems.HOTSPOT_HADES_PHONE_RECEIVER,
            ZorkGrandInquisitorItems.HOTSPOT_HADES_PHONE_BUTTONS,
            ZorkGrandInquisitorItems.POUCH_OF_ZORKMIDS,
            ZorkGrandInquisitorItems.SWORD,
            ZorkGrandInquisitorItems.SPELL_OBIDIL,
            ZorkGrandInquisitorItems.SUBWAY_DESTINATION_FLOOD_CONTROL_DAM,
            ZorkGrandInquisitorItems.HOTSPOT_SOUVENIR_COIN_SLOT,
            ZorkGrandInquisitorItems.SPELL_GOLGATEM,
        ),
        (
            ZorkGrandInquisitorItems.SUBWAY_DESTINATION_CROSSROADS,
            ZorkGrandInquisitorItems.OLD_SCRATCH_CARD,
            ZorkGrandInquisitorItems.SPELL_KENDALL,
        ),
        (
            ZorkGrandInquisitorItems.HOTSPOT_HADES_PHONE_RECEIVER,
            ZorkGrandInquisitorItems.HOTSPOT_HADES_PHONE_BUTTONS,
            ZorkGrandInquisitorItems.SWORD,
            ZorkGrandInquisitorItems.SUBWAY_DESTINATION_MONASTERY,
            ZorkGrandInquisitorItems.MONASTERY_ROPE,
            ZorkGrandInquisitorItems.HOTSPOT_TOTEMIZER_SWITCH,
            ZorkGrandInquisitorItems.HOTSPOT_TOTEMIZER_WHEELS,
            ZorkGrandInquisitorItems.TOTEMIZER_DESTINATION_STRAIGHT_TO_HELL,
        ),
        (
            ZorkGrandInquisitorItems.MAP,
            ZorkGrandInquisitorItems.TELEPORTER_DESTINATION_DM_LAIR,
            ZorkGrandInquisitorItems.HOTSPOT_GLASS_CASE,
            ZorkGrandInquisitorItems.HOTSPOT_SNAPDRAGON,
            ZorkGrandInquisitorItems.HOTSPOT_SPRING_MUSHROOM,
            ZorkGrandInquisitorItems.HAMMER,
        ),
    ),
    ZorkGrandInquisitorStartingLocations.SUBWAY_FLOOD_CONTROL_DAM: (
        (
            ZorkGrandInquisitorItems.HOTSPOT_FLOOD_CONTROL_DOORS,
            ZorkGrandInquisitorItems.HOTSPOT_FLOOD_CONTROL_BUTTONS,
            ZorkGrandInquisitorItems.SPELL_REZROV,
            ZorkGrandInquisitorItems.SUBWAY_DESTINATION_MONASTERY,
            ZorkGrandInquisitorItems.MAP,
            ZorkGrandInquisitorItems.TELEPORTER_DESTINATION_SPELL_LAB,
        ),
        (
            ZorkGrandInquisitorItems.SPELL_GOLGATEM,
            ZorkGrandInquisitorItems.SUBWAY_DESTINATION_CROSSROADS,
            ZorkGrandInquisitorItems.OLD_SCRATCH_CARD,
        ),
        (
            ZorkGrandInquisitorItems.SPELL_THROCK,
            ZorkGrandInquisitorItems.HOTSPOT_MOSSY_GRATE,
            ZorkGrandInquisitorItems.TELEPORTER_DESTINATION_MONASTERY,
            ZorkGrandInquisitorItems.MAP,
            ZorkGrandInquisitorItems.TELEPORTER_DESTINATION_DM_LAIR,
            ZorkGrandInquisitorItems.HOTSPOT_SNAPDRAGON,
        ),
        (
            ZorkGrandInquisitorItems.POUCH_OF_ZORKMIDS,
            ZorkGrandInquisitorItems.HOTSPOT_SOUVENIR_COIN_SLOT,
            ZorkGrandInquisitorItems.SUBWAY_DESTINATION_MONASTERY,
            ZorkGrandInquisitorItems.MAP,
            ZorkGrandInquisitorItems.TELEPORTER_DESTINATION_GUE_TECH,
            ZorkGrandInquisitorItems.HOTSPOT_GUE_TECH_WINDOWS,
        ),
        (
            ZorkGrandInquisitorItems.POUCH_OF_ZORKMIDS,
            ZorkGrandInquisitorItems.HOTSPOT_SOUVENIR_COIN_SLOT,
            ZorkGrandInquisitorItems.SUBWAY_DESTINATION_HADES,
            ZorkGrandInquisitorItems.HOTSPOT_HADES_PHONE_RECEIVER,
            ZorkGrandInquisitorItems.HOTSPOT_HADES_PHONE_BUTTONS,
            ZorkGrandInquisitorItems.SWORD,
        ),
    ),
    ZorkGrandInquisitorStartingLocations.MONASTERY: (
        (
            ZorkGrandInquisitorItems.HOTSPOT_TOTEMIZER_WHEELS,
            ZorkGrandInquisitorItems.HOTSPOT_TOTEMIZER_SWITCH,
            ZorkGrandInquisitorItems.TOTEMIZER_DESTINATION_HALL_OF_INQUISITION,
            ZorkGrandInquisitorItems.HOTSPOT_CLOSING_THE_TIME_TUNNELS_HAMMER_SLOT,
            ZorkGrandInquisitorItems.HOTSPOT_CLOSING_THE_TIME_TUNNELS_LEVER,
            ZorkGrandInquisitorItems.LARGE_TELEGRAPH_HAMMER,
            ZorkGrandInquisitorItems.SPELL_NARWILE,
        ),
        (
            ZorkGrandInquisitorItems.HOTSPOT_TOTEMIZER_WHEELS,
            ZorkGrandInquisitorItems.HOTSPOT_TOTEMIZER_SWITCH,
            ZorkGrandInquisitorItems.TOTEMIZER_DESTINATION_STRAIGHT_TO_HELL,
            ZorkGrandInquisitorItems.OLD_SCRATCH_CARD,
        ),
        (
            ZorkGrandInquisitorItems.HOTSPOT_TOTEMIZER_WHEELS,
            ZorkGrandInquisitorItems.HOTSPOT_TOTEMIZER_SWITCH,
            ZorkGrandInquisitorItems.SUBWAY_DESTINATION_CROSSROADS,
            ZorkGrandInquisitorItems.SUBWAY_TOKEN,
            ZorkGrandInquisitorItems.HOTSPOT_SUBWAY_TOKEN_SLOT,
        ),
        (
            ZorkGrandInquisitorItems.MAP,
            ZorkGrandInquisitorItems.TELEPORTER_DESTINATION_SPELL_LAB,
            ZorkGrandInquisitorItems.SPELL_REZROV,
        ),
        (
            ZorkGrandInquisitorItems.MAP,
            ZorkGrandInquisitorItems.TELEPORTER_DESTINATION_DM_LAIR,
            ZorkGrandInquisitorItems.HOTSPOT_HARRY,
            ZorkGrandInquisitorItems.HOTSPOT_DUNGEON_MASTERS_LAIR_ENTRANCE,
            ZorkGrandInquisitorItems.SWORD,
        ),
    ),
    ZorkGrandInquisitorStartingLocations.MONASTERY_EXHIBIT: (
        (
            ZorkGrandInquisitorItems.HOTSPOT_CLOSING_THE_TIME_TUNNELS_HAMMER_SLOT,
            ZorkGrandInquisitorItems.HOTSPOT_CLOSING_THE_TIME_TUNNELS_LEVER,
            ZorkGrandInquisitorItems.LARGE_TELEGRAPH_HAMMER,
            ZorkGrandInquisitorItems.SPELL_NARWILE,
            ZorkGrandInquisitorItems.SPELL_YASTARD,
            ZorkGrandInquisitorItems.TOTEM_GRIFF,
            ZorkGrandInquisitorItems.HOTSPOT_PORT_FOOZLE_PAST_TAVERN_DOOR,
        ),
        (
            ZorkGrandInquisitorItems.SUBWAY_DESTINATION_HADES,
        ),
        (
            ZorkGrandInquisitorItems.SUBWAY_DESTINATION_FLOOD_CONTROL_DAM,
        ),
        (
            ZorkGrandInquisitorItems.MAP,
            ZorkGrandInquisitorItems.TELEPORTER_DESTINATION_CROSSROADS,
        ),
        (
            ZorkGrandInquisitorItems.HOTSPOT_TOTEMIZER_WHEELS,
            ZorkGrandInquisitorItems.HOTSPOT_TOTEMIZER_SWITCH,
        ),
    ),
}

starting_location_to_region: Dict[
    ZorkGrandInquisitorStartingLocations, ZorkGrandInquisitorRegions
] = {
    ZorkGrandInquisitorStartingLocations.PORT_FOOZLE: ZorkGrandInquisitorRegions.PORT_FOOZLE,
    ZorkGrandInquisitorStartingLocations.CROSSROADS: ZorkGrandInquisitorRegions.CROSSROADS,
    ZorkGrandInquisitorStartingLocations.DM_LAIR: ZorkGrandInquisitorRegions.DM_LAIR,
    ZorkGrandInquisitorStartingLocations.DM_LAIR_INTERIOR: ZorkGrandInquisitorRegions.DM_LAIR_INTERIOR,
    ZorkGrandInquisitorStartingLocations.GUE_TECH: ZorkGrandInquisitorRegions.GUE_TECH,
    ZorkGrandInquisitorStartingLocations.SPELL_LAB: ZorkGrandInquisitorRegions.SPELL_LAB,
    ZorkGrandInquisitorStartingLocations.HADES_SHORE: ZorkGrandInquisitorRegions.HADES_SHORE,
    ZorkGrandInquisitorStartingLocations.SUBWAY_FLOOD_CONTROL_DAM: ZorkGrandInquisitorRegions.SUBWAY_FLOOD_CONTROL_DAM,
    ZorkGrandInquisitorStartingLocations.MONASTERY: ZorkGrandInquisitorRegions.MONASTERY,
    ZorkGrandInquisitorStartingLocations.MONASTERY_EXHIBIT: ZorkGrandInquisitorRegions.MONASTERY_EXHIBIT,
}
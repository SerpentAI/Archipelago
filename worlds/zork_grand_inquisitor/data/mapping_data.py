from typing import Dict, Optional, Tuple, Union

from ..enums import (
    ZorkGrandInquisitorClientSeedInformation,
    ZorkGrandInquisitorCraftableSpellBehaviors,
    ZorkGrandInquisitorDeathsanity,
    ZorkGrandInquisitorGoals,
    ZorkGrandInquisitorHotspots,
    ZorkGrandInquisitorItems,
    ZorkGrandInquisitorLandmarksanity,
    ZorkGrandInquisitorRegions,
    ZorkGrandInquisitorStartingLocations,
)


death_cause_labels: Dict[int, str] = {
    1: "PLAYER got their noggin smitten in twain",
    3: "PLAYER decided to jump into a bottomless pit",
    4: "PLAYER decided to step into the infinite",
    5: "PLAYER became an evil spawn's plaything",
    6: "PLAYER started a career as a talking manhole cover",
    7: "PLAYER got sucked into a starship's tractor beam",
    8: "PLAYER became a paperweight",
    9: "PLAYER rolled into the airless expanse of the cosmos",
    10: "PLAYER got their head bitten off",
    11: "PLAYER was swallowed whole by a dragon",
    13: "PLAYER decided to spend an eternity staring at scenic vistas",
    18: "PLAYER was eaten by a grue",
    19: "PLAYER was vaporized by Zork Rocks",
    20: "PLAYER got stung by a thousand quelbees",
    21: "PLAYER broke curfew",
    22: "PLAYER lost their soul to a scratch-and-win card",
    29: "PLAYER was outsmarted by bees",
    30: "PLAYER got pureed by a six-armed invisible guard",
    32: "PLAYER's head exploded",
    33: "PLAYER died of arteriosclerosis",
    34: "PLAYER decided to ignore the sign and THROCK the grass",
    37: "PLAYER lost a game of strip grue, fire, water",
}

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
    ZorkGrandInquisitorStartingLocations.DM_LAIR_INTERIOR: None,
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
    ZorkGrandInquisitorGoals.GRIM_JOURNEY: (
        ZorkGrandInquisitorRegions.HADES_BEYOND_GATES
    ),
}

hotspot_to_regional_hotspot: Dict[ZorkGrandInquisitorItems, ZorkGrandInquisitorItems] = {
    ZorkGrandInquisitorItems.HOTSPOT_666_MAILBOX: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_HADES
    ),
    ZorkGrandInquisitorItems.HOTSPOT_ALPINES_QUANDRY_CARD_SLOTS: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_PORT_FOOZLE_PAST
    ),
    ZorkGrandInquisitorItems.HOTSPOT_BLANK_SCROLL_BOX: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_SPELL_LAB
    ),
    ZorkGrandInquisitorItems.HOTSPOT_BLINDS: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_DM_LAIR
    ),
    ZorkGrandInquisitorItems.HOTSPOT_BUCKET: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_CROSSROADS
    ),
    ZorkGrandInquisitorItems.HOTSPOT_CANDY_MACHINE_BUTTONS: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_GUE_TECH
    ),
    ZorkGrandInquisitorItems.HOTSPOT_CANDY_MACHINE_COIN_SLOT: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_GUE_TECH
    ),
    ZorkGrandInquisitorItems.HOTSPOT_CANDY_MACHINE_VACUUM_SLOT: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_GUE_TECH
    ),
    ZorkGrandInquisitorItems.HOTSPOT_CHANGE_MACHINE_SLOT: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_GUE_TECH
    ),
    ZorkGrandInquisitorItems.HOTSPOT_CLOSET_DOOR: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_DM_LAIR
    ),
    ZorkGrandInquisitorItems.HOTSPOT_CLOSING_THE_TIME_TUNNELS_HAMMER_SLOT: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_MONASTERY
    ),
    ZorkGrandInquisitorItems.HOTSPOT_CLOSING_THE_TIME_TUNNELS_LEVER: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_MONASTERY
    ),
    ZorkGrandInquisitorItems.HOTSPOT_COOKING_POT: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_WHITE_HOUSE
    ),
    ZorkGrandInquisitorItems.HOTSPOT_DENTED_LOCKER: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_GUE_TECH
    ),
    ZorkGrandInquisitorItems.HOTSPOT_DIRT_MOUND: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_GUE_TECH
    ),
    ZorkGrandInquisitorItems.HOTSPOT_DOCK_WINCH: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_PORT_FOOZLE
    ),
    ZorkGrandInquisitorItems.HOTSPOT_DRAGON_CLAW: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_DRAGON_ARCHIPELAGO
    ),
    ZorkGrandInquisitorItems.HOTSPOT_DRAGON_NOSTRILS: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_DRAGON_ARCHIPELAGO
    ),
    ZorkGrandInquisitorItems.HOTSPOT_DUNGEON_MASTERS_LAIR_ENTRANCE: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_CROSSROADS
    ),
    ZorkGrandInquisitorItems.HOTSPOT_DUNGEON_MASTERS_HOUSE_EXIT: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_DM_LAIR
    ),
    ZorkGrandInquisitorItems.HOTSPOT_FLOOD_CONTROL_BUTTONS: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_FLOOD_CONTROL_DAM
    ),
    ZorkGrandInquisitorItems.HOTSPOT_FLOOD_CONTROL_DOORS: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_FLOOD_CONTROL_DAM
    ),
    ZorkGrandInquisitorItems.HOTSPOT_FROZEN_TREAT_MACHINE_COIN_SLOT: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_GUE_TECH
    ),
    ZorkGrandInquisitorItems.HOTSPOT_FROZEN_TREAT_MACHINE_DOORS: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_GUE_TECH
    ),
    ZorkGrandInquisitorItems.HOTSPOT_GLASS_CASE: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_CROSSROADS
    ),
    ZorkGrandInquisitorItems.HOTSPOT_GRAND_INQUISITOR_DOLL: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_PORT_FOOZLE
    ),
    ZorkGrandInquisitorItems.HOTSPOT_GUE_TECH_DOOR: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_GUE_TECH
    ),
    ZorkGrandInquisitorItems.HOTSPOT_GUE_TECH_GRASS: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_GUE_TECH
    ),
    ZorkGrandInquisitorItems.HOTSPOT_GUE_TECH_WINDOWS: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_GUE_TECH
    ),
    ZorkGrandInquisitorItems.HOTSPOT_HADES_PHONE_BUTTONS: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_HADES
    ),
    ZorkGrandInquisitorItems.HOTSPOT_HADES_PHONE_RECEIVER: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_HADES
    ),
    ZorkGrandInquisitorItems.HOTSPOT_HARRY: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_DM_LAIR
    ),
    ZorkGrandInquisitorItems.HOTSPOT_HARRYS_ASHTRAY: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_DM_LAIR
    ),
    ZorkGrandInquisitorItems.HOTSPOT_HARRYS_BIRD_BATH: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_DM_LAIR
    ),
    ZorkGrandInquisitorItems.HOTSPOT_IN_MAGIC_WE_TRUST_DOOR: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_CROSSROADS
    ),
    ZorkGrandInquisitorItems.HOTSPOT_JACKS_DOOR: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_PORT_FOOZLE
    ),
    ZorkGrandInquisitorItems.HOTSPOT_LOUDSPEAKER_VOLUME_BUTTONS: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_PORT_FOOZLE
    ),
    ZorkGrandInquisitorItems.HOTSPOT_MAILBOX_DOOR: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_WHITE_HOUSE
    ),
    ZorkGrandInquisitorItems.HOTSPOT_MAILBOX_FLAG: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_WHITE_HOUSE
    ),
    ZorkGrandInquisitorItems.HOTSPOT_MIRROR: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_DM_LAIR
    ),
    ZorkGrandInquisitorItems.HOTSPOT_MOSSY_GRATE: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_FLOOD_CONTROL_DAM
    ),
    ZorkGrandInquisitorItems.HOTSPOT_PORT_FOOZLE_PAST_TAVERN_DOOR: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_PORT_FOOZLE_PAST
    ),
    ZorkGrandInquisitorItems.HOTSPOT_PURPLE_WORDS: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_GUE_TECH
    ),
    ZorkGrandInquisitorItems.HOTSPOT_QUELBEE_HIVE: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_DM_LAIR
    ),
    ZorkGrandInquisitorItems.HOTSPOT_ROPE_BRIDGE: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_SPELL_LAB
    ),
    ZorkGrandInquisitorItems.HOTSPOT_SKULL_CAGE: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_WHITE_HOUSE
    ),
    ZorkGrandInquisitorItems.HOTSPOT_SNAPDRAGON: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_DM_LAIR
    ),
    ZorkGrandInquisitorItems.HOTSPOT_SODA_MACHINE_BUTTONS: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_GUE_TECH
    ),
    ZorkGrandInquisitorItems.HOTSPOT_SODA_MACHINE_COIN_SLOT: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_GUE_TECH
    ),
    ZorkGrandInquisitorItems.HOTSPOT_SOUVENIR_COIN_SLOT: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_FLOOD_CONTROL_DAM
    ),
    ZorkGrandInquisitorItems.HOTSPOT_SPELL_CHECKER: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_SPELL_LAB
    ),
    ZorkGrandInquisitorItems.HOTSPOT_SPELL_LAB_BRIDGE_EXIT: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_SPELL_LAB
    ),
    ZorkGrandInquisitorItems.HOTSPOT_SPELL_LAB_CHASM: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_SPELL_LAB
    ),
    ZorkGrandInquisitorItems.HOTSPOT_SPRING_MUSHROOM: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_DM_LAIR
    ),
    ZorkGrandInquisitorItems.HOTSPOT_STUDENT_ID_MACHINE: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_GUE_TECH
    ),
    ZorkGrandInquisitorItems.HOTSPOT_SUBWAY_TOKEN_SLOT: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_CROSSROADS
    ),
    ZorkGrandInquisitorItems.HOTSPOT_TAVERN_FLY: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_PORT_FOOZLE_PAST
    ),
    ZorkGrandInquisitorItems.HOTSPOT_TOTEMIZER_SWITCH: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_MONASTERY
    ),
    ZorkGrandInquisitorItems.HOTSPOT_TOTEMIZER_WHEELS: (
        ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_MONASTERY
    ),
}

hotspots_for_regional_hotspot: Dict[ZorkGrandInquisitorItems, Tuple[ZorkGrandInquisitorItems, ...]] = {
    ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_CROSSROADS: (
        ZorkGrandInquisitorItems.HOTSPOT_BUCKET,
        ZorkGrandInquisitorItems.HOTSPOT_DUNGEON_MASTERS_LAIR_ENTRANCE,
        ZorkGrandInquisitorItems.HOTSPOT_GLASS_CASE,
        ZorkGrandInquisitorItems.HOTSPOT_IN_MAGIC_WE_TRUST_DOOR,
        ZorkGrandInquisitorItems.HOTSPOT_SUBWAY_TOKEN_SLOT,
    ),
    ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_DM_LAIR: (
        ZorkGrandInquisitorItems.HOTSPOT_BLINDS,
        ZorkGrandInquisitorItems.HOTSPOT_CLOSET_DOOR,
        ZorkGrandInquisitorItems.HOTSPOT_DUNGEON_MASTERS_HOUSE_EXIT,
        ZorkGrandInquisitorItems.HOTSPOT_HARRY,
        ZorkGrandInquisitorItems.HOTSPOT_HARRYS_ASHTRAY,
        ZorkGrandInquisitorItems.HOTSPOT_HARRYS_BIRD_BATH,
        ZorkGrandInquisitorItems.HOTSPOT_MIRROR,
        ZorkGrandInquisitorItems.HOTSPOT_QUELBEE_HIVE,
        ZorkGrandInquisitorItems.HOTSPOT_SNAPDRAGON,
        ZorkGrandInquisitorItems.HOTSPOT_SPRING_MUSHROOM,
    ),
    ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_DRAGON_ARCHIPELAGO: (
        ZorkGrandInquisitorItems.HOTSPOT_DRAGON_CLAW,
        ZorkGrandInquisitorItems.HOTSPOT_DRAGON_NOSTRILS,
    ),
    ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_FLOOD_CONTROL_DAM: (
        ZorkGrandInquisitorItems.HOTSPOT_FLOOD_CONTROL_BUTTONS,
        ZorkGrandInquisitorItems.HOTSPOT_FLOOD_CONTROL_DOORS,
        ZorkGrandInquisitorItems.HOTSPOT_MOSSY_GRATE,
        ZorkGrandInquisitorItems.HOTSPOT_SOUVENIR_COIN_SLOT,
    ),
    ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_GUE_TECH: (
        ZorkGrandInquisitorItems.HOTSPOT_CANDY_MACHINE_BUTTONS,
        ZorkGrandInquisitorItems.HOTSPOT_CANDY_MACHINE_COIN_SLOT,
        ZorkGrandInquisitorItems.HOTSPOT_CANDY_MACHINE_VACUUM_SLOT,
        ZorkGrandInquisitorItems.HOTSPOT_CHANGE_MACHINE_SLOT,
        ZorkGrandInquisitorItems.HOTSPOT_DENTED_LOCKER,
        ZorkGrandInquisitorItems.HOTSPOT_DIRT_MOUND,
        ZorkGrandInquisitorItems.HOTSPOT_FROZEN_TREAT_MACHINE_COIN_SLOT,
        ZorkGrandInquisitorItems.HOTSPOT_FROZEN_TREAT_MACHINE_DOORS,
        ZorkGrandInquisitorItems.HOTSPOT_GUE_TECH_DOOR,
        ZorkGrandInquisitorItems.HOTSPOT_GUE_TECH_GRASS,
        ZorkGrandInquisitorItems.HOTSPOT_GUE_TECH_WINDOWS,
        ZorkGrandInquisitorItems.HOTSPOT_PURPLE_WORDS,
        ZorkGrandInquisitorItems.HOTSPOT_SODA_MACHINE_BUTTONS,
        ZorkGrandInquisitorItems.HOTSPOT_SODA_MACHINE_COIN_SLOT,
        ZorkGrandInquisitorItems.HOTSPOT_STUDENT_ID_MACHINE,
    ),
    ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_HADES: (
        ZorkGrandInquisitorItems.HOTSPOT_666_MAILBOX,
        ZorkGrandInquisitorItems.HOTSPOT_HADES_PHONE_BUTTONS,
        ZorkGrandInquisitorItems.HOTSPOT_HADES_PHONE_RECEIVER,
    ),
    ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_MONASTERY: (
        ZorkGrandInquisitorItems.HOTSPOT_CLOSING_THE_TIME_TUNNELS_HAMMER_SLOT,
        ZorkGrandInquisitorItems.HOTSPOT_CLOSING_THE_TIME_TUNNELS_LEVER,
        ZorkGrandInquisitorItems.HOTSPOT_TOTEMIZER_SWITCH,
        ZorkGrandInquisitorItems.HOTSPOT_TOTEMIZER_WHEELS,
    ),
    ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_PORT_FOOZLE: (
        ZorkGrandInquisitorItems.HOTSPOT_DOCK_WINCH,
        ZorkGrandInquisitorItems.HOTSPOT_GRAND_INQUISITOR_DOLL,
        ZorkGrandInquisitorItems.HOTSPOT_JACKS_DOOR,
        ZorkGrandInquisitorItems.HOTSPOT_LOUDSPEAKER_VOLUME_BUTTONS,
    ),
    ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_PORT_FOOZLE_PAST: (
        ZorkGrandInquisitorItems.HOTSPOT_ALPINES_QUANDRY_CARD_SLOTS,
        ZorkGrandInquisitorItems.HOTSPOT_PORT_FOOZLE_PAST_TAVERN_DOOR,
        ZorkGrandInquisitorItems.HOTSPOT_TAVERN_FLY,
    ),
    ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_SPELL_LAB: (
        ZorkGrandInquisitorItems.HOTSPOT_BLANK_SCROLL_BOX,
        ZorkGrandInquisitorItems.HOTSPOT_ROPE_BRIDGE,
        ZorkGrandInquisitorItems.HOTSPOT_SPELL_CHECKER,
        ZorkGrandInquisitorItems.HOTSPOT_SPELL_LAB_BRIDGE_EXIT,
        ZorkGrandInquisitorItems.HOTSPOT_SPELL_LAB_CHASM,
    ),
    ZorkGrandInquisitorItems.HOTSPOT_REGIONAL_WHITE_HOUSE: (
        ZorkGrandInquisitorItems.HOTSPOT_COOKING_POT,
        ZorkGrandInquisitorItems.HOTSPOT_MAILBOX_DOOR,
        ZorkGrandInquisitorItems.HOTSPOT_MAILBOX_FLAG,
        ZorkGrandInquisitorItems.HOTSPOT_SKULL_CAGE,
    ),
}

labels_for_enum_items: Dict[
    Union[
        ZorkGrandInquisitorCraftableSpellBehaviors,
        ZorkGrandInquisitorDeathsanity,
        ZorkGrandInquisitorGoals,
        ZorkGrandInquisitorHotspots,
        ZorkGrandInquisitorLandmarksanity,
        ZorkGrandInquisitorStartingLocations,
    ],
    str
] = {
    ZorkGrandInquisitorClientSeedInformation.REVEAL_NOTHING: "Reveal Nothing",
    ZorkGrandInquisitorClientSeedInformation.REVEAL_GOAL: "Reveal Goal",
    ZorkGrandInquisitorClientSeedInformation.REVEAL_GOAL_AND_OPTIONS: "Reveal Goal and Options",
    ZorkGrandInquisitorCraftableSpellBehaviors.VANILLA: "Vanilla",
    ZorkGrandInquisitorCraftableSpellBehaviors.ANY_SPELL: "Any Spell",
    ZorkGrandInquisitorCraftableSpellBehaviors.ANYTHING: "Anything",
    ZorkGrandInquisitorDeathsanity.OFF: "Off",
    ZorkGrandInquisitorDeathsanity.ON: "On",
    ZorkGrandInquisitorGoals.THREE_ARTIFACTS: "Three Artifacts",
    ZorkGrandInquisitorGoals.ARTIFACT_OF_MAGIC_HUNT: "Artifact of Magic Hunt",
    ZorkGrandInquisitorGoals.SPELL_HEIST: "Spell Heist",
    ZorkGrandInquisitorGoals.ZORK_TOUR: "Zork Tour",
    ZorkGrandInquisitorGoals.GRIM_JOURNEY: "Grim Journey",
    ZorkGrandInquisitorHotspots.ENABLED: "Enabled",
    ZorkGrandInquisitorHotspots.REQUIRE_ITEM_PER_REGION: "Require Item Per Region",
    ZorkGrandInquisitorHotspots.REQUIRE_ITEM_PER_HOTSPOT: "Require Item Per Hotspot",
    ZorkGrandInquisitorLandmarksanity.OFF: "Off",
    ZorkGrandInquisitorLandmarksanity.ON: "On",
    ZorkGrandInquisitorStartingLocations.PORT_FOOZLE: "Port Foozle",
    ZorkGrandInquisitorStartingLocations.CROSSROADS: "Crossroads",
    ZorkGrandInquisitorStartingLocations.DM_LAIR: "Dungeon Master's Lair",
    ZorkGrandInquisitorStartingLocations.DM_LAIR_INTERIOR: "Dungeon Master's House",
    ZorkGrandInquisitorStartingLocations.GUE_TECH: "GUE Tech",
    ZorkGrandInquisitorStartingLocations.SPELL_LAB: "Spell Lab",
    ZorkGrandInquisitorStartingLocations.HADES_SHORE: "Hades Shore",
    ZorkGrandInquisitorStartingLocations.SUBWAY_FLOOD_CONTROL_DAM: "Flood Control Dam #3",
    ZorkGrandInquisitorStartingLocations.MONASTERY: "Monastery Totemizer",
    ZorkGrandInquisitorStartingLocations.MONASTERY_EXHIBIT: "Monastery Exhibit",
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

voxam_cast_game_locations: Dict[
    ZorkGrandInquisitorStartingLocations,
    Tuple[Tuple[str, int], ...]
] = {
    ZorkGrandInquisitorStartingLocations.PORT_FOOZLE: (
        ("px1j", 0),
        ("ps20", 1),
        ("pe20", 1),
        ("pe2j", 0),
        ("pe30", 1),
        ("pe40", 1),
        ("pe50", 1),
        ("pe5e", 0),
        ("pe5f", 0),
        ("pe6e", 0),
    ),
    ZorkGrandInquisitorStartingLocations.CROSSROADS: (
        ("uc10", 1),
        ("uc20", 1),
        ("uc30", 1),
        ("uc3e", 0),
        ("uc40", 1),
        ("uc4e", 0),
        ("uc50", 1),
        ("uc6e", 0),
    ),
    ZorkGrandInquisitorStartingLocations.DM_LAIR: (
        ("dg10", 1),
        ("dg20", 1),
        ("dg4f", 0),
        ("dg30", 1),
        ("dg3e", 0),
    ),
    ZorkGrandInquisitorStartingLocations.DM_LAIR_INTERIOR: (
        ("dv10", 1),
        ("dv1j", 0),
        ("dw10", 1),
        ("dw1g", 0),
    ),
    ZorkGrandInquisitorStartingLocations.GUE_TECH: (
        ("tr20", 1),
        ("tr1k", 0),
        ("tr1g", 0),
        ("tr2g", 0),
        ("tr50", 1),
        ("tr5e", 0),
        ("tr5f", 0),
        ("tr5g", 0),
        ("tr4g", 0),
        ("tr4f", 0),
        ("th30", 1),
        ("th50", 1),
        ("th60", 1),
        ("th40", 1),
    ),
    ZorkGrandInquisitorStartingLocations.SPELL_LAB: (
        ("tp20", 1),
        ("tp50", 1),
        ("tp10", 1),
        ("tp2f", 0),
        ("tp2g", 0),
        ("tp2e", 0),
        ("tp30", 1),
        ("tp3f", 0),
        ("tp3e", 0),
        ("tp4f", 0),
        ("tp4e", 0),
    ),
    ZorkGrandInquisitorStartingLocations.HADES_SHORE: (
        ("uh10", 1),
        ("uh20", 1),
        ("uh2f", 0),
        ("uh2e", 0),
    ),
    ZorkGrandInquisitorStartingLocations.SUBWAY_FLOOD_CONTROL_DAM: (
        ("ue10", 1),
        ("ue20", 1),
        ("ue2g", 0),
        ("ue2e", 0),
        ("ue2j", 0),
        ("ue2k", 0),
        ("ue2f", 0),
    ),
    ZorkGrandInquisitorStartingLocations.MONASTERY: (
        ("mt20", 1),
        ("mt1e", 0),
        ("mt1f", 0),
        ("mt2g", 0),
        ("mt2e", 0),
        ("mt30", 1),
    ),
    ZorkGrandInquisitorStartingLocations.MONASTERY_EXHIBIT: (
        ("me10", 1),
        ("me1f", 0),
        ("me1h", 0),
        ("me1g", 0),
        ("me20", 1),
        ("me2h", 0),
        ("me2j", 0),
        ("me5f", 0),
        ("me2m", 0),
    ),
}

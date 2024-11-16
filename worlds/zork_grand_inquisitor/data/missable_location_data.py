from typing import Dict, NamedTuple, Optional, Tuple

from ..enums import ZorkGrandInquisitorItems, ZorkGrandInquisitorLocations


class ZorkGrandInquisitorMissableLocationGrantConditionsData(NamedTuple):
    game_location_condition: Optional[str]
    location_condition: Tuple[ZorkGrandInquisitorLocations, ...]
    item_conditions: Optional[Tuple[ZorkGrandInquisitorItems, ...]]


missable_location_grant_conditions_data: Dict[
    ZorkGrandInquisitorLocations, ZorkGrandInquisitorMissableLocationGrantConditionsData
] = {
    ZorkGrandInquisitorLocations.BOING_BOING_BOING:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            game_location_condition="dg3e",
            location_condition=(ZorkGrandInquisitorLocations.FLYING_SNAPDRAGON,),
            item_conditions=None,
        )
    ,
    ZorkGrandInquisitorLocations.BONK:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            game_location_condition="dg2f",
            location_condition=(ZorkGrandInquisitorLocations.PROZORKED,),
            item_conditions=(ZorkGrandInquisitorItems.HAMMER,),
        )
    ,
    ZorkGrandInquisitorLocations.DEATH_ARRESTED_WITH_JACK:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            game_location_condition="pe6e",
            location_condition=(ZorkGrandInquisitorLocations.ARREST_THE_VANDAL,),
            item_conditions=None,
        )
    ,
    ZorkGrandInquisitorLocations.DEATH_ATTACKED_THE_QUELBEES:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            game_location_condition="dg4f",
            location_condition=(ZorkGrandInquisitorLocations.OUTSMART_THE_QUELBEES,),
            item_conditions=None,
        )
    ,
    ZorkGrandInquisitorLocations.DEATH_LOST_GAME_OF_STRIP_GRUE_FIRE_WATER:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            game_location_condition="qs1e",
            location_condition=(ZorkGrandInquisitorLocations.STRIP_GRUE_FIRE_WATER,),
            item_conditions=None,
        )
    ,
    ZorkGrandInquisitorLocations.DEATH_LOST_SOUL_TO_OLD_SCRATCH:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            game_location_condition=None,
            location_condition=(ZorkGrandInquisitorLocations.OLD_SCRATCH_WINNER,),
            item_conditions=None,
        )
    ,
    ZorkGrandInquisitorLocations.DEATH_OUTSMARTED_BY_THE_QUELBEES:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            game_location_condition="dg4f",
            location_condition=(ZorkGrandInquisitorLocations.OUTSMART_THE_QUELBEES,),
            item_conditions=None,
        )
    ,
    ZorkGrandInquisitorLocations.DEATH_SLICED_UP_BY_THE_INVISIBLE_GUARD:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            game_location_condition="tp1e",
            location_condition=(ZorkGrandInquisitorLocations.YOU_GAINED_86_EXPERIENCE_POINTS,),
            item_conditions=None,
        )
    ,
    ZorkGrandInquisitorLocations.DEATH_STEPPED_INTO_THE_INFINITE:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            game_location_condition="th10",
            location_condition=(ZorkGrandInquisitorLocations.A_SMALLWAY,),
            item_conditions=None,
        )
    ,
    ZorkGrandInquisitorLocations.DEATH_SWALLOWED_BY_A_DRAGON:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            game_location_condition="cd20",
            location_condition=(ZorkGrandInquisitorLocations.THAR_SHE_BLOWS,),
            item_conditions=None,
        )
    ,
    ZorkGrandInquisitorLocations.DEATH_YOURE_NOT_CHARON:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            game_location_condition="hp60",
            location_condition=(ZorkGrandInquisitorLocations.OPEN_THE_GATES_OF_HELL,),
            item_conditions=None,
        )
    ,
    ZorkGrandInquisitorLocations.DEATH_ZORK_ROCKS_EXPLODED:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            game_location_condition="th3j",
            location_condition=(ZorkGrandInquisitorLocations.CRISIS_AVERTED,),
            item_conditions=None,
        )
    ,
    ZorkGrandInquisitorLocations.DENIED_BY_THE_LAKE_MONSTER:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            game_location_condition="dc10",
            location_condition=(ZorkGrandInquisitorLocations.WOW_IVE_NEVER_GONE_INSIDE_HIM_BEFORE,),
            item_conditions=(ZorkGrandInquisitorItems.SPELL_GOLGATEM,),
        )
    ,
    ZorkGrandInquisitorLocations.EMERGENCY_MAGICATRONIC_MESSAGE:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            game_location_condition="th10",
            location_condition=(ZorkGrandInquisitorLocations.ARTIFACTS_EXPLAINED,),
            item_conditions=None,
        )
    ,
    ZorkGrandInquisitorLocations.FAT_LOT_OF_GOOD_THATLL_DO_YA:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            game_location_condition="tp1e",
            location_condition=(ZorkGrandInquisitorLocations.YOU_GAINED_86_EXPERIENCE_POINTS,),
            item_conditions=(ZorkGrandInquisitorItems.SPELL_IGRAM,),
        )
    ,
    ZorkGrandInquisitorLocations.I_DONT_THINK_YOU_WOULDVE_WANTED_THAT_TO_WORK_ANYWAY:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            game_location_condition="dg2f",
            location_condition=(ZorkGrandInquisitorLocations.PROZORKED,),
            item_conditions=(ZorkGrandInquisitorItems.SPELL_THROCK,),
        )
    ,
    ZorkGrandInquisitorLocations.I_SPIT_ON_YOUR_FILTHY_COINAGE:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            game_location_condition="tp1e",
            location_condition=(ZorkGrandInquisitorLocations.YOU_GAINED_86_EXPERIENCE_POINTS,),
            item_conditions=(ZorkGrandInquisitorItems.POUCH_OF_ZORKMIDS,),
        )
    ,
    ZorkGrandInquisitorLocations.MEAD_LIGHT:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            game_location_condition="pe1e",
            location_condition=(
                ZorkGrandInquisitorLocations.FIRE_FIRE,
                ZorkGrandInquisitorLocations.WANT_SOME_RYE_COURSE_YA_DO,
            ),
            item_conditions=(ZorkGrandInquisitorItems.MEAD_LIGHT,),
        )
    ,
    ZorkGrandInquisitorLocations.MUSHROOM_HAMMERED:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            game_location_condition="dg3e",
            location_condition=(ZorkGrandInquisitorLocations.THROCKED_MUSHROOM_HAMMERED,),
            item_conditions=None,
        )
    ,
    ZorkGrandInquisitorLocations.NO_AUTOGRAPHS:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            game_location_condition="pe1e",
            location_condition=(ZorkGrandInquisitorLocations.FIRE_FIRE,),
            item_conditions=None,
        )
    ,
    ZorkGrandInquisitorLocations.NO_BONDAGE:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            game_location_condition="pe20",
            location_condition=(ZorkGrandInquisitorLocations.HELP_ME_CANT_BREATHE,),
            item_conditions=(
                ZorkGrandInquisitorItems.WELL_ROPE,
                ZorkGrandInquisitorItems.SPELL_GLORF,
            ),
        )
    ,
    ZorkGrandInquisitorLocations.TALK_TO_ME_GRAND_INQUISITOR:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            game_location_condition="pe5e",
            location_condition=(ZorkGrandInquisitorLocations.FIRE_FIRE,),
            item_conditions=None,
        )
    ,
    ZorkGrandInquisitorLocations.THATS_A_ROPE:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            game_location_condition="pe1e",
            location_condition=(ZorkGrandInquisitorLocations.FIRE_FIRE,),
            item_conditions=(
                ZorkGrandInquisitorItems.WELL_ROPE,
                ZorkGrandInquisitorItems.SPELL_GLORF,
            ),
        )
    ,
    ZorkGrandInquisitorLocations.THATS_IT_JUST_KEEP_HITTING_THOSE_BUTTONS:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            game_location_condition="us2e",
            location_condition=(ZorkGrandInquisitorLocations.ENJOY_YOUR_TRIP,),
            item_conditions=None,
        )
    ,
    ZorkGrandInquisitorLocations.THATS_STILL_A_ROPE:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            game_location_condition="tp1e",
            location_condition=(ZorkGrandInquisitorLocations.YOU_GAINED_86_EXPERIENCE_POINTS,),
            item_conditions=(
                ZorkGrandInquisitorItems.WELL_ROPE,
                ZorkGrandInquisitorItems.SPELL_GLORF,
            ),
        )
    ,
    ZorkGrandInquisitorLocations.WHAT_ARE_YOU_STUPID:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            game_location_condition="pe1e",
            location_condition=(
                ZorkGrandInquisitorLocations.FIRE_FIRE,
                ZorkGrandInquisitorLocations.HELP_ME_CANT_BREATHE,
            ),
            item_conditions=(ZorkGrandInquisitorItems.PLASTIC_SIX_PACK_HOLDER,),
        )
    ,
    ZorkGrandInquisitorLocations.YAD_GOHDNUORGREDNU_3_YRAUBORF:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            game_location_condition="dw10",
            location_condition=(ZorkGrandInquisitorLocations.REASSEMBLE_SNAVIG,),
            item_conditions=None,
        )
    ,
    ZorkGrandInquisitorLocations.YOUR_PUNY_WEAPONS_DONT_PHASE_ME_BABY:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            game_location_condition="dv10",
            location_condition=(ZorkGrandInquisitorLocations.WANT_SOME_RYE_COURSE_YA_DO,),
            item_conditions=(ZorkGrandInquisitorItems.SWORD, ZorkGrandInquisitorItems.HOTSPOT_HARRY),
        )
    ,
    ZorkGrandInquisitorLocations.YOU_DONT_GO_MESSING_WITH_A_MANS_ZIPPER:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            game_location_condition="tp1e",
            location_condition=(ZorkGrandInquisitorLocations.YOU_GAINED_86_EXPERIENCE_POINTS,),
            item_conditions=(ZorkGrandInquisitorItems.SPELL_REZROV,),
        )
    ,
    ZorkGrandInquisitorLocations.YOU_WANT_A_PIECE_OF_ME_DOCK_BOY:
        ZorkGrandInquisitorMissableLocationGrantConditionsData(
            game_location_condition="pe20",
            location_condition=(ZorkGrandInquisitorLocations.HELP_ME_CANT_BREATHE,),
            item_conditions=None,
        )
    ,
}
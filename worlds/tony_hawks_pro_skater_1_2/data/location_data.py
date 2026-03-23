from typing import Dict, List, NamedTuple, Optional, Tuple, Union

from ..data.game_data import level_to_level_types, skater_to_specials

from ..enums import (
    TonyHawksProSkater12APTags,
    TonyHawksProSkater12Levels,
    TonyHawksProSkater12LevelTypes,
    TonyHawksProSkater12Skaters,
    TonyHawksProSkater12Specials,
)


TonyHawksProSkater12LocationRule = Union[
    Tuple[
        Union[
            Tuple[str, int],
            Tuple[
                Tuple[str, int],
                ...,
            ],
        ],
        ...,
    ],
    None,
]


class TonyHawksProSkater12LocationData(NamedTuple):
    archipelago_id: Optional[int]
    region: str
    tags: Optional[Tuple[TonyHawksProSkater12APTags, ...]] = None
    requirements: TonyHawksProSkater12LocationRule = None


locations_requiring_stats: List[str] = [
    f"{TonyHawksProSkater12Levels.MALL.value} - SKATER - Secret Tape",
    f"{TonyHawksProSkater12Levels.DOWNTOWN.value} - SKATER - Secret Tape",
    f"{TonyHawksProSkater12Levels.DOWNHILL_JAM.value} - SKATER - Secret Tape",
    f"{TonyHawksProSkater12Levels.STREETS.value} - SKATER - SKATE Letter A",  # BP_Collectible_THPS1_Skate_A
    f"{TonyHawksProSkater12Levels.STREETS.value} - SKATER - SKATE Letter E",  # BP_Collectible_THPS1_Skate_E
    f"{TonyHawksProSkater12Levels.STREETS.value} - SKATER - Secret Tape",
    f"{TonyHawksProSkater12Levels.SCHOOL_II.value} - SKATER - Secret Tape",
    f"{TonyHawksProSkater12Levels.VENICE_BEACH.value} - SKATER - Secret Tape",
    f"{TonyHawksProSkater12Levels.PHILADELPHIA.value} - SKATER - SKATE Letter K",  # BP_Collectible_Skate_K
]

location_offset: int = 10000000

location_data: Dict[str, TonyHawksProSkater12LocationData] = dict()

i: int
level: TonyHawksProSkater12Levels
for i, level in enumerate(TonyHawksProSkater12Levels):
    level_offset: int = i * 10000

    ii: int
    skater: TonyHawksProSkater12Skaters
    for ii, skater in enumerate(TonyHawksProSkater12Skaters):
        skater_offset: int = ii * 100

        # High Score
        location_data[f"{level.value} - {skater.value} - High Score"] = TonyHawksProSkater12LocationData(
            archipelago_id=location_offset + level_offset + skater_offset + 1,
            region=f"{level.value} - {skater.value}",
            tags=(
                TonyHawksProSkater12APTags.HIGH_SCORE_LOCATION,
                eval(f"TonyHawksProSkater12APTags.{level.name}_LOCATION"),
                eval(f"TonyHawksProSkater12APTags.{skater.name}_LOCATION"),
                eval(f"TonyHawksProSkater12APTags.{level.name}_{skater.name}_LOCATION"),
            ),
            requirements=None,
        )

        # Pro Score
        location_data[f"{level.value} - {skater.value} - Pro Score"] = TonyHawksProSkater12LocationData(
            archipelago_id=location_offset + level_offset + skater_offset + 2,
            region=f"{level.value} - {skater.value}",
            tags=(
                TonyHawksProSkater12APTags.PRO_SCORE_LOCATION,
                eval(f"TonyHawksProSkater12APTags.{level.name}_LOCATION"),
                eval(f"TonyHawksProSkater12APTags.{skater.name}_LOCATION"),
                eval(f"TonyHawksProSkater12APTags.{level.name}_{skater.name}_LOCATION"),
            ),
            requirements=(
                (f"Progressive Stats: {skater.value}", 1),
                (
                    (f"Spin Tricks: {skater.value}", 1),
                    (f"Extra Tricks: {skater.value}", 1),
                ),
            ),
        )

        # Sick Score
        location_data[f"{level.value} - {skater.value} - Sick Score"] = TonyHawksProSkater12LocationData(
            archipelago_id=location_offset + level_offset + skater_offset + 3,
            region=f"{level.value} - {skater.value}",
            tags=(
                TonyHawksProSkater12APTags.SICK_SCORE_LOCATION,
                eval(f"TonyHawksProSkater12APTags.{level.name}_LOCATION"),
                eval(f"TonyHawksProSkater12APTags.{skater.name}_LOCATION"),
                eval(f"TonyHawksProSkater12APTags.{level.name}_{skater.name}_LOCATION"),
            ),
            requirements=(
                (f"Progressive Stats: {skater.value}", 2),
                (f"Extra Tricks: {skater.value}", 1),
                (f"Spin Tricks: {skater.value}", 1),
            ),
        )

        # Platinum Score
        location_data[f"{level.value} - {skater.value} - Platinum Score"] = TonyHawksProSkater12LocationData(
            archipelago_id=location_offset + level_offset + skater_offset + 4,
            region=f"{level.value} - {skater.value}",
            tags=(
                TonyHawksProSkater12APTags.PLATINUM_SCORE_LOCATION,
                eval(f"TonyHawksProSkater12APTags.{level.name}_LOCATION"),
                eval(f"TonyHawksProSkater12APTags.{skater.name}_LOCATION"),
                eval(f"TonyHawksProSkater12APTags.{level.name}_{skater.name}_LOCATION"),
            ),
            requirements=(
                (f"Progressive Stats: {skater.value}", 2),
                (f"Progressive Manual Tricks: {skater.value}", 1),
                (f"Double Score: {skater.value}", 1),
                (f"Extra Tricks: {skater.value}", 1),
                (f"Spin Tricks: {skater.value}", 1),
            ),
        )

        # High Combo
        location_data[f"{level.value} - {skater.value} - High Combo"] = TonyHawksProSkater12LocationData(
            archipelago_id=location_offset + level_offset + skater_offset + 5,
            region=f"{level.value} - {skater.value}",
            tags=(
                TonyHawksProSkater12APTags.HIGH_COMBO_LOCATION,
                eval(f"TonyHawksProSkater12APTags.{level.name}_LOCATION"),
                eval(f"TonyHawksProSkater12APTags.{skater.name}_LOCATION"),
                eval(f"TonyHawksProSkater12APTags.{level.name}_{skater.name}_LOCATION"),
            ),
            requirements=(
                (f"Progressive Manual Tricks: {skater.value}", 1),
            ),
        )

        # Pro Combo
        location_data[f"{level.value} - {skater.value} - Pro Combo"] = TonyHawksProSkater12LocationData(
            archipelago_id=location_offset + level_offset + skater_offset + 6,
            region=f"{level.value} - {skater.value}",
            tags=(
                TonyHawksProSkater12APTags.PRO_COMBO_LOCATION,
                eval(f"TonyHawksProSkater12APTags.{level.name}_LOCATION"),
                eval(f"TonyHawksProSkater12APTags.{skater.name}_LOCATION"),
                eval(f"TonyHawksProSkater12APTags.{level.name}_{skater.name}_LOCATION"),
            ),
            requirements=(
                (f"Progressive Stats: {skater.value}", 1),
                (f"Progressive Manual Tricks: {skater.value}", 1),
                (f"Transfers: {skater.value}", 1),
                (f"Stance Switching: {skater.value}", 1),
            ),
        )

        # Sick Combo
        location_data[f"{level.value} - {skater.value} - Sick Combo"] = TonyHawksProSkater12LocationData(
            archipelago_id=location_offset + level_offset + skater_offset + 7,
            region=f"{level.value} - {skater.value}",
            tags=(
                TonyHawksProSkater12APTags.SICK_COMBO_LOCATION,
                eval(f"TonyHawksProSkater12APTags.{level.name}_LOCATION"),
                eval(f"TonyHawksProSkater12APTags.{skater.name}_LOCATION"),
                eval(f"TonyHawksProSkater12APTags.{level.name}_{skater.name}_LOCATION"),
            ),
            requirements=(
                (f"Progressive Stats: {skater.value}", 2),
                (f"Progressive Manual Tricks: {skater.value}", 1),
                (f"Transfers: {skater.value}", 1),
                (f"Stance Switching: {skater.value}", 1),
                (f"Wallplants: {skater.value}", 1),
                (f"Extra Tricks: {skater.value}", 1),
            ),
        )

        # Platinum Combo
        location_data[f"{level.value} - {skater.value} - Platinum Combo"] = TonyHawksProSkater12LocationData(
            archipelago_id=location_offset + level_offset + skater_offset + 8,
            region=f"{level.value} - {skater.value}",
            tags=(
                TonyHawksProSkater12APTags.PLATINUM_COMBO_LOCATION,
                eval(f"TonyHawksProSkater12APTags.{level.name}_LOCATION"),
                eval(f"TonyHawksProSkater12APTags.{skater.name}_LOCATION"),
                eval(f"TonyHawksProSkater12APTags.{level.name}_{skater.name}_LOCATION"),
            ),
            requirements=(
                (f"Progressive Stats: {skater.value}", 2),
                (f"Progressive Manual Tricks: {skater.value}", 1),
                (f"Double Score: {skater.value}", 1),
                (f"Transfers: {skater.value}", 1),
                (f"Stance Switching: {skater.value}", 1),
                (f"Wallplants: {skater.value}", 1),
                (f"Extra Tricks: {skater.value}", 1),
                (f"Spin Tricks: {skater.value}", 1),
            ),
        )

        # Long Grind
        location_data[f"{level.value} - {skater.value} - Long Grind Trick"] = TonyHawksProSkater12LocationData(
            archipelago_id=location_offset + level_offset + skater_offset + 9,
            region=f"{level.value} - {skater.value}",
            tags=(
                TonyHawksProSkater12APTags.LONG_GRIND_TRICK_LOCATION,
                eval(f"TonyHawksProSkater12APTags.{level.name}_LOCATION"),
                eval(f"TonyHawksProSkater12APTags.{skater.name}_LOCATION"),
                eval(f"TonyHawksProSkater12APTags.{level.name}_{skater.name}_LOCATION"),
            ),
            requirements=(
                (f"Progressive Stats: {skater.value}", 2),
                (f"Progressive Grind Tricks: {skater.value}", 1),
            ),
        )

        # Long Lip
        location_data[f"{level.value} - {skater.value} - Long Lip Trick"] = TonyHawksProSkater12LocationData(
            archipelago_id=location_offset + level_offset + skater_offset + 10,
            region=f"{level.value} - {skater.value}",
            tags=(
                TonyHawksProSkater12APTags.LONG_LIP_TRICK_LOCATION,
                eval(f"TonyHawksProSkater12APTags.{level.name}_LOCATION"),
                eval(f"TonyHawksProSkater12APTags.{skater.name}_LOCATION"),
                eval(f"TonyHawksProSkater12APTags.{level.name}_{skater.name}_LOCATION"),
            ),
            requirements=(
                (f"Progressive Stats: {skater.value}", 2),
                (f"Progressive Lip Tricks: {skater.value}", 1),
            ),
        )

        # Long Manual
        location_data[f"{level.value} - {skater.value} - Long Manual Trick"] = TonyHawksProSkater12LocationData(
            archipelago_id=location_offset + level_offset + skater_offset + 11,
            region=f"{level.value} - {skater.value}",
            tags=(
                TonyHawksProSkater12APTags.LONG_MANUAL_TRICK_LOCATION,
                eval(f"TonyHawksProSkater12APTags.{level.name}_LOCATION"),
                eval(f"TonyHawksProSkater12APTags.{skater.name}_LOCATION"),
                eval(f"TonyHawksProSkater12APTags.{level.name}_{skater.name}_LOCATION"),
            ),
            requirements=(
                (f"Progressive Stats: {skater.value}", 2),
                (f"Progressive Manual Tricks: {skater.value}", 1),
            ),
        )

        # Gaps
        iii: int
        for iii in range(1, 11):
            location_data[f"{level.value} - {skater.value} - Gap #{iii}"] = TonyHawksProSkater12LocationData(
                archipelago_id=location_offset + level_offset + skater_offset + 11 + iii,
                region=f"{level.value} - {skater.value}",
                tags=(
                    TonyHawksProSkater12APTags.GAP_LOCATION,
                    eval(f"TonyHawksProSkater12APTags.{level.name}_LOCATION"),
                    eval(f"TonyHawksProSkater12APTags.{skater.name}_LOCATION"),
                    eval(f"TonyHawksProSkater12APTags.{level.name}_{skater.name}_LOCATION"),
                ),
                requirements=(
                    (f"Progressive Stats: {skater.value}", 2),
                    (f"Progressive Manual Tricks: {skater.value}", 1),
                    (f"Progressive Special Meter: {skater.value}", 1),
                    (f"Transfers: {skater.value}", 1),
                ),
            )

        if level_to_level_types.get(level) != TonyHawksProSkater12LevelTypes.OBJECTIVES:
            continue

        # SKATE Letters
        iii: int
        letter: str
        for iii, letter in enumerate(["S", "K", "A", "T", "E"]):
            logic_lookup_key = f"{level.value} - SKATER - SKATE Letter {letter}"
            logic_requirements: Optional[TonyHawksProSkater12LocationRule] = None

            if logic_lookup_key in locations_requiring_stats:
                logic_requirements = (
                    (f"Progressive Stats: {skater.value}", 2),
                )

            location_data[f"{level.value} - {skater.value} - SKATE Letter {letter}"] = TonyHawksProSkater12LocationData(
                archipelago_id=location_offset + level_offset + skater_offset + 25 + iii,
                region=f"{level.value} - {skater.value}",
                tags=(
                    TonyHawksProSkater12APTags.SKATE_LETTER_LOCATION,
                    eval(f"TonyHawksProSkater12APTags.{level.name}_LOCATION"),
                    eval(f"TonyHawksProSkater12APTags.{skater.name}_LOCATION"),
                    eval(f"TonyHawksProSkater12APTags.{level.name}_{skater.name}_LOCATION"),
                ),
                requirements=logic_requirements,
            )

        # Secret Tape
        logic_lookup_key = f"{level.value} - SKATER - Secret Tape"
        logic_requirements: Optional[TonyHawksProSkater12LocationRule] = None

        if logic_lookup_key in locations_requiring_stats:
            logic_requirements = (
                (f"Progressive Stats: {skater.value}", 2),
            )

        location_data[f"{level.value} - {skater.value} - Secret Tape"] = TonyHawksProSkater12LocationData(
            archipelago_id=location_offset + level_offset + skater_offset + 75,
            region=f"{level.value} - {skater.value}",
            tags=(
                TonyHawksProSkater12APTags.SECRET_TAPE_LOCATION,
                eval(f"TonyHawksProSkater12APTags.{level.name}_LOCATION"),
                eval(f"TonyHawksProSkater12APTags.{skater.name}_LOCATION"),
                eval(f"TonyHawksProSkater12APTags.{level.name}_{skater.name}_LOCATION"),
            ),
            requirements=logic_requirements,
        )

# Signature Specials
location_offset = 1000000

i: int
skater: TonyHawksProSkater12Skaters
for i, skater in enumerate(TonyHawksProSkater12Skaters):
    skater_offset: int = i * 10

    signature_specials: List[TonyHawksProSkater12Specials] = skater_to_specials[skater]

    ii: int
    special: TonyHawksProSkater12Specials
    for ii, special in enumerate(signature_specials):
        location_data[f"{skater.value} - Special - {special.value}"] = TonyHawksProSkater12LocationData(
            archipelago_id=location_offset + skater_offset + ii,
            region=f"{skater.value}",
            tags=(
                TonyHawksProSkater12APTags.SIGNATURE_SPECIAL_LOCATION,
                eval(f"TonyHawksProSkater12APTags.{skater.name}_LOCATION"),
            ),
            requirements=(
                (f"Progressive Special Meter: {skater.value}", 1),
                (f"Progressive Stats: {skater.value}", 1),
                (f"Progressive Manual Tricks: {skater.value}", 1),
            ),
        )

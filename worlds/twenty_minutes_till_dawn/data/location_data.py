from typing import Dict, List, NamedTuple, Optional, Tuple

from ..enums import TwentyMinutesCharacters, TwentyMinutesMaps, TwentyMinutesTags, TwentyMinutesWeapons


class TwentyMinutesLocationData(NamedTuple):
    archipelago_id: Optional[int]
    region: str
    tags: Optional[Tuple[TwentyMinutesTags, ...]] = None


location_base_offset: int = 10000000

location_data: Dict[str, TwentyMinutesLocationData] = dict()

# Kill Count Locations
location_offset = 0

kill_count_checkpoints_by_chunk: List[Tuple[int, int, int]] = [
    (150, 350, 500),
    (750, 1000, 1250),
    (1650, 2100, 2500),
    (3000, 3500, 4000),
    (5000, 6250, 7500),
]

i: int
map_: TwentyMinutesMaps
for i, map_ in enumerate(TwentyMinutesMaps):
    map_offset = i * 1000

    chunk_index: int
    chunk_kill_counts: Tuple[int, int, int]
    for chunk_index, chunk_kill_counts in enumerate(kill_count_checkpoints_by_chunk):
        chunk_offset = chunk_index * 10

        checkpoint_index: int
        kill_count: int
        for checkpoint_index, kill_count in enumerate(chunk_kill_counts):
            location_data[f"{map_.value} - {kill_count} Kills"] = TwentyMinutesLocationData(
                archipelago_id=location_base_offset + location_offset + map_offset + chunk_offset + checkpoint_index,
                region=map_.value,
                tags=(
                    TwentyMinutesTags.KILL_COUNT_LOCATION,
                    getattr(TwentyMinutesTags, f"{map_.name}_LOCATION"),
                    getattr(TwentyMinutesTags, f"MAP_SEGMENT_{chunk_index + 1}_LOCATION"),
                ),
            )

# Survival Time Locations X Character
location_offset = 100000

survival_minutes_by_chunk: List[List[int]] = [
    [1, 3],
    [5, 7],
    [9, 11],
    [13, 15],
    [17, 19],
]

i: int
map_: TwentyMinutesMaps
for i, map_ in enumerate(TwentyMinutesMaps):
    map_offset = i * 10000

    j: int
    character: TwentyMinutesCharacters
    for j, character in enumerate(TwentyMinutesCharacters):
        character_offset = j * 100

        chunk_index: int
        chunk_minutes: List[int]
        for chunk_index, chunk_minutes in enumerate(survival_minutes_by_chunk):
            chunk_offset = chunk_index * 10

            checkpoint_index: int
            minutes: int
            for checkpoint_index, minutes in enumerate(chunk_minutes):
                minute_word: str = "Minute" if minutes == 1 else "Minutes"

                location_data[f"{map_.value} - {character.value} - Survive {minutes} {minute_word}"] = TwentyMinutesLocationData(
                    archipelago_id=location_base_offset + location_offset + map_offset + character_offset + chunk_offset + checkpoint_index,
                    region=f"{map_.value} - {character.value}",
                    tags=(
                        TwentyMinutesTags.SURVIVAL_TIME_LOCATION,
                        getattr(TwentyMinutesTags, f"{map_.name}_LOCATION"),
                        getattr(TwentyMinutesTags, f"{character.name}_LOCATION"),
                        getattr(TwentyMinutesTags, f"MAP_SEGMENT_{chunk_index + 1}_LOCATION"),
                    ),
                )

        # Alternate location. Used with maps capped to 12 minutes
        location_data[f"{map_.value} - {character.value} - Survive the Run"] = TwentyMinutesLocationData(
            archipelago_id=location_base_offset + location_offset + map_offset + character_offset + 25,
            region=f"{map_.value} - {character.value}",
            tags=(
                TwentyMinutesTags.SURVIVAL_TIME_LOCATION,
                getattr(TwentyMinutesTags, f"{map_.name}_LOCATION"),
                getattr(TwentyMinutesTags, f"{character.name}_LOCATION"),
                TwentyMinutesTags.MAP_SEGMENT_3_LOCATION,
            ),
        )

# Survival Time Locations X Weapon
location_offset = 500000

i: int
map_: TwentyMinutesMaps
for i, map_ in enumerate(TwentyMinutesMaps):
    map_offset = i * 10000

    j: int
    weapon: TwentyMinutesWeapons
    for j, weapon in enumerate(TwentyMinutesWeapons):
        weapon_offset = j * 100

        chunk_index: int
        chunk_minutes: List[int]
        for chunk_index, chunk_minutes in enumerate(survival_minutes_by_chunk):
            chunk_offset = chunk_index * 10

            checkpoint_index: int
            minutes: int
            for checkpoint_index, minutes in enumerate(chunk_minutes):
                minute_word: str = "Minute" if minutes == 1 else "Minutes"

                location_data[f"{map_.value} - {weapon.value} - Survive {minutes} {minute_word}"] = TwentyMinutesLocationData(
                    archipelago_id=location_base_offset + location_offset + map_offset + weapon_offset + chunk_offset + checkpoint_index,
                    region=f"{map_.value} - {weapon.value}",
                    tags=(
                        TwentyMinutesTags.SURVIVAL_TIME_LOCATION,
                        getattr(TwentyMinutesTags, f"{map_.name}_LOCATION"),
                        getattr(TwentyMinutesTags, f"{weapon.name}_LOCATION"),
                        getattr(TwentyMinutesTags, f"MAP_SEGMENT_{chunk_index + 1}_LOCATION"),
                    ),
                )

        # Alternate location. Used with maps capped to 12 minutes
        location_data[f"{map_.value} - {weapon.value} - Survive the Run"] = TwentyMinutesLocationData(
            archipelago_id=location_base_offset + location_offset + map_offset + weapon_offset + 25,
            region=f"{map_.value} - {weapon.value}",
            tags=(
                TwentyMinutesTags.SURVIVAL_TIME_LOCATION,
                getattr(TwentyMinutesTags, f"{map_.name}_LOCATION"),
                getattr(TwentyMinutesTags, f"{weapon.name}_LOCATION"),
                TwentyMinutesTags.MAP_SEGMENT_3_LOCATION,
            ),
        )

# Level Up Locations X Character
location_offset = 1000000

level_checkpoints_by_chunk: List[List[int]] = [
    [5, 10],
    [13, 15],
    [18, 20],
    [23, 25],
    [30, 35],
]

i: int
map_: TwentyMinutesMaps
for i, map_ in enumerate(TwentyMinutesMaps):
    map_offset = i * 10000

    j: int
    character: TwentyMinutesCharacters
    for j, character in enumerate(TwentyMinutesCharacters):
        character_offset = j * 100

        chunk_index: int
        chunk_levels: List[int]
        for chunk_index, chunk_levels in enumerate(level_checkpoints_by_chunk):
            chunk_offset = chunk_index * 10

            checkpoint_index: int
            level: int
            for checkpoint_index, level in enumerate(chunk_levels):
                location_data[f"{map_.value} - {character.value} - Reach Level {level}"] = TwentyMinutesLocationData(
                    archipelago_id=location_base_offset + location_offset + map_offset + character_offset + chunk_offset + checkpoint_index,
                    region=f"{map_.value} - {character.value}",
                    tags=(
                        TwentyMinutesTags.LEVEL_UP_LOCATION,
                        getattr(TwentyMinutesTags, f"{map_.name}_LOCATION"),
                        getattr(TwentyMinutesTags, f"{character.name}_LOCATION"),
                        getattr(TwentyMinutesTags, f"MAP_SEGMENT_{chunk_index + 1}_LOCATION"),
                    ),
                )

# Level Up Locations X Weapon
location_offset = 1500000

i: int
map_: TwentyMinutesMaps
for i, map_ in enumerate(TwentyMinutesMaps):
    map_offset = i * 10000

    j: int
    weapon: TwentyMinutesWeapons
    for j, weapon in enumerate(TwentyMinutesWeapons):
        weapon_offset = j * 100

        chunk_index: int
        chunk_levels: List[int]
        for chunk_index, chunk_levels in enumerate(level_checkpoints_by_chunk):
            chunk_offset = chunk_index * 10

            checkpoint_index: int
            level: int
            for checkpoint_index, level in enumerate(chunk_levels):
                location_data[f"{map_.value} - {weapon.value} - Reach Level {level}"] = TwentyMinutesLocationData(
                    archipelago_id=location_base_offset + location_offset + map_offset + weapon_offset + chunk_offset + checkpoint_index,
                    region=f"{map_.value} - {weapon.value}",
                    tags=(
                        TwentyMinutesTags.LEVEL_UP_LOCATION,
                        getattr(TwentyMinutesTags, f"{map_.name}_LOCATION"),
                        getattr(TwentyMinutesTags, f"{weapon.name}_LOCATION"),
                        getattr(TwentyMinutesTags, f"MAP_SEGMENT_{chunk_index + 1}_LOCATION"),
                    ),
                )

from typing import Any, Dict, List

import copy

from .data.item_data import DrMarioItemData, item_data
from .data.location_data import DrMarioLocationData, location_data

from .enums import (
    DrMarioColors,
    DrMarioFinalLevelSpeedOptions,
    DrMarioGoalOptions,
    DrMarioLevels,
    DrMarioMusicTracks,
    DrMarioNesColors,
    DrMarioSpeeds,
    DrMarioSpeedUpBehaviorOptions,
    DrMarioTags,
    DrMarioTrapTypes,
)


def id_to_final_level_speeds() -> Dict[int, DrMarioFinalLevelSpeedOptions]:
    return {speed.value: speed for speed in DrMarioFinalLevelSpeedOptions}


def id_to_goals() -> Dict[int, DrMarioGoalOptions]:
    return {goal.value: goal for goal in DrMarioGoalOptions}


def id_to_items() -> Dict[int, str]:
    return {data.archipelago_id: item for item, data in item_data.items()}


def id_to_locations() -> Dict[int, str]:
    return {
        data.archipelago_id: location
        for location, data in location_data.items()
        if data.archipelago_id is not None
    }


def id_to_speed_up_behaviors() -> Dict[int, DrMarioSpeedUpBehaviorOptions]:
    return {behavior.value: behavior for behavior in DrMarioSpeedUpBehaviorOptions}


def item_groups() -> Dict[str, List[str]]:
    groups: Dict[str, List[str]] = dict()

    item: str
    data: DrMarioItemData
    for item, data in item_data.items():
        if data.tags is not None:
            tag: DrMarioTags
            for tag in data.tags:
                groups.setdefault(tag.value, list()).append(item)

    return {k: v for k, v in groups.items() if len(v)}


def item_names_to_id() -> Dict[str, int]:
    return {item: data.archipelago_id for item, data in item_data.items()}


def items_with_tag(tag: DrMarioTags) -> List[str]:
    item: str
    data: DrMarioItemData

    return [item for item, data in item_data.items() if data.tags is not None and tag in data.tags]


def location_groups() -> Dict[str, List[str]]:
    groups: Dict[str, List[str]] = dict()

    location: str
    data: DrMarioLocationData
    for location, data in location_data.items():
        if data.tags is not None:
            tag: DrMarioTags
            for tag in data.tags:
                groups.setdefault(tag.value, list()).append(location)

    return {k: v for k, v in groups.items() if len(v)}


def location_names_to_id() -> Dict[str, int]:
    return {
        location: data.archipelago_id
        for location, data in location_data.items()
        if data.archipelago_id is not None
    }


def locations_with_tag(tag: DrMarioTags) -> List[str]:
    location: str
    data: DrMarioLocationData

    return [location for location, data in location_data.items() if data.tags is not None and tag in data.tags]


def process_slot_data(slot_data: Dict[str, Any]) -> Dict[str, Any]:
    slot_data_processed: Dict[str, Any] = copy.deepcopy(slot_data)

    slot_data_processed["goal"] = id_to_goals()[slot_data["goal"]]
    slot_data_processed["final_level_speed"] = id_to_final_level_speeds()[slot_data["final_level_speed"]]
    slot_data_processed["speed_up_behavior"] = id_to_speed_up_behaviors()[slot_data["speed_up_behavior"]]

    trap_weights: Dict[DrMarioTrapTypes, int] = dict()

    trap_type_name: str
    weight: int
    for trap_type_name, weight in slot_data["trap_weights"].items():
        trap_weights[DrMarioTrapTypes(trap_type_name)] = weight

    slot_data_processed["trap_weights"] = trap_weights

    slot_data_processed["selected_levels"] = [
        DrMarioLevels(level_name) for level_name in slot_data["selected_levels"]
    ]

    slot_data_processed["selected_starting_levels"] = [
        DrMarioLevels(level_name) for level_name in slot_data["selected_starting_levels"]
    ]

    slot_data_processed["selected_final_level"] = DrMarioLevels(slot_data["selected_final_level"])

    slot_data_processed["level_to_starting_pill"] = {
        DrMarioLevels(level_name): pill for level_name, pill in slot_data["level_to_starting_pill"].items()
    }

    slot_data_processed["level_to_starting_rotation"] = {
        DrMarioLevels(level_name): rotation for level_name, rotation in slot_data["level_to_starting_rotation"].items()
    }

    slot_data_processed["level_to_starting_garbage_levels"] = {
        DrMarioLevels(level_name): garbage_levels
        for level_name, garbage_levels in slot_data["level_to_starting_garbage_levels"].items()
    }

    slot_data_processed["level_to_virus_count_delta"] = {
        DrMarioLevels(level_name): delta for level_name, delta in slot_data["level_to_virus_count_delta"].items()
    }

    slot_data_processed["selected_music_tracks"] = {
        DrMarioMusicTracks(music_track_name): DrMarioMusicTracks(selected_music_track_name)
        for music_track_name, selected_music_track_name in slot_data["selected_music_tracks"].items()
    }

    slot_data_processed["selected_mario_color"] = DrMarioNesColors(slot_data["selected_mario_color"])

    slot_data_processed["selected_virus_colors"] = {
        DrMarioColors(color_name): DrMarioNesColors(nes_color)
        for color_name, nes_color in slot_data["selected_virus_colors"].items()
    }

    slot_data_processed["level_to_checkerboard_colors"] = {
        DrMarioLevels(level_name): {DrMarioSpeeds(speed_name): DrMarioNesColors(nes_color) for speed_name, nes_color in speed_colors.items()}
        for level_name, speed_colors in slot_data["level_to_checkerboard_colors"].items()
    }

    slot_data_processed["selected_splash_checkerboard_color"] = DrMarioNesColors(slot_data["selected_splash_checkerboard_color"])

    return slot_data_processed

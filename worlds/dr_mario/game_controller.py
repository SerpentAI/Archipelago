from typing import Dict, List, Optional, Set, Tuple

import collections
import logging
import random
import time

from .data.game_data import level_to_vanilla_virus_count, level_to_virus_rows
from .data_funcs import items_with_tag

from .enums import (
    DrMarioColors,
    DrMarioFinalLevelSpeedOptions,
    DrMarioGoalOptions,
    DrMarioInputEffects,
    DrMarioLevels,
    DrMarioModes,
    DrMarioMusicTracks,
    DrMarioMusicTypes,
    DrMarioNesColors,
    DrMarioPaletteRegions,
    DrMarioSpeeds,
    DrMarioSpeedUpBehaviorOptions,
    DrMarioTags,
    DrMarioTrapTypes,
)

from .game_state_manager import GameStateManager, GameState


class GameController:
    logger: Optional[logging.Logger]

    game_state_manager: GameStateManager

    received_items: Dict[str, int]
    completed_locations: Set[str]

    completed_locations_queue: collections.deque
    received_items_queue: collections.deque

    goal_completed: bool

    logged_errors: Set[str]

    # Game State
    game_state: Optional[GameState]

    # Generation Options
    option_goal: Optional[DrMarioGoalOptions]
    option_antiviral_serum_total: Optional[int]
    option_antiviral_serum_required: Optional[int]
    option_final_level: Optional[int]
    option_final_level_speed: Optional[DrMarioFinalLevelSpeedOptions]
    option_progressive_level_unlocks: Optional[bool]
    option_starting_match_length: Optional[int]
    option_starting_garbage_levels: Optional[int]
    option_restrict_rotations: Optional[bool]
    option_lock_next_pill_preview: Optional[bool]
    option_speed_up_behavior: Optional[DrMarioSpeedUpBehaviorOptions]
    option_trap_percentage: Optional[int]
    option_trap_weights: Optional[Dict[DrMarioTrapTypes, int]]
    option_trap_duration: Optional[int]
    option_randomize_music: Optional[bool]
    option_lock_music_choices: Optional[bool]
    option_randomize_mario_color: Optional[bool]
    option_randomize_virus_colors: Optional[bool]
    option_randomize_checkerboard_colors: Optional[bool]
    option_death_link: Optional[bool]

    # Generation Data
    selected_levels: Optional[List[DrMarioLevels]]
    selected_starting_levels: Optional[List[DrMarioLevels]]
    selected_final_level: Optional[DrMarioLevels]
    level_to_starting_pill: Optional[Dict[DrMarioLevels, str]]
    level_to_starting_rotation: Optional[Dict[DrMarioLevels, str]]
    level_to_starting_garbage_levels: Optional[Dict[DrMarioLevels, int]]
    level_to_virus_count_delta: Optional[Dict[DrMarioLevels, int]]
    selected_music_tracks: Optional[Dict[DrMarioMusicTracks, DrMarioMusicTracks]]
    selected_mario_color: Optional[DrMarioNesColors]
    selected_virus_colors: Optional[Dict[DrMarioColors, DrMarioNesColors]]
    level_to_checkerboard_colors: Optional[Dict[DrMarioLevels, Dict[DrMarioSpeeds, DrMarioNesColors]]]
    selected_splash_checkerboard_color: Optional[DrMarioNesColors]

    # State
    is_return_to_splash_pending: bool
    is_return_to_splash_requested: bool

    tracked_level: Optional[DrMarioLevels]
    previous_is_before_first_pill: bool
    previous_viruses_remaining: Optional[int]
    level_viruses_destroyed: int
    previous_virus_counts: Optional[Dict[DrMarioColors, int]]
    level_color_viruses_destroyed: Dict[DrMarioColors, int]
    is_virus_baseline_stale: bool
    is_starting_garbage_dropped: bool
    mutated_colors: Set[DrMarioColors]
    owned_pill_colors: List[DrMarioColors]
    pre_mutation_colors: Set[DrMarioColors]
    has_board_edit_this_tick: bool

    pending_death_link: Tuple[bool, Optional[str], Optional[str]]
    outgoing_death_link: Tuple[bool, Optional[str]]
    pause_death_monitoring: bool

    toasts_pending: collections.deque
    locations_in_logic: Optional[List[str]]
    previous_options_level: Optional[int]

    should_prepare_processed_filler_counters: bool
    processed_filler_counters: Dict[str, int]

    should_prepare_processed_trap_counters: bool
    processed_trap_counters: Dict[DrMarioTrapTypes, int]
    active_trap_timestamps: Dict[DrMarioTrapTypes, Optional[int]]

    def __init__(self, logger: logging.Logger = None) -> None:
        self.logger = logger

        self.game_state_manager = GameStateManager()

        self.received_items = dict()
        self.completed_locations = set()

        self.completed_locations_queue = collections.deque()
        self.received_items_queue = collections.deque()

        self.goal_completed = False

        self.logged_errors = set()

        self.game_state = None

        self.option_goal = None
        self.option_antiviral_serum_total = None
        self.option_antiviral_serum_required = None
        self.option_final_level = None
        self.option_final_level_speed = None
        self.option_progressive_level_unlocks = None
        self.option_starting_match_length = None
        self.option_starting_garbage_levels = None
        self.option_restrict_rotations = None
        self.option_lock_next_pill_preview = None
        self.option_speed_up_behavior = None
        self.option_trap_percentage = None
        self.option_trap_weights = None
        self.option_trap_duration = None
        self.option_randomize_music = None
        self.option_lock_music_choices = None
        self.option_randomize_mario_color = None
        self.option_randomize_virus_colors = None
        self.option_randomize_checkerboard_colors = None
        self.option_death_link = None

        self.selected_levels = None
        self.selected_starting_levels = None
        self.selected_final_level = None
        self.level_to_starting_pill = None
        self.level_to_starting_rotation = None
        self.level_to_starting_garbage_levels = None
        self.level_to_virus_count_delta = None
        self.selected_music_tracks = None
        self.selected_mario_color = None
        self.selected_virus_colors = None
        self.level_to_checkerboard_colors = None
        self.selected_splash_checkerboard_color = None

        self.is_return_to_splash_pending = True
        self.is_return_to_splash_requested = False

        self.tracked_level = None
        self.previous_is_before_first_pill = False
        self.previous_viruses_remaining = None
        self.level_viruses_destroyed = 0
        self.previous_virus_counts = None
        self.level_color_viruses_destroyed = {color: 0 for color in DrMarioColors}
        self.is_virus_baseline_stale = False
        self.is_starting_garbage_dropped = False
        self.mutated_colors = set()
        self.pre_mutation_colors = set()
        self.owned_pill_colors = list()
        self.has_board_edit_this_tick = False

        self.pending_death_link = (False, None, None)
        self.outgoing_death_link = (False, None)
        self.pause_death_monitoring = False

        self.toasts_pending = collections.deque(maxlen=20)
        self.locations_in_logic = None
        self.previous_options_level = None

        self.should_prepare_processed_filler_counters = True

        self.processed_filler_counters = {
            filler_item_name: 0 for filler_item_name in items_with_tag(DrMarioTags.FILLER_ITEM)
        }

        self.should_prepare_processed_trap_counters = True

        self.processed_trap_counters = {
            DrMarioTrapTypes.CONTAGION: 0,
            DrMarioTrapTypes.GARBAGE: 0,
            DrMarioTrapTypes.GRAYSCALE: 0,
            DrMarioTrapTypes.MUTATION: 0,
            DrMarioTrapTypes.REVERSE_CONTROL: 0,
            DrMarioTrapTypes.SMILEY: 0,
        }

        self.active_trap_timestamps = {
            DrMarioTrapTypes.CONTAGION: None,
            DrMarioTrapTypes.GARBAGE: None,
            DrMarioTrapTypes.GRAYSCALE: None,
            DrMarioTrapTypes.MUTATION: None,
            DrMarioTrapTypes.REVERSE_CONTROL: None,
            DrMarioTrapTypes.SMILEY: None,
        }

    def log(self, message) -> None:
        if self.logger:
            self.logger.info(message)

    def log_debug(self, message) -> None:
        if self.logger:
            self.logger.debug(message)

    def open_process_handle(self) -> bool:
        if self.game_state_manager.open_process_handle():
            self.is_return_to_splash_pending = True
            self.is_return_to_splash_requested = False

            return True

        return False

    def close_process_handle(self) -> bool:
        return self.game_state_manager.close_process_handle()

    def is_process_running(self) -> bool:
        if self.game_state_manager.is_process_still_running():
            return True

        self.game_state = None

        return False

    def update(self) -> None:
        if self.game_state_manager.is_process_still_running():
            try:
                self._refresh_game_state()

                if self.game_state is None or not self.game_state.is_valid:
                    return

                if self.option_goal is None:
                    return

                if self.game_state.is_in_demo or self.is_return_to_splash_pending:
                    self._return_to_splash()
                    return

                self.has_board_edit_this_tick = False

                self._track_level()

                self._apply_permanent_game_state()
                self._apply_conditional_game_state()

                self._check_for_completed_locations()
                self._process_received_items()

                if (self.option_trap_percentage or 0) > 0:
                    self._manage_traps()

                self._manage_filler()

                if self.option_death_link:
                    self._handle_death_link()

                self._check_for_victory()

                self._announce_level_logic()
                self._show_toasts()

                self.game_state_manager.end_tick()
            except Exception:
                import traceback

                error: str = traceback.format_exc()

                if error not in self.logged_errors:
                    self.logged_errors.add(error)

                    with open("dr_mario_errors.log", "a") as f:
                        f.write(error + "\n\n")

    def reset(self) -> None:
        self.received_items = dict()
        self.completed_locations = set()

        self.completed_locations_queue = collections.deque()
        self.received_items_queue = collections.deque()

        self.goal_completed = False

        self.logged_errors = set()

        self.game_state = None

        self.option_goal = None
        self.option_antiviral_serum_total = None
        self.option_antiviral_serum_required = None
        self.option_final_level = None
        self.option_final_level_speed = None
        self.option_progressive_level_unlocks = None
        self.option_starting_match_length = None
        self.option_starting_garbage_levels = None
        self.option_restrict_rotations = None
        self.option_lock_next_pill_preview = None
        self.option_speed_up_behavior = None
        self.option_trap_percentage = None
        self.option_trap_weights = None
        self.option_trap_duration = None
        self.option_randomize_music = None
        self.option_lock_music_choices = None
        self.option_randomize_mario_color = None
        self.option_randomize_virus_colors = None
        self.option_randomize_checkerboard_colors = None
        self.option_death_link = None

        self.selected_levels = None
        self.selected_starting_levels = None
        self.selected_final_level = None
        self.level_to_starting_pill = None
        self.level_to_starting_rotation = None
        self.level_to_starting_garbage_levels = None
        self.level_to_virus_count_delta = None
        self.selected_music_tracks = None
        self.selected_mario_color = None
        self.selected_virus_colors = None
        self.level_to_checkerboard_colors = None
        self.selected_splash_checkerboard_color = None

        self.is_return_to_splash_pending = True
        self.is_return_to_splash_requested = False

        self.tracked_level = None
        self.previous_is_before_first_pill = False
        self.previous_viruses_remaining = None
        self.level_viruses_destroyed = 0
        self.previous_virus_counts = None
        self.level_color_viruses_destroyed = {color: 0 for color in DrMarioColors}
        self.is_virus_baseline_stale = False
        self.is_starting_garbage_dropped = False
        self.mutated_colors = set()
        self.pre_mutation_colors = set()
        self.owned_pill_colors = list()
        self.has_board_edit_this_tick = False

        self.pending_death_link = (False, None, None)
        self.outgoing_death_link = (False, None)
        self.pause_death_monitoring = False

        self.toasts_pending = collections.deque(maxlen=20)
        self.locations_in_logic = None
        self.previous_options_level = None

        self.should_prepare_processed_filler_counters = True

        self.processed_filler_counters = {
            filler_item_name: 0 for filler_item_name in items_with_tag(DrMarioTags.FILLER_ITEM)
        }

        self.should_prepare_processed_trap_counters = True

        self.processed_trap_counters = {
            DrMarioTrapTypes.CONTAGION: 0,
            DrMarioTrapTypes.GARBAGE: 0,
            DrMarioTrapTypes.GRAYSCALE: 0,
            DrMarioTrapTypes.MUTATION: 0,
            DrMarioTrapTypes.REVERSE_CONTROL: 0,
            DrMarioTrapTypes.SMILEY: 0,
        }

        self.active_trap_timestamps = {
            DrMarioTrapTypes.CONTAGION: None,
            DrMarioTrapTypes.GARBAGE: None,
            DrMarioTrapTypes.GRAYSCALE: None,
            DrMarioTrapTypes.MUTATION: None,
            DrMarioTrapTypes.REVERSE_CONTROL: None,
            DrMarioTrapTypes.SMILEY: None,
        }

    def _refresh_game_state(self) -> None:
        self.game_state = self.game_state_manager.determine_game_state()

    def _return_to_splash(self) -> None:
        if self.game_state.is_on_splash or (self.game_state.mode == DrMarioModes.OPTIONS and not self.game_state.is_in_demo):
            self.is_return_to_splash_pending = False
            self.is_return_to_splash_requested = False

            return

        if self.game_state.is_in_demo or not self.is_return_to_splash_requested:
            if self.game_state_manager.return_to_splash():
                self.is_return_to_splash_requested = True

    def _track_level(self) -> None:
        if not (self.game_state.mode == DrMarioModes.PLAYING or self.game_state.is_before_first_pill) or self.game_state.level > 20:
            self.previous_is_before_first_pill = False
            return

        level: DrMarioLevels = list(DrMarioLevels)[self.game_state.level]

        is_level_start: bool = bool(self.game_state.is_before_first_pill) and not self.previous_is_before_first_pill
        is_attached_mid_level: bool = self.tracked_level is None and not self.game_state.is_between_levels

        if is_level_start or is_attached_mid_level:
            self.tracked_level = level
            self.previous_viruses_remaining = self.game_state.viruses_remaining
            self.level_viruses_destroyed = 0
            self.previous_virus_counts = dict(self.game_state.virus_counts)
            self.level_color_viruses_destroyed = {color: 0 for color in DrMarioColors}
            self.is_virus_baseline_stale = False
            self.is_starting_garbage_dropped = is_attached_mid_level and not is_level_start
            self.mutated_colors = set()
            self.pre_mutation_colors = set()

        self.previous_is_before_first_pill = bool(self.game_state.is_before_first_pill)

        if self.previous_viruses_remaining is not None and self.game_state.viruses_remaining < self.previous_viruses_remaining:
            self.level_viruses_destroyed += self.previous_viruses_remaining - self.game_state.viruses_remaining

        self.previous_viruses_remaining = self.game_state.viruses_remaining

        if self.previous_virus_counts is not None and not self.is_virus_baseline_stale:
            color: DrMarioColors
            for color in DrMarioColors:
                if self.game_state.virus_counts[color] < self.previous_virus_counts[color]:
                    self.level_color_viruses_destroyed[color] += self.previous_virus_counts[color] - self.game_state.virus_counts[color]

        self.previous_virus_counts = dict(self.game_state.virus_counts)
        self.is_virus_baseline_stale = False

    def _apply_permanent_game_state(self) -> None:
        self.game_state_manager.apply_base_patches()

        levels: List[DrMarioLevels] = list(DrMarioLevels)

        unlocked_levels: List[DrMarioLevels]

        if self.option_progressive_level_unlocks:
            progressive_level_unlocks: int = self.received_items.get("Progressive Level Unlock", 0)
            unlocked_levels = [level for level in self.selected_levels if levels.index(level) <= progressive_level_unlocks + 2]
        else:
            unlocked_levels = [level for level in self.selected_levels if self.received_items.get(f"Level Unlock: {level.value}", 0) > 0]

        if self.option_goal == DrMarioGoalOptions.ANTIVIRAL_SERUM_FINAL_LEVEL:
            if self.received_items.get("Antiviral Serum", 0) >= self.option_antiviral_serum_required:
                unlocked_levels.append(self.selected_final_level)

        self.game_state_manager.set_unlocked_levels([levels.index(level) for level in unlocked_levels])

        progressive_speed_unlocks: int = self.received_items.get("Progressive Speed Unlock", 0)
        unlocked_speeds: List[DrMarioSpeeds] = [DrMarioSpeeds.LOW]

        if progressive_speed_unlocks >= 1:
            unlocked_speeds.append(DrMarioSpeeds.MEDIUM)

        if progressive_speed_unlocks >= 2:
            unlocked_speeds.append(DrMarioSpeeds.HIGH)

        self.game_state_manager.set_unlocked_speeds(unlocked_speeds)

        unlocked_music_types: List[DrMarioMusicTypes] = [DrMarioMusicTypes.OFF]

        if self.received_items.get("Music Unlock: Fever", 0) > 0:
            unlocked_music_types.append(DrMarioMusicTypes.FEVER)

        if self.received_items.get("Music Unlock: Chill", 0) > 0:
            unlocked_music_types.append(DrMarioMusicTypes.CHILL)

        self.game_state_manager.set_unlocked_music_types(unlocked_music_types)

        if self.game_state.mode == DrMarioModes.OPTIONS and len(unlocked_levels):
            level: int = self.game_state.level

            if self.game_state.level > 20 or levels[self.game_state.level] not in unlocked_levels:
                lower_levels: List[int] = [levels.index(unlocked_level) for unlocked_level in unlocked_levels if levels.index(unlocked_level) <= self.game_state.level]
                level = max(lower_levels) if len(lower_levels) else min(levels.index(unlocked_level) for unlocked_level in unlocked_levels)

            speed: DrMarioSpeeds = self.game_state.speed if self.game_state.speed in unlocked_speeds else DrMarioSpeeds.LOW
            music_type: DrMarioMusicTypes = self.game_state.music_type if self.game_state.music_type in unlocked_music_types else DrMarioMusicTypes.OFF

            self.game_state_manager.set_options(level, speed, music_type)

        self.game_state_manager.set_level_virus_counts({
            levels.index(level): level_to_vanilla_virus_count[level] + delta for level, delta in self.level_to_virus_count_delta.items()
        })

        self.game_state_manager.set_level_virus_rows({
            levels.index(level): row_count for level, row_count in level_to_virus_rows.items()
        })

        self.game_state_manager.set_match_length(max(3, 7 - self.received_items.get("Progressive Match Length Reduction", 0)))

        if self.option_speed_up_behavior == DrMarioSpeedUpBehaviorOptions.DISABLED:
            self.game_state_manager.set_speed_up_cap(0)
        else:
            self.game_state_manager.set_speed_up_cap(0x31)

        self.game_state_manager.set_music_tracks(self.selected_music_tracks)
        self.game_state_manager.set_mario_color(self.selected_mario_color)
        self.game_state_manager.set_virus_colors(self.selected_virus_colors)

        self.game_state_manager.set_background_colors({
            DrMarioPaletteRegions.SPLASH_CHECKERBOARD: self.selected_splash_checkerboard_color,
        })

        if self.game_state.level <= 20 and not self.game_state.is_between_levels:
            self.game_state_manager.set_next_pill_visible(self.received_items.get(f"{levels[self.game_state.level].value}: Next Pill Preview", 0) > 0)

            checkerboard_colors: Dict[DrMarioSpeeds, DrMarioNesColors] = self.level_to_checkerboard_colors[levels[self.game_state.level]]

            self.game_state_manager.set_background_colors({
                DrMarioPaletteRegions.CHECKERBOARD_HIGH: checkerboard_colors[DrMarioSpeeds.HIGH],
                DrMarioPaletteRegions.CHECKERBOARD_LOW: checkerboard_colors[DrMarioSpeeds.LOW],
                DrMarioPaletteRegions.CHECKERBOARD_MEDIUM: checkerboard_colors[DrMarioSpeeds.MEDIUM],
            })

    def _apply_conditional_game_state(self) -> None:
        if self.game_state.mode not in (DrMarioModes.PLAYING, DrMarioModes.VIRUS_PLACEMENT) or self.game_state.is_between_levels or self.game_state.level > 20:
            self.game_state_manager.set_input_effects(list())
            return

        level_name: str = list(DrMarioLevels)[self.game_state.level].value

        pill_types: List[Tuple[DrMarioColors, DrMarioColors]] = list()

        item_name: str
        item_count: int
        for item_name, item_count in self.received_items.items():
            if item_name.startswith(f"{level_name}: ") and item_name.endswith(" Pill") and item_count > 0:
                left_color: str
                right_color: str
                left_color, right_color = item_name[len(level_name) + 2:-len(" Pill")].split("-")

                pill_types.append((DrMarioColors(left_color), DrMarioColors(right_color)))

        self.game_state_manager.set_pill_types(pill_types)

        self.owned_pill_colors = [color for color in DrMarioColors if any(color in pill_type for pill_type in pill_types)]

        input_effects: List[DrMarioInputEffects] = list()

        if self.received_items.get(f"{level_name}: Clockwise Rotation", 0) < 1:
            input_effects.append(DrMarioInputEffects.CLOCKWISE_ROTATION_DISABLED)

        if self.received_items.get(f"{level_name}: Counterclockwise Rotation", 0) < 1:
            input_effects.append(DrMarioInputEffects.COUNTERCLOCKWISE_ROTATION_DISABLED)

        if self.active_trap_timestamps[DrMarioTrapTypes.REVERSE_CONTROL] is not None:
            input_effects.append(DrMarioInputEffects.REVERSED_CONTROLS)

        self.game_state_manager.set_input_effects(input_effects)

        match_length: int = max(3, 7 - self.received_items.get("Progressive Match Length Reduction", 0))
        garbage_levels: int = max(0, 3 - self.received_items.get(f"{level_name}: Progressive Starting Garbage Reduction", 0))

        self.game_state_manager.set_hud_text([
            "MGNPAB",
            "".join([
                str(match_length),
                str(garbage_levels),
                "Y" if self.received_items.get(f"{level_name}: Next Pill Preview", 0) > 0 else "N",
                str(len(pill_types)),
                "Y" if self.received_items.get(f"{level_name}: Clockwise Rotation", 0) > 0 else "N",
                "Y" if self.received_items.get(f"{level_name}: Counterclockwise Rotation", 0) > 0 else "N",
            ]),
        ])

        if self.game_state.is_before_first_pill and not self.is_starting_garbage_dropped:
            if garbage_levels == 0 or self.game_state_manager.add_random_garbage(garbage_levels, self.owned_pill_colors):
                self.is_starting_garbage_dropped = True

    def _check_for_completed_locations(self) -> None:
        if self.game_state.mode != DrMarioModes.PLAYING or self.tracked_level is None:
            return

        if self.tracked_level not in self.selected_levels:
            return

        level: DrMarioLevels = self.tracked_level
        level_name: str = level.value
        level_index: int = list(DrMarioLevels).index(level)

        starting_virus_count: int = level_to_vanilla_virus_count[level] + self.level_to_virus_count_delta[level]

        color: DrMarioColors
        for color in self.pre_mutation_colors:
            if self.game_state.virus_counts[color] == 0:
                self.mutated_colors.add(color)

        self.pre_mutation_colors = set()

        checked_locations: List[str] = list()

        if self.level_viruses_destroyed >= starting_virus_count // 4:
            checked_locations.append(f"{level_name} - Eliminate a Quarter of the Viruses")

        if self.level_viruses_destroyed >= starting_virus_count // 2:
            checked_locations.append(f"{level_name} - Eliminate Half of the Viruses")

        color: DrMarioColors
        for color in DrMarioColors:
            if self.game_state.virus_counts[color] == 0 and color not in self.mutated_colors:
                checked_locations.append(f"{level_name} - Eliminate All {color.value} Viruses")

            if self.level_color_viruses_destroyed[color] >= 1:
                checked_locations.append(f"{level_name} - Eliminate 1 {color.value} Virus")

            if level_index >= 1 and self.level_color_viruses_destroyed[color] >= 2:
                checked_locations.append(f"{level_name} - Eliminate 2 {color.value} Viruses")

            if level_index >= 3 and self.level_color_viruses_destroyed[color] >= 3:
                checked_locations.append(f"{level_name} - Eliminate 3 {color.value} Viruses")

        if self.game_state.is_between_levels:
            speed_to_index: Dict[DrMarioSpeeds, int] = {DrMarioSpeeds.LOW: 0, DrMarioSpeeds.MEDIUM: 1, DrMarioSpeeds.HIGH: 2}

            speed: DrMarioSpeeds
            speed_index: int
            for speed, speed_index in speed_to_index.items():
                if speed_index <= speed_to_index[self.game_state.speed] and speed_index <= self.option_final_level_speed.value:
                    checked_locations.append(f"{level_name} - Clear the Level on {speed.value} Speed")

        if self.game_state.pills_used >= 2:
            if level_index >= 6 and self.game_state.last_pill_viruses_destroyed >= 2:
                checked_locations.append(f"{level_name} - Destroy 2 Viruses with One Pill")

            if level_index >= 12 and self.game_state.last_pill_viruses_destroyed >= 3:
                checked_locations.append(f"{level_name} - Destroy 3 Viruses with One Pill")

            if self.game_state.last_pill_lines_cleared >= 2:
                checked_locations.append(f"{level_name} - Clear 2 Lines with One Pill")

            if level_index >= 8 and self.game_state.last_pill_lines_cleared >= 3:
                checked_locations.append(f"{level_name} - Clear 3 Lines with One Pill")

            if level_index >= 6:
                color: DrMarioColors
                for color in DrMarioColors:
                    if self.game_state.last_pill_line_colors.count(color) >= 2:
                        checked_locations.append(f"{level_name} - Clear 2 {color.value} Lines with One Pill")

            if level_index >= 4 and self.game_state.last_pill_chains >= 2:
                checked_locations.append(f"{level_name} - Trigger a 2-Chain")

        location: str
        for location in checked_locations:
            if location not in self.completed_locations and location not in self.completed_locations_queue:
                self.completed_locations.add(location)
                self.completed_locations_queue.append(location)

    def _process_received_items(self) -> None:
        while len(self.received_items_queue) > 0:
            item: str = self.received_items_queue.popleft()

            if item not in self.received_items:
                self.received_items[item] = 0

            self.received_items[item] += 1

        if self.should_prepare_processed_filler_counters:
            self.should_prepare_processed_filler_counters = False

            item: str
            item_count: int
            for item, item_count in self.received_items.items():
                if item in self.processed_filler_counters:
                    self.processed_filler_counters[item] = item_count

        if self.should_prepare_processed_trap_counters:
            self.should_prepare_processed_trap_counters = False

            item: str
            item_count: int
            for item, item_count in self.received_items.items():
                if item.endswith(" Trap"):
                    self.processed_trap_counters[DrMarioTrapTypes(item)] = item_count

    def _manage_filler(self) -> None:
        if self.game_state.mode != DrMarioModes.PLAYING or self.game_state.is_paused or self.game_state.is_between_levels:
            return

        if self.game_state.is_topped_out or not self.game_state.is_pill_falling or self.game_state.pills_used < 2:
            return

        self.processed_filler_counters["Placebo"] = self.received_items.get("Placebo", 0)

        if self.has_board_edit_this_tick:
            return

        if self.received_items.get("Virus Buster", 0) > self.processed_filler_counters["Virus Buster"]:
            if self.game_state.viruses_remaining > 1 and self.game_state_manager.remove_random_viruses(1):
                self.processed_filler_counters["Virus Buster"] += 1
                self.has_board_edit_this_tick = True

                return

        if self.received_items.get("Garbage Cleanup", 0) > self.processed_filler_counters["Garbage Cleanup"]:
            if self.game_state_manager.clear_garbage(4):
                self.processed_filler_counters["Garbage Cleanup"] += 1
                self.has_board_edit_this_tick = True

    def _manage_traps(self) -> None:
        now_timestamp: int = int(time.time())

        trap_type: DrMarioTrapTypes
        expiry_timestamp: Optional[int]
        for trap_type, expiry_timestamp in self.active_trap_timestamps.items():
            if expiry_timestamp is not None and now_timestamp >= expiry_timestamp:
                if trap_type == DrMarioTrapTypes.GRAYSCALE:
                    self.game_state_manager.set_color_blind(False)

                self.active_trap_timestamps[trap_type] = None

        if self.active_trap_timestamps[DrMarioTrapTypes.GRAYSCALE] is not None:
            self.game_state_manager.set_color_blind(True)

        if self.game_state.mode != DrMarioModes.PLAYING or self.game_state.is_paused or self.game_state.is_between_levels:
            return

        if self.game_state.is_topped_out or not self.game_state.is_pill_falling or self.game_state.pills_used < 2:
            return

        item: str
        item_count: int
        for item, item_count in self.received_items.items():
            if not item.endswith(" Trap"):
                continue

            trap_type = DrMarioTrapTypes(item)

            if item_count <= self.processed_trap_counters[trap_type]:
                continue

            if trap_type == DrMarioTrapTypes.CONTAGION:
                if self.has_board_edit_this_tick:
                    continue

                if self.game_state_manager.add_random_viruses(4, list(DrMarioColors)):
                    self.processed_trap_counters[trap_type] += 1
                    self.has_board_edit_this_tick = True
            elif trap_type == DrMarioTrapTypes.GARBAGE:
                colors: List[DrMarioColors] = [random.choice(list(DrMarioColors)) for _ in range(4)]

                if self.game_state_manager.drop_garbage(colors):
                    self.processed_trap_counters[trap_type] += 1
            elif trap_type == DrMarioTrapTypes.GRAYSCALE:
                if self.active_trap_timestamps[trap_type] is not None:
                    continue

                if self.game_state_manager.set_color_blind(True):
                    self.active_trap_timestamps[trap_type] = now_timestamp + self.option_trap_duration
                    self.processed_trap_counters[trap_type] += 1
            elif trap_type == DrMarioTrapTypes.MUTATION:
                if self.has_board_edit_this_tick:
                    continue

                if self.game_state_manager.scramble_viruses(list(DrMarioColors)):
                    self.pre_mutation_colors = {color for color in DrMarioColors if self.game_state.virus_counts[color] > 0}
                    self.is_virus_baseline_stale = True
                    self.processed_trap_counters[trap_type] += 1
                    self.has_board_edit_this_tick = True
            elif trap_type == DrMarioTrapTypes.REVERSE_CONTROL:
                if self.active_trap_timestamps[trap_type] is not None:
                    continue

                self.active_trap_timestamps[trap_type] = now_timestamp + self.option_trap_duration
                self.processed_trap_counters[trap_type] += 1
            elif trap_type == DrMarioTrapTypes.SMILEY:
                if self.has_board_edit_this_tick:
                    continue

                if self.game_state_manager.add_filled_smiley_viruses(list(DrMarioColors)):
                    self.processed_trap_counters[trap_type] += 1
                    self.has_board_edit_this_tick = True

    def _handle_death_link(self) -> None:
        if self.game_state.mode not in (DrMarioModes.PLAYING, DrMarioModes.ROUND_END, DrMarioModes.GAME_OVER):
            return

        is_dead: bool = bool(self.game_state.is_topped_out)

        if self.pause_death_monitoring and not is_dead:
            self.pause_death_monitoring = False

        if not is_dead and self.pending_death_link[0] and self.game_state.is_pill_falling:
            if self.game_state_manager.kill_player():
                if self.pending_death_link[2]:
                    self.show_toast(f"Death Link: {self.pending_death_link[2]}")
                else:
                    self.show_toast(f"Death Link: Triggered by {self.pending_death_link[1]}")

                self.pending_death_link = (False, None, None)
                self.pause_death_monitoring = True

        if not self.pause_death_monitoring and is_dead:
            self.outgoing_death_link = (True, "PLAYER topped out")
            self.pause_death_monitoring = True

    def _check_for_victory(self) -> None:
        if self.received_items.get("Antiviral Serum", 0) < self.option_antiviral_serum_required:
            return

        if self.option_goal == DrMarioGoalOptions.ANTIVIRAL_SERUM_HUNT:
            self.goal_completed = True
        elif self.option_goal == DrMarioGoalOptions.ANTIVIRAL_SERUM_FINAL_LEVEL:
            if self.game_state.mode == DrMarioModes.PLAYING and self.game_state.is_between_levels:
                if self.tracked_level == self.selected_final_level:
                    speed_to_index: Dict[DrMarioSpeeds, int] = {DrMarioSpeeds.LOW: 0, DrMarioSpeeds.MEDIUM: 1, DrMarioSpeeds.HIGH: 2}

                    if speed_to_index[self.game_state.speed] >= self.option_final_level_speed.value:
                        self.goal_completed = True

    def _announce_level_logic(self) -> None:
        if self.game_state.mode != DrMarioModes.OPTIONS or self.game_state.level > 20:
            self.previous_options_level = None
            return

        if self.game_state.level == self.previous_options_level:
            return

        self.previous_options_level = self.game_state.level

        if self.locations_in_logic is None:
            return

        level: DrMarioLevels = list(DrMarioLevels)[self.game_state.level]

        location_count: int = sum(
            1 for location in self.locations_in_logic
            if location.startswith(f"{level.value} - ") and location not in self.completed_locations
        )

        self.show_toast(f"{level.value}: {location_count} in logic")

    def _show_toasts(self) -> None:
        if not len(self.toasts_pending):
            return

        message: str
        is_item_received: bool
        message, is_item_received = self.toasts_pending[0]

        if self.game_state_manager.display_message(message):
            self.toasts_pending.popleft()

            if is_item_received:
                self.game_state_manager.play_item_received_sound()

    def show_toast(self, message: str, is_item_received: bool = False) -> None:
        self.toasts_pending.append((message, is_item_received))

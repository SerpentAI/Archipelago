import logging

from typing import Any, ClassVar, Dict, List, TextIO, Tuple

from BaseClasses import Item, ItemClassification, Location, Region, Tutorial

from worlds.AutoWorld import WebWorld, World

from .data.item_data import TromboneChampItemData, item_data
from .data.location_data import TromboneChampLocationData, location_data
from .data.song_data import song_data

from .data_funcs import (
    item_names_to_id,
    location_names_to_id,
    id_to_goals,
    id_to_goal_songs,
    item_groups,
    location_groups,
    location_access_rule_for,
    location_goal_access_rule_for,
)

from .enums import (
    TromboneChampGoals,
    TromboneChampGoalSongs,
    TromboneChampItems,
    TromboneChampNotes,
    TromboneChampSongs,
    TromboneChampTrombonerCards,
    TromboneChampTromboners,
)

from .options import TromboneChampOptions, option_groups

from .song_funcs import notes_required_for_starting_songs


class TromboneChampItem(Item):
    game = "Trombone Champ"


class TromboneChampLocation(Location):
    game = "Trombone Champ"


class TromboneChampWebWorld(WebWorld):
    theme: str = "partyTime"

    tutorials: List[Tutorial] = [
        Tutorial(
            "Multiworld Setup Guide",
            "A guide to setting up the Trombone Champ randomizer connected to an Archipelago Multiworld",
            "English",
            "setup_en.md",
            "setup/en",
            ["Serpent.AI"],
        )
    ]

    option_groups = option_groups


class TromboneChampWorld(World):
    """
    Honk, blow, & toot your way through over 70 songs, collect all 50 unique Tromboner Cards, and uncover the mysteries
    of the Trombiverse. Do you have what it takes to become the true Trombone Champ?
    """

    options_dataclass = TromboneChampOptions
    options: TromboneChampOptions

    game = "Trombone Champ"

    item_name_to_id = item_names_to_id()
    location_name_to_id = location_names_to_id()

    item_name_groups = item_groups()
    location_name_groups = location_groups()

    required_client_version: Tuple[int, int, int] = (0, 6, 3)

    web = TromboneChampWebWorld()

    filler_item_names: List[str] = item_groups()["Filler"]

    # Options
    a_rank_maximum_difficulty: int
    card_sack_cost: int
    cardsanity: bool
    craftsanity: bool
    engoldenated_turding_reward: int
    engoldenatesanity: bool
    goal: TromboneChampGoals
    goal_song: TromboneChampGoalSongs
    golden_baboons_required: int
    golden_baboons_total: int
    include_a_ranks: bool
    include_s_ranks: bool
    include_turbo_mode: bool
    rank_threshold_percentage: int
    s_rank_maximum_difficulty: int
    shuffle_music_notes: bool
    song_count: int
    starting_song_count: int
    starting_tromboner_count: int
    toots_percentage: int
    tromboner_count: int
    turd_crafting_cost: int
    turding_average_reward: int
    turdsanity: bool

    # Generation
    selected_goal_song: TromboneChampSongs
    selected_goal_song_tromboner: TromboneChampTromboners
    selected_songs: List[TromboneChampSongs]
    selected_starting_songs: List[Tuple[TromboneChampTromboners, TromboneChampSongs]]
    selected_tromboners: List[TromboneChampTromboners]

    # Universal Tracker
    ut_can_gen_without_yaml: bool = True

    tracker_world: ClassVar = {
        "map_page_folder": "ut",
        "map_page_maps": "maps/maps.json",
        "map_page_locations": "locations/locations.json",
    }

    @property
    def is_universal_tracker(self) -> bool:
        return hasattr(self.multiworld, "re_gen_passthrough")

    def generate_early(self) -> None:
        self.goal = id_to_goals()[self.options.goal.value]
        self.goal_song = id_to_goal_songs()[self.options.goal_song.value]

        self.tromboner_count = self.options.tromboner_count.value

        self.selected_tromboners = self.random.sample(list(TromboneChampTromboners), self.tromboner_count)

        self.song_count = self.options.song_count.value
        self.selected_songs = list()

        song_list: List[TromboneChampSongs] = list(TromboneChampSongs)

        if self.goal_song == TromboneChampGoalSongs.TROMBONE_CHAMP_MEDLEY:
            song_list.remove(TromboneChampSongs.TROMBONE_CHAMP_MEDLEY)

            self.selected_songs.append(TromboneChampSongs.TROMBONE_CHAMP_MEDLEY)
            self.selected_songs += self.random.sample(song_list, self.song_count - 1)

            self.selected_goal_song = TromboneChampSongs.TROMBONE_CHAMP_MEDLEY
        elif self.goal_song == TromboneChampGoalSongs.ANY:
            self.selected_songs += self.random.sample(song_list, self.song_count)
            self.selected_goal_song = self.random.choice(self.selected_songs)

        self.selected_goal_song_tromboner = self.random.choice(self.selected_tromboners)

        self.golden_baboons_required = self.options.golden_baboons_required.value
        self.golden_baboons_total = self.options.golden_baboons_total.value

        if self.golden_baboons_required > self.golden_baboons_total:
            self.golden_baboons_total = self.golden_baboons_required

            logging.warning(
                f"Trombone Champ: {self.player_name} has more required golden baboons than total golden baboons. "
                "Using required golden baboons as total golden baboons..."
            )

        self.starting_song_count = self.options.starting_song_count.value
        self.selected_starting_songs = list()

        while len(self.selected_starting_songs) < self.starting_song_count:
            tromboner: TromboneChampTromboners = self.random.choice(self.selected_tromboners)
            song: TromboneChampSongs = self.random.choice(self.selected_songs)

            if song == self.selected_goal_song:
                continue
            elif (tromboner, song) in self.selected_starting_songs:
                continue

            self.selected_starting_songs.append((tromboner, song))

        self.include_a_ranks = bool(self.options.include_a_ranks)
        self.include_s_ranks = bool(self.options.include_s_ranks)

        self.a_rank_maximum_difficulty = self.options.a_rank_maximum_difficulty.value
        self.s_rank_maximum_difficulty = self.options.s_rank_maximum_difficulty.value

        self.rank_threshold_percentage = self.options.rank_threshold_percentage.value

        self.shuffle_music_notes = bool(self.options.shuffle_music_notes)
        self.include_turbo_mode = bool(self.options.include_turbo_mode)

        self.cardsanity = bool(self.options.cardsanity)
        self.craftsanity = bool(self.options.craftsanity)
        self.turdsanity = bool(self.options.turdsanity)
        self.engoldenatesanity = bool(self.options.engoldenatesanity)

        self.toots_percentage = self.options.toots_percentage.value
        self.card_sack_cost = self.options.card_sack_cost.value
        self.turd_crafting_cost = self.options.turd_crafting_cost.value
        self.turding_average_reward = self.options.turding_average_reward.value
        self.engoldenated_turding_reward = self.options.engoldenated_turding_reward.value

        # Universal Tracker Support
        if self.is_universal_tracker:
            self._apply_universal_tracker_passthrough()

    def create_regions(self) -> None:
        region_menu: Region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(region_menu)

        # Tromboners
        tromboner: TromboneChampTromboners
        for tromboner in self.selected_tromboners:
            region_tromboner: Region = Region(f"TROMBONER - {tromboner.value}", self.player, self.multiworld)

            region_menu.connect(region_tromboner)
            region_tromboner.connect(region_menu)

            # Locations
            song: TromboneChampSongs
            for song in self.selected_songs:
                # Goal Song Handling
                if tromboner == self.selected_goal_song_tromboner and song == self.selected_goal_song:
                    location_name: str = f"{tromboner.value} - {song.value} Clear!"
                    data: TromboneChampLocationData = location_data[location_name]

                    location: TromboneChampLocation = TromboneChampLocation(
                        self.player,
                        location_name,
                        data.archipelago_id,
                        region_tromboner,
                    )

                    location.place_locked_item(self.create_item(TromboneChampItems.GOOD_JOB.value))

                    location.access_rule = eval(
                        location_goal_access_rule_for(location_name, self.player, self.golden_baboons_required)
                    )

                    region_tromboner.locations.append(location)

                    # We do not create rank and turbo mode locations for the goal song, for obvious reasons...
                    continue

                # Clears
                location_name: str = f"{tromboner.value} - {song.value} Clear!"
                data: TromboneChampLocationData = location_data[location_name]

                location: TromboneChampLocation = TromboneChampLocation(
                    self.player,
                    location_name,
                    data.archipelago_id,
                    region_tromboner,
                )

                location_access_rule: str = location_access_rule_for(location_name, self.player)

                if location_access_rule != "lambda state: True":
                    location.access_rule = eval(location_access_rule)

                region_tromboner.locations.append(location)

                # Clears (Extra)
                location_name: str = f"{tromboner.value} - {song.value} Clear! (Extra)"
                data: TromboneChampLocationData = location_data[location_name]

                location: TromboneChampLocation = TromboneChampLocation(
                    self.player,
                    location_name,
                    data.archipelago_id,
                    region_tromboner,
                )

                location_access_rule: str = location_access_rule_for(location_name, self.player)

                if location_access_rule != "lambda state: True":
                    location.access_rule = eval(location_access_rule)

                region_tromboner.locations.append(location)

                # C Ranks
                location_name = f"{tromboner.value} - {song.value} C Rank!"
                data = location_data[location_name]

                location = TromboneChampLocation(
                    self.player,
                    location_name,
                    data.archipelago_id,
                    region_tromboner,
                )

                location_access_rule = location_access_rule_for(location_name, self.player)

                if location_access_rule != "lambda state: True":
                    location.access_rule = eval(location_access_rule)

                region_tromboner.locations.append(location)

                # B Ranks
                location_name = f"{tromboner.value} - {song.value} B Rank!"
                data = location_data[location_name]

                location = TromboneChampLocation(
                    self.player,
                    location_name,
                    data.archipelago_id,
                    region_tromboner,
                )

                location_access_rule = location_access_rule_for(location_name, self.player)

                if location_access_rule != "lambda state: True":
                    location.access_rule = eval(location_access_rule)

                region_tromboner.locations.append(location)

                # A Ranks
                if self.include_a_ranks:
                    if song_data[song].difficulty > self.a_rank_maximum_difficulty:
                        continue

                    location_name = f"{tromboner.value} - {song.value} A Rank!"
                    data = location_data[location_name]

                    location = TromboneChampLocation(
                        self.player,
                        location_name,
                        data.archipelago_id,
                        region_tromboner,
                    )

                    location_access_rule = location_access_rule_for(location_name, self.player)

                    if location_access_rule != "lambda state: True":
                        location.access_rule = eval(location_access_rule)

                    region_tromboner.locations.append(location)

                # S Ranks
                if self.include_s_ranks:
                    if song_data[song].difficulty > self.s_rank_maximum_difficulty:
                        continue

                    location_name = f"{tromboner.value} - {song.value} S Rank!"
                    data = location_data[location_name]

                    location = TromboneChampLocation(
                        self.player,
                        location_name,
                        data.archipelago_id,
                        region_tromboner,
                    )

                    location_access_rule = location_access_rule_for(location_name, self.player)

                    if location_access_rule != "lambda state: True":
                        location.access_rule = eval(location_access_rule)

                    region_tromboner.locations.append(location)

                # Turbo Modes
                if self.include_turbo_mode:
                    location_name = f"{tromboner.value} - {song.value} Turbo Mode!"
                    data = location_data[location_name]

                    location = TromboneChampLocation(
                        self.player,
                        location_name,
                        data.archipelago_id,
                        region_tromboner,
                    )

                    location_access_rule = location_access_rule_for(location_name, self.player)

                    if location_access_rule != "lambda state: True":
                        location.access_rule = eval(location_access_rule)

                    region_tromboner.locations.append(location)

            self.multiworld.regions.append(region_tromboner)

        # Card Collection
        if any([self.cardsanity, self.craftsanity, self.turdsanity, self.engoldenatesanity]):
            region_card_collection: Region = Region("Card Collection", self.player, self.multiworld)

            region_menu.connect(region_card_collection)
            region_card_collection.connect(region_menu)

            # Locations
            tromboner_card: TromboneChampTrombonerCards
            for tromboner_card in list(TromboneChampTrombonerCards):
                # Cardsanity
                if self.cardsanity:
                    location_name: str = f"Collect Tromboner Card: {tromboner_card.value}"
                    data: TromboneChampLocationData = location_data[location_name]

                    location: TromboneChampLocation = TromboneChampLocation(
                        self.player,
                        location_name,
                        data.archipelago_id,
                        region_card_collection,
                    )

                    location_access_rule: str = location_access_rule_for(location_name, self.player)

                    if location_access_rule != "lambda state: True":
                        location.access_rule = eval(location_access_rule)

                    region_card_collection.locations.append(location)

                # Craftsanity
                if self.craftsanity:
                    location_name: str = f"Craft Tromboner Card: {tromboner_card.value}"
                    data: TromboneChampLocationData = location_data[location_name]

                    location: TromboneChampLocation = TromboneChampLocation(
                        self.player,
                        location_name,
                        data.archipelago_id,
                        region_card_collection,
                    )

                    location_access_rule: str = location_access_rule_for(location_name, self.player)

                    if location_access_rule != "lambda state: True":
                        location.access_rule = eval(location_access_rule)

                    region_card_collection.locations.append(location)

                # Turdsanity
                if self.turdsanity:
                    location_name: str = f"Turd Tromboner Card: {tromboner_card.value}"
                    data: TromboneChampLocationData = location_data[location_name]

                    location: TromboneChampLocation = TromboneChampLocation(
                        self.player,
                        location_name,
                        data.archipelago_id,
                        region_card_collection,
                    )

                    location_access_rule: str = location_access_rule_for(location_name, self.player)

                    if location_access_rule != "lambda state: True":
                        location.access_rule = eval(location_access_rule)

                    region_card_collection.locations.append(location)

                # Engoldenatesanity
                if self.engoldenatesanity:
                    location_name: str = f"Engoldenate Tromboner Card: {tromboner_card.value}"
                    data: TromboneChampLocationData = location_data[location_name]

                    location: TromboneChampLocation = TromboneChampLocation(
                        self.player,
                        location_name,
                        data.archipelago_id,
                        region_card_collection,
                    )

                    location_access_rule: str = location_access_rule_for(location_name, self.player)

                    if location_access_rule != "lambda state: True":
                        location.access_rule = eval(location_access_rule)

                    region_card_collection.locations.append(location)

            self.multiworld.regions.append(region_card_collection)

    def create_items(self) -> None:
        ## Precollect
        items_to_precollect: List[str] = list()

        # Starting Songs
        tromboner: TromboneChampTromboners
        song: TromboneChampSongs
        for tromboner, song in self.selected_starting_songs:
            items_to_precollect.append(f"SONG - {tromboner.value}: {song.value}")

        # Music Notes
        notes_to_precollect: List[str] = list()

        if self.shuffle_music_notes:
            notes_to_precollect = notes_required_for_starting_songs(self.selected_starting_songs)
        else:
            tromboner: TromboneChampTromboners
            for tromboner in self.selected_tromboners:
                note: TromboneChampNotes
                for note in list(TromboneChampNotes):
                    notes_to_precollect.append(f"MUSIC NOTE - {tromboner.value}: {note.value}")

        items_to_precollect += notes_to_precollect

        ## Item Pool
        item_pool: List[TromboneChampItem] = list()

        # Golden Baboons
        i: int
        for i in range(self.golden_baboons_total):
            item: TromboneChampItem = self.create_item(TromboneChampItems.GOLDEN_BABOON.value)

            if i >= self.golden_baboons_required:
                item.classification = ItemClassification.useful

            item_pool.append(item)

        # Abilities
        if self.craftsanity:
            item_pool.append(self.create_item(TromboneChampItems.TURD_CRAFTING.value))

        if self.craftsanity or self.turdsanity:
            item_pool.append(self.create_item(TromboneChampItems.TURDING.value))

        if self.engoldenatesanity:
            item_pool.append(self.create_item(TromboneChampItems.ENGOLDENATING.value))

        # Tromboners
        tromboner: TromboneChampTromboners
        for tromboner in self.selected_tromboners:
            # Songs
            song: TromboneChampSongs
            for song in self.selected_songs:
                item_name = f"SONG - {tromboner.value}: {song.value}"

                if item_name not in items_to_precollect:
                    item_pool.append(self.create_item(item_name))

            # Music Notes
            if self.shuffle_music_notes:
                note: TromboneChampNotes
                for note in list(TromboneChampNotes):
                    item_name = f"MUSIC NOTE - {tromboner.value}: {note.value}"

                    if item_name not in items_to_precollect:
                        item_pool.append(self.create_item(item_name))

            # Turbo Mode
            if self.include_turbo_mode:
                item_name = f"{TromboneChampItems.TURBO_MODE.value} - {tromboner.value}"

                if item_name not in items_to_precollect:
                    item_pool.append(self.create_item(item_name))

            # License to Toot
            if any([self.cardsanity, self.craftsanity, self.turdsanity, self.engoldenatesanity]):
                item_name = f"{TromboneChampItems.LICENSE_TO_TOOT.value} - {tromboner.value}"

                if item_name not in items_to_precollect:
                    item_pool.append(self.create_item(item_name))

        # Filler
        total_location_count: int = len(self.multiworld.get_unfilled_locations(self.player))
        to_fill_location_count: int = total_location_count - len(item_pool)

        item_pool += [self.create_filler() for _ in range(to_fill_location_count)]

        self.multiworld.itempool += item_pool

        item: str
        for item in items_to_precollect:
            self.multiworld.push_precollected(self.create_item(item))

    def create_item(self, name: str) -> TromboneChampItem:
        data: TromboneChampItemData = item_data[name]

        return TromboneChampItem(
            name,
            data.classification,
            data.archipelago_id,
            self.player,
        )

    def generate_basic(self) -> None:
        self.multiworld.completion_condition[self.player] = lambda state: state.has(
            TromboneChampItems.GOOD_JOB.value, self.player
        )

    def fill_slot_data(self) -> Dict[str, Any]:
        pass

    def write_spoiler_header(self, spoiler_handle: TextIO) -> None:
        spoiler_handle.write(f"\nSelected Tromboners: {', '.join(sorted([t.value for t in self.selected_tromboners]))}")
        spoiler_handle.write(f"\nSelected Songs: {', '.join(sorted([t.value for t in self.selected_songs]))}")

        spoiler_handle.write(f"\nStarting Songs: {', '.join(sorted([t.value + ' - ' + s.value for t, s in self.selected_starting_songs]))}")

        spoiler_handle.write(f"\n\nGoal Song Tromboner: {self.selected_goal_song_tromboner.value}")
        spoiler_handle.write(f"\nGoal Song: {self.selected_goal_song.value}")

    def get_filler_item_name(self) -> str:
        return self.random.choice(self.filler_item_names)

    # Universal Tracker Support
    # ...

    def _apply_universal_tracker_passthrough(self) -> None:
        pass

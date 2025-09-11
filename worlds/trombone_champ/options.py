from typing import List

from dataclasses import dataclass

from Options import (
    Choice,
    OptionGroup,
    PerGameCommonOptions,
    Range,
    StartInventoryPool,
    Toggle,
)


class Goal(Choice):
    """
    Determines the victory condition.

    Golden Baboons Goal Song: Acquire enough golden baboons to unlock and clear the goal song
    """
    display_name: str = "Goal"

    option_golden_baboons_goal_song: int = 0

    default = 0


class GoalSong(Choice):
    """
    Determines the goal song that must be cleared to win.

    Trombone Champ Medley: The goal song is Trombone Champ Medley
    Any: Any song can be selected as the goal song
    """
    display_name: str = "Goal Song"

    option_trombone_champ_medley: int = 0
    option_any: int = 1

    default = 0


class GoldenBaboonsTotal(Range):
    """
    Determines how many golden baboons are in the item pool.
    """
    display_name = "Golden Baboons Total"

    range_start = 3
    range_end = 50

    default = 40


class GoldenBaboonsRequired(Range):
    """
    Determines how many golden baboons are required to unlock the goal song.
    """
    display_name = "Golden Baboons Required"

    range_start = 3
    range_end = 50

    default = 30


class SongCount(Range):
    """
    Determines how many songs to randomly select as having location checks.

    This count includes the starting songs, as well as the goal song.

    Example: With 20 and 3 starting songs, you will have 16 additional songs to unlock that will have location checks.
             20 - 3 (starting) - 1 (goal) = 16
    """
    display_name = "Song Count"

    range_start = 20
    range_end = 71

    default = 50


class StartingSongCount(Range):
    """
    Determines how many songs you will start with.

    Other songs will need to be unlocked by receiving their respective items.
    """
    display_name = "Starting Song Count"

    range_start = 1
    range_end = 10

    default = 3


class IncludeCRanks(Toggle):
    """
    If true, scoring a C Rank or better on a song will unlock a location check.
    """
    display_name: str = "Include C Ranks"


class IncludeBRanks(Toggle):
    """
    If true, scoring a B Rank or better on a song will unlock a location check.
    """
    display_name: str = "Include B Ranks"


class IncludeARanks(Toggle):
    """
    If true, scoring an A Rank or better on a song will unlock a location check.
    """
    display_name: str = "Include A Ranks"


class ARankMaximumDifficulty(Range):
    """
    Determines the maximum allowed difficulty for songs to have an A Rank location check.
    """
    display_name = "A Rank Maximum Difficulty"

    range_start = 1
    range_end = 10

    default = 8


class IncludeSRanks(Toggle):
    """
    If true, scoring an S Rank on a song will unlock a location check.
    """
    display_name: str = "Include S Ranks"


class SRankMaximumDifficulty(Range):
    """
    Determines the maximum allowed difficulty for songs to have an S Rank location check.
    """
    display_name = "S Rank Maximum Difficulty"

    range_start = 1
    range_end = 10

    default = 7


class RankThresholdPercentage(Range):
    """
    Determines the percentage to apply to each song's required rank score.
    """
    display_name = "Rank Threshold Percentage"

    range_start = 50
    range_end = 120

    default = 100


class ShuffleMusicNotes(Toggle):
    """
    If true, the ability to see, and therefore hit each music note will need to be unlocked with an item.

    Turning this on will enable more complex logic if you have any rank location checks enabled.

    C Rank: 50% of the song's total music notes must be playable to be in logic
    B Rank: 70% of the song's total music notes must be playable to be in logic
    A Rank: 85% of the song's total music notes must be playable to be in logic
    S Rank: 95% of the song's total music notes must be playable to be in logic

    You will always be granted a set of starter music notes to ensure you can roughly C Rank each starting song.

    If all rank location checks are disabled, this option will not have any logic implications and is just for fun.
    """
    display_name: str = "Shuffle Music Notes"


class IncludeTurboMode(Toggle):
    """
    If true, clearing a song in Turbo Mode will unlock a location check.

    Turbo Mode will need to be unlocked by receiving the Turbo Mode item.
    """
    display_name: str = "Include Turbo Mode"


class TrombonerCount(Range):
    """
    Determines how many different tromboners will be available to plays as.

    Each song / ability (turbo mode, music notes etc.) will have to be unlocked for each tromboner separately.
    Each song clear, rank clears (if enabled) and turbo mode clear will be counted separately for each tromboner.

    Note: There are no gameplay differences between tromboners.
          Adding more tromboners purely acts as a location check multiplier, allowing you to scale for larger games.
    """
    display_name = "Tromboners Count"

    range_start = 1
    range_end = 10

    default = 1


class StartingTrombonerCount(Range):
    """
    Determines how many tromboners you will start with.

    Other tromboners will need to be unlocked by receiving their respective items.
    """
    display_name = "Starting Tromboners Count"

    range_start = 1
    range_end = 10

    default = 1


class Cardsanity(Toggle):
    """
    If true, collecting each of the 50 tromboner cards will unlock a location check.

    You will not be able to get toots from playing songs until you receive the License to Toot!!! item.
    """
    display_name: str = "Cardsanity"


class Craftsanity(Toggle):
    """
    If true, crafting each of the 50 tromboner cards with turds will unlock a location check.

    You will not be able to craft cards until you receive the Turd Crafting!!! item.

    Craftsanity must be on for this option to have any effect.
    """
    display_name: str = "Craftsanity"


class Turdsanity(Toggle):
    """
    If true, turding each of the 50 tromboner cards will unlock a location check.

    You will not be able to turd cards until you receive the Turding!!! item.

    Craftsanity must be on for this option to have any effect.
    """
    display_name: str = "Turdsanity"


class Engoldenatesanity(Toggle):
    """
    If true, engoldenating each of the 50 tromboner cards will unlock a location check.

    You will not be able to engoldenate cards until you receive the Engoldenating!!! item.

    Craftsanity must be on for this option to have any effect.
    """
    display_name: str = "Engoldenatesanity"


class TootsPercentage(Range):
    """
    Determines the percentage to apply to the number of toots you receive from playing songs.

    Example: After clearing a song, where you would normally receive 1000 toots, you will receive 1250 toots if the
             percentage is set to 125. If the percentage is set to 75, you will receive 750 toots instead.
    """
    display_name = "Toot Percentage"

    range_start = 1
    range_end = 1000

    default = 100


class CardSackCost(Range):
    """
    Determines the cost (in toots) of card sacks. Vanilla: 499

    Only relevant if Cardsanity is enabled.
    """
    display_name = "Card Sack Cost"

    range_start = 1
    range_end = 2499

    default = 499


class TurdCraftingCost(Range):
    """
    Determines the cost (in turds) to craft a card. Vanilla: 399

    Only relevant if Craftsanity is enabled.
    """
    display_name = "Turd Crafting Cost"

    range_start = 1
    range_end = 1999

    default = 399


class TurdingAverageReward(Range):
    """
    Determines the average reward (in turds) for turding a card. Vanilla: 150 (100 to 200)

    Only relevant if Cardsanity is enabled.
    """
    display_name = "Turding Average Reward"

    range_start = 1
    range_end = 749

    default = 150


class EngoldenatedTurdingReward(Range):
    """
    Determines the reward (in turds) for turding an engoldenated card. Vanilla: 375

    Only relevant if Cardsanity is enabled.
    """
    display_name = "Engoldenated Turding Reward"

    range_start = 1
    range_end = 1874

    default = 375


@dataclass
class TromboneChampOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    goal: Goal
    goal_song: GoalSong
    golden_baboons_total: GoldenBaboonsTotal
    golden_baboons_required: GoldenBaboonsRequired
    song_count: SongCount
    starting_song_count: StartingSongCount
    include_c_ranks: IncludeCRanks
    include_b_ranks: IncludeBRanks
    include_a_ranks: IncludeARanks
    a_rank_maximum_difficulty: ARankMaximumDifficulty
    include_s_ranks: IncludeSRanks
    s_rank_maximum_difficulty: SRankMaximumDifficulty
    rank_threshold_percentage: RankThresholdPercentage
    shuffle_music_notes: ShuffleMusicNotes
    include_turbo_mode: IncludeTurboMode
    tromboner_count: TrombonerCount
    starting_tromboner_count: StartingTrombonerCount
    cardsanity: Cardsanity
    craftsanity: Craftsanity
    turdsanity: Turdsanity
    engoldenatesanity: Engoldenatesanity
    toots_percentage: TootsPercentage
    card_sack_cost: CardSackCost
    turd_crafting_cost: TurdCraftingCost
    turding_average_reward: TurdingAverageReward
    engoldenated_turding_reward: EngoldenatedTurdingReward


option_groups: List[OptionGroup] = [
    OptionGroup(
        "Goal Options",
        [
            Goal,
            GoalSong,
            GoldenBaboonsTotal,
            GoldenBaboonsRequired,
        ],
    ),
    OptionGroup(
        "Song Options",
        [
            SongCount,
            StartingSongCount,
            IncludeCRanks,
            IncludeBRanks,
            IncludeARanks,
            ARankMaximumDifficulty,
            IncludeSRanks,
            SRankMaximumDifficulty,
            RankThresholdPercentage,
            ShuffleMusicNotes,
            IncludeTurboMode
        ],
    ),
    OptionGroup(
        "Tromboner Options",
        [
            TrombonerCount,
            StartingTrombonerCount,
        ],
    ),
    OptionGroup(
        "Card Options",
        [
            Cardsanity,
            Craftsanity,
            Turdsanity,
            Engoldenatesanity,
            TootsPercentage,
            CardSackCost,
            TurdCraftingCost,
            TurdingAverageReward,
            EngoldenatedTurdingReward,
        ],
    ),
]

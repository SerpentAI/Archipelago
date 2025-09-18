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

    Golden Baboons Goal Song: Acquire enough golden baboons, unlock and clear the goal song
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
    range_end = 30

    default = 30


class GoldenBaboonsRequired(Range):
    """
    Determines how many golden baboons are required to unlock the goal song.
    """
    display_name = "Golden Baboons Required"

    range_start = 3
    range_end = 30

    default = 24


class SongCount(Range):
    """
    Determines how many songs to randomly select as having location checks.

    This count includes the starting songs, as well as the goal song.

    Example: With 30 and 3 starting songs, you will have 26 additional songs to unlock that will have location checks.
             30 - 3 (starting) - 1 (goal) = 26
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

    range_start = 3
    range_end = 10

    default = 3


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

    Example: If an S rank normally requires 100,000 points...
             At 80%, you will only need 80,000 points to achieve S rank.
             At 100%, you will need the normal 100,000 points to achieve S rank.
             At 120%, you will need 120,000 points to achieve S rank.
    """
    display_name = "Rank Threshold Percentage"

    range_start = 50
    range_end = 120

    default = 100


class ShuffleMusicNotes(Toggle):
    """
    If true, the ability to see, and therefore hit each music note will need to be unlocked with an item.

    Turning this on will enable more complex logic for rank location checks.

    C Rank: 50% of the song's total music notes must be playable to be in logic
    B Rank: 70% of the song's total music notes must be playable to be in logic
    A Rank: 85% of the song's total music notes must be playable to be in logic
    S Rank: 95% of the song's total music notes must be playable to be in logic

    You will always be granted a set of starter music notes to ensure you can roughly B Rank each starting song.
    """
    display_name: str = "Shuffle Music Notes"


class IncludeTurboMode(Toggle):
    """
    If true, clearing a song in Turbo Mode will unlock a location check.

    Turbo Mode will need to be unlocked for each tromboner by receiving their Turbo Mode item.
    """
    display_name: str = "Include Turbo Mode"


class TrombonerCount(Range):
    """
    Determines how many different tromboners will be available to plays as.

    Each song / music note / ability (turbo mode, license to toot etc.) will have to be unlocked for each tromboner
    separately.

    Each song clear, rank clear and turbo mode clear will be counted separately for each tromboner.

    Note: There are no gameplay differences between tromboners.
          Adding more tromboners purely acts as a location check multiplier, allowing you to scale for larger games.
    """
    display_name = "Tromboners Count"

    range_start = 1
    range_end = 10

    default = 1


class Cardsanity(Toggle):
    """
    If true, collecting each of the 50 tromboner cards will unlock a location check.

    You will not be able to get toots from playing songs until you receive a License to Toot!!! item for at least one
    tromboner.
    """
    display_name: str = "Cardsanity"


class Craftsanity(Toggle):
    """
    If true, crafting each of the 50 tromboner cards with turds will unlock a location check.

    You will not be able to get toots from playing songs until you receive a License to Toot!!! item for at least one
    tromboner.

    You will not be able to turd cards until you receive the Turding!!! item.
    You will not be able to craft cards until you receive the Turd Crafting!!! item.
    """
    display_name: str = "Craftsanity"


class Turdsanity(Toggle):
    """
    If true, turding each of the 50 tromboner cards will unlock a location check.

    You will not be able to get toots from playing songs until you receive a License to Toot!!! item for at least one
    tromboner.

    You will not be able to turd cards until you receive the Turding!!! item.
    """
    display_name: str = "Turdsanity"


class Engoldenatesanity(Toggle):
    """
    If true, engoldenating each of the 50 tromboner cards will unlock a location check.

    You will not be able to get toots from playing songs until you receive a License to Toot!!! item for at least one
    tromboner.

    You will not be able to engoldenate cards until you receive the Engoldenating!!! item.
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

    Only relevant if any of the card collection sanities are enabled.
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

    Only relevant if Turdsanity or Craftsanity is enabled.
    """
    display_name = "Turding Average Reward"

    range_start = 1
    range_end = 749

    default = 150


class EngoldenatedTurdingReward(Range):
    """
    Determines the reward (in turds) for turding an engoldenated card. Vanilla: 375

    Only relevant if Engoldenatesanity is enabled.
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
    include_a_ranks: IncludeARanks
    a_rank_maximum_difficulty: ARankMaximumDifficulty
    include_s_ranks: IncludeSRanks
    s_rank_maximum_difficulty: SRankMaximumDifficulty
    rank_threshold_percentage: RankThresholdPercentage
    shuffle_music_notes: ShuffleMusicNotes
    include_turbo_mode: IncludeTurboMode
    tromboner_count: TrombonerCount
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

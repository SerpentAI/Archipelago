from random import Random
from typing import Dict, List, Set

from .data.entrance_data import Entrance, EntranceRule, EntranceRuleData, entrance_rule_data

from .data.entrance_randomizer_data import (
    dead_end_entrances,
    dead_end_entrances_reverse,
    one_way_entrances,
    randomizable_entrances,
)

from .data.mapping_data import starting_location_to_region

from .data_funcs import entrances_by_region_for_world

from .enums import (
    ZorkGrandInquisitorEntranceRandomizer,
    ZorkGrandInquisitorRegions,
    ZorkGrandInquisitorStartingLocations,
)


class EntranceRandomizer:
    mode: ZorkGrandInquisitorEntranceRandomizer
    random: Random

    randomizable_entrances: List[Entrance]

    remaining_randomizable_entrances: List[Entrance]
    remaining_randomizable_destinations: List[Entrance]

    processed_regions: Set[ZorkGrandInquisitorRegions]
    processed_entrances: Set[Entrance]

    randomized_entrance_rule_data: EntranceRuleData

    swaps: Dict[Entrance, Entrance]
    swaps_reversed: Dict[Entrance, Entrance]

    def __init__(self, mode: ZorkGrandInquisitorEntranceRandomizer, random_instance: Random):
        self.mode = mode
        self.random = random_instance

        self.randomizable_entrances = (
            list(randomizable_entrances)
            + list(dead_end_entrances)
            + list(dead_end_entrances_reverse)
        )

        self.remaining_randomizable_entrances = list(self.randomizable_entrances)
        self.remaining_randomizable_destinations = list(self.randomizable_entrances)

        self.processed_regions = set()
        self.processed_entrances = set()

        self.randomized_entrance_rule_data = dict()

        self.swaps = dict()
        self.swaps_reversed = dict()

    # Rename to generate_entrance_rule_data
    def generate_entrance_rule_data(self, starting_location: ZorkGrandInquisitorStartingLocations) -> EntranceRuleData:
        if self.mode == ZorkGrandInquisitorEntranceRandomizer.DISABLED:
            return entrance_rule_data

        # TODO: Have a retry mechanism in place in case of failure (e.g. too many passes)
        return self._generate_randomized_entrance_rule_data(starting_location)

    def _generate_randomized_entrance_rule_data(
        self,
        starting_location: ZorkGrandInquisitorStartingLocations
    ) -> EntranceRuleData:
        # Randomize entrances moving out from starting location
        initial_region: ZorkGrandInquisitorRegions = starting_location_to_region[starting_location]

        next_regions: List[ZorkGrandInquisitorRegions] = [initial_region]
        next_entrances: List[Entrance] = list()

        passes: int = 0
        final_pass: bool = False

        while True:
            passes += 1

            # Determine entrances in next regions
            region: ZorkGrandInquisitorRegions
            for region in next_regions[:]:
                entrance: Entrance
                for entrance in entrances_by_region_for_world(entrance_rule_data)[region]:
                    if entrance in self.randomizable_entrances and entrance not in self.processed_entrances:
                        next_entrances.append(entrance)

                self.processed_regions.add(region)
                next_regions.remove(region)

            if not len(next_entrances):
                if len(self.remaining_randomizable_entrances):
                    next_entrances = self.remaining_randomizable_entrances[:]
                    final_pass = True
                else:
                    break

            # Randomize next entrances
            self.random.shuffle(next_entrances)

            entrance: Entrance
            for entrance in next_entrances[:]:
                if entrance in self.processed_entrances:
                    continue

                swap: Entrance
                filtered_dataset: List[Entrance] = list()

                for swap in self.remaining_randomizable_destinations:
                    # Don't swap with dead ends in coupled mode unless it's the final pass
                    if self.mode == ZorkGrandInquisitorEntranceRandomizer.COUPLED:
                        if swap in dead_end_entrances_reverse and not final_pass:
                            continue

                    # Don't swap with entrances that lead back to the same region
                    if swap[1] != entrance[0]:
                        filtered_dataset.append(swap)

                if not filtered_dataset:
                    next_entrances.remove(entrance)
                    continue

                swap = self.random.choice(filtered_dataset)
                swap_region: ZorkGrandInquisitorRegions = swap[1]

                if swap_region not in self.processed_regions and swap_region not in next_regions:
                    next_regions.append(swap_region)

                self.swaps[entrance] = swap
                self.swaps_reversed[swap] = entrance

                self._commit_entrance_rule_data((entrance[0], swap[1]), entrance)

                self.remaining_randomizable_entrances.remove(entrance)
                self.remaining_randomizable_destinations.remove(swap)

                self.processed_entrances.add(entrance)
                next_entrances.remove(entrance)

                if self.mode == ZorkGrandInquisitorEntranceRandomizer.COUPLED:
                    # Register opposite entrance immediately
                    opposite_entrance: Entrance = (swap[1], swap[0])
                    opposite_swap: Entrance = (entrance[1], entrance[0])

                    self.swaps[opposite_entrance] = opposite_swap
                    self.swaps_reversed[opposite_swap] = opposite_entrance

                    self._commit_entrance_rule_data((opposite_entrance[0], opposite_swap[1]), opposite_entrance)

                    self.remaining_randomizable_entrances.remove(opposite_entrance)
                    self.remaining_randomizable_destinations.remove(opposite_swap)

                    self.processed_entrances.add(opposite_entrance)

                    if opposite_entrance in next_entrances:
                        next_entrances.remove(opposite_entrance)

            if passes >= 100:
                raise Exception("Too many entrance randomizer passes! Something went wrong!")

        # One-way entrances
        sampled_swaps: List[Entrance] = self.random.sample(
            self.randomizable_entrances,
            len(one_way_entrances)
        )

        i: int
        entrance: Entrance
        for i, entrance in enumerate(one_way_entrances):
            self.swaps[entrance] = sampled_swaps[i]
            self.swaps_reversed[sampled_swaps[i]] = entrance

            swap: Entrance = (entrance[0], sampled_swaps[i][1])

            self._commit_entrance_rule_data(swap, entrance)

        # Non-randomizable entrances
        for entrance in entrance_rule_data.keys():
            if entrance not in self.randomizable_entrances and entrance not in one_way_entrances:
                self._commit_entrance_rule_data(entrance, entrance)

        return self.randomized_entrance_rule_data

    def _commit_entrance_rule_data(self, entrance_randomized: Entrance, entrance_original: Entrance) -> None:
        if entrance_randomized in self.randomized_entrance_rule_data:
            existing_rule: EntranceRule = self.randomized_entrance_rule_data[entrance_randomized]
            new_rule: EntranceRule = entrance_rule_data[entrance_original]

            if new_rule is None:
                return
            elif existing_rule is None:
                self.randomized_entrance_rule_data[entrance_randomized] = new_rule
            else:
                self.randomized_entrance_rule_data[entrance_randomized] = tuple(list(existing_rule) + list(new_rule))
        else:
            self.randomized_entrance_rule_data[entrance_randomized] = entrance_rule_data[entrance_original]

    @classmethod
    def test(cls):
        er = cls(ZorkGrandInquisitorEntranceRandomizer.COUPLED, Random(x=12345))
        er.generate_entrance_rule_data(ZorkGrandInquisitorStartingLocations.DM_LAIR_INTERIOR)

        for entrance in randomizable_entrances:
            print(f"{entrance[0].value} -> {entrance[1].value}")

            if entrance in er.swaps:
                print(f"{er.swaps[entrance][0].value} -> {er.swaps[entrance][1].value}")
            else:
                print("UNCONNECTED! UNCONNECTED! UNCONNECTED!")

            print()

        for entrance in dead_end_entrances:
            print(f"{entrance[0].value} -> {entrance[1].value}")

            if entrance in er.swaps:
                print(f"{er.swaps[entrance][0].value} -> {er.swaps[entrance][1].value}")
            else:
                print("UNCONNECTED! UNCONNECTED! UNCONNECTED!")

            print()

        for entrance in dead_end_entrances_reverse:
            print(f"{entrance[0].value} -> {entrance[1].value}")

            if entrance in er.swaps:
                print(f"{er.swaps[entrance][0].value} -> {er.swaps[entrance][1].value}")
            else:
                print("UNCONNECTED! UNCONNECTED! UNCONNECTED!")

            print()

        for entrance in one_way_entrances:
            print(f"{entrance[0].value} -> {entrance[1].value}")

            if entrance in er.swaps:
                print(f"{er.swaps[entrance][0].value} -> {er.swaps[entrance][1].value}")
            else:
                print("UNCONNECTED! UNCONNECTED! UNCONNECTED!")

            print()

        import pprint
        pprint.pprint(er.randomized_entrance_rule_data)

        count_1 = dict()

        for entrance in entrance_rule_data:
            if entrance[0] not in count_1:
                count_1[entrance[0]] = 0

            count_1[entrance[0]] += 1

        count_2 = dict()

        for entrance in er.randomized_entrance_rule_data:
            if entrance[0] not in count_2:
                count_2[entrance[0]] = 0

            count_2[entrance[0]] += 1

        for region, count in count_1.items():
            if count != count_2[region]:
                print(f"{region} has {count} entrances in original, but {count_2[region]} in randomized")
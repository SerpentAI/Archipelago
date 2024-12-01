from random import Random
from typing import Dict, List, Set, Tuple, Union

from .data.entrance_data import EntranceRuleData, entrance_rule_data, entrances_by_region
from .data.entrance_randomizer_data import dead_end_entrances, dead_end_entrances_reverse, one_way_entrances, randomizable_entrances
from .data.mapping_data import starting_location_to_region

from .enums import (
    ZorkGrandInquisitorEntranceRandomizer,
    ZorkGrandInquisitorRegions,
    ZorkGrandInquisitorStartingLocations,
)


Entrance = Tuple[ZorkGrandInquisitorRegions, ZorkGrandInquisitorRegions]


# TODO: Generate location string tuples for client / slot
# TODO: Figure out how to give location hints to AP
class EntranceRandomizer:
    mode: ZorkGrandInquisitorEntranceRandomizer
    random: Random

    randomizable_entrances: List[Entrance]
    randomizable_destinations: List[Entrance]

    randomizable_entrances_expanded: List[Entrance]
    randomizable_destinations_expanded: List[Entrance]

    remaining_randomizable_entrances: List[Entrance]
    remaining_randomizable_destinations: List[Entrance]

    remaining_randomizable_entrances_expanded: List[Entrance]
    remaining_randomizable_destinations_expanded: List[Entrance]

    processed_regions: Set[ZorkGrandInquisitorRegions]
    processed_entrances: Set[Entrance]

    randomized_entrance_rule_data: EntranceRuleData

    swaps: Dict[Entrance, Entrance]
    swaps_reversed: Dict[Entrance, Entrance]

    def __init__(self, mode: ZorkGrandInquisitorEntranceRandomizer, random_instance: Random):
        self.mode = mode
        self.random = random_instance

        self.randomizable_entrances = list(randomizable_entrances)
        self.randomizable_destinations = list(randomizable_entrances)

        self.randomizable_entrances_expanded = list(randomizable_entrances) + list(dead_end_entrances)
        self.randomizable_destinations_expanded = list(randomizable_entrances) + list(dead_end_entrances)

        self.remaining_randomizable_entrances = list(randomizable_entrances)
        self.remaining_randomizable_destinations = list(randomizable_entrances)

        self.remaining_randomizable_entrances_expanded = list(randomizable_entrances) + list(dead_end_entrances)
        self.remaining_randomizable_destinations_expanded = list(randomizable_entrances) + list(dead_end_entrances)

        self.processed_regions = set()
        self.processed_entrances = set()

        self.randomized_entrance_rule_data = dict()

        self.swaps = dict()
        self.swaps_reversed = dict()

    def randomize(self, starting_location: ZorkGrandInquisitorStartingLocations) -> EntranceRuleData:
        if self.mode == ZorkGrandInquisitorEntranceRandomizer.COUPLED:
            return self._randomize_coupled(starting_location)
        elif self.mode == ZorkGrandInquisitorEntranceRandomizer.UNCOUPLED:
            return self._randomize_uncoupled(starting_location)

        return entrance_rule_data

    def _randomize_coupled(self, starting_location: ZorkGrandInquisitorStartingLocations) -> EntranceRuleData:
        if self.mode == ZorkGrandInquisitorEntranceRandomizer.DISABLED:
            return entrance_rule_data

        # Seed all non-randomizable entrances
        # TODO: Still need a clean way to do this. Better data?
        # for entrance in entrance_rule_data.keys():
        #     if entrance not in self.randomizable_entrances_expanded and entrance not in one_way_entrances:
        #         self.randomized_entrance_rule_data[entrance] = entrance_rule_data[entrance]

        # Randomize entrances moving out from starting location
        initial_region: ZorkGrandInquisitorRegions = starting_location_to_region[starting_location]

        next_regions: List[ZorkGrandInquisitorRegions] = [initial_region]
        next_entrances: List[Entrance] = list()

        count = 0

        while len(self.remaining_randomizable_entrances):
            count += 1

            # Determine entrances in next regions
            region: ZorkGrandInquisitorRegions
            for region in next_regions.copy():
                entrance: Entrance
                for entrance in entrances_by_region[region]:
                    if entrance in self.randomizable_entrances_expanded and entrance not in self.processed_entrances:
                        next_entrances.append(entrance)

                self.processed_regions.add(region)
                next_regions.remove(region)

            # Randomize next entrances
            self.random.shuffle(next_entrances)

            entrance: Entrance
            for entrance in next_entrances.copy():
                dataset: List[Entrance] = self.remaining_randomizable_destinations_expanded

                if len(next_entrances) == 1:
                    dataset = self.remaining_randomizable_destinations or dataset

                # Prevent looping back to the same region
                filtered_dataset: List[Entrance] = list()

                swap: Entrance
                for swap in dataset:
                    if swap[1] != entrance[0]:
                        filtered_dataset.append(swap)

                swap: Entrance = self.random.choice(filtered_dataset)
                swap_region: ZorkGrandInquisitorRegions = swap[1]

                if swap_region not in self.processed_regions and swap_region not in next_regions:
                    next_regions.append(swap_region)

                self.swaps[entrance] = swap
                self.swaps_reversed[swap] = entrance

                self.randomized_entrance_rule_data[(entrance[0], swap[1])] = entrance_rule_data[entrance]

                if entrance in self.remaining_randomizable_entrances_expanded:
                    self.remaining_randomizable_entrances_expanded.remove(entrance)
                if entrance in self.remaining_randomizable_entrances:
                    self.remaining_randomizable_entrances.remove(entrance)

                if swap in self.remaining_randomizable_destinations_expanded:
                    self.remaining_randomizable_destinations_expanded.remove(swap)
                if swap in self.remaining_randomizable_destinations:
                    self.remaining_randomizable_destinations.remove(swap)

                self.processed_entrances.add(entrance)
                next_entrances.remove(entrance)

                # Register opposite entrance
                self.swaps[(swap[1], swap[0])] = (entrance[1], entrance[0])
                self.swaps_reversed[(entrance[1], entrance[0])] = (swap[1], swap[0])

                self.randomized_entrance_rule_data[(swap[1], entrance[0])] = entrance_rule_data[(swap[1], swap[0])]

                if (swap[1], swap[0]) in self.remaining_randomizable_entrances_expanded:
                    self.remaining_randomizable_entrances_expanded.remove((swap[1], swap[0]))
                if (swap[1], swap[0]) in self.remaining_randomizable_entrances:
                    self.remaining_randomizable_entrances.remove((swap[1], swap[0]))

                if (entrance[1], entrance[0]) in self.remaining_randomizable_destinations_expanded:
                    self.remaining_randomizable_destinations_expanded.remove((entrance[1], entrance[0]))
                if (entrance[1], entrance[0]) in self.remaining_randomizable_destinations:
                    self.remaining_randomizable_destinations.remove((entrance[1], entrance[0]))

                self.processed_entrances.add((swap[1], swap[0]))

            print(len(self.remaining_randomizable_entrances_expanded))

            if count > 10:
                break

        # Connect leftover entrances
        print()
        print(self.remaining_randomizable_entrances_expanded)
        print()
        print(self.remaining_randomizable_destinations_expanded)
        print()
        print(self.remaining_randomizable_entrances)
        print()
        print(self.remaining_randomizable_destinations)

        # Add one-way entrances

    def _randomize_uncoupled(self, starting_location: ZorkGrandInquisitorStartingLocations) -> EntranceRuleData:
        pass

    @classmethod
    def test(cls):
        er = cls(ZorkGrandInquisitorEntranceRandomizer.COUPLED, Random(x=54321))
        er.randomize(ZorkGrandInquisitorStartingLocations.PORT_FOOZLE)

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


        # for entrance, swap in er.swaps.items():
        #     print(f"{entrance[0].value} -> {entrance[1].value}")
        #     print(f"{swap[0].value} -> {swap[1].value}")
        #     print()
        #
        # for entrance, rule in er.randomized_entrance_rule_data.items():
        #     print(f"{entrance[0].value} -> {entrance[1].value}")
        #     print(rule)
        #     print()
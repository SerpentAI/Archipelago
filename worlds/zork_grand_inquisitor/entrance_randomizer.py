from random import Random
from typing import Dict, List, Optional, Set, Tuple

from .data.entrance_data import Entrance, EntranceRule, EntranceRuleData, entrance_rule_data

from .data.entrance_randomizer_data import (
    dead_end_entrances,
    dead_end_entrances_reverse,
    one_way_entrances,
    randomizable_entrances,
)

from .enums import ZorkGrandInquisitorEntranceRandomizer, ZorkGrandInquisitorRegions


class EntranceRandomizer:
    mode: ZorkGrandInquisitorEntranceRandomizer
    random: Random

    passes: int

    randomizable_entrances: List[Entrance]
    one_way_entrances: List[Entrance]

    replacement_entrances: Dict[Entrance, Entrance]

    randomized_entrance_rule_data: EntranceRuleData

    def __init__(self, mode: ZorkGrandInquisitorEntranceRandomizer, random_instance: Random):
        self.mode = mode
        self.random = random_instance

        self.passes = 0

        self.randomizable_entrances = (
            list(randomizable_entrances)
            + list(dead_end_entrances)
            + list(dead_end_entrances_reverse)
        )

        self.one_way_entrances = list(one_way_entrances)

        self.replacement_entrances = dict()

        self.randomized_entrance_rule_data = dict()

    def generate_entrance_rule_data(self) -> EntranceRuleData:
        if self.mode == ZorkGrandInquisitorEntranceRandomizer.DISABLED:
            return entrance_rule_data

        graph: Graph = Graph(
            edges=entrance_rule_data.keys(),
            edges_randomizable=self.randomizable_entrances,
            edges_one_way=self.one_way_entrances,
        )

        while True:
            self.passes += 1
            print(f"Zork Grand Inquisitor - Entrance Randomizer Pass #{self.passes}...")

            if self.passes > 100:
                raise Exception("Zork Grand Inquisitor - Entrance Randomizer Failure")

            if self.mode == ZorkGrandInquisitorEntranceRandomizer.COUPLED:
                if graph.shuffle_edges_coupled(random=self.random):
                    break
            elif self.mode == ZorkGrandInquisitorEntranceRandomizer.UNCOUPLED:
                if graph.shuffle_edges_uncoupled(random=self.random):
                    break

        self.replacement_entrances = graph.replacement_edges

        # One-way entrances
        sampled_replacement_entrances: List[Entrance] = self.random.sample(
            self.randomizable_entrances,
            len(self.one_way_entrances)
        )

        i: int
        entrance: Entrance
        for i, entrance in enumerate(self.one_way_entrances):
            self.replacement_entrances[entrance] = sampled_replacement_entrances[i]

        self.randomized_entrance_rule_data = dict()

        return self._assemble_entrance_rule_data()

    def _assemble_entrance_rule_data(self) -> EntranceRuleData:
        entrance: Entrance
        for entrance in entrance_rule_data.keys():
            if entrance in self.replacement_entrances:
                self._commit_entrance_rule_data((entrance[0], self.replacement_entrances[entrance][1]), entrance)
            else:
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
        max_passes: int = 0

        for _ in range(1):
            er = EntranceRandomizer(
                ZorkGrandInquisitorEntranceRandomizer.COUPLED,
                Random(x=12345),
            )

            er.generate_entrance_rule_data()

            if er.passes > max_passes:
                max_passes = er.passes

        print(f"Max passes: {max_passes}")


GraphNode = ZorkGrandInquisitorRegions
GraphNodes = List[ZorkGrandInquisitorRegions]

GraphEdge = Tuple[ZorkGrandInquisitorRegions, ZorkGrandInquisitorRegions]
GraphEdges = List[Tuple[ZorkGrandInquisitorRegions, ZorkGrandInquisitorRegions]]


class Graph:
    nodes: GraphNodes

    edges: GraphEdges

    edges_non_randomizable: GraphEdges
    edges_randomizable: GraphEdges
    edges_one_way: GraphEdges

    replacement_edges: Dict[GraphEdge, GraphEdge]

    def __init__(self, edges: GraphEdges, edges_randomizable: GraphEdges, edges_one_way: GraphEdges):
        self.edges = edges

        self.edges_randomizable = edges_randomizable
        self.edges_one_way = edges_one_way

        self.nodes = list()
        self.edges_non_randomizable = list()

        edge: GraphEdge
        for edge in self.edges:
            if edge[0] not in self.nodes:
                self.nodes.append(edge[0])

            if edge not in edges_randomizable and edge not in edges_one_way:
                self.edges_non_randomizable.append(edge)

        assert self.is_fully_connected()

        self.replacement_edges = dict()

    def shuffle_edges_coupled(self, random: Optional[Random] = None) -> bool:
        if random is None:
            random = Random()

        shuffled_edges: GraphEdges = self.edges_non_randomizable[:]

        remaining_edges: GraphEdges = self.edges_randomizable[:]
        random.shuffle(remaining_edges)

        remaining_replacement_edges: GraphEdges = self.edges_randomizable[:]
        random.shuffle(remaining_replacement_edges)

        cycle: int = 0
        while remaining_edges:
            cycle += 1

            if cycle > 250:
                return False

            edge: GraphEdge = remaining_edges.pop()

            potential_replacement_edges: GraphEdges = [
                replacement for replacement in remaining_replacement_edges if replacement != (edge[1], edge[0])
            ]

            if not potential_replacement_edges:
                remaining_edges.append(edge)
                continue

            replacement_edge: GraphEdge = random.choice(potential_replacement_edges)
            remaining_replacement_edges.remove(replacement_edge)

            new_edge: GraphEdge = (edge[0], replacement_edge[1])
            shuffled_edges.append(new_edge)

            reverse_replacement_edge: GraphEdge = (replacement_edge[1], replacement_edge[0])
            remaining_edges.remove(reverse_replacement_edge)

            reverse_edge: GraphEdge = (edge[1], edge[0])
            remaining_replacement_edges.remove(reverse_edge)

            new_reverse_edge: GraphEdge = (replacement_edge[1], edge[0])
            shuffled_edges.append(new_reverse_edge)

            node_adjacency_list: Dict[GraphNode, GraphNodes] = self.generate_node_adjacency_list(
                edges=shuffled_edges + remaining_edges
            )

            if not self.is_fully_connected(node_adjacency_list):
                remaining_edges.append(edge)
                remaining_replacement_edges.append(replacement_edge)

                shuffled_edges.remove(new_edge)

                remaining_edges.append(reverse_replacement_edge)
                remaining_replacement_edges.append(reverse_edge)

                shuffled_edges.remove(new_reverse_edge)

                continue

            self.replacement_edges[edge] = replacement_edge
            self.replacement_edges[reverse_replacement_edge] = reverse_edge

        print(f"Success! Cycles: {cycle}")

        for edge, replacement_edge in self.replacement_edges.items():
            print(edge)
            print(replacement_edge)
            print()

        return True

    def shuffle_edges_uncoupled(self, random: Optional[Random] = None) -> GraphEdges:
        if random is None:
            random = Random()

        shuffled_edges: GraphEdges = self.edges_non_randomizable[:]

        remaining_edges: GraphEdges = self.edges_randomizable[:]
        random.shuffle(remaining_edges)

        remaining_replacement_edges: GraphEdges = self.edges_randomizable[:]
        random.shuffle(remaining_replacement_edges)

        cycle: int = 0
        while remaining_edges:
            cycle += 1

            if cycle > 500:
                return False

            edge: GraphEdge = remaining_edges.pop()

            potential_replacement_edges: GraphEdges = [
                replacement for replacement in remaining_replacement_edges if replacement != (edge[1], edge[0])
            ]

            if not potential_replacement_edges:
                remaining_edges.append(edge)
                continue

            replacement_edge: GraphEdge = random.choice(potential_replacement_edges)
            remaining_replacement_edges.remove(replacement_edge)

            new_edge: GraphEdge = (edge[0], replacement_edge[1])
            shuffled_edges.append(new_edge)

            node_adjacency_list: Dict[GraphNode, GraphNodes] = self.generate_node_adjacency_list(
                edges=shuffled_edges + remaining_edges
            )

            if not self.is_fully_connected(node_adjacency_list):
                remaining_edges.append(edge)
                remaining_replacement_edges.append(replacement_edge)

                shuffled_edges.remove(new_edge)

                continue

            self.replacement_edges[edge] = replacement_edge

        print(f"Success! Cycles: {cycle}")

        return True

    def is_fully_connected(self, node_adjacency_list: Dict[GraphNode, GraphNodes] = None) -> bool:
        node_adjacency_list = node_adjacency_list or self.generate_node_adjacency_list()
        nodes_seen: Set[GraphNode] = set()

        def dfs(node: GraphNode):
            nodes_seen.add(node)

            adjacent_node: GraphNode
            for adjacent_node in node_adjacency_list[node]:
                if adjacent_node not in nodes_seen:
                    dfs(adjacent_node)

        dfs(self.nodes[0])

        return len(nodes_seen) == len(self.nodes)

    def generate_node_adjacency_list(
        self, nodes: Optional[GraphNodes] = None, edges: Optional[GraphEdges] = None,
    ) -> Dict[GraphNode, GraphNodes]:
        nodes = nodes or self.nodes
        edges = edges or self.edges

        adjacency_list: Dict[GraphNode, GraphNodes] = {node: list() for node in nodes}

        edge: GraphEdge
        for edge in edges:
            adjacency_list[edge[0]].append(edge[1])

        return adjacency_list

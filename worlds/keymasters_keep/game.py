import abc

from random import Random
from typing import Any, List, Optional, Tuple

from .enums import KeymastersKeepGamePlatforms

from .game_objective_template import GameObjectiveTemplate


class Game:
    name: str  # Official name of the game. Use a resource like IGDB to get the correct name
    platform: KeymastersKeepGamePlatforms  # Platform that the game integration was developed with and tested on

    # Other available platforms the game integration might work with
    platforms_other: Optional[List[KeymastersKeepGamePlatforms]] = None

    is_adult_only_or_unrated: bool = True  # ESRB AO / PEGI 18 / USK 18 / Unrated? Used for filtering

    random: Random  # Random instance
    archipelago_options: Any  # Archipelago options dataclass

    def __init__(self, random: Random = None, archipelago_options: Any = None) -> None:
        self.random = random or Random()
        self.archipelago_options = archipelago_options

    @property
    def only_has_difficult_objectives(self) -> bool:
        template: GameObjectiveTemplate
        for template in self.game_objective_templates():
            if not template.is_difficult:
                return False

        return True

    @property
    def only_has_time_consuming_objectives(self) -> bool:
        template: GameObjectiveTemplate
        for template in self.game_objective_templates():
            if not template.is_time_consuming:
                return False

        return True

    @abc.abstractmethod
    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()

    @abc.abstractmethod
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        ...

    def filter_game_objective_templates(
        self,
        include_difficult: bool = False,
        include_time_consuming: bool = False,
    ) -> List[GameObjectiveTemplate]:
        filtered_objectives: List[GameObjectiveTemplate] = list()

        template: GameObjectiveTemplate
        for template in self.game_objective_templates():
            if not include_difficult and template.is_difficult:
                continue

            if not include_time_consuming and template.is_time_consuming:
                continue

            filtered_objectives.append(template)

        return filtered_objectives

    def generate_objectives(
        self,
        count: int = 1,
        include_difficult: bool = False,
        include_time_consuming: bool = False,
    ) -> Tuple[List[str], List[str]]:
        optional_constraints: List[str] = list()

        template: GameObjectiveTemplate
        for template in self.optional_game_constraint_templates():
            optional_constraints.append(template.generate_game_objective(self.random))

        filtered_objectives: List[GameObjectiveTemplate] = list()
        weights: List[int] = list()

        for template in self.game_objective_templates():
            if not include_difficult and template.is_difficult:
                continue

            if not include_time_consuming and template.is_time_consuming:
                continue

            filtered_objectives.append(template)
            weights.append(template.weight)

        selected_objectives: List[str] = list()

        if count <= len(filtered_objectives):
            selected_objectives = self.random.choices(filtered_objectives, weights=weights, k=count)
        else:
            for _ in range(count):
                selected_objectives.append(self.random.choices(filtered_objectives, weights=weights)[0])

        objectives: List[str] = [template.generate_game_objective(self.random) for template in selected_objectives]

        return optional_constraints, objectives

    @classmethod
    def game_name_with_platforms(cls) -> str:
        game_name = f"{cls.name} ({cls.platform.value}"

        if cls.platforms_other:
            game_name += " + "
            game_name += f"{', '.join(platform.value for platform in cls.platforms_other)}"

        game_name += ")"

        return game_name
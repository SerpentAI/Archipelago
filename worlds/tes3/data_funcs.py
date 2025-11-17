from typing import Dict, List, Tuple

from random import Random

from .data.mapping_data import ingredient_alchemy_effects

from .enums import (
    TES3AlchemyEffects,
    TES3AlchemyEffectShuffleModes,
    TES3Ingredients,
)


def process_ingredient_alchemy_effects(
    alchemy_effect_shuffle_mode: TES3AlchemyEffectShuffleModes = TES3AlchemyEffectShuffleModes.VANILLA,
    random: Random = None
) -> Dict[TES3Ingredients, Tuple[TES3AlchemyEffects, ...]]:
    if alchemy_effect_shuffle_mode == TES3AlchemyEffectShuffleModes.VANILLA:
        return ingredient_alchemy_effects | dict()

    if random is None:
        random = Random()

    base_ingredient_alchemy_effects: Dict[TES3Ingredients, Tuple[TES3AlchemyEffects, ...]] = (
        ingredient_alchemy_effects | dict()
    )

    if alchemy_effect_shuffle_mode == TES3AlchemyEffectShuffleModes.REORDER:
        return _process_ingredient_alchemy_effects_reorder(
            base_ingredient_alchemy_effects=base_ingredient_alchemy_effects,
            random=random
        )
    elif alchemy_effect_shuffle_mode == TES3AlchemyEffectShuffleModes.SHUFFLE:
        return _process_ingredient_alchemy_effects_shuffle(
            base_ingredient_alchemy_effects=base_ingredient_alchemy_effects,
            random=random
        )
    elif alchemy_effect_shuffle_mode == TES3AlchemyEffectShuffleModes.SHUFFLE_AND_REORDER:
        shuffled_ingredient_alchemy_effects: Dict[TES3Ingredients, Tuple[TES3AlchemyEffects, ...]] = (
            _process_ingredient_alchemy_effects_shuffle(
                base_ingredient_alchemy_effects=base_ingredient_alchemy_effects,
                random=random
            )
        )

        return _process_ingredient_alchemy_effects_reorder(
            base_ingredient_alchemy_effects=shuffled_ingredient_alchemy_effects,
            random=random
        )
    elif alchemy_effect_shuffle_mode == TES3AlchemyEffectShuffleModes.RANDOMIZE:
        return _process_ingredient_alchemy_effects_randomize(
            base_ingredient_alchemy_effects=base_ingredient_alchemy_effects,
            random=random
        )
    else:
        return base_ingredient_alchemy_effects


def _process_ingredient_alchemy_effects_reorder(
    base_ingredient_alchemy_effects: Dict[TES3Ingredients, Tuple[TES3AlchemyEffects, ...]] = None,
    random: Random = None
) -> Dict[TES3Ingredients, Tuple[TES3AlchemyEffects, ...]]:
    if base_ingredient_alchemy_effects is None:
        base_ingredient_alchemy_effects = ingredient_alchemy_effects | dict()

    if random is None:
        random = Random()

    processed_ingredient_alchemy_effects: Dict[TES3Ingredients, Tuple[TES3AlchemyEffects]] = dict()

    ingredient: TES3Ingredients
    alchemy_effects: Tuple[TES3AlchemyEffects, ...]
    for ingredient, alchemy_effects in base_ingredient_alchemy_effects.items():
        alchemy_effects_reordered: List[TES3AlchemyEffects, ...] = list(alchemy_effects)
        random.shuffle(alchemy_effects_reordered)

        processed_ingredient_alchemy_effects[ingredient] = tuple(alchemy_effects_reordered)

    return processed_ingredient_alchemy_effects


def _process_ingredient_alchemy_effects_shuffle(
    base_ingredient_alchemy_effects: Dict[TES3Ingredients, Tuple[TES3AlchemyEffects, ...]] = None,
    random: Random = None
) -> Dict[TES3Ingredients, Tuple[TES3AlchemyEffects, ...]]:
    if base_ingredient_alchemy_effects is None:
        base_ingredient_alchemy_effects = ingredient_alchemy_effects | dict()

    if random is None:
        random = Random()

    processed_ingredient_alchemy_effects: Dict[TES3Ingredients, Tuple[TES3AlchemyEffects]] = dict()

    ingredients: List[TES3Ingredients] = list(base_ingredient_alchemy_effects.keys())
    alchemy_effects_pool: List[Tuple[TES3AlchemyEffects, ...], ...] = list(base_ingredient_alchemy_effects.values())

    random.shuffle(alchemy_effects_pool)

    i: int
    ingredient: TES3Ingredients
    for i, ingredient in enumerate(ingredients):
        processed_ingredient_alchemy_effects[ingredient] = alchemy_effects_pool[i]

    return processed_ingredient_alchemy_effects


def _process_ingredient_alchemy_effects_randomize(
    base_ingredient_alchemy_effects: Dict[TES3Ingredients, Tuple[TES3AlchemyEffects, ...]] = None,
    random: Random = None
) -> Dict[TES3Ingredients, Tuple[TES3AlchemyEffects, ...]]:
    if base_ingredient_alchemy_effects is None:
        base_ingredient_alchemy_effects = ingredient_alchemy_effects | dict()

    if random is None:
        random = Random()

    processed_ingredient_alchemy_effects: Dict[TES3Ingredients, Tuple[TES3AlchemyEffects]] = dict()

    alchemy_effects: List[TES3AlchemyEffects] = list(TES3AlchemyEffects)

    ingredient: TES3Ingredients
    for ingredient in base_ingredient_alchemy_effects.keys():
        alchemy_effects_randomized: List[TES3AlchemyEffects] = random.sample(
            alchemy_effects,
            k=4
        )

        processed_ingredient_alchemy_effects[ingredient] = tuple(alchemy_effects_randomized)

    return processed_ingredient_alchemy_effects

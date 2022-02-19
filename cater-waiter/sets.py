"""Cater Waiter

https://exercism.org/tracks/python/exercises/cater-waiter

"""

from typing import List, Tuple, Set

from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name: str, dish_ingredients: List[str]) -> Tuple[str, Set[str]]:
    """

    :param dish_name: str
    :param dish_ingredients: list
    :return: tuple of (dish_name, ingredient set)

    This function should return a `tuple` with the name of the dish as the first item,
    followed by the de-duped `set` of ingredients as the second item.
    """

    return dish_name, set(dish_ingredients)


def check_drinks(drink_name: str, drink_ingredients: List[str]) -> str:
    """

    :param drink_name: str
    :param drink_ingredients: list
    :return: str drink name + ("Mocktail" or "Cocktail")

    The function should return the name of the drink followed by "Mocktail" if the drink has
    no alcoholic ingredients, and drink name followed by "Cocktail" if the drink includes alcohol.
    """

    is_cocktail = False
    for ingredient in drink_ingredients:
        if ingredient in ALCOHOLS:
            is_cocktail = True
            break

    drink_suffix = 'Cocktail' if is_cocktail else 'Mocktail'
    return f'{drink_name} {drink_suffix}'


def categorize_dish(dish_name: str, dish_ingredients: List[str]) -> str:
    """

    :param dish_name: str
    :param dish_ingredients: list
    :return: str "dish name: CATEGORY"

    This function should return a string with the `dish name: <CATEGORY>` (which meal category the dish belongs to).
    All dishes will "fit" into one of the categories imported from `sets_categories_data.py`
    (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).
    """

    dish_type = ''
    set_dish_ingredients = set(dish_ingredients)
    if set_dish_ingredients & VEGAN == set_dish_ingredients:
        dish_type = 'VEGAN'
    if set_dish_ingredients & VEGETARIAN == set_dish_ingredients:
        dish_type = 'VEGETARIAN'
    if set_dish_ingredients & PALEO == set_dish_ingredients:
        dish_type = 'PALEO'
    if set_dish_ingredients & KETO == set_dish_ingredients:
        dish_type = 'KETO'
    if set_dish_ingredients & OMNIVORE == set_dish_ingredients:
        dish_type = 'OMNIVORE'
    return f'{dish_name}: {dish_type}'


def tag_special_ingredients(dish: Tuple[str, List[str]]) -> Tuple[str, Set[str]]:
    """

    :param dish: tuple of (str of dish name, list of dish ingredients)
    :return: tuple of (str of dish name, set of dish special ingredients)

    Return the dish name followed by the `set` of ingredients that require a special note on the dish description.
    For the purposes of this exercise, all allergens or special ingredients that need to be tracked are in the
    SPECIAL_INGREDIENTS constant imported from `sets_categories_data.py`.
    """

    dish_name, ingredients = dish
    special_ingredients = set()
    for ingredient in ingredients:
        if ingredient in SPECIAL_INGREDIENTS:
            special_ingredients.add(ingredient)
    return dish_name, special_ingredients


def compile_ingredients(dishes: List[Set[str]]) -> Set[str]:
    """

    :param dishes: list of dish ingredient sets
    :return: set

    This function should return a `set` of all ingredients from all listed dishes.
    """

    all_ingredients = set()
    for dish in dishes:
        for ingredient in dish:
            all_ingredients.add(ingredient)
    return all_ingredients


def separate_appetizers(dishes: List[str], appetizers: List[str]) -> List[str]:
    """

    :param dishes: list of dish names
    :param appetizers: list of appetizer names
    :return: list of dish names

    The function should return the list of dish names with appetizer names removed.
    Either list could contain duplicates and may require de-duping.
    """

    return list(set(dishes) - set(appetizers))


def singleton_ingredients(dishes: List[Set[str]], intersection: Set[str]):
    """

    :param intersection: constant - one of (VEGAN_INTERSECTION,VEGETARIAN_INTERSECTION,PALEO_INTERSECTION,
                                            KETO_INTERSECTION,OMNIVORE_INTERSECTION)
    :param dishes:  list of ingredient sets
    :return: set of singleton ingredients

    Each dish is represented by a `set` of its ingredients.
    Each `<CATEGORY>_INTERSECTION` is an `intersection` of all dishes in the category.
    The function should return a `set` of ingredients that only appear in a single dish.
    """

    singletons = set()
    for dish in dishes:
        for ingredient in dish - intersection:
            singletons.add(ingredient)
    return singletons

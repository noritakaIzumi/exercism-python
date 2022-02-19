"""Inventory Management

https://exercism.org/tracks/python/exercises/inventory-management

"""
from typing import List, Dict, Tuple

Inventory = Dict[str, int]


def create_inventory(items: List[str]) -> Inventory:
    """

    :param items: list - list of items to create an inventory from.
    :return:  dict - the inventory dictionary.
    """

    return add_items({}, items)


def add_items(inventory: Inventory, items: List[str]) -> Inventory:
    """

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return:  dict - the inventory dictionary update with the new items.
    """

    for item in items:
        if not inventory.get(item):
            inventory[item] = 0
        inventory[item] += 1
    return inventory


def decrement_items(inventory: Inventory, items: List[str]) -> Inventory:
    """

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return:  dict - updated inventory dictionary with items decremented.
    """

    for item in items:
        if not inventory.get(item):
            continue
        if inventory.get(item) <= 0:
            continue
        inventory[item] -= 1
    return inventory


def remove_item(inventory: Inventory, item: str) -> Inventory:
    """
    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return:  dict - updated inventory dictionary with item removed.
    """

    if inventory.get(item):
        del inventory[item]
    return inventory


def list_inventory(inventory: Inventory) -> List[Tuple[str, int]]:
    """

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    _list = []
    for item in inventory.keys():
        count = inventory[item]
        if count > 0:
            _list.append((item, count))
    return _list

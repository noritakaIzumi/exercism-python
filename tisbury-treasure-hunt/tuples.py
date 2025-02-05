"""Tisbury Treasure Hunt

https://exercism.org/tracks/python/exercises/tisbury-treasure-hunt

"""
from typing import Tuple, Union, Literal


def get_coordinate(record: Tuple[str, str]) -> str:
    """

    :param record: tuple - a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """

    return record[1]


def convert_coordinate(coordinate: str) -> Tuple[str, str]:
    """

    :param coordinate: str - a string map coordinate
    :return:  tuple - the string coordinate seperated into its individual components.
    """

    return coordinate[0], coordinate[1]


def compare_records(azara_record: Tuple[str, str], rui_record: Tuple[str, Tuple[str, str], str]) -> bool:
    """

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: bool - True if coordinates match, False otherwise.
    """

    return azara_record[1] == ''.join(rui_record[1])


def create_record(
        azara_record: Tuple[str, str],
        rui_record: Tuple[str, Tuple[str, str], str]
) -> Union[
    Tuple[str, str, str, Tuple[str, str], str],
    Literal["not a match"]
]:
    """

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return:  tuple - combined record, or "not a match" if the records are incompatible.
    """

    if compare_records(azara_record, rui_record):
        return azara_record + rui_record
    return "not a match"


def clean_up(combined_record_group: Tuple[Tuple, ...]) -> str:
    """

    :param combined_record_group: tuple of tuples - everything from both participants.
    :return: string of tuples separated by newlines
     - everything "cleaned". Excess coordinates and information removed.
    """

    output = ''
    for group in combined_record_group:
        treasure, _, location, coordinate, quadrant = group
        output += str((treasure, location, coordinate, quadrant))
        output += '\n'
    return output

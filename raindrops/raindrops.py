"""Raindrops

https://exercism.org/tracks/python/exercises/raindrops

"""


def convert(number: int) -> str:
    """convert number to rain string.

    Args:
        number (int):

    Returns:
        str:

    """
    result = ''

    if number % 3 == 0:
        result += 'Pling'
    if number % 5 == 0:
        result += 'Plang'
    if number % 7 == 0:
        result += 'Plong'

    if result == '':
        result = str(number)

    return result

"""Hamming

https://exercism.org/tracks/python/exercises/hamming

"""


def distance(strand_a: str, strand_b: str) -> int:
    """count the mistakes between two DNA strands.

    :type strand_a: str
    :type strand_b: str
    :param strand_a: DNA strands.
    :param strand_b: DNA strands.
    :return: mistake count.

    :raises: ValueError if lengths of the two strands are different.
    """
    if len(strand_a) != len(strand_b):
        raise ValueError('Strands must be of equal length.')

    _distance = 0
    for (letter_a, letter_b) in zip(strand_a, strand_b):
        if letter_a != letter_b:
            _distance += 1

    return _distance

"""Isogram

https://exercism.org/tracks/python/exercises/isogram

"""


def is_isogram(string: str) -> bool:
    """check the given string is a word or phrase without a repeating letter.

    :param string:
    :return:
    """
    # noinspection SpellCheckingInspection
    alphabets = list('abcdefghijklmnopqrstuvwxyz')
    counts = {}
    for alphabet in alphabets:
        counts[alphabet] = 0
    for char in string:
        if counts.get(char.lower()) is not None:
            counts[char.lower()] += 1
    return max(counts.values()) <= 1

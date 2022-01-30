"""Pangram

https://exercism.org/tracks/python/exercises/pangram

"""

import string


def is_pangram(sentence: str) -> bool:
    """get whether the given sentence is a pangram.

    Args:
        sentence (str):

    Returns:
        bool:

    """
    alphabets = {}
    for char in string.ascii_lowercase:
        alphabets[char] = False

    for char in sentence:
        to_lower = char.lower()
        if to_lower in alphabets:  # dict foreach iterates keys
            alphabets[to_lower] = True

    return False not in alphabets.values()

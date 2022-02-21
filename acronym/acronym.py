"""Acronym

https://exercism.org/tracks/python/exercises/acronym

"""
from typing import List

ALPHABETS: List[str] = list('abcdefghijklmnopqrstuvwxyz'.upper())


def abbreviate(words: str) -> str:
    """Convert a phrase to its acronym.

    :param words:
    :return:
    """
    words = words.replace('-', ' ').split()
    abbr = ''
    for word in words:
        if word == '':
            continue
        for char in word:
            if char.upper() in ALPHABETS:
                abbr += char.upper()
                break
    return abbr

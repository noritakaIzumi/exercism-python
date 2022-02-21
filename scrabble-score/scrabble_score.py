"""Scrabble Score

https://exercism.org/tracks/python/exercises/scrabble-score

"""
from typing import List, Tuple

SCORE_MAP: List[Tuple[List[str], int]] = [
    (list('AEIOULNRST'), 1),
    (list('DG'), 2),
    (list('BCMP'), 3),
    (list('FHVWY'), 4),
    (list('K'), 5),
    (list('JX'), 8),
    (list('QZ'), 10),
]


def score(word: str) -> int:
    """get the Scrabble score for the word.

    :param word:
    :return:
    """
    _score = 0
    for char in word:
        for letters, value in SCORE_MAP:
            if char.upper() in letters:
                _score += value
    return _score

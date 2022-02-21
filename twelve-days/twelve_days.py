"""Twelve Days

https://exercism.org/tracks/python/exercises/twelve-days

"""
from typing import List

VERSES = {
    1: 'first',
    2: 'second',
    3: 'third',
    4: 'fourth',
    5: 'fifth',
    6: 'sixth',
    7: 'seventh',
    8: 'eighth',
    9: 'ninth',
    10: 'tenth',
    11: 'eleventh',
    12: 'twelfth',
}
STUFF = {
    1: 'a Partridge in a Pear Tree',
    2: 'two Turtle Doves',
    3: 'three French Hens',
    4: 'four Calling Birds',
    5: 'five Gold Rings',
    6: 'six Geese-a-Laying',
    7: 'seven Swans-a-Swimming',
    8: 'eight Maids-a-Milking',
    9: 'nine Ladies Dancing',
    10: 'ten Lords-a-Leaping',
    11: 'eleven Pipers Piping',
    12: 'twelve Drummers Drumming',
}


def get_lyrics(verse_num: int) -> str:
    """get lyrics.

    :param verse_num:
    :return:
    """
    if verse_num not in range(1, 13):
        return ''
    header = f'On the {VERSES[verse_num]} day of Christmas my true love gave to me: '
    stuffs = [STUFF[i] for i in range(1, verse_num + 1)[::-1]]
    if len(stuffs) > 1:
        stuffs[-1] = f'and {stuffs[-1]}'
    return f'{header}{", ".join(stuffs)}.'


def recite(start_verse: int, end_verse: int) -> List[str]:
    """output text.

    :param start_verse:
    :param end_verse:
    :return:
    """
    return [get_lyrics(i) for i in range(start_verse, end_verse + 1)]

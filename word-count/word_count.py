"""Word Count

https://exercism.org/tracks/python/exercises/word-count

"""
from typing import Dict


def count_words(sentence: str) -> Dict[str, int]:
    """get count of words.

    :param sentence:
    :return:
    """
    count = {}
    words = sentence.strip().replace(',', ' ').replace('.', ' ').replace('_', ' ').split()
    for word in words:
        word = word.strip('\"\'!&@$%^:').lower()
        if word == '':
            continue
        if count.get(word) is None:
            count[word] = 0
        count[word] += 1

    return count

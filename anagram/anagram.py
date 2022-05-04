"""Anagram"""
from typing import List, Set


def find_anagrams(word: str, candidates: List[str]) -> List[str]:
    """

    :param word:
    :param candidates:
    :return:
    """

    def get_codepoint_set(_word: str) -> Set[int]:
        """

        :param _word:
        :return:
        """
        return set(sorted(map(ord, _word)))

    def get_lower_sorted(_word: str) -> List[str]:
        return sorted(_word.lower())

    word_codepoint_set = get_codepoint_set(word)
    word_sorted = get_lower_sorted(word)

    result: List[str] = []
    for candidate in candidates:
        if word.lower() == candidate.lower():
            continue
        codepoint_intersection = list(get_codepoint_set(candidate) & word_codepoint_set)
        if word.lower() != word:
            if not codepoint_intersection:
                continue
            print(codepoint_intersection)
            min_codepoint_intersection = min(codepoint_intersection)
            if min_codepoint_intersection < 65:
                continue
        if get_lower_sorted(candidate) == word_sorted:
            result.append(candidate)
    return result

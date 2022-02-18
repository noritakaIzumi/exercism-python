"""Making the Grade

https://exercism.org/tracks/python/exercises/making-the-grade

"""
import math
from typing import List, Union


def round_scores(student_scores: List[float]) -> List[int]:
    """
    :param student_scores: list of student exam scores as float or int.
    :return: list of student scores *rounded* to nearest integer value.
    """

    return list(map(round, student_scores))


def count_failed_students(student_scores: List[int]) -> int:
    """
    :param student_scores: list of integer student scores.
    :return: integer count of student scores at or below 40.
    """

    return len(list(filter(lambda x: x <= 40, student_scores)))


def above_threshold(student_scores: List[int], threshold: int) -> List[int]:
    """
    :param student_scores: list of integer scores
    :param threshold :  integer
    :return: list of integer scores that are at or above the "best" threshold.
    """

    return list(filter(lambda x: x >= threshold, student_scores))


def letter_grades(highest: int) -> List[int]:
    """
    :param highest: integer of highest exam score.
    :return: list of integer lower threshold scores for each D-A letter grade interval.
             For example, where the highest score is 100, and failing is <= 40,
             The result would be [41, 56, 71, 86]:

             41 <= "D" <= 55
             56 <= "C" <= 70
             71 <= "B" <= 85
             86 <= "A" <= 100
    """

    interval = highest - 40
    return [40 + math.floor(interval * i / 4) + 1 for i in range(4)]


def student_ranking(student_scores: List[int], student_names: List[str]) -> List[str]:
    """
     :param student_scores: list of scores in descending order.
     :param student_names: list of names in descending order by exam score.
     :return: list of strings in format ["<rank>. <student name>: <score>"].
     """

    output = []
    for i, (score, name) in enumerate(zip(student_scores, student_names)):
        output.append(f'{i + 1}. {name}: {score}')
    return output


def perfect_score(student_info: List[List[Union[str, int]]]) -> List[Union[str, int]]:
    """
    :param student_info: list of [<student name>, <score>] lists
    :return: first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    for name, score in student_info:
        if score == 100:
            return [name, score]
    return []

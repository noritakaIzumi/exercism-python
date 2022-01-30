"""High Scores

https://exercism.org/tracks/python/exercises/high-scores

"""


def latest(scores: list) -> int:
    """get latest score.

    Args:
        scores (list):

    Returns:
        int:

    """
    return scores[-1]


def personal_best(scores: list) -> int:
    """get personal best score.

    Args:
        scores (list):

    Returns:
        int:

    """
    return max(scores)


def personal_top_three(scores: list) -> list:
    """get personal top three scores.

    Args:
        scores (list):

    Returns:
        list:

    """
    return sorted(scores, reverse=True)[:3]

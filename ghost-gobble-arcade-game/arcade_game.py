"""Ghost Gobble Arcade Game

https://exercism.org/tracks/python/exercises/ghost-gobble-arcade-game

"""


def eat_ghost(power_pellet_active: bool, touching_ghost: bool) -> bool:
    """

    Args:
        power_pellet_active (bool): does the player have an active power pellet?
        touching_ghost (bool): is the player touching a ghost?

    Returns:
        bool

    """
    return power_pellet_active and touching_ghost


def score(touching_power_pellet: bool, touching_dot: bool) -> bool:
    """

    Args:
        touching_power_pellet (bool): does the player have an active power pellet?
        touching_dot (bool): is the player touching a dot?

    Returns:
        bool
    """
    return touching_power_pellet or touching_dot


def lose(power_pellet_active: bool, touching_ghost: bool) -> bool:
    """

    Args:
        power_pellet_active (bool): does the player have an active power pellet?
        touching_ghost (bool): is the player touching a ghost?

    Returns:
        bool
    """
    return not power_pellet_active and touching_ghost


def win(has_eaten_all_dots: bool, power_pellet_active: bool, touching_ghost: bool) -> bool:
    """

    Args:
        has_eaten_all_dots (bool): has the player "eaten" all the dots?
        power_pellet_active (bool): does the player have an active power pellet?
        touching_ghost (bool): is the player touching a ghost?

    Returns:
        bool
    """
    return has_eaten_all_dots and not lose(power_pellet_active, touching_ghost)

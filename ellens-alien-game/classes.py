"""Ellen's Alien Game

https://exercism.org/tracks/python/exercises/ellens-alien-game

"""
from typing import Any, List, Tuple


class Alien:
    """Alien class.

    """

    total_aliens_created: int = 0

    def __init__(self, x_coordinate: int, y_coordinate: int) -> None:
        """constructor.

        :param x_coordinate:
        :param y_coordinate:
        """

        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        Alien.total_aliens_created += 1

    def hit(self) -> None:
        """decrements the health of an alien object by 1 when called.

        :return:
        """

        self.health -= 1

    def is_alive(self) -> bool:
        """check the alien is alive.

        :return: bool - True if health of the alien is positive, False otherwise.
        """

        return self.health > 0

    def teleport(self, x_coordinate: int, y_coordinate: int) -> None:
        """move.

        :param x_coordinate:
        :param y_coordinate:
        :return:
        """

        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def collision_detection(self, *args, **kwargs) -> Any:
        """detect collision.

        :return:
        """

        pass


def new_aliens_collection(positions: List[Tuple[int, int]]) -> List[Alien]:
    """Function taking a list of position tuples, creating one Alien instance per position.

    :param positions: list - A list of tuples of (x, y) coordinates.
    :return: list - A list of Alien objects.
    """

    aliens = []
    for position in positions:
        aliens.append(Alien(*position))
    return aliens

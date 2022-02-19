"""Matrix

https://exercism.org/tracks/python/exercises/matrix

"""
from typing import List


class Matrix:
    """Matrix class.

    """

    def __init__(self, matrix_string: str) -> None:
        rows = []
        for row in matrix_string.strip().split('\n'):
            rows.append(list(map(int, row.split(' '))))
        self.rows = rows

    def row(self, index: int) -> List[int]:
        """get row.

        :param index: int - row number.
        :return:
        """
        return self.rows[index - 1]

    def column(self, index: int) -> List[int]:
        """get column.

        :param index: int - column number.
        :return:
        """
        column = []
        for row in self.rows:
            column.append(row[index - 1])
        return column

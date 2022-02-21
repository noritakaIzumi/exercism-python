"""Kindergarten Garden

https://exercism.org/tracks/python/exercises/kindergarten-garden

"""
from typing import Optional, List

STUDENTS = [
    'Alice', 'Bob', 'Charlie', 'David',
    'Eve', 'Fred', 'Ginny', 'Harriet',
    'Ileana', 'Joseph', 'Kincaid', 'Larry',
]
FLOWERS = {
    'G': 'Grass',
    'C': 'Clover',
    'R': 'Radishes',
    'V': 'Violets',
}


class Garden:
    """Garden class.

    Place flowers on the garden.

    """

    def __init__(self, diagram: str, students: Optional[List[str]] = None):
        if students is None:
            students = STUDENTS
        self.__set_flower_rows(diagram)
        self.students = sorted(students)

    def __set_flower_rows(self, diagram: str) -> None:
        flower_rows = []
        for row in diagram.split():
            flower_rows.append([row[i:i + 2] for i in range(0, len(row), 2)])
        self.flower_rows = flower_rows

    def plants(self, name: str) -> List[str]:
        """get plants.

        :param name:
        :return:
        """
        if name not in self.students:
            return []
        _list = []
        index = self.students.index(name)
        for row in self.flower_rows:
            for flower in row[index]:
                _list.append(FLOWERS[flower[0]])
        return _list

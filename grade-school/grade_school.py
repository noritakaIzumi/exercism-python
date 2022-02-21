"""Grade School

https://exercism.org/tracks/python/exercises/grade-school

"""
from typing import Dict, Tuple, List, Iterable


class School:
    """School class.
    """

    def __init__(self):
        self.students: Dict[str, Tuple[str, int]] = {}
        self._added: List[bool] = []

    def add_student(self, name: str, grade: int) -> None:
        """

        :param name:
        :param grade:
        :return:
        """
        if self.students.get(name) is not None:
            self._added.append(False)
            return
        self.students[name] = name, grade
        self._added.append(True)

    def roster(self) -> List[str]:
        """get all students.

        :return:
        """

        def sort_by_grade_and_name(
                student: Iterable[Tuple[str, Tuple[str, int]]]
        ) -> Tuple[int, str]:
            name, (_, grade) = student
            return grade, name

        return [student[0] for student in sorted(self.students.items(), key=sort_by_grade_and_name)]

    def grade(self, grade_number: int) -> List[str]:
        """

        :param grade_number:
        :return:
        """
        return sorted(name for name, (_, grade) in self.students.items() if grade == grade_number)

    def added(self) -> List[bool]:
        """

        :return:
        """
        return self._added

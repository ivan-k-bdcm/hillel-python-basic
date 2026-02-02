from .human import Human

class Student(Human):
    """Class representing a student"""

    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str) -> None:
        """
        Initialize a Student object.

        :param gender: Student gender
        :param age: Student age
        :param first_name: Student first name
        :param last_name: Student last name
        :param record_book: Student record book
        """
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        if isinstance(other, Student):
            return NotImplemented
        return str(self) == str(other)

    def __str__(self) -> str:
        """Return string representation of the student"""
        return f'{super().__str__()}Record Book: {self.record_book}\n'
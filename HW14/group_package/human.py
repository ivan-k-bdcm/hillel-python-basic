class Human:
    """Base class representing a human."""

    def __init__(self, gender: str, age: int, first_name: str, last_name: str) -> None:
        """
        Initialize a Human object.

        :param gender: Human gender
        :param age: Human age
        :param first_name: Human first name
        :param last_name: Human last name
        """
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def __str__(self) -> str:
        """Return string representation of the human"""
        return f'Name: {self.first_name}\nSurname: {self.last_name}\nGender: {self.gender}\nAge:{self.age}\n'

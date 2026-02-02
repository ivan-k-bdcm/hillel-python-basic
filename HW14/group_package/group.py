from .student import Student

class Group:
    """Class representing a group of students."""

    def __init__(self, number: str) -> None:
        """
        Initialize a Group object.

        :param number: Group number
        """
        self.number = number
        self.group = set()

    def add_student(self, student_to_add: Student) -> None:
        """
        Add a student to the group.

        :param student_to_add: Student object
        :raises GroupLimitError: if student already has 10 students
        """
        self.group.add(student_to_add)

    def find_student(self, last_name: str) -> Student | None:
        """
        Find a student by last name.

        :param last_name: Student last name
        :return: Student object or None
        """
        for student_to_find in self.group:
            if student_to_find.last_name == last_name:
                return student_to_find
        return None

    def delete_student(self, last_name: str) -> None:
        """
        Delete a student from the group by last name.

        :param last_name: Student last name to delete
        """
        student_to_delete = self.find_student(last_name)
        if student_to_delete is not None:
            self.group.remove(student_to_delete)

    def __str__(self) -> str:
        """Return string representation of the group"""
        all_students = '\n'.join(str(student_to_print) for student_to_print in self.group)

        return f'Number:{self.number}\n {all_students} '
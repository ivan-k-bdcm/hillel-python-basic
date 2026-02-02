class GroupLimitError(Exception):
    """Raised when trying to add more than 10 students to a group."""
    pass


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

    def __str__(self) -> str:
        """Return string representation of the student"""
        return f'{super().__str__()}Record Book: {self.record_book}\n'


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
        if len(self.group) >= 10:
            raise GroupLimitError(
                f'Group {self.number} already has 10 students'
            )
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

gr = Group('PD1')

students_data = [
    ('Male', 30, 'Steve', 'Jobs', 'AN142'),
    ('Female', 25, f'Liz', 'Taylor', f'AN14'),
]

# Add 10 students
for i in range(10):
    students_data.append(
        ('Female', 25, f'Liz{i}', 'Tay', f'AN14{i}')
    )

try:
    for student_gender, student_age, student_first_name, student_last_name, student_record_book in students_data:
        student = Student(student_gender, student_age, student_first_name, student_last_name, student_record_book)
        gr.add_student(student)

except GroupLimitError as e:
    print(f'Error: {e}')

print(gr)

# ====== Tests ======

assert isinstance(gr.find_student('Jobs'), Student), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'

gr.delete_student('Taylor')
print(gr)

gr.delete_student('Taylor')  # No error
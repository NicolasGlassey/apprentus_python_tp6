from datetime import datetime, date
from Person import Person
from Student import Student


def display_person(person):
    print(f'{person.get_lastname()}, {person.get_firstname()}, {person.get_dateofbirth()}')


def display_student(student):
    print(f'{student.get_lastname()}, {student.get_firstname()}, {student.get_dateofbirth()},{student.get_grades()}')


if __name__ == "__main__":
    # region person
    person = Person("Smith", "John", date(1959, 9, 9))
    display_person(person)
    # endregion person

    # region student
    student = Student("Favre", "Jean", date(1964, 7, 12))
    display_student(student)

    student.set_grades([5.5])
    display_student(student)

    student.study("Math", 3)
    display_student(student)
    # endregion student

    # region employee

    # endregion employee

    # region teacher

    # endregion teacher

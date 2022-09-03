from datetime import datetime, date
from Person import Person
from Student import Student
from Employee import Employee
from Teacher import Teacher


def display_person(person):
    print(f'{person.get_lastname()}, {person.get_firstname()}, {person.get_dateofbirth()}')

def display_student(student):
    print(f'{student.get_lastname()}, {student.get_firstname()}, {student.get_dateofbirth()},{student.get_grades()}')

def display_employee(employee):
    print(f'{employee.get_lastname()}, {employee.get_firstname()}, {employee.get_dateofbirth()}, {employee.get_salary()}, {employee.get_social_insurance_number()}')

def display_teacher(teacher):
    print(f'{teacher.get_lastname()}, {teacher.get_firstname()}, {teacher.get_dateofbirth()}, {teacher.get_salary()}, {teacher.get_social_insurance_number()}, {teacher.get_branch()}')

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
    employee = Employee("McDonald", "Ronald", date(1963, 5, 1), 80000.10, "756-ABC-456")
    display_employee(employee)
    # endregion employee

    # region teacher
    teacher = Teacher("Getaz", "Nicole", date(1986, 4, 27), 85000.50, "345-123-234")
    display_teacher(teacher)

    teacher.set_branch("Philosophie")
    display_teacher(teacher)

    teacher.set_branch("Sport")
    display_teacher(teacher)
    # endregion teacher

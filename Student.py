from Person import Person

class Student(Person):
    def __init__(self, lastname, firstname, dateofbirth):
        Person.__init__(self, lastname, firstname, dateofbirth)
        self.__grades = []

    def study(self, branch, study_time):
        pass

    def set_grades(self, grade_to_add):
        self.__grades.append(grade_to_add)

    def get_grades(self):
        return self.__grades

    def clean_grades(self):
        self.__grades.clear()


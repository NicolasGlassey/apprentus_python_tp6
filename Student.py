from Person import Person

class Student(Person):
    def __init__(self, lastname, firstname, dateofbirth):
        Person.__init__(self, lastname, firstname, dateofbirth)
        self.__grades = []

    def study(self, branch, study_time):
        pass

    def set_grades(self, grade_to_add):
        pass

    def get_grades(self):
        pass


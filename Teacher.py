from Employee import Employee

class Teacher(Employee):
    def __init__(self, lastname, firstname, dateofbirth, salary, social_insurance_number):
        Employee.__init__(self,  lastname, firstname, dateofbirth, salary, social_insurance_number)
        self.__branches = []

    def teach(self, branch):
        pass

    def set_branch(self, branch):
        self.__branches.append(branch)

    def get_branch(self):
        return self.__branches
from Person import Person

class Employee(Person):
    def __init__(self, lastname, firstname, dateofbirth, salary, social_insurance_number):
        Person.__init__(self, lastname, firstname, dateofbirth)
        self.__salary = salary
        self.__social_insurance_number = social_insurance_number

    def get_salary(self):
        return self.__salary

    def get_social_insurance_number(self):
        return self.__social_insurance_number

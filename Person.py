class Person:
    def __init__(self, lastname, firstname, dateofbirth):
        self.__lastname = lastname
        self.__firstname = firstname
        self.__dateofbirth = dateofbirth

    def get_lastname(self):
        return self.__lastname

    def get_firstname(self):
        return self.__firstname

    def get_dateofbirth(self):
        return self.__dateofbirth
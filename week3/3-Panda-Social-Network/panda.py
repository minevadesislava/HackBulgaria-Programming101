
import re
class Panda:
    def __init__(self, name, email, gender):
        self.__name = name
        self.__email = email
        self.__gender = gender
    def name(self):
        return self.__name

    def email(self):
        return self.__email

    def gender(self):
        return self.__gender

    def isMale(self):
        return self.__gender == 'male'

    def isFemale(self):
        return self.__gender == 'female'

    def __str__(self):
        return "Panda: {}, {}, {}".format(self.__name, self.__email, self.__gender)

    def __repr__(self):
        return "A repr Panda: {}, {}, {} ".format(self.name, self.email, self.gender)

    def __eg__(self, other):
        return str(self) == str(other)

    def _hash_(self):
        return hash(self.name)  


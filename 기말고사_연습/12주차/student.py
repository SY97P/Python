class Student:
    def __init__(self, number, name, score):
        self.__number = number
        self.__name = name
        self.__score = score

    def getNumber(self):
        return self.__number
    def getName(self):
        return self.__name
    def getScore(self):
        return self.__score

    def setNumber(self, number):
        self.__number = number
    def setName(self, name):
        self.__name = name
    def setScore(selt, score):
        self.__score = score

    def __str__(self):
        return str(self.__number) + '\t'+  self.__name + '\t' + str(self.__score)


'''
11주차 실습 3번, 4번, 5번 이용 클래스

student.py 모듈

class Student 정의

'''

class Student :

    def __init__(self, number, name, score) :
        self.__number = number
        self.__name = name
        self.__score = score


    def __str__(self) :
        return str(self.__number) + "  " + str(self.__name) +"\t" + str(self.__score)

    def getNumber(self) :
        return self.__number

    def getName(self) :
        return self.__name

    def getScore(self) :
        return self.__score

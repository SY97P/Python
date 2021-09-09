'''
11주차 실습 2번


한 줄에 기준 날짜와 비교할 날짜가 있는 "input1.txt" 파일에서

클래스 Date 만들어 compare 메소드, increment 메소드 추가하여 경과한 날짜 출력

class Date

date.py 모듈

'''

class Date :
    def __init__(self, year, month, day) :
        self.__year = year
        self.__month = month
        self.__day = day


    def __str__(self) :
        return str(self.__year) + "/" + str(self.__month) + "/" + str(self.__day)


    def compare(self, other) :
        if self.__year < other.__year :
            return "<"
        elif self.__year > other.__year:
            return ">"
        elif self.__month < other.__month:
            return "<"
        elif self.__month > other.__month:
            return ">"
        elif self.__day < other.__day:
            return "<"
        elif self.__day > other.__day:
            return ">"
        else:
            return "="

    def increment(self) :
        limit = 0

        if self.__month in (1, 3, 5, 7, 8, 10, 12) :
            limit = 31
        elif self.__month in (4, 6, 9, 11) :
            limit = 30
        else :
            if (self.__year % 4 == 0) and (self.__year % 100 != 0 ) or (self.__year % 400 == 0) :
                limit = 29
            else :
                limit = 28

        if self.__day < limit :
            self.__day += 1
        else :
            ## 그 달의 끝 날짜와 같으면 일 = 1 , 다음 달, 다음 년
            self.__day = 1
            if self.__month < 12 :
                self.__month += 1
            else :
                self.__month = 1
                self.__year += 1
            





        


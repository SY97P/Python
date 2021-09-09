'''
2주차 과제 3번

연도를 입력받아 윤년인지 평년인지 판별하는 프로그램
윤년은 4의 배수이며 100의 배수는 제외하지만 400의 배수는 윤년이다.
'''
## 함수 선언 부분 ##
def noLeap() :
    print("%d년은 평년입니다." %year)
def yesLeap() :
    print("%d년은 윤년입니다." %year)
    
def leapYear(int) :

    if (year % 4) == 0 : # 4의 배수라면 #
        if ((year % 100) == 0) and ((year % 400) != 0) : 
            noLeap()
        else :
            yesLeap()
    else :
        noLeap()

## 변수 선언 부분 ##
year = 0

## 메인 코드 부분 ##
year = int(input("연도를 입력하세요 : "))
leapYear(year)
        

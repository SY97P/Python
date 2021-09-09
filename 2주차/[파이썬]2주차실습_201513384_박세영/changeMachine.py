'''
2주차 과제 2번

교환할 돈을 5만원부터 10원 단위까지 몇 장(개)로 줄 수 있는지 출력
교환이 안 되는 금액도 따로 출력

메인에서 다 하지 않고 함수를 선언해보자
'''
## 함수 선언 부분 ##
def parseM() :
    money = int(input("교환할 돈을 입력하세요 : "))
    
    if money >= 50000 :
        count = money/50000
        money %= 50000
    print("5만원 :   %d" %count)
    count = 0
    
    if money >= 10000 :
        count = money/10000
        money %= 10000
    print("1만원 :   %d" %count)
    count = 0
    
    if money >= 5000 :
        count = money/5000
        money %= 5000
    print("5000원 :  %d" %count)
    count = 0
    
    if money >= 1000 :
        count = money/1000
        money %= 1000
    print("1000원 :  %d" %count)
    count = 0
    
    if money >= 500 :
        count = money/500
        money %= 500
    print("500원 :   %d" %count)
    count = 0
    
    if money >= 100 :
        count = money/100
        money %= 100
    print("100원 :   %d" %count)
    count = 0
    
    if money >= 50 :
        count = money/50
        money %= 50
    print("50원 :    %d" %count)
    count = 0
    
    if money >= 10 :
        count = money/10
        money %= 10
    print("10원 :    %d" %count)
    count = 0
    
    print("남는돈 :  %d원" %money)

## 변수 선언 부분 ##
money, noChange = 0, 0
count = 0

## 메인 코드 부분 ##
parseM()

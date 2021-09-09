'''
5주차 교수 연습문제 1번

A~F로 주어진 학점을 숫자로 나타내기
A : 4.0
B : 3.0
C : 2.0
D : 1.0
F : 0
'''


## 함수 선언 부분 ##
def main() :
    while(True) :
        grade = input("학점을 입력하세요 : ")

        if grade == 'Q' or grade == 'q' :
            break

        score = getScore(grade)

        print(grade + " : %d" %score)

def getScore(grade) :
    if grade == 'A' :
        return 4
    elif grade == 'B' :
        return 3
    elif grade == 'C' :
        return 2
    elif grade == 'D' :
        return 1
    else :
        return 0
    
## 변수 선언 부분 ##

## 메인 코드 부분 ##
main()

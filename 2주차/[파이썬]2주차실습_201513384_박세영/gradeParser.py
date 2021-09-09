'''
2주차 실습과제 4번

점수별 학점 나누기
'''
## 함수 선언 부분 ##
def getGrade(int) :
    if score >= 90 :
        print("A 학점 입니다.")
    elif score >= 80 :
        print("B 학점 입니다.")
    elif score >= 70 :
        print("C 학점 입니다.")
    elif score >= 60 :
        print("D 학점 입니다.")
    else : 
        print("F 학점 입니다.")

## 변수 선언 부분 ##
score = 0

## 메인 코드 부분 ##
score = int(input("점수를 입력하세요 : "))
getGrade(score)

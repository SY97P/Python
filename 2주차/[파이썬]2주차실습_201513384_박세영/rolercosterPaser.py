'''
2주차 실습과제 5번

롤러코스터 키제한, 나이제한으로 입구컷하기
'''
## 함수 선언 부분 ##
def nonePass() :
    print("죄송합니다.")
def yesPass() :
    print("타도 좋습니다.")
    
def passParse(stature, age) :
    if(stature < 140) or (age < 10) :
        nonePass()
    else : 
        yesPass()
        
## 변수 선언 부분 ##
stature, age = 0, 0

## 메인 코드 부분 ##
stature = int(input("키를 입력하세요 (cm) : "))
age = int(input("나이를 입력하세요 : "))
passParse(stature, age)

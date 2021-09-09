'''
6주차 self study 1번 (9-2)

계산기 프로그램

1. 숫자1, 연산자, 숫자2 순서로 입력
2. 제곱(**) 연산자 추가
3. 0으로 나누려고 하면 메시지 출력 - 계산 x
'''

## 함수 선언 부분 ##
def cal(val1, val2, oper) :
    if oper == '+' :
        return val1 + val2
    elif oper == '-' :
        return val1 - val2
    elif oper == '*' :
        return val1 * val2
    elif oper == '/' :
        if val2 == 0 :
            print('0으로는 나누면 안 됩니다. ㅠㅠ')
        else :
            return val1 / val2
    elif oper == '**' :
        return val1 ** val2
    else :
        print("Wrong operater")

## 변수 선언 부분 ##
val1, val2, oper = 0, 0, ""

## 메인 코드 부분 ##
val1 = int(input("첫 번재 수를 입력하세요 : "))
oper = input("계산을 입력하세요(+, -, *, /, **) : ")
val2 = int(input("두 번째 수를 입력하세요 : "))

result = cal(val1, val2, oper)

print("## 계산기 : %d %s %d = %d" % (val1, oper, val2, result))

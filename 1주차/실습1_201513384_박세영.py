'''
1주차 과제 - 간단한 계산기 만들기
'''
##함수 선언 부분##

##변수 선언 부분##

##메인 코드 부분##
a = int(input('숫자1 입력: '))
b = int(input('숫자2 입력: '))

result = a+b
print(a, '+', b, '=', result)
result = a*b
print(a, '*', b, '=', result)
result = pow(a, b)
print(a, '^', b, '=', result)


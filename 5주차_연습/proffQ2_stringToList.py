'''
5주차 교수 연습문제 2번

한 줄에 여러 개의 숫자를 입력 받아 최소 값, 최대 값, 합계를 구한다.

'''

string = input("여러 개의 숫자를 입력하세요 : ")

list = list(map(int, string.split()))

min = list[0]
max = list[0]
sum = 0

for i in list :
    sum += i
    if min > i :
        min = i
    elif max < i :
        max = i

print("최소값 : %d" %min)
print("최대값 : %d" %max)
print("합계   : %d" %sum)

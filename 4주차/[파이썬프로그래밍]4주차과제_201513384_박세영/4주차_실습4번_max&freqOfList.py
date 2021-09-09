'''
4주차 실습 4번

정수 리스트를 만들고 리스트 전체, 가장 큰 숫자, 그 숫자 출현횟수 출력

-1 => 종료
'''

list = []
max = 0
count = 0

while(True) :
    num = int(input("숫자를 입력하세요 : "))

    if num == -1 :
        break
    
    list.append(num)

    if max < num :
        max = num
        count = 1
    elif max == num :
        count += 1

print("리스트    : %s" %list)
print("최대값    : %d" % max)
print("출현 횟수 : %d" %count)

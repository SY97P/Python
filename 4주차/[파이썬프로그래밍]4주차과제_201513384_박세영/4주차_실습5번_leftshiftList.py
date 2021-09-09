'''
4주차 실습 5번

정수 리스트를 만들고 왼쪽으로 한 칸씩 이동시킨다.

index 0의 원소는 리스트 맨 마지막으로 이동시킨다.

-1 => 종료

'''

list = []

## 원본 리스트 만들기
while(True) :
    num = int(input("숫자를 입력하세요 : "))

    if num == -1 :
        break

    list.append(num)

print("초기 리스트  :  %s" % list)

## 리스트 이동시키기
temp = list[0]

for i in range(0, len(list)-1) :
    list[i] = list[i+1]
list[len(list)-1] = temp

print("이동후 리스트 : %s" % list)

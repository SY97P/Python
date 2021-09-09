'''
12주차 실습 4번


연습문제 3번을 재귀적으로 구현



정렬된 양의 정수 생성한 후, 찾고자 하는 정수 주어지면 이진 탐색하여 찾는다.


정수가 있으면 인덱스를 출력하며, -1이 주어지면 프로그램 종료한다.

정렬된 양의 정수 생성은 다음을 사용한다.

단, 이진 탐색은 재귀적인 방법을 사용한다. 

'''
import random

def binaryS(lst, low, high, target) :
    if low <= high :
        mid = (low + high) // 2

        if target < lst[mid] :
            return binaryS(lst, low, mid-1, target)
        elif target > lst[mid] :
            return binaryS(lst, mid+1, high, target)
        else :
            return mid
    else :
        return -1

    
def main() :
    n = int(input("Enter a number of data : "))

    data = 0

    numbers = []

    for i in range(n) :
        data += random.randint(1, 5)
        numbers.append(data)

    print("list : ", end = "")
    print(numbers)
    print()

    while True :
        target = int(input("Enter a number to find by recursice method : "))

        if target == -1 :
            break

        index = binaryS(numbers, 0, n-1, target)

        if index == -1 :
            print(target, "is not in the list.")
        else :
            print(target, "is in the list at index ", index,".")
        print()



main()

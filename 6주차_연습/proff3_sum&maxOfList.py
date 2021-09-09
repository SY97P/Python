'''
5주차 교수 연습문제 3번

숫자를 입력받아 합계와 최대값을 출력하는 프로그램

* 모범코드에는 함수에서 두개의 반환값을 갖도록 구현 *

'''

## 함수 선언 부분 ##
def main() :
    line = input("숫자를 한 줄에 입력하세요 : ")

    list1 = list(map(int, line.split(" ")))

    print("주어진 숫자 리스트 : ", list1)

    sum = getSum(list1)
    max = getMax(list1)

    print("합계 : %d, 최대값 : %d" %( sum, max))

def getSum(list1) :
    sum = 0
    for i in list1 :
        sum += i
    return sum

def getMax(list1) :
    max = list1[0]
    for i in list1 :
        if max < i :
            max = i
    return max

## 메인 코드 부분 ##
main()

'''
모범코드

def main() :
    strings = input("숫자를 한 줄에 입력하세요 : ")
    lst = list(map(int, strings.split(" ")))
    print("주어진 숫자 리스트 : ", lst)
    total, max = maxSum(lst)
    print("합계 : %d, 최대값 : %d" % (total, max))

def maxSum(lst) :
    max = lst[0]
    total = lst[0]
    for i in range(1, len(lst)) :
        if lst[i] > max :
            max = lst[i]
        total += lst[i]
    return total, max

main()

'''

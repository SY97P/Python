'''
6주차 실습 3번


1. 한 줄에 숫자를 입력받아 리스트에 저장.
2. 가장 작은 숫자를 제외한 나머지 숫자 합 구하는 프로그램
3. 가장 작은 숫자는 모두 제외
4. 반복문 하나만 사용

'''

def main() :
    line = input("숫자를 한 줄에 입력하세요 : ")

    lst = list(map(int, line.split()))

    print("주어진 숫자 리스트 :\t", lst)

    sum = exceMinSum(lst)

    print("최소 값을 제외한 합계 :\t%d" % sum)

# 리스트 탐색으로 전체 합 구하고
# 최소값 개수를 구하여 전체 합 - 최소값 * 개수
def exceMinSum(lst) :
    min = lst[0]
    sum = 0
    cnt = 0

    for i in lst :
        if min > i :
            min = i
        sum += i

    cnt = lst.count(min)
    sum = sum - cnt*min

    return sum

main()

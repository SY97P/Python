'''
6주차 실습 5번


두 줄의 숫자 리스트를 입력받고 각 요소 순서와 중복 무시하고 같은지 검사하는 프로그램

1. 집합 함수 사용하지 않는다.
2. 리스트 함수 사용가능
3. 필요한 보조 함수 선언 가능

[3, 2, 2, 2, 1, 4, 4, 1] = [2, 1, 3, 3, 3, 4]

'''

def main() :
    line1 = input("첫번째 숫자를 한 줄에 입력하세요 : ")
    line2 = input("두번째 숫자를 한 줄에 입력하세요 : ")

    list1 = list(map(int, line1.split()))
    list2 = list(map(int, line2.split()))

    # 두 리스트 낮은 숫자부터 정렬
    list1.sort()
    list2.sort()

    same = sameSet(list1, list2)

    if same == True :
        print("=> Same sets")
    else :
        print("=> Not same sets")

def sameSet(list1, list2) :
    same = True

    lst1 = [list1[0]]
    lst2 = [list2[0]]

    # 정렬된 두 리스트에서 중복을 제거
    val = list1[0]
    for i in list1 :
        if val != i :
            lst1.append(i)
            val = i
    # print(lst1)

    val = list2[0]
    for i in list2 :
        if val != i :
            lst2.append(i)
            val = i
    # print(lst2)

    for i in range(0, len(lst1)) :
        if lst1[i] != lst2[i] :
            same = False

    return same

main()

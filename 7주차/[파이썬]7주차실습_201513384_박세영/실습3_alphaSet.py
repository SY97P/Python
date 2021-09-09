'''
7주차 실습 3번

[집합]


두 개의 문자열을 입력 받아 알파벳만 집합으로 저장하고 출력하는 프로그램.


1. 대문자는 소문자로 변환
2. 집합으로 나타낸 두 개의 문자열을 출력
3. 교집합, 합집합, 차집합, 대칭 차집합을 출력

'''

def main() :
    line1 = input("첫 번째 문자열 : ")
    line2 = input("두 번째 문자열 : ")

    line1 = line1.lower()
    line2 = line2.lower()

    lst1 = list(line1)
    lst2 = list(line2)

    set1 = set(lst1)
    set2 = set(lst2)

    print(set1)
    print(set2)

    print("Intersection : ", set1.intersection(set2))
    print("Union : ", set1.union(set2))
    print("Set difference (s1 - s2) : ", set1 - set2)
    print("Set difference (s2 - s1) : ", set2 - set1)
    print("Symmetric difference : ", set1^set2)



main()

'''
7주차 실습 문제 1번


한 줄에 숫자를 입력 받아 튜플에 저장하고 출력하는 프로그램.

튜플에 중복된 숫자를 제거하고 튜플에 있는 순서대로 리스트 만들어 출력한다.

'''

def main() :
    line = input("숫자를 한 줄에 입력 : ")

    t = tuple(map(int, line.split()))
    print(t)

    ## 튜플에 중복된 숫자 제거하고 튜플 순서대로 리스트 출력 ##
    lst = []
    for item in t :
        if not(item in lst) :
            lst.append(item)
    print(lst)

    

main()

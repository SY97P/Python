'''
7주차 실습 2번


두 번 숫자를 입력 받아 튜플에 저장하고 출력하는 프로그램

1. 두 튜플 출력
2. 2개의 튜플이 같은지 판별한다.

튜플은 중복될 수 있으며, 순서에 상관없이 개수가 같으면 같다고 본다.

'''

def main() :
    line1 = input("첫번째 숫자를 한 줄에 입력하세요 : ")
    line2 = input("두번째 숫자를 한 줄에 입력하세요 : ")

    tuple1 = tuple(map(int, line1.split()))
    tuple2 = tuple(map(int, line2.split()))

    print("첫번째 숫자 튜플 : \t", tuple1)
    print("두번째 숫자 튜플 : \t", tuple2)
    

    ## 두 튜플이 같은지는 정렬 리스트로 만들어서 확인하자 ##
    same = True
    
    lst1 = sorted(list(tuple1))
    lst2 = sorted(list(tuple2))

    '''
    print(lst1)
    print(lst2)
    '''

    for i in range(len(lst1)) :
        if lst1[i] != lst2[i] :
            same = False
            break

    if same == True :
        print("=> Same elements")
    else :
        print("=> Not the same elements")

main()

'''
7주차 교수 연습 문제 1번


키보드에서 입력받아 튜플 생성하는 프로그램

힌트 : 튜플은 리스트와 달리 변경 가능하지 않으므로 데이터 들어 올 때마다 하나씩
       하나씩 추가하며 튜플을 변경할 수 없다.
        따라서 입력된 데이터 전체를 튜플로 받아 들여야 한다.

        ->

        입려된 데이터를 리스트로 만든 다음 튜플로 변환한다.

'''

def main() :
    strings = input("숫자를 입력하세요 : ")
    t = tuple(map(int, strings.split()))
    ## t = tuple(int(s) for s in strings.split()) ##
    print(t)


main()

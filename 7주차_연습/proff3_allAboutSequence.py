'''
7주차 교수 연습 문제 3번


[컴프리헨션]

1. 리스트 만들어 0 ~ 9 각 숫자를 제곱하여 출력
2. 리스트 만들어 1 ~ 10까지 짝수만 출력
3. 튜플 만들어 1에서 10까지 짝수만 출력
4. 0에서 10까지 홀수를 키로 홀수의 제곱을 값으로 하는 딕셔너리 생성
5. 두 리스트의 각 요소를 하나는 키로, 다른 하나는 값으로 딕셔너리 생성
6. 위의 딕셔너리를 key 순서로 정렬

'''

def main() :
    # 1번
    lst1 = [i**2 for i in range(0, 10)]
    print(lst1)

    lst1 = []

    # 2번
    lst1 = [i for i in range(1, 11) if i % 2 == 0]
    print(lst1)

    lst1 = []

    # 3번
    t = tuple(i for i in range(1, 11) if i % 2 == 1)
    print(t)

    # 4번
    dic = {i:i*i for i in range(11) if i % 2 == 0}
    print(dic)

    # 5번
    lst1 = ['Python', 'Java', 'C++']
    lst2 = [100, 90, 95]
    dic = { key : value for key, value in zip(lst1, lst2)}
    print(dic)

    '''
    컴프리헨션을 사용하지 않는다면 이렇게 해도 괜찮음
    dic = dict(zip(lst1, lst2))
    print(dic)
    '''

    # 6번
    dic = {key : dic[key] for key in sorted(dic)}
    print(dic)
    


main()

'''
7주차 실습 5번

[컴프리헨션]


1. 다음 리스트에서 정수만 제곱하여 리스트 만들어 출력하는 컴프리헨션 프로그램
2. 다음 딕셔너리에서 key/value 쌍을 반대로 만들어 출력하는 컴프리헨션 프로그램

'''

def main() :
    lst = [1, 2, 'Python', 20.5, 5]
    dic = {1:'Python', 2:'Java', 3:'C++'}

    ## 1. 정수만 제곱해 리스트 만들어 출력
    rList = [item**2 for item in lst if type(item) == int]

    print("주어진 리스트 : ", lst)
    print("정수만 제곱한 리스트 : ", rList)
    

    ## 2. key/ value 쌍이 반대인 딕셔너리 만들어 출력
    rDic = {dic[key]:key for key in dic}

    print("주어진 딕셔너리 : ", dic)
    print("키/값을 반대로 한 딕셔너리 : ", rDic)

    



main()

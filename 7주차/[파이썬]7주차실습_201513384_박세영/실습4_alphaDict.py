'''
7주차 실습 4번

[딕셔너리]


문장을 입력 받아 알파벳의 출현 횟수를 딕셔너리 사용하여 출력하고
키를 정렬하여 출력하는 프로그램

1. 딕셔너리 사용하여 출력
2. 키 정렬하여 표로 출력
3. 알파벳은 모두 소문자 변환하여 계산

힌트 : 딕셔너리에 저장된 key/value 쌍은 순서가 없으므로 키 값으로 정렬시켜야
        할 때 다음을 사용한다.

        for key in sorted(dic) :
            print("%5s %7d" % (key, dic[key]))

'''

def main() :
    line = input("문장을 입력하세요 : ")

    line = line.lower()

    lst = list(line)

    dic = {}

    ## 정렬 안 된 딕셔너리 완성
    for c in lst :
        if c == ' ' :
            pass
        elif c in dic.keys() :
            dic[c] = dic[c] + 1
        else :
            dic[c] = 1

    coma = False
    print("{", end = "")
    for key in dic :
        if coma == True :
            print(", ", end="")
        else :
            coma = True
        print("'"+key+"':", dic[key], end="")
    print("}")

    ## 정렬 된 딕셔너리 표 출력
    print("   문자   개수   ")
    print("-----------------")
    for key in sorted(dic) :
        print("%5s %7d" % (key, dic[key]))
    




main()

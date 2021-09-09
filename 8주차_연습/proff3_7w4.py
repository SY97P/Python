'''
8주차 교수 연습문제 3번


7주차 실습 4번 연장 문제

문장을 입력 받아 알파멧의 출현 횟수를 딕셔너리 사용하여 키를 정렬하였다.

같은 문제를 키보드에서 입력 받지 않고 파일 "text2.txt"에 있는 문장을 입력 받아 출력하는 프로그램

'''
# 교수가 푼 거

def main() :
    dic = getChars()
    print("   문자     개수    ")
    print("--------------------")
    for key in sorted(dic) :
        print("%5s %7d" % (key, dic[key]))


def getChars() :
    dic = {}
    inFile = open("text2.txt", "r")

    while True :
        char = inFile.read(1)
        if char == "" :
            break
        if char.isalpha() :
            if char.lower() not in dic :
                dic[char.lower()] = 1
            else :
                dic[char.lower()] += 1
    inFile.close()
    return dic

main()

'''
내가 푼 거
def main() :
    inFp = open("text2.txt" , "r" , encoding = "utf-8")
    inStr = ""

    for inStr in inFp :
        line = inStr.lower()

        lst = list(line)

    dic = {}

    ## 정렬 안 된 딕셔너리 완성
    for c in lst :
        if c == " " :
            pass
        elif c in dic.keys() :
            dic[c] = dic[c] + 1
        else :
            dic[c] = 1

    ## 딕셔너리 정렬된 거 출
    print("   문자    개수   ")
    print("------------------")
    for key in sorted(dic) :
        print("%5s %7d" % (key, dic[key]))
    

    inFp.close()



main()

'''

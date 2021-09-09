'''
12주차 실습 2번


행의 개수를 입력 받아 삼각형 모양의 테이블 생성하는 프로그램


테이블 내의 각 원소는 1부터 차례로 채운다.

테이블에서 각 열의 합을 구하여 맨 아래에 출력한다.

0 입력 -> 종료

'''
def printSumTable(lst, count) :
    sum = 0
    sumlst = []

    for i in range(count) :
        for j in range(i, count) :
            sum += lst[j][i]
        sumlst.append(sum)
        sum = 0

    return sumlst
    
def printTable(lst) :
    count = 0
    for i in range(len(lst)) :
        for j in range(len(lst[i])) :
            count = j+1
            print("%d" % lst[i][j], end = "\t")
        print()
    for i in range(count) :
        print("--", end = "\t")
    print()
    sumlst = printSumTable(lst, count)
    for i in sumlst :
        print("%d" % i , end = "\t")
    print()
    print()
    
    
def main() :
    while True :
        n = int(input("Enter a number : "))

        if n == 0 :
            break

        entire = []

        templst = []

        value = 1

        for i in range(n) :
            for j in range(i+1) :
                templst.append(value)
                value += 1
            entire.append(templst)
            templst = []

        printTable(entire)




main()

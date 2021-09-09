'''
11주차 실습 1번


1부터 100까지 난수 발생하여 선택 정렬한 후
한 줄에 10개씩 정렬된 데이터를
화면과 파일 "sorted.txt"에 출력하는 프로그램

'''
from random import randint

def select(lst) :
    for i in range(len(lst)-1) :
        minIndex = i
        for j in range(i+1, len(lst)) :
            if lst[minIndex] > lst[j] :
                minIndex = j
        if minIndex != i :
            temp = lst[i]
            lst[i] = lst[minIndex]
            lst[minIndex] = temp
            
    return lst
                


def main() :
    outFile = open("sorted.txt", "w")

    lst = []
    
    for i in range(100) :
        n = randint(1, 100)

        lst.append(n)
        '''
        print("%3d" %n, end = "")
        if i % 10 == 9:
            print()
        '''
    lst = select(lst)

    for i in range(len(lst)) :
        print("%3d" %lst[i], end = "")
        outFile.write("%3d" %lst[i])
        if i % 10 == 9 :
            print()
            outFile.write("\n")

    outFile.close()



main()

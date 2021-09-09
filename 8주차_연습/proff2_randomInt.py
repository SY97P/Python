'''
8주차 교수 연습문제 2번


1부터 100까지 난수 발생하여 정렬한 후 파일 "sorted.txt"에 한 줄에 10씩 출력하는 프로그램

'''
from random import randint

'''
def main() :
    lst = []

    for i in range(100) :
        n = randint(1, 100)
        lst.append(n)
    lst.sort()
    writeToFile(lst)


def writeToFile(lst) :
    outFile = open("sorted.txt", "w", encoding = 'utf-8')
    for i in range(len(lst)) :
        if i != 0 and (i+1) % 10 == 0 :
            outFile.write(str(lst[i]) + "\n")
        else :
            outFile.write(str(lst[i]) + " ")
    outFile.close()
'''

def main() :

    outFile = open("sorted.txt", "w", encoding = "utf-8")
    for i in range(100) :
        n = randint(1, 100)
        outFile.write("%d " % n)

        if i != 0 and i % 9 == 0 :
            outFile.write("\n")

    outFile.close()
        

main()
            

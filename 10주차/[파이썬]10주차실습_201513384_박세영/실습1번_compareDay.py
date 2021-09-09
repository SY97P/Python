'''
10주차 실습 1번


파일 "input1.txt"에는 한 줄에 기준 날짜와 비교할 날짜가 주어진다.

두 날짜를 비교하는 함수를 만들어 비교하여 출력하는 프로그램.



두 날짜를 비교하여 기준 날짜가 비교할 날자보다 앞서면 부등호로 표시.

'''
def cmpDay(lst1, lst2) :
    oper = ""
    
    if lst1[0] < lst2[0] :
        oper = "<"
    elif lst1[0] > lst2[0] :
        oper = ">"
    else :
        if lst1[1] < lst2[1] :
            oper = "<"
        elif lst1[1] > lst2[1] :
            oper = ">"
        else :
            if lst1[2] < lst2[2] :
                oper = "<"
            elif lst1[2] > lst2[2] :
                oper = ">"
            else :
                oper = "="

    print(lst1[0],"/",lst1[1],"/", lst1[2], end = " ")
    print("%3s" % oper, end="    ")
    print(lst2[0],"/",lst2[1],"/", lst2[2])
    

def main() :
    inFile = open("input1.txt", "r")

    lst1 = []
    lst2 = []
    
    for line in inFile :
        lst1.append(int(line.split()[0]))
        lst1.append(int(line.split()[1]))
        lst1.append(int(line.split()[2]))

        lst2.append(int(line.split()[3]))
        lst2.append(int(line.split()[4]))
        lst2.append(int(line.split()[5]))

        cmpDay(lst1, lst2)

        lst1 = []
        lst2 = []

    inFile.close()



main()

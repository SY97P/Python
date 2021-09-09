'''
10주차 실습 3번


"input1.txt"에는 한 줄에 기준 날자와 비교할 날짜가 주어진다.


기준 날짜에서 비교할 날짜까지 겨오가한 날짜 수를 셈하여 출력한다.

문제 1에서 만들어 놓은 두 날짜를 비교하는 함수와 문제 2에서 사용한

하루를 증가시키는 함수를 이용하여 구한다.

'''

def increment(lst) :
    y = lst[0]
    m = lst[1]
    d = lst[2]

    rlst = []

    limit = 0
    
    if m in (1, 3, 5, 7, 8, 10, 12) :
        limit = 31
    elif m in (4, 6, 9, 11) :
        limit = 30
    else :
        if (y%4==0) and (y%100!=0) or (y%400==0) :
            limit = 29
        else :
            limit = 28

    if d < limit :
        d += 1
    else :
        # 그 달의 끝 날짜라면
        if m==12 :
            y += 1
            m = 1
        else :
            m += 1
                
        d = 1

    rlst.append(y)
    rlst.append(m)
    rlst.append(d)

    return rlst


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

    '''
    print(lst1[0],"/",lst1[1],"/", lst1[2], end = " ")
    print("%3s" % oper, end="    ")
    print(lst2[0],"/",lst2[1],"/", lst2[2])
    '''

    return oper
    

def main() :
    inFile = open("input1.txt", "r")

    lst1 = []
    lst2 = []

    oper = ""

    count = 0
    
    for line in inFile :
        lst1.append(int(line.split()[0]))
        lst1.append(int(line.split()[1]))
        lst1.append(int(line.split()[2]))

        lst2.append(int(line.split()[3]))
        lst2.append(int(line.split()[4]))
        lst2.append(int(line.split()[5]))

        nlst1 = lst1
        nlst2 = lst2

        while True :
            oper = cmpDay(nlst1, nlst2)

            if oper == "=" :
                break
            elif oper == "<" :
                nlst1 = increment(nlst1)
                count += 1
            else :
                nlst2 = increment(nlst2)
                count -= 1
 
        print(lst1[0],"/",lst1[1],"/", lst1[2], end = "\t\t")
        print(lst2[0],"/",lst2[1],"/", lst2[2], end = "\t\t")
        print(count, "일 경과")

        count = 0
        lst1 = []
        lst2 = []

    inFile.close()



main()

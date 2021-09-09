'''
10주차 실습 5번


"input5.txt"에는 첫 줄에 연도, 달, 시작하는 첫째날의 요일이 주어져있다.

다음 줄 부터는 연도, 달이 주어지며 첫 줄에 주어진 데이터를 바탕으로 달력을
출력하는 프로그램

'''
# 날짜를 하루씩 증가하는 함수
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


# 해당 달의 끝 일수를 구하는 함수
def getDay(y, m) :
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

    return limit



# 달력 출력하는 함수 
def printCal(y, m, d, l) :
    month = ["January", "Feburary", "March", "April", "May", "June", "July",
             "August", "September", "October", "November", "December"]
    date = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    start = 0
    for i in range(len(date)) :
        if date[i] == d :
            start = i
    nstart = start
    count = 1

    print("\t%d %s" % (y, month[m-1]))
    print("-----------------------------")
    print(" Sun Mon Tue Wed Thr Fri Sat")
    while (count <= l) :
        if start > 0 :
            print("    ", end="")
            start -= 1
        else :
            if (nstart+count) % 7 == 1 :
                print()
            print("%4d" % count, end = "")
            count += 1

            
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
    

# 해당하는 달의 첫 시작 요일을 반환하는 함수 
def getDate(lst1, lst2) :
    # 기준이 되는 날과 주어진 날 차이를 계산하여 요일 구하자.
    date = ""

    lst1.append(lst1[2])
    lst1[2] = 1
    lst2.append(1)

    count = 0
    

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

    count = count % 7

    darr = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    date = darr[count]

    return date

    
    

def main() :
    inFile = open("input5.txt", "r")

    chk = True

    olst = []
    tlst = []

    for line in inFile :

        year = int(line.split()[0])
        mon = int(line.split()[1])

        tlst.append(year)
        tlst.append(mon)
        

        if chk :
            year = int(line.split()[0])
            mon = int(line.split()[1])
            date = line.split()[2]
            olst.append(year)
            olst.append(mon)
            olst.append(date)

        

        limit = getDay(year, mon)

        date = getDate(olst, tlst)

        if not chk :
            printCal(year, mon, date, limit)
            print()
        else :
            chk = False


        tlst = []


    inFile.close()





main()

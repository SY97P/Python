'''
10주차 실습 2번


"input2.txt"에는 한 줄에 기준 날짜와 날짜 수가 주어진다.

기준 날짜에서 날짜 수만큼 진행한 후의 날짜를 출력한다. 하루를 증가시키는
함수 increment()를 구현하여 사용한다.


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
    

def main() :
    inFile = open("input2.txt", "r")

    lst = []
    
    for line in inFile :
        year = int(line.split()[0])
        mon = int(line.split()[1])
        day = int(line.split()[2])

        lst.append(year)
        lst.append(mon)
        lst.append(day)

        
        incr = int(line.split()[3]) 

        for i in range(incr) :
            lst = increment(lst)
            
        print("%d/%d/%d, %d일 후\t" %(year, mon, day, incr) , end = "=>")
        print("%d/%d/%d" %(lst[0], lst[1], lst[2]))

        lst = []

    inFile.close()





main()


'''
연습한 코드 

def increment(y, m, d, i) :
    limit = 0
    after = ""

    while ( i > 0 ) :
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
            i -= 1
        else :
            # 그 달의 끝 날짜라면
            if m==12 :
                y += 1
                m = 1
            else :
                m += 1
                
            d = 1
            i -= 1

    after = str(y)+"/"+str(m)+"/"+str(d)

    return after

def main() :
    inFile = open("input2.txt", "r")

    for line in inFile :

        year = int(line.split()[0])
        mon = int(line.split()[1])
        day = int(line.split()[2])

        incr = int(line.split()[3]) 


        after = increment(year, mon, day, incr)

        print("%d/%d/%d, %d일 후\t" %(year, mon, day, incr) , end = "=>")
        print(after)

    inFile.close()





main()
'''

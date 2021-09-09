'''
10주차 실습 4번


"input3.txt"에는 한 줄에 연도, 달, 시작하는 첫째 날의 요일이 주어져있다.


주어진 연도와 달에 해당하는 달력을 출력하는 프로그램

'''
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



def main() :
    inFile = open("input3.txt", "r")

    for line in inFile :
        year = int(line.split()[0])
        mon = int(line.split()[1])
        date = line.split()[2]

        limit = getDay(year, mon)
        
        printCal(year, mon, date, limit)
        print()

    inFile.close()




main()

'''
12주차 실습 1번


다음과 같이 사원의 주당 근무 시간이 기록되어 있다.

8명의 사원(Emp1 ~ Emp8)의 7일 동안의 근무시간이 7개의 열에 저장되어 있다.

사원과 사원의 총근무시간을 총근무시간의 내림차순으로 출력한다.

'''
def selectedSort(nlst) :
    lst = []
    for i in nlst :
        lst.append(i)
    for i in range(len(lst)-1) :
        minIndex = i
        for j in range(i+1, len(lst)) :
            if lst[minIndex] > lst[j] :
                minIndex = j
        if minIndex != i :
            temp = lst[minIndex]
            lst[minIndex] = lst[i]
            lst[i] = temp

    return lst
                

    
    
def totalTime(lst) :
    templst = []

    sum = 0

    for i in range(len(lst)) :
        for j in range(len(lst[0])) :
            sum += lst[i][j]
        templst.append(sum)
        sum = 0

    complst = selectedSort(templst)

    print(complst)
    print(templst)

    indexlst = []
    prev = 0
    
    for i in complst :
        if prev != i :
            for j in range(len(templst)) :
                if i == templst[j] :
                    indexlst.append(j+1)
        prev = i
                

    for i in indexlst :
        print("Emp%d\t\t%d" % (i, templst[i-1]))
        

    
            
    
    
def main() :
    workTime = [[2,4,3,4,5,8,8],
                [7,3,4,3,3,4,4],
                [3,3,4,3,3,2,2],
                [9,3,4,7,3,4,1],
                [3,5,4,3,6,3,8],
                [3,4,4,6,3,4,4],
                [3,7,4,8,3,8,4],
                [6,3,5,9,2,7,9]]

    print("\t  Su   M   T   W   Th  F   Sa ")
    value = 1
    for i in range(len(workTime)) :
        print("Emp%d\t" % value, end = "")
        for j in range(len(workTime[0])) :
            print("%4d" % workTime[i][j], end = "")
        value += 1
        print()

    print()
    print("사원의 총 근무시간")
    print("------------------")
    totalTime(workTime)
    


main()

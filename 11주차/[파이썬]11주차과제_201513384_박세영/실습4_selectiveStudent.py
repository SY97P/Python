'''
11주차 실습 4번


"student.txt" 파일과 student.py 모듈을 이용해 리스트 출력하고

학번 순 선택 정렬 출력

학생 이름 순 선택 정렬 출력

'''

from student import Student

def main() :
    
    infile = open("student.txt", "r")

    stulst = []

    while True :
        line = infile.readline()
        if line == "" :
            break
        lst = line.split()

        number, name, score = int(lst[0]), lst[1], float(lst[2])
        stu = Student(number, name, score)
        stulst.append(stu)

    print("Student data")
    printStudent(stulst)
    print()

    numberlst = selectNumber(stulst)
    print("Sort by student number")
    printStudent(numberlst)
    print()


    namelst = selectName(stulst)
    print("Sort by student name")
    printStudent(namelst)
    print()

    infile.close()


def selectNumber(stulst) :
    for i in range(len(stulst)-1) :
        minIndex = i
        for j in range(i+1, len(stulst)) :
            if stulst[minIndex].getNumber() > stulst[j].getNumber() :
                minIndex = j
        if minIndex != i :
            temp = stulst[i]
            stulst[i] = stulst[minIndex]
            stulst[minIndex] = temp

    return stulst
    

def selectName(stulst) :
    for i in range(len(stulst)-1) :
        minIndex = i
        for j in range(i+1, len(stulst)) :
            if stulst[minIndex].getName() > stulst[j].getName() :
                minIndex = j
        if minIndex != i :
            temp = stulst[i]
            stulst[i] = stulst[minIndex]
            stulst[minIndex] = temp

    return stulst

def printStudent(stulist) :
    for student in stulist :
        print(student)





    


main()

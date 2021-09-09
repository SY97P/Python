'''
11주차 실습 5번


"student.txt" 파일 학생 정보 출력하고


성적 최소 학생 정보와 최고 학생 정보 출력


student.py 모듈 이용

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


    scorelst = selectScore(stulst)
    
    print("Min")
    print(scorelst[0])
    print()

    print("Max")
    print(scorelst[len(scorelst)-1])
    print()


    infile.close()


def selectScore(stulst) :
    for i in range(len(stulst)-1) :
        minIndex = i
        for j in range(i+1, len(stulst)) :
            if stulst[minIndex].getScore() > stulst[j].getScore() :
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

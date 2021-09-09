'''
11주차 실습 3번


메인 함수 파일

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

    printStudent(stulst)

    infile.close()



def printStudent(stulist) :
    for student in stulist :
        print(student)




main()

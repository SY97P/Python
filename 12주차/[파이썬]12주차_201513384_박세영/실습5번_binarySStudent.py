'''
12주차 실습 5번


입력 파일 "student.txt"에는 학번, 이름, 성적이 학번 순으로 저장되어 있다.

한 줄에 해당되는 학생 데이터를 읽어 Student 객체 생성하여 리스트에 저장한다.

리스트에 저장된 학생 데이터를 출력하고 학번을 입력 받아 해당되는 학생을 이진탐색하여 출력한다.


학번으로 -1이 주어지면 탐색을 종료한다.

이진 탐색은 반복적인 방법 또는 재귀적인 방법 어느 것을 사용해도 무방.

Student 객체 사용할 때 사용할 Student 클래스는 주어진 "student.py" 파일의

Student 클래스를 import 하여 사용한다.

'''
from student import Student

def biSearchSt(lst, low, high, target) :
    if low <= high :
        mid = (low + high) // 2

        if target < lst[mid].getNumber() :
            return biSearchSt(lst, low, mid-1, target)
        elif target > lst[mid].getNumber() :
            return biSearchSt(lst, mid+1, high, target)
        else :
            return mid
    else :
        return -1

        

def main() :
    inFile = open("student.txt", "r")

    print("Student data")

    lst = []
    
    for line in inFile :
        number = line.split()[0]
        name = line.split()[1]
        score = line.split()[2]

        s = Student(number, name, score)

        lst.append(s)

        print(s)

    print()

    while True :
        target = input("Enter a student number to find by binary search : ")

        if target == '-1' :
            break
        
        index = biSearchSt(lst, 0, len(lst)-1, target)

        if index == -1 :
            print("Student number", target, "is not in the list.")
        else :
            print("Found!")
            print(lst[index])
        print()

    inFile.close()



main()

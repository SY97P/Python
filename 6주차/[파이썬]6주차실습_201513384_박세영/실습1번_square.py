'''
6주차 실습 1번


1. 한 줄에 숫자를 입력받아 리스트에 저장.
2. 각 숫자를 제곱한 리스트를 만들어 출력
3. 함수 이름 square()

'''

## 함수 선언 부분 ##
def main() :
    strings = input("숫자를 한 줄에 입력하세요 : ")
    lst = list(map(int, strings.split(" ")))
    print("주어진 숫자 리스트:\t", lst)
    newList = square(lst)
    print("제곱한 숫자 리스트:\t", newList)

def square(lst) :
    newList = []
    
    for i in lst :
        newList.append(i**2)

    return newList


## 메인 코드 부분 ##
main()

'''
5주차 교수 연습문제 2번

숫자를 입력 받아 리스트를 만들고 리스트를 역순으로 만들어 출력

리스트 메소드는 사용하지 않는다.

'''


## 함수 선언 부분 ##
def main() :
    line = input("숫자를 한 줄에 입력하세요 : ")

    list1 = list(map(int, line.split(" ")))

    list2 = revList(list1)

    print("주어진 숫자 리스트 : ", list1)
    print("역순으로 만든 리스트 : ", list2)

def revList(list1) :
    list2 = []
    length = len(list1)

    j = 0
    
    for i in range(length-1, -1, -1) :
        list2.append(list1[i])
        
    return list2
    
## 변수 선언 부분 ##
list1 = []

## 메인 코드 부분 ##
main()

'''
모범코드

def main() :
    strings = iput("숫자를 한 줄에 입력하세요 : ")
    lst = list(map(int, strings.split()))
    print("주어진 숫자 리스트:\t", lst)
    revList = reverse(lst)
    print("역순으로 만든 리스트:\t", revList)

def reverse(lst) :
    reverse = []
    for i in range(len(lst)) :
        reverse.append(lst[len(lst) - (i+1)])
    return reverse

main()

'''

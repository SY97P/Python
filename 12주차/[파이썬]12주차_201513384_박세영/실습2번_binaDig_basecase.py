'''
12주차 실습 2번


10진수의 숫자를 입력 받아 이진수로 변환하는 프로그램.


단, 반복적인 방법을 사용한다.

입력으로 -1이 주어지면 프로그램을 종료한다.

'''
def biDig(n) :
    return str(n%2)
    
def main() :
    while True :
        n = int(input("Enter a number : "))

        if n == -1 :
            break

        result = []

        temp = n
        while temp != 0 :
            result.insert(0, biDig(temp))
            temp = temp//2

            
        print("".join(result))
        print()

main()

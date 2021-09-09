'''
12주차 실습 1번


숫자를 입력 받아 숫자의 각 자리 수를 합하여 출력하는 프로그램.

단, 재귀적인 방법을 사용한다.

입력으로 -1이 주어지면 프로그램 종료

'''
def recSumDig(n) :
    if n < 10 :
        return n
    return recSumDig(n//10) + (n%10)
    
    
def main() :
    while True :
        n = int(input("Enter a number : "))

        if n == -1 :
            break

        sum = recSumDig(n)

        print("Sum of digits in", n, ":", sum)
        print()



main()

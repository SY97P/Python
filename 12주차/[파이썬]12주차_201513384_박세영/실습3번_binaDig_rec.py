'''
12주차 실습 3번


실습 2번 재귀 방법 사용하여 구현

'''
def recDig(n) :
    if n < 2 :
        return str(n)
    return recDig(n//2) + str(n%2)
    
def main() :
    while True :
        n = int(input("Enter a number : "))

        if n == -1  :
            break

        result = recDig(n)

        print(result)
        print()




main()

'''
6주차 실습 2번

sum (i) = 1/i + 2/(i-1) + 3/(i-2) + ... + i/1 구하는 프로그램

i 입력 0 => 종료

'''

## 함수 선언 부분 ##
def main() :
    while(True) :
        num = int(input("숫자를 입력하세요 : "))

        if num == 0 :
            break

        sum = getSum(num)

        print("i \t sum(i)")
        print("------------------")
        print(num, "\t %.6f" % sum)
        print()

def getSum(num) :
    sum = 0
    j = 1
    for i in range(num, 0, -1) :
        sum += j/i
        j += 1
    return sum

## 메인 코드 부분 ##
main()

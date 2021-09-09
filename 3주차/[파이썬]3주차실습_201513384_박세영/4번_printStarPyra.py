'''
3주차 실습 4번
별로 만들어진 마름모 만들기
'''

while True :

    num = int(input("숫자를 입력하세요 : "))

    if num % 2 == 0 :
        break

    for k in range(0, num) :
        for i in range(num-k, 1, -1) :
            print(" ", end="")
        for j in range(0, 2*k+1) :
            print("*", end = "")
        print()

    i, j, k = 0, 0, 0

    for k in range(1, num) :
        for i in range(0, k) :
            print(" ", end = "")
        for j in range(0, 2*num-1-2*k) :
            print("*", end = "")
        print()

    print()

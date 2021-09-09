'''
3주차 실습 3번
덧셈 로그 테이블
'''

while True :
    i, j, sum = 0, 0, 0

    num = int(input("숫자를 입력하세요 : "))

    if num == 0 :
        break

    for i in range(1, num+1) :
        sum = 0
        for j in range(1, i+1) :
            if j > 1 :
                print(" +", end = " ")
            print("%d" %j, end = "")
            sum += j
        print(" = %d" %sum)

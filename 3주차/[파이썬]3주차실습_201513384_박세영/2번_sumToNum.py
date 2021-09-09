'''
3주차 실습 2번
1부터 입력받은 숫자까지의 sum of 구하기
'''

while True :

    sum = 0
    
    num = int(input("숫자를 입력하세요 : "))

    if num == 0 :
        break

    for i in range(1, num+1) :
        if i>1 :
            print("+ ", end = "")
        print("%d " %i, end = "")
        sum += i

    print("= %d" %sum)

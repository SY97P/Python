'''
4주차 실습 1번

정수를 입력받아 몇 자리 수인지, 자리수의 합은 얼마인지 구하는 프로그램

-1이 입력되면 프로그램 종료
'''

while(True) :
    num = int(input("숫자를 입력하세요 : "))

    if num == -1 :
        break

    list = []

    count = 0
    div = 1
    while(True) :
        if(num >= div) :
            count += 1
            list.append(int(num/div))
            div *= 10
        else :
            break
    
    for i in range(0, count-1) :
        list[i] = list[i] - list[i+1]*10
    
    sum = 0

    for i in range(0, count) :
        sum += list[i]

    # print("%s" %list)
    print("자릿수의 개수 :  %d" %count)
    print("자릿수의 합   :  %d" %sum)

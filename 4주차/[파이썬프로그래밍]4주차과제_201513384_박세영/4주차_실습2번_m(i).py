'''
4주차 실습 2번

m(i) = 1/2 + 2/3 + ... + i/ (i+1) 급수 만드는 프로그램

0 입력  => 프로그램 종료
'''

while(True) :
    num = int(input("숫자를 입력하세요 : "))

    if num == 0 :
        break

    list = []
    m = 0
    
    for i in range(1, num+1) :
        m += i/(i+1)
        list.append(m)

    print("i         m(i)     ")
    print("-------------------")
    for i in range(0, num) :
        print("%d            %f" %(i+1, list[i]))
    print()
    

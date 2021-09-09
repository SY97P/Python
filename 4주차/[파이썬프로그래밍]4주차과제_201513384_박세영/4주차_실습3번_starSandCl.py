'''
4주차 실습 3번

홀수를 입력 받아 모래시계 모양의 별 출력.

짝수 입력 => 프로그램 종료
'''

while(True) :
    num = int(input("숫자를 입력하세요 : "))

    if num / 2 == 0 :
        break

    list = []
    div = int(num/2)

    for i in range(0, div+1) :
        str = ""
        for j in range(0, i) :
            str += " "
        for j in range(0, num-2*i) :
            str += "*"
        # print("%s" % str)
        list.append(str)

    for i in range(div+1, num) :
        list.append(list[2*div-i])
    
    for i in range(0, num) :
        print("%s" %list[i])
    print()

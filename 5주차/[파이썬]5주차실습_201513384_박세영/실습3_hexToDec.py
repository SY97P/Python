'''
5주차 실습 3번


16진수로 주어진 숫자를 10진수로 변환하는 프로그램

십진수 표현은 대소문자 모두 가능하다


Q 또는 q 입력 => 종료

'''

while(True) :
    string = input("문자열을 입력하세요 : ")

    hexSt = string.lower()

    if hexSt == 'q' :
        break

    hexList = list(hexSt)

    hexLen = len(hexList)

    sum = 0
    j = 0
    
    for i in range(hexLen-1, -1, -1) :
        if ord(hexList[i]) >= ord('a') and ord(hexList[i]) <= ord('f') :
            sum += (ord(hexList[i]) - ord('a')+ 10) * (16 ** j)
        else :
            sum += (ord(hexList[i]) - ord('0')) * (16 ** j)
        j += 1

    print(string + " => 십진수 : %d" % sum)
    print()
    

    


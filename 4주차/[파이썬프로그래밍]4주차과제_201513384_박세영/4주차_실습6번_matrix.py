'''
4주차 실습 6번

이차원 행렬 만들고 5의 배수로 채우는 프로그램

입력 중 0이 있다면 프로그램 종료
'''

while(True) :
    row = int(input("행을 입력하세요 : "))
    col = int(input("열을 입력하세요 : "))

    if row == 0 or col == 0 :
        break

    temp = []
    matrix = []
    value = 0
    
    for i in range(0, row) :
        for j in range(0, col) :
            temp.append(value)
            value += 5
        matrix.append(temp)
        temp = []

    print("%s" % matrix)
    print()

    for i in range(0, row) :
        for j in range(0, col) :
            print("%5d" % matrix[i][j] , end="")
        print()

    print()

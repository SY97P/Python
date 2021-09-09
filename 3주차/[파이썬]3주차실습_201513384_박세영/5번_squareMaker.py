'''
3주차 실습 5번
별로 만들어진 사각형 만들기 (가운데는 비어있다)
'''

while True :
    num = int(input("숫자를 입력하세요 : "))

    if num == 0 :
        break
    
    for i in range(0, num) :
        if i == 0 or i == num-1 :
            for j in range(0, num) :
                print("*", end = "")
        else :
            for j in range(0, num) :
                if j == 0 or j == num-1 :
                    print("*", end = "")
                else :
                    print(" ", end = "")
        print()
    print()

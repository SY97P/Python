'''
3주차 실습 과제 1번

구구단 단수를 입력받아 출력
곱을 내림차순으로 출력한다
'''

while True :

    num = int(input("구구단의 단을 입력하세요 : "))

    if num == 0 :
        break
    
    for i in range(9, 0, -1) :
        print("%d x %d = %d" % (num, i, num*i))

    print()
        

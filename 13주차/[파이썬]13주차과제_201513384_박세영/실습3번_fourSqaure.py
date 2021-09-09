'''
12주차 실습 3번


정사각형 5개를 그린다. 크기는 20px, 정사각형의 간격은 20으로 한다.

배경은 녹색, 펜 색깔은 볼빨간 레드

'''
import turtle as t

def main() :
    t.bgcolor("green")
    t.color("red")
    t.pensize(2)

    for i in range(5) :
        for j in range(4) :
            t.fd(20)
            t.lt(90)
        t.pu()
        t.fd(40)
        t.pd()
    
    t.hideturtle()
    



main()

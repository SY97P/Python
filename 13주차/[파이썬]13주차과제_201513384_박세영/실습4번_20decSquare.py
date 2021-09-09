'''
12주차 실습 4번


다음과 같이 정사각형 10개를 그리는 프로그램


맨 바깥 정사각형의 크기는 200, 내부 사각형은 20씩 줄여 180, 160, 140, ... 으로 한다.

정사각형의 간격은 10으로 한다.

배경은 녹색, 펜색 빨강

'''
import turtle as t

def printSquare(n) :
    if n < 20 :
        return

    for i in range(4) :
        t.fd(n)
        t.lt(90)

    t.pu()
    t.goto(t.xcor()+10, t.ycor()+10)
    t.pd()
    printSquare(n-20)

def main() :
    t.bgcolor("green")
    t.color("red")
    t.pensize(2)

    printSquare(200)

    t.hideturtle()




main()

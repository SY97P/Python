'''
12주차 실습 5번


다음과 같이 눈사람을 그린다. 아래 원의 반경은 100, 위의 원의 반경은 50으로 한다.



두유워너빌더스노우맨-
    
      o
    ㅡOㅡ
      Q

'''
import turtle as t

def main() :
    t.bgcolor("grey")
    t.color("white")
    
    t.begin_fill()
    t.circle(100)
    t.end_fill()

    t.goto(t.xcor(), t.ycor()+200)
    t.begin_fill()
    t.circle(50)
    t.end_fill()

    t.lt(90)
    t.fd(50)
    t.color("black")
    t.pensize(5)
    t.bk(10)
    
    t.pu()
    t.lt(135)
    t.fd(15)
    t.lt(135)
    t.pd()
    t.fd(20)

    t.pu()
    t.lt(90)
    t.fd(35)
    t.rt(90)
    t.fd(5)
    t.pd()
    t.fd(15)

    t.pu()
    t.bk(45)
    t.pd()
    t.bk(15)
    

    t.hideturtle()


main()

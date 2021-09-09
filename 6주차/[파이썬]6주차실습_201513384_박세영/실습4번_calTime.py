'''
6주차 실습 4번


하루 이내의 초를 시, 분, 초로 출력하는 프로그램

1. 하루를 초과하는 시간이 입력되면 다시 입력받는다

2. 0 => 종료

3. 함수 이름 calTime()

'''

def main() :
    while (True) :
        time = int(input("시간을 초로 입력하세요 : "))

        if time == 0 :
            break

        if time < 24 * 60 * 60 :
            hour, minute, second = calTime(time)
            print(time, "초 => ", hour, "시 ", minute, "분 ", second, "초")
        else :
            print("하루 이내의 시간을 입력하세요")

def calTime(time) :
    hour, minute, second = 0, 0, 0

    minute = int(time / 60)
    second = time % 60

    hour = int(minute / 60)
    minute = minute % 60

    return hour, minute, second


main()

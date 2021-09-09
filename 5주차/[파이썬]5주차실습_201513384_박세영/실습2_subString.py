'''
5주차 실습 2번

문자열을 입력.
그 문자열의 위치와 길이에 해당하는 부분문자열(subString) 출력 프로그램

0 입력 => 프로그램 종료

단, 스트링에 내장된 substring 메소드나 함수는 사용하지 않는다.
substring을 제외한 메소드나 함수는 사용 가능하다.

'''

string = input("문자열을 입력하세요 : ")

len = len(string)

while(True) :
    start = int(input("부분 문자열의 시작 위치를 입력하세요 : "))
    length = int(input("부분 문자열의 길이를 입력하세요 : "))

    if start == 0 or length == 0 :
        break

    output = ""

    for i in range(start-1, start+length-1) :
        output += string[i]

    print("substring: \""+ output + '"')
        

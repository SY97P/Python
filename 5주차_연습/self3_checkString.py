'''
5주차 수업 self 3번 (8-3)

입력한 값이 글자인지, 숫자인지, 특수문자인지 판별하는 프로그램

한글, 영어 => '글자입니다.'
숫자       => '숫자입니다.'
특수문자   => '모르겠습니다.'
'''

input = input("문자열 입력 : ")


if input.isalpha() == True :
    print("글자입니다.")
elif input.isdigit() == True :
    print("숫자입니다.")
elif input.isalnum() == True :
    print("글자+숫자입니다.")
else :
    print("모르겠습니다.")

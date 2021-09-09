'''
5주차 교수 연습문제 1번

문자열을 입력 받아 소문자는 대문자로, 대문자는 소문자로 변환하는 프로그램

'''

input = input("문자열을 입력하세요 : ")
output = ""

print("주어진 문자열 : "+ input)

len = len(input)

for i in range(0, len) :
    if input[i].islower() == True :
        output += input[i].upper()
    elif input[i].isupper() == True :
        output += input[i].lower()
    else :
        output += ' '

print("변환된 문자열 : "+ output)

## 모범답안 ##
'''
string = input("문자열을 입력하세요 : ")

newStr = ""

for ch in string :
    if ch.isupper() :
        newCh = ch.lower()
    elif ch.islower() :
        newCh = ch.upper()
    else :
        newCh = ch
    newStr += newCh

print("주어진 문자열 : %s" %string)
print("변환된 문자열 : %s" %newStr)
'''


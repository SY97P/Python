'''
5주차 실습 1번

회문(palindrome)은 앞으로 읽으나 뒤로부터 읽으나 같은 단어나 문장이다.
문자열을 받아서 회문인지 판별하는 프로그램을 작성한다.

'''

string = input("문자열을 입력하세요 : ")

newStr = ""

len = len(string)

for i in range(len-1, -1, -1) :
    newStr += string[i]

isPal = True

for i in range(0, len) :
    if newStr[i] != string[i] :
        isPal = False
        break

if isPal == True :
    print("Palindrome!")
else :
    print("Not a palindrome!")

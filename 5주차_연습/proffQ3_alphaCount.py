'''
5주차 교수 연습문제 3번

문장을 입력받아 각 문자의 출현 횟수와 사용된 문자 총 합계를 구한다.
문자는 알파벳에 국한하고 대무자인 경우 소문자로 바꾸어 계산한다.
'''

string = input("문장을 입력하세요 : ")

lowerStr = string.lower()

countList = [0] * 26
# alphabet 순서에 따라 횟수를 저장하는 int 타입의 26개 원소 list

for ch in lowerStr :
    if ch.isalpha() :
        countList[ord(ch) - ord('a')] += 1

sum = 0

for i in countList :
    sum += i
    if i != 0 :     # 횟수가 0번이 아니라면
        print( chr(i + ord('a')) + "       %d"  % i)

print("Number of characters = %d" % sum)

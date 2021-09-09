'''
5주차 실습 4번


애너그램(anagram) 판별 프로그램

애너그램은 두 문자열이 순서와 상관없이 똑같은 문자를 포함하는 것.

ex) abac와 bcaa는 애너그램이다.

'''

first = input("첫번째 문자열을 입력하세요 : ")
second = input("두번째 문자열을 입력하세요 : ")


# 두 문자열의 알파벳이 각각 몇 번씩 나타났는지 알려주는 리스트
firstList = [0] * 26
secondList = [0] * 26

for ch in first :
    firstList[ord(ch) - ord('a')] += 1

for ch in second :
    secondList[ord(ch) - ord('a')] += 1

isAna = True

# 두 리스트의 같은 알파벳 index끼리 확인하면서 count가 다르면 F, else T
for i in range(0, 26) :
    if firstList[i] != secondList[i] :
        isAna = False
        break

if isAna == True :
    print("Anagram!")
else :
    print("Not an anagram!")

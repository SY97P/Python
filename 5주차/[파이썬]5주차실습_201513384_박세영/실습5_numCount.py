'''
5주차 실습 5번


한 라인에 숫자를 입력 받아 최대 연속된 숫자와 출현 횟수 출력 프로그램

'''

line = input("여러 개의 숫자를 한 줄에 입력하세요 : ")

numList = line.split(" ")

totalCount = len(numList)

countList = [0] * totalCount


prevNum = numList[0]
prevCount = 1

for i in range(1, totalCount) :
    if prevNum == numList[i] :
        prevCount += 1
    else :
        countList[ord(prevNum) - ord('0')] = prevCount
        prevCount = 1
    prevNum = numList[i]
countList[ord(prevNum) - ord('0')] = prevCount

maxNum = countList[0]
count = 0

for i in range(0, len(countList)) :
    if count < countList[i] :
        count = countList[i]
        maxNum = i
    
    
print("최대 연속된 숫자 : %d" %maxNum)
print("연속된 출현 횟수 : %d" % count)

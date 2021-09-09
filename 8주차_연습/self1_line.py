'''
8주차 self study 1번 (11-1)


읽은 각 행에 행 번호를 출력하는 프로그램

힌트 : 1,2,3,... 으로 변경되는 변수를 하나 추가하갸ㅗ, print() 함수에서 "%d %s"

'''
inFp = None
inStr = ""

inFp = open("C:/Users/SYP/Desktop/5학기/[Python]/8주차/data1.txt", "r", encoding = 'UTF8')

'''
while True :
    inStr = inFp.readline()
    if inStr == "" :
        break
    print(inStr , end = "")
'''

count = 1
for inStr in inFp :
    print("%d: %s" % (count,inStr), end = "")
    count = count + 1

inFp.close()

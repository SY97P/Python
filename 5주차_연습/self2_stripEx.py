'''
5주차 수업 self 2번 (8-2)

'<<<파<<이>>썬>>>' 문자열을 '파이썬'으로 출력되도록 하는 프로그램
'''

input = '<<<파<<이>>썬>>>'
output = ""

len = len(input)

for i in range(0, len) :
    # 문자열을 하나씩 탐색하고 <, >가 아니면 문자를 문자열에 연결
    if input[i] != '<' and input[i] != '>' :
        output += input[i]

print("원래 문자열 : %s" %input)
print("바뀐 문자열 : " + output)
    


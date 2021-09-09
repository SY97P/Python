'''
5주차 수업 self 1번

'파이썬은완전재미있어요'에서 '파#썬#완#재#있#요'를 출력하는 프로그램
'''

line = '파이썬은완전재미있어요'

len = len(line)
for i in range(0, len) :
    if i % 2 != 0 :
        print('#', end ="")
    else :
        print(line[i], end ="")

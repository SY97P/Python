'''
7주차 교수 연습 문제 2번


학번과 학생 이름을 입력 받아 딕셔너리에 저장하는 프로그램

키는 학번으로, 값은 학생 이름으로 한다.

q or Q => 종료

1. 딕셔너리
2. 모든 키 값
3. 모든 value 값
4. 모든 key / value 값 쌍
5. 모든 key / value 쌍 키 순서대로

이하 5개를 출력하라.

'''

def main() :
    dic = {}
    
    while True :
        s = input("학번, 이름을 입력하세요 : ")
        if s == 'Q' or s == 'q' :
            break
        key, value = s.split()
        dic[key] = value

    print(dic)
    print(list(dic.keys()))
    print(list(dic.values()))
    print(list(dic.items()))
    for key in sorted(dic) :
        print(key, dic[key])



main()

'''
8주차 교수 연습문제 1번


파일 "text1.txt"에 다음과 같이 학생이름, ":", 점수가
한 라인에 주어졌을 때 데이터를 읽고 평균을 구하여,
출력파일 "out1.txt"에 학생 이름, 성적, 평균을 출력하는 프로그램

'''

def main() :
    inFp, outFp = None, None
    inStr = ""

    with open("C:/Users/SYP/Desktop/5학기/[Python]/8주차/text1.txt", "r", encoding = 'utf-8') as inFp :
        with open("C:/Users/SYP/Desktop/5학기/[Python]/8주차/out1.txt", "w", encoding = 'utf-8') as outFp :
            count = 0
            sum = 0
            ave = 0
            for inStr in inFp :
                field = inStr.split(":")
                name = field[0]
                score = int(field[1])
                count= count + 1

                outFp.write("%s\t\t%.2f\n" %(name, score))
                
                sum = sum + score
                
            ave = sum / count
            outFp.write("Average:\t\t%.2f" %ave)






main()

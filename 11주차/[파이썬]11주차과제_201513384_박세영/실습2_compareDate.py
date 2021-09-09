'''
11주차 실습 2번

메인 함수 파일

'''
from date import Date

def main() :
    infile = open("input1.txt", "r")

    for line in infile :
        datelst = [int(item) for item in line.split()]

        fdate = Date(datelst[0], datelst[1], datelst[2])
        bdate = Date(datelst[3], datelst[4], datelst[5])

        print(fdate, end = "\t\t")
        print(bdate, end = "\t\t")


        count = 0
        
        if fdate.compare(bdate) == "<" :
            temp1 = fdate
            temp2 = bdate
            while (temp1.compare(temp2) != "=") :
                temp1.increment()
                count += 1

            print(count, "일 경과")
            
        elif fdate.compare(bdate) == ">" :
            temp1 = bdate
            temp2 = fdate
            while (temp1.compare(temp2) != "=") :
                temp1.increment()
                count -= 1

            print(count, "일 경과")
            
        else :
            print("0 일 경과")

        
        

    infile.close()



main()

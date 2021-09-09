'''
10주차 실습 1번

'''
def compare(lst1, lst2) :
    for i in range(len(lst1)) :
        f = int(lst1[i])

def main() :
    inFile = open("input1.txt", "r")

    lst1, lst2 = [], []
    
    for instr in inFile :
        temp = ""
        for j in range(3) :
            temp += instr.split()[j]
            if j != 2 :
                temp += "/"
        lst1.append(temp)
        temp = ""
        for j in range(3, 6) :
            temp += instr.split()[j]
            if j != 5 :
                temp += "/"
        lst2.append(temp)
        temp = ""

    compare(lst1, lst2)
            
    inFile.close()

main()

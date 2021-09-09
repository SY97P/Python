from random import randint

def selectiveSort(lst) :
    for i in range(len(lst)-1) :
        minIndex = i
        for j in range(i+1, len(lst)) :
            if lst[minIndex] > lst[j] :
                minIndex = j
        if minIndex != i :
            temp = lst[minIndex]
            lst[minIndex] = lst[i]
            lst[i] = temp


def binaryRepeat(lst, target) :
    low, high = 0, len(lst)-1
    while(low != high) :
        mid = (low+high) // 2
        if target < lst[mid] :
            high = mid-1
        elif target > lst[mid] :
            low = mid+1
        else :
            return mid
    return -1

def binaryRec(lst, low, high, target) :
    if low <= high :
        mid = (low+high) // 2
        if target < lst[mid] :
            binaryRec(lst, low, mid-1, target)
        elif target > lst[mid] :
            binaryRec(lst, mid+1, high, target)
        else :
            return mid
    else :
        return -1


## 2차원 리스트 생성 ##
2dlst, lst, value = [],[],0
for i in range(3) :
    for j in range(4) :
        lst.append(value)
        value += 1
    2dlst.append(lst)
    lst = []

print(2dlst)

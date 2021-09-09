'''
7주차 수업 중 도움될 팁

딕셔너리 key 값만 추출해서 출력해주는 프로그램
+
사용자가 원하는 음식에 대한 궁합 출력 프로그램

'''

foods = { ... }

while(True) :

    myfood = input(str(list(foods.keys())) + "중 좋아하는 음식은?")

    if myfood in foods :
        print("<%s> 궁합 음식은 <%s> 입니다." % (myfood, foods.get(myfood)))
    elif myfood == "끝" :
        break
    else :
        print("그런 음식이 없습니다. 확인해보세요. ")

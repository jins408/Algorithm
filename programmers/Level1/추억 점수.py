def solution(name, yearning, photo):
    answer = []

    # 이름을 담은 딕셔너리 만듬
    dic_name = {}
    for i in range(len(name)):
        dic_name[i] = name[i]
    #print(dic_name)

    # 호감점수를 담은 딕셔너리를 만듬
    dic_year = {}
    for j in range(len(yearning)):
        dic_year[j] = yearning[j]
    #print(dic_year)

    # 이름, 점수를 담은 딕셔너리를 key=점수, value=이름 으로 새로운 딕셔너리 만듬
    dic = dict([(dic_name.get(key), value) for key, value in dic_year.items()])
    print(dic)

    #2중 for문으로만 해결하는 방법
    for case in photo:
        sum = 0
        for k in range(len(case)):
            #이름이 dic에 없다면 넘어가고
            if case[k] not in dic:
                continue
            else:
            #있다면, key값을 찾아서 더 해줌
                sum += dic[case[k]]
        answer.append(sum)


    '''
    # photo 2차원 배열
    for case in photo:
        sum = 0
        # 2중 for문을 이용해 각각 1차원배열의 원소를 확인
        for r in range(len(case)):
            # dic 딕셔너리에서 이름이 같은게 있다면, 점수를 더해줌
            for k in dic.items():
                if case[r] == k[0]:
                    sum += k[1]
        answer.append(sum)
    
    '''




    return answer

name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
print(solution(name, yearning, photo))
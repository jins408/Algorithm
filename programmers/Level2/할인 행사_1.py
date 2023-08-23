def solution(want, number, discount):
    answer = 0

    # want와 number 배열의 길이가 같기때문에 상품별 갯수를 담을 딕셔너리 만들어줌
    dic = {}
    for i in range(len(want)):
        dic[want[i]] = number[i]
    print(dic)
    # 범위를 길이10만큼만 봐줄거라서 len(discount)-9를 해줌
    for i in range(len(discount)-9):
        temp_dic = {}
        # 10개씩 for문들 돌려서 그중 각 품목별로 몇개씩 있는지 새어 temp_dic 딕셔너리에 담음
        for j in range(i,10+i):
            d = temp_dic.get(discount[j])
            if d == None:
                temp_dic[discount[j]] = 1
            else:
                temp_dic[discount[j]] += 1
        # for문 한바퀴씩 돌고 끝났을때 시점을 비교하기 위해 flag값을 줌
        flag = True
        for key, value in temp_dic.items():
            if dic.get(key) == None or dic[key] < value:
                flag = False
                # 이 조건에 해당하다면 for문을 돌면서 원소값들은 각각 확인함
                #if key in dic and dic[key] >= value:
                #    continue
            #else:
                # 하나라도 dic딕셔너리가 일치하는게 없다면 flag를 False로해주고 break
                #flag = False
                #break
        # flag값이 True일 때만 answer+1 해준다.
        if flag == True:
            answer += 1

    return answer

want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
print(solution(want, number, discount))
def solution(want, number, discount):
    answer = 0

    # want와 number 배열의 길이가 같기때문에 상품별 갯수를 담을 딕셔너리 만들어줌
    dic = {}
    for i in range(len(want)):
        dic[want[i]] = number[i]
    print(dic)

    for i in range(len(discount)-9):
        temp_dic = {}
        for j in range(i,10+i):
            d = temp_dic.get(discount[j])
            if d == None:
                temp_dic[discount[j]] = 1
            else:
                temp_dic[discount[j]] += 1
        flag = True
        for key, value in temp_dic.items():
            if key in dic and dic[key] >= value:
                continue
            else:
                flag = False
                break
        if flag == True:
            answer += 1

    return answer

want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
print(solution(want, number, discount))
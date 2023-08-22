def solution(want, number, discount):
    answer = 0

    # want와 number 배열의 길이가 같기때문에 상품별 갯수를 담을 딕셔너리 만들어줌
    dic = {}
    for i in range(len(want)):
        dic[want[i]] = number[i]
    print(dic)

    # 열흘동안 원하는 품목과 개수가 일치하는걸 확인해야 하기 때문에 discount리스트를 10개씩 확인
    for i in range(len(discount)-9):
        # 품목이 같은게 있다면 value 값을 -1 해주기위해 dic를 copy한 딕셔너리 만듬(원본은 유지해야함)
        temp_dic = dic.copy()
        for j in range(i, i+10):
            # discount의 품목과 temp_dic 품목이 일하고 value값이 0이 아니면
            if discount[j] in temp_dic and temp_dic[discount[j]] != 0:
                # 해당 품목의 value 값을 -1 해준다.
                temp_dic[discount[j]] -= 1
            else:
                break
        # 품목당 해당하는 value가 모두 0이 되면 열훌동안 모두 정현이가 원하는 품목을 사는 것
        if sum(temp_dic.values()) == 0:
            answer += 1

    return answer

want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
print(solution(want, number, discount))
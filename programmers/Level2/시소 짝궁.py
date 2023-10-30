def solution(weights):
    answer = 0

    dic = {}
    # 딕셔너리에 weights의 각 숫자를 key로 저장하고 숫자의 개수를 value로 저장
    for i in weights:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    # 해당하는 키에 일치하는 값이 있는지 확인
    for i in dic:
        if dic[i] > 1:
            # 정수롤 +1 해주기위해 /2를 해줌
            answer += (dic[i]*(dic[i]-1)) / 2
        if i*2 in dic:
            answer += dic[i]*dic[2*i]
        if i*2/3 in dic:
            # 정수롤 +1 해주기위해 /3를 해줌
            answer += dic[i]*dic[i*2/3]
        if i*3/4 in dic:
            # 정수롤 +1 해주기위해 /4를 해줌
            answer += dic[i]*dic[i*3/4]


    return answer

weights = [100,180,360,100,270]
print(solution(weights))
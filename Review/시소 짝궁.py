def solution(weights):
    answer = 0

    dic = {}

    for i in weights:
        a = dic.get(i)
        if a == None:
            dic[i] = 1
        else:
            dic[i] += 1

    for i in dic:
        if dic[i] > 1:
            answer += (dic[i]*(dic[i]-1))/2
        if i*2 in dic:
            answer += dic[i]*dic[2*i]
        if i*2/3 in dic:
            answer += dic[i]*dic[i*2/3]
        if i*3/4 in dic:
            answer += dic[i]*dic[i*3/4]

    return answer

weights=[100, 180, 360, 100, 270]
print(solution(weights))
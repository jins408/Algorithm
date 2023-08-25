def solution(k, tangerine):
    answer = 0

    dic = {}
    for i in tangerine:
        d = dic.get(i)
        if d == None:
            dic[i] = 1
        else:
            dic[i] += 1
    print(dic)

    num = sorted(dic.values(), reverse=True)
    print(num)

    sum = 0
    cnt = 0
    for i in num:
        sum += i
        cnt += 1
        if sum >= k:
            answer = cnt
            break
    return answer

k = 6
tangerine =[1, 3, 2, 5, 4, 5, 2, 3]
print(solution(k, tangerine))
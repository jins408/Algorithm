def solution(topping):
    answer = 0

    first = set()
    seccond = {}
    for i in topping:
        d = seccond.get(i)
        if d == None:
            seccond[i] = 1
        else:
            seccond[i] += 1

    for j in topping:
        first.add(j)
        seccond[j] -= 1
        if seccond[j] == 0:
            del seccond[j]
        if len(first) == len(seccond):
            answer +=1

    return answer


topping = [1, 2, 1, 3, 1, 4, 1, 2]
print(solution(topping))
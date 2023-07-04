def solution(absolutes, signs):
    answer = 0

    for i in range(len(signs)):
        if signs[i] == False:
            absolutes[i] = -absolutes[i]

    for i in absolutes:
        answer += i

    return answer


absolutes = [1,2,3]
signs=[False, False, True]
print(solution(absolutes, signs))
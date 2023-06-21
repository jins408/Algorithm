def solution(n, numlist):
    answer = []

    for i in range(len(numlist)):
        if numlist[i]%n == 0:
            answer.append(numlist[i])

    return answer


n = 5
numlist=[1, 9, 3, 10, 13, 5]
print(solution(n, numlist))
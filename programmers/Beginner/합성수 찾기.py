def solution(n):
    answer = 0
    num = []
    for i in range(1, n + 2):
        if len(num) >= 3:
            answer += 1
        num = []
        for j in range(1, i+1):
            if i%j == 0:
                num.append(j)
    return answer


n = 10
print(solution(n))
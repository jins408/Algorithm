def solution(n):
    answer = 0
    for x in range(1, n+1):
        sum = 0
        for y in range(x, n+1):
            sum += y
            if sum == n:
                answer += 1
                break
            elif sum > n:
                break

    return answer


n = 15
print(solution(n))
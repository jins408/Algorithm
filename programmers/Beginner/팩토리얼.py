def solution(n):
    answer = 0

    num = 0
    factorial = 1
    while factorial <= n:
        num += 1
        factorial = factorial*num
        if factorial <= n:
            answer = num

    return answer

n = 3628800
print(solution(n))
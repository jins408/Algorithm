def solution(n, k):
    answer = 0

    service = (n // 10)
    k = k - service

    answer = (n * 12000) + (k * 2000)


    return answer

n = 10
k=3
print(solution(n,k))


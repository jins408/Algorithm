def solution(n):
    answer = 0

    a = 0
    i = 1       # 현재값
    index = 2   # 인덱스
    while i >= 0:
        a = i-a # 이전값
        i = i+a # 현재값+이전값
        index += 1
        if index == n:
            answer = i%1234567
            break

    return answer

n = 5
print(solution(n))
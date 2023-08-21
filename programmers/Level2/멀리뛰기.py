def solution(n):
    answer = 0

    # 피보나치수 문제..
    i = 0
    a = 1   # 현재값
    index = 1
    while a >= 0:
        i = a-i     # 이전값
        a = a+i     # 현재값+이전값
        index += 1
        if index == n:
            answer = a%1234567
            break
        if n == 1:
            answer = 1
            break

    return answer

n = 4
print(solution(n))
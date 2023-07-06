def solution(n):
    answer = 0

    num = []
    while n >= 0:
        b = n%3
        n //= 3
        num.append(b)
        if n < 1:
            break
    a = num[::-1]
    for i in range(len(a)):
        answer += a[i]*(3**i)

    return answer

n = 45
print(solution(n))
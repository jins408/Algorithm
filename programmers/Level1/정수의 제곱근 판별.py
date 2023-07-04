def solution(n):
    answer = 0

    i = 1
    while i <= n:
        if i**2 == n:
            return (i+1)**2
        else:
            i += 1
        if i > n:
            return -1

n= 121
print(solution(n))
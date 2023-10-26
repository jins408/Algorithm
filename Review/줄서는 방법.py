def factorial(n):
    if n > 1:
        return n*factorial(n-1)
    else:
        return 1

def solution(n, k):
    answer = []

    num = [i for i in range(1,n+1)]

    while n > 0:
        a = factorial(n-1)
        idx = k//a
        k = k%a
        if k == 0:
            answer.append(num.pop(idx-1))
        else:
            answer.append(num.pop(idx))
        n -=1
    return answer

n = 3
k = 5
print(solution(n,k))
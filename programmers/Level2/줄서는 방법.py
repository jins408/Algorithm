def my_factorial(n):
    if(n > 1):
        return n * my_factorial(n - 1)
    else:
        return 1


def solution(n, k):
    answer = []

    num_list = [i for i in range(1, n+1)]
    while (n != 0):
        s = my_factorial(n-1)
        idx = k//s
        k = k%s
        if k == 0:
            answer.append(num_list.pop(idx-1))
        else:
            answer.append(num_list.pop(idx))
        n -= 1
    return answer


n = 3
k = 5
print(solution(n,k))
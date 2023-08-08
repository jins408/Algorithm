n = 123

def solution(n):

    n_str = str(n)
    arr = []
    sum = 0
    for i in n_str:
        arr.append(i)
        sum += int(i)

    return sum

print(solution(n))
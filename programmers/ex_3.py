n=11873

def solution(n):

    n_str = str(n)
    arr = []
    for i in range(len(n_str)):
        arr.append(n_str[i])
        arr.sort()
        arr.reverse()

    return int(''.join(arr))
    # result = ''
    # for i in arr:
    #     result += i
    # return int(result)

print(solution(n))
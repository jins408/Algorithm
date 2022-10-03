numbers  = [1,2,3,4,6,7,8,0]


def solution(numbers):
    answer = 0

    arr = [-1]*10
    for n in numbers:
        arr[n] = n

    for i in range(len(arr)):
        if arr[i] == -1: answer += i


    # for i in range(10):
    #     if i not in numbers:
    #         answer += i
    return answer


print(solution(numbers))

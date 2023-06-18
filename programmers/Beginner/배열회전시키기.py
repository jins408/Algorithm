def solution(numbers, direction):
    answer = []

    arr = [0]*len(numbers)

    if direction == "right":
        arr[0] = numbers[-1]
        for i in range(1, len(numbers)):
            arr[i] = numbers[i-1]
        answer = arr
    else:
        for i in range(len(numbers)):
            if i == 0:
                arr[len(numbers) - 1] = numbers[i]
            else:
                arr[i - 1] = numbers[i]
        answer = arr


    return answer


numbers = [1, 2, 3]
direction = "right"

print(solution(numbers, direction))
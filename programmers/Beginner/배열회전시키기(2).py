def solution(numbers, direction):
    answer = []

    if direction == "right":
        answer.append(numbers[-1])
        answer += numbers[:-1]
    else:
        answer = numbers[1:]
        answer.append(numbers[0])


    return answer


numbers = [1, 2, 3]
direction = "left"

print(solution(numbers, direction))
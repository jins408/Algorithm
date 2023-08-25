def solution(numbers, target):
    answer = 0

    queue = [[0,0]]

    while len(queue) > 0:
        index, a = queue.pop()

        if index < len(numbers):
            queue.append([index+1, a+numbers[index]])
            queue.append([index+1, a-numbers[index]])

        if index == len(numbers):
            if a == target:
                answer+=1
    return answer

numbers =[4, 1, 2, 1]
target = 4
print(solution(numbers, target))
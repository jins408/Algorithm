def solution(numbers):

    answer = [-1]*len(numbers)
    stack = []

    for idx, num in enumerate(numbers):
        print(idx, num)
        while stack and numbers[stack[-1]] < num:
            answer[stack.pop()] = num
        stack.append(idx)


    return answer

numbers = [9, 1, 5, 3, 6, 2]
print(solution(numbers))
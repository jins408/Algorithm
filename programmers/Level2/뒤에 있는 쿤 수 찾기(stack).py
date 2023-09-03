
def solution(numbers):
    answer = [-1]*len(numbers)

    stack = []

    for i, num in enumerate(numbers):
        while stack and numbers[stack[-1]] < num:
            answer[stack.pop()] = num
        stack.append(i)

    return answer

numbers = [9, 1, 5, 3, 6, 2]
    #[2, 3, 3, 5]
    #[9, 1, 5, 3, 6, 2]
print(solution(numbers))
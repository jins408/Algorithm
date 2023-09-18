def solution(number, k):
    answer = ''

    stack = []

    for num in number:

        while stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)

    answer = ''.join(stack)

    return answer

number = "1924"
k = 2
print(solution(number, k))
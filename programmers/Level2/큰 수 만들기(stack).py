def solution(number, k):
    answer = ''

    stack = []

    for n in number:
        while stack and stack[-1] < n:
            stack.pop()
            k -= 1
        stack.append(n)

    answer = ''.join(stack)

    return answer

number = "1924"
k = 2
print(solution(number, k))
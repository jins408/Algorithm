def solution(order):
    answer = 0

    stack = []

    for i in range(len(order)):
        stack.append(i+1)

        while stack and stack[-1] == order[answer]:
            answer += 1
            stack.pop()

    return answer

order = [4, 3, 1, 2, 5]
print(solution(order))
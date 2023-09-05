def solution(prices):
    answer = [-1]*len(prices)
    stack = []

    for idx, num in enumerate(prices):
        while stack and prices[stack[-1]] > num:
            j = stack.pop()
            answer[j] = idx-j
        stack.append(idx)
    print(answer)
    print(stack)

    for i in stack:
        answer[i] = len(prices)-i-1

    return answer

prices = [1, 2, 3, 2, 3]
print(solution(prices))
def solution(prices):

    answer = [-1]*len(prices)
    stack = []

    for idx, num in enumerate(prices):
        # stack에 prices인덱스 값을 넣어준다.
        # 현재값 보디 이전값이 더 크면 answer 인덱스 자리에 현재인덱스-이전인덱스 값을 넣어준다.
        while stack and prices[stack[-1]] > num:
            j = stack.pop()
            answer[j] = idx-j
        # 현재값보다 이전값이 크지 않으면 스택에 인덱스값을 넣어준다.
        stack.append(idx)
    print(answer)
    print(stack)
    # 스택에 인덱스값이 저장되어 있으므로
    for i in stack:
        # answer에 해당하는 인덱스값에 계산하여 값을 넣어준다.
        answer[i] = len(prices)-i-1

    return answer

prices = [1, 2, 3, 2, 3]
print(solution(prices))
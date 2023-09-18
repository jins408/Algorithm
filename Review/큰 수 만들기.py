def solution(number, k):
    answer = ''

    stack = []

    for num in number:

        while k>0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)

    answer = ''.join(stack[:len(stack)-k])
    # print(''.join(stack)) -> 마지막 테스트케이스 실패

    return answer

number = "1231234"
k = 3
print(solution(number, k))
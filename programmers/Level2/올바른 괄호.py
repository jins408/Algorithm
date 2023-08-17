def solution(s):
    answer = True

    # Level1 햄버거 만들기(stack문제) 비슷한 문제
    stack = []
    for i in s:
        stack.append(i)
        if stack[-2:] == ['(',')']:
            for _ in range(2):
                stack.pop()

    if stack == []:
        return True
    else:
        return False

s=")()("
    #"(())()"
    #"()()"
print(solution(s))
def divide(p):
    open_p=0
    close_p=0

    for i in range(len(p)):
        if p[i] == "(":
            open_p +=1
        else:
            close_p +=1
        if open_p == close_p:
            return p[:i+1], p[i+1:]

def check(u):
    stack = []

    for j in u:
        if j == "(":
            stack.append(j)
        else:
            if not stack:
                return False
            stack.pop()
    return True

def solution(p):
    answer = ''

    # 과정 1
    if p == "":
        return ""

    # 과정 2
    u,v = divide(p)

    # 과정 3
    if check(u):
        return u+solution(v)
    else:
        answer += "("
        answer += solution(v)
        answer += ")"

        for p in u[1:len(p)-1]:
            if p == "(":
                answer += ")"
            else:
                answer += "("
    return answer

p = "(()())()"
print(solution(p))

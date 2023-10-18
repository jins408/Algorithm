# 문자열 p를 u, v로 분리하는 함수
def divide(p):
    open_p = 0
    close_p = 0

    for i in range(len(p)):
        if p[i] == "(":
            open_p += 1
        else:
            close_p += 1

        if open_p == close_p:
            return p[:i+1], p[i+1:]

# 문자열 u가 올바른 괄호 문자열인지 확인하는 함수
def check(u):
    stack = []

    for p in u:
        if p == "(":
            stack.append(p)
        else:
            if not stack:
                return False
            stack.pop()
    return True

def solution(p):
    answer = ''

    # 과정 1 : p가 빈 문자열이면 빈 문자열을 반환한다.
    if p == "":
        return ""

    # 과정 2 : "균형잡힌 괄호 문자열" u, v로 분리
    # 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있다.
    u, v = divide(p)

    # 과정 3 : 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행
    if check(u):
        # 수행한 결과 문자열을 u에 이어 붙인 후 반환
        return u+solution(v)
    # 과정 4
    else:
        # 문자열 u가 "올바른 괄호 문자열"이 아니면
        answer += "("   # 빈 문자열에 첫 번째 문자로 '('를 붙인다.
        answer += solution(v) # 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙인다.
        answer += ")"   # ')'를 다시 붙입니다.

        # u의 첫 번째와 마지막 문자를 제거하고
        for p in u[1:len(u)-1]:
            # 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙인다.
            if p == "(":
                answer += ")"
            else:
                answer += "("

    # 생성된 문자열을 반환
    return answer

p = "()))((()"
print(solution(p))
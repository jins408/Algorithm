def solution(n):
    ans = 0

    # 10진수인 n을 2진수를 바꾸고
    num = bin(n)[2:]
    # 2진수의 1의 개수 만큼이 점프를 한 횟수가 된다.
    ans = num.count('1')

    return ans

n = 5
print(solution(n))
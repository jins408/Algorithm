def solution(balls, share):
    answer = 0

    num = 1
    for i in range(1, balls+1):
        num *= i

    num2 = balls-share

    s = 1
    for i in range(1,num2+1):
        s *= i
    b = 1
    for i in range(1, share+1):
        b *= i

    answer = num//(s*b)

    return answer


balls = 5
share = 3
print(solution(balls, share))
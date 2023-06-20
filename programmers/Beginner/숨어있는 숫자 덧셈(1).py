def solution(my_string):
    answer = 0

    num = '123456789'
    sum = []
    for i in my_string:
        if i in num:
            sum.append(i)

    result = list(map(int, sum))

    for i in range(len(result)):
        answer += result[i]

    return answer

my_stirng="aAb1B2cC34oOp"
print(solution(my_stirng))
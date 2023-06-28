import math

def arr(number, num, total):
    answer = []
    a = 0
    while True:
        sum = 0
        for i in range(a, a + num):
            sum += number[i]
            answer.append(number[i])
        if sum == total:
            break
        else:
            answer = []
        a += 1

    return sorted(answer)


def solution(num, total):
    number = []
    if total == 0:
        end = round(num/2)
        print(end)
        for i in range(end):
            number.append(i)
        for i in range(end):
            number.append(-i)
        arr(number, num, total)
        print(number)
    elif num == total:
        end = math.ceil(num/2)
        print(end)
        for i in range(end+1):
            number.append(i)
        for i in range(end+1):
            number.append(-i)
        arr(number, num, total)
    else:
        if num > 100 or total > 1000:
            return 0
        for i in range(1, num + total + 1):
            number.append(i)
        arr(number, num, total)

    return arr(number,num, total)

num = 100
total = 1
print(solution(num,total))

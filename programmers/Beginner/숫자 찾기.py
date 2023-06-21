def solution(num, k):
    answer = 0

    number = str(num)
    for i in number:
        if i in str(k):
           answer = number.index(i)+1
        if str(k) not in number:
            answer = -1

    return answer

num = 232443
k = 4

print(solution(num, k))
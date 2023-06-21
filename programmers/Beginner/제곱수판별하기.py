def solution(n):
    answer = 0

    num = 2
    while num <= n:
        a = num*num
        if a != n:
            num+= 1
            if a >= n:
                answer = 2
        elif a == n :
            answer = 1
            break


    return answer


n = 144
print(solution(n))

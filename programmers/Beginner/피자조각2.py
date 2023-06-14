def solution(n):

    '''
    answer = 1
    while 1:
        if (6 * answer) % n == 0:
            return answer
        answer += 1
    '''

    #for문을 이용한 경우
    answer = 0 
    num = 0
    if n%6 != 0:
        for i in range(1, n+1):
            num = 6 * i
            if num % n == 0:
                answer = i
                break
    else:
        answer = n//6

    return answer

n = 10
print(solution(n))






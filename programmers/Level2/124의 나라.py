def solution(n):
    answer = ''

    while n:
        a = n%3
        # 나머지가 0이면 3의 배수이기 때문에
        if not a:
            # 3의 배수인 경우 나머지를 4로 바꿔주고
            a = 4
            # 몫에대해서 1을 빼준다.
            n -= 1
        answer += str(a)
        # 다시 3의로 나눠주길 반복
        n//=3

        # 진법 변환이기 때문에 거꾸로 표시해 줘야함
    return answer[::-1]


n = 4
print(solution(n))
def solution(n):
    answer = []

    num = 2 #소수는 2부터 시작이니까 일단 2로 먼저 나눠줌
    # n//num을 해줌으로써 n값은 계속 줄어들게 됨, n은 n=+1해주기 때문에 계속 증가 -> num이 n보다 <= 때까지 while문 돌림
    while num <= n:
        if n%num == 0:
            # 나눈 나머지가 0이면 answer에 추가
            answer.append(num)
            # 나눈 몫으로 또 나눠줘야 하기때문에 n//num을 해줌
            n = n//num
        else:
            # 나머지가 0이 안되면 num숫자를 +1 해줌(소수를 찾는 과정)
            num+=1

    return list(set(answer))

n= 420
print(solution(n))
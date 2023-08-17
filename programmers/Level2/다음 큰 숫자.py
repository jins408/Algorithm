def solution(n):
    answer = 0

    # n을 2진수로 만들고
    num = bin(n)
    num = num[2:]
    # 1의 개수를 카운트
    cnt_num = num.count('1')

    while n >=0:
        # 다음큰수는 n보다 무조건 큰수이기 때문에 n+1해준 숫자부터 비교
        n = n+1
        # 2진수로 바꾸고
        a = bin(n)
        a = a[2:]
        # n의 1의 개수가 똑같은 숫자가 나오면 값을 받음(제일 작은수를 찾는것이기 때문에 1의 개수가 동일한 숫자가 제일 작은 숫자)
        if a.count('1') == cnt_num:
            answer = a
            break
    # 2진수를 다시 10진수롤 바꿔주기
    return int(answer,2) 

n = 78
print(solution(n))
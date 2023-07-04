#1-1. 입력된 수가 짝수라면 2로 나눕니다.
#1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
#2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다.

def solution(num):
    answer = 0

    cnt = 0
    while cnt >= 0:
        if num == 1:
            return 0
        if num%2 == 0:
            num//=2
            cnt += 1
        elif num%2 != 0:
            num = (num*3)+1
            cnt += 1
        if num == 1:
            return cnt
        elif cnt > 500:
            return -1


num = 1
print(solution(num))
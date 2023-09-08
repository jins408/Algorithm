def solution(n):
    answer = 0

    a = 1   # 첫번재 값 (이전값)
    i = 2   # 두번째 값(현재값)
    idx = 2
    while n >= 0:
        a = i-a
        # 효율성 시간초과 나서 더해 줄때 같이 값을 나눠준다.
        i = (i+a)%1000000007
        idx += 1
        if idx == n:
            return i
n = 4
print(solution(n))
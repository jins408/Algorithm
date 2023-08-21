import math
def solution(n,a,b):
    answer = 0

    while True:
        # ceil은 주어진 숫자와 같은 정수 또는 주어진 숫자보다 큰 가장 가까운 정수를 return
        # round는 함수로 소수점 첫째자리 수를 기준으로 반올림을 해줌
        a = math.ceil(a/2) # ceil(2.4)-> 3 round(2.4) -> 2
        b = math.ceil(b/2)
        answer += 1
        if a == b or a == 0 or b == 0:
            break

    return answer

n = 8
a = 4
b = 5
print(solution(n,a,b))
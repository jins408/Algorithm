# 최대공약수 구하는 유클리드 호제법
def gcd_get(a, b):
    if b > a:
        a, b = b, a
    while True:
        # 나머지가 0이 나왔을 때, 나눠준 수가 바로 최대공약수
        if b == 0:
            break
        a, b = b, a%b
    return a

def solution(a, b):

    # 최대공약수 구하기
    gcd = gcd_get(a, b)

    #a = a//gcd 분자
    b = b//gcd #분모

    while b % 2 == 0:
        b //= 2  # 2로 나누어 떨어지면 2로 나눈 값 넣기
    while b % 5 == 0:
        b //= 5  # 5로 나누어 떨어지면 5로 나눈 값 넣기

    if b == 1:
        return 1
    else:
        return 2  # 다 나누어 떨어지면 1,아니면 2넣기


a = 12
b = 6
print(solution(a, b))
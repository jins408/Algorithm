# 최대공약수
def gcd(a,b):
    while b > 0:
        a, b = b, a%b
    return a

#최대공배수
def lcm(a,b):
    result = a*b//gcd(a,b)
    return result

def solution(n, m):
    answer = []

    get_gcd = gcd(n,m)
    get_lcm = lcm(n,m)

    answer = [get_gcd, get_lcm]

    return answer

n = 3
m = 12
print(solution(n, m))
# 최대공약수 구하는 유클리드 호제법
def gcd(a,b):
    while b>0:
        a, b = b, a%b
    return a

# 최소공배수 구하는 유클리드호제법
def lcm(a,b):
    return (a*b)//gcd(a,b)

def solution(arr):
    answer = 0
    # arr 리스트에서 끝에서부터 2개씩 뽑아서 그 숫자들의 최대공약수와 최소공배수를 구해 arr에 다시 추가해줌
    # arr 리스트에 남은 하나의 수가 답
    while len(arr) >= 2:
        a = arr.pop()
        b = arr.pop()
        arr.append(lcm(a, b))

    answer = arr[0]

    return answer

arr = [2,6,8,14]
    #[2,6,8,14]
print(solution(arr))
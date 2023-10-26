# 최대공약수
def gcd_(a, b):
    while b > 0:
        a,b = b, a%b
    return a

# N개의 최대공약수 구하기
def gcd_N(arr):
    gcd = arr[0]
    for i in arr:
        gcd = gcd_(gcd, i)
    return gcd

# 조건에 따라서 나눠어 떨어지는이 아닌지 확인
def div(num,array):
    for i in array:
        if i%num == 0:
            return False
    return True

def solution(arrayA, arrayB):
    answer = 0

    num_a = gcd_N(arrayA)
    num_b = gcd_N(arrayB)

    # 첫 번째 조건 div가 True일때만 확인
    if div(num_a, arrayB):
        # 둘중에 큰 값을 찾아 줘야 하므로 max로 큰값을 answer에 넣어주면서 큰 양수 값을 찾음
        answer = max(answer, num_a)

    # 두 번째 조건
    if div(num_b, arrayA):
        answer = max(answer, num_b)

    return answer

arrayA= [10, 17]
arrayB= [5, 20]
print(solution(arrayA, arrayB))
#[10, 17], [5, 20]
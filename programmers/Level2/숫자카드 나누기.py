def gcd_(a, b):
    while b > 0:
        a,b = b, a%b
    return a

def gcd_N(arr):
    gcd = arr[0]
    for i in arr:
        gcd = gcd_(gcd, i)
    return gcd

def div(num,array):
    for i in array:
        if i%num == 0:
            return False
    return True

def solution(arrayA, arrayB):
    answer = 0

    num_a = gcd_N(arrayA)
    num_b = gcd_N(arrayB)

    # 첫 번째 조건
    if div(num_a, arrayB):
        answer = max(answer, num_a)

    # 두 번째 조건
    if div(num_b, arrayA):
        answer = max(answer, num_b)

    return answer

arrayA= [10, 17]
arrayB= [5, 20]
print(solution(arrayA, arrayB))
#[10, 17], [5, 20]
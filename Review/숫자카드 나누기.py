def gcd_(a, b):
    while b > 0:
        a, b = b, a%b
    return a

def gcd_N(arr):
    gcd = arr[0]

    for i in arr:
        gcd = gcd_(gcd, i)

    return gcd

def divi(num, array):

    for i in array:
        if i%num == 0:
            return False
    return True


def solution(arrayA, arrayB):
    answer = 0

    num_a = gcd_N(arrayA)
    num_b = gcd_N(arrayB)

    if divi(num_a, arrayB):
        answer = max(answer, num_a)

    if divi(num_b, arrayB):
        answer = max(answer, num_b)

    return answer

arrayA= [14, 35, 119]
arrayB= [18, 30, 102]
print(solution(arrayA, arrayB))
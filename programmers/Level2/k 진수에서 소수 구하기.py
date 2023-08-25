import math
def bin_(x):
    if x > 1:
        for i in range(2,int(math.sqrt(x))+1):
            if x%i == 0:
                return False
        return True

def fun(n,k):

    bin = ''
    while k >= 0:
        a = n%k
        n //= k
        bin += str(a)
        if n == 0:
            return bin[::-1]

def solution(n, k):
    answer = 0

    # 진법 변환 함수
    fun(n,k)
    get_fun = fun(n,k)
    #print(get_fun)
    num = get_fun.split('0')

    for i in range(len(num)):
        if num[i] == "":
            continue
        if bin_(int(num[i])):
            answer+=1

    return answer

n = 437674
    #110011
    #437674
k = 3
    #10
    #3
print(solution(n , k))
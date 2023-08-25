import math
def bin_(x):
    # 1은 소수로 판별 안하기때문에 1이상인 값만 확인
    if x > 1:
        # 소수인지 아닌지 판별
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

    # 변환된 진법을 0을 제외한 값으로 바꾸기
    num = get_fun.split('0')
    #['211', '2', '1', '1', '11']

    # for문을 돌면서 해당 값이 소수인지 아닌지 판별하기
    for i in range(len(num)):
        if num[i] == "":
            continue
        # 소수인지 판별해주는 함수
        if bin_(int(num[i])):
            # 소수가 맞다면 answer +1 해줌
            answer+=1

    return answer

n = 437674
    #110011
    #437674
k = 3
    #10
    #3
print(solution(n , k))
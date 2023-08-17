def solution(brown, yellow):
    answer = []

    n = brown+yellow
    num = []
    # n의 약수의 개수 구하기
    for i in range(1, n//2+1):
        if n%i == 0:
            num.append(i)
    num.append(n)
    print(num)

    x = len(num)
    i = 0
    while n >= 0:
        # (x-2)(y-2) == yellow와 같아야 한다.
        a = (num[i]-2)*(num[x-1]-2)
        i+=1 # 첫번째 인덱스(+1)
        x-=1 # 마지막 인덱스(-1)
        if a == yellow:
            answer.append(num[x])
            answer.append(num[i-1])
            break

    return answer

brown = 24
yellow = 24
print(solution(brown, yellow))
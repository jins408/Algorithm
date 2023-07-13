def solution(n):
    num=set(range(2,n+1)) # {2,3,4,5,6,7,8,9,10}

    for i in range(2,n+1):
        # num 범위에 i(해당하는 숫자)가 있다면
        if i in num:
            # set(range(2*i,n+1,i)) 범위에 해당하는 숫자들을 num에서 지워줌
            # i=2일때 {4,6,8,10} -> 이 숫자들을 num에서 제거
            num-=set(range(2*i,n+1,i))
    return len(num)

n = 10
print(solution(n))
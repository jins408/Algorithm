def fun(n,num):
    bin = ''

    while num != 0:
        a = num % n
        num //= n
        # 10~15까지는 "ABCDEF"로 나타낸다는 조건이 있어서 나머지(a)%10을 한 값으로 "ABCDEF"문자열에 인덱스를 찾아서 bin에 더해줌
        if 10 <= a <= 15:
            bin += "ABCDEF"[a % 10]
        else:
            bin += str(a)

    return bin[::-1]

def solution(n, t, m, p):
    answer = ''
    # fun함수에서 while문이 num!=0이 아닐때이므로 temp에 0을 넣고 시작한다.
    temp = '0'

    for i in range(t*m):
        fun(n,i)
        # n진법 변환 함수
        get_fun = fun(n,i)
        temp += get_fun
    print(temp)

    for i in range(len(temp)):
        answer += temp[p-1]
        # 내 순서가 p
        # -> p+m(참여인원수)하면 내 차례가 다시 돌아옴
        p+=m
        if i == t-1: # i랑 갯수가 같아지면 break(i가 0부터라 t-1해줌)
            break

    return answer

n=16
t=16
m=2
p=1
print(solution(n,t,m,p))
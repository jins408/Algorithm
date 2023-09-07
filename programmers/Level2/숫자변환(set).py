def solution(x, y, n):
    answer = 0

    num = set() # 계산 한 값들을 담을 집합(중복제거)
    num.add(x)  # 처음 x값을 넣어주고

    while num:
        # num 집함에 y랑 동일한 값이 있다면 answer을 return해준다.
        if y in num:
            return answer

        # 계산할 값을 답을 집합
        nxt = set() # 초기화 시켜주고 현재 num안에 있는 원소를 하나하나 계산해 준다.
        # num{15,20,30}이라면, -> 15+5,15*2,15*30 20+5,20*2,20*3 30+5,30*2,30*3 -> 어차피 중복된 값은 들어가지 않기때문에
        for i in num:
            if i+n <= y:
                nxt.add(i+n)
            if i*2 <= y:
                nxt.add(i*2)
            if i*3 <= y:
                nxt.add(i*3)
        num = nxt   # num집합을 계산된 값으로 바꿔준다.
        answer += 1

    return -1

x = 10
y = 40
n = 5
print(solution(x, y, n))
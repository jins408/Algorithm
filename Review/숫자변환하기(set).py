def solution(x, y, n):
    answer = 0

    num = set()
    num.add(x)

    while num:

        if y in num:
            return answer

        nxt = set()
        for i in num:
            if i+n <= y:
                nxt.add(i+n)
            if i*2 <= y:
                nxt.add(i*2)
            if i*3 <= y:
                nxt.add(i*3)
        num = nxt
        answer +=1

    return answer

x = 10
y = 40
n = 5
print(solution(x,y,n))
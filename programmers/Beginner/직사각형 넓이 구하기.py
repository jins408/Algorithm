def solution(dots):
    answer = 0

    x = []
    y = []
    for i in range(len(dots)):
        a = dots[i][0]
        x.append(a)
        b = dots[i][1]
        y.append(b)

    x1 = max(x)-min(x)
    y1 = max(y)-min(y)
    answer = x1*y1

    return abs(answer)


dots=[[1, 1], [2, 1], [2, 2], [1, 2]]
print(solution(dots))
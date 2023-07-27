def solution(n, lost, reserve):
    answer = 0

    lost = sorted(lost)
    reserve = sorted(reserve)
    s = []
    b = []
    for i in range(1,n+1):
        if i not in lost:
            s.append(i)
            b.append(i)

    for i in range(len(lost)):
        for j in reserve:
            if j-1 < lost[i] <= j+1:
                s.append(lost[i])
            if j-1 >= lost[i] > j+1:
                b.append(lost[i])
    s = list(set(s))
    b = list(set(b))
    print(s)
    print(b)
    if len(s) < len(b):
        answer = len(b)
    else:
        answer = len(s)


    return answer

n = 24
lost = [12, 13, 16, 17, 19, 20, 21, 22]
reserve = [1,22, 16, 18, 9, 10]
    #[1,3,5]
print(solution(n,lost,reserve))
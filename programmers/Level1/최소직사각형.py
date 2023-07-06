def solution(sizes):
    answer = 0

    a = [] # 큰값
    b = [] # 작은값

    for i in range(len(sizes)):
        # 큰값 들만 따로 a배열에 저장
        if sizes[i][0] >= sizes[i][1]:
            a.append(sizes[i][0])
            b.append(sizes[i][1])
        # 작은 값들만 따로 b배열에 저장
        else:
            a.append(sizes[i][1])
            b.append(sizes[i][0])


    answer = max(a)*max(b)

    return answer


sizes=[[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(sizes))
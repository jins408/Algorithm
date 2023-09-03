def solution(land):
    answer = []

    arr = [[0 for _ in range(4)] for _ in range(len(land))]
    print(arr)

    for i in range(len(land)):

        if i == 0:
            arr[0] = land[0]
            continue

        for j in range(4):
            maxValue = -1
            for k in range(4):
                if j != k:
                    maxValue = max(maxValue, arr[i-1][k])
                    arr[i][j] = land[i][j]+maxValue


    return max(arr[-1])

land=[[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land))
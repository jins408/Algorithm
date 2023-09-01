def solution(land):
    answer = []

    dp = [[0 for _ in range(4)] for _ in range(len(land))]
    print(dp)
    for i in range(len(land)):
        # 초기 성분 입력
        if i == 0:
            dp[0] = land[0]
            continue
        # DP 테이블 업데이트
        for j in range(4):
            maxValue = -1
            for k in range(4):
                if k != j:
                    maxValue = max(maxValue, dp[i - 1][k])
                    dp[i][j] = land[i][j] + maxValue
            #dp[i][j] = land[i][j] + max([dp[i - 1][k] for k in range(4) if k != j])
    print(dp)
    return max(dp[-1])
#[[1, 2, 3, 5], [10, 11, 12, 11], [15, 14, 13, 13]]
#[[1, 2, 3, 5], [10, 11, 12, 11], [16, 15, 13, 13]]
land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land))
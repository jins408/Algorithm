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
            for k in range(4):
                if k != j:
                    a = max([dp[i - 1][k]])
                    dp[i][j] = land[i][j] + a
            #dp[i][j] = land[i][j] + max([dp[i - 1][k] for k in range(4) if k != j])

    return max(dp[-1])

land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land))
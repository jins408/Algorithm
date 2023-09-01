def solution(land):
    answer = []

    dp = [[0 for _ in range(4)] for _ in range(len(land))]
    print(dp)
    for i in range(len(land)):
        # 초기 성분 입력
        if i == 0:
            # dp 첫번째 행을 land 첫번째 행과 동일하게 만들어줘서 값을 계속 더할 수 있게끔 만든다.
            dp[0] = land[0]
            continue
        # DP 테이블 업데이트
        for j in range(4):
            maxValue = -1
            for k in range(4):
                # 바로 아래있는 값은 값은 더해주지 않기 위해서 k != j 일때만 더해준다
                # 같은 열을 반복해서 밟을 수 없다는 조건이 있기 때문에
                if k != j:
                    # 더 한 값들 중에서 최대값을 찾아준다
                    maxValue = max(maxValue, dp[i - 1][k])
                    dp[i][j] = land[i][j] + maxValue
            #dp[i][j] = land[i][j] + max([dp[i - 1][k] for k in range(4) if k != j])
    print(dp)
            # 계속 더 한 값을 dp에 넣어주기 때문에, 제일 마지막 행에서 제일 큰 값을 가져오면 정답
    return max(dp[-1])
#[[1, 2, 3, 5], [10, 11, 12, 11], [15, 14, 13, 13]]
#[[1, 2, 3, 5], [10, 11, 12, 11], [16, 15, 13, 13]]
land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land))
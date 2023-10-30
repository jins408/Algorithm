# dp문제
def solution(board):
    answer = 0

    n = len(board)
    m = len(board[0])
    dp = [[0]*m for _ in range(n)]
    # dp의 첫번째 행값을 채워준다.
    dp[0] = board[0]

    # dp 첫번째 열의 값을 채워준다. -> dp값을 확인하면서 계산해주기 위해
    for i in range(1, n):
        dp[i][0] = board[i][0]

    for i in range(1, n):
        for j in range(1, m):
            # board[i][j] == 1 일때만 왼쪽,위,왼쪽대각선위를 확인하면서 최소값에 +1을해준다.
            # board[i][j] == 0 이면 확인하지 않고 그냥 0이다.
            if board[i][j] == 1:
                # 왼쬑위대각선, 위, 왼쪽 -> 확인해 주면 된다.
                dp[i][j] = min(dp[i-1][j-1],dp[i-1][j], dp[i][j-1])+1

    for i in range(n):
        temp = max(dp[i])
        # dp[i]한 행에서 최대값을 찾아가면서
        # answer에 최대값을 갱신해준다.
        answer = max(answer, temp)

        # 정사각형의 넓이를 구한는 문제이므로 최대값에서 **2를 해준다.
    return answer**2

board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
print(solution(board))
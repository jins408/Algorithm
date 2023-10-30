# dp문제
def solution(board):
    answer = 0

    n = len(board)
    m = len(board[0])
    dp = [[0]*m for _ in range(n)]
    dp[0] = board[0]

    for i in range(1, n):
        dp[i][0] = board[i][0]

    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 1:
                # 왼쬑위대각선, 위, 왼쪽 -> 확인해 주면 된다.
                dp[i][j] = min(dp[i-1][j-1],dp[i-1][j], dp[i][j-1])+1

    for i in range(n):
        temp = max(dp[i])
        answer = max(answer, temp)

    return answer**2

board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
print(solution(board))
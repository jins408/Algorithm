def solution(board):
    answer = 0

    dr=[-1,1,0,0,-1,-1,1,1]
    dc=[0,0,-1,1,-1,1,-1,1]

    visited = [[0 for i in range(len(board))] for j in range(len(board))]

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                for x in range(8):
                    visited[i][j] = 1
                    nr, nc = i, j
                    nr += dr[x]
                    nc += dc[x]
                    if 0<= nr < len(visited) and 0<= nc< len(visited) and visited[nr][nc]==0:
                        visited[nr][nc] = 1

    for i in range(len(visited)):
        for j in range(len(visited)):
            if visited[i][j] == 0:
                answer+=1

    return answer


board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
print(solution(board))
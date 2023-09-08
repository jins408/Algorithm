def solution(m, n, board):
    answer = 0

    board = [list(board[i]) for i in range(m)]

    visited = set()

    while True:
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == []:
                    continue
                if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                    visited.add((i,j))
                    visited.add((i, j+1))
                    visited.add((i+1,j))
                    visited.add((i+1,j+1))

        if len(visited) > 0 :
            answer += len(visited)
            for i,j in visited:
                board[i][j] = []
            visited = set()
        else:
            return answer

        while True:
            moved = 0
            for i in range(m-1):
                for j in range(n):
                    if board[i][j] and board[i+1][j] == []:
                        board[i+1][j] = board[i][j]
                        board[i][j] = []
                        moved = 1
            if moved == 0:
                break

m= 4
n= 5
board =["CCBDE", "AAADE", "AAABF", "CCBBF"]
print(solution(m,n,board))
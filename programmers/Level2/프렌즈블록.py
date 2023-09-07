def solution(m, n, board):
    answer = 0

    board = [list(board[i]) for i in range(m)]


    target = set()
    while True:
        #지울거 찾기

        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == []:
                    continue
                if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                    target.add((i,j)),
                    target.add((i,j+1)),
                    target.add((i+1,j)),
                    target.add((i+1,j+1))

        # target이 존재하면 tartget의 길이만큼 더해주고 블록을 지움
        if len(target) > 0:
            answer += len(target)
            for i , j in target:
                board[i][j] = []
            target = set()
        else:
            return answer

        # 블록을 아래로 당겨준다
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

m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
print(solution(m,n,board))
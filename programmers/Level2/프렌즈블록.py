def solution(m, n, board):
    answer = 0

    # 1차원 문자열 리스트 -> char형태로 하나하나 2차원 리스트로 바꿔준다.
    board = [list(board[i]) for i in range(m)]

    # 중복죄표를 제거하기 위해 set()으로 만들어줌
    target = set()
    while True:
        #지울거 찾기 2*2형태로 같은 문자가 있는지 확인해주면 되므로 m-1,n-1 범위로 준다.
        for i in range(m-1):
            for j in range(n-1):
                # 나중에 target에 해당하는 좌표 값들을 []처리해주기 때문에 []이면 넘어가게 조건을 준다.
                if board[i][j] == []:
                    continue
                # 2*2형태에 같은 문자가 있다면, target에 넣어준다.
                if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                    target.add((i,j)),      # 현재좌표
                    target.add((i,j+1)),    # 오른쪽
                    target.add((i+1,j)),    # 아래
                    target.add((i+1,j+1))   # 오른쪽 대각선 아래

        # target이 존재하면 tartget의 길이만큼 더해주고
        if len(target) > 0:
            answer += len(target)
            # target 집합에 있는 좌표들은 전부 []로 바꿔준다.
            for i, j in target:
                board[i][j] = []
            target = set() # 다시 초기화 시켜줌
        else:
            # target이 빈값이라면 answer을 최종적으로 return해준다.
            return answer

        # 블록을 아래로 당겨준다
        while True:
            moved = 0
            # 아래로만 이동하기 때문에 m-1로 범위를 잡아준다.
            for i in range(m-1):
                for j in range(n):
                    # 현재값에서 아래로 이동한 곳이 []이라면
                    if board[i][j] and board[i+1][j] == []:
                        # 아래 이동한 자리에 현재값을 넣어주고
                        board[i+1][j] = board[i][j]
                        # 현재값은 [] 처리 (이동했기때문에 빈값으로 바꿔준다)
                        board[i][j] = []
                        moved = 1
            # 더이상 이동할 곳이 없다면 break
            if moved == 0:
                break

m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
print(solution(m,n,board))
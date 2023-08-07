def solution(board, moves):
    answer = 0
    temp = [] # 크레인을 통해 쌓은 숫자를 담을 배열
    n = len(board) # board의 크기
    for i in moves:
        for r in range(n):
            for c in range(n):
                # board[c][r] 크레인이 위에서부터 시작해서 가로가 아닌 세로로 봐줌
                # 0은 제외이기때문에 0이 아니고 크레인 숫자와 동일한 것이 있다면, temp 배열에 넣어주고 board[c][r]=0으로 만들어줌(중복방지위해서)
                if board[c][r] != 0 and i == r+1:
                    temp.append(board[c][r])
                    board[c][r] = 0
                    break
    print(temp)

    # 연속되는 두 수를 찾기위한 배열
    list_dup = []
    for i in range(0, len(temp)):
        list_dup.append(temp[i])  # list_dup에 temp를 순서대로 쌓는다.
        if len(list_dup) > 1:
            if list_dup[-1] == list_dup[-2]:  # 쌓이는 마지막행과 마지막 이전행끼리 같으면
                list_dup.pop(-1)
                list_dup.pop(-1)
                answer += 2  #  같은번호를 2개 이상일때 제거해주기 때문에 +2를 해줌


    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))
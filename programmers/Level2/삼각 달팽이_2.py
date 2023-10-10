def solution(n):
    answer = []

    # 삼각형모양이라 아래, 오른쪽, 왼쪽대각선위 방향 확인
    dr = [0,1,-1]
    dc = [1,0,-1]

    # 방문할 곳을 0의로 채워서 만든 배열
    visited = [[0]*n for _ in range(n)]

    # angle = 이동할 방향의 좌표(dr,dc기준)
    r,c,angle = 0,0,0
    cnt = 1

    # 전체크키(n=4)일때 16이지만, 1~10까지만 나와야 하므로 size를 계산해줌
    size = (n+1)*n//2

    while cnt <= size:

        # 아래로 이동해야 하기때문에 visited[r][c]가 아니라 visited[c][r]로 해준다.
        visited[c][r] = cnt

        nr = r+dr[angle]
        nc = c+dc[angle]
        cnt += 1

        # 삼각형 모양으로 돌아야 하기 때문에 행으로 이동 후 왼쪽대각선위쪽으로 가기 위해 nx는 ny이랑 비교
        # visited[c][r]로 시작하기때문에 이동좌표로 visited[nc][nr] 형식으로 비교
        if 0<=nc<n and 0<=nr<=nc and visited[nc][nr] == 0:
            r, c = nr, nc
        else:
            # dr,dc기준으로 좌표 이동하기 위해 %3을 해준다.
            angle = (angle+1)%3
            r += dr[angle]
            c += dc[angle]

    # 0이 아닌 숫자만 1차원 배열에 담기위해 2중 for문을 돌려준다.
    for i in visited:
        for j in i:
            if j != 0:
                answer.append(j)

    return answer
n = 4
print(solution(n))
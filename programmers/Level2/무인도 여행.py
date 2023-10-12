from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

def bfs(n,m,r,c,visited,field):

    q = deque([(r,c)])
    visited[r][c] = 1   # 방문했다고 1로 표시해주고
    cost = int(field[r][c]) # cost에 해당 숫자 값을 더해준다.

    # q에 더 이상 값이 없을때 까지 while문들 돌린다.
    while q:
        r, c = q.popleft()

        # 상하좌우로 이동하기 위해 for문을 돌림
        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]

            # 범위 조건때문에 bfs함수에 n,m값을 넘겨줘야 한다.
            if 0<=nr<n and 0<=nc<m and field[nr][nc] != 'X':
                # 범위에 벗어나지 않고 숫자값이면
                if not visited[nr][nc]:
                    visited[nr][nc] =1 # 방문표시를 해주고
                    cost += int(field[nr][nc]) # 숫자 합계
                    q.append((nr,nc)) # q에 해당 좌표값을 넣어준다.

    return visited, cost

def solution(maps):
    answer = []
    n, m = len(maps), len(maps[0])
    visited = [[0]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            # mpas에서 'X'가 아니고 visited[i][j]에 방문한 적이 없다면, bfs를 탄다. -> 즉 숫자값인 경우 bfs함수를 탄다.
            if maps[i][j] != 'X' and not visited[i][j] :
                visited, ans = bfs(n,m,i,j,visited,maps)
                answer.append(ans)

    if answer == []:
        return [-1]
    else:
        return sorted(answer)


maps = ["X591X","X1X5X","X231X", "1XXX1"]
    #["X591X","X1X5X","X231X", "1XXX1"]
print(solution(maps))
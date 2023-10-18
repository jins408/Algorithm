from collections import deque

dr = [0,0,-1,1]
dc = [-1,1,0,0]

def bfs(n,m,r,c,visited,filed):

    q = deque([(r,c)])
    visited[r][c] = 1
    cost = int(filed[r][c])

    while q:
        r,c = q.popleft()

        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]

            if 0<=nr<n and 0<=nc<m and filed[nr][nc] != 'X':
                if visited[nr][nc] != 1:
                    visited[nr][nc] = 1
                    cost += int(filed[nr][nc])
                    q.append((nr,nc))
    return visited, cost

def solution(maps):
    answer = []

    n,m = len(maps), len(maps[0])
    visited = [[0]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and visited[i][j]==0:
                visited[i][j] = 1
                visited, ans = bfs(n,m,i,j,visited,maps)
                answer.append(ans)

    if answer == []:
        return [-1]
    else:
        return sorted(answer)


maps = ["X591X","X1X5X","X231X", "1XXX1"]
print(solution(maps))

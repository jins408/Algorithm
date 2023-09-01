from collections import deque

def solution(maps):
    dr = [0, 0, 1, -1]
    dc = [-1, 1, 0, 0]

    n, m  = len(maps), len(maps[0])

    q = deque()
    q.append((1,0,0))
    maps[0][0] = 0 # 시작 위치 방문 표시

    while q:
        cnt, r, c = q.popleft() # 이동 칸, row, column

        for k in range(4):
            nr = dr[k]+r
            nc = dc[k]+c
            if nr == n-1 and nc == m-1: # 가장 먼저 도착한 것이 가장 짧은 거리
                return cnt+1
            if -1 < nr < n and -1 < nc < m and maps[nr][nc]:  # 맵을 넘어가지 않고 1이라면
                q.append((cnt+1, nr, nc))
                maps[nr][nc] = 0   # 방문할 위치를 미리 방문 표시(효율성 포인트)

    return -1 # 전부 순회해도 도달하지 못함

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))
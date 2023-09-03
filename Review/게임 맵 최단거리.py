from collections import deque

def solution(maps):
    answer = []

    dr = [0, 0, 1, -1]
    dc = [-1, 1, 0, 0]

    n, m = len(maps) , len(maps[0])

    q = deque()
    q.append((1,0,0))
    maps[0][0] = 0

    while q:
        cnt, r, c = q.popleft()

        for i in range(4):
            nr = dr[i]+r
            nc = dc[i]+c
            if n-1 == nr and m-1 == nc:
                return cnt+1
            if -1<nr<n and -1<nc<m and maps[nr][nc] == 1:
                q.append((cnt+1, nr, nc))
                maps[nr][nc] = 0

    return -1


maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))

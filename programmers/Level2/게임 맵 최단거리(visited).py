from collections import deque

def solution(maps):
    answer = 0

    dr = [0, 0, 1, -1]
    dc = [-1, 1, 0, 0]

    q = deque()
    q.append((0,0))

    # 이동한 곳을 체크할 리스트
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    visited[0][0] = 1 # 방문위치
    maps[0][0] = 0  # 시작위치

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = dr[i]+r
            nc = dc[i]+c
            # maps범위 안에 있고
            if 0<=nr<len(maps) and 0<=nc<len(maps[0]):
                # mpas에 이동할 수 있는 곳이 1이고, visited를 방문하지 않았다면
                if maps[nr][nc] == 1 and not visited[nr][nc]:
                    # visited에  +1를 해준다
                    visited[nr][nc] = visited[r][c]+1
                    q.append((nr,nc))
    # while문을 다 돌아도 목적지까지 도달할 수 없다면, -1
    answer = -1
    if visited[-1][-1]:
        return visited[-1][-1]
    return answer

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))
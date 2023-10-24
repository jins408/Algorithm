from collections import deque

def bfs(s, G, visited, K):

    q = deque([[s,0]])
    visited[1] = 0

    cnt = 0
    while q:
        tartget, num = q.popleft()

        for i in G[tartget]:
            # 1[0](노드번호):1과 연결된 번호, i[1](노드간 연결된 거리): 노드(1)와 노드(i[0]) 사이의 거리
            # num+i[1] 노드간의 거리가 K보다 작거나 같고, 노드간의 거리가 visited[i[0]] 보다 잘을때
            if num + i[1] <= K and num + i[1] < visited[i[0]]:
                # visited[i[0]]를 노드간의 거리로 바꿔준다.(특정 노드를 방문하는데 걸린 시간 중 최소의 값을 찾기 위해)
                visited[i[0]] = num + i[1]
                # 해당 노드와 노드간의 거리를 q에 넣어준다.
                q.append([i[0], num+i[1]])
    print(visited)
    for k in visited:
        if k != 0xfffff:
            cnt += 1

    return cnt

def solution(N, road, K):
    answer = 0

    G = [[] for _ in range(N+1)]
    # 중요한 것은 특정 노드를 방문했느냐 안했느냐(0 or 1)가 아닙니다.
    # 특정 노드를 방문하는데 걸린 시간 중 최소의 값을 visit에 저장하고
    # 특정 노드를 방문하는데 그 값보다 큰 시간이 걸리는 경우에는 탐색하지 않는 식으로 구현해보세요.
    # visited = [False] * (N + 1) -> 이런식으로 하면 안되는 이유
    visited = [0xfffff] * (N + 1)

    for u,v,w in road:
        G[u].append([v,w])
        G[v].append([u,w])
    print(G)
    a = bfs(1, G, visited, K)
    answer = a
    return answer

N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3
print(solution(N, road, K))
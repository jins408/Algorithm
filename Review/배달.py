from collections import deque

def bfs(s,G,visited,K):

    q = deque([[s,0]])
    visited[1] = 0

    cnt = 0
    while q:
        target, num = q.popleft()

        for i in G[s]:
            if num + i[1] <= K and num+i[0] < visited[i[0]]:
                visited[i[0]] = num + i[1]
                q.append([ i[0], num+i[1]])


    for k in visited:
        if k != 0xfffff:
            cnt += 1

    return cnt

def solution(N, road, K):
    answer = 0

    G = [[] for _ in range(N+1)]
    visited = [0xfffff]*(N+1)

    for u,v,w in road:
        G[u].append([v,w])
        G[v].append([u,w])

    a = bfs(1,G,visited,K)

    answer = a

    return answer

N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3

print(solution(N, road, K))
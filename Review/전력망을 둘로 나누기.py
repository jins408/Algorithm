from collections import deque
def bfs(num, check, visited, graph):

    q = deque([num])
    visited[num] = True
    cnt = 1
    while q:
        s = q.popleft()

        for v in graph[s]:
            if visited[v] == False and check[num][v]:
                q.append(v)
                visited[v] = True
                cnt += 1

    return cnt


def solution(n, wires):
    answer = n

    check = [[True]*(n+1) for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]

    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
    print(graph)

    for a,b in wires:
        visited = [False] * (n + 1)
        check[a][b] = False
        cnt_a = bfs(a,check,visited, graph)
        cnt_b = bfs(b,check,visited, graph)
        check[a][b] = True

        answer = min(answer, abs(cnt_a-cnt_b))

    return answer

n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
print(solution(n, wires))
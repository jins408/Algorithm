from collections import deque
def bfs(start, graph, visited, check):

    q = deque([start])
    visited[start] = True
    cnt = 1 # 연결된 노드의 개수(송전탑의 개수)를 세기위한 카운트
    while q:
        s = q.popleft()

        for v in graph[s]:
            # visited[v]를 아직 방문하지 않았고, check[start][v]도 True인 경우(간선이 끊기지 않은 경우)
            if visited[v] == False and check[start][v]:
                q.append(v)
                visited[v] = True # 방문했다고 표시
                cnt += 1    # 연결 되어있다는 것이기때문에 cnt 1증가

    return cnt


def solution(n, wires):
    answer = n

    # 끊은 간선인지 아닌지 체크하기 위한 리스트
    check = [[True]*(n+1) for _ in range(n+1)]
    # 송전탑 그래프 -> 노드간 서로 연결된 노드의 개수를 확인하기 위해
    graph = [[] for _ in range(n+1)]

    # graph 채우기
    for a,b in wires:
        graph[a].append(b) # a에 연결된 노드의 개수
        graph[b].append(a) # b에 연견된 노드의 개수

    for a,b in wires:   # 간선 정보를 다 확인하면서
        visited = [False]*(n+1)     # a,b에 붙어있는 송전탑의 개수(노드의 개수)를 세기 위해
        check[a][b] = False         # a에서 b로가는 간선을 끊어준다.
        cnt_a = bfs(a, graph, visited, check)   # 그때 a랑 붙어있는 노드의 개수(송전탑의 개수)
        cnt_b = bfs(b, graph, visited, check)   # 그때 b랑 붙어있는 노드의 개수(송전탐의 개수)
        check[a][b] = True  # 그리고 다시 a에소 b로 가는 간선 연결

        # 그 중에 가장 작은 값을 받도록 answer에 할당
        answer = min(answer, abs(cnt_a - cnt_b))

    return answer

n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
print(solution(n,wires))
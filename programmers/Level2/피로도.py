#for문 안에 재귀함수가 있는 경우
#answer,N 전역변수, visited 전역배열
answer = 0
N = 0
visited = []

def dfs(k,cnt,dungeons, visited):
    # 2단계: 함수 안에 있는  지역변수answer를 전역변수화 시킨다. answer는 전역변수이다.
    global answer

    # 1단계:비교 등호를 사용하면 인터프리터가 answer가 지역변수로 간주해버린다. 그런데 answer에 할당된 값이 없다.
    if cnt > answer:
        answer = cnt

    for j in range(N):
        if k >= dungeons[j][0] and visited[j] == 0:
            visited[j] = 1 #방문하려는 곳은 1로 체크
            dfs(k-dungeons[j][1],cnt+1, dungeons, visited)
            visited[j]=0 #back하려는 경우에는 0로 되돌려 놓는다.


def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    # 방문 했는지 안했는지 체크해줄 리스트
    visited = [0]*N
    dfs(k, 0, dungeons, visited)
    return answer

k=80
dungeons = [[80,20],[50,40],[30,10]]
print(solution(k, dungeons))
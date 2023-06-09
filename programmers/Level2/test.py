
def solution(n):
    dx = [0,1,-1]
    dy = [1,0,-1]

    arr2 = [[0]*n for _ in range(n)]
    x = y = visited = 0
    cnt = 1

    size = (n+1)*n//2

    while cnt <= size:
        arr2[y][x] = cnt
        ny = y+dy[visited]
        nx = x+dx[visited]
        cnt += 1

        if 0<=ny<n and 0<=nx<=ny and arr2[ny][nx] == 0:
            y = ny
            x = nx
        else:
            visited = (visited+1)%3
            y += dy[visited]
            x += dx[visited]

    answer = []
    for i in arr2:
        for j in i:
            if j != 0:
                answer.append(j)

    return answer


n=4
print(solution(n))

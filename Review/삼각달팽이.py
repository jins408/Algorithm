def solution(n):
    answer = []

    dr = [1,0,-1]
    dc = [0,1,-1]

    visited = [[0]*n for _ in range(n)]
    r,c,num = 0,0,0
    cnt = 1
    size = (n+1)*n//2

    while cnt <= size:

        visited[c][r] = cnt

        nr = r+dr[num]
        nc = c+dc[num]
        cnt += 1

        if 0<=nc<n and 0<=nr<=nc and visited[nr][nc] == 0:
            r = nr
            c = nc
        else:
            num = (num+1)%3
            r += dr[num]
            c += dc[num]

    for i in visited:
        for j in i:
            if j != 0:
                answer.append(j)
    return answer

n = 4
print(solution(n))
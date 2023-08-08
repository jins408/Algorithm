n=3
def solution(n):
    answer = 0
    arr = [[0 for j in range(n)] for i in range(n)]
    r,c = 0,-1
    dr = [0,1,0,-1] #방향에 대한 r변량
    dc = [1,0,-1,0] #방향에 대한 c변량
    dir = 0         # 방향
    loop = n
    num = 0

    while num < n*n:
        for i in range(loop):
            r = r+dr[dir]
            c = c+dc[dir]
            num += 1
            arr[r][c] = num
        dir = (dir+1)%4     #
        if dir % 2:
            loop -= 1

    for x in range(n):
        answer += arr[x][x]
    return answer

print(solution(n))
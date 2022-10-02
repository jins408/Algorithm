n=3
def solution(n):
    answer = 0

    arr = [[0 for j in range(n)] for i in range(n)]
    print(arr)
    k = n
    r = 0
    c = -1
    dr=[0,1,0,-1]
    dc=[1,0,-1,0]
    num = 0
    dir = 0

    while num < n*n:
        for i in range(k):
            r = r+dr[dir]
            c = c+dc[dir]
            num += 1
            arr[r][c] = num

        dir = (dir+1)%4
        if dir%2:
            k -=1

    for x in range(n):
        answer += arr[x][x]

    return answer



print(solution(n))
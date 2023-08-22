def solution(n, left, right):

    arr = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(i,i+1):
            arr[i][j] = i+1

        # 위, 왼쪽
        dr = [-1, 0]
        dc = [0, -1]
        r = i
        c = j
        index = i+1
        for i in range(2):
            nr = r
            nc = c
            while True:
                nr += dr[i]
                nc += dc[i]
                if 0 <= nr <= n and 0 <= nc <= n and arr[nr][nc]==0:
                    arr[nr][nc] = index
                else:
                    break

    list = [data for i in arr for data in i]

    return  list[left:right+1]

n = 3
left = 2
right = 5
print(solution(n, left, right))
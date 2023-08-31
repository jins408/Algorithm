def solution(land):
    answer = []
    # 최대값 찾는 방향 (좌,우)
    dr = [0, 0]
    dc = [-1,1]

    # 아래로 이동하는 방향(대각선 오른쪽, 왼쪽)
    down_r = [1, 1]
    down_c = [-1,1]

    r = 0
    c = 0
    now = land[0][0]
    for i in range(len(land)):
        for j in range(4):

            for k in range(2):
                nr = dr[k]+r
                nc = dc[k]+c
                if 0<=nr<=len(land) and 0<=nc<=3 and (now < land[nr][nc] or land[nr][nc]==0):
                    now = land[nr][nc]
                    r = nr
                    c = nc
                else:
                    continue
        answer.append(now)
        if r+1 <= len(land)-1 and c <= 3:
            land[r+1][c] = 0
        for x in range(2):
            ndr = down_r[x] + r
            ndc = down_r[x] + c
            if 0 <= ndr <= len(land)-1 and 0 <= ndc <= 3 and now < land[ndr][ndc]:
                now = land[ndr][ndc]
                r = ndr
                c = ndc
            else:
                continue

    return answer

land = [[1,2,5,3],[5,6,7,8],[4,3,2,1]]
print(solution(land))
def solution(park, routes):
    r = 0
    c = 0

    dic = {'N':(-1,0), 'S':(1,0),'W':(0,-1),'E':(0,1)}
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                r = i
                c = j

    for route in routes:
        dr, dc = dic[route.split()[0]]
        n = int(route.split()[1])

        s_r = r
        s_c = c
        for _ in range(n):
            nr = r+dr
            nc = c+dc
            if 0<=nr<=len(park)-1 and 0<=nc<=len(park[0])-1 and park[nr][nc] != 'X':
                r = nr
                c = nc
            else:
                r = s_r
                c = s_c
                break
    return [r, c]

park = ["OSO","OOO","OXO","OOO"]
routes = ["E 2","S 3","W 1"]
print(solution(park,routes))
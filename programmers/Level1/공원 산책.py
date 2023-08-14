def solution(park, routes):
    answer = []

    dic_routes={}
    for route in routes:
        k, v = route.split()
        dic_routes[k] = int(v)
    print(dic_routes)

    # 위치
    r = 0
    c = 0

    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                r = i
                c = j
                break
    # 이동
    for route in dic_routes:
        nr = r
        nc = c
        for k in range(dic_routes[route]):
            # 동
            if route == 'E' and nc < len(park[0])-1 and park[nr][nc+1] != 'X':
                nc += 1
                if k == dic_routes[route]-1:
                    c = nc
            # 서
            elif route == 'W' and nc > 0 and park[nr][nc-1] != 'X':
                nc-=1
                if k == dic_routes[route]-1:
                    c = nc
            # 남
            elif route == 'S' and nr < len(park)-1 and park[nr+1][nc] != 'X':
                nr += 1
                if k == dic_routes[route]-1:
                    r = nr
            # 북
            elif route == 'N' and nr > 0 and park[nr-1][nc] != 'X':
                nr -= 1
                if k == dic_routes[route]-1:
                    r = nr

    return [r, c]

park = ["OXXO", "XSXO", "XXXX"]
    #["OSO","OOO","OXO","OOO"]
    #["SOO","OXX","OOO"]
    #["SOO","OOO","OOO"]
routes =["E 1", "S 1"]
    #["E 2","S 3","W 1"]
    #["E 2","S 2","W 1"]
    #["E 2","S 2","W 1"]
print(solution(park,routes))
def solution(park, routes):
    # 위치
    r = 0
    c = 0

    # 'S'가 있는 곳이 좌표의 시작위치
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                r = i
                c = j
                break
    # 이동
    for route in routes:
        # if,elif에 걸리지 않으면 좌표 초기화
        nr = r
        nc = c
        for k in range(int(route[2])): # route="E 2"일때,route[0]='E' route[2]=2
            # route[2]만큼 for문을 돌면서 좌표를 찾아준다.
            # 동 (동쪽으로 이동했을때, 동쪽 맨끝쪽이면 안되고, 장애물을 만나서도 안됨)
            if route[0] == 'E' and nc < len(park[0])-1 and park[nr][nc+1] != 'X':
                nc += 1
                if k == int(route[2])-1:
                    # k가 route[2]와 같아지면 해당하는 if문 종료
                    c = nc
            # 서 (서쪽으로 이동했을때, 서쪽 맨끝쪽이면 안되고, 장애물을 만나서도 안됨)
            elif route[0] == 'W' and nc > 0 and park[nr][nc-1] != 'X':
                nc-=1
                if k == int(route[2])-1:
                    c = nc
            # 남 (남쪽으로 이동했을때, 남쪽 맨끝쪽이면 안되고, 장애물을 만나서도 안됨)
            elif route[0] == 'S' and nr < len(park)-1 and park[nr+1][nc] != 'X':
                nr += 1
                if k == int(route[2])-1:
                    r = nr
            # 북 (북쪽으로 이동했을때, 북쪽 맨끝쪽이면 안되고, 장애물을 만나서도 안됨)
            elif route[0] == 'N' and nr > 0 and park[nr-1][nc] != 'X':
                nr -= 1
                if k == int(route[2])-1:
                    r = nr

    return [r, c]

park = ["SOO","OOO","OOO"]
    #["OSO","OOO","OXO","OOO"]
    #["SOO","OXX","OOO"]
    #["SOO","OOO","OOO"]
routes =["E 2","S 2","W 1"]
    #["E 2","S 3","W 1"]
    #["E 2","S 2","W 1"]
    #["E 2","S 2","W 1"]
print(solution(park,routes))
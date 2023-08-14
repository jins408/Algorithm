def solution(park, routes):
    r,c = 0,0
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                r,c = i,j

    # 북,남,서,동
    dic = {'N':(-1, 0), 'S':(1, 0), 'W':(0, -1), 'E':(0, 1)}

    for i in routes:
        #i.split()) -> ['E', '2']
        #i.split()[0]) -> E
        dr, dc = dic[i.split()[0]] # 이동방향 ex) dic[E]=(0,1) dr=0,dc=1
        n = int(i.split()[1])   # 이동횟수 i.split()[1]) -> 2 n=2

        # 현재위치
        s_r = r
        s_c = c
        for _ in range(n):
            nr = r+dr #현재위치에서 이동방향만큼 더해준다
            nc = c+dc
            if 0<=nr<=len(park)-1 and 0<=nc<=len(park[0])-1 and park[nr][nc] != 'X':
                # 조건에 맞으면 이동방향이 현재 위치가 되고
                r,c = nr,nc
            else:
                # 조건에 맞지않으면 현재위치로 다시 초기화 시켜준다
                r,c = s_r,s_c
                break

    return [r, c]

park = ["OSO","OOO","OXO","OOO"]
    #["OSO","OOO","OXO","OOO"]
    #["SOO","OXX","OOO"]
    #["SOO","OOO","OOO"]
routes =["E 2","S 3","W 1"]
    #["E 2","S 3","W 1"]
    #["E 2","S 2","W 1"]
    #["E 2","S 2","W 1"]
print(solution(park,routes))
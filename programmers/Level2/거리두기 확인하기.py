def check(place):
    # P='사람' O='빈책상' X='파티션'
    # 전달 받은 place는 1차원 배열로 이루어진 문자열을 2차원 배열로 만들어서 인덱스로 거리를 확인하기 위해 enumerate함수를 사용
    #print(place)
    for idx_row, row in enumerate(place):
        for idx_col, cell in enumerate(row):
            #print(idx_row, idx_col, cell)
            if cell != 'P': #현재 자신의 위치에서 다른 응시자가 있으면 안되는 경우만 전부 확인하고 아니면 넘어가기(cell='P'일때 비교하기)
                continue

            # 대기실은 5개까지로 5*5 고정배열로 진행
            isNotEndrow = idx_row != 4  #세로방향 비교 (인덱스가 4까지 있지만, 세로방향으로 3,4비교하면 인데스4는 더이상 비교할 곳이 없으므로 3까지만 비교)
            isNotEndcol = idx_col != 4  #가로방향 비교 (인덱스가 4까지 있지만, 가로방향으로 3,4비교하면 인데스4는 더이상 비교할 곳이 없으므로 3까지만 비교)
            isNotFirstCol = idx_col != 0 #왼쪽 이동(0이면 왼쪽으로 더이상 이동할 곳이 없으니까 0이 아닐때만 확인)
            isBeforeThirdRow = idx_row < 3 #세로 두번이동(맨해튼거리2까지만 확인)
            isBeforThirdCol = idx_col < 3  #가로 두번이동(맨해튼거리2까지만 확인)

            # D:아래로 한칸 D2:아래로 두칸 L:왼쪽한칸 LD:왼쪽아래 R:오른쪽한칸 RD:오른쪽아래 R2:오른쪽 두칸

            # 세로방향으로 비교하는 모든 경우
            if isNotEndrow:
                # 밑으로 한번
                D = place[idx_row+1][idx_col] # idx_row=0 row=POOOP idx_row=1 row=OXXOX.. idx_co1=0 일때만비교(밑으로 이동해서)
                if D == 'P': # 바로 밑에 P사람이 있으면 거리두기 지키기X
                    return 0 # 0을 반환(거리두기 지키기X)
                # 밑으로 두번
                if isBeforeThirdRow:
                    D2 = place[idx_row+2][idx_col]
                    if D2 == 'P' and D != 'X': # 파티션이 아닌경우 거리두기 지키기X
                        return 0 # 0을 반환(거리두기 지키기X)
                # 오른쪽 밑에
                if isNotEndcol:
                    R = place[idx_row][idx_col+1] #오른쪽으로 이동
                    RD = place[idx_row+1][idx_col+1] #오른쪽 아래로 이동
                    if RD == 'P' and (D != 'X' or R !='X'): # 오른쪽 또는 밑에 파티션이 아닌데 오른쪽 아래 사람이 있는 경우(거리두기 지키기X)
                        return 0
                # 왼쪽으로 밑에
                if isNotFirstCol:
                    L = place[idx_row][idx_col-1]  #왼쪽으로 이동
                    LD = place[idx_row+1][idx_col-1] #왼쪽 아래로 이동
                    if LD == 'P' and (D != 'X' or L !='X'): # 왼쪽 또는 밑이 파티션이 아닌데 왼쪽 아래에 사람이 있는 경우(거리두기 지키기X)
                        return 0
            # 가로방향 모든 경우
            if isNotEndcol:
                # 오른쪽으로 한번 이동
                R = place[idx_row][idx_col+1]
                if R == 'P': return 0 # 바로 옆에 사림이 있으면(거리두기 지키기X)
                # 오른쪽으로 두번 이동
                if isBeforThirdCol:
                    R2 = place[idx_row][idx_col+2]
                    if R !='X' and R2=='P': #PXP가 사이에 파이션이 아닌경우면(거리두기 지키기X)
                        return 0
    return 1


def solution(places):
    return [check(place) for place in places]


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

print(solution(places))
#print(check(places))


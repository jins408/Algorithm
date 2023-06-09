def solution(n):
    # 반시계방향
    # y+1(아래이동) x+1(오른쪽이동) x-1,y-1(왼쪽대각선위)
    dx = [0,1,-1]
    dy = [1,0,-1]
    # 2차원 0으로 채워진 배열 생성
    snail = [[0]*i for i in range(1,n+1)]
    x = y = angle = 0
    cnt = 1
    # 결과가 나올 배열의 크기 지정
    size = (n+1)*n // 2

    # cnt랑 비교해서 size배열과 같을 때까지 while문 돌림
    while cnt <= size:
        # snail배열에 채워 넣을 수
        snail[y][x] = cnt # snail[0][0] = 1
        # 반시계 방향으로 배열에 채워넣기 위해 다음에 이동할 위치 지정 ny, nx
        ny = y+dy[angle] # 0+1 = 1
        nx = x+dx[angle] # 0+0 = 0
        cnt += 1 # 배열에 넣을 수 증가

        # 방향전환을 하기 위해 조건을 줘야 함
        # 삼각 달팽이 모양으로 돌아야 하기 때문에 행으로 이동 후 왼쪽대각선위쪽으로 가기 위해 nx는 ny이랑 비교
        # 0일 배열에만 숫자을 넣을 수 채워 넣을 수 있으므로 0이 아닌 숫자가 있으면 조건과 일치하지 않음
        if 0<=ny<n and 0<=nx<=ny and snail[ny][nx]==0:
            # 조건과 일치한다면 같은 행이나 열에서 숫자를 채워 넣야야 함으로 y,x 값을 다을으로 넘어갈 값으로 가져감 dx,dc 방향 값 그대로 유지
            y, x = ny,nx
        else:
            # 일치하지 않다면 방향전환 dx=0,dy=1 에서 dx=1, dy=0으로 바꾸기 위해
            angle = (angle + 1)%3 #3방향으로만 이동해서 3으로 나눈 나머지 값으로 계산
            y += dy[angle] # dy[0] -> dy[1] -> dy[2]
            x += dx[angle] # dx[0] -> dx[1] -> dx[3]

            # 2차원 배열을 1차원으로 바꿈
    return [i for j in snail for i in j]

n=4
print(solution(n))


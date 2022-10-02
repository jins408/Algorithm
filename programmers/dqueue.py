from collections import deque

def solution(garden):
    dx = [1, -1, 0, 0] ## 하상우좌 다 비교하기 위해
    dy = [0, 0, 1, -1]

    n = len(garden)
    q = deque()
    cnt = 0
    for i in range(n):
        for j in range(n):
            if garden[i][j] == 1:
                q.append([i, j])
                cnt += 1
    if cnt == n * n:
        return 0

    t = 0
    while q:
        t += 1
        for _ in range(len(q)):
            x, y = q.popleft()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and garden[nx][ny] == 0:
                    q.append([nx, ny])
                    garden[nx][ny] = 1
                    cnt += 1
                    if cnt == n * n:
                        return t

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
garden1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
ret1 = solution(garden1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

garden2 = [[1, 1], [1, 1]]
ret2 = solution(garden2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")
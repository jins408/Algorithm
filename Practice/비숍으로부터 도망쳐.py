def solution(bishops):
    answer = 0

    count = [[0 for i in range(9)] for j in range(9)]

    dr = [-1, -1, 1, 1]
    dc = [-1, 1, -1, 1]

    for bishop in bishops:
        x = ord(bishop[0]) - ord('A') + 1
        y = 8 - int(bishop[1]) + 1

        count[x][y] = 1

        for i in range(4):
            nr, nc = x, y
            while True:     # 비숍이 한쪽 방향으로 이동하는 경로를 파악하기 위해 while문 돌림
                nr += dr[i]
                nc += dc[i]
                if 0 < nr < 9 and 0 < nc < 9:
                    count[nr][nc] = 1
                else:
                    break

    # 비숍이 이동하지 않은 곳을 찾아서 +1 해주기 위해 for문 돌림
    for i in range(1, 9):
        for j in range(1, 9):
            if not count[i][j]: # count[x][y] == 1 이 아닌경우
                answer += 1
    return answer

bishops1 = ["D5"]
ret1 = solution(bishops1)

print("solution 함수의 반환 값은", ret1, "입니다.")

bishops2 = ["D5", "E8", "G2"]
ret2 = solution(bishops2)

print("solution 함수의 반환 값은", ret2, "입니다.")
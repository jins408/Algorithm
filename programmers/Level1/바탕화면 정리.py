def solution(wallpaper):
    answer = []

    start = [] # 시작좌표를 담을 리스트
    end = [] # 종료좌표를 담을 리스트
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                start.append((i,j))     # 시작좌표
                end.append((i+1,j+1))   # 끝좌표

    print(start)
    print(end)
    start_min1 = [] # 시작좌표 첫번째 값들을 담을 리스트
    start_min2 = [] # 시작좌표 두번째 값들을 담을 리스트
    end_max1 = [] # 끝표 첫번째 값들을 담을 리스트
    end_max2 = [] # 끝표 첫번째 값들을 담을 리스트

    for i in start:
        start_min1.append(i[0]) # 첫번째 값 중 제일 작은 값
        start_min2.append(i[1]) # 두번째 값 중 제일 작은 값
    a = min(start_min1)
    b = min(start_min2)
    answer.append(a)
    answer.append(b)

    for j in end:
        end_max1.append(j[0]) # 첫번째 값 중 제일 큰 값
        end_max2.append(j[1]) # 두번째 값 중 제일 큰 값
    c = max(end_max1)
    d = max(end_max2)
    answer.append(c)
    answer.append(d)

    return answer

wallpaper = ["..", "#."]
    #[".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]
    #["..........", ".....#....", "......##..", "...##.....", "....#....."]
    #[".#...", "..#..", "...#."]
print(solution(wallpaper))
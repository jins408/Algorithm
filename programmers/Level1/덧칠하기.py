def solution(n, m, section):
    answer = 0

    # 페인트칠한 마지막 위치
    max = 0
    for i in section:
        # i가 max보다 크면 section에 칠해야하는 곳에 도착한것
        if i > max:
            # i가 페인트칠한 시작위치
            # answer +1 해줌
            answer +=1
            # 페인트칠한 마지막위치를 알아야 하기 때문에 max값에 칠한시작위치(i)+롤러의길이(m)까지 더해주고 시작점이 포함되기 때문에 -1
            max = i+m-1


    return answer

# 페인트칠할 벽 길이
n = 8
    #8
# 페인트칠할 롤러의 길이
m = 4
    #4
# 다시 페인트를 칠할 구역
section=[2, 3, 6]
    #[2, 3, 6]
print(solution(n,m,section))
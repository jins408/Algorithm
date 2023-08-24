import math
def solution(progresses, speeds):
    answer = []

    day = []
    for i in range(len(progresses)):
        # 기능이 100%가 될 날짜를 구해서 day에 넣어 줌
        day.append(math.ceil((100-progresses[i])/speeds[i]))
    print(day)

    temp = day[0]
    cnt = 0
    for i in range(len(day)):
        if temp < day[i]:
            answer.append(cnt)
            temp = day[i]
            cnt= 0
        cnt+=1
    answer.append(cnt)

    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds))
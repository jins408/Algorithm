import math
def solution(progresses, speeds):
    answer = []

    day = []
    for i in range(len(progresses)):
        # 기능이 100%가 될 날짜를 구해서 day에 넣어 줌
        day.append(math.ceil((100-progresses[i])/speeds[i]))
    print(day)

    cnt = 0
    num = day[0]
    # 첫번째 일수보다 큰 값이 나올때까지 비교하며 cnt+1해줌
    for i in range(len(day)):
        # 첫번째 일수보다 큰 값이 나오면
        if num < day[i]:
            # 첫번째 일수보다 작은경우를 카운트한 cnt를 먼저 answer에 넣어줌
            answer.append(cnt)
            # num을 큰값으로 변경 해준다.
            num = day[i]
            # cnt초기화
            cnt = 0
        # num 값이 변경 된 경우에도 cnt+1해줌(이 경우에도 배포되었다고 체크해야 되기때문에)
        cnt += 1
    # for문이 다 돈 후 cnt값을 answer에 넣어 줌
    answer.append(cnt)

    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds))
lottos	=[0, 0, 0, 0, 0, 0]
win_nums = [31, 10, 45, 1, 6, 19]

def solution(lottos, win_nums):
    Ranking = {1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 0}
    # {6:1,5:2,4:3,3:4,2:5,1:6,0:6}

    answer = []

    cnt = 0  ## 기존 리스트끼리 비교했을 때, 일치한 숫자가 있다면 그 개수만큼 최소등수
    num = 0  ## 알아 볼 수 없는 번호
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            cnt += 1
        if lottos[i] == 0:
            num += 1
    print(cnt)
    print(num)
    total = cnt + num
    print(total)

    for r in Ranking:
        if Ranking[r] == total:
            answer.append(r)
        if Ranking[r] == cnt:
            answer.append(r)
    if cnt <= 1:
        answer.append(6)

    # answer = [Ranking[total], Ranking[cnt]]

    return answer

print(solution(lottos,win_nums))
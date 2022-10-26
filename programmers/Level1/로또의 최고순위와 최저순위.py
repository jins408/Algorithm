lottos	=[0, 0, 0, 0, 0, 0]
win_nums = [38, 19, 20, 40, 15, 25]
#[0, 0, 0, 0, 0, 0] [38, 19, 20, 40, 15, 25]
#[44, 1, 0, 0, 31, 25] [31, 10, 45, 1, 6, 19]
#[12, 2, 3, 4, 5, 25]
def solution(lottos, win_nums):
    '''
    Ranking = {6:1,5:2,4:3,3:4,2:5,1:6,0:6}
        #{1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 0}
    answer = []
    num = win_nums[::]
    cnt = 0   ## 기존 리스트끼리 비교했을 때, 일치한 숫자가 있다면 그 개수만큼 최소등수
    max_num = 0
    for i in range(len(lottos)):
        for j in range(len(num)):
            if lottos[i] == num[j]:
                cnt += 1
                win_nums.remove(num[j])
    if lottos[i] == 0:
        cnt = len(lottos)

    print(cnt)
    print(win_nums)
    if cnt < len(win_nums):
        result = len(win_nums) - cnt
       # if len(win_nums) != 0:
       #     result = 0
        max_num = result + cnt
    if cnt < 1:
        max_num = 0
    elif len(win_nums) == 0:
        max_num = 6

    print(max_num)
    print(cnt)

    answer = [Ranking[cnt], Ranking[max_num]]

    for r in Ranking:
        if Ranking[r] == max_num:
            answer.append(r)
        if Ranking[r] == cnt:
            answer.append(r)
    '''

    Ranking = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}

    answer = []

    cnt = 0  ## 기존 리스트끼리 비교했을 때, 일치한 숫자가 있다면 그 개수만큼 최소등수
    num = 0  ## 알아 볼 수 없는 번호
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            cnt += 1
        if lottos[i] == 0:
            num += 1

    total = cnt + num

    answer = [Ranking[total], Ranking[cnt]]
    return answer

print(solution(lottos,win_nums))
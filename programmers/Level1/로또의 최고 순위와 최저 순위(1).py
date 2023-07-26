def solution(lottos, win_nums):
    answer = []

    # 맞은 개수로 로또 등수를 알 수 있는 딕셔너리 생성
    # 키 값은 중복 값이 들어 갈 수 없으므로 (6등은 0,1일때 둘다 해당) key값에 맞은 개수를 넣어주도록 함
    score = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}

    num = 0 # lottos와 win_nums 일치하는 숫자의 개수 (최저순위)
    cnt = 0 # 0의 개수 (최고순위로 바뀔 수 있는 경우의 수)
    for i in range(len(lottos)):
        if lottos[i] == 0:
            cnt += 1
        for j in range(len(win_nums)):
            if lottos[i] == win_nums[j]:
                num += 1

    # 0의 개수가 1게 이상이면, 최고순위가 바뀔수 있는 경우가 생겨서 각각 최저,최고 순위를 봐줌
    if cnt != 0:
        sum = num+cnt
        for i in score:
            if i == num:
                answer.append(score[i])
            elif i == sum:
                answer.append(score[i])
    else:
        # 0의개수가 0개일때는 num의 개수로 최저최고순위 판단
        for j in score:
            if j == num:
                answer.append(score[j])
                answer.append(score[j])

    return answer

lottos = [0, 0, 0, 0, 0, 0]
    #[1, 2, 3, 4, 5, 6]
    #[0, 0, 0, 0, 0, 0]
    #[45, 4, 35, 20, 3, 9] [1,1]
    #[44, 1, 0, 0, 31, 25] [3,5]
win_nums =[38, 19, 20, 40, 15, 25]
    #[7, 8, 9, 10, 11, 12]
    #[38, 19, 20, 40, 15, 25]
    #[20, 9, 3, 45, 4, 35]  [1,1]
    #[31, 10, 45, 1, 6, 19] [3,5]
print(solution(lottos, win_nums))
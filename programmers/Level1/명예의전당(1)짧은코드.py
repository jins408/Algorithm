def solution(k, score):
    answer = []

    # 명예의 전당을 비교하기 위한 배열
    temp = []
    for i in range(len(score)):
        if i < k:
            temp.append(score[i])
            answer.append(min(temp))
        else:
            if min(temp) < score[i]:
                temp.remove(min(temp))
                temp.append(score[i])
            answer.append(min(temp))

    return answer


k = 9
score =  [10, 30, 40, 3, 0, 20, 4]
    #[10, 30, 40, 3, 0, 20, 4]
    #[10, 100, 20, 150, 1, 100, 200]
print(solution(k, score))
#k = 9, score = [10, 30, 40, 3, 0, 20, 4] [10, 10, 10, 3, 0, 0, 0]
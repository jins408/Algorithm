def solution(k, score):
    answer = [score[0]]

    # 명예의 전당을 비교하기 위한 배열
    temp = [score[0]]

    # score 배열 길이가 k보다 큰경우
    if len(score) > k:
        i = 1
        # k의 길이만큼 temp 배열에 score점수를 일단 담는다.
        while len(temp) < k:
            temp.append(score[i])
            i += 1
            # score의 모든 원소가 0인경우가 있을 수 있기때문에 <=로 조건을 줌
            if min(temp) <= max(temp):
                answer.append(min(temp))

        # temp와 score를 비교
        for i in range(k, len(score)):
            # temp 제일 큰값이 score[i]보다 작다면, temp의 제일 작은 값을 지워주고 score[i]를 temp에 넣어주고
            # -> 명에의 전당에는 점수가 제일 높은 사람이 와야하기 때문에
            # 그 다음 temp중에 제일 작은 값을 answer에 넣어줌
            # -> 명예의 전당에서 제일 최하위 점수를 뽑아줘야 하기때문에 remove(min(temp))를 해줌
            if max(temp) <= score[i]:
                temp.remove(min(temp))
                temp.append(score[i])
                answer.append(min(temp))
            else:
                # temp의 제일 작은값보다 score[i]가 큰 경우, temp제일 작은 값을 지워주고 temp에 score[i]를 넣어주고
                # -> 명에의 전당에는 점수가 제일 높은 사람이 와야하기 때문에
                # 그 후에 temp중 제일 작은 값을 answer에 넣어줌
                # -> 명예의 전당에서 제일 최하위 점수를 뽑아줘야 하기때문에 remove(min(temp))를 해줌
                if min(temp) < score[i]:
                    temp.remove(min(temp))
                    temp.append(score[i])
                    answer.append(min(temp))
                else:
                    answer.append(min(temp))
    else:
        # temp에 score점수를 담고 항상 제일 작은 값만 찾으면 됌
        for i in range(1, len(score)):
            temp.append(score[i])
            if min(temp) <= score[i]:
                answer.append(min(temp))

    return answer


k = 3
score = [10, 100, 20, 150, 1, 100, 200]
    #[10, 30, 40, 3, 0, 20, 4]
    #[10, 100, 20, 150, 1, 100, 200]
print(solution(k, score))
#k = 9, score = [10, 30, 40, 3, 0, 20, 4] [10, 10, 10, 3, 0, 0, 0]
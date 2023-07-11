def solution(k, m, score):
    answer = 0

    # 큰 수부터 상자를 몇개 만들 수 있는지 확인
    score = sorted(score, reverse=True)
    print(score)


    # 내림차순으로 정렬한다음 m개씩 묶고 그중 최솟값*m을 result에 계속 더하면 됩니다.
    box = []
    for i in range(0, len(score), m):
        if i+m > len(score):
            break
        for j in range(i, i + m):
            box.append(score[j])
        if len(box) == m:
            answer += min(box) * m
            box = []

    return answer

k = 4
m = 3
score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]
    #[1, 2, 3, 1, 2, 3, 1]
    #[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]
print(solution(k, m, score))
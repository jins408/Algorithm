def solution(k, m, score):
    answer = 0

    # 큰 수부터 상자를 몇개 만들 수 있는지 확인
    score = sorted(score, reverse=True)
    print(score)

    # 내림차순으로 정렬한다음 m개씩 묶고 그중 최솟값*m을 result에 계속 더하면 됩니다.
    # while로 했을때, 런타임에러남-> score배열 자체에서 remove해서 그런듯
    box = []
    # m개씩 묶어서 확인하려고 2중 for문 돌림
    for i in range(0, len(score), m):
        # i+m이 len(score)크면 index에러 남 i+m이 score전체 길이보다 작을때만 봐줌
        if i+m > len(score):
            break
        for j in range(i, i + m):
            box.append(score[j])
        if len(box) == m:
            answer += min(box) * m
            # m개씩 묶은것만 확인해야하므로 box초기화 시켜줌
            box = []

    return answer

k = 4
m = 3
score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]
    #[1, 2, 3, 1, 2, 3, 1]
    #[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]
print(solution(k, m, score))
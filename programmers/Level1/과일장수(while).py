def solution(k, m, score):
    answer = 0

    # 큰 수부터 상자를 몇개 만들 수 있는지 확인
    score = sorted(score)

    while len(score) > 0:
        box = []
        for i in range(len(score)):
            if len(box) == m :
                break
            box.append(score[-1])
            score.pop()
        if len(box) == m:
            answer += min(box) * m
        elif len(score) < m:
            break

    return answer

k = 3
m = 4
score = [1, 2, 3, 1, 2, 3, 1]
    #[1, 2, 3, 1, 2, 3, 1]
    #[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]
print(solution(k, m, score))
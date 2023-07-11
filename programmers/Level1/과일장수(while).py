def solution(k, m, score):
    answer = 0

    # 큰 수부터 상자를 몇개 만들 수 있는지 확인
    score = sorted(score)

    while len(score) > 0:
        box = []
        for i in range(len(score)):
            # for문 전체를 돌기때문에 시간초과나서 len(box)가 m이랑 같을때 break로 끝까지 안보게 해줌
            if len(box) == m :
                break
            # 오름차순으로 정렬해서 score끝에 제일 큰 수부터 비교하고
            box.append(score[-1])
            # pop() 배열의 끝에있는 원소부터 제거
            score.pop()
        # box배열에 전체에서 제일 작은 값찾아서 (최저 사과 점수) x (한 상자에 담긴 사과 개수)해줌
        if len(box) == m:
            answer += min(box) * m
        # pop해준 score길이가 m보다 작은경우 더이상 확인하지 않고 break로 빠져나옴
        elif len(score) < m:
            break

    return answer

k = 3
m = 4
score = [1, 2, 3, 1, 2, 3, 1]
    #[1, 2, 3, 1, 2, 3, 1]
    #[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]
print(solution(k, m, score))
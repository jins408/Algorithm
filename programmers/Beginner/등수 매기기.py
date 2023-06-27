def solution(score):
    answer = []

    sum=[]
    # 2차원 배열로 각각 더한 값의 평균을 구해야 하므로 for문을 돌려서 점수의 평균을 구해줌
    for i in range(len((score))):
        avg = 0
        for j in range(2):
            avg += score[i][j]
        # 소수점까지 고려해서 문제를 풀어줘야 함
        sum.append(avg/2)

    # 내림차순으로 다시 정렬
    sort_sum = sorted(sum, reverse=True)

    # 정렬하기 전 sum과 졍렬한 후의 sort_sum을 비교해줌 -> sort_sum배열의 인덱스를 활용해서 등수를 매겨줄 것이기 때문에
    for i in range(len(sum)):
        for j in range(len(sort_sum)):
            # 동일한 점수의 등수가 존재 할 수 있으므로 sum배열에 있는 원소값을 +1에서 다른 값으로 바꿔줌(두번체크하지 않기위해!)
            if sum[i] == sort_sum[j]:
                sum[i] = sum[i]+1
                # sort_sum 인덱스를 answer에 등수로 넎어줌
                answer.append(j + 1)

    return answer

score = [[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]
#[[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]
#[4, 4, 6, 2, 2, 1, 7]
print(solution(score))
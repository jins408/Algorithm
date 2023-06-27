def solution(score):
    answer = []

    sum=[]
    for i in range(len((score))):
        avg = 0
        for j in range(2):
            avg += score[i][j]
        sum.append(avg/2)

    sort_sum = sorted(sum, reverse=True)

    for i in range(len(sum)):
        for j in range(len(sort_sum)):
            if sum[i] == sort_sum[j]:
                sum[i] = sum[i]+1
                answer.append(j + 1)

    return answer

score = [[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]
#[[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]
#[4, 4, 6, 2, 2, 1, 7]
print(solution(score))
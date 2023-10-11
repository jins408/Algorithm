def solution(sequence, k):
    answer = []

    right = 0
    cnt = 0

    for left in range(len(sequence)):

        while right < len(sequence) and cnt < k:
            cnt += sequence[right]
            right += 1

        if cnt == k:
            if not answer:
                answer= [left, right-1]
            else:
                if answer[1] - answer[0] > right-1-left:
                    answer = [left, right-1]

        cnt -= sequence[left]


    return answer

sequence = [1, 2, 3, 4, 5]
k = 7
print(solution(sequence, k))
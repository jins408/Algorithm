def solution(sequence, k):
    answer = []
    right = 0
    cnt = 0

    for left in range(len(sequence)):

        # 합이 작으면 오른쪽으로 이동
        while right < len(sequence) and cnt < k:
            # cnt가 k랑 같아질때까지 sequence리스트 오른쪽으로 이동하면서 계속 더해준다.
            cnt += sequence[right]
            # 인덱스 값을 구하기 위한 값
            right += 1

        # 크거나 같으면 다음 왼쪽 포인터를 이동
        if cnt == k:
            if not answer:
                # right에 +1을 해줬기때문에 -1로 인덱스 값을 찾는다.
                answer = [left, right - 1]
            else:
                # cnt가 k값과 같아도 길이가 짧은 수열을 찾거나, 길이가 짧은 수열이 여러개일때 시작인덱스값이 작은 걸 찾아야하기때문에
                # cnt와 k가 같은 값이 나와도 sequence리스트를 계속 확인해줘야한다.
                if answer[1] - answer[0] > right - 1 - left:
                    answer = [left, right - 1]

        # cnt = 0이 될때까지 계속 빼줌
        cnt -= sequence[left]


    return answer

sequence = [1, 1, 1, 2, 3, 4, 5]
    #[1, 2, 3, 4, 5]
k = 5
print(solution(sequence,k))

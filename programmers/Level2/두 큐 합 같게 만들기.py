from collections import deque

def solution(queue1, queue2):
    answer = 0

    deque1 = deque(queue1)
    deque2 = deque(queue2)

    sum_deq1 = sum(deque1)
    sum_deq2 = sum(deque2)
    total = sum_deq1+sum_deq2

    # 합이 홀수이면 둘다 똑같이 나눌 수 없기 때문에 return 1 해준다.
    if total%2 == 1:
        return -1

    # queue1과 queue2의 모든 원소를 바꾸면 queue1 길이의 2배만큼 횟수가 필요하고
    # 다시 모든 원소를 바꿔 원래의 모습으로 만들면 queue1 길이의 2배만큼 필요해 총 len(queue1) * 4 만큼 횟수가 필요하다.
    limit = len(deque1)*4

    while True:
        # 합이 큰 큐에서 삭제, 작은 큐에 추가
        # 원소의 합이 높은 쪽에서 낮은 쪽으로 원소를 옮기는 패턴을 찾을 수 있다.
        if sum_deq1 > sum_deq2:
            tartget = deque1.popleft()
            deque2.append(tartget)
            sum_deq1 -= tartget
            sum_deq2 += tartget
            answer += 1
        elif sum_deq1 < sum_deq2:
            tartget = deque2.popleft()
            deque1.append(tartget)
            sum_deq1 += tartget
            sum_deq2 -= tartget
            answer += 1
        else:
            break

        # 아무리 넣었다 뺏다해도 불가능한 경우가 있어서 limit을 주고 횟수를 넘으면 -1을 return해준다.
        if answer == limit:
            answer = -1
            break

    return answer

queue1 = [1,1]
    #[1, 2, 1, 2]
    #[3, 2, 7, 2]
queue2 = [1,5]
    #[1, 10, 1, 2]
    #[4, 6, 5, 1]
print(solution(queue1,queue2))
from collections import deque

def solution(queue1, queue2):
    answer = 0

    deque1 = deque(queue1)
    deque2 = deque(queue2)

    sum_deque1 = sum(deque1)
    sum_deque2 = sum(deque2)
    total = sum_deque1 + sum_deque2

    limit = len(queue1)*4

    if total%2 == 1:
        return -1

    while True:
        if sum_deque1 > sum_deque2:
            a = deque1.popleft()
            deque2.append(a)
            sum_deque1 -= a
            sum_deque2 += a
            answer += 1
        elif sum_deque1 < sum_deque2:
            b = deque2.popleft()
            deque1.append(b)
            sum_deque1 += b
            sum_deque2 -= b
            answer += 1
        else:
            break

        if answer == limit:
            answer = -1
            break

    return answer

queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]
print(solution(queue1, queue2))
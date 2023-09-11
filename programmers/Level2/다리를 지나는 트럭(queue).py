from collections import deque
def solution(bridge_length, weight, truck_weights):

    # []    7,4,5,6    0초
    # [0,7] 4,5,6      1초
    # [7,0] 4,5,6      2초
    # [0,4] 5,6        3초   7
    # [4,5] 6          4초   7
    # [5,0] 6   5초  7,4
    # [0,6]     6초  7,4,5
    # [6,0]     7초  7,4,5
    # [0,0]     8초  7,4,5,6
    answer = 0

    truck = deque(truck_weights)
    q = deque([0]*bridge_length)

    # 시간초과 났던 sum(stack) 대신 변수로 지정해줌
    current_weight = 0
    while q:
        answer += 1
        current_weight -= q.popleft()   # 이전값을 빼줘야하기때문에(pop한 값을 빼줌)

        if truck:
            if current_weight+truck[0] <= weight:
                # sum(stack) 작업과 동일
                current_weight += truck[0]
                a = truck.popleft()
                q.append(a)
            else:
                q.append(0)

    return answer

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
zprint(solution(bridge_length, weight, truck_weights))

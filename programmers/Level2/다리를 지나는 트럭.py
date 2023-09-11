#from collections import deque
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
    stack = [0]*bridge_length   # 0을 함께 담아줄 리스트(bridge_length->다리 길이만큼)
    while len(stack): # 다리 길이만큼 while문을 돈다.
        answer += 1   # truck_weights 리스트에 0값이 없지만, 0포함 weight를 비교하기 때문에 answer에 +1을 먼저 해준다.
        stack.pop(0)  # 0값을 stack에서 뽑아주고

        if truck_weights: # truck_weights 리스트의 첫번째 값이랑 stack의 모든 원소의 sum값을 합한 값을 weight와 비교
            if sum(stack)+truck_weights[0] <= weight:   # sum(시간초과)
                a = truck_weights.pop(0)
                # stack에 truck_weights값을 넣어준다.
                stack.append(a)
            else:
                stack.append(0)

    return answer

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
print(solution(bridge_length, weight, truck_weights))

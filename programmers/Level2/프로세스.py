from collections import deque
def solution(priorities, location):
    answer = 1
    #queue = deque((i, j) for i, j in enumerate(priorities))
    #print(queue)
    temp = deque(priorities)
    print(temp)
    index = location
    while len(temp) >= 0:
        num = max(temp)
        a = temp.popleft()
        if a < num:
            temp.append(a)
            if index == 0:
                index = len(temp)-1
            else:
                index -= 1
        else:
            if index == 0:
                return answer
            else:
                answer += 1
                index -= 1
    return answer

priorities = [1, 1, 9, 1, 1, 1]
    #[2, 1, 3, 2]
#[1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))
def solution(priorities, location):
    answer = 0

    queue = [(i,j) for i,j in enumerate(priorities)]
    print(queue)

    cnt = 0
    while True:
        temp = queue.pop(0)
        if any(temp[1] < i[1] for i in queue):
            queue.append(temp)
        else:
            cnt += 1
            if temp[0] == location:
                return cnt



priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))
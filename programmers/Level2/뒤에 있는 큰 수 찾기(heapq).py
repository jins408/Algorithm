import heapq
def solution(numbers):
    answer = [-1]*len(numbers)

    q = []

    for i, num in enumerate(numbers):
        while q and q[0][0] < num:
            v,idx = heapq.heappop(q)
            answer[idx] = num
        heapq.heappush(q,(num,i))

    return answer

numbers = [9, 1, 5, 3, 6, 2]
    #[2, 3, 3, 5]
    #[9, 1, 5, 3, 6, 2]
print(solution(numbers))
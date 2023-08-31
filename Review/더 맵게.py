import heapq
def solution(scoville, k):
    answer = 0

    heapq.heapify(scoville)
    now = scoville[0]

    while now < k and len(scoville) > 1:

        first = heapq.heappop(scoville)
        second= heapq.heappop(scoville)

        sum = first+(second*2)
        answer+=1
        heapq.heappush(scoville, sum)
        now = scoville[0]

    if min(scoville) < k:
        return -1
    else:
        return answer


scoville = [1, 2, 3, 9, 10, 12]
k = 7
print(solution(scoville, k))



import heapq
def solution(scoville, k):
    answer = 0
    # 최소힙을 이용해서 푸는 문제
    heapq.heapify(scoville)
    print(scoville)
    now = scoville[0]
    cnt = 0
    while now < k and len(scoville) > 1:

        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)

        now = first + second*2
        cnt += 1
        # heapq는 최소값이 항상 맨앞으로 오게 된다(heapq정렬)
        heapq.heappush(scoville, now)
        # 다시 scoville[0]번째를 now값에 넣어준다(제일 작은 값이기 때문에)
        now = scoville[0]

    # 스코빌 지수를 K 이상으로 만들 수 없는 경우는 모두 섞어서 음식이 하나 남았는데도 그 음식의 스코빌 지수가 K보다 작은 경우이므로 if문으로 걸러준다.
    if min(scoville) < k:
        return -1
    else:
        return cnt

scoville = [1]
k = 2
print(solution(scoville, k))
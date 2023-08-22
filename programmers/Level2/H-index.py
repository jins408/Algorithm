def solution(citations):
    answer = 0
    # 인용수 기준 내림차순 정렬 후
    # 정렬된 상태에서의 논문 순서가 인용 수와 같거나 커지는 시점을 h index라고 한다
    # 순서 >= 인용수
    citation = sorted(citations,reverse=True)
    print(citation)
    for i in range(len(citation)):
        if i >= citation[i]:
            return i

    # 논문의 갯수보다 모든 논문이 인용이 더 많은 경우 citation배열 길이 자체를 return해줌
    return len(citation)

citations = [3, 0, 6, 1, 5]
    #[6, 5, 5, 5, 3, 2, 1, 0]
    #[3, 0, 6, 1, 5]
print(solution(citations))
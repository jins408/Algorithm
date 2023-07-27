def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    completion.append("1")
    # 인덱스 오류를 피하기 위해서 +1을 해줌 (문제에서도 completion배열이 participant보다 1 작다고 했음)
    for i, person in enumerate(participant):
        # 같지 않은게 발견되면 바로 resturn 해줌
        if person != completion[i]:
            return person
            # 단 한명의 선수만 제외하고 모두 마라톤을 완주하기때문에 이름이 다른걸 발견하고 다른 부분을 살펴볼 필요가 없다.
    #return answer


participant =["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant,completion))
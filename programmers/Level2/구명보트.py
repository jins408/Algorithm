def solution(people, limit):
    answer = 0

    people.sort() # 오름차순으로 정렬

    # 이 문제의 포인트!
    # 첫 번째 인덱스(0)와 마지막 인덱스(len(people)-1)에 포인터를 설정해서
    # 그 합이 limit 초과일 때와 limit 이하일 때 구명보트에 2명, 1명 태워가며 포인터를 이동시키는 게 핵심
    i = 0
    j = len(people)-1
    # i와 j값이 같아지면 while문 종료
    while i <= j:
        if people[i]+people[j] <= limit:
            # limit보다 작으면 두명
            i+=1
            j-=1
            answer+=1
        else:
            # limit보다 크면 한명만
            j-=1
            answer+=1

    return answer

people = [40, 90, 60, 50]
    #[70, 50, 80, 50]
limit = 100
print(solution(people,limit))
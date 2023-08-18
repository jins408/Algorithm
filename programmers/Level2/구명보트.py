def solution(people, limit):
    answer = 0

    people.sort(reverse=True)
    temp = []
    for i in range(len(people)):
        if limit/2 < people[i]:
            temp.append(people[i])
        elif temp[-1]+people[i] > limit:
            break

    for j in range(len(people)-len(temp), len((people))-1):
        if people[j]+people[j+1] <= limit:
            temp.append(people[j])

    answer = len(temp)

    return answer

people = [70,80,50]
    #[70, 50, 80, 50]
limit = 100
print(solution(people,limit))
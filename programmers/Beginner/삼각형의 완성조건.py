def solution(sides):
    answer = 0

    sort_sides = sorted(sides)


    Min =  sort_sides[1]-sort_sides[0]
    num2 = sort_sides[1]
    Max = sort_sides[0] + sort_sides[1]

    cnt = []
    for i in range(Min+1, num2+1):
        cnt.append(i)

    for j in range(num2+1, Max):
        cnt.append(j)

    answer = len(cnt)

    return answer

sides = [11, 7]
print(solution(sides))

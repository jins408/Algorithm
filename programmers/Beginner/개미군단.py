def solution(hp):
    answer = 0
    # ant = 5, 3, 1

    for ant in [5,3,1]:
        a, hp = divmod(hp, ant)
        answer += a
    return answer
hp = 23
print(solution(hp))
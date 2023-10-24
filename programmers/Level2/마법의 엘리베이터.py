def solution(storey):
    answer = 0

    while storey:
        div = storey%10
        # 6~9
        if div > 5:
            answer += (10-div)
            storey += 10
        # 0~4
        elif div < 5:
            answer += div
        # 5
        else:
            if (storey//10)%10 > 4:
                storey += 10
            answer += div
        storey//=10

    return answer

storey = 2554
print(solution(storey))
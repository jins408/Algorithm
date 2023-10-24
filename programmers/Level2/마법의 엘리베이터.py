def solution(storey):
    answer = 0

    while storey:
        # 자리수에 따라 어떤 값을 가지고 있냐에 따라 계산을 다르게 해줘야함
        div = storey%10 # 자리수를 알기 위해 10으로 나눈 나머지 값을 가진다.
        # 6~9 -> 무조건 올려준다
        if div > 5:
            answer += (10-div)
            storey += 10   # 올려주는 경우이기 때문에 storey에 10을 더해준다.
        # 0~4 -> 무조건 내려준다.(해당하는 div값이 빼줘야하는 돌의 갯수이기 때문에 answer에 그대로 더해준다.)
        elif div < 5:
            answer += div
        # 5 -> 올려줄 때 유리한경우, 내려줄때 유리한 경우 두가지가 있다.
        # 4보다 큰경우는 올려주고, 4보다 작은경우 내려준다.
        else:
            if (storey//10)%10 > 4:
                storey += 10 # 올려주는 경우이기 때문에 storey에 10을 더해준다.
            answer += div # 내려주는 경우이기 때문에 div만 answer에 더해준다.
        # 계산을 다 하고 나면 해달 자리수를 제외하면 몫을 가지고 다시 계산한다.
        storey//=10

    return answer

storey = 2554
print(solution(storey))
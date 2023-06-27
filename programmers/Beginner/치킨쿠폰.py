def solution(chicken):
    answer = 0

    # 10마리당 쿠폰 하나를 제공해 준다
    while True:
        num = chicken
        # chicken 나누기 10 한 몫을 계속 10으로 나눠준다
        chicken = num // 10
        answer += chicken
        # 10으로 나눈 나머지를 다시 chicken값에 더해준 누적 값으로 다시 10으로 나눠준다
        # 나머지가 8,1,1 인 경우 다시 쿠폰아 10장이 됬으므로 한마리를 더 시켜먹을 수 있기때문에 누적해서 치킨값을 더해줘야함
        chicken = chicken+(num%10)
        if chicken < 10:
            break

    return answer

chicken = 100
print(solution(chicken))
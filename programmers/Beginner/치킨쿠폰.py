def solution(chicken):
    answer = 0

    while True:
        num = chicken
        chicken = num // 10
        answer += chicken
        chicken = chicken+(num%10)
        if chicken < 10:
            break

    return answer

chicken = 100
print(solution(chicken))
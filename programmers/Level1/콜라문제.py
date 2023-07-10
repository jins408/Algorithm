def solution(a, b, n):
    answer = 0

    coke = n
    while coke <= n:
        # 먼저 몫과 나머지를 구해 줌
        mod = coke % a
        coke //= a
        # a의 개수만큼 마트에서 돌려주는 콜라병 수 체크
        coke *= b
        # 먼저 몫값을 계속 answer에 더해줌
        answer += coke
        # 해당 조건에 걸리면 더 이상 a개수만큼 나눌 수 있는 빈병이 존재하지 않음(몫과 나머지 모두 체크하는 조건)
        # 몫이 b보다 작으면 더 이상 돌려받을 수 없는 콜라가 없다는 것
        # 몫이 a로 나눈 나머지가 0이면 더 이상 돌려 받을 수 있는 콜라가 없다는 것
        if coke <= b and coke%a == 0:
            break
        else:
            # 나머지와 몫값을 더해서 또 a개수만큼 나눠주기 위해 더해 줌
            coke += mod

    return answer


# 콜라를 받기 위해 마트에 주어야 하는 병 수
a = 3
# 빈 병 a개를 가져다 주면 마트가 주는 콜라 병 수
b = 2
# 상빈이가 가지고 있는 빈 병의 개수
n = 20

print(solution(a, b, n))
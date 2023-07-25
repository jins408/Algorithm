import math

def fun(number):

    num = [1]
    for i in range(2, number+1):
        # 제곱근 구해주는 함수 (float타입이라 int로 형변환)
        N = math.sqrt(i)
        cnt = 0
        for j in range(1, int(N)+1):
            if i%j == 0:
                cnt += 2
                # N=2 이고 i=4인경우 나머지가 0이고 몫이 j값과 동일할때 두가지 경우 모두 봐줘야 하기때문에 if문 걸어줌
                if i/j == j:
                    cnt -= 1
        num.append(cnt)

    return  num
def solution(number, limit, power):
    answer = 0

    # number의 약수의 개수 구하기
    get_fun = fun(number)

    for i in get_fun:
        # limit보다 작으면 그대로 그 숫자를 더해주고
        if i <= limit:
            answer += i
        else:
            # limit보다 큰 경우는 power값을 더해줘야 함
            answer += power

    return answer

number = 5
limit = 3
power = 2
print(solution(number, limit, power))
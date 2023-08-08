
def solution(money):
    coin = [10, 50, 100, 500, 1000, 5000, 10000, 50000]
    counter = 0
    idx = len(coin) - 1
    while money: # monoy가 0이 될때까지 반복
        counter += money // coin[idx] # 제일 큰 화페부터 지폐를 반환
        money %= coin[idx]  ## 반환된 금액은 조외하고 나머지만 money에 저장
        idx -= 1
    return counter


money = 2760
ret = solution(money)

print("solution 함수의 반환 값은", ret, "입니다.")
def solution(t, p):
    answer = 0

    # 문자을 p읠 길이 값
    length = len(p)
    num = ''
    # t문자열에서 p의 부분문자열을 찾기 위한 범위 t길이에서 p길이 뺀 후 1 더해주기
    for i in range((len(t)-length)+1):
        # 부분문자열 구하는 범위
        a = t[i:i+length]
        # 구한 부분문자열을 num 빈 문자열에 더 해줌 ,기준으로 잘라주기 위해 +','해줌
        num += a+','
    # 마지막에 ,까지 들어가서 마지막 원소 제외한 모든 원소 가져오기
    num = num[:-1]

    a = num.split(',')
    # p보다 작거나 같은 값이 있다면 answer+1해줌
    for i in a:
        if i <= p:
            answer+=1

    return answer


t = "500220839878"
    #"500220839878"
    #"3141592"
p = "7"
    #"7"
    #"271"
print(solution(t, p))
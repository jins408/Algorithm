def solution(food):
    answer = ''

    for i in range(1, len(food)):
        # 짝수,홀수 인지 먼저 구분 ex)food[i]=3이면 두 선수가 하나씩 나눠 가질 수 있음(나머지 1은 2명이 나눌 수 없는 음식)
        a = food[i]//2
        # a의 수만큼 반복해서 빈문자열에 숫자를 넣어줌
        for j in range(a):
            answer += str(i)
    print(answer)
    # 두 선수가 똑같이 나눠 가지기 때문에, 0(물)을 기준으로 거꾸로 숫를 돌려서 문자열에 붙여줌
    a = answer[::-1]
    answer = answer+"0"+a

    return answer


food=[1, 3, 4, 6]
    #[1, 7, 1, 2]
print(solution(food))
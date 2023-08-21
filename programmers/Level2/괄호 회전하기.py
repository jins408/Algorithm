def solution(s):
    answer = 0

    temp = []
    cnt = 0

    index = 0
    while len(s) >= index+1:
        for i in s:
            temp.append(i)
            if temp[-2:] == ['[',']'] or temp[-2:] == ['(' ,')'] or temp[-2:] == ['{','}'] and len(temp)>=2:
                for _ in range(2):
                    temp.pop()
        index += 1
        if len(temp) == 0:
            cnt += 1
        else:
            temp = []
        # 왼쪽으로 한칸씩 회전시켜주는 구간
        s = s[1:]+s[0]

    answer = cnt

    return answer

s = "[](){}"
    #"}]()[{"
    #"[](){}"
print(solution(s))
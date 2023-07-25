import re
def solution(dartRbesult):
    answer = 0

    # 숫자와 문자를 구분해주는 함수 re.split('([^0-9])', 문자열)
    # 리스트의 공백 요소를 제거해 주기 위해 join 사용
    dartResult = re.split('([^0-9])', dartRbesult)
    dartResult = ' '.join(dartResult).split()
    print(dartResult)

    # *,# 인 경우 2배해주고 -1곱해주는 작업을 하기위해 따로 score배열에 숫자 계산한 것을 넣어줌
    score = []
    for i in range(1,len(dartResult)):
        if dartResult[i] == "S":
            score.append(int(dartResult[i-1])**1)
        elif dartResult[i] == "D":
            score.append(int(dartResult[i-1])**2)
        elif dartResult[i] == "T":
            score.append(int(dartResult[i-1])**3)
        elif dartResult[i] == "*":
            # 1보다 큰경우 조건을 준 이유는 *가 처음으로 나오면 앞에 숫자 하나에만 2배를 해주고
            # 중간에 *가 나오면 해당 숫자와 그 전에 나왔던 숫자 둘다 2배를 해줘야하기때문에 if조건을 줌
            if len(score) > 1:
                score[-2] = score[-2]*2
                score[-1] = score[-1]*2
            else:
                score[-1] = score[-1]*2
        elif dartResult[i] == "#":
            # 해당하는 숫자에 -1을 곱해줘서 계산해줘야 하므로
            score[-1] = score[-1]*-1

    return sum(score)
            # score 배열에 모든 숫자를 더해 준다.

dartResult="1S*2T*3S"
print(solution(dartResult))
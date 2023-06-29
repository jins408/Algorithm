def arr(number, num, total):
    # num 숫자 만큼 연속된 수의 합이 total되는 경우를 찾아주는 함수
    answer = []
    a = 0
    while True:
        sum = 0
        #number 배열에서 연속된 num수만큼의 합을 더해줌
        for i in range(a, a + num):
            sum += number[i]
            answer.append(number[i])
        if sum == total:
            break
        else:
            # total값이 아니면 append해준 answer배열을 초기화해줌
            answer = []
        # 연속된 수의 합이 total이 아니면 한칸 이동한 인덱스부터 연속된 num까지 확인하기 위해 a+=1을 해줌
        a += 1

    return sorted(answer)


def solution(num, total):
    number = []
    # num=99 total=0 일 경우
    if total == 0:
        # number배열에 음수 양수 다 들어가야 하기 때문에 num을 2로 나눔
        end = round(num/2)
        # num=1 이고 total=0 이면 연속되는 수를 더했을 때 나오는 수는 0밖에 없음
        if end == 0:
            return [0]
        # 음수부터 양수까지 number에 다 넣어주고
        for i in range(-end,end):
            number.append(i)
        # 함수를 탐
        arr(number, num, total)
    else:
        for i in range(-total, num + total + 1):
            number.append(i)
        arr(number, num, total)

    return arr(number, num, total)

num = 1
total = 0
print(solution(num,total))

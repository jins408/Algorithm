def solution(a, b):
    answer = 0

    day = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    # 1월1일이 금요일이므로 7로 나눴을 때 인덱스 1이 금요일로 나오게 배열을 설정
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    # 각 달의 날짜만큼 배열로 저장

    # month배열에 (a-1)월까지 더한수에 <- 3월이면 2월까지의 날짜 다 더한수
    for i in range(a-1):
        answer += month[i]

    # a월 이전까지의 각 달별 일수를 모두 더하고 b일을 또 더하고 1을 빼줍니다.
    answer += b-1
    # 7로 나눈 나머지의 인덱스에 해당하는 수 반환
    answer = answer%7

    return day[answer]

a = 5
b = 24
print(solution(a, b))
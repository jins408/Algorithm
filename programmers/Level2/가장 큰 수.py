def solution(numbers):
    answer = ''

    # 문자열 형태로 바꿔서 진행하기 위해 형변환을 해줌
    numbers = [str(i) for i in numbers]
    #numbers.sort(reverse=True)

    # max값을 뽑기위해서 큰 숫자가 제일 앞으로 올 수 있게 만들기 위해 lambda 정렬을 사용
    # 문자열은 아스키값으로 치환되서 정렬되기 때문에 첫번째 인덱스값으로 비교를 합니다.
    # (666,101010,222)여기서는 아스키값으로 보면 1: 81, 2: 82, 6:86 이기 때문에  -> [6,2, 10]
    numbers.sort(key=lambda x: x*3, reverse=True)
    print(numbers)

    for i in numbers:
        answer += i

    # '000'인 경우 '0'으로 바꾸기 위해 int형으로 바꾸고 다시 str형태로 바꿔준다.
    return str(int(answer))

numbers = [6, 10, 2]
    #[3, 30, 34, 5, 9]
    #[6, 10, 2]
print(solution(numbers))
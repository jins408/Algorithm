def solution(numbers, k):
    answer = 0
    # 인덱스 찾는 방법
    # 공을 받는 사람 순서를 찾습니다.(k * 2)
    # 공을 던지는 사람 순서로 변경합니다.((K - 1) * 2)
    # 순환되는 구조이므로 나머지를 통해 위치를 찾습니다. % people

    people = len(numbers)

    






    '''
    # len(numbers) 짝수일 때
    if len(numbers)%2 == 0:
        num = 0
        while num < k:
            for i in range(len(numbers)):
                if i % 2 == 0:
                    num += 1
                    answer = numbers[i]
                    if num == k:
                        break

    else:
        num = 0
        while num < k :
            answer = numbers[num]
            num += 2
            if answer == numbers[-1]:
                for i in range(1, len(numbers)):
                    if i%2 != 0:
                        answer = numbers[i]
                        if answer == numbers[-1]:
                            answer = numbers[1]
    '''

    return answer

numbers=[1, 2, 3,4]
k=2
print(solution(numbers, k))
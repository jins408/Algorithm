def solution(numbers, k):
    answer = 0
    # 인덱스 찾는 방법
    # 공을 받는 사람 순서를 찾습니다.(k * 2)
    # 공을 던지는 사람 순서로 변경합니다.((K - 1) * 2)
    # 순환되는 구조이므로 나머지를 통해 위치를 찾습니다. % people

    index = 0
    # k 숫자 하나씩 줄어가면서 index위치 확인
    while k > 1:
        index += 2
        index %= len(numbers)
        #print(index, end="")
        k -= 1
    return numbers[index]

numbers=[1, 2, 3,4,5]
k=5
print(solution(numbers, k))



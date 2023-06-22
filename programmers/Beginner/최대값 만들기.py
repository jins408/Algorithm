def solution(numbers):
    answer = 0

    num = 0
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] * numbers[j] > num:
                num = numbers[i] * numbers[j]
            if len(numbers) == 2:
                num = numbers[i] * numbers[j]

    return num


number = [7,-7]
# [1, 2, -3, 4, -5]
# 배열에 원소 값이 최대값과 최소값만 있는 경우도 생각해야함 
print(solution(number))
def solution(numbers):
    answer = 0

    max = 0
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] * numbers[j] > max:
                max = numbers[i] * numbers[j]
                answer = max

    return answer

numbers=[1,2,3,4,5]
print(solution(numbers))
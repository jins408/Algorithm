def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        cnt = 0
        num = numbers[i]
        for j in range(i,len(numbers)):
            if num < numbers[j]:
                answer.append(numbers[j])
                break
            else:
                cnt += 1
                continue
        if cnt == len(numbers)-i:
            answer.append(-1)

    return answer

numbers = [2, 3, 3, 5]
    #[9, 1, 5, 3, 6, 2]
print(solution(numbers))
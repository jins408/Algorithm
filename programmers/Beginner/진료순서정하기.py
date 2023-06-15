def solution(emergency):
    answer = []
    new_arr = sorted(emergency, reverse=True)

    for i in range(len(emergency)):
        for j in range(len(new_arr)):
            if emergency[i] == new_arr[j]:
                answer.append(j+1)


    return answer


emergency = [1, 2, 3, 4, 5, 6, 7]
    #[3, 76, 24]
print(solution(emergency))
def solution(answers):
    answer = []
    num1 = [1, 2, 3, 4, 5]
    num2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    result_num1 = 0
    result_num2 = 0
    result_num3 = 0

    # 수포자1가 정답을 맞춘 개수를 구하기 위한 로직
    for i in range(0,len(answers),len(num1)):
        for j in range(i, len(num1)+i):
            if j == len(answers):
                break
            if answers[j] == num1[j%5]:
                result_num1 += 1
    # 수포자2가 정답을 맞춘 개수를 구하기 위한 로직
    for i in range(0,len(answers),len(num2)):
        for j in range(i,len(num2)+i):
            if j == len(answers):
                break
            if answers[j] == num2[j%8]:
                result_num2+=1
    # 수포자3가 정답을 맞춘 개수를 구하기 위한 로직
    for i in range(0,len(answers),len(num3)):
        for j in range(i, len(num3)):
            if j == len(answers):
                break
            if answers[j] == num3[j%10]:
                result_num3+=1

    # 세명 중 최대값을 찾아서
    max_score = max(result_num1, result_num2, result_num3)

    # 최대값과 같은 값을 가지면 result_num1값과 비교하여 해당 번호를 넣어줌
    # 최대값이 하나면 answer에 한개만 append될 것이고, 동등한 값이 있다면 그거에 맞게 번호가 들어감
    if (max_score == result_num1):
        answer.append(1)
    if (max_score == result_num2):
        answer.append(2)
    if (max_score == result_num3):
        answer.append(3)
    return answer

answes = [5, 5, 5, 5, 5, 5, 5]
    #[1,3,2,4,2]
    #[5, 5, 4, 2, 3]
    #[5, 5, 5, 5, 5, 5, 5, 5]
    #[1,2,3,4,5]
print(solution(answes))
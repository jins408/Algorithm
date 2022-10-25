answers = [1,2,3,4,5]

def solution(answers):
    result = []

    num1 = [1, 2, 3, 4, 5]
    num2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score = [0,0,0]  ## 명의 수포자가 맞춘 개수를 넣을 리스트

    for i, answer in enumerate(answers):
        if answer == num1[i%len(num1)]: ## 리스트에 가지고 있는 값을 끝까지 체크하기 위해서 리스트의 길이만큼 나눠 줌
            score[0] += 1
        if answer == num2[i%len(num2)]:
            score[1] += 1
        if answer == num3[i%len(num3)]:
            score[2] += 1

    for i, s in enumerate(score):
        if s == max(score):
            result.append(i+1)


    return result

print(solution(answers))
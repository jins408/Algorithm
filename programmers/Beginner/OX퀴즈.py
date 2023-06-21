def solution(quiz):
    answer = []

    for i in quiz:
        a, b = i.split("=")
        a = a.split()
        if a[1] == "+":
            sum = int(a[0]) + int(a[2])
            if sum == int(b):
                answer.append("O")
            else:
                answer.append("X")
        if a[1] == "-":
            sum = int(a[0])-int(a[2])
            if sum == int(b):
                answer.append("O")
            else:
                answer.append("X")


    return answer


quiz =["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]
print(solution(quiz))
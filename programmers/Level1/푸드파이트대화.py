def solution(food):
    answer = ''

    for i in range(1, len(food)):
        a = food[i]//2
        for j in range(a):
            answer += str(i)
    print(answer)
    a = answer[::-1]
    answer = answer+"0"+a

    return answer


food=[1, 3, 4, 6]
    #[1, 7, 1, 2]
print(solution(food))
def solution(s):
    answer = ''

    s = s.split(' ')
    print(s)

    for i in s:
        answer += ' '
        for j in range(len(i)):
            if j%2 == 0 :
                answer += i[j].upper()
            else:
                answer += i[j].lower()
    return answer[1::]


s = "try hello world"
print(solution(s))
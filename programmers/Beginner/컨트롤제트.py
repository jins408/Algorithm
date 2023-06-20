def solution(s):
    answer = 0

    aa = s.split(" ")

    for i in range(len(aa)):
        if aa[i] == 'Z':
            answer = answer-(int(aa[i-1]))
        else:
            answer += int(aa[i])

    return answer


s="-1 -2 -3 Z"
print(solution(s))
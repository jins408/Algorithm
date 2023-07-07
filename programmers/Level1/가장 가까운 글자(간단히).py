def solution(s):

    answer = []
    for i in range((len(s))):
        t = s[:i]
        # rfind()문자열을 오른쪽부터 찾는다
        idx = t.rfind(s[i])
        # 예로 t = "bana" i=4일때, s[i]="n" t의 인덱스는 0,1,2,3 문자'n'의 인덱스는 2
        # 오른쪽부터 찾는이유 끝에서부터 살펴봐야 제일 최근에 같은 문자가 나온걸 찾을 수 있기 때문에
        if idx == -1:
            answer.append(-1)
        else:
            # 4-2 = 2
            answer.append(i - idx)


    return answer


s="banana"

print(solution(s))
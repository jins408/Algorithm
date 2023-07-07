def solution(s):
    answer = []

    char = ''
    for i in s:
        cnt = 0
        char += i
        # 확인한 문자를 넣어주기 위해 char빈 문자열에 s문자 넣어줌
        for j in range(len(char)):
            if i == s[j]:
                cnt += 1
        # s문자열에 바교했을때 똑같은 문자가 없다면 -1
        if cnt == 1:
            answer.append(-1)
        # 중복되는 문자를 cnt개수가 2개 이상인 것에서 찾음
        elif cnt > 1:
            k = -2
            num = 1
            # char끝에 문자와 바로 앞에 문자가 같다면 바로 num을 넣어줌
            if char[k] == char[-1]:
                answer.append(num)
            # 바로 앞에 문자와 똑같지 않다면 while문 돌려서 똑같은 문자가 나올때까지 반복해줌
            else:
                # char문자열의 끝에문자부터 비교에서 제일 끝에문자와 제일 가까운 똑같은 문자를 찾음
                while char[k] != char[-1]:
                        k -= 1
                        num += 1
                        if char[k] == char[-1]:
                            answer.append(num)


    return answer


s="banana"
    #"banana"
print(solution(s))
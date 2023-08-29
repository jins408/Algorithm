def solution(msg):
    answer = []

    # dic = {chr(i + 64): i for i in range(1, 27)}
    index = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,
             'M':13,'N':14,'O':15,'P':16,'Q':17,'R': 18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

    # w = 현재문자 c = 다음문자
    w = c = 0
    num = 26
    while True:
        c += 1
        if c == len(msg):
            answer.append(index[msg[w:c]])
            break
        # 현재글자+다음글자가 색인에 없다면,
        if msg[w:c+1] not in index:
            num += 1
            index[msg[w:c+1]] = num # 색인 추가
            answer.append(index[msg[w:c]]) # answer에 색인번호 추가
            w = c   # 현재글자를 다음글자로 옮겨줌

        # 만약 [현재글자+다음글자]가 사전에 있다면, w값은 변하지 않고 c의 값만 1씩 증가
        # -> 2글자보고 그다음 3글자확인, 3글자보고 그다음 4글자확인(이런식으로 반복되기때문에)
    return answer

msg = "KAKAO"
print(solution(msg))
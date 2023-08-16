def solution(s):
    answer = ''

    a = []
    word = s.split(' ')

    for i in word:
        # 공백이 아니고 첫번째글자가 소문자이고, 문자일때만 대문자로 변경
        if i != "" and i[0].lower() and i[0].isalpha():
            i = i[0].upper()+i[1:].lower()
            a.append(i)
        else:
            # 첫글자가 숫자여도 그 뒤에 모든 단여들은 소문자로 되어야한다.
            i = i.lower()
            a.append(i)

    # 리스트에 공백 유지해서 문자열에 넣을때, " ".join() 사용
    answer = " ".join(a)

    return answer

s = "1HELLO 1WORLD"
print(solution(s))
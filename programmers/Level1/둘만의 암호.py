def solution(s, skip, index):
    answer = ''

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    # skip에 포함된 영단어를 제거한 알파벳으로만 확인하기 위해 먼저 제거해 준다.
    for i in skip:
        if i in alphabet:
            alphabet.remove(i)
    alphabet = ''.join(alphabet)

    print(alphabet)

    # 문자열s에 해당하는 단어의 인덱스 위치해서 index값 다음으로 오는 단어를 찾아야함
    for i in range(len(s)):
        for j in alphabet:
            if s[i] == j:
                # j의 인덱스 위치부터 index값을 더한 위치를 봐야하기때문에 둘이 더해준다.
                a_index = alphabet.index(j)+index
                # 전체 알파벳 길이보다 작다면 해당하는 a_index값으로 찾아서 그대로 넣어준다.
                if a_index < len(alphabet):
                    answer += alphabet[a_index]
                    break
                else:
                    # z마지막까지 도달했는데 아직 살펴볼 값이 남아있다면 다시 첫글자 부터 확인해야하므로
                    # a_index에서 전체 알파벳길이를 나눈 나머지 값으로 다시 첫글자부터 확인하도록 한다
                    # -> 나머지가 0인경우, 인덱스0부터(첫글자)부터 다시 살펴보기때문에
                    x = a_index%len(alphabet)
                    answer += alphabet[x]
                    break

    return answer

s = "klmnopqrstuvwxyz"
    #"aukks"    -> "happy"
    #"klmnopqrstuvwxyz" ->"opqrstuvwxyzklmn"
skip="abcdefghij"
    #"wbqd"
    #"abcdefghij"
index =20
    #5
    #20
print(solution(s, skip,index))
words = []
def create_word(lev, s):
    global words

    dict= ['A', 'E', 'I', 'O', 'U']
    words.append(s)
    for i in range(5):
        # dict길이보다 작을때까지만 해준다.
        # 그래야 AAAAA -> AAAA로 다시 돌아간 다음 AAAAE로 만들어 줄 수있다.
        if lev < 5:
            create_word(lev+1,s+dict[i])

def solution(word):
    answer = 0
    # 'A', 'E', 'I', 'O', 'U' 문자로 만들 수 있는 모든 형태를 담을 words배열을 global변수로 받는다
    global words
    # 모든 경우의 수를 words리스트에 담아줄 함수
    create_word(0,'')
    print(words)
    for idx, i in enumerate(words):
        if i == word:
            answer = idx

    return answer


word = "AAAAE"
print(solution(word))
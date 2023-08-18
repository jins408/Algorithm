def solution(n, words):
    answer = [0,0]

    cnt = 0
    used_word = []
    used_word.append(words[0])
    print(used_word[0][-1]) # 첫단어의 마지막 글자 확인
    print(words[1][0]) # 다음 단어의 첫번째 글자 확인
    for i in range(1, len(words)):
        cnt += 1
        # used_word리스트에 동일한 단어가 없고, 첫번째단어 끝글자와 다음 단어 첫번째글자가 같은지 확인
        if words[i] not in used_word and used_word[i-1][-1] == words[i][0]:
            used_word.append(words[i])
        else:
            answer[0] = cnt%n+1   # 탈락번호
            answer[1] = cnt//n+1  # 탈락차례
            break

    return answer

n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
    #["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
    #["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
print(solution(n,words))
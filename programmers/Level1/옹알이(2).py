def solution(babbling):
    answer = 0

    word = ["aya", "ye", "woo", "ma" ]

    for i in babbling:
        for j in word:
            # 연속되는 단어가 아니면 공백으로 바꿔준다.
            if j*2 not in i:
                i = i.replace(j," ")
        # isspace() 모두 공백인지 확인해주는 함수
        if i.isspace():
            # 공백인것만 +1 해준다
            answer +=1
    return answer

babbling =["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]
    #["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]
    #["ayayeayayeaya"]
print(solution(babbling))
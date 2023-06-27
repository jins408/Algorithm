def solution(babbling):
    answer = 0

    word = ["aya", "ye", "woo", "ma"]

    ww = ''
    # babbling의 원소 값을 하나하나 체크해주기 위해 for문 돌림
    for i in babbling:
        # babbling의 각각의 원소를 word와 비교하기 위해서 aa 문자열 초기화
        aa = ''
        for j in word:
            # babbling 원소 값과 word원소 값이 일치하면 aa 문자열에 넣어줌
            if j in i:
                aa += j
        # 문자가 만들어진 순서에 상관없이 word에 모두 동일한 원소가 존재한다면 문자열의 길이가 같아지므로 문자열 길이로 정답 판단
        if len(aa) == len(i):
            ww += aa+' '

    result = ww.split(' ')

    # -1 해주는 이유는 문자를 더해줄때 공백과 함께 더해줬으므로 공백 개수는 카운트하지 않기 위해 -1해줌
    answer = len(result)-1

    return answer


babbling = ["aya", "yee", "u", "maa", "wyeoo"]
#["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]
print(solution(babbling))
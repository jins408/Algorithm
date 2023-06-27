def solution(babbling):
    answer = 0

    word = ["aya", "ye", "woo", "ma"]

    ww = ''
    for i in babbling:
        aa = ''
        for j in word:
            if j in i:
                aa += j
        if len(aa) == len(i):
            ww += aa+' '

    result = ww.split(' ')

    answer = len(result)-1

    return answer


babbling = ["aya", "yee", "u", "maa", "wyeoo"]
#["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]
print(solution(babbling))
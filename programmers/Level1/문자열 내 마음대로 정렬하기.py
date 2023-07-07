def solution(strings, n):
    answer = []

    # 먼저 문자열 배열을 정렬
    strings = sorted(strings)
    # n 번째 문자열을 저장하는 배열
    eng = []
    for i in strings:
        for j in range(len(i)):
            if j == n:
                eng.append(i[j])

    # n번째 문자열을 담은 배열도 정렬
    eng = sorted(eng)
    print(eng)

    for i in eng:
        for j in strings:
            # strings의 문자열의 n번째 문자와 eng의 문자가 같다면, answer에 담아주고
            if j[n] == i:
                answer.append(j)
                # strings배열에서 해당 문자열을 제거해준다(중복을 피하기 위해)
                strings.remove(j)
                # break해주는 이유 -> 이미 알파벳순으로 정렬을 했기때문에 같은 문자를 찾았다면 그 뒤에 문자까지 확인하지 않고 반복문을 빠져나온다(끝까지 확인할 필요x)
                # 반례 ['ba', 'aea', 'ce', 'aee'] 1
                break

    return answer

strings=["sun", "bed", "car"]
    #["abzcd","cdzab","abzfg","abzaa","abzbb","bbzaa"] 2
    #["abce", "abcd", "cdx"] 2
    #["sun", "bed", "car"]
    #['ba', 'aea', 'ce', 'aee'] 1
n = 2
print(solution(strings,n))
def solution(strings, n):
    answer = []

    index = []
    for i in strings:
        for j in range(len(i)):
            if j == n:
                index.append(i[j]+i)
                # n번째 인덱스를 찾고 해당하는 문자열을 같이 index배열에 넣어준다

    print(index)
    # 정렬해서
    index.sort()
    print(index)
    # n번째 문자열을 제거한 나머지 문자열만 추출하면 끝남
    for i in index:
        answer.append(i[1:])

    return answer

strings=["sun", "bed", "car"]
    #["abzcd","cdzab","abzfg","abzaa","abzbb","bbzaa"] 2
    #["abce", "abcd", "cdx"] 2
    #["sun", "bed", "car"]
    #['ba', 'aea', 'ce', 'aee'] 1
n = 1
print(solution(strings,n))
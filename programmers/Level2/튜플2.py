def solution(s):
    answer = {} #[] 배열대신 딕셔너리로 교체

    s = sorted(s[2:-2].split("},{"), key=len) #특정 키 값으로 정렬가능
    #  s=['3', '2,3', '4,2,3', '2,3,4,1']

    for tuples in s:
        elements = tuples.split(",")
        # elements = ['3'] ['2', '3'] ['4', '2', '3'] ['2', '3', '4', '1']
        for element in elements:
            number = int(element) #['3'] -> 3 문자열을 숫자로
            if number not in answer:
                answer[number] = 1  # 딕셔너리 키 사용(값(value)은 아무거나)
                # answer = {3:1, 2:1, 4:1, 1:1}

    return list(answer) # 딕셔너리 키값만 배열의 인자가 됨


s="{{4,2,3},{3},{2,3,4,1},{2,3}}"

print(solution(s))
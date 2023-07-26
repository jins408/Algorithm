def solution(X, Y):
    answer = ''

    # 각 숫자의 개수를 세기
    x_list = []
    for i in range(10):
        x_list.append(X.count(str(i)))
    #print(x_list)
    y_list = []
    for i in range(10):
        y_list.append(Y.count(str(i)))
    #print(y_list)

    for i in range(9, -1,-1): # 큰 숫자부터 answer에 추가해주도록 한다.(공통된 수 중에 제일 큰값을 결과값으로 받아야해서)
        for _ in range(min(x_list[i], y_list[i])): #x_list[i]와 y_list[i] 중 더 작은 값이 숫자 i의 공통된 개수
            # 배열중에 작은 값의 개수 만큰 안쪽 for을 돈다.
            # 3,2 인경우 작은 값인 2가 왔을때 2번 반복해서 해당 인덱스i값이 answer에 i(인덱스)동일한 숫자가 들어간다.
            answer += str(i)

    if answer == "":
        answer = '-1'  # 반환된 문자열이 비어있으면 '-1' 리턴
    elif answer[0] == '0':  # 첫 문자가 '0'이다 == 모든 문자가 '0'으로 이루어져 있다.
        answer = '0'
    return answer

X = "100"
    #"5525"
    #"12321"
Y = "123450"
    #"1255"
    #"42531"
print(solution(X, Y))
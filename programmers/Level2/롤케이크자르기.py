
def solution(topping):
    answer = 0

    first = set()   # 중복제거해서 담을 변수
    second = {}     # topping리스트의 원소별 개수를 담을 딕셔너리
    for i in topping:
        d = second.get(i)
        if d == None:
            second[i] = 1
        else:
            second[i] += 1

    for j in topping:
        first.add(j)    # topping에서 원소 하나씩 first에 담는다.
        second[j] -= 1  # second 딕셔너리에 topping 원소에 해당하는 value의 개수를 -1 해준다.
        if second[j] == 0:  # 해당 원소의 value값이 0이되면
            del second[j]   # 딕셔너리에서 제거해준다.
        if len(first) == len(second):   # 길이가 서로 같아지면(나눠가진 토핑의 개수가 같다는 것) answer에 +1 해준다.
            answer += 1

    return answer

topping = [1, 2, 1, 3, 1, 4, 1, 2]
    #[1, 2, 3, 1, 4]
    #[1, 2, 1, 3, 1, 4, 1, 2]
print(solution(topping))
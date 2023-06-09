def solution(s):
    # {}제거 이중중괄호이기 때문에 필요없는 부분

    # 중괄호를 제거한 숫자 문자열 -> 문자열을 숫자로 변환 -> 숫자
    # 중괄호를 제거한 숫자 문자열
    # data = s[2:-2]
    # data = 4,2,3},{3},{2,3,4,1},{2,3
    #문자열을 숫자로 변환
    data = s[2:-2].split("},{")
    # data = ['4,2,3', '3', '2,3,4,1', '2,3']
    # 오름차순으로 정렬 (쪼개진 문자열을 길이에 맞게 정렬)
    data = sorted(data, key=lambda x: len(x))
    # print(data) ['3', '2,3', '4,2,3', '2,3,4,1']

    #숫자만 가진 문자열만 뽑아냄
    # item = [3] [2, 3] [4, 2, 3] [2, 3, 4, 1]
    # value = 3 2 3 4 2 3 2 3 4 1
    answer = []
    for item in data:
        item = list(map(int, item.split(",")))
        for value in item:
            if value not in answer:
                answer.append(value)

    return answer


s="{{4,2,3},{3},{2,3,4,1},{2,3}}"

print(solution(s))
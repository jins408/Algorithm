def solution(array):
    # set을 이용해 array배열의 중복값을 제거
    keys = set(array)
    # 빈 딕셔너리 선언
    dict = {}
    max_freq = []
    # 중복값을 제거한 keys에 값을 이용해 array배열에 있는 원소들의 개수를 count하여 dict에 key:values 값으로 담음 dict={80:3, 90:2}
    for key in keys:
        dict[key] = array.count(key)
    # dict.values()의 values의 max값을 이용해 원소의 개수가 제일 많은 값을 max_freq배열에 넣어줌
    for key in keys:
        if dict[key] == max(dict.values()):
            max_freq.append(key)
    # 최대값이 중복이면 -1을 return해줘야 하므로 if으로 max_freq길이 값 체크
    if len(max_freq) > 1:
        answer = -1
    else:
        # dict.values() 최대값인 하나만 max_freq배열에 append해주므로 max_freq[0]으로만 값을 가져오면 됨
        answer = max_freq[0]
    return answer

array = [1, 2, 3, 3, 3, 4]
# [1, 2, 3, 3, 3, 4]
print(solution(array))
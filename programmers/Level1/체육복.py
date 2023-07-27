def solution(n, lost, reserve):
    answer = 0

    # 중복값을 제거하기 위해 정렬하는 과정이 필요
    #  n = 5, lost = [2, 4], reserve = [3, 1] 일때 i=3일때, i-1=2 lost[4] 되고 i=1일때, i-1,i+1 0,2로
    # lost에 존재하지 않아 lost[4]로 남게 되어 n-len(lost)=4가 된다.
    # 정답은 5가 나와야 하기 때문에 정렬하는 과정이 필요하다
    lost.sort()
    reserve.sort()

    # 공통으로 존재하는 요소를 각 배열에 제거한다
    # 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다.
    # 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다. 조건이 있기 때문에
    for i in reserve[:]:
        if i in lost:
            reserve.remove(i)
            lost.remove(i)

    print(reserve)
    print(lost)
    # 체육복 빌려 줄수 있는 범위 확인하기
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
        # 한 명에게만 빌려줄 수 있으므로 if - elif로 작성하여 하나의 조건에 대해서만 작업을 진행할 수 있도록 해야 한다.
        elif i+1 in lost:
            lost.remove(i+1)

    answer = n-len(lost)

    return answer

n = 5
lost = [2,4]
reserve = [3]
    #[1,3,5]
print(solution(n,lost,reserve))
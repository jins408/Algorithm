def solution(common):
    answer = 0

    # 등비수열
    # b가 a, c의 등비중항이고, 공비를 r이라고 하면 b = ar, c = br
    m = len(common) // 2
    # common배열에 첫번째 원소값이 0일때 나눌 수 없어서 a=0으로 줌
    if common[m-1] == 0:
        a = 0
    else:
        # 공비는 중앙값 나누기 바로 전 원소값으로 나눈 값
        a = common[m] // common[m - 1]

    #등차수열
    n = common[1]-common[0]

    # 현재원소값에서 구한 공차(n)를 더한 값이 다음 원소값과 같으면 등비수열계산
    if common[m]+n == common[m+1]:
        answer = common[-1]+n
    else:
        # 공차를 구한값이 아니라면 등비로 계산
        if common[1]%a == 0:
            answer = common[-1]*a

    return answer

common = [2,4,8]
print(solution(common))
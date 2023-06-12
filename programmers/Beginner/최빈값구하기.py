def solution(array):
    answer = 0

    # 배열의 길이만큼 0으로 채원 배열을 만듬(cnt배열의 인덱스를 활용하기 위해)
    cnt = [0]*(max(array)+1)

    # array의 배열의 값 하나를 array전체 값을 비교
    for i in array:
        num = 0
        for j in range(len(array)):
            # i == arrar[j] ex) i=80 array[0]=80 같다면 num+1(최빈값을 구해주기 위해 카운트)
            if i == array[j]:
                num += 1
        # cnt배열의 인덱스 값에 카운트한 num값을 넣어 줌
        cnt[i] = num

    # cnt배열의 최대값 구하기
    max_cnt = max(cnt)

    result = 0 #최빈값이 여러개인 경우를 확인하기 위해 for문을 돌면서 result+1
    for i in range(len(cnt)):
        if cnt[i] == max_cnt:
            result += 1
            # 최빈값이 하나만 존재하면 cnt배열의 인덱스 값으로 return
            answer = i

        #최빈값이 여러개인 경우는 reslt의 값이 2개 이상일때이므로
        if result >= 2:
            answer = -1

    return answer

array = [80,80,80,9,9,9]
# [1, 2, 3, 3, 3, 4]
print(solution(array))
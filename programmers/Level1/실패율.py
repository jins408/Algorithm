def solution(N, stages):
    answer = []

    # stages 오름차순으로 정렬 인덱스번호를 스테이지번호로 쓰기위해)
    stage = sorted(stages)
    print(stage)

    # 중복된 개수를 len(stages)길이와 나눠주기 위한 배열
    num = []
    # stage에서 N+1까지 범위중 같은 숫자가 있다면 cnt증가 시켜서 num에 넣어줌
    for i in range(1,N+1):
        cnt = 0
        for j in range(len(stage)):
            if i == stage[j]:
                cnt += 1
        num.append(cnt)

    length = len(stages)
    # 실패율을 넣어줄 배열
    fail = []
    for i in range(len(num)):
        # 0은 나눠주지 않기위해 그냥 0으로 넣어버림
        if num[i] == 0 and length == 0:
            fail.append(0)
        else:
            # float(실수)자료형으로 fail배열에 넣어줌
            fail.append(float(num[i]/length))
            # 그 숫자만큼 스테이지 길이에서 빼줌
            # 그리고 다시 num[i]와 나눠주기 반복
            length-=num[i]
    print(fail)

    # 오름차순으로 정렬해주기 위해 fail배열에서 제일 큰 수의 인덱스를 찾아서 answer에 넣어줌
    # 그리고 찾은 큰수는 제일 작은 수로 바꾸준다.
    for i in range(len(fail)):
        answer.append(fail.index(max(fail))+1)
        fail[fail.index(max(fail))] = -1

    return answer

N=2
stages= [1, 1, 1, 1]
    # [1, 2, 3, 2, 1] 4
    #[2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N,stages))
def solution(N, stages):
    answer = []

    set_stage = sorted(set(stages))
    print(set_stage)

    num = []
    for i in set_stage:
        num.append(stages.count(i))
    print(num)

    length = len(stages)
    fail = []
    for i in range(len(num)):
        fail.append(num[i]/length)
        length-=num[i]
    print(fail)

    if len(fail) == 1:
        answer.append(set_stage[0])
        for i in range(1,N):
            answer.append(i)
    else:
        for i in range(len(fail)):
            answer.append(fail.index(max(fail))+1)
            fail[fail.index(max(fail))] = -1

        a = answer.pop(0)
        answer.append(a)

    return answer

N=4
stages = [4,4,4,4,4]
    #[2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N,stages))
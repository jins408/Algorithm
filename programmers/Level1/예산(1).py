def solution(d, budget):
    answer = 0

    # d 예산 배열을 오름차순으로 정렬해 준다
    d.sort()
    # 배열의 길이만큼 while돌려서 배열의 원소 전체 더한 값이 budget보다 크면 길이를 -1만큼씩 줄어서 다시 더해준다.(이작업 반복)
    a = len(d)
    while a >= 0:
        sum = 0
        for i in range(a):
            sum += d[i]
        if sum > budget:
            a -= 1
        else:
            # sum이 budget과 같거나 작아지면 길이 값 반환
            answer = a
            break

    return answer


d =[2,2,3,3]
budget = 10
print(solution(d, budget))
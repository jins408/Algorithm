def solution(numlist, n):
    answer = []

    # n로부터의 거리가 같다면, 더 큰 수를 앞에 오도록 배치
    # 4-5 4-3 거리가 1로 같기 때문에 더 큰수인 5가 먼저 앞으로 나와서 4,5,3
    # 4-6, 4-2 거리가 2로 같기 때문에 더 쿤수인 6이 먼저 앞으로 나와서 4,5,3,6,2
    # 4-1 거리가 3으로 제일 크기 때문에 맨 마지막으로 4,5,3,6,2,1

    temp = []
    #sort_num = sorted(numlist)
    #print(sort_num)
    for i in numlist:
        if i < n:
            num = n - i
        else:
            num = i - n
        temp.append(num)

    set_temp = set(temp)
    a = sorted(set_temp)
    print(a)
    for i in range(len(a)):
        if a[i] < n:
            if n+a[i] in numlist and a[i]>0:
                answer.append(n+a[i])
            if n-a[i] in numlist:
                answer.append(n-a[i])
        else:
            answer.append(a[i]+n)

    return answer


numlist = [1, 2, 3, 4, 5, 6]
n = 4
# [36, 40, 20, 47, 10, 6, 7000, 10000]
print(solution(numlist, n))
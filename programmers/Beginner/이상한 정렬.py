def solution(numlist, n):
    answer = []

    # n로부터의 거리가 같다면, 더 큰 수를 앞에 오도록 배치
    # 4-5 4-3 거리가 1로 같기 때문에 더 큰수인 5가 먼저 앞으로 나와서 4,5,3
    # 4-6, 4-2 거리가 2로 같기 때문에 더 쿤수인 6이 먼저 앞으로 나와서 4,5,3,6,2
    # 4-1 거리가 3으로 제일 크기 때문에 맨 마지막으로 4,5,3,6,2,1

    temp = []
    #sort_num = sorted(numlist)
    #print(sort_num)

    # temp 배열에 n값을 기준으로 i가 n보다 작으면 n-i, i가 n보다 크면 i-n 차이값을 배열에 넣어줌
    # temp 차이값과 n값을 더하거나 빼주면, numlist있던 원소 값과 동일해줌 -> 이걸 이용해서 문제를 풀어줄 예정
    for i in numlist:
        if i < n:
            num = n - i
        else:
            num = i - n
        temp.append(num)

    # set로 temp 배열의 중복값 제거 (set은 순서 없이 마음대로 정렬되므로)
    # 중복제거하는 이유는 차이값이 동일한 경우 더 큰값이 우전적으로 나오게 해줘야하기때문에 중복제거해서 n+(차이값) n-(차이값) 둘다 계산해줌
    set_temp = set(temp)
    # 다시 정렬 시켜줌
    a = sorted(set_temp)
    print(a)
    for i in range(len(a)):
        if a[i] < n:
            # temp 원소값으로 +,- 함께 계산하지만 numlist 존재하는 원소값만 찾아서 넣어줌으로 동시에 계산 가능
            #  a[i]>0 해주는 이유는  numlist에 n값과 동일한게 있는 경우 +,- 한값이 두개 중복으로 들어가게 되어서 조건 추가해 줌
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
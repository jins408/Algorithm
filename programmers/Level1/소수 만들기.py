def fun(num):

    max_num = max(num)
    cnt = 0
    for i in range(len(num)):
        sum = 0
        for j in range(2,max_num+1):
            if num[i]%j == 0:
                sum += 1
            if sum >= 2:
                break
            # 쟈기 자신과 똑같은 수를 가진것만 소수이므로 j(인덱스)와 num[i] 같을때 cnt+1
            if sum == 1 and j == num[i]:
                cnt +=1
    return cnt

def solution(nums):
    answer = 0

    # 3개씩 더한 수
    num = []
    for i in range(0, len(nums)-2):
        for j in range(i+1,len(nums)):
            for k in range(j+1, len(nums)):
                num.append(nums[i]+nums[j]+nums[k])
    print(num)
    # 소수를 찾는 함수
    get_fun = fun(num)

    return get_fun

nums = [1,2,7,6,4]
    #[1,2,3,4]
print(solution(nums))
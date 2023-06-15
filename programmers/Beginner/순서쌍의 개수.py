def solution(n):
    answer = 0

    #약수구하기
    nums = []
    for i in range(1,n+1):
        if n%i == 0:
            nums.append(i)
    print(nums)

    ff = []
    #for i_row, i in enumerate(nums):
    for i_cell, j in enumerate(nums):
        #print(i_cell, j)
        #print(len(nums)-i_cell-1)
        #print(0, len(nums)-i_cell-1, nums[len(nums)-i_cell-1])

        a = (j, nums[len(nums)-i_cell-1])
        ff.append(a)
    answer = len(ff)


    return answer


n=20
print(solution(n))
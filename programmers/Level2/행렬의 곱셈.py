def solution(arr1, arr2):
    answer = []

    # A*B C*D 행렬은 B,C가 같아야함 -> 결과 행렬은 A*D
    # k -< 0,1
    for k in range(len(arr1)):
        num = []
        # i -> 0,1
        for i in range(len(arr2[0])):
            a = 0
            # j -> 0,1,2
            for j in range(len(arr1[0])):
                a += arr1[k][j]*arr2[j][i]
            num.append(a)
        answer.append(num)
    return answer


arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
    #[[1, 2, 3], [4, 5, 6]] ->[[14, 32], [32, 77]]
    #[[2, 3, 2], [4, 2, 4], [3, 1, 4]]
    #[[1, 4], [3, 2], [4, 1]]
arr2 =[[5, 4, 3], [2, 4, 1], [3, 1, 1]]
    #[[1, 4], [2, 5], [3, 6]]
    #[[5, 4, 3], [2, 4, 1], [3, 1, 1]]
    #[[3, 3], [3, 3]]
print(solution(arr1, arr2))
arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]

def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        sum = []
        for j in range(len(arr1[0])):
            sum.append((arr1[i][j]+arr2[i][j]))
        answer.append(sum)

    return answer


print(solution(arr1, arr2))
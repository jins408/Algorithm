
def solution(rows, columns, queries):
    answer = []

    arr = [[0]*columns for _ in range(rows)]
    num = 1
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = num
            num += 1
   # print(arr)

    for x1,y1,x2,y2 in queries:
        temp = arr[x1-1][y1-1]
        mini = temp

        # 왼쪽 세로
        for k in range(x1-1, x2-1):
            test = arr[k+1][y1-1]
            arr[k][y1-1] = test
            mini = min(mini, test)

        for k in range(y1-1, y2-1):  # 하단 가로
            test = arr[x2-1][k+1]
            arr[x2-1][k] = test
            mini = min(mini, test)

        for k in range(x2-1, x1-1, -1):  # 오른쪽 세로
            test = arr[k-1][y2-1]
            arr[k][y2-1] = test
            mini = min(mini, test)

        for k in range(y2-1, y1-1, -1):  # 상단 가로
            test = arr[x1-1][k-1]
            arr[x1-1][k] = test
            mini = min(mini, test)



    return answer

rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(rows, columns, queries))
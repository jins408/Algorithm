
def solution(rows, columns, queries):
    answer = []

    arr = [[0]*columns for _ in range(rows)]
    num = 1
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = num
            num += 1

    for x1,y1,x2,y2 in queries:
        # array[x1-1][y1-1]값은 array[x-1][y1]로 이동을 해줘야 하는 값인데
        # 첫번째 for문이 왼쪽 세로 부분이기 때문에 상단 가로 for문이 돌아갈 때 옮겨질 예정인 값
        temp = arr[x1-1][y1-1] # 8을 가지고있고
        # 현재 값을 옮기면서 array[x-1][y-1]값이 다른 값으로 대체되기 때문에 그 값을 저장해서 마지막에 넣어주기 위해 가지고 있는 것
        # 8이 있던 위치가 14로 바뀐다
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

        # tmp에 저장한 값을 다시 array[x1-1][y1-1] 에 넣어주는 과정이 마지막에 들어가야 한다.
        # 그 이후 회전한 값 중 제일 최솟값을 정답 배열에 추가해주면 한 회전이 끝난다.
        arr[x1-1][y1] = temp
        answer.append(mini)

    return answer

rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(rows, columns, queries))
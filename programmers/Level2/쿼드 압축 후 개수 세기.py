def solution(arr):
    answer = [0,0]
    n = len(arr)

    def compression(r, c, n):
        start = arr[r][c]
        for i in range(r, r+n):
            for j in range(c, c+n):
                # 매 시행마다 첫 원소를 지정하고, 다른 원소가 나올 경우 4 등분을 진행한다. -> 정사각형의 모든 수가 같지 않은 경우
                # i,j를 n만큼 돌아도 start와 계속 같다면 4등분을 하지 않고, answer[start] += 1 해준다 -> 정사각형의 모든 수가 같은 경우
                if arr[i][j] != start:
                    # 4분할
                    n = n//2
                    # n=4일 경우 시작점(시작좌표)가 (0,0),(0,2),(2,0),(2,2)로 나눠지기 때문에
                    compression(r,c,n)  # 왼쪽 위
                    compression(r,c+n,n) # 오른쪽 위
                    compression(r+n,c,n) # 왼쪽 아래
                    compression(r+n,c+n,n) # 오른쪽 아래
                    return
        answer[start] += 1

    compression(0, 0, n)
    return answer

arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
print(solution(arr))
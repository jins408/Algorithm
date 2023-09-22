def solution(arr):
    answer = [0,0]

    n = len(arr)

    def compression(r,c,n):
        start = arr[r][c]
        for i in range(r, r+n):
            for j in range(c, c+n):
                if arr[i][j] != start:
                    n = n//2
                    compression(r,c,n)
                    compression(r,c+n,n)
                    compression(r+n, c, n)
                    compression(r+n, c+n, n)
                    return
        answer[start] += 1


    compression(0,0,n)
    return answer

arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
print(solution(arr))
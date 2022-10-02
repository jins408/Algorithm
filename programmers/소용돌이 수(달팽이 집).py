
def solution(n):
    answer = 0

    arr = [[0 for j in range(n)] for i in range(n)]

    num = 1    #배열에 넣을 수
    k = n       #회전하는 횟수(수행 횟수) 5->4->4->3->3->2->2->1
    r = 0       #행
    c = -1       #열
    s = 1       #증가.감소 해줄 변수 i=i+1, i=i-1, j=j+1, j=j-1 이걸 합쳐서 i=i+s, j=j+s 라고 해줄 것이다.

    while k > 0:
        for i in range(k):
            c = c+s
            arr[r][c] = num
            num = num + 1
        k = k-1
        for j in range(k):
            r = r+s
            arr[r][c] = num
            num = num+1
        s = s*(-1)

    for x in range(n):
        answer += arr[x][x]
    return answer


n1 = 3
ret1 = solution(n1)

print("solution 함수의 반환 값은", ret1, "입니다.")

n2 = 2
ret2 = solution(n2)

print("solution 함수의 반환 값은", ret2, "입니다.")

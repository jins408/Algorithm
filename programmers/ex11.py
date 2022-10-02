arr = [[5,12,4,31],[24,13,11,2],[43,44,19,26],[33,65,20,21]]
k =4


def solution(arr, k):
    ## 일차원 배열에 다 넣어버려서 정렬해서 4번째로 작은 값 찾기
    list = []
    for i in arr:
        list += i
    list.sort()

    return list[k - 1] ## 인덱스틑 0부터 시작하니까 -1을 해줘야 4번째로 작은 값 찾을 수 있음

print(solution(arr,k))
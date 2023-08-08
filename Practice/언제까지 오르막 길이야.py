def solution(arr):
    answer = 0

    count = [0 for i in range(len(arr))]  # 증가하는 걸 카운트해주려고 0을 채운 배열을 만듬
    idx = 0
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            count[idx] += 1
        else:
            idx += 1

        answer = max(count)+1
    
    # return 값 조건 확인하기!! (문제에 나와있음)
    if answer < 2:
        return 1

    return answer


arr = [3, 1, 2, 4, 5, 1, 2, 2, 3, 4]
ret = solution(arr)

print("solution 함수의 반환 값은", ret, "입니다.")
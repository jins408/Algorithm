def solution(arr, K):
    # 여기에 코드를 작성해주세요.
    answer = 10000

    arr.sort()
    for i in range(len(arr)-(K-1)):
        dif = arr[i+K-1]-arr[i]
        if answer > dif:
            answer = dif

    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [9, 11, 9, 6, 4, 19]
K = 4
ret = solution(arr, K)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
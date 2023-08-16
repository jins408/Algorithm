def solution(A, B):
    answer = 0

    #[1,2,3]이라는 배열이 있다면 3이라는 숫자가 가장 적게 곱해졌을때가 최적의 해가 되는 문제
    A.sort()  # 각 배열을 오른차순
    B.sort(reverse=True) # 내림차순 정렬

    # 배열의 가장 큰값이 다른 배열의 가장 작은 값과 곱해지게 되서 최소값 갖는 결과를 return 해줌
    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer

A = [1, 4, 2]
B = [5, 4, 4]
print(solution(A, B))
def solution(number, k):
    answer = ''

    # 입력 받은 numbers를 리스트로 저장
    number = list(number)
    # result = number의 첫번째 요소를 꺼내어 result에 저장
    result = [number.pop(0)]

    for num in number:
        if result[-1] < num: #이전 요소(result의 마지막 요소) 가 현재 요소보다 작다면
            # 이전 요소가 남아있음 and 이전 요소(result의 마지막 요소) < 현재 요소 and 아직 k개의 수가 제거 안됨
            while result and result[-1] < num and k > 0:
                #결과의 마지막 요소 제거
                result.pop()
                k -= 1
            result.append(num)
        # 이미 k개의 수가 제거됨 또는 이전 요소(result의 마지막 요소)가 현재 요소보다 큼
        elif k == 0 or result[-1] >= num:
            # 결과에 현재 요소 추가
            result.append(num)

    # 아직 k개의 수가 제거 안된 경우
    if k > 0:
        #result의 뒤 부터 제거
        result = result[:-k]
    answer = ''.join(result)

    return answer

number = "1924"
k=2
print(solution(number, k))
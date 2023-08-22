def solution(elements):
    answer = 0

    n = len(elements)
    # 중복인 숫자를 제거해 주기 위해 set()
    num = set()

    for length in range(1, n+1):
        for start in range(n):
            # 범위를 초과하면
            if start + length > n:
                # 뒤에서부터 다시 앞에 숫자를 더해줌(원형이기 때문에 처음과 끝기 서로 연결되어 있다고 생각
                # -> 다시 처음으로 돌아가기 위해 (start + length)%n 나눈 나머지 값으로 값을 찾음
                num.add(sum(elements[start:] + elements[:(start + length)%n]))
            else:
                num.add(sum(elements[start:start+length]))

    answer = len(num)


    return answer


elements = [7,9,1,1,4]
print(solution(elements))
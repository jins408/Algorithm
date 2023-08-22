def solution(elements):
    answer = 0

    n = len(elements)
    # 중복인 숫자를 제거해 주기 위해 set()
    num = set()

    for length in range(1, n+1):
        for start in range(n):
            if start + length > n:
                num.add(sum(elements[start:] + elements[:(start + length)%n]))
            else:
                num.add(sum(elements[start:start+length]))

    answer = len(num)


    return answer


elements = [7,9,1,1,4]
print(solution(elements))
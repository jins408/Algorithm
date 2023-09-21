def solution(numbers):
    answer = []

    for num in numbers:
        # 짝수일때
        if num%2 == 0:
            # 짝수를 2진수로 변홨했을때 1의 자리수가 0이기 때문에 +1 해주면 된다.
            a = num+1
            answer.append(a)
        else:
            # 홀수 일때
            # 가장 작은 수가 되려면 0을 1로 바꾼 비트 자리 다음 비트를 0으로 만들어야 가장 작은 수가 된다.
            b = '0'+bin(num)[2:]
            idx = b.rfind('0')
            b = list(b)
            b[idx]  = '1'
            b[idx+1] = '0'
            # 리스트를 바꾼걸 다시 int형태로 바꿔준다.
            answer.append(int(''.join(b),2))

    return answer

numbers = [2,3]
print(solution(numbers))

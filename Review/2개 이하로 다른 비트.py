def solution(numbers):
    answer = []

    for num in numbers:
        if num%2 == 0:
            answer.append(num+1)
        else:
            b = '0'+bin(num)[2:]
            index = b.rfind('0')
            b = list(b)
            b[index] = '1'
            b[index+1] = '0'
            answer.append(int(''.join(b),2))

    return answer

numbers=[2,7]
print(solution(numbers))
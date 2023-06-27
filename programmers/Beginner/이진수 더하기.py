def solution(bin1, bin2):
    answer = []

    bin1 = list(bin1)
    bin2 = list(bin2)

    a = bin1[::-1]
    b = bin2[::-1]
    num1 = 0
    for i in range(len(a)):
        if a[i] == "1":
            num1 += 2**i
        if a[i] == "0":
            num1 += 0

    num2 = 0
    for i in range(len(b)):
        if b[i] == "1":
            num2 += 2 ** i
        if b[i] == "0":
            num2 += 0

    sum = num1+num2

    while sum >= 0:
        c = sum
        sum = c//2
        answer.append(c%2)
        if sum == 0:
            break
    answer = answer[::-1]
    answer = ''.join(str(s) for s in answer )

    return answer

bin1 = "10"
bin2 = "11"
print(solution(bin1, bin2))
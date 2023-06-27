def solution(bin1, bin2):
    answer = []

    bin1 = list(bin1)
    bin2 = list(bin2)

    a = bin1[::-1]
    b = bin2[::-1]
    # 2진수를 10진수로 바꾸기
    num1 = 0
    for i in range(len(a)):
        if a[i] == "1":
            num1 += 2**i
        if a[i] == "0":
            num1 += 0
    # 2진수를 10진수로 바꾸기
    num2 = 0
    for i in range(len(b)):
        if b[i] == "1":
            num2 += 2 ** i
        if b[i] == "0":
            num2 += 0
    # 10진수끼리 더해주고
    sum = num1+num2

    # 10진수를 다시 2진수로 바꾸기
    while sum >= 0:
        c = sum
        sum = c//2
        # 빈 배열에 넣어주고
        answer.append(c%2)
        if sum == 0:
            break
    # [0,0,0,1,1] 이런식으로 되서 다시 배열 거꾸로 정렬시켜주고
    answer = answer[::-1]
    # 리스트를 문자열로 바꿔줌
    answer = ''.join(str(s) for s in answer )

    return answer

bin1 = "10"
bin2 = "11"
print(solution(bin1, bin2))
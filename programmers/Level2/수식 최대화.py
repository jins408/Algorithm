def cal(check, num, op):
    tempboho = []
    temp = []
    for i in op:
        tempboho.append(i)
    for j in num:
        temp.append(j)

    memonum = 0
    while True:
        while(check[0] in tempboho):
            memonum = tempboho.index(check[0])

            temp[memonum] = checkboho(check[0], temp[memonum], temp[memonum+1])
            temp.pop(memonum+1)
            tempboho.pop(memonum)

        while (check[1] in tempboho):
            memonum = tempboho.index(check[1])

            temp[memonum] = checkboho(check[1], temp[memonum], temp[memonum + 1])
            temp.pop(memonum + 1)
            tempboho.pop(memonum)

        while (check[2] in tempboho):
            memonum = tempboho.index(check[2])

            temp[memonum] = checkboho(check[2], temp[memonum], temp[memonum + 1])
            temp.pop(memonum + 1)
            tempboho.pop(memonum)

        if temp[0] <= 0:
            temp[0] = temp[0] * -1
        break
    return temp[0]

def checkboho(str, a,b):
    if str == "*":
        return a*b
    elif str == "+":
        return a+b
    else:
        return a-b

def solution(expression):
    answer = []

    # 문자열 에서 숫자들만 split 하여 추출
    num = expression
    num = num.replace('*',' ')
    num = num.replace('+',' ')
    num = num.replace('-',' ')
    num = num.split(' ')
    # 문자열을 int형으로 형 변환해주기 위해
    nums = [int(i) for i in num]
    print(nums)
    # 문자열에서 +, -, * 만 추출
    operands = [ op for op in expression if not op.isdecimal()]
    print(operands)

    # 6가지 연산자 우선순위 다 계산해서 최대 값을 뽑아 주도록 한다.
    check = ["*","+","-"]
    answer.append(cal(check, nums, operands))
    check = ["*","-","+"]
    answer.append(cal(check, nums, operands))
    check = ["+","*","-"]
    answer.append(cal(check, nums, operands))
    check = ["+","-","*"]
    answer.append(cal(check, nums, operands))
    check = ["-","*","+"]
    answer.append(cal(check, nums, operands))
    check = ["-","+","*"]
    answer.append(cal(check, nums, operands))

    return max(answer)

expression = "100-200*300-500+20"
print(solution(expression))

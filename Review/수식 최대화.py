def cal(check, op, num):
    tempop = []
    temp = []

    for i in op:
        tempop.append(i)

    for j in num:
        temp.append(j)

    memonum = 0
    while True:
        # check[0]
        while(check[0] in tempop):
            memonum = tempop.index(check[0])
            temp[memonum] = chbuho(check[0], temp[memonum], temp[memonum+1])
            temp.pop(memonum+1)
            tempop.pop(memonum)
        # check[1]
        while(check[1] in tempop):
            memonum = tempop.index(check[1])
            temp[memonum] = chbuho(check[1], temp[memonum], temp[memonum+1])
            temp.pop(memonum+1)
            tempop.pop(memonum)
        # check[2]
        while(check[2] in tempop):
            memonum = tempop.index(check[2])
            temp[memonum] = chbuho(check[2], temp[memonum], temp[memonum+1])
            temp.pop(memonum+1)
            tempop.pop(memonum)

        if temp[0] <= 0:
            temp[0] = temp[0]*-1
        break
    return temp[0]

def chbuho(buho, a, b):
    if buho == "*":
        return a*b
    elif buho == "+":
        return a+b
    else:
        return a-b

def solution(expression):
    answer = []

    # 숫자랑 연산자 분리
    num = expression
    num = num.replace('*',' ')
    num = num.replace('+',' ')
    num = num.replace('-',' ')
    num = num.split(' ')

    nums = [int(i) for i in num]
    operands = [ ex for ex in expression if not ex.isdecimal()]

    # 연산자 우선순위 6가지 모두 확인
    check = ['*', '+', '-']
    answer.append(cal(check, operands, nums))
    check = ['*', '-', '+']
    answer.append(cal(check, operands, nums))
    check = ['+', '*', '-']
    answer.append(cal(check, operands, nums))
    check = ['+', '-', '*']
    answer.append(cal(check, operands, nums))
    check = ['-', '*', '+']
    answer.append(cal(check, operands, nums))
    check = ['-', '+', '*']
    answer.append(cal(check, operands, nums))

    return max(answer)

expression = "100-200*300-500+20"
print(solution(expression))
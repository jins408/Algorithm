def solution(polynomial):
    answer = ''

    a = polynomial.replace('x','2')
    b = a.split(' ')
    print(b)
    num = 0
    num2 = 0
    for i in b:
        if i[-1] == '2' and len(i) > 1:
            num += int(i[0:-1])
        elif i == '2':
            num += 1
        elif i == '1':
            num2 += 1
        elif i != '+' and i[-1] != 1:
            num2 += int(i)


    if num2 != 0 and num != 0:
        answer = str(num)+'x'+' '+'+'+' '+str(num2)
    elif num == 0:
        answer = str(num2)
    elif num == 2:
        answer = 'x'
    elif num2 == '1':
        answer = str(num2)+' '+str(num)+'x'
    elif len(str(num)) >= 1:
        answer = str(num)+'x'
    else:
        answer = str(num)+'x'

    return answer

polynomial="x + x + x"
#"3x + 7 + x"
print(solution(polynomial))
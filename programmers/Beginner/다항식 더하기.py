def solution(polynomial):
    answer = ''

    a = polynomial.split(' + ')
    print(a)
    num = 0
    num2 = 0
    for i in a:
        if i.isdigit():
            num += int(i)
        else:
            if i == 'x':
                num2 = num2+1
            else:
                num2 = num2+int(i[:-1])

    if num2 == 0:
        return str(num)
    elif num2 == 1:
        if num != 0:
            return 'x + '+str(num)
        else:
            return 'x'
    else:
        if num != 0:
            return f'{num2}x + {num}'
        else:
            return f'{num2}x'


polynomial="x + x + x"
#"3x + 7 + x"
print(solution(polynomial))
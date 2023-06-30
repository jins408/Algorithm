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
                num2+int(i[:-1])
            #num2 = num2+1 if i == 'x' else num2 + int(i[:-1])



    return answer

polynomial="3x + 7 + x"
#"3x + 7 + x"
print(solution(polynomial))
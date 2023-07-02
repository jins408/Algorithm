def solution(polynomial):
    answer = ''

    a = polynomial.split(' + ')
    print(a)
    num = 0
    num2 = 0
    for i in a:
        # 숫자이면 num 변수에 더해주기
        if i.isdigit():
            num += int(i)
        else:
            # 'x' 면 1이기 때문에 num2+1 해줌
            if i == 'x':
                num2 = num2+1
            else:
                # 3x, 12x 이런식이면 앞에 숫자 값만 가져오도록 [:-1]슬라이싱 해주고 num2에 더해줌
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
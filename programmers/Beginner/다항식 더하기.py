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

    # num2가 0면이 x계수가 없는 것이므로 num만 return
    if num2 == 0:
        return str(num)
    # num2가 1이면 x만 return해주면 됨 x는 1값을 의미
    elif num2 == 1:
        # num이 0이 아니면 x+num 으로 return 해줘야 하므로
        if num != 0:
            return 'x + '+str(num)
        # num 0 이면 x만 return
        else:
            return 'x'
    else:
        # num2가 0,1이 아닐때, 그리고 num이 값이 있을때 나눠서 return해줌
        if num != 0:
            return f'{num2}x + {num}'
        else:
            return f'{num2}x'


polynomial="x + x + x"
#"3x + 7 + x"
print(solution(polynomial))
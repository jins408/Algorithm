def solution(order):
    answer = 0

    num = '369'
    str_order = str(order)
    cnt = 0
    for i in str_order:
        if i in num:
            cnt += 1
    answer = cnt

    '''
     cnt = 0
    number = str(order)
    for i in number:
        if int(i) % 3 == 0:
            cnt += 1
            if int(i)//3 == 0:
                cnt -=1

    answer = cnt
        
    '''

    return answer

order = 33033
print(solution(order))
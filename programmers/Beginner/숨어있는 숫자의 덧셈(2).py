def solution(my_string):
    #answer = 0
    answer = 0
    temp = ''
    for i in my_string:
        if i.isdigit():
            temp += i
        else:
            if temp:
                answer += int(temp)
                temp = ''
    if temp:
        answer += int(temp)

    '''
    # 모든 알파벳을 공백으로 바꿔준다
    for i in my_string:
        if i.isalpha():
            my_string = my_string.replace(i, ' ')

    a = my_string.split(' ')
    for i in a:
        if i != '':
            answer += int(i)
    '''

    return answer

my_string="1a2b3c4d123Z"
print(solution(my_string))
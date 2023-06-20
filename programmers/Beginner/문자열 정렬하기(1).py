def solution(my_string):
    answer = []
    numbers = '0123456789'

    for i in my_string:
        if i in numbers:
            answer.append(i)

    result = list(map(int, answer))

    '''
    isdigit() 이용해서 푸는 방법
    for i in my_string:
        if i.isdigit():
            answer.append(int(i))
    answer.sort()
    '''

    return sorted(result)

my_string="hi12392"
print(solution(my_string))
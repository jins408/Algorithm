def solution(num_list, n):
    answer = []

    '''
    num = 0
    for i in range(len(num_list)//n):
        a = num_list[num:num+n]
        num += n
        answer.append(a)
    '''

    for i in range(0,len(num_list), n):
        a = num_list[i:i+n]

        answer.append(a)

    return answer


num_list = [1, 2, 3, 4, 5, 6, 7, 8]
n = 2
print(solution(num_list, n))
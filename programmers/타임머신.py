def solution(num):
    answer = []

    sum = num + 1

    str_num = str(sum)

    for i in str_num:
        if i == '0':
            i = '1'
        answer.append(i)

    result = ''.join(answer)
    return result


    ##answer = int(str(num+1).replace('0','1'))

num = 9949999
ret = solution(num)

print("solution 함수의 반환 값은", ret, "입니다.")
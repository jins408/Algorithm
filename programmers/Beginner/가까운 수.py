def solution(array, n):
    answer = 0
    array_dic = {}
    for i in array:
        array_dic[i] = abs(n-i)
    a = min(array_dic.values())

    num = []
    for values in array_dic:
        if array_dic[values] == a:
            num.append(values)

    answer = min(num)

    return answer

#[3, 10, 28] 20
#[1, 4, 2, 1] 3
array=[3, 10, 28]
n= 20
print(solution(array, n))
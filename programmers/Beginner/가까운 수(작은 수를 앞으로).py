def solution(array, n):
    answer = 0

    temp = []
    for i in array:
        temp.append(abs(i-n))
    Index = temp.index(min(temp))
    answer = array[Index]
    return answer

#[3, 10, 28] 20
#[1, 4, 2, 1] 3
array=[3, 10, 28]
n= 20
print(solution(array, n))


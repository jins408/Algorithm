def solution(array):
    answer = 0
    array.sort()

    num = len(array)//2
    answer = array[num]
    return answer


array = [9, -1, 0]
#[1,3,2,8,4,6] [9, -1, 0]
print(solution(array))
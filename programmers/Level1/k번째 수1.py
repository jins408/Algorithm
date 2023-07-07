def solution(array, commands):
    answer = []

    for num in commands:
        for i in range(len(num)):
            #commands 각 원소 값만큼[2,5] array배열을 슬라이싱
            arr = array[num[0]-1:num[1]]
            # 정렬해주고
            arr.sort()
            # commands 마지막 값[3]의 해당하는 arr에서 가져오기 위해
            answer.append(arr[num[2]-1])
            break
            #중복제거를 위해 break

    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))
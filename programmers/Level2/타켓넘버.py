def solution(numbers, target):
    answer = 0

    queue = [[0,0]]
    while len(queue) >0:
        # queue에 pop한 첫번째 값을 index 두번째 값을 a로 줌
        index, a = queue.pop()

        if index < len(numbers):
            # index는 numbers길이만큼 계속+1해주고, a값은 -,+를 번갈아가면서 해준다.
            # 이러한 작업을 반복 적으로 해줌
            queue.append([index+1, a+numbers[index]])
            queue.append([index+1, a-numbers[index]])

        # index가 numbers길이와 같고 a가 target과 같으면 answer +1해준다
        if index == len(numbers):
            if a == target:
                answer +=1

    return answer


numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers,target))
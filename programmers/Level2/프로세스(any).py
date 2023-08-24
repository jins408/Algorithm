from collections import deque
def solution(priorities, location):
    answer = 0

    # (인덱스,priorities원소값) 튜블 형식으로 queue를 만들어줌
    queue = [(i,j) for i,j in enumerate(priorities)]

    while True:
        temp = queue.pop(0) #queue 맨 처음 값을 pop()
        # any for문 중에서 하나라도 조건에 맞다면 True
        if any(temp[1] < i[1] for i in queue):
            # 조건에 해당하면 temp를 queue에 다시 추가(맨뒤로)
            queue.append(temp)
        else:
            # any 조건에 해당하느게 하나도 없다면, answer+=1
            answer+=1
            # 다시 append를 해주지 않기때문에 queue에 원소값이 앞에서부터 하나하나하 빠진다
            # (인덱스,priorities원소값) 튜블형식으로 만들었기 때문에 temp인덱스값과 location일치하면 해당하는 원소의 인덱스 값을 찾을 수 있음
            if temp[0] == location:
                return answer

priorities = [1, 1, 9, 1, 1, 1]
    #[2, 1, 3, 2]
#[1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))
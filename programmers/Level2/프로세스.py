from collections import deque
def solution(priorities, location):
    # 인덱스가 0부터 시작해서 처음부터 answer=1로 해준다(찾고자 하는 값이 리스트 인덱스1부터 시작해서 값을 찾기때문에)
    answer = 1
    temp = deque(priorities)
    print(temp)
    # 찾고자 하는 값을 location으로 잡아준다
    index = location
    # 우선순위를 탐색하기 위해 while문들 돌림
    while len(temp) >= 0:
        num = max(temp)
        # temp에서 첫번째 값을 뽑아
        a = temp.popleft()
        # 우선순위가 제일 큰값보다 작으면 다시 append를 해준다.
        if a < num:
            temp.append(a)
            # index가 처음부터 0인경우도 있기때문에 0일때는 len(temp)-1로 계속 탐색할 수 있게 한다.
            if index == 0:
                index = len(temp)-1
            else:
                # 최고 우선순위보다 작고 index가 0이 아니면 index-1을 해준다.
                index -= 1
        else:
            # index가 0이되면 queue에 더이상 비교해가며 탐색할게 없기 때문에 졸료시킨다.
            if index == 0:
                return answer
            else:
                # answer+1 해주고 index는 -1을 해준다.
                answer += 1
                index -= 1
    return answer

priorities = [1, 1, 9, 1, 1, 1]
    #[2, 1, 3, 2]
#[1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))
def hanoi(n, start,to,mid,answer):
    if n == 1: # 종료기준 올길 원판이 하나만 남았을 때
        return answer.append([start,to])
    hanoi(n-1,start,mid,to,answer) # 옮겨야 할 원판의 크기, 시작지, 경유지, 목적지)
    # 1번 탑에 있는 두개의 원판을 3번 탑을 경유하여 2번탐으로 이동
    answer.append([start, to])
    hanoi(n-1, mid,to,start,answer) # 옮겨야 할 원판의 크기, 경유지, 목적지, 시작지)
    # 2번 탑에 있는 두개의 원판을 1번 탑을 경유하여 3번 탑으로 이동

def solution(n):
    answer = []
    hanoi(n, 1,3,2, answer) #하노이의 탑은 3기둥으로 이루어진 답이라서 첫번째로 원판이 움직이는 것은 1->3->2로 고정
    return answer

n = 3
print(solution(n))
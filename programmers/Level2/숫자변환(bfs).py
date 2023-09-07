from collections import deque

def solution(x, y, n):
    answer = -1

    q = deque()
    q.append((x,0)) # x값과 cnt값을 q에 담아준다.

    visited = set() # 중복값 확인을 위해 set()으로 만들어준다.

    while q:
        num, cnt = q.popleft()

        # num값이 y값과 같아지면 cnt값을 return (num=x)
        if num == y:
            answer = cnt
            break

        if num*3 <= y and not num*3 in visited:     # x*3이 y보다 작거나 같은지 확인하고, visited에 없으면
            visited.add(num*3)                      # visited에 추가해주고, q에도 다시 계산한 값과 cnt +1을 해준다.
            q.append((num*3,cnt+1))
        if num*2 <= y and not num*2 in visited:     # x*2일때 위에와 동일하게 작업 반복
            visited.add(num*2)
            q.append((num*2, cnt+1))
        if num+n <= y and not num+n in visited:     # x+n일때 위에와 동일하게 작업 반복
            visited.add(num+n)
            q.append((num+n, cnt+1))

    return answer
x=10
y=40
n=5
print(solution(x,y,n))
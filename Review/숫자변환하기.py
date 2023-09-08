from collections import deque

def solution(x, y, n):
    answer = -1

    q = deque()
    q.append((x,0))

    visited = set()

    while q:
        num, cnt = q.popleft()

        if num == y:
            answer = cnt
            break

        if num*3 <= y and not num*3 in visited:
            visited.add(num*3)
            q.append((num*3, cnt+1))
        if num*2 <= y and not num*2 in visited:
            visited.add(num*2)
            q.append((num*2, cnt+1))
        if num+n <= y and not num+n in visited:
            visited.add(num+n)
            q.append((num+n, cnt+1))


    return answer

x = 10
y = 40
n = 5
print(solution(x,y,n))
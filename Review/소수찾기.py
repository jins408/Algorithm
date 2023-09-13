def dfs(stack, num, r_num, v):

    if stack:
        r_num.add(int(''.join(stack)))

    for i in range(len(num)):
        if v[i] == 0:
            v[i] = 1
            stack.append(num[i])
            dfs(stack, num, r_num, v)
            stack.pop()
            v[i] = 0

    return list(r_num)

def solution(numbers):
    answer = 0

    visited = [0]*len(numbers)
    numbers = list(map(str, numbers))
    numbers = dfs([],numbers, set(), visited)

    for i in numbers:
        print(i)
        ans = 0
        if i != 1 and i != 0:
            for k in range(1, (i+1)//2+1):
                if i%k == 0:
                    ans+=1
        if ans == 1:
            answer += 1

    return answer

numbers = "011"
print(solution(numbers))
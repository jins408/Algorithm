def dfs(stack, num, r_num, v):

    # stack안에 들어간 값을 set변수은 r_num에 담는다
    # -> stack=['1'] str형태를 제거하고 int형으로 담아준다 r_num = {1}
    if stack:
        r_num.add(int(''.join(stack)))

    for i in range(len(num)):
        # 방문하지 않았다면 않았다면 방문했다고 1로 바꿔주고 stack에 num[i]값을 넣어준다.
        if v[i] == 0:
            v[i] = 1
            stack.append(num[i])
            # dfs 재귀함수를 계속 호출하면 작업을 반복한다.
            dfs(stack,num,r_num, v)
            # i가 0 일때, {1, 17} -> 다시 i가 1일때 {7, 71} 형식으로 봐주기 위해
            # v[i]를 0으로 바꿔주고
            v[i] = 0
            # stack도 pop해서 빈 리스트로 다시 만들어준다.
            stack.pop()

    return list(r_num)

def solution(numbers):

    visited = [0]*len(numbers)  # 방문했는지 안했는지 체크해줄 리스트
    numbers = list(map(str, numbers)) # 문자열을 문자열 리스트로 바꿔줌
    #  [str(i) for i in numbers] -> 시간초과 list(map(str, numbers))로 바꾸니까 시간초과 안남
    numbers = dfs([],numbers,set(),visited) # 재귀를 돌릴 함수(dfs)
                # 빈 stack, number리스트, 중복제거, 방문체크

    answer = 0
    # 소수인지 아닌지 판별하는 과정
    for k in numbers:
        ans = 0
        if k != 1 and k != 0:
            # k가 71인경우 71까지 굳이 봐줄필요 없고 71//2한 값까지만 확인해도 소수인지 아닌지 판별할 수 있다.
            for i in range(1, (k+1)//2+1):
                print(i)
                # 1~자기자신//2까지 나눈 후, 나누어떨어지는 경우가 1 이상인 경우를 소수로 분류
                if k%i == 0:
                    ans += 1
        if ans == 1:
            answer += 1


    return answer

numbers = "17"
print(solution(numbers))
def solution(order):
    answer = 0

    stack = []

    for idx, num in enumerate(order):
        stack.append(idx+1) # stack에 인덱스 값을 넣는다(인덱스는 1부터) -> 택배상자가 1번부터 순서대로 들어가기 때문에

        while stack and stack[-1] == order[answer]: # stack에 뽑은수와 order의 수가 일치하면
            stack.pop() # pop해주고
            answer +=1  # +1을 해준다

    return answer

order = [4, 3, 1, 2, 5]
print(solution(order))
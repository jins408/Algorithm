
def solution(numbers):
    answer = [-1]*len(numbers)

    stack = []

    for i, num in enumerate(numbers):
        # 맨처음에는 stack가 공백이라 무조건 stack에 0(인덱스)가 들어감
        # numbers[0] < num 작다면, -> 뒤에 숫자가 더 큰지 비교한 부분
        while stack and numbers[stack[-1]] < num:
            # num(현재숫자)가 이전숫자보다 크다면 answer에 있는 값을 바꿔줌
            # 이전숫자의 위치를 저장하고 있는 stack에서 인덱스를 뽑아 answer인덱스 위치에 현재 값(num)을 넣어준다.
            answer[stack.pop()] = num
        stack.append(i)

    return answer

numbers = [9, 1, 5, 3, 6, 2]
    #[2, 3, 3, 5]
    #[9, 1, 5, 3, 6, 2]
print(solution(numbers))
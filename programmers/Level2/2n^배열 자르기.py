def solution(n, left, right):
    answer =[]

    # 1차원으로 바꾸면,
    # index	0 (0, 0)	1 (0, 1)	2 (0, 2)	3 (1, 0)	4 (1, 1)	5 (1, 2)	6 (2, 0)	7 (2, 1)	8 (2, 2)
    # value	1	        2	        3	        2	        2	        3	        3	        3	        3
    # 규칙을 보면 각 index의 밸류 값은 max((index // n ), (index % n ))+1
    for i in range(left, right+1):
        answer.append(max(i//n, i%n)+1)

    return answer

n = 3
left = 2
right = 5
print(solution(n, left, right))
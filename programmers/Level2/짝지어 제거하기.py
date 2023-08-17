def solution(s):
    #answer = -1

    word = []
    for i in s:
        word.append(i)
        # 문자가 2개씩 연속으로 있을때만 비교하기 때문에 len(word) >= 2로 조건 걸어줌
        if len(word) >= 2 and word[-2] == word[-1]:
            # 연속된 문자2개씩만 봐주면 되기때문에 for문 2번만 돌림
            for _ in range(2):
                word.pop()

    if word == []:
        return 1
    else:
        return 0

s="cdcd"
print(solution(s))

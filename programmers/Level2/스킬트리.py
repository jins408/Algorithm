def solution(skill, skill_trees):
    answer = 0

    temp = []
    for tree in skill_trees:
        # 빈리스트로 했더니 런타임 에러나서 빈 문자열로 바꿔줌
        str = ""
        for j in tree:
            # skill_trees 원소 중에 skill 문자열과 동일한게 있다면
            if j in skill:
                # 빈문자열에 넣어줌
                str += j
            else:
                continue
        temp.append(str)

    # skill문자열에 해당하는 문자열을 담은 temp 리스트에서
    for i in temp:
        # skill문자열을 temp원소들의 길이만큼 잘라서 동일하다면 -> skill과 순서가 동일하다는 것
        if skill[:len(i)] == i:
            # skill 순서가 동일한것만 체크해주면 된다.
            answer +=1

    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill,skill_trees))
def solution(skill, skill_trees):
    answer = 0

    temp = []
    for tree in skill_trees:
        str = ''
        for i in tree:
            if i in skill:
                str += i
        temp.append(str)

    for i in temp:
        if skill[:len(i)] == i:
            answer+=1

    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))
def solution(cards1, cards2, goal):
    # 배열의 순서를 바꿀 수 없으니까, 순서대로 pop시키는데 만약 goal의 순서와 cards순서에 맞지 않는 단어가 존재하면 바로 No를 return해버림
    # goal는 존재하지 않지만, cards에 존재하는 경우에도 배열의 순서만 다 맞고 goal문자을 다 확인했기 때문에
    # 남아 있는 단어는 확인 할 필요 없이 바로 Yes를 return 해버림
    for g in goal:
        if len(cards1) > 0 and g == cards1[0]:
            cards1.pop(0)
        elif len(cards2) >0 and g == cards2[0]:
            cards2.pop(0)
        else:
            return "No"
    return "Yes"

cards1 =  ["i", "water", "drink"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]
#  ["i", "drink", "water"], ["want", "to", "juice"], ["i", "want", "to", "drink", "water"]
print(solution(cards1, cards2, goal))
def solution(spell, dic):
    answer = 0


    for i in dic:
        num = 0
        for j in spell:
            if j in i:
                num += 1
        if num == len(spell):
            return 1
    return 2


spell=["s", "o", "m", "d"]
dic=["moos", "dzx", "smm", "sunmmo", "som"]
print(solution(spell,dic))
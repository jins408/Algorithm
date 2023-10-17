from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for c in course:
        temp = []
        for order in orders:
            combi = combinations(sorted(order), c)
            temp += combi

        conter = Counter(temp)

        if len(conter) != 0 and max(conter.values()) != 1:
            for key in conter:
                if conter[key] == max(conter.values()):
                    answer.append(''.join(key))

    return sorted(answer)

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
print(solution(orders, course))
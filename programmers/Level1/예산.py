d=[1,3,2,5,4]
budget = 9

def solution(d, budget):
    answer = 0

    d.sort()
    for i in range(len(d)):
        if d[i] <= budget:
            answer += 1
            budget -= d[i]
        else:
            break
    return answer

print(solution(d, budget))
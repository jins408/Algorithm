def solution(i, j, k):
    answer = 0

    for i in range(i, j+1):
        a = str(i)
        for j in a:
            if str(k) in j:
                answer+=1

    return answer

i=1
j=13
k=1
print(solution(i,j,k))
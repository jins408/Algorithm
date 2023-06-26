def solution(lines):
    answer = 0

    start1 = lines[0][0]
    start2 = lines[1][0]
    start3 = lines[2][0]

    end1 = lines[0][1]
    end2 = lines[1][1]
    end3 = lines[2][1]

    sum1 = lines[0][1] - lines[0][0]
    sum2 = lines[1][0]+lines[1][1]
    sum3 = lines[2][0]+lines[2][1]

    if sum2 < sum1 and sum3 < sum1:
        result = (sum2 + sum3) - sum1
        return result

    if end1 > start2 and start1 < start2:
        a = end1 - start2
    else:
        a = 0
    if end2 > start3 and start2 < start3:
        b = end2 - start3
    elif start2 > start3 :
        b = start2 - start3
    else:
        b = 0
    if end3 > start1 and start3 < start1:
        c = end3 - start1
    elif end1 > start3:
        c = end1 - start3
    else:
        c = 0

    answer = a+b+c

    return answer

lines = [[-1, 1], [1, 3], [3, 9]]
    #[[0, 5], [3, 9], [1, 10]] [[0, 1], [2, 5], [3, 9]] [[-1, 1], [1, 3], [3, 9]]
print(solution(lines))
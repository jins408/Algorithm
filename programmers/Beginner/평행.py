
def solution(dots):
    answer = 0

    p1 = (dots[0][0], dots[0][1])
    p2 = (dots[1][0], dots[1][1])
    p3 = (dots[2][0], dots[2][1])
    p4 = (dots[3][0], dots[3][1])

    if (p3[1] - p1[1]) / (p3[0] - p1[0]) == (p4[1] - p2[1]) / (p4[0] - p2[0]):
        return 1
    elif (p4[1] - p3[1]) /(p4[0]-p3[0]) == (p2[1] - p1[1]) // (p2[0] - p1[0]):
        return 1
    else:
        return 0

    #return answer


dots= [[1, 4], [9, 2], [3, 8], [11, 6]]
print(solution(dots))
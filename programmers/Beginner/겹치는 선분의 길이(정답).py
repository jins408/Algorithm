def solution(lines):
    starts = [min(a) for a in lines]
    ends = [max(a) for a in lines]
    starts.sort()
    ends.sort()
    answer = 0
    answer += max(0, ends[0] - starts[1])
    answer += max(0, ends[1] - starts[2])
    answer -= max(0, ends[0] - starts[2])

    '''
    # 가장 작은점, 큰점 구한 범위 내에서 계산
    line_list = []
    for line in lines:
        line_list += line
    mx, mn = max(line_list), min(line_list)

    x, y, z = lines
    overlap_line_count = 0
    for i in range(mn, mx+1):
        overlap_point_count = 0

        if x[0] <= i < x[1]:
            overlap_point_count += 1
        if y[0] <= i < y[1]:
            overlap_point_count += 1
        if z[0] <= i < z[1]:
            overlap_point_count += 1

        if overlap_point_count >= 2:
            overlap_line_count += 1
        #print(f'i x y z overlap_point_count overlap_line_count', i, x, y, z, overlap_point_count, overlap_line_count)

    return overlap_line_count
    '''

    return answer
lines= [[0, 5], [3, 9], [1, 10]]
print(solution(lines))
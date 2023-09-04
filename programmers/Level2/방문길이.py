
def solution(dirs):
    answer = 0

    dic = {"U":(1,0),"D":(-1,0),"R":(0,1),"L":(0,-1)}
    visited = set()

    r,c = 0,0

    for cmd in dirs:
        nr = r+dic[cmd][0]
        nc = c+dic[cmd][1]

        if -5 <= nr <=5 and -5<=nc<=5 :
            # ((기존좌표), (이동좌표))
            go = (r, c, nr, nc)
            # ((이동좌표), (기존좌표))
            back = (nr, nc, r, c)
            if go not in visited:
                visited.add(go)
                visited.add(back)
                answer += 1
            r,c = nr,nc
    return answer

dirs= "ULURRDLLU"
print(solution(dirs))
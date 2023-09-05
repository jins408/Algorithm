def solution(dirs):
    answer = 0

    dic = {"U":(1,0),"D":(-1,0),"R":(0,1),"L":(0,-1)}
    visited = set()

    r, c = 0,0
    for cmd in dirs:
        nr = dic[cmd][0]+r
        nc = dic[cmd][1]+c

        if -5<=nr<=5 and -5<=nc<=5:
            go = (r, c, nr, nc)
            back = (nr, nc, r, c)
            if go not in visited:
                answer += 1
                visited.add(go)
                visited.add(back)
            r,c = nr,nc

    return answer

dirs = "ULURRDLLU"
print(solution(dirs))

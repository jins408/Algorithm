
def solution(dirs):
    answer = 0

    # dirs문자열에 따라 이동할 방향들을 담은 딕셔너리
    dic = {"U":(1,0),"D":(-1,0),"R":(0,1),"L":(0,-1)}
    # set을 이용해 방문여부를 판단
    visited = set()

    # 시작 위치
    r,c = 0,0

    for cmd in dirs:
        nr = r+dic[cmd][0]
        nc = c+dic[cmd][1]

        # 빔위에 넘어가지 않는다면
        if -5 <= nr <=5 and -5<=nc<=5 :
            # ((기존좌표), (이동좌표)) 가는 방향
            go = (r, c, nr, nc) # A -> B
            # ((이동좌표), (기존좌표)) 돌아오는 방향
            back = (nr, nc, r, c) # B -> A
            # A에서 B로 이동할때 set에 (A,B)(B,A) 존재하는지 확인한 다음
            if go not in visited:
                # set에 저장하고
                visited.add(go)
                visited.add(back)
                #answer 값을 1증가 시켜준다
                answer += 1
            # 이동한위치를 현재위치로 바꿔준다
            r,c = nr,nc
    return answer

dirs= "ULURRDLLU"
print(solution(dirs))
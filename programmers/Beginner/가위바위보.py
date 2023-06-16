def solution(rsp):
    answer = ''
    # 가위2 바위0 보5
    game = {'0':'5','5':'2','2':'0'}

    for i in rsp:
        if i in game:
            answer += game[i]

    return answer


rsp = "205"
print(solution(rsp))
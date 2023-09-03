def solution(record):
    answer = []

    result = []
    dic = {}
    for recd in record:
        mesg = recd.split()
        if mesg[0] == "Enter":
            result.append([mesg[1],"님이 들어왔습니다."])
            dic[mesg[1]] = mesg[2]
        elif mesg[0] == "Leave":
            result.append([mesg[1],"님이 나갔습니다."])
        else:
            dic[mesg[1]] = mesg[2]
    print(dic)
    print(result)

    for i in result:
       answer.append(dic[i[0]]+i[1])

    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))
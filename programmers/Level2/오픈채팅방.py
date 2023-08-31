def solution(record):
    answer = []

    result = []
    dic = {}
    for cord in record:
        # 문자열을 공백 기준으로 잘라 ['입장유무','유저아이디','닉네임']으로 나눠준다.
        mesg = cord.split(" ")
        if mesg[0] == "Enter":
            result.append([mesg[1], "님이 들어왔습니다."])
            # dic에 유저아이디:닉네임 형태로 담아준다.
            dic[mesg[1]] = mesg[2]
        elif mesg[0] == "Leave":
            # 채팅방을 나간 경우에는 닉네임이 존재하지 않으므로 딕녀너리(dic)에는 넣어주지 않고 result에만 유저아이디를 넘어줌
            # -> 닉네임에 따라 어떤 상태인지 알기위해서 result에는 넣어줘야함
            result.append([mesg[1],"님이 나갔습니다."])
        else:
            # "Change" -> 닉네임 변경이므로 해당 유저아이디에 대한 value값을 변경해준다.
            dic[mesg[1]] = mesg[2]
    print(result)
    print(dic)

    for i in result:
        # result에서 dic의 key값과 같으면 그 해당하는 value값으로 넣어준다.
        answer.append(dic[i[0]]+i[1])

    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))
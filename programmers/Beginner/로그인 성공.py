def solution(id_pw, db):
    answer = ''

    answer = "fail"
    for i in range(len(db)):
        # 아이디, 비밀번호 모두 일치
        if db[i][0] == id_pw[0] and db[i][1] == id_pw[1]:
            answer = "login"
            # 아이디 일치하는 회원 없는 경우
        elif db[i][0] == id_pw[0] and db[i][1] != id_pw[1]:
            answer = "wrong pw"



    return answer

id_pw = ["programmer01", "15789"]
    #["meosseugi", "1234"]
db = [["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]
print(solution(id_pw, db))
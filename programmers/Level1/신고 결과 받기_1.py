def solution(id_list,reports , k):
    answer = []

    id = {}  # {'muzi': [], 'frodo': [], 'apeach': [], 'neo': []}
    # 신고한 유저와 신고받은 유저를 넣어줄 딕셔너리
    id_ = {} # {'muzi': 0, 'frodo': 0, 'apeach': 0, 'neo': 0}
    # 신고당한 유저의 횟수를 저장할 딕셔너리
    for i in id_list:
        id[i] = []
        id_[i] = 0

    for report in set(reports): #한유저가 동인한 유저를 계속 신고해도 신고횟수는 한번으로 보기때문에 set으로 중복제거
        id_[report.split()[1]] += 1 # 신고당한 횟수를 저장(한유저가 동인한 유저를 연속으로 신고해도 횟수는 1로 저장)
        id[report.split()[0]].append(report.split()[1]) # 신고당한유저와 신고받은 유저를 넣어줌
    print(id)
    print(id_)

    # id 딕셔너리의 key 값을 통해 id_의 신고횟수를 k만큼 비교에서 cnt(카운트)헤줌
    for key in id:
        cnt = 0
        for value in id[key]:
            if id_[value] >= k:
                cnt += 1
        answer.append(cnt)
    return answer

id_list = ["con", "ryan"]
        #["con", "ryan"]
        #["muzi", "frodo", "apeach", "neo"]
reports = ["ryan con", "ryan con", "ryan con", "ryan con"]
    #["ryan con", "ryan con", "ryan con", "ryan con"]
    #["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

print(solution(id_list, reports, k))
'''
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
'''

id_list = ["con", "ryan"]
reports = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3


def solution(id_list, report, k):
    answer = [0] * len(id_list)
    # [0,0,0,0]

    # 딕셔너리 생성(딕서셔너리 컴프리헨션)  id_list의 리스트를 입력받아 value가 빈 딕셔너리 생성
    # {'muzi': [], 'frodo': [], 'apeach': [], 'neo': []}
    dic_report = {id: [] for id in id_list}
    stop = []
    cnt = 0

    # set 요소들 간에는 순서가 없어서 인덱싱을 사용할 수 없음 for 돌려서 모든 값들은 얻을 수 있지만 순서대로 진행한다는 보장이 없음
    for i in set(report):
        report_value = i.split(' ')
        stop.append(report_value[1]) # 신고당한 사람들의 리스트 stop=['muzi', 'frodo', 'neo', 'frodo', 'neo']
        # dic_report에 신고한사람을 key로보고 신고받은 사람을 value에 넣어주기
        # dic_report = {'muzi': ['frodo', 'neo'], 'frodo': ['neo'], 'apeach': ['muzi', 'frodo'], 'neo': []}
        dic_report[report_value[0]].append(report_value[1])
    print(dic_report)
    stop = set([i for i in stop if stop.count(i) >= k])
    print(stop)
    # 신고받은 사람들 중 k번 이상 받은 사람들을 stop = {i} set 형태로 중복제거해서 다시 stop에 넣어줌 stop = {'frodo', 'neo'}

    # dic_report.items() key-value 쌍을 리스트 형태로 반환
    # [{'muzi': ['frodo', 'neo'], 'frodo': ['neo'], 'apeach': ['muzi', 'frodo'], 'neo': []}]
    for key, value in dic_report.items():
        for s in stop:  # s= 'frodo' , 'neo'
            if s in value: # value에 stop이 가지고 있는 값을 가지고 있다면
                answer[id_list.index(key)] += 1 # id_list에 index를 사용해서 id_list.index(muzi) 찾아서 1을 더해준다.
                # 신고한 사람에게 신고처리한 결과를 메일로 보내줘야 함으로(신고당한 유저별로 각각 보내줘야해서 횟수를 +1로 해서 카운트)
    return answer

print(solution(id_list, reports, k))
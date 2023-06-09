id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

def solution(id_list, reports, k):
    dic_report = {id: [] for id in id_list}
    answer = [0] * len(id_list)
    # dic_report = {'muzi': [], 'frodo': [], 'apeach': [], 'neo': []} 신고를 받은 사람
    for report in set(reports):
        report = report.split(' ')
        print(report)
        # report를 공백으로 구분하면, 첫번째에는 신고 한 사람, 두번째 인덱스에는 신고 받는 사람
        # 신고 받은 사람의 value에 신고 한 사람을 넣는다. -> apeach가 frodo를 신고했으니까 frodo에 apeach를 넣어 줌
        # dic_report = {'muzi': ['apeach'], 'frodo': ['apeach', 'muzi'], 'apeach': [], 'neo': ['muzi', 'frodo']}
        dic_report[report[1]].append(report[0])

    # dic_report.items() key-value 쌍을 리스트 형태로 반환
    # dic_report = [{'muzi': ['apeach'], 'frodo': ['apeach', 'muzi'], 'apeach': [], 'neo': ['muzi', 'frodo']}]
    for key, value in dic_report.items():
        # value 길이를 보면 몇번 신고당한지 알 수 있ㄴ
        if len(value) >= k:
            # 신고 당한 횟수 보다 크거나 같으면
            for v in value:
                # id_list에 index를 사용해서 id_list.index(apeach) 찾아서 1을 더해준다.
                answer[id_list.index(v)] += 1
                # 신고한 사람에게 신고처리한 결과를 메일로 보내줘야 함으로
                # apeach가 frodo를 신고했으니까 apeach에 +1 muzi가 frodo를 신고했으니까 muzi에 +1ㄴ
    return answer

print(solution(id_list, report, k))
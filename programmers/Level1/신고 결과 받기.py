id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

'''
def solution(id_list, reports, k):
    stop = []
    answer = [0] * len(id_list)
    dicReports = {id: [] for id in id_list}
    for i in set(reports):
        report = i.split(' ')
        stop.append(report[1])
        dicReports[report[0]].append(report[1])

    stop = set([i for i in stop if stop.count(i) >= k])

    for key, value in dicReports.items():
        for s in stop:
            if s in value:
                answer[id_list.index(key)] += 1
    return answer
'''
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    # [0,0,0,0]

    # 딕셔너리 생성(딕서셔너리 컴프리헨션)  id_list의 리스트를 입력받아 value가 빈 딕셔너리 생성
    # {'muzi': [], 'frodo': [], 'apeach': [], 'neo': []}
    dic_report = {id: [] for id in id_list}
    stop = []
    cnt = 0

    for i in set(report):
        ss = i.split(' ')
        print(ss)
        stop.append(ss[1])
        print(stop)
        dic_report[ss[0]].append(ss[1])
    print(dic_report)
    return answer

print(solution(id_list, report, k))
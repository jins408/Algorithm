import math
def solution(fees, records):
    answer = []

    #기본시간, 기본요금, 단위시간, 단위요금
    dt, df, ut, uf = fees

    # 자동차번호를 key값으로 시간과 입/출차 여부를 딕셔너리에 담음
    dic = {}
    for record in records:
        times, id, type = record.split(" ")
        hh,mm = times.split(':')
        # 시간을 분으로 바꿔서 더해준다.
        minutes = int(hh)*60 + int(mm)

        if id in dic :
            dic[id].append([minutes, type]) # dic에 존재 하다면 해당하는 key값에 value를 추가 해준다.
        else:
            dic[id] = [[minutes, type]] # dic 없다면 key,value로 새로 넣어준다

    print(dic)

    dic_sort = sorted(dic.items()) # dic를 차번호를 오름차순으로 정렬해준다.
    print(dic_sort)

    for sdic in dic_sort:
        t = 0
        for i in sdic[1]:
            if i[1] == 'IN':
                t -= i[0]
            else:
                t += i[0]

        # 입차 이후 출차된 내역이 없다라는 것은 각 입/출차 내역의 마지막 내역이 입차(IN)로 끝나는 것이기 때문에,
        # 이 경우 누적 주차 시간 계산할 때 "23:59"를 분으로 환산한 만큼 더해주어 계산
        if sdic[1][-1][1] == "IN":
            t += (23*60)+59

        if t <= dt:
            answer.append(df)
        else:
            # 올림해주다는 조건이 있어서 ceil로 올림을 해줌
            answer.append(df + math.ceil((t-dt)/ut)*uf)

    return answer


fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN",
           "06:34 0000 OUT", "07:59 5961 OUT",
           "07:59 0148 IN", "18:59 0000 IN",
           "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees,records))

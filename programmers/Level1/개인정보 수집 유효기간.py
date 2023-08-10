def solution(today, terms, privacies):
    answer = []

    term_list = {}
    for i in range(len(terms)):
        term = terms[i]
        a = term[0:1]
        b = term[2:4]
        term_list[a] = b
    print(term_list)
    data = []
    for privacie in privacies:
        privacie = list(map(str, privacie.split(' ')))
        date_ = ''
        if privacie[1] in term_list:
            date = privacie[0]
            #print(date)
            month = int(date[5:7])+int(term_list[privacie[1]])
            #print(month)
            year = int(date[0:4])
            #print(year)
            day = int(date[8:11])
            day_ = day-1
            if day_ == 0:
                month -= 1
                day_ = 28
            #    print(day_)
            #print(day_)
            #달 = 계산된 달 % 12
            #연도 = 기존연도 + 계산된 달 // 12
            month_ = month%12
            #print(month_)
            year = year+(month//12)
            #print(year)
            date_ += str(year)+str(month_)+str(day_)
            data.append(date_)
    print(data)
    today = today.replace('.','')
    print(today)
    y = today[0:4]
    m = today[4:6]
    d = today[6:8]
    for i in range(len(data)):
        a = data[i]
        print(a[0:4], a[4:6], a[6:8])
        if a[0:4] <= y and a[4:6] <= m and a[6:8]<=d:
            answer.append(i+1)


    return answer

today = "2022.05.19"
    #"2022.05.19"
terms = ["A 6", "B 12", "C 3"]
    #["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
    #["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
    #["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
print(solution(today, terms, privacies))
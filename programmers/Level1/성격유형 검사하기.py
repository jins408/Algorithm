def solution(survey, choices):
    answer = ''

    # 유형에 따라 점수를 부여할 딕셔너리
    type = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    # choices 점수에 따라 type.value 값에 점수를 더해주기 위한 딕셔너리
    score = {1:3, 2:2, 3:1, 4:0, 5:1, 6:2, 7:3}
    # 1(매우비동의)3점, 2(비동의)2점, 3(약갼비동의)1점, 4(모르겠음)0점, 5(약간동의)1점, 6(동의)2점, 7(매우동의)3점

    for i in range(len(survey)):
        # 1,2,3 점수가 낮을때는 "AN"로 주어졌을때 앞에 단어인 A
        if choices[i] in (1,2,3):
            for s_key, s_value in score.items():
                if choices[i] == s_key:
                    a = survey[i]
                    # 앞에 단어 하나만 뽑아주기 위해
                    b = a[:1]
                    print(b)
                    # type딕셔너리랑 비교해서 value값에 해당하는 점수를 더해줌
                    for t_key, t_value in type.items():
                        if b == t_key:
                            type[t_key] += s_value
        # 5,6,7 점수가 높을때는 "AN"로 주어졌을때 뒤에 단어인 N
        elif choices[i] in (5,6,7):
            for s_key, s_value in score.items():
                if choices[i] == s_key:
                    a = survey[i]
                    # 뒤에 단어 하나만 뽑아주기 위해
                    b = a[1:]
                    print(b)
                    # type딕셔너리랑 비교해서 value값에 해당하는 점수를 더해줌
                    for t_key, t_value in type.items():
                        if b == t_key:
                            type[t_key] += s_value
    print(type)

    # type 딕셔너리에서 유형별로 2개씩 비교에서 더 점수를 가진 유형을 answer에 넣어줌
    a = [] # 2개유형 별로 비교하기 위한 빈 배열
    for i, item in enumerate(type.items()):
        # i=0, i=1 일때 a비열에 넣어줌 예시(a=['R': 0, 'T': 3])
        if i or i+1:
            a.append(item[0])
            a.append(item[1])
        # 길이가 4일때
        if len(a) >= 4:
            # 점수를 비교해서 더 크값을 answer에 넣어줌
            if a[1] < a[3]:
                answer += a[2]
                # 다시 비교해주기 위해 a를 초기화
                a = []
            else:
                answer += a[0]
                a = []

    return answer


survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
print(solution(survey,choices))
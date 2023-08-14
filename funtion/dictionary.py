name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]

# 공백으로 나눠진 문자열 딕셔너리로 만들기
terms =["Z 3", "D 5"]
dic = dict()
for term in terms:
    k, v = term.split()
    dic[k] = int(v)
print(dic)


# 빈 딕셔너리에 key, value 추가
dic_name = {}
for i in range(len(name)):
    dic_name[i] = name[i]
print(dic_name)

dic_year = {}
for j in range(len(yearning)):
    dic_year[j] = yearning[j]
print(dic_year)

# for문 이용해서 key, value 값 넣는 방법
dic = dict([(dic_name.get(key), value) for key, value in dic_year.items()])
print(dic)
# zip 함수를 이용해서 딕녀너리에 key,value 값 동시에 넣는 방법
score_dict = {}
for a,b in zip(name,yearning): # 이름:스코어 딕셔너리
    score_dict[a] = b
print(score_dict)

# key, vlaue 값 이용해서 값 찾는 방법
for k in score_dict.items():
    print(k)
    print(k[0], k[1])
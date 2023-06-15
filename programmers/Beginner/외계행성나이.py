def solution(age):
    answer = ''
    str_age = str(age)
    age_eng = {'0':'a','1':'b','2':'c','3':'d','4':'e','5':'f','6':'g','7':'h','8':'i','9':'j'}
    #{'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9}
    #{0:'a',1:'b',2:'d',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j'}


    for i in range(len(str_age)):
        for j in age_eng:
            if str_age[i] == j:
                answer += age_eng[j]


    return answer


age = 29
print(solution(age))
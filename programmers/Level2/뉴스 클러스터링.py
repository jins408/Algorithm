import math
def solution(str1, str2):
    answer = 0

    a = []
    for i in range(len(str1)-1):
        s = str1[i]+str1[i+1]
        if s.isalpha():
            a.append(s.upper())
    print(a)
    b = []
    for i in range(len(str2)-1):
        x = str2[i]+str2[i+1]
        if x.isalpha():
            b.append(x.upper())
    print(b)

    # 교집합
    aa = []
    for a_ in a:
        if a_ in b:
            aa.append(a_)
            # s1 = [a,a,a,b,b] s2 = [a,a,b,b,b] 일때 'a'를 교집합에 추가 한 후 s2에서 'a'를 삭제를 안시켜줬기 때문에,
            # s1의 세번째 a에서도 in 연산자가 true가 나와 교집합에 추가되기 때문입니다.
            b.remove(a_)
            # 교집합에 추가 해준 후에는 s2의 원소에서 삭제시켜주는 작업을 해야합니다.
    print(aa)
    #합집합
    union = a+b
    print(union)

    result1 = len(aa)
    result2 = len(union)
    print(result1)
    print(result2)

    if aa ==[] and union == []:
        answer = 1*65536
    else:
        answer = math.floor((result1/result2)*65536)

    return answer

str1= "aa1+aa2"
    #"abab"
    #"handshake"
    #"aa1+aa2"
    #"FRANCE"
str2= "AAAA12"
    #"baba"
    #"shake hands"
    #"AAAA12"
    #"french"
print(solution(str1, str2))
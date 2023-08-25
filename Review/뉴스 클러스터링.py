import math
def solution(str1, str2):
    answer = 0

    a = []
    for i in range(len(str1) - 1):
        s = str1[i] + str1[i + 1]
        if s.isalpha():
            a.append(s.upper())

    b = []
    for i in range(len(str2) - 1):
        x = str2[i] + str2[i + 1]
        if x.isalpha():
            b.append(x.upper())

    #교집합
    aa = []
    for a_ in a:
        if a_ in b:
            aa.append(a_)
            b.remove(a_)
    print(aa)
    print(b)

    # 합집함
    union = a+b

    result1 = len(aa)
    result2 = len(union)
    print(result1)
    print(result2)
    answer = math.floor((result1/result2)*65536)

    return answer

str1 = "FRANCE"
str2 = "french"
print(solution(str1, str2))
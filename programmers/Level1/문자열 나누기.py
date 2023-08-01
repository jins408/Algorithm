def solution(s):
    answer = 0

    cnt = 0
    sum = 0
    a = ''
    first = s[cnt+sum]
    for i in s:
        if i == first:
            cnt += 1
        else:
            sum += 1
        if cnt == sum:
            a += s[:cnt+sum]+","
            first = s[cnt + sum]
            cnt = 0
            sum = 0

    #print(a)
    a = a.split(',')
    a = a[:-1]
    #print(a)
    answer = len(a)

    return answer
s= "banana"
    #"abracadabra"
    #"aaabbaccccabba"
print(solution(s))
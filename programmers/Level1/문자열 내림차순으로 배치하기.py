def solution(s):
    answer = ''

    alphabet = 'zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA'

    index = -1
    for i in range(len(alphabet)):
        if alphabet[i] in s:
            cnt = s.count(alphabet[i])
            if i > index:
                index = i
                answer += alphabet[i]
            if cnt > 1:
                for j in range(cnt-1):
                    answer += alphabet[i]
            

    '''
    a = list(s)
    a.sort(reverse=True)

    answer = ''.join(a)
    '''

    return answer


s= "Zbcdefg"
print(solution(s))
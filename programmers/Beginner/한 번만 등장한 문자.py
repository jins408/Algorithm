def solution(s):
    answer = ''

    alphabet = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,
                'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}

    for i in s:
        if i in alphabet.keys():
            alphabet[i] += 1

    for i in alphabet:
        if alphabet[i] == 1:
            answer += i


    return answer


s="hello"
print(solution(s))

arr =[1,2,3,4]
a = arr.index(arr[-1])
print(a)
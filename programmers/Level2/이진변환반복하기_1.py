def fun(a):
    temp = ''
    while True:
        b = a % 2
        a //= 2
        temp += str(b)
        if a == 0:
            break
    return temp[::-1]

def solution(s):
    cnt = 0  # 반복횟수
    zero = 0 # 0제거개수

    while True:
        cnt += 1
        num = ''
        for i in s:
            if i == '1':
                num += '1'
        a = len(num)
        zero += len(s) - a
        # 이진법으로 변환
        get_fun = fun(a)
        s = get_fun
        if s == '1':
            break

    return [cnt, zero]

s = "110010101001"
    #"01110"
    #"1111111" [4,1]
print(solution(s))
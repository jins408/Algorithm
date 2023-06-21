def solution(cipher, code):
    answer = ''

    num = 1
    i = num * code
    while i <= len(cipher):
        answer += cipher[i-1]
        num += 1
        i = num * code

    return answer


cipher = "abc"
code = 2

print(solution(cipher,code))

